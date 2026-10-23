<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-verification-2EA043?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🧊 spinor64 — frozen reference data

> **The inputs of the 64-spinor-structure verification: the Klein graph, the reference spectrum, stats and class table.**

Four frozen files that define the spinor-64 experiment: [`klein_graph_edges.csv`](klein_graph_edges.csv) (the graph skeleton of the Klein quartic), [`reference_spectrum.csv`](reference_spectrum.csv) and [`reference_stats.json`](reference_stats.json) (the reference eigenvalues and their summary statistics), and [`spinor_classes.csv`](spinor_classes.csv) (the 64 structures with their orbit classes 28/21/7/7/1). Everything the verification asserts is a property *of these files* — which is why they are checksum-tracked and never regenerated.

The consuming code and the run outputs live in [`../`](../README.md) (implementation) and [`../output/`](../output/) (frozen results of the last certified run).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`klein_graph_edges.csv`](klein_graph_edges.csv) | CSV | 814 B | — |
| [`reference_spectrum.csv`](reference_spectrum.csv) | CSV | 1.3 KB | — |
| [`reference_stats.json`](reference_stats.json) | JSON | 399 B | — |
| [`spinor_classes.csv`](spinor_classes.csv) | CSV | 12.2 KB | — |

## 🧭 Navigation

[⬅ spinor64/](../README.md) · [→ run outputs](../output/) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder holds **frozen, committed data**: the byte-identical inputs that the verification pipeline reads. The discipline of the repository is that nothing downstream depends on a recomputation — every figure, test and document replays these committed files, so editing or regenerating them in place is forbidden by convention. Where a file also exists in another module's canon, the copies are byte-identical by design.
