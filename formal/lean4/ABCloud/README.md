# formal/lean4 — Machine-checked AB-Cloud core in Lean 4

![Lean4](https://img.shields.io/badge/Lean4-4.19.0-2E7D32?style=flat-square&logo=lean&logoColor=white)
![Deps](https://img.shields.io/badge/dependencies-lean%20core%20only-2EA043?style=flat-square)
![CI](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/formal.yml?branch=main&style=flat-square&label=formal%20CI)

This directory is the **Lean 4 wing of the formal verification layer**
([`formal/`](../README.md)). It contains two complementary artifacts:

1. **The exact layer** (`ABCloud/Basic.lean`) — machine-checked theorems over
   ℕ/ℤ covering the algebraic skeleton of the verification program:
   the b(N) sum (nonnegativity, monotone accumulation, additivity, triangle
   stability), the Gram offset lattice `g(k) = 8k − 7`, the Hofstadter flux
   certificates, the Hurwitz group orders |PSL(2,7)| = 168 / |PSL(2,8)| = 504 /
   |PSL(2,13)| = 1092, the Klein-quartic orbit decomposition 28+21+7+7+1 = 64,
   and the trace identity Tr(AB) = Tr(BA).
2. **The executable layer** (`ABCloud/Zeta.lean` + `ABCloud/Verify.lean`) — a
   dependency-free Float64 port of the entire Python verification pipeline
   (Lambert W → Gram points → b(N) ladder → unfolded spacings → GUE CDF →
   KS / Cramér–von Mises → log–log fit), which **recomputes the frozen
   reference numbers of the flagship run and checks every one of them**
   (`lake exe abcloud-verify`, exit code 0 = all checks pass).

Zero external dependencies — no Mathlib, no Std: `lake build` finishes in
well under a minute and the formal CI job needs nothing but the pinned
toolchain (`lean-toolchain`: `leanprover/lean4:v4.19.0`).

## Quick start

```bash
cd formal/lean4
lake build            # compile the library + the executable (~40 s)
lake exe abcloud-verify        # full check against the frozen 50k dataset
lake exe abcloud-verify --embedded   # self-contained mode (256 embedded zeros)
```

Expected tail of a healthy run:

```text
  b(100) = 3.058617   ref 3.058617   Δ = 0.000000  (tol 0.000001)  PASS
  b(500) = 2.192884   ref 2.192884   Δ = 0.000000  (tol 0.000001)  PASS
  b(1000) = 1.932106   ref 1.932106   Δ = 0.000000  (tol 0.000001)  PASS
  b(5000) = 1.494224   ref 1.494224   Δ = 0.000000  (tol 0.000001)  PASS
  KS D = 0.099187   ref 0.099187   Δ = 0.000000  (tol 0.000500)  PASS
  CvM W² = 17.604855   ref 17.604855   Δ = 0.000000  (tol 0.005000)  PASS
  decay slope = -0.183102   ref -0.183102   Δ = 0.000000  (tol 0.001000)  PASS
  decay R² = 0.994609   ref 0.994609   Δ = 0.000000  (tol 0.001000)  PASS
 RESULT: 8/8 checks PASS — Lean 4 re-derives the frozen numbers
```

## Files

| File | What it is |
|------|------------|
| `lakefile.lean` | Lake package definition (library + executable), `autoImplicit` off |
| `lean-toolchain` | pinned toolchain `leanprover/lean4:v4.19.0` |
| `ABCloud.lean` | root module |
| `ABCloud/Basic.lean` | the exact layer — theorems over ℕ/ℤ (fixed-point discipline) |
| `ABCloud/Zeta.lean` | the numeric port — Lambert W, gram points, b(N), KS, CvM, ⟨r⟩, regression |
| `ABCloud/Embed.lean` | generated frozen reference data (256 embedded zeros + both reference blocks) |
| `ABCloud/Verify.lean` | the `abcloud-verify` executable (parser, check battery, CLI) |

## What is machine-checked vs. checked numerically

| Statement | Kind | Where |
|-----------|------|-------|
| `0 ≤ Σ\|γ_k − γ̃_k\|` (any residual list) | theorem (induction) | `Basic.sumAbs_nonneg` |
| Partial sums never decrease (Test 2 discipline) | theorem | `Basic.sumAbs_mono` |
| `Σ\|xs ++ ys\| = Σ\|xs\| + Σ\|ys\|` | theorem | `Basic.sumAbs_append` |
| Triangle stability of the residual sum | theorem | `Basic.sumAbs_triangle` |
| `Σ\|·\|/N ≥ 0` for N > 0 | theorem | `Basic.mean_nonneg` |
| Gram lattice `g(k) = 8k−7 > 0` for k ≥ 1 | theorem (`omega`) | `Basic.gramScaled_pos` |
| Gram lattice strictly increasing | theorem (`omega`) | `Basic.gramScaled_mono` |
| Flux equality ⟺ cross-multiplication | theorem | `Basic.flux_eq_cert` |
| Magnetic translation `q(p+1) = qp + q` | theorem | `Basic.flux_shift_scaled` |
| \|PSL(2,7)\| = 168, \|PSL(2,8)\| = 504, \|PSL(2,13)\| = 1092 | theorem (`decide`) | `Basic.psl2*_order` |
| Orbits 28/21/7 divide 168 | theorem (`decide`) | `Basic.klein_orbits_divide_168` |
| Tr(AB) = Tr(BA) for 2×2 matrices | theorem (`simp`) | `Basic.mat2_trace_mul_comm` |
| b(N) ladder reproduces b(100…5000) | executable check, tol 1e-6 | `Verify` |
| KS D = 0.099187 on 4999 spacings | executable check, tol 5e-4 | `Verify` |
| Cramér–von Mises W² = 17.6049 | executable check, tol 5e-3 | `Verify` |
| Decay slope −0.1831, R² = 0.9946 | executable check, tol 1e-3 | `Verify` |

The frozen reference constants in `ABCloud/Embed.lean` are produced by
`verification/python/ab_cloud_verify.py` from the same frozen dataset —
that is what makes the executable layer a genuine cross-language
re-derivation (the 12th language of the verification program) rather than
a self-consistency test.

## Design notes

* **No Mathlib on purpose.** The exact layer needs only `omega`, `decide`,
  `simp` and induction; keeping the dependency surface at zero makes the CI
  job deterministic and fast, and makes the audit surface small.
* **Fixed-point exact layer.** Exact residuals are integers on a common
  scale (e.g. 10¹²) — the same discipline the frozen reference tables use.
* **Regenerating `Embed.lean`.** The data file is generated; if the frozen
  dataset ever changes (it should not — see the data charter), regenerate
  with the reference pipeline and re-run the checks.
* The KS/CvM statistics sort with `Array.qsort` (`a < b`), mirroring the
  Python reference; float parsing is a self-contained decimal parser whose
  round-off differs from platform `strtod` by at most 1 ulp — absorbed by
  the tolerances.
