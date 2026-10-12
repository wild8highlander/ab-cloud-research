#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate animated SVGs (SMIL) for VISUAL_ANIMATIONS.
All five are self-contained, GitHub-safe (used via <img>), Critical Line & Copper."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "svg"))
os.makedirs(OUT, exist_ok=True)

BG = "#221B16"; PANEL = "#2C241E"; COPPER = "#C96F4A"; TEAL = "#0E7C86"
GOLD = "#C9A227"; TEXT = "#EDE6E0"; MUTED = "#B8A99C"; GRID = "#3A3028"

def write(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(name, os.path.getsize(path) // 1024, "KB")

# ── 1. architecture flow ──────────────────────────────────────────
ARCH = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="500" viewBox="0 0 880 500">
<defs>
  <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
    <path d="M0,0 L7,3 L0,6 Z" fill="{MUTED}"/>
  </marker>
  <linearGradient id="flow" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{COPPER}" stop-opacity="0.9"/>
    <stop offset="1" stop-color="{TEAL}" stop-opacity="0.9"/>
  </linearGradient>
</defs>
<rect width="880" height="500" fill="{BG}"/>
<text x="440" y="40" text-anchor="middle" fill="{TEXT}" font-size="21" font-family="Segoe UI, sans-serif" font-weight="600">AB Cloud Quantum Research · one machine, four levels</text>
<rect x="290" y="70" width="300" height="78" rx="12" fill="{PANEL}" stroke="{COPPER}" stroke-width="2"/>
<text x="440" y="102" text-anchor="middle" fill="{COPPER}" font-size="15" font-weight="700" font-family="Segoe UI, sans-serif">SPECTRAL CORE</text>
<text x="440" y="126" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">V01–V19 · Th1–Th6 · V13 obligation machine</text>
<rect x="80" y="230" width="230" height="78" rx="12" fill="{PANEL}" stroke="{TEAL}" stroke-width="2"/>
<text x="195" y="262" text-anchor="middle" fill="{TEAL}" font-size="15" font-weight="700" font-family="Segoe UI, sans-serif">AB PROCESSOR</text>
<text x="195" y="286" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">V20 · ISA · Givens-QR · P0</text>
<rect x="570" y="230" width="230" height="78" rx="12" fill="{PANEL}" stroke="{GOLD}" stroke-width="2"/>
<text x="685" y="262" text-anchor="middle" fill="{GOLD}" font-size="15" font-weight="700" font-family="Segoe UI, sans-serif">VERIFICATION</text>
<text x="685" y="286" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">E01–E18 · blind · SHA256 pins · Julia</text>
<rect x="290" y="380" width="300" height="78" rx="12" fill="{PANEL}" stroke="#8C6D1F" stroke-width="2"/>
<text x="440" y="412" text-anchor="middle" fill="#D4A94A" font-size="15" font-weight="700" font-family="Segoe UI, sans-serif">SPINOR STUDY</text>
<text x="440" y="436" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">ES1–ES5 · TS1–TS3 · θ = π/2, π/3, π/7</text>
<g stroke="url(#flow)" stroke-width="2.4" fill="none" marker-end="url(#arr)">
  <path d="M 370 148 L 220 226">
    <animate attributeName="stroke-dasharray" values="4 10; 14 4" dur="1.6s" repeatCount="indefinite"/>
  </path>
  <path d="M 510 148 L 660 226">
    <animate attributeName="stroke-dasharray" values="4 10; 14 4" dur="1.6s" begin="0.4s" repeatCount="indefinite"/>
  </path>
  <path d="M 300 308 L 400 376">
    <animate attributeName="stroke-dasharray" values="4 10; 14 4" dur="1.6s" begin="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M 580 308 L 480 376">
    <animate attributeName="stroke-dasharray" values="4 10; 14 4" dur="1.6s" begin="1.2s" repeatCount="indefinite"/>
  </path>
</g>
<circle r="5" fill="{TEXT}">
  <animateMotion dur="3.2s" repeatCount="indefinite"
    path="M 440 148 L 195 226 L 440 376 L 685 226 L 440 148"/>
</circle>
<text x="440" y="486" text-anchor="middle" fill="{MUTED}" font-size="11.5" font-family="Segoe UI, sans-serif" font-style="italic">reads mathematics in real time · compiles it · carries nothing · survives blind verification</text>
</svg>'''
write("architecture_flow.svg", ARCH)

# ── 2. critical line with pulsing zeros ──────────────────────────
zeros = [14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.00,49.77,52.80,56.45,59.35,61.19]
H = 460
circles = ""
for i, g in enumerate(zeros):
    y = 420 - g * (370 / 100.0)
    circles += f'''<circle cx="300" cy="{y:.0f}" r="6" fill="{TEAL}">
  <animate attributeName="r" values="4;7;4" dur="{1.6 + (i % 4) * 0.25}s" begin="{i * 0.22}s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.55;1;0.55" dur="{1.6 + (i % 4) * 0.25}s" begin="{i * 0.22}s" repeatCount="indefinite"/>
</circle>\n'''
CRIT = f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="{H}" viewBox="0 0 640 {H}">
<rect width="640" height="{H}" fill="{BG}"/>
<line x1="180" y1="30" x2="180" y2="{H-40}" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 5"/>
<line x1="420" y1="30" x2="420" y2="{H-40}" stroke="{GRID}" stroke-width="1" stroke-dasharray="3 5"/>
<line x1="300" y1="25" x2="300" y2="{H-35}" stroke="{COPPER}" stroke-width="3"/>
<text x="308" y="45" fill="{COPPER}" font-size="14" font-family="monospace">Re(s) = 1/2</text>
<text x="120" y="45" fill="{MUTED}" font-size="12" font-family="monospace">σ &lt; 1/2</text>
<text x="432" y="45" fill="{MUTED}" font-size="12" font-family="monospace">σ &gt; 1/2</text>
<text x="180" y="{H-14}" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="monospace">Im s = 0</text>
<text x="420" y="{H-14}" text-anchor="middle" fill="{MUTED}" font-size="12" font-family="monospace">γ = 100</text>
{circles}
<text x="524" y="{H-60}" fill="{TEXT}" font-size="13" font-family="Segoe UI, sans-serif">649 + 639 zeros</text>
<text x="524" y="{H-42}" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">read blind to T = 1000</text>
<text x="524" y="{H-24}" fill="{TEAL}" font-size="12" font-family="monospace">cross-engine: 0.0</text>
</svg>'''
write("critical_line.svg", CRIT)

# ── 3. spinor ring ────────────────────────────────────────────────
def ring_svg(name, k, color, label):
    N = 2 * k
    dots = ""
    for i in range(N):
        a = 2 * math.pi if False else (2 * 3.141592653589793 * i) / N
        import math as _m
        a = _m.radians(360 * i / N)
        x = 150 + 90 * _m.cos(a)
        y = 150 + 90 * _m.sin(a)
        dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{color}" opacity="0.8"/>\n'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="330" viewBox="0 0 300 330">
<rect width="300" height="330" fill="{BG}"/>
<circle cx="150" cy="150" r="90" fill="none" stroke="{GRID}" stroke-width="1.5"/>
{dots}<g>
  <animateTransform attributeName="transform" type="rotate" from="0 150 150" to="360 150 150" dur="{6 * k}s" repeatCount="indefinite"/>
  <circle cx="240" cy="150" r="11" fill="{TEXT}" stroke="{color}" stroke-width="3"/>
</g>
<text x="150" y="286" text-anchor="middle" fill="{color}" font-size="16" font-weight="700" font-family="monospace">θ = π/{k}</text>
<text x="150" y="310" text-anchor="middle" fill="{MUTED}" font-size="12.5" font-family="monospace">N = 2k = {N} · gap = 2π/{N}</text>
</svg>'''
    write(name, svg)

import math
ring_svg("spinor_ring_pi2.svg", 2, COPPER, "θ = π/2")
ring_svg("spinor_ring_pi3.svg", 3, TEAL, "θ = π/3")
ring_svg("spinor_ring_pi7.svg", 7, GOLD, "θ = π/7")

# ── 4. folder map with animated highlights ────────────────────────
def folder_map():
    rows = [
        ("AB_Cloud_Quantum_Research/", COPPER, "the program root · v1.1.0"),
        ("MONOGRAPH_ARCHIVE/", TEAL, "monographs RU/EN × DOCX/PDF + LaTeX"),
        ("HYPOTHESIS_LAB/", GOLD, "test your own hypotheses · CLI + browser"),
        ("VISUAL_ANIMATIONS/", "#D4A94A", "this folder · GIF + SVG + HTML"),
        ("modules/ · research/ · theorems_lemmas/", MUTED, "the machine: core, processor, verification, spinor"),
    ]
    y0 = 78
    boxes = ""
    anims = ""
    for i, (name, color, sub) in enumerate(rows):
        y = y0 + i * 74
        boxes += f'''<rect x="60" y="{y}" width="760" height="56" rx="10" fill="{PANEL}" stroke="{color}" stroke-width="1.8"/>
<text x="84" y="{y+24}" fill="{color}" font-size="15.5" font-weight="600" font-family="Consolas, monospace">{name}</text>
<text x="84" y="{y+44}" fill="{MUTED}" font-size="12" font-family="Segoe UI, sans-serif">{sub}</text>\n'''
        # highlight sweep
        anims += f'''<rect x="60" y="{y}" width="760" height="56" rx="10" fill="{color}" opacity="0">
  <animate attributeName="opacity" values="0;0.16;0" dur="5s" begin="{i * 1.0}s" repeatCount="indefinite"/>
</rect>\n'''
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="880" height="470" viewBox="0 0 880 470">
<rect width="880" height="470" fill="{BG}"/>
<text x="440" y="40" text-anchor="middle" fill="{TEXT}" font-size="20" font-weight="600" font-family="Segoe UI, sans-serif">How this folder works — the map</text>
{boxes}{anims}
<text x="440" y="456" text-anchor="middle" fill="{MUTED}" font-size="11.5" font-style="italic" font-family="Segoe UI, sans-serif">43 campaigns PASS · 9 theorems · storage = 0 · RH honestly blocked (V13)</text>
</svg>'''
    write("folder_map.svg", svg)

folder_map()

# ── 5. logo pulse ─────────────────────────────────────────────────
LOGO = f'''<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">
<defs>
  <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{COPPER}" stop-opacity="0.5"/>
    <stop offset="1" stop-color="{COPPER}" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="240" height="240" fill="{BG}"/>
<circle cx="120" cy="120" r="86" fill="url(#glow)">
  <animate attributeName="r" values="78;92;78" dur="3s" repeatCount="indefinite"/>
</circle>
<circle cx="120" cy="120" r="70" fill="none" stroke="{COPPER}" stroke-width="2.5">
  <animateTransform attributeName="transform" type="rotate" from="0 120 120" to="360 120 120" dur="14s" repeatCount="indefinite"/>
  <animate attributeName="stroke-dasharray" values="90 60; 60 90" dur="3s" repeatCount="indefinite"/>
</circle>
<circle cx="120" cy="120" r="52" fill="none" stroke="{TEAL}" stroke-width="1.6">
  <animateTransform attributeName="transform" type="rotate" from="360 120 120" to="0 120 120" dur="10s" repeatCount="indefinite"/>
</circle>
<text x="120" y="114" text-anchor="middle" fill="{TEXT}" font-size="30" font-weight="800" font-family="Georgia, serif">AB</text>
<text x="120" y="140" text-anchor="middle" fill="{COPPER}" font-size="13" font-family="monospace" letter-spacing="2">CLOUD</text>
<text x="120" y="222" text-anchor="middle" fill="{MUTED}" font-size="10.5" font-family="Segoe UI, sans-serif">reads · compiles · stores nothing</text>
</svg>'''
write("logo_pulse.svg", LOGO)
print("done")
