<div align="center">

<img src="../assets/logo_abcloud_light.png" width="110" alt="AB Cloud Quantum Research"/>

# VISUAL ANIMATIONS

**How the AB Cloud Quantum Research folder works — shown, not told: GIF
animations for the READMEs, animated SVGs visible right on GitHub, and
interactive HTML pages that run offline.**

Visual animations of the whole folder at work · GIF + SVG + HTML

![badge-gifs](https://img.shields.io/badge/gif-5%20animations-C96F4A?style=for-the-badge)
![badge-svg](https://img.shields.io/badge/svg-7%20animated%20%28SMIL%29-0E7C86?style=for-the-badge)
![badge-html](https://img.shields.io/badge/html-6%20interactive%20pages-C9A227?style=for-the-badge)
![badge-license](https://img.shields.io/badge/license-proprietary-6B6455?style=for-the-badge)

</div>

> [!TIP]
> **Start here:** open [`html/index.html`](html/index.html) — the visual portal
> linking every animation. Everything runs locally; no network, no dependencies.
> On GitHub, the GIFs and animated SVGs below play right inside the README.

---

## 📖 Contents

- [The map of this folder](#-the-map-of-this-folder)
- [GIF collection](#-gif-collection)
- [Animated SVGs](#-animated-svgs)
- [Interactive HTML pages](#-interactive-html-pages)
- [Rebuild everything](#-rebuild-everything)

---

## 🗺 The map of this folder

This folder is the *visual explanation layer* of the program. The research
layers produce verdicts; this folder shows **how and what works**: the
architecture, the blind zero reading, the spinor cycles, the reproducibility
pipeline, and the role of every new folder — with the same honesty the program
itself follows (every number on screen comes from the committed verdicts).

```
VISUAL_ANIMATIONS/
├── README.md                      ← this file
├── LICENSE                        ← the repository license (duplicated verbatim)
├── gif/                           ← five animations for READMEs and slides
│   ├── zeros_rising.gif           ← ζ zeros rise along Re(s) = 1/2
│   ├── pipeline_flow.gif          ← the pulse travels the four levels
│   ├── spinor_cycles.gif          ← θ = π/2 · π/3 · π/7 phase cycles
│   ├── campaign_timeline.gif      ← 43 campaigns appear, all PASS
│   └── compiler_gates.gif         ← Givens gates compile a unitary
├── svg/                           ← animated SMIL SVGs (GitHub-visible)
│   ├── architecture_flow.svg      ← the level map with flowing dashes
│   ├── critical_line.svg          ← pulsing zeros on the critical line
│   ├── spinor_ring_pi2|pi3|pi7.svg← rotating phase on the ring
│   ├── folder_map.svg             ← the folder map with highlight sweeps
│   └── logo_pulse.svg             ← the AB cloud medallion
├── html/                          ← interactive pages (canvas)
│   ├── index.html                 ← ★ the visual portal — start here
│   ├── architecture_tour.html     ← click to send a pulse through the levels
│   ├── zeros_live.html            ← N(T) counts while zeros rise
│   ├── spinor_lab.html            ← cycles and reset (TS2) drawn live
│   ├── how_this_folder_works.html ← campaigns → verdicts → artifacts → monographs
│   └── pipeline_flow.html         ← verdict → dataset → artifact → monograph
└── scripts/                       ← rebuild everything yourself
    ├── make_gifs.py               ← matplotlib + Pillow → gif/
    ├── make_svgs.py               ← SMIL templates → svg/
    └── make_html.py               ← canvas pages → html/
```

## 🎞 GIF collection

| GIF | What it shows | Where to use |
|-----|--------------|--------------|
| `zeros_rising.gif` | the first 29 ζ ordinates rise along the critical line, counter ticking | main README, slides |
| `pipeline_flow.gif` | the pulse travels core → processor → spinor → verification with captions | architecture sections |
| `spinor_cycles.gif` | three phase rings θ = π/2, π/3, π/7 stepping in real time | spinor sections |
| `campaign_timeline.gif` | all 43 campaigns appear level by level — every one PASS | timeline sections |
| `compiler_gates.gif` | Givens gates compile a 4×4 unitary; depth ≤ 7, 1−F ≤ 4.4e−16 | processor sections |

## ✨ Animated SVGs

Seven self-contained SMIL SVGs. They animate **directly on GitHub** when used
via an `<img src="path/to/animation.svg">` tag: the architecture map with flowing connector dashes,
the critical line with pulsing zeros, three rotating spinor rings, the folder
map with highlight sweeps, and the pulsing program medallion. Drop them into
any README:

```markdown
<img src="VISUAL_ANIMATIONS/svg/architecture_flow.svg" width="880">
```

## 🌐 Interactive HTML pages

| Page | Interaction |
|------|-------------|
| `index.html` | the portal — links to everything, embeds the architecture SVG |
| `architecture_tour.html` | **click** anywhere to launch a pulse through the levels |
| `zeros_live.html` | live N(T) counter with the actual zero staircase and rising zeros |
| `spinor_lab.html` | switch θ = π/2 · π/3 · π/7, watch the cycle; **reset** demonstrates TS2 erasure |
| `how_this_folder_works.html` | the four-layer evidence machine, animated top to bottom |
| `pipeline_flow.html` | verdict → dataset → artifact → monograph, with the forbidden reverse arc greyed out |

## 🔧 Rebuild everything

```bash
cd VISUAL_ANIMATIONS/scripts
python3 make_gifs.py    # → gif/*.gif   (matplotlib + Pillow)
python3 make_svgs.py    # → svg/*.svg   (SMIL templates)
python3 make_html.py    # → html/*.html (canvas pages)
```

Requirements: Python ≥ 3.10 with matplotlib and Pillow. No network. The GIF
zero ordinates are the public first 29 zeros — the same data that feeds
`datasets/zeta_zeros_reference.csv` for the blind E17 reference.

---

<div align="center">

*Watch — and verify: every number on screen is taken from the verdicts*

**AB Cloud Quantum Research** · VISUAL_ANIMATIONS · v1.1.0 · © Isaev Iskhak Khamzatovich

</div>
