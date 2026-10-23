<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-labs-7FC8A8?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🗃️ Vortex_optimization — data

> **The sweep tables and the GUE control of the T-34 study, CSV + JSON.**

The numeric middle layer of the T-34 vortex-optimization study: three sweep tables (`sweep_A_L24.csv`, `sweep_B_refine.csv`, `sweep_C_L96.csv`) covering the lattice ladder from L = 24 to L = 96 with the refinement pass, and [`gue_control_L96.json`](gue_control_L96.json) — the GUE control run that the study's statistics are calibrated against. Everything the report and the monograph quote is traceable to these files and, through them, to the frozen curves in [`../curves/`](../curves/).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`gue_control_L96.json`](gue_control_L96.json) | JSON | 207 B | — |
| [`sweep_A_L24.csv`](sweep_A_L24.csv) | CSV | 29.3 KB | — |
| [`sweep_B_refine.csv`](sweep_B_refine.csv) | CSV | 8.2 KB | — |
| [`sweep_C_L96.csv`](sweep_C_L96.csv) | CSV | 917 B | — |

## 🧭 Navigation

[⬅ Vortex_optimization/](../README.md) · [→ frozen curves](../curves/) · [→ figures](../figures/) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds **frozen, committed data**: the byte-identical inputs that the verification pipeline reads. The discipline of the repository is that nothing downstream depends on a recomputation — every figure, test and document replays these committed files, so editing or regenerating them in place is forbidden by convention. Where a file also exists in another module's canon, the copies are byte-identical by design.

The committed data tables of the optimization study: the scan summaries and configuration registers behind the report and the monograph.
