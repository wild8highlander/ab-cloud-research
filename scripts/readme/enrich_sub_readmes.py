#!/usr/bin/env python3
"""Enrich all nested (sub) READMEs of AB-Cloud Research (Tier 2, ~445 files).
Idempotent via AB-ENRICHED marker. Adds:
  - prepend: thin capsule-render venice strip (category gradient) + nav line
  - append:  animated category divider + (unified footer if none present)
Excludes root README and the 16 section READMEs (Tier 1, already enriched).
"""
import os

import os as _os
REPO = _os.environ.get("REPO_ROOT", ".")
MARKER = "AB-ENRICHED:v1"

CAT = {
 "verification": ("00e5ff", "cyan"), "formal": ("a78bfa", "violet"),
 "monographs": ("ffd60a", "gold"), "AB_Cloud_Quantum_Research": ("ff2ec4", "magenta"),
 "AB_Cloud_Academic_Package": ("ffd60a", "gold"), "Hilbert_Polya": ("a78bfa", "violet"),
 "dirac-lab": ("00e5ff", "cyan"), "lab-3d": ("ff2ec4", "magenta"),
 "Wave_attractors": ("00e5ff", "cyan"), "Vortex_optimization": ("ff2ec4", "magenta"),
 "meridian-spectral-observatory": ("a78bfa", "violet"), "results": ("22c55e", "green"),
 "code": ("9558B2", "purple"), "apps": ("4FC3F7", "blue"), "docs": ("526CFE", "blue"),
 "assets": ("8B949E", "gray"),
}
SECTION_KEYS = set(CAT)

def find_parent_readme(rel_dir):
    """Nearest ancestor dir (walking up to repo root) containing README.md.
    Returns repo-relative path to that README and its depth."""
    parts = rel_dir.split("/") if rel_dir else []
    while parts:
        cand_dir = "/".join(parts)
        cand = os.path.join(REPO, cand_dir, "README.md")
        if os.path.isfile(cand):
            return cand_dir + "/README.md", len(parts)
        parts.pop()
    return "README.md", 0

def nav_label(rel_parent):
    d = os.path.dirname(rel_parent)
    if not d:
        return "Root README"
    return d.split("/")[-1] + "/"

def enrich(path):
    rel = os.path.relpath(path, REPO).replace(os.sep, "/")
    rel_dir = os.path.dirname(rel)
    depth = len(rel_dir.split("/")) if rel_dir else 0
    top = rel_dir.split("/")[0] if rel_dir else ""
    color, divider = CAT.get(top, ("00e5ff", "cyan"))
    src = open(path, encoding="utf-8").read()
    is_section_readme = (depth == 1 and top in SECTION_KEYS
                         and os.path.basename(path).lower() == "readme.md")
    if MARKER in src or rel == "README.md" or is_section_readme:
        return None

    parent_rel, parent_depth = find_parent_readme(rel_dir)
    # parent must be strictly above this file's own README
    if rel == parent_rel:
        parent_rel, parent_depth = find_parent_readme("/".join(rel_dir.split("/")[:-1]))
    up_root = "../" * depth + "README.md"
    up_parent = os.path.relpath(parent_rel, rel_dir).replace(os.sep, "/") if rel_dir else parent_rel
    ap = "../" * depth + "assets"

    cap = (f'<img src="https://capsule-render.vercel.app/api?type=venice&height=48'
           f'&color=0:{color},100:05060f&section=header" alt="" width="100%"/>')
    head = (f"<!-- {MARKER} · sub -->\n<div align=\"center\">\n\n{cap}\n\n"
            f"**🧭 [⬆ {nav_label(parent_rel)}]({up_parent}) · [🏠 Root README]({up_root})**\n\n</div>\n")

    has_partof = "Part of the" in src or "Part of [" in src
    tail_rows = [f'<img src="{ap}/svg/divider-{divider}.svg" alt="—" width="100%" height="12"/>', ""]
    if has_partof:
        tail = ("<div align=\"center\">\n\n" + "\n".join(tail_rows) + "</div>\n")
    else:
        tail = ("<div align=\"center\">\n\n" + "\n".join(tail_rows) +
                f"<sub>⚡ Part of <a href=\"{up_root}\">AB-Cloud Research</a> — numbers are verbatim from the "
                f"unified registry; no result on this page is a claim about the Riemann hypothesis · "
                f"<a href=\"{up_parent}\">⬆ parent section</a></sub>\n\n</div>\n")

    new = head + src.rstrip() + "\n\n" + tail
    open(path, "w", encoding="utf-8").write(new)
    return rel

def main():
    done, skipped = [], 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            lf = f.lower()
            if not lf.startswith("readme") or not lf.endswith(".md"):
                continue
            # skip provenance / template artifacts
            if any(t in lf for t in ("_source", "_original", "_template", "_documents")):
                continue
            p = os.path.join(root, f)
            # skip tiny pointer stubs ("see README.md" language notes)
            if os.path.getsize(p) < 400:
                continue
            r = enrich(p)
            if r:
                done.append(r)
            else:
                skipped += 1
    print(f"Enriched {len(done)} sub-READMEs, skipped {skipped} (sections/root/already-done)")
    top_counts = {}
    for r in done:
        k = r.split("/")[0]
        top_counts[k] = top_counts.get(k, 0) + 1
    for k, v in sorted(top_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
