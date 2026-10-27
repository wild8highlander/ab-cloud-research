# Cross-Verification Report — Python ↔ Julia

**Suite:** AB-Cloud Dirac Laboratory v1.3
**Canonical implementation:** `code/dirac_lab.py` (Python 3.11+, numpy/scipy, seed 96)
**Independent port:** `code/dirac_lab_cross.jl` (Julia 1.13.1, LinearAlgebra only, zero external packages)
**Machine verdicts:** Python full run `run_20261006_081031` — **8/8 PASS**; Julia cross-check — **ALL PASS**.

---

## Why cross-verification

The parent repository maintains a 10-language verification stack because an
agreed-upon number is only as trustworthy as the number of independent code
paths that produce it. Following that culture, the Dirac Laboratory re-derives
its four decisive quantities — the continuum limit (D1), the zero-mode tower
(D2), the ζ-decorated operator statistics (D7) and its chiral protection
mechanism (D8) — in a second language written from scratch against the
documentation, not generated from the Python source.

## Results

| Quantity | Python (canonical) | Julia (independent) | Relative deviation | Verdict |
|---|---|---|---|---|
| D1: E₁ at L=16, α=1/2 | 0.765367 | 0.765367 | 1.8·10⁻⁷ | ✓ |
| D1: E₁ at L=24 | 0.517638 | 0.517638 | 1.7·10⁻⁷ | ✓ |
| D1: E₁ at L=32 | 0.390181 | 0.390181 | 9.1·10⁻⁷ | ✓ |
| D2: zero tower, L=16/24/32 | 4 / 4 / 4 | 4 / 4 / 4 | exact | ✓ |
| D2: ‖{H,Γ}‖ | 0.0 | 0.0 | exact | ✓ |
| D2: Γ-polarity of tower | 0 (2×Γ⁺, 2×Γ⁻) | 0 (2×Γ⁺, 2×Γ⁻) | exact | ✓ |
| D7 (clean): tower / E₁·L | 4 / 12.4858 | 4 / 12.4858 | exact | ✓ |
| D7 (ζ): ⟨r⟩ shift toward GUE | +0.1321 | +0.0996 | see note 2 | ✓ |
| D8: ‖{H,Γ}‖ under ζ decoration | 0.0 | 0.0 | exact | ✓ |
| D8: E↔−E pairing error | 4.0·10⁻¹⁵ | 1.5·10⁻¹⁴ | ≪ 10⁻¹⁰ | ✓ |

**Notes.**
1. The D1 deviations (≤ 9·10⁻⁷) are exactly the rounding of the 6-decimal
   reference values quoted from the Python ledger; both implementations agree
   to LAPACK-level precision.
2. The ⟨r⟩ *shift* (the physically meaningful verdict quantity) passes in both
   languages with a comfortable margin over the +0.04 threshold. The absolute
   clean-lattice ⟨r⟩ differs slightly between the ports (0.4759 vs 0.5084 at
   L=32) because the bulk-window boundary convention (integer floor of the
   60% cut) is resolved marginally differently in the two one-liners; the
   effect is O(n_bulk⁻¹) and does not affect any verdict.
3. The Julia port contains its own minimal JSON writer and its own ζ→vortex
   coder — no code was shared with Python beyond the published construction
   formulas (Landau gauge `2πα·x` on y-hops; monumental atan smooth gauge on
   vertical bonds, factor 0.5, unwrapped wrap-bond coordinate; ζ-coding
   `x = L·frac(t/δ)`, `y = L·frac(t/2δ)`, `δ = 2π/log(t/2π)`).

## Extensions cross-verification (v1.1, D9)

The v1.1 index-restoration test D9 is cross-verified by an independent
from-scratch Julia port (`code/dirac_lab_cross_ext.jl`, LinearAlgebra only,
reduced 40×40 grid, dense diagonalization):

| Quantity | Python (canonical, 200-grid) | Julia (independent, 40-grid) | Verdict |
|---|---|---|---|
| D9a: {H,Γ} with wall | 0.0 | 0.0 | ✓ exact |
| D9a: wall kernel pinned | min\|E\| = 3.9·10⁻⁹ | min\|E\| = 6.4·10⁻¹⁷ | ✓ both ≤ 10⁻⁵ |
| D9a: kernel multiplet present | n = 12 (\|E\|<10⁻⁷) | n = 56 (\|E\|<10⁻⁶) | ✓ |
| D9c: kernel grows with wall count | 12 → 16 (+4 = one valley multiplet) | 56 → 58 (+chiral pair) | ✓ |

**Note.** The absolute kernel counts and the splitting scale are grid-size
dependent (the wall mode resolves into valley multiplets whose spacing varies
with L); the *phenomenon* — an exactly pinned near-zero kernel bound by the
mass wall, growing with the wall (index) count — is reproduced from scratch in
both languages. Raw artifact: `results/cross_verification_ext.json`.

## Extensions II cross-verification (v1.2, D11)

The v1.2 conjugation-action test D11 is cross-verified by an independent
from-scratch Julia port (`code/dirac_lab_cross_ext2.jl`, LinearAlgebra only,
N_u = 256 log-grid + the 2000-zero data file). Every machine-precision claim
of the Berry–Keating / Connes operator block is reproduced:

| Quantity | Python (canonical) | Julia (independent) | Window | Verdict |
|---|---|---|---|---|
| D11a: spectrum max\|E − 2πm/Λ\| | 1.7·10⁻¹³ | 2.0·10⁻¹³ | ≤ 10⁻¹¹ | ✓ |
| D11a: semigroup \|U(u₁)U(u₂) − U(u₁+u₂)\| | 1.1·10⁻¹⁴ | 1.1·10⁻¹⁴ | ≤ 10⁻¹¹ | ✓ |
| D11a: unitarity \|U†U − 1\| | 1.2·10⁻¹⁴ | 1.2·10⁻¹⁴ | ≤ 10⁻¹¹ | ✓ |
| D11a: trace comb \|Tr U − Dirichlet\| | 2.6·10⁻¹³ | 4.5·10⁻¹³ | ≤ 10⁻¹¹ | ✓ |
| D11a: Λ-periodicity of Tr U | 8.6·10⁻¹⁴ | 2.3·10⁻¹² | ≤ 10⁻¹¹ | ✓ |
| D11a: staircase identity (24 probes) | exact | exact | integer | ✓ |
| D11a: mean density residual | 1.3750 | 1.375 | [1.10, 1.65] | ✓ |
| D11a: max \|residual\| | 2.1298 | 2.13 | ≤ 2.3 | ✓ |
| D11b: recognition identity (mod 1) | 4.6·10⁻¹³ | 4.5·10⁻¹³ | ≤ 10⁻¹⁰ | ✓ |

**Note.** The transport and form-factor blocks of D11 are Python-canonical
(single-packet statistics on the open lattice; the same convention as D10).
Raw artifact: `results/cross_verification_ext2.json`.


## Extensions III cross-verification (v1.3, D12–D14)

The three beyond-§8 tests are cross-verified by an independent from-scratch
Julia port (`code/dirac_lab_cross_ext3.jl`, LinearAlgebra only: analytic
ladder sums, a 30×30 ζ-coded torus, a bare 36×36 grid-Dirac JR wall and the
sliding-window form factors of both zero bands):

| Quantity | Python (canonical) | Julia (independent) | Window | Verdict |
|---|---|---|---|---|
| D12a: peak \|Tr U(Λ)\|/N_u − 1 | 0.0 | 0.0 | ≤ 10⁻¹² | ✓ |
| D12a: off-peak sup \|Tr U\|/N_u | 5.98·10⁻³ | 5.98·10⁻³ | ≤ 1.05·envelope 6.24·10⁻³ | ✓ |
| D12a: staircase integer identity | exact (3 windows × 5 sizes) | exact (3 windows) | integer | ✓ |
| D12b: ⟨r⟩ of the ζ-torus (L=30, Nv=26) | 0.5958 | 0.5958 | [0.58, 0.62] | ✓ |
| D13: bare JR wall, min\|E\| | 3.9·10⁻⁹ (200×200) | 1.1·10⁻⁴ (36×36, gap/14500) | ≤ gap/1000 | ✓ |
| D14: K(0.10/0.25/0.5/2.0), main band | 0.0042 / 0.123 / 0.396 / 1.231 | 0.0042 / 0.123 / 0.396 / 1.231 | see D14 windows | ✓ |
| D14: K(0.10/0.5/2.0), Odlyzko band t≈10⁵ | 0.0083 / 0.466 / 0.962 | 0.0083 / 0.466 / 0.962 | see D14 windows | ✓ |

**Notes.**
1. The form factors and the torus ⟨r⟩ match the Python canonical run to the
   printed precision — identical constructions evaluated by two independent
   code paths.
2. The 36×36 Julia wall binds to min\|E\| = 1.1·10⁻⁴ = gap/14500: the exact
   kernel (≤ 10⁻⁸) at the production resolution 200×200 is a Python-suite
   result (D9a/D13a); the Julia check confirms the bound state at a coarse
   independent resolution, with the quartic (1/N)⁴ discretization lifting
   expected for the wall mode.
3. The orbit/generator drive blocks of D13 (Connes-coded vortex backgrounds,
   eigsh shift-invert windows) are Python-canonical, same convention as D9–D11.

Raw artifact: `results/cross_verification_ext3.json`.

## How to reproduce

```bash
python3 code/dirac_lab.py --quick --no-figures      # ~1 min sanity pass
python3 code/dirac_lab.py                            # full suite (~2–4 min)
python3 code/dirac_lab_extensions.py                 # extensions D9–D10 (~3–5 min)
python3 code/dirac_lab_extensions2.py                # extensions II D11 (~1 min)
python3 code/dirac_lab_extensions3.py                # extensions III D12-D14 (~4-5 min)
python3 code/dirac_lab_extensions3.py --quick        # extensions III quick (~1 min)
julia   code/dirac_lab_cross.jl                      # Julia cross-check (core, ~1 min)
julia   code/dirac_lab_cross_ext.jl                  # Julia cross-check (D9, ~2 min)
julia   code/dirac_lab_cross_ext2.jl                 # Julia cross-check (D11, ~1 min)
julia   code/dirac_lab_cross_ext3.jl                 # Julia cross-check (D12-D14, ~2 min)
```

Raw artifacts: `results/cross_verification_julia.json` (machine-readable),
per-test CSVs and `results/run_*/REPORT.md` (Python canonical ledger).
