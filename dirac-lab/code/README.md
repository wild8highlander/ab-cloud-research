# code/ — Computational core of the Dirac Laboratory

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Julia](https://img.shields.io/badge/Julia-1.10+-9558B2?style=flat-square&logo=julia&logoColor=white)]()
[![Verdicts](https://img.shields.io/badge/Run-14%2F14%20PASS-2EA043?style=flat-square)]()
[![Extensions](https://img.shields.io/badge/v1.1%20extensions-D9--D10%20ALL%20PASS-2EA043?style=flat-square)]()
[![Extensions II](https://img.shields.io/badge/v1.2%20extensions--II-D11%20ALL%20PASS-2EA043?style=flat-square)]()
[![Extensions III](https://img.shields.io/badge/v1.3%20extensions--III-D12--D14%20ALL%20PASS-2EA043?style=flat-square)]()

Two independent implementations of the same fourteen-test verification programme (v1.4),
with separate Julia cross-checks for the D9, D11 and D12–D14 extensions:

| File | Language | Role |
|---|---|---|
| `dirac_lab.py` | Python 3.10+ (numpy, scipy, matplotlib) | **Canonical core suite** — full D1–D8 ledger, figures (600 dpi), GIF, CSV/JSON artifacts |
| `dirac_lab_extensions.py` | Python 3.10+ (numpy, scipy) | **v1.1 extensions** — D9 (index restoration, Jackiw–Rossi programme) and D10 (Montgomery in motion, transport imaging), same harness/culture |
| `dirac_lab_extensions2.py` | Python 3.10+ (numpy, scipy) | **v1.2 extensions II** — D11 (conjugation-action encoding, Berry–Keating / Connes): exact spectral dilation operator, recognition identity, Connes-substitution transport, drive form factor + dilation sweep |
| `dirac_lab_extensions3.py` | Python 3.10+ (numpy, scipy) | **v1.3 extensions III (beyond §8)** — D12 (the infinite BK ladder, N_u → ∞ at fixed density: comb → delta train, fixed-density staircase, extensive ζ protection), D13 (the D9+D11 pairing: JR wall under the Connes orbit — pinned at 3.9e-9 — and under the conjugating generator — quasi-zero band at gap/679 with measured chiral breaking), D14 (the second form factor à la Odlyzko on three real zero bands incl. t ≈ 1e5) |
| `dirac_lab_cross.jl` | Julia 1.10+ (LinearAlgebra only) | **Independent cross-verification** of D1/D2/D7/D8, zero external packages |
| `dirac_lab_cross_ext.jl` | Julia 1.10+ (LinearAlgebra only) | **Independent cross-verification of D9** (reduced 40×40 grid, dense) |
| `dirac_lab_cross_ext2.jl` | Julia 1.10+ (LinearAlgebra only) | **Independent cross-verification of D11** (operator block: spectrum, algebra, comb, staircase, density, recognition; N_u = 256 + the 2000-zero data file) |
| `dirac_lab_cross_ext3.jl` | Julia 1.10+ (LinearAlgebra only) | **Independent cross-verification of D12–D14** (ladder comb + staircase at N_u = 1024, ζ-torus ⟨r⟩ at L = 30 — exact match 0.5958, bare 36×36 JR wall, form factors of the main and Odlyzko bands — exact match to printed precision) |

## Conventions (both files, verbatim parent-repository recipes)

- Landau-gauge Peierls phase `exp(2πiαx)` on y-hops; x-hops flat; torus wrap.
- Monumental atan smooth vortex gauge on **vertical** bonds, factor **½**,
  principal-value `atan2`, unwrapped coordinate for the wrap bond.
- Density-scaled vortex count `N_v(L) = round(25·L²/900)`, bumped to even.
- ζ→vortex coding: `x = L·frac(t/δ)`, `y = L·frac(t/(2δ))`, `δ = 2π/log(t/2π)`, charges `(−1)^k`.
- Deterministic seed **96**.

## Usage

```bash
python3 dirac_lab.py                  # full core suite (≈ 2–4 min) → ../results/run_*/, ../figures/
python3 dirac_lab.py --quick          # fast pass (≈ 1 min)
python3 dirac_lab.py --test D7        # a single core test
python3 dirac_lab.py --no-figures     # computations only
python3 dirac_lab_extensions.py       # v1.1 extensions D9–D10 (≈ 3–5 min)
python3 dirac_lab_extensions.py --test D9
python3 dirac_lab_extensions2.py     # v1.2 extensions II D11 (≈ 1 min)
python3 dirac_lab_extensions3.py     # v1.3 extensions III D12–D14 (≈ 5 min)
julia   dirac_lab_cross.jl            # core cross-verification → ../results/cross_verification_julia.json
julia   dirac_lab_cross_ext.jl        # D9 cross-verification → ../results/cross_verification_ext.json
julia   dirac_lab_cross_ext2.jl       # D11 cross-verification → ../results/cross_verification_ext2.json
julia   dirac_lab_cross_ext3.jl       # D12–D14 cross-verification → ../results/cross_verification_ext3.json
```

**v1.4 mode independence.** The quick and FULL modes now carry identical verdict
logic at identical sensitive scales: D10b transport runs at L = 48, D10a pair
statistics at the canonical 2000 zeros, and the D9d composite vortex on the
canonical 200² domain in both modes — a quick run reproduces every FULL verdict
(`../results/PERFORMANCE.md` records the measured wall times; the benchmark is
reproducible via `make benchmark` / `python3 ../scripts_gen/benchmark.py`).

## Extension II test map (v1.2, D11)

| ID | Test | Method (one line) |
|---|---|---|
| D11a | Berry–Keating operator | exact spectral dilation generator Ĥ = F†diag(2πm/Λ)F on the log-grid: spectrum 1.7e-13, semigroup/unitarity 1.1e-14, Dirichlet trace comb 2.6e-13, Λ-periodic; staircase integer identity |
| D11a | BK density on real zeros | residual n − (t/2π)ln(t/2πe): mean 1.3750 (7/8 + ⟨S⟩), max 2.13 over all 2000 zeros |
| D11b | recognition identity | frac(t/δ) ≡ frac((t/2π)ln(t/2π)) to 4.6e-13 — the coding phase IS the BK staircase |
| D11b | Connes substitution | Φ_C(t) = (t/2π)ln(t/2πe) cloud re-scatters every vortex: T = 0.1245 vs Poisson 0.0756, T within 1.4% of plain |
| D11c | drive form factor | unfolded K(τ) of the zeros vs in-suite GUE synthetic: ramp on τ ≤ 0.75 (secular S(t) string at τ ≥ 1 documented) |
| D11c | conjugation drive sweep | t → eᵘt, u ∈ [0.05, 0.35]: protected class persists (min T/T_P = 1.26, mean R/R_P = 0.78) |

## Extension test map (v1.1)

| ID | Test | Method (one line) |
|---|---|---|
| D9a | Jackiw–Rebbi wall | grid-Dirac + m(y)σx wall: chiral-pair kernel at 3.9e-9 (gap/4e8), wall-localized |
| D9b | wall + ζ-background | the same wall inside 178 real-ζ monumental vortices: survives; contrast 7e6 vs control |
| D9c | winding scaling | two walls → kernel grows by exactly one fourfold valley multiplet (index = winding) |
| D9d | composite JR vortex | mass winding ν = 2 + statistical Goldstone flux Φ = ν/2 → kernel at 1.3e-15 |
| D10a | pair statistics | unfolded zeros: g(u) vs Montgomery 1−(sinπu/πu)²; number variance Σ²(20) = 0.33 |
| D10b | transport | open L = 48 lattice, equal-density clouds: R_ζ < R_uniform < R_Poisson; T_ζ largest |
| D10c | momentum fingerprint | flip weight and packet broadening order ζ < uniform < Poisson |

## Test map

| ID | Test | Method (one line) |
|---|---|---|
| D1 | Continuum limit | Bloch FT vs analytic bands; E₁(1/L) fit → v_F; tower = Dirac shells |
| D2 | Zero tower | \|E\|<1e-9 count on L-ladder; {H,Γ}; Γ-polarity |
| D3 | Berry phase | Wilson loops: cone loop = π, control loops = 0; curvature map |
| D4 | Landau levels | Exact strip: E_n² = 2v_F²B·n vs Schrödinger B(n+½); lattice n=0 LL |
| D5 | Klein tunneling | 2D grid Dirac vs Schrödinger packet through a smooth barrier (expm_multiply) |
| D6 | Zitterbewegung | Dirac box ω = 2E₁; torus interband dipole |
| D7 | ζ-decoration | clean vs random vs ζ-coded: tower, E₁·L, ⟨r⟩ |
| D8 | Chiral protection | {H,Γ}, bipartiteness, E↔−E pairing under ζ decoration |

*(core D1–D8; the extension maps are above)*

Full documentation: the parent [`README.md`](../README.md#-repository-map) and monograph §12.
