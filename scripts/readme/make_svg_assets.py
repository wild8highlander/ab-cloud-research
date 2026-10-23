#!/usr/bin/env python3
"""Generate animated SVG assets for AB-Cloud Research READMEs.
Outputs -> <repo>/assets/svg/
All animations are SMIL (work inside <img> on GitHub).
No inline SVG in markdown (lint MD033 forbids <svg>) — files are referenced via <img>.
"""
import os

REPO = os.environ.get("REPO_ROOT", ".")
OUT = os.path.join(REPO, "assets", "svg")
os.makedirs(OUT, exist_ok=True)

BG = "#05060f"
FG = "#e5e7eb"
CYAN = "#00e5ff"
MAGENTA = "#ff2ec4"
VIOLET = "#a78bfa"
GOLD = "#ffd60a"
GREEN = "#22c55e"
PURPLE = "#9558B2"
BLUE = "#4FC3F7"
GRAY = "#8B949E"

MONO = "ui-monospace,'Cascadia Mono','JetBrains Mono',Menlo,Consolas,monospace"

HEADER = ('<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
          'viewBox="0 0 {w} {h}" role="img" aria-label="{label}">\n')

def divider(color_a, color_b, name):
    """Animated gradient dashed divider line."""
    svg = HEADER.format(w=600, h=14, label=f"divider {name}") + f'''  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BG}"/>
      <stop offset="0.18" stop-color="{color_a}"/>
      <stop offset="0.5" stop-color="{color_b}"/>
      <stop offset="0.82" stop-color="{color_a}"/>
      <stop offset="1" stop-color="{BG}"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{color_b}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{color_b}" stop-opacity="0.55"/>
      <stop offset="1" stop-color="{color_b}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="7" x2="600" y2="7" stroke="url(#g)" stroke-width="2"
        stroke-dasharray="10 7" stroke-linecap="round">
    <animate attributeName="stroke-dashoffset" from="0" to="34" dur="1.6s" repeatCount="indefinite"/>
  </line>
  <line x1="0" y1="7" x2="600" y2="7" stroke="url(#glow)" stroke-width="6" stroke-opacity="0.35">
    <animate attributeName="stroke-opacity" values="0.15;0.4;0.15" dur="2.8s" repeatCount="indefinite"/>
  </line>
</svg>
'''
    with open(os.path.join(OUT, f"divider-{name}.svg"), "w") as f:
        f.write(svg)

def badge_passing():
    """Pulsing 'ALL 39 TESTS PASSING' badge with glowing green dot."""
    svg = HEADER.format(w=210, h=24, label="all 39 tests passing") + f'''  <defs>
    <linearGradient id="rg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#12172b"/>
      <stop offset="1" stop-color="{BG}"/>
    </linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="209" height="23" rx="12" fill="url(#rg)" stroke="{GREEN}" stroke-opacity="0.55"/>
  <rect x="0.5" y="0.5" width="209" height="23" rx="12" fill="none" stroke="{GREEN}" stroke-opacity="0.9">
    <animate attributeName="stroke-opacity" values="0.9;0.25;0.9" dur="2.2s" repeatCount="indefinite"/>
  </rect>
  <circle cx="14" cy="12" r="4" fill="{GREEN}">
    <animate attributeName="opacity" values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="14" cy="12" r="7" fill="{GREEN}" opacity="0.35">
    <animate attributeName="r" values="4;8;4" dur="1.4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.4;0;0.4" dur="1.4s" repeatCount="indefinite"/>
  </circle>
  <text x="27" y="16" fill="{FG}" font-size="11" font-family="{MONO}" letter-spacing="0.5">ALL 39 TESTS PASSING</text>
</svg>
'''
    with open(os.path.join(OUT, "badge-tests-passing.svg"), "w") as f:
        f.write(svg)

def progress_bar(name, label, value, frac=1.0, c1=CYAN, c2=MAGENTA, w=600):
    """Animated shimmer progress bar, e.g. VERIFICATION · 10/10 LANGUAGES."""
    h = 40
    x0, x1 = 12, w - 12
    y0, bh = 22, 10
    fill_w = int((x1 - x0) * max(0.0, min(1.0, frac)))
    svg = HEADER.format(w=w, h=h, label=label) + f'''  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8" fill="{BG}" stroke="{c1}" stroke-opacity="0.35"/>
  <text x="{x0}" y="14" fill="{FG}" font-size="10.5" font-family="{MONO}" letter-spacing="1.2">{label}</text>
  <text x="{x1}" y="14" text-anchor="end" fill="{c1}" font-size="10.5" font-family="{MONO}" font-weight="bold">{value}</text>
  <rect x="{x0}" y="{y0}" width="{x1-x0}" height="{bh}" rx="5" fill="#0d1220" stroke="#1d2740" stroke-width="1"/>
  <rect x="{x0}" y="{y0}" width="{fill_w}" height="{bh}" rx="5" fill="url(#pg)">
    <animate attributeName="fill-opacity" values="0.85;1;0.85" dur="2.4s" repeatCount="indefinite"/>
  </rect>
  <defs>
    <linearGradient id="pg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect x="{x0}" y="{y0}" width="{fill_w}" height="{bh}" rx="5" fill="url(#sh)">
    <animate attributeName="x" from="{x0-80}" to="{x1}" dur="2.6s" repeatCount="indefinite"/>
  </rect>
  <defs>
    <linearGradient id="sh" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
  </defs>
</svg>
'''
    with open(os.path.join(OUT, f"progress-{name}.svg"), "w") as f:
        f.write(svg)

# ---- dividers (category palette variants) ----
divider(CYAN, MAGENTA, "animated")            # universal (root README)
divider(CYAN, CYAN, "cyan")                   # verification, dirac-lab, Wave_attractors, apps
divider(MAGENTA, MAGENTA, "magenta")          # AB_Cloud_Quantum_Research, lab-3d, Vortex_optimization
divider(VIOLET, VIOLET, "violet")             # formal, Hilbert_Polya, meridian-spectral-observatory
divider(GOLD, GOLD, "gold")                   # monographs, AB_Cloud_Academic_Package
divider(GREEN, CYAN, "green")                 # results
divider(PURPLE, VIOLET, "purple")             # code
divider(BLUE, VIOLET, "blue")                 # docs
divider(GRAY, CYAN, "gray")                   # assets

# ---- live badge ----
badge_passing()

# ---- progress bars (values traceable to results/ registry) ----
progress_bar("tests", "JULIA SUITE · TWO-PASS FLAGSHIP", "39/39 TESTS", 1.0, GREEN, CYAN)
progress_bar("verification", "CROSS-LANGUAGE VERIFICATION", "10/10 LANGUAGES", 1.0, CYAN, MAGENTA)
progress_bar("formal", "FORMAL VERIFICATION", "4/4 ASSISTANTS", 1.0, VIOLET, CYAN)
progress_bar("dataset", "FROZEN ζ-ZERO DATASET", "2,001,058 ZEROS", 1.0, BLUE, VIOLET)
progress_bar("spinor64", "SPINOR STRUCTURES · GUE-CONSISTENT", "64/64", 1.0, CYAN, GREEN)
progress_bar("monographs", "MONOGRAPH EDITIONS RU·EN·ZH", "5/5 EDITIONS", 1.0, GOLD, MAGENTA)

print("SVG assets written to", OUT)
for f in sorted(os.listdir(OUT)):
    print(f"  {f}  {os.path.getsize(os.path.join(OUT, f))} B")
