<!-- AB-ENRICHED:v2 · wave-deep-dive · executable layer -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=cylinder&height=72&color=0:05060f,50:a78bfa,100:05060f&section=header&text=W1%20EXECUTABLE%20LAYER&fontSize=22&fontColor=e5e7eb&fontAlignY=55&animation=fadeIn" alt="W1 executable layer" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=500&size=14&duration=2600&pause=1000&color=a78bfa&center=true&vCenter=true&width=720&lines=the+pipeline%3A+simulator+to+figure;same+seed+-+same+bytes+out;physics+in+ab_water+py+%C2%B7+recipes+in+e%2A+drivers" alt="Typing: scripts tagline"/>

**🧭 [⬆ wave_attractors/](../README.md) · [🏠 Root README](../../../README.md)**

</div>

<div align="center">

<img src="../../assets/visuals/glyph-scripts.svg" alt="Animated scripts glyph — glowing angle brackets around a pulsing slash" width="72"/>

<img src="../../assets/ai/banner-scripts.webp" alt="AI banner: glowing code streams flowing from floating terminals into a polygonal cavity where they ignite a closed wave route (prompt P-W11)" width="100%"/>

</div>

<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)
[![Kernel](https://img.shields.io/badge/core-ray__billiard.py-a78bfa?style=flat-square)](ray_billiard.py)

</div>

# ⚙️ `scripts/` — the study pipeline

> **The study's pipeline: simulator, experiments E1–E7, reference dumps and the figure builders.**

The executable layer of the W-1 study: [`ab_water.py`](ab_water.py) is the core simulator/analyser, the `e*_*.py` files are the per-experiment drivers (E4 frequency, E6 η-scan, E7 time-domain; E1–E3/E5 live in [`run_experiments.py`](run_experiments.py)) that wrote [`../data/`](../data/README.md), [`dump_reference_csv.py`](dump_reference_csv.py) maintains the frozen reference tables, and [`README_documents.md`](README_documents.md) explains how the document set is assembled. Start from `ab_water.py` if you want the physics, from an `e*` driver if you want a reproduction recipe.

<div align="center">

<img src="../../assets/visuals/pipeline-flow.svg" alt="Animated E1–E7 pipeline with a travelling pulse" width="100%"/>

</div>

> **🧭 Navigation:** [⬅ wave_attractors/](../README.md) · [→ data](../data/README.md) · [🏠 Repo root](../../../README.md)

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`ab_water.py`](ab_water.py) | Python | 7.5 KB | — |
| [`dump_reference_csv.py`](dump_reference_csv.py) | Python | 2.7 KB | — |
| [`e4_frequency.py`](e4_frequency.py) | Python | 5.5 KB | — |
| [`e6_eta_scan.py`](e6_eta_scan.py) | Python | 15.0 KB | — |
| [`e7_time_domain.py`](e7_time_domain.py) | Python | 18.7 KB | — |
| `julia/` | folder | 2 items | see inside — the Julia port and its TD kernel |
| [`make_figures.py`](make_figures.py) | Python | 36.2 KB | — |
| `monograph/` | folder | 11 items | see inside — the document build chain |
| [`ray_billiard.py`](ray_billiard.py) | Python | 22.1 KB | — |
| [`README_documents.md`](README_documents.md) | Markdown | 1.6 KB | — |
| `report/` | folder | 7 items | see inside — the report build chain |
| [`run_experiments.py`](run_experiments.py) | Python | 16.4 KB | — |
| [`verify_cross.py`](verify_cross.py) | Python | 5.9 KB | — |
| [`verify_repro.py`](verify_repro.py) | Python | 10.7 KB | — |
| [`verify_td_cross.py`](verify_td_cross.py) | Python | 3.6 KB | — |
| [`wave_directional.py`](wave_directional.py) | Python | 8.2 KB | — |
| [`wave_helmholtz.py`](wave_helmholtz.py) | Python | 8.2 KB | — |

<details>
<summary><strong>🗺️ Who calls whom — the dependency spine (click)</strong></summary>

```mermaid
flowchart LR
    CORE["ray_billiard.py<br/>k-vector billiard core"] --> RUN["run_experiments.py<br/>E1 · E2 · E3 · E5"]
    CORE --> E4["e4_frequency.py"]
    CORE --> E6["e6_eta_scan.py"]
    WH["wave_helmholtz.py"] --> WD["wave_directional.py"]
    WD --> E6
    E6 --> E7["e7_time_domain.py<br/>ADE-FDTD"]
    AB["ab_water.py<br/>companion"]
    RUN --> DUMP["dump_reference_csv.py"]
    DUMP --> JL["julia/wave_attractors.jl"]
    E7 --> JTD["julia/td_check.jl"]
    JL --> VC["verify_cross.py"]
    JTD --> VTD["verify_td_cross.py"]
    VR["verify_repro.py<br/>audits everything"]
    ALL["every driver"] --> MF["make_figures.py"]
```

The scripts follow the repository's seed discipline — **same input, same seed, same
bytes out** — so a re-run on the pinned platform reproduces the committed artifacts.
Nothing here is executed at import time by other modules; they are entry points.

</details>

## 🧭 Navigation

[⬅ wave_attractors/](../README.md) · [→ julia port](julia/README.md) · [→ monograph build](monograph/README.md) · [→ report build](report/README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

<img src="../../assets/visuals/wave-divider-violet.svg" alt="Animated wave divider" width="100%" height="16"/>

<a href="../README.md"><img src="../../assets/ai/avatar.webp" alt="Study W1 avatar" width="56"/></a>

<sub>🌀 <strong>Hyperbolic Wave Attractors — study W1</strong> · part of the
<a href="../../../README.md">AB-Cloud Research</a> repository ·
DOI <a href="https://doi.org/10.5281/zenodo.21825394">10.5281/zenodo.21825394</a> ·
© 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the
<a href="../../../LICENSE">license terms</a></sub>

</div>
