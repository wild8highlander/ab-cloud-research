<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ⚙️ Vortex_optimization — scripts

> **The full pipeline of the T-34 study: engine, sweeps, GUE control, charts, report builder — and its tests.**

Six scripts that generate the entire study: [`t34_engine.py`](t34_engine.py) is the optimization engine, [`t34_sweep.py`](t34_sweep.py) drives the A/B/C sweeps that wrote [`../data/`](../data/), [`gue96.py`](gue96.py) runs the 96-lattice GUE control, [`t34_charts.py`](t34_charts.py) renders [`../figures/`](../figures/), [`t34_report.py`](t34_report.py) assembles the report, and [`test_engine.py`](test_engine.py) keeps the engine honest. The order matters and is the reproduction recipe: engine → sweep → control → charts → report.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`gue96.py`](gue96.py) | Python | 1.9 KB | — |
| [`t34_charts.py`](t34_charts.py) | Python | 11.3 KB | — |
| [`t34_engine.py`](t34_engine.py) | Python | 19.2 KB | — |
| [`t34_report.py`](t34_report.py) | Python | 47.1 KB | — |
| [`t34_sweep.py`](t34_sweep.py) | Python | 17.3 KB | — |
| [`test_engine.py`](test_engine.py) | Python | 3.4 KB | — |

## 🧭 Navigation

[⬅ Vortex_optimization/](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>
