<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ data/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-hilbert-polya-FFB74D?style=flat-square)](../README.md)

</div>

# 🧊 frozen ζ-zero datasets

> **The reference zero datasets (mpmath-computed), stored as NumPy archives — the frozen input of every campaign.**

Four NumPy archives of Riemann-zeta zeros at increasing depth — n = 30, 60, 100 and 800 — computed with `mpmath` and frozen. Everything downstream (the gate family, the trace formula, the statistics ladder) reads these files rather than recomputing zeros, so that a result can always be traced to the same input bits. Treat them as immutable: changing a dataset here invalidates every frozen verdict in the package.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`zeros_mpmath_n100.npz`](zeros_mpmath_n100.npz) | NumPy | 1.8 KB | — |
| [`zeros_mpmath_n30.npz`](zeros_mpmath_n30.npz) | NumPy | 1.2 KB | — |
| [`zeros_mpmath_n60.npz`](zeros_mpmath_n60.npz) | NumPy | 1.5 KB | — |
| [`zeros_mpmath_n800.npz`](zeros_mpmath_n800.npz) | NumPy | 7.2 KB | — |

## 🧭 Navigation

<!-- enriched-r3 -->

This folder holds **frozen, committed data**: the byte-identical inputs that the verification pipeline reads. The discipline of the repository is that nothing downstream depends on a recomputation — every figure, test and document replays these committed files, so editing or regenerating them in place is forbidden by convention. Where a file also exists in another module's canon, the copies are byte-identical by design.

The frozen ζ-zero datasets of the series (NumPy archives): the exact zero values the campaigns and tests replay, byte-identical to the package canon.

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
</div>
