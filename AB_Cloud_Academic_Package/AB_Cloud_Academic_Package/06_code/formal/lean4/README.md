<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ formal/](../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-formal-7C4DFF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🟩 `formal/lean4` — the executable Lean 4 re-derivation

> **A Float64 port of the reference pipeline that lives inside a proof assistant — and re-derives the frozen flagship numbers from the raw ζ-zero dataset.**

This folder contains the Lean 4 development of the AB-Cloud formal layer: the exact algebraic skeleton (residual nonnegativity, the Gram-offset lattice, group orders, the trace identity Tr(AB) = Tr(BA)) proved with `sorry`-free kernels where exactness is possible, and — the centrepiece — **`ABCloud.lean`, an executable 12th language**: a full Float64 port of the Python reference pipeline (Lambert W → Gram points → b(N) ladder → unfolded spacings → GUE CDF → KS / Cramér–von Mises → log–log fit).

The executable reads the same frozen ζ-zero dataset as the numerical suite and prints the same headline numbers, exiting non-zero if anything drifts beyond the committed tolerance — so the formal CI job doubles as a numerical regression gate. Zero external dependencies: `lake-manifest.json` pins nothing beyond core, by design (see the [design notes](../README.md#design-notes) of the formal layer).

## ▶️ Build & run

```bash
cd formal/lean4
lake build            # elaborates the whole development, proofs included
lake exe abcloud-verify    # runs the executable re-derivation; non-zero exit = drift
```
CI runs both commands on every push — see the `lean4` job in [`formal.yml`](`.github/workflows/formal.yml` in the repository). The pinned toolchain in `lean-toolchain` is what CI installs; any newer toolchain must re-verify cleanly before being pinned here.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| `ABCloud/` · [README](ABCloud/README.md) | folder | 5 items | module namespace for the development's submodules |
| [`ABCloud/Basic.lean`](ABCloud/Basic.lean) | Lean 4 | 8.7 KB | exact layer — theorems over ℕ/ℤ (b(N) residual, Gram-offset lattice, group orders, orbit decomposition, trace identity) |
| [`ABCloud/Zeta.lean`](ABCloud/Zeta.lean) | Lean 4 | 7.9 KB | numeric port — Lambert W → Gram points → b(N) ladder → spacings → GUE CDF → regression |
| [`ABCloud/Embed.lean`](ABCloud/Embed.lean) | Lean 4 | 8.5 KB | generated frozen reference data (golden anchors + embedded 256-zero dataset) |
| [`ABCloud/Verify.lean`](ABCloud/Verify.lean) | Lean 4 | 10.6 KB | the `abcloud-verify` executable (parser, check battery, CLI) |
| [`ABCloud.lean`](ABCloud.lean) | Lean 4 | 336 B | root module — exact lemmas + the executable re-derivation with exit-code-gated tolerance checks |
| [`lake-manifest.json`](lake-manifest.json) | JSON | 113 B | lockfile — intentionally dependency-free |
| [`lakefile.lean`](lakefile.lean) | Lean 4 | 807 B | Lake build recipe (checked by CI on every push) |
| [`lean-toolchain`](lean-toolchain) | file | 25 B | pinned Lean 4 toolchain version |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>

<div align="center">

<img src="../../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
</div>
