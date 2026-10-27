#!/usr/bin/env python3
"""Enrich the 16 top-level section READMEs (Tier 1) for AB-Cloud Research.
Idempotent: skips files already marked with AB-ENRICHED.
Adds:
  1. Thin capsule-render waving header (category gradient) + typing-SVG tagline
     + optional progress bar (all inside one centered block, prepended)
  2. <details> mermaid "connections" diagram
  3. Appends: animated category divider + AI end-cap banner (4:1, prompt ref)
     + unified footer
Existing content is preserved verbatim.
"""
import os, re, sys

import os as _os
REPO = _os.environ.get("REPO_ROOT", ".")
MARKER = "AB-ENRICHED:v1"

# per-section config ----------------------------------------------------------
S = {
 "verification": dict(color="00e5ff", divider="cyan", prompt="P-02",
   title="VERIFICATION SUITE",
   typing=["Ten+languages+%C2%B7+one+number+each", "Same+frozen+%CE%B6-data+%C2%B7+same+verdicts", "Cross-language+agreement+%7E1e-12"],
   progress="progress-verification",
   out="10 independent ports — identical headline numbers",
   sib="code · formal"),
 "formal": dict(color="a78bfa", divider="violet", prompt="P-03",
   title="FORMAL VERIFICATION",
   typing=["Lean+4+%C2%B7+Coq+%C2%B7+Agda+%C2%B7+Isabelle", "Zero+external+dependencies", "8%2F8+PASS+vs+frozen+references"],
   progress="progress-formal",
   out="machine-checked theorems + executable re-derivation",
   sib="verification · code"),
 "monographs": dict(color="ffd60a", divider="gold", prompt="P-04",
   title="MONOGRAPHS",
   typing=["Five+editions+%C2%B7+RU+%C2%B7+EN+%C2%B7+ZH", "57+plates+%40+600+dpi", "Every+number+traceable+to+the+suite"],
   progress="progress-monographs",
   out="trilingual scholarly apparatus (pdf · tex · docx · html · pptx)",
   sib="results · verification"),
 "projects/quantum-research": dict(color="ff2ec4", divider="magenta", prompt="P-05",
   title="QUANTUM RESEARCH PACK",
   typing=["The+packaged+program", "Live+laboratories+%C2%B7+visual+campaigns", "One+click+from+data+to+figure"],
   progress=None,
   out="packaged experiments, animations and campaign data",
   sib="lab-3d · dirac-lab"),
 "projects/academic-package": dict(color="ffd60a", divider="gold", prompt="P-10",
   title="ACADEMIC PACKAGE",
   typing=["FAIR-aligned+academic+bundle", "Data+%C2%B7+figures+%C2%B7+reports+%C2%B7+code", "Zenodo-ready+packaging"],
   progress=None,
   out="FAIR academic bundle (meta/data/figures/reports/code)",
   sib="monographs · results"),
 "projects/hilbert-polya": dict(color="a78bfa", divider="violet", prompt="P-06",
   title="HILBERT–PÓLYA BRIDGE",
   typing=["Spectral+staircase+to+the+zeros", "Campaigns+C1%E2%80%93C10", "Every+step+reproducible"],
   progress=None,
   out="computation campaigns bridging spectra and ζ",
   sib="verification · formal"),
 "dirac-lab": dict(color="00e5ff", divider="cyan", prompt="P-07",
   title="DIRAC LABORATORY",
   typing=["Zitterbewegung+on+a+Dirac+cone", "Relativistic+Landau+ladder", "Berry+phase+%3D+%CF%80"],
   progress=None,
   out="Dirac-dynamics test benches D01–Dxx",
   sib="lab-3d · verification"),
 "lab-3d": dict(color="ff2ec4", divider="magenta", prompt="P-08",
   title="3D LATTICE LABORATORY",
   typing=["36%C2%B3+Hofstadter+lattice", "WebGL+in+the+browser", "Zero+installation"],
   progress=None,
   out="interactive WebGL lattice lab + prebuilt bundles",
   sib="apps · projects/quantum-research"),
 "projects/wave-attractors": dict(color="00e5ff", divider="cyan", prompt="P-13",
   title="HYPERBOLIC WAVE ATTRACTORS",
   typing=["Rays+cascade+onto+closed+routes", "Chiral+attractor+twins", "Group-velocity+cone+geometry"],
   progress=None,
   out="attractor campaigns and ray-tracing figures",
   sib="projects/vortex-optimization · projects/hilbert-polya"),
 "projects/vortex-optimization": dict(color="ff2ec4", divider="magenta", prompt="P-14",
   title="VORTEX OPTIMIZATION",
   typing=["Convergence+ladder+D%3D0.1096+%E2%86%92+0.0220", "GUE+floor+by+lattice+size", "Vortex+density+as+control+knob"],
   progress=None,
   out="convergence ladders to the GUE floor",
   sib="projects/hilbert-polya · results"),
 "projects/meridian-observatory": dict(color="a78bfa", divider="violet", prompt="P-15",
   title="MERIDIAN SPECTRAL OBSERVATORY",
   typing=["Critical+line+observatory", "GUE+density+in+view", "Compass+set+to+Re%28s%29%3D%C2%BD"],
   progress=None,
   out="observatory docs, banners and spectral views",
   sib="projects/hilbert-polya · monographs"),
 "results": dict(color="22c55e", divider="green", prompt="P-09",
   title="RESULTS — RUN ARTIFACTS",
   typing=["Reference+run+artifacts", "453+files+%C2%B7+39+directories", "Nothing+hand-typed"],
   progress="progress-tests",
   out="frozen logs, reports and per-test artifacts",
   sib="verification · code"),
 "code": dict(color="9558B2", divider="purple", prompt="P-11",
   title="CODE — CANONICAL JULIA SUITE",
   typing=["Julia+v23+%C2%B7+39+tests", "Two-pass+flagship+design", "Exit-code+gated+tolerances"],
   progress="progress-tests",
   out="the canonical suite + Test-38 ports",
   sib="verification · results"),
 "apps": dict(color="4FC3F7", divider="blue", prompt="P-12",
   title="APPS — INTERACTIVE REACT TOOLS",
   typing=["Verdict+dashboard", "WebGL+3D+lattice+lab", "Static+bundles+%C2%B7+Pages-ready"],
   progress=None,
   out="two React applications with prebuilt dist/",
   sib="lab-3d · docs"),
 "docs": dict(color="526CFE", divider="blue", prompt="P-16",
   title="DOCUMENTATION SITE",
   typing=["MkDocs+Material+site", "MathJax+everywhere", "Deployed+to+GitHub+Pages"],
   progress=None,
   out="the deployed documentation site",
   sib="apps · monographs"),
 "assets": dict(color="8B949E", divider="gray", prompt=None,
   title="ASSETS — PROJECT BRANDING",
   typing=["Banners+%C2%B7+icons+%C2%B7+SVG", "One+palette+to+rule+them+all"],
   progress=None,
   out="branding, banners, icons and SVG components",
   sib="docs · .readme-components"),
}

def rel_root(depth):           # depth = number of dirs below repo root
    return "../" * depth + "README.md"

def build_header(key, cfg, depth):
    enc = cfg["title"].replace(" ", "%20").replace("–", "%E2%80%93").replace("—", "%E2%80%94")
    cap = (f'<img src="https://capsule-render.vercel.app/api?type=waving&height=90'
           f'&color=0:05060f,50:{cfg["color"]},100:05060f&section=header'
           f'&text={enc}&fontSize=26&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" '
           f'alt="{cfg["title"]}" width="100%"/>')
    lines = "&".join(f"lines={cfg['typing'][0]}" for _ in ())  # placeholder
    typed = ";".join(cfg["typing"])
    typ = (f'<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono'
           f'&weight=500&size=15&duration=2800&pause=1100&color={cfg["color"]}'
           f'&center=true&vCenter=true&width=760&lines={typed}" '
           f'alt="Typing: section tagline"/>')
    parts = [f"<!-- {MARKER} · section={key} -->", "<div align=\"center\">", "", cap, "", typ]
    if cfg["progress"]:
        parts += ["", f'<img src="{"../"*depth}assets/svg/{cfg["progress"]}.svg" '
                      f'alt="{cfg["progress"]}" width="420"/>']
    parts += ["", "</div>"]
    return "\n".join(parts)

def build_mermaid(key, cfg, title_friendly):
    return (f"<details>\n<summary><strong>🗺️ How <code>{key}/</code> connects to the repository (click)</strong></summary>\n\n"
            "```mermaid\nflowchart LR\n"
            f'    ROOT["🏠 Root README"] --> SEC["{title_friendly}"]\n'
            '    DATA["🧊 Frozen data<br/>verification/data/"] -.-> SEC\n'
            f'    SEC --> OUT["{cfg["out"]}"]\n'
            f'    SEC <-.-> SIB["{cfg["sib"]}"]\n'
            "```\n\n</details>\n")

def build_footer(key, cfg, depth):
    ap = "../" * depth + "assets"
    root = rel_root(depth)
    rows = ["<div align=\"center\">",
            f'<img src="{ap}/svg/divider-{cfg["divider"]}.svg" alt="—" width="100%" height="14"/>', ""]
    if cfg["prompt"]:
        rows += [
            f'<!-- AI end-cap — prompt {cfg["prompt"]}, registry: assets/prompts/AI_PROMPTS.md -->',
            f'<img src="{ap}/banners/banner-{key}.webp" alt="AI-rendered section art (prompt {cfg["prompt"]})" width="100%"/>',
            "",
            f'<sub>🖼️ Section art: <a href="{ap}/prompts/AI_PROMPTS.md">{cfg["prompt"]}</a> · '
            f'palette <code>#05060f · #00e5ff · #ff2ec4 · #a78bfa · #ffd60a</code></sub>', ""]
    rows += [
        f'<sub>⚡ Part of <a href="{root}">AB-Cloud Research</a> — phase resonator for the zeros '
        f'of the Riemann zeta function · <a href="{root}">🏠 Root README</a></sub>',
        "</div>", ""]
    return "\n".join(rows)

FRIENDLY = {
 "verification": "Verification Suite (10 languages)", "formal": "Formal Layer (4 assistants)",
 "monographs": "Monographs (5 editions)", "projects/quantum-research": "Quantum Research Pack",
 "projects/academic-package": "Academic Package", "projects/hilbert-polya": "Hilbert–Pólya Bridge",
 "dirac-lab": "Dirac Laboratory", "lab-3d": "3D Lattice Lab",
 "projects/wave-attractors": "Wave Attractors", "projects/vortex-optimization": "Vortex Optimization",
 "projects/meridian-observatory": "Meridian Observatory", "results": "Results & Artifacts",
 "code": "Canonical Julia Suite", "apps": "Interactive Apps", "docs": "Documentation Site",
 "assets": "Assets & Branding",
}

def main():
    changed = []
    for key, cfg in S.items():
        path = os.path.join(REPO, key, "README.md")
        if not os.path.exists(path):
            print(f"[missing] {key}/README.md"); continue
        src = open(path, encoding="utf-8").read()
        if MARKER in src:
            print(f"[skip] {key} (already enriched)"); continue
        depth = 1  # all section READMEs sit one level below root
        header = build_header(key, cfg, depth)
        mermaid = build_mermaid(key, cfg, FRIENDLY[key])
        footer = build_footer(key, cfg, depth)
        # strip trailing whitespace/newlines for a clean join
        body = src.rstrip() + "\n"
        new = header + "\n" + mermaid + "\n" + body + "\n" + footer
        open(path, "w", encoding="utf-8").write(new)
        changed.append(key)
        print(f"[ok] {key}/README.md  (+{len(new)-len(src)} B)")
    print(f"\nEnriched {len(changed)} section READMEs")

if __name__ == "__main__":
    main()
