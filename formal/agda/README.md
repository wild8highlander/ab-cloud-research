<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ formal/](../README.md) · [🏠 Root README](../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-formal-7C4DFF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🟫 `formal/agda` — the Agda witness

> **One file, builtins only: the smallest independent restatement of the exact layer.**

[`ABCloud.agda`](ABCloud.agda) is the Agda member of the four-assistant panel: a single self-contained module that restates the exact identities of the audit's algebraic skeleton in Agda's dependent-type style, importing nothing beyond the standard-library builtins. Its job is cross-validation by *independent formalisation* — if Coq, Isabelle, Lean and Agda agree on the statements, the agreement is a property of the mathematics rather than of any one proof assistant's library.

Type-check it with `agda ABCloud.agda` (any Agda ≥ 2.6 — the module imports nothing, not even the standard library). The CI job in [`formal.yml`](../../.github/workflows/formal.yml) does exactly that on every push.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`ABCloud.agda`](ABCloud.agda) | Agda | 8.3 KB | the single-module development (builtins-only imports) |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>

<div align="center">

<img src="../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
</div>
