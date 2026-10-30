#!/usr/bin/env python3
"""
prepare-test-explorer-data.py — freeze the per-test verification reports of
the repository into the JSON the dashboard "Test explorer" and the
"Hilbert–Pólya audit" tabs fetch.

Sources (all already committed — no numerics re-run, pure text parsing):
  results/Test 1-37 ab_cloud_full.jl/run_20260902_134759/test_*/report.md
      → apps/ab-cloud-dashboard/public/data/test_reports.json   (37 panels)
  results/Test H1-H8 hp_audit_standalone.jl/run_*/final_report.md
      → apps/ab-cloud-dashboard/public/data/hp_audit.json       (8 panels)

What is extracted per suite test (T1–T37):
  • id, slug, title, verdict, generated date, category
  • description ("What this test verifies") + reproduce command
  • the Result line
  • key metrics parsed from the "calc: name = value (...)" computation log
  • numeric tables from the console capture (header + rows, max 3 tables,
    max 60 rows each) — rendered in the explorer as data tables and charts
  • sub-check lines (H0..H7 hardcore sub-checks)
  • a trimmed console excerpt (first 64 non-empty lines)

What is extracted per audit test (H1–H8):
  • title, verdict, battery verdict, parameters block, the result line,
    the sub-check table (sub-check / status / detail), and the method notes.

Requires: python3 (stdlib only). Run once after a new suite run; the
generated JSON is committed and ships with the site.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "results" / "Test 1-37 ab_cloud_full.jl" / "run_20260902_134759"
HP_DIR = ROOT / "results" / "Test H1-H8 hp_audit_standalone.jl"
DST = ROOT / "apps" / "ab-cloud-dashboard" / "public" / "data"

MAX_TABLES = 3
MAX_ROWS = 60
MAX_EXCERPT = 64
MAX_DETAIL = 500  # max chars of one sub-check detail cell
MAX_CALC = 80     # cap calc metric entries per test (test 11 has 3000+)
MAX_CHECKS = 14   # cap verdict-keyword console lines per test

# category assignment (id → [category, one-line focus]) — mirrors the
# grouping of the suite's own FINAL_REPORT and docs/monographs.md
CATEGORIES = {
    1: ("b(N) convergence", "Gram-point approximation b(N) = (1/N)Σ|γ−γ̃|"),
    2: ("b(N) convergence", "monotonicity of the b(N) descent"),
    3: ("b(N) convergence", "power-law fit of the convergence rate"),
    4: ("Spacing statistics", "KS test vs the GUE ratio law, full range"),
    5: ("Spacing statistics", "KS test vs GUE, high-height subranges"),
    6: ("Spacing statistics", "χ² goodness-of-fit of the spacing histogram"),
    7: ("Regression stability", "log–log regression slope of the decay"),
    8: ("Regression stability", "residual analysis of the fit"),
    9: ("Regression stability", "bootstrap CI for the slope"),
    10: ("Regression stability", "cross-validation of the fit stability"),
    11: ("Goodness-of-fit", "Anderson–Darling tail-sensitive test"),
    12: ("Goodness-of-fit", "two-sample KS: real zeros vs GUE matrix"),
    13: ("Long-range RMT", "number variance Σ²(L) vs Poisson/GUE"),
    14: ("Long-range RMT", "spectral rigidity Δ₃(L) audit"),
    15: ("AB construction & topology", "Hermiticity, TRB flux, Dirac string of the Hamiltonian"),
    16: ("AB construction & topology", "⟨r⟩ bulk statistics vs GUE classification"),
    17: ("AB construction & topology", "Connes self-duality α ↔ 1/α"),
    18: ("AB construction & topology", "chiral symmetry class AIII at α = 1/2"),
    19: ("AB construction & topology", "Dirac cone 1/L scaling, v_F"),
    20: ("AB construction & topology", "TKNN Chern number C₁ = 1 (gapped anchors)"),
    21: ("Quantum geometry", "spinorial phase arg(γ*) ≈ π/2"),
    22: ("Quantum geometry", "AB phase Φ_AB = π/7 = δ_C"),
    23: ("Quantum geometry", "complex fractal factor CF"),
    24: ("Quantum geometry", "Dirac string flux verification"),
    25: ("Quantum geometry", "Byers–Yang theorem check"),
    26: ("Quantum geometry", "PBC torus Dirac string"),
    27: ("Quantum geometry", "binary chiral symmetry at α = 1/2"),
    28: ("Cross-comparisons", "f_GUE figure of merit"),
    29: ("Scaling & non-Hermitian", "Dirac dip in the DOS at α = 1/2"),
    30: ("Scaling & non-Hermitian", "Dirac cone v_F scaling vs L"),
    31: ("Scaling & non-Hermitian", "Hatano–Nelson non-Hermitian skin"),
    32: ("Cross-comparisons", "multi-realization ⟨r⟩ bootstrap"),
    33: ("Cross-comparisons", "L-scaling of ⟨r⟩ (10→112) and plateau"),
    34: ("Cross-comparisons", "DIRECT AB-cloud vs ζ on the full loaded set"),
    35: ("Cross-comparisons", "spectral form factor K(t) vs GUE"),
    36: ("Robustness & normalization", "byte-level robustness of ⟨r⟩"),
    37: ("Robustness & normalization", "(1/2)! via Γ and GUE normalization"),
}

CATEGORY_ORDER = [
    "b(N) convergence",
    "Spacing statistics",
    "Regression stability",
    "Goodness-of-fit",
    "Long-range RMT",
    "AB construction & topology",
    "Quantum geometry",
    "Scaling & non-Hermitian",
    "Cross-comparisons",
    "Robustness & normalization",
]

NUM_RE = re.compile(r"^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
SKIP_TOKENS = {"---", "--", "—", "-", "…", "..."}


def to_num(tok):
    """'1.2126' → float; '---'/'—'/other → None (kept as null)."""
    t = tok.strip().rstrip(",")
    if t in SKIP_TOKENS:
        return None
    if NUM_RE.match(t):
        v = float(t)
        if v != v or v in (float("inf"), float("-inf")):
            return None
        return int(v) if "." not in t and "e" not in t.lower() else v
    return None


def clean(x):
    if isinstance(x, float):
        if x != x or x in (float("inf"), float("-inf")):
            return None
        return round(x, 8)
    return x


def is_num_row(line):
    toks = line.split()
    if len(toks) < 2:
        return False
    return all(NUM_RE.match(t.strip().rstrip(",")) or t.strip() in SKIP_TOKENS for t in toks)


CALC_PARAM_RE = re.compile(
    r"calc:\s*([^\n=(]+?)\((\w+)\s*[=<>]\s*([\d.]+)\)\s*=\s*([+-]?[\d.]+(?:[eE][+-]?\d+)?)\s*(\([^)\n]*\))?")
CALC_PLAIN_RE = re.compile(
    r"calc:\s*([^\n=(]+?)\s*=\s*([+-]?[\d.]+(?:[eE][+-]?\d+)?)\s*(\([^)\n]*\))?")


def parse_calc_lines(log_text):
    """calc: ⟨r⟩ = 0.572908 (n_r=5527 ...) → ({name, value, note} list,
    series list).  A name carrying a parameter — Σ²(L=2.000), Δ₃(L=23.331) —
    additionally feeds a series of (x, y) points grouped by metric family,
    which the explorer renders as a chart."""
    out = []
    fam = {}
    taken = []  # spans consumed by the parameterized form
    for m in CALC_PARAM_RE.finditer(log_text):
        base, xname, xs, val = m.group(1).strip(), m.group(2), float(m.group(3)), float(m.group(4))
        taken.append((m.start(), m.end()))
        out.append({"name": f"{base}({xname}={xs:g})", "value": clean(val),
                    "note": (m.group(5) or "").strip()})
        f = fam.setdefault(base, {"x": xname, "pts": []})
        f["pts"].append((xs, clean(val)))
    for m in CALC_PLAIN_RE.finditer(log_text):
        if any(s <= m.start() < e for s, e in taken):
            continue
        try:
            val = float(m.group(2))
        except ValueError:
            continue
        out.append({"name": m.group(1).strip(), "value": clean(val),
                    "note": (m.group(3) or "").strip()})
    series = []
    for base, s in fam.items():
        pts = s["pts"]
        if len(pts) >= 3:
            series.append({"name": base, "x": s["x"],
                           "points": sorted(pts, key=lambda p: p[0])})
    return out, series


def extract_checks(console_text):
    """Console lines carrying a verdict keyword — the per-bench check
    headlines ("Float64 round-off    PASS — |Δa|=1.2e-19 ...")."""
    out, seen = [], set()
    for line in console_text.split("\n"):
        t = line.strip()
        if len(t) < 12 or len(t) > 300:
            continue
        if not re.search(r"\b(PASS|WARN|FAIL)\b", t):
            continue
        if t.startswith(("═", "─", "```", "|", "#")):
            continue
        key = t[:80]
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
        if len(out) >= MAX_CHECKS:
            break
    return out


def extract_tables(console_text):
    """Find blocks of >=3 consecutive all-numeric whitespace-separated rows.
    A directly preceding non-numeric line with the same token count is the
    header; any other preceding text line becomes the table title."""
    lines = console_text.split("\n")
    tables = []
    i, n = 0, len(lines)
    while i < n and len(tables) < MAX_TABLES:
        if is_num_row(lines[i]):
            j = i
            block = []
            while j < n and is_num_row(lines[j]):
                block.append(lines[j].split())
                j += 1
            if len(block) >= 3:
                header, title = None, None
                k = i - 1
                while k >= 0 and not lines[k].strip():
                    k -= 1
                if k >= 0 and not is_num_row(lines[k]):
                    prev = lines[k].split()
                    if len(prev) == len(block[0]):
                        header = prev
                    elif len(prev) > len(block[0]) >= 2:
                        # multi-word last column ("Δ vs prev") — first cols map
                        # 1:1, all remaining tokens merge into the last name
                        ncols = len(block[0])
                        header = prev[:ncols - 1] + [" ".join(prev[ncols - 1:])]
                    else:
                        title = lines[k].strip()[:120]
                rows = [[clean(to_num(t)) for t in r] for r in block[:MAX_ROWS]]
                tables.append({
                    "title": title or "",
                    "header": header or [],
                    "rows": rows,
                    "n_rows_total": len(block),
                })
            i = j
        else:
            i += 1
    return tables


def extract_subchecks(console_text):
    """Hardcore sub-check lines: ' H0 reproduce : ...' → [{tag, label, text}]"""
    out = []
    for m in re.finditer(r"^\s*(H\d+)\s+([a-zA-Z_'\- ]{2,24}?)\s*:\s+(.+)$", console_text, re.M):
        text = m.group(3).strip()
        if len(text) < 8 or len(text) > 1200:
            continue
        out.append({"tag": m.group(1), "label": m.group(2).strip(), "text": text})
    return out[:16]


def parse_suite_report(md_path, tid, slug):
    md = md_path.read_text(encoding="utf-8", errors="replace")
    first = md.split("\n", 1)[0].lstrip("# ").strip()
    vm = re.search(r"Verdict:\s*(PASS|WARN|FAIL|DONE)", md)
    dm = re.search(r"Generated:\s*([0-9\-]+ [0-9:]+)", md)
    desc_m = re.search(r"## What this test verifies\n(.*?)\n\n## ", md, re.S)
    res_m = re.search(r"## Result\n\s*(.+)", md)
    log_m = re.search(r"## FULL COMPUTATION LOG\n+```text\n(.*?)```", md, re.S)
    con_m = re.search(r"## CONSOLE CAPTURE\n+```text\n(.*?)```", md, re.S)
    rep_m = re.search(r"Reproduce with:\s*(.+)", md)

    desc, method = "", ""
    if desc_m:
        block = [l.strip() for l in desc_m.group(1).strip().split("\n") if l.strip()]
        if block:
            desc = block[0]
        for l in block:
            if l.startswith("METHOD:"):
                method = l[len("METHOD:"):].strip()
                break

    console = con_m.group(1) if con_m else ""
    calcs_all, series = parse_calc_lines(log_m.group(1)) if log_m else ([], [])
    calcs = calcs_all[:MAX_CALC]
    tables = extract_tables(console)
    subs = extract_subchecks(console)
    checks = extract_checks(console)
    bench_m = re.search(r"^\s*TEST\s+\d+[^\n]*", console, re.M)
    excerpt = [l.rstrip() for l in console.split("\n") if l.strip()][:MAX_EXCERPT]

    verdict = vm.group(1) if vm else "DONE"
    cat, focus = CATEGORIES.get(tid, ("Other", ""))
    return {
        "id": tid,
        "slug": slug,
        "title": first,
        "short": first.split(":", 1)[1].strip() if ":" in first else first,
        "verdict": verdict,
        "generated": dm.group(1) if dm else "",
        "category": cat,
        "focus": focus,
        "description": desc,
        "method": method,
        "result": res_m.group(1).strip() if res_m else "",
        "reproduce": rep_m.group(1).strip() if rep_m else "",
        "bench": bench_m.group(0).strip()[:140] if bench_m else "",
        "calc": calcs,
        "n_calc_total": len(calcs_all),
        "series": series,
        "tables": tables,
        "subchecks": subs,
        "checks": checks,
        "excerpt": excerpt,
        "report_path": f"results/Test 1-37 ab_cloud_full.jl/run_20260902_134759/{md_path.parent.name}/report.md",
    }


# ── Hilbert–Pólya audit (H1–H8) ───────────────────────────────────────────

def strip_md(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"_(.+?)_", r"\1", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    return t


def parse_hp_sections(md):
    """Parse '## H<n>. Title — **VERDICT**' sections of a battery report."""
    sections = []
    pat = re.compile(r"^## (H\d+)\.\s+(.+?)\s+—\s+\*\*(PASS|WARN|FAIL)\*\*\s*$", re.M)
    matches = list(pat.finditer(md))
    for idx, m in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md)
        body = md[m.end():end]
        subs = []
        for row in re.finditer(r"^\|\s*([^|\n]+?)\s*\|\s*(PASS|WARN|FAIL)\s*\|\s*(.+?)\s*\|\s*$", body, re.M):
            detail = strip_md(row.group(3).strip())
            subs.append({"check": row.group(1).strip(), "status": row.group(2),
                         "detail": detail[:MAX_DETAIL]})
        res = ""
        rm = re.search(r"^>\s*(Test\s+H\d+:\s*.+)$", body, re.M)
        if rm:
            res = rm.group(1).strip()
        notes = []
        for pm in re.finditer(r"^(?!\s*>)(?!\s*\|)(?!\s*```)(?!#)(?!\!\[).{40,}$", body, re.M):
            t = pm.group(0).strip()
            if t.startswith(("![", "```", "---", "[")):
                continue
            notes.append(strip_md(t))
        sections.append({
            "id": m.group(1),
            "title": m.group(2).strip(),
            "verdict": m.group(3),
            "result": res,
            "subchecks": subs,
            "notes": notes[:4],
        })
    return sections


def parse_hp_battery(dir_path):
    md = (dir_path / "final_report.md").read_text(encoding="utf-8", errors="replace")
    battery = ""
    bm = re.search(r"\*\*Battery verdict:\*\*\s*(.+)", md)
    if bm:
        battery = bm.group(1).strip()
    pm = re.search(r"## Parameters\n+```text\n(.*?)```", md, re.S)
    params = pm.group(1).strip() if pm else ""
    run = dir_path.name.split()[0]
    zm = re.search(r"ζ zeros loaded:\s*\*\*(\w+)\*\*", md)
    return {
        "run": run,
        "battery": battery,
        "params": params,
        "zeros_loaded": zm.group(1) if zm else "?",
        "sections": parse_hp_sections(md),
    }


def main():
    if not RUN_DIR.is_dir():
        sys.exit(f"missing {RUN_DIR} — clone the full repository first")
    DST.mkdir(parents=True, exist_ok=True)

    tests = []
    for d in sorted(RUN_DIR.glob("test_*")):
        md = d / "report.md"
        if not md.is_file():
            continue
        parts = d.name.split("_", 2)
        tests.append(parse_suite_report(md, int(parts[1]), parts[2]))
    tests.sort(key=lambda t: t["id"])

    cats = []
    for c in CATEGORY_ORDER:
        members = [t["id"] for t in tests if t["category"] == c]
        if members:
            cats.append({"name": c, "ids": members})

    n_tables = sum(len(t["tables"]) for t in tests)
    n_calcs = sum(t["n_calc_total"] for t in tests)
    n_subs = sum(len(t["subchecks"]) for t in tests)
    n_checks = sum(len(t["checks"]) for t in tests)
    n_series = sum(len(t["series"]) for t in tests)
    with open(DST / "test_reports.json", "w", encoding="utf-8") as f:
        json.dump({
            "_meta": {
                "what": "Per-test deep-dive panels parsed from the frozen suite reports "
                        "(results/Test 1-37 ab_cloud_full.jl/run_20260902_134759)",
                "run": "run_20260902_134759",
                "generated_by": "scripts/prepare-test-explorer-data.py",
                "n_tests": len(tests),
                "n_tables": n_tables,
                "n_calc_metrics": n_calcs,
                "n_subchecks": n_subs,
                "n_checks": n_checks,
                "n_series": n_series,
            },
            "categories": cats,
            "tests": tests,
        }, f, ensure_ascii=False, indent=1)

    # H battery: each final_report.md re-runs the earlier tests, so parse
    # every run and keep the FIRST occurrence of each H-section
    chosen = {}
    for r in sorted(HP_DIR.glob("run_*")):
        if not (r / "final_report.md").is_file():
            continue
        bat = parse_hp_battery(r)
        for s in bat["sections"]:
            chosen.setdefault(s["id"], {"battery": bat, "section": s})
    hp_tests = []
    for hid in sorted(chosen, key=lambda x: int(x[1:])):
        ch = chosen[hid]
        sec = dict(ch["section"])
        sec["run"] = ch["battery"]["run"]
        sec["params"] = ch["battery"]["params"]
        sec["zeros_loaded"] = ch["battery"]["zeros_loaded"]
        sec["report_path"] = f"results/Test H1-H8 hp_audit_standalone.jl/{ch['battery']['run']}*/final_report.md"
        hp_tests.append(sec)
    with open(DST / "hp_audit.json", "w", encoding="utf-8") as f:
        json.dump({
            "_meta": {
                "what": "Hilbert–Pólya deep audit H1–H8, parsed from the frozen battery reports "
                        "(results/Test H1-H8 hp_audit_standalone.jl)",
                "generated_by": "scripts/prepare-test-explorer-data.py",
                "n_tests": len(hp_tests),
            },
            "tests": hp_tests,
        }, f, ensure_ascii=False, indent=1)

    print(f"test_reports.json: {len(tests)} tests, {n_tables} tables, {n_calcs} calc metrics, "
          f"{n_series} series, {n_subs} sub-checks, {n_checks} check lines")
    print(f"hp_audit.json: {len(hp_tests)} audit tests:",
          ", ".join(f"{t['id']}({len(t['subchecks'])} checks)" for t in hp_tests))


if __name__ == "__main__":
    main()
