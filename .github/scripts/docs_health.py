#!/usr/bin/env python3
"""docs_health.py — repository documentation & sync health gate.

Three subcommands, all stdlib-only, all CI-friendly (GitHub annotations):

  links    every relative link/image target in every tracked .md file must
           resolve to a real file (URL-decoded, anchors checked against the
           target file's headings);
  readmes  every directory that carries documentation/code/data must contain
           a README.md;
  sync     the Academic Package's byte-copies must not drift from the canon
           (Julia suite, HP audit, formal layer, D-variants, frozen zeros)
           and the verdict layer must agree with the research registry.

Exit code 1 iff at least one ERROR is reported (warnings don't fail CI).
"""
import hashlib
import json
import os
import re
import sys
import urllib.parse

ROOT = os.environ.get("AB_CLOUD_ROOT", os.path.join(os.path.dirname(__file__), "..", ".."))
ROOT = os.path.abspath(ROOT)
PKG = os.path.join(ROOT, "projects", "academic-package")

SKIP_DIRS = {".git", "node_modules", ".ruff_cache", "__pycache__", ".venv", "site", ".github"}

errors: list[str] = []
warnings: list[str] = []


def err(path: str, line: int, msg: str) -> None:
    errors.append(f"{path}:{line}: {msg}")
    print(f"::error file={path},line={line}::{msg}")


def warn(path: str, line: int, msg: str) -> None:
    warnings.append(f"{path}:{line}: {msg}")
    print(f"::warning file={path},line={line}::{msg}")


def load_allowlist(name: str) -> dict:
    p = os.path.join(ROOT, ".github", name)
    if not os.path.exists(p):
        return {}
    return json.load(open(p, encoding="utf-8"))


ALLOW = {}  # filled in main() once


def target_allowed(target: str) -> bool:
    return any(re.fullmatch(pat, target) for pat in ALLOW.get("skip_targets", []))


# ────────────────────────────── links ──────────────────────────────
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_RE = re.compile(r"\!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.M)


def github_slug(h: str) -> str:
    """Approximate github-slugger: lowercase, strip non-word chars (keep
    unicode letters/digits and hyphens), spaces -> hyphens. Compared loosely
    (alphanumeric-only projection) so emoji/slugger edge cases never produce
    false positives — see _slug_matches."""
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h, flags=re.UNICODE)
    return h.replace(" ", "-")


def _slug_matches(anchor: str, headings: set[str]) -> bool:
    """Loose comparison: ignore everything outside [a-z0-9] on both sides.
    Catches genuinely broken anchors while tolerating emoji-slug quirks."""
    def norm(s: str) -> str:
        return re.sub(r"[^a-z0-9]", "", s.lower())
    a = norm(urllib.parse.unquote(anchor))
    if not a:
        return True
    return any(norm(h) == a for h in headings)


def anchors_of(path: str) -> set[str]:
    out = set()
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return out
    for m in HEADING_RE.finditer(text):
        out.add(github_slug(m.group(1)))
    for m in re.finditer(r'<a\s[^>]*?id="([^"]+)"', text):
        out.add(m.group(1))
    return out


def cmd_links() -> int:
    allow = load_allowlist("docs-health-allowlist.json")
    checked = skipped_files = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for fn in sorted(filenames):
            if not fn.lower().endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            if any(re.fullmatch(pat, rel) for pat in allow):
                skipped_files += 1
                continue
            try:
                text = open(full, encoding="utf-8", errors="replace").read()
            except OSError as e:
                err(rel, 0, f"unreadable markdown: {e}")
                continue
            for m in LINK_RE.finditer(text):
                checked += 1
                _check_target(rel, full, m.group(1))
            for m in IMG_RE.finditer(text):
                checked += 1
                _check_target(rel, full, m.group(1))
    print(f"links: checked {checked} targets, {len(errors)} broken, {skipped_files} files skipped via allowlist")
    return 1 if errors else 0


def _check_target(rel: str, full: str, target: str) -> None:
    if target.startswith(("http://", "https://", "mailto:", "data:")):
        return
    if target_allowed(target):
        return
    path_part, _, anchor = target.partition("#")
    if not path_part:
        if anchor and not _slug_matches(anchor, anchors_of(full)):
            err(rel, 0, f"broken anchor #{anchor}")
        return
    decoded = urllib.parse.unquote(path_part)
    if decoded.startswith("/"):
        return  # site-absolute (Pages) — the external-link job's domain
    cand = os.path.normpath(os.path.join(os.path.dirname(full), decoded))
    if not os.path.exists(cand):
        err(rel, 0, f"broken link target: {target}")
        return
    if anchor and os.path.isfile(cand):
        if not _slug_matches(anchor, anchors_of(cand)):
            err(rel, 0, f"missing anchor #{anchor} in {path_part}")


# ────────────────────────────── readmes ──────────────────────────────
DOC_KINDS = (".md", ".py", ".jl", ".rs", ".go", ".js", ".java", ".c", ".cc", ".cpp",
             ".h", ".hpp", ".f90", ".v", ".lean", ".thy", ".agda", ".r", ".R",
             ".csv", ".tsv", ".json", ".yaml", ".yml", ".toml", ".txt", ".tex")
README_EXEMPT = ("node_modules",)
# Pure content containers / generated outputs documented by their parent README.
EXEMPT_BASENAMES = {
    "src", "logs", "log", "data", "docs", "latex", "static", "figures",
    "figures_hires", "assets", "palettes", "themes", "i18n", "pwa", "api",
    "completions", "hooks", "plugins", "scripts", "shared", "curves",
    "test_reports", "computation_logs", "FINAL_REPORT", "ABCloud",
    "fonts", "img", "images", "charts", "output", "outputs", "build", "dist",
}


def _exempt(rel_norm: str) -> bool:
    parts = rel_norm.split("/")
    if parts[0] == "results":          # auto-generated run artifacts
        return True
    base = parts[-1]
    if base in EXEMPT_BASENAMES:
        return True
    if base.startswith(("run_", "test_")) and any(ch.isdigit() for ch in base):
        return True
    return False


def cmd_readmes() -> int:
    allow = load_allowlist("docs-health-allowlist.json")
    missing = scanned = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and d not in README_EXEMPT)
        if rel_dir == ".":
            continue
        scanned += 1
        if "README.md" in filenames or "readme.md" in filenames:
            continue
        if not any(fn.lower().endswith(DOC_KINDS) for fn in filenames):
            continue
        rel_norm = rel_dir.replace(os.sep, "/")
        if _exempt(rel_norm) or any(re.fullmatch(pat, rel_norm) for pat in allow):
            continue
        missing += 1
        err(rel_norm + "/", 0, "directory carries docs/code/data but has no README.md")
    print(f"readmes: scanned {scanned} directories, {missing} missing README")
    return 1 if errors else 0


# ─────────────────────────────── sync ───────────────────────────────
SYNC_PAIRS = [
    ("code/ab_cloud_full.jl", "projects/academic-package/06_code/lab_standalone/ab_cloud_full.jl"),
    ("code/hp_audit_standalone.jl", "projects/academic-package/06_code/lab_standalone/hp_audit_standalone.jl"),
    ("code/RH_Unified_D.jl", "projects/academic-package/06_code/meridian/RH_Unified_D.jl"),
    ("code/RH_Sweep_Pro_D.jl", "projects/academic-package/06_code/meridian/RH_Sweep_Pro_D.jl"),
    ("verification/zeros1.txt", "projects/academic-package/02_data/frozen/zeros/zeros1.txt"),
    ("verification/zeros50k.txt", "projects/academic-package/02_data/frozen/zeros/zeros50k.txt"),
    ("verification/zeta_zeros_13661.txt", "projects/academic-package/02_data/frozen/zeros/zeta_zeros_13661.txt"),
    ("verification/zeta_zeros_highT_blocks.txt", "projects/academic-package/02_data/frozen/zeros/zeta_zeros_highT_blocks.txt"),
]


def _md5(p: str) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_sync() -> int:
    drift = 0
    for canon, copy in SYNC_PAIRS:
        c1, c2 = os.path.join(ROOT, canon), os.path.join(ROOT, copy)
        if not os.path.exists(c1) or not os.path.exists(c2):
            err(canon, 0, "sync pair incomplete: one side missing")
            drift += 1
            continue
        if _md5(c1) != _md5(c2):
            err(copy, 0, f"package copy drifted from canon {canon} — re-copy the canonical file")
            drift += 1
    print(f"sync: {len(SYNC_PAIRS)} byte-copy pairs, {drift} drifted")

    f_root, f_pkg = os.path.join(ROOT, "formal"), os.path.join(PKG, "06_code", "formal")
    n_mismatch = 0
    for dirpath, dirnames, filenames in os.walk(f_root):
        rel = os.path.relpath(dirpath, f_root)
        for fn in sorted(filenames):
            if fn.endswith((".png", ".svg", ".pdf", ".md")):
                continue  # binaries carry no drift signal; READMEs are context-adapted
            a = os.path.join(dirpath, fn)
            b = os.path.join(f_pkg, rel, fn)
            if not os.path.exists(b) or _md5(a) != _md5(b):
                n_mismatch += 1
                err(f"formal/{os.path.join(rel, fn)}".replace("./", ""), 0,
                    "formal layer file missing or drifted in the package's 06_code/formal mirror")
    print(f"sync: formal/ mirror, {n_mismatch} drifted/missing")

    reg = json.load(open(os.path.join(PKG, "02_data/processed/research_registry.json"), encoding="utf-8"))
    reg_ids = [v["id"] for v in reg["verdicts"]]
    v_bad = 0
    lab = open(os.path.join(PKG, "07_web_lab/index.html"), encoding="utf-8").read()
    i = lab.find("const DATA =")
    k = lab.find("{", i)
    depth = 0
    end = None
    for idx in range(k, len(lab)):
        ch = lab[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = idx + 1
                break
    data = json.loads(lab[k:end])
    lab_ids = [v["id"] for v in data["verdicts"]]
    if lab_ids != reg_ids:
        err("projects/academic-package/07_web_lab/index.html",
            0, f"web-lab verdicts {lab_ids} != registry {reg_ids}")
        v_bad += 1
    readme = open(os.path.join(PKG, "EDITION.md"), encoding="utf-8").read()
    for gid in reg_ids:
        if gid != "RH" and not re.search(rf"^\| {re.escape(gid)}\b", readme, re.M):
            err("projects/academic-package/EDITION.md",
                0, f"verdict {gid} missing from the package README ledger table")
            v_bad += 1
    print(f"sync: verdict layer, {v_bad} inconsistencies (registry: {len(reg_ids)} verdicts)")
    return 1 if errors else 0


def main() -> int:
    global ALLOW
    ALLOW = load_allowlist("docs-health-allowlist.json")
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    rc = 0
    if cmd in ("links", "all"):
        rc |= cmd_links()
    if cmd in ("readmes", "all"):
        rc |= cmd_readmes()
    if cmd in ("sync", "all"):
        rc |= cmd_sync()
    print(f"docs-health[{cmd}]: {len(errors)} errors, {len(warnings)} warnings")
    return rc


if __name__ == "__main__":
    sys.exit(main())
