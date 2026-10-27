#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the avatar set: author medallion + four level medallions (SVG)."""
import os

OUT = "/home/z/my-project/repo-work/AB_Cloud_Quantum_Research/assets/avatars"
os.makedirs(OUT, exist_ok=True)
BG = "#221B16"; COPPER = "#C96F4A"; TEAL = "#0E7C86"; GOLD = "#C9A227"
TEXT = "#EDE6E0"; MUTED = "#B8A99C"

def avatar(name, ring, glyph, label, sub):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="180" viewBox="0 0 160 180">
<defs>
  <radialGradient id="g-{name}" cx="0.5" cy="0.42" r="0.62">
    <stop offset="0" stop-color="{ring}" stop-opacity="0.42"/>
    <stop offset="1" stop-color="{ring}" stop-opacity="0"/>
  </radialGradient>
</defs>
<circle cx="80" cy="72" r="66" fill="url(#g-{name})"/>
<circle cx="80" cy="72" r="52" fill="{BG}" stroke="{ring}" stroke-width="2.6"/>
<circle cx="80" cy="72" r="45" fill="none" stroke="{ring}" stroke-width="1" opacity="0.55"
        stroke-dasharray="6 5">
  <animateTransform attributeName="transform" type="rotate" from="0 80 72" to="360 80 72"
    dur="16s" repeatCount="indefinite"/>
</circle>
<text x="80" y="{72 - (0 if len(glyph) < 3 else 4)}" text-anchor="middle" fill="{TEXT}"
      font-size="{40 if len(glyph) < 3 else 26}" font-weight="700"
      font-family="Georgia, serif" dominant-baseline="central">{glyph}</text>
<text x="80" y="148" text-anchor="middle" fill="{ring}" font-size="12.5" font-weight="600"
      font-family="Segoe UI, sans-serif">{label}</text>
<text x="80" y="165" text-anchor="middle" fill="{MUTED}" font-size="10"
      font-family="Segoe UI, sans-serif">{sub}</text>
</svg>'''
    path = os.path.join(OUT, f"avatar_{name}.svg")
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(os.path.basename(path), os.path.getsize(path) // 1024, "KB")

avatar("author", COPPER, "ИИ", "Isaev I. Kh.", "author · ORCID 0009-0003-7299-0701")
avatar("core", COPPER, "ξ", "Spectral core", "V01–V19 · Th1–Th6 · V13")
avatar("processor", TEAL, "U", "AB processor", "V20 · ISA · Givens-QR")
avatar("verifier", GOLD, "Z", "Verification", "E01–E18 · blind · Julia")
avatar("spinor", "#D4A94A", "φ", "Spinor study", "ES1–ES5 · TS1–TS3")
print("done")
