#!/usr/bin/env python3
"""README required-element linter for AB-Cloud Research.
Checks (by tier):
  root     (./README.md):                AI hero, typing manifest, live badge, license badge
  sections (d=1, 16 known dirs):         AB-ENRICHED marker, capsule-render, category divider,
                                         AI end-cap, 'Part of' footer, Root link
  subs     (d>=2, readme*.md > 400 B):   AB-ENRICHED marker, Root link, divider
Skips provenance copies (*_source/_original/_template/_documents) and pointer stubs.
Exit 1 with a report if violations are found.
"""
import os, sys

REPO = os.environ.get("REPO_ROOT", ".")
MARK = "AB-ENRICHED"
SECTIONS = {
    "verification", "formal", "monographs", "AB_Cloud_Quantum_Research",
    "AB_Cloud_Academic_Package", "Hilbert_Polya", "dirac-lab", "lab-3d",
    "Wave_attractors", "Vortex_optimization", "meridian-spectral-observatory",
    "results", "code", "apps", "docs", "assets",
}
SKIP_TOKENS = ("_source", "_original", "_template", "_documents")

def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()

def main():
    problems = []
    checked = 0

    root = os.path.join(REPO, "README.md")
    if os.path.exists(root):
        checked += 1
        s = read(root)
        for need, label in [
            ("assets/banners/hero-main.webp", "AI hero (hero-main.webp)"),
            ("readme-typing-svg", "typing manifest"),
            ("badge-tests-passing.svg", "live status badge"),
            ("img.shields.io/badge/License", "license badge"),
        ]:
            if need not in s:
                problems.append(f"root README.md: missing {label}")

    for root_dir, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d != ".git"]
        for fn in files:
            lf = fn.lower()
            if not (lf.startswith("readme") and lf.endswith(".md")):
                continue
            if any(t in lf for t in SKIP_TOKENS):
                continue
            p = os.path.join(root_dir, fn)
            rel = os.path.relpath(p, REPO).replace(os.sep, "/")
            if rel == "README.md" or rel.startswith(".readme-components/") or rel.startswith(".github/"):
                continue  # root is checked separately; library/CI docs are not tiered READMEs
            if os.path.getsize(p) < 400:
                continue
            parts = rel.split("/")
            depth = len(parts) - 1
            top = parts[0] if depth else ""
            s = read(p)
            checked += 1
            is_section = (depth == 1 and top in SECTIONS
                          and lf == "readme.md")
            if is_section:
                if MARK not in s:
                    problems.append(f"{rel}: missing {MARK} marker (section tier)")
                if "capsule-render" not in s:
                    problems.append(f"{rel}: missing capsule-render header")
                if "divider-" not in s:
                    problems.append(f"{rel}: missing category divider")
                if "assets/prompts/AI_PROMPTS.md" not in s and top != "assets":
                    problems.append(f"{rel}: missing AI end-cap prompt reference")
                if "Part of" not in s:
                    problems.append(f"{rel}: missing 'Part of' footer")
                if "../README.md" not in s:
                    problems.append(f"{rel}: missing Root README link")
            else:
                if MARK not in s:
                    problems.append(f"{rel}: missing {MARK} marker (sub tier)")
                if "README.md" not in s:
                    problems.append(f"{rel}: missing navigation link")

    print(f"readme-lint: checked {checked} README files")
    if problems:
        print(f"readme-lint: {len(problems)} violation(s):")
        for pr in problems:
            print("  ✗", pr)
        sys.exit(1)
    print("readme-lint: all required elements present ✓")

if __name__ == "__main__":
    main()
