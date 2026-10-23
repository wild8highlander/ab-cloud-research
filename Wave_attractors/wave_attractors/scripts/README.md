<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ⚙️ Wave_attractors — scripts

> **The study's pipeline: simulator, experiments E1–E7, reference dumps and the figure builders.**

The executable layer of the W-1 study: [`ab_water.py`](ab_water.py) is the core simulator/analyser, the `e*_*.py` files are the per-experiment drivers (E4 frequency, E6 η-scan, E7 time-domain; E1–E3/E5 live in [`run_experiments.py`](run_experiments.py)) that wrote [`../data/`](../data/), [`dump_reference_csv.py`](dump_reference_csv.py) maintains the frozen reference tables, and [`README_documents.md`](README_documents.md) explains how the document set is assembled. Start from `ab_water.py` if you want the physics, from an `e*` driver if you want a reproduction recipe.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`ab_water.py`](ab_water.py) | Python | 7.5 KB | — |
| [`dump_reference_csv.py`](dump_reference_csv.py) | Python | 2.7 KB | — |
| [`e4_frequency.py`](e4_frequency.py) | Python | 5.5 KB | — |
| [`e6_eta_scan.py`](e6_eta_scan.py) | Python | 15.0 KB | — |
| [`e7_time_domain.py`](e7_time_domain.py) | Python | 18.7 KB | — |
| `julia/` | folder | 2 items | see inside |
| [`make_figures.py`](make_figures.py) | Python | 36.2 KB | — |
| `monograph/` | folder | 11 items | see inside |
| [`ray_billiard.py`](ray_billiard.py) | Python | 22.1 KB | — |
| [`README_documents.md`](README_documents.md) | Markdown | 1.6 KB | — |
| `report/` | folder | 7 items | see inside |
| [`run_experiments.py`](run_experiments.py) | Python | 16.4 KB | — |
| [`verify_cross.py`](verify_cross.py) | Python | 5.9 KB | — |
| [`verify_repro.py`](verify_repro.py) | Python | 10.7 KB | — |
| [`verify_td_cross.py`](verify_td_cross.py) | Python | 3.6 KB | — |
| [`wave_directional.py`](wave_directional.py) | Python | 8.2 KB | — |
| [`wave_helmholtz.py`](wave_helmholtz.py) | Python | 8.2 KB | — |

## 🧭 Navigation

[⬅ wave_attractors/](../README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds the **pipeline scripts** of its module: the deterministic code paths that turn frozen inputs into reports, figures and verdicts. The scripts follow the repository's seed discipline — same input, same seed, same bytes out — so a re-run on the pinned platform reproduces the committed artifacts. Nothing here is executed at import time by other modules; they are entry points, documented in the module README.

The experiment scripts of the study: the staged pipeline from ray-level experiments to the cross-reference dump.

**Subfolders:** `julia/` · `monograph/` · `report/`
