<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ formal/](../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-formal-7C4DFF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🟥 `formal/coq` — the Coq certification

> **The algebraic skeleton of the suite in Gallina: one project, zero axioms beyond Coq's standard library.**

The Coq development certifies the same exact layer as the other three assistants, in Coq's own idiom: `_CoqProject` declares the single-module namespace and [`ABCloud/Core.v`](ABCloud/Core.v) carries the proofs — nonnegativity and monotone accumulation behind the b(N) residual, the Gram-offset lattice identities, group orders and orbit decompositions, and the trace identity Tr(AB) = Tr(BA). The file is deliberately self-contained: no external opam packages, so the CI job needs nothing beyond a stock Coq installation.

Compile it locally with `coq_makefile -f _CoqProject && make` (or open the folder in CoqIDE / VsCoq). The [`formal.yml`](`.github/workflows/formal.yml` in the repository) workflow compiles it on every push; the [`isabelle/`](../isabelle/) and [`agda/`](../agda/) developments mirror the same statements so the three assistants cross-check each other rather than a single formalisation choice.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`_CoqProject`](_CoqProject) | file | 68 B | the project declaration (-Q mapping, source list) |
| `ABCloud/` | folder | 1 item | namespace directory holding the development itself |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

<div align="center">

<img src="../../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
</div>
