<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ formal/](../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-formal-7C4DFF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🟧 `formal/isabelle` — the Isabelle/HOL session

> **The same skeleton as an Isabelle/HOL session — two files, stock HOL, nothing else.**

An intentionally minimal Isabelle/HOL session: [`ROOT`](ROOT) declares the `ABCloud` session against pure HOL, and [`ABCloud.thy`](ABCloud.thy) carries the formalisation — the residual inequalities of the b(N) ladder, the Gram-offset identities, and the finite group facts used by the audit's exact layer. Keeping the session to two files is a stated design goal: the formal layer certifies the algebraic *skeleton*, not the Float64 numerics (that role belongs to the [Lean 4 executable](../lean4/)).

Open the folder in Isabelle/jEdit and the session builds on the spot; headlessly, `isabelle build -D .` does the same. CI compiles the session on every push via [`formal.yml`](`.github/workflows/formal.yml` in the repository).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`ABCloud.thy`](ABCloud.thy) | Isabelle | 4.5 KB | the formalisation — definitions, lemmas and their proofs |
| [`ROOT`](ROOT) | file | 47 B | Isabelle session declaration (HOL import, session name) |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

<div align="center">

<img src="../../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
</div>
