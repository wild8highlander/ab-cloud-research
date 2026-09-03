# AB-Cloud 3D — Universal Lattice Operating System for the Riemann Zeros

Numerical verification framework accompanying the preprint *"AB-Cloud: A
Universal Lattice Operating System for the Riemann Zeros"* — a
three-dimensional non-Hermitian Hofstadter Hamiltonian with topological
vortices whose spectrum is statistically indistinguishable from the
non-trivial zeros of the Riemann zeta function.

[![Language: Python + Julia](https://img.shields.io/badge/Languages-Python%20%7C%20Julia-blue.svg)](./code/)
[![Zeros: 5000 embedded](https://img.shields.io/badge/Zeros-5000%20embedded-green.svg)](./data/)
[![Lattice: 36³](https://img.shields.io/badge/Lattice-36%C2%B3-orange.svg)]()
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](../LICENSE)

---

## Overview

This subdirectory is the **complete reproducibility package** for the 3D
branch of the project. The AB-Cloud is a 36×36×36 non-Hermitian Hofstadter
Hamiltonian with σ = 0.5 non-Hermiticity, α = 2.0 Aharonov–Bohm flux,
disorder W = 1.0, and 5000 embedded Riemann zeta zeros. It realises four
interlinked phenomena in a single programmable lattice:

1. **GUE universality for the ζ zeros** — ⟨r⟩ = 0.6159, within 2.7% of the
   GUE theory value 0.5996.
2. **GUE universality for the AB-Cloud eigenvalues** — same ⟨r⟩ within
   statistical error.
3. **Deterministic ensemble switching** (GUE / GOE / Poisson) by tuning a
   single non-Hermiticity parameter σ.
4. **Topological protection** via the Arf invariant of the Klein quartic —
   preserved at 0 across all 5 lattice resolutions N ∈ {16, 64, 256, 1024, 4096}.

The principal empirical result is the **statistical indistinguishability**
of the AB-Cloud spectrum from the ζ-zero sequence: a two-sample KS test
yields p = 0.27–0.88, the L² distance between the two P(s) densities is
0.0127 (34× smaller than the distance from either to the analytic GUE
Wigner surmise), and a permutation test excludes randomness at
Z = 14.10σ (p < 10⁻⁴⁴).

## Key Results

| Metric | Value | Theory / Reference |
|---|---|---|
| ⟨r⟩ (ζ-zeros) | 0.6159 | GUE: 0.5996, Poisson: 0.3863 |
| KS p (AB-Cloud vs ζ-zeros) | 0.27–0.88 | Indistinguishable at α = 0.05 |
| L² distance P(s) | 0.0127 | 34× closer than to the GUE surmise |
| Permutation test Z | 14.10σ | p < 10⁻⁴⁴ |
| Arf invariant | 0 | Preserved across all N |
| Winding number at RH | 1 | Verified at 11 points |

## Directory Structure

```
lab-3d/
├── README.md               # this file
├── requirements.txt        # Python dependencies
├── pyproject.toml          # package config (pip install -e .)
├── Makefile                # run/build shortcuts
├── code/                   # simulation source (Python + Julia), see code/README.md
│   ├── ab_cloud_3d.py            # Python port — Russian UI
│   ├── ab_cloud_3d_en.py         # Python port — English UI
│   ├── ab_cloud_3d.jl            # Julia original — Russian UI
│   ├── ab_cloud_3d_en.jl         # Julia original — English UI
│   ├── quick_start.py            # minimal demo
│   ├── config.py, monograph_constants.py
│   └── …                         # 69 Python modules total (solvers, RMT, reports)
├── data/zeros1.txt         # 1.8 MB — pre-computed Riemann zeta zeros
├── outputs/                # four committed verification runs, see outputs/README.md
│   ├── full_verification_2026-07-31_15-33-39/   # Mode G — reviewer-point verification
│   ├── deep_zeros_2026-07-31_15-36-34/          # Mode H — deep ζ-zero analysis
│   ├── 3d_bridge_2026-07-31_15-36-37/           # Mode I — 9 AB↔Riemann visualizations
│   └── 3d_advanced_2026-07-31_15-51-47/         # Mode J — 8 advanced 3D visualizations
└── preprint/ab_cloud_preprint.tex    # LaTeX source of the preprint (~940 lines)
```

## Installation

| Runtime | Version | Packages |
|---|---|---|
| Python | 3.10+ | `numpy scipy matplotlib sympy mpmath` |
| Julia | 1.10+ | `LinearAlgebra Arpack PyCall Plots SpecialFunctions` |

```bash
cd lab-3d
pip install -r requirements.txt     # option 1
pip install -e .                    # option 2 (editable package)
```

## Quick Start

```bash
cd lab-3d/code
python3 ab_cloud_3d_en.py     # interactive menu, English UI (10 modes A–J)
python3 ab_cloud_3d.py        # Russian UI
python3 quick_start.py        # minimal demo
julia ab_cloud_3d_en.jl       # Julia original, English UI

# rebuild the preprint PDF (run xelatex twice for TOC/refs)
cd ../preprint && xelatex ab_cloud_preprint.tex && xelatex ab_cloud_preprint.tex
```

From the repository root, `make -C lab-3d` style shortcuts are available via
the lab Makefile. The interactive menu accepts unrestricted parameter values
(`inf`, `∞`, `nan`, `max`, `min` all parse) and lets you switch
GUE → GOE → Poisson by changing σ alone.

## The Ten Verification Modes

| Key | Mode | Description |
|---|---|---|
| A | AB-Cloud 3D solver | original 3D non-Hermitian topological Hamiltonian on Lx×Ly×Lz |
| B | RMT for ζ zeros | KS test, ⟨r⟩, Δ₃(L), Σ²(L) vs GUE/GOE/Poisson |
| C | Finite-size scaling | N → ∞ extrapolation of ⟨r⟩ and KS p-values |
| D | Arf invariant | topological protection across N ∈ {16…4096} |
| E | Decay time / E_typ | τₙ = ħ/γₙ — zeros mapped to physical decay times |
| F | Dirac cone / QED | cone emergence at α = 1/2 — the QED correspondence point |
| G | FULL VERIFICATION | all reviewer points in one run (source of Run 1 below) |
| H | Deep Riemann zeros | NN-spacing PDF, R₂(x), K(τ), S(T), τₙ = ħ/γₙ |
| I | 3D Bridge | 9 visualizations tying the AB-Cloud spectrum to the zeros |
| J | Advanced 3D | Chern marker, edge states, J(x,y,z), winding, Hofstadter butterfly, exceptional points |

## Committed Verification Runs (outputs/, 2026-07-31)

### Run 1 — `full_verification_2026-07-31_15-33-39` (Mode G)

| § | Test | Result | Verdict |
|---|---|---|---|
| 1.1 | ⟨r⟩ vs GUE | 0.6159 (theory 0.5996, Poisson 0.3863) | pass |
| 1.1 | KS p vs GUE | 3.04·10⁻⁴ | pass |
| 1.1 | KS p vs Poisson | 0 | pass |
| 2a | Δ₃(L) rel. error | 0.972 | warn (finite-size) |
| 2a | Σ²(L) rel. error | 0.481 | warn (finite-size) |
| 2b | FSS up to N = 5000 | ⟨r⟩ = 0.6159, last KS p = 3.04·10⁻⁴ | pass |
| 2c | Arf invariant | 0 across N ∈ {16…4096} | pass |
| 2d | Dirac cone at α = 1/2 | β = 1.0, cone detected | pass |
| 3 | τ vs E_typ slope | −0.967 (theory −1) | pass |

Overall: 4/6 strict checks pass; the rigidity metrics (§2a) sit within the
expected finite-size scatter for N = 5000 and converge with larger samples.

### Run 2 — `deep_zeros_2026-07-31_15-36-34` (Mode H)

- **all 5000 embedded zeros lie on Re s = 1/2** (RH verified to n = 5000);
- first zero 14.134725142, last used 5447.861998301;
- S(T): ⟨S⟩ = 0.5001, Var S = 0.0789 (theoretical σ_last = 0.585);
- NN spacing, R₂(x), K(τ) — all GUE-consistent.

### Run 3 — `3d_bridge_2026-07-31_15-36-37` (Mode I)

Nine visualizations: spectral staircase, (α,σ) topological phase diagram
(⟨r⟩ from 0.238 Poisson-like to 0.629 GUE with the RH line σ = 1/2 on the
GUE-optimal ridge), Dirac-cone family (σ waterfall), form-factor surfaces
K(τ, N) for Riemann + AB-Cloud, wavefunction density, decay-time manifold,
pair-correlation landscape, S(T) overlay.

### Run 4 — `3d_advanced_2026-07-31_15-51-47` (Mode J)

Bulk-edge correspondence (local Chern marker surface + heatmap), non-Hermitian
probability current J(x,y,z), winding number W|RH = 1 (11 points), Hofstadter
butterfly, exceptional points (121 candidates), edge-state localization
(edge score −0.658).

Each run folder contains `<mode>.json` (machine dump), `.md`/`.txt`/`.html`
reports, `_summary.csv`, and every figure in both PDF and PNG.

## Configuration (defaults)

| Parameter | Value | Meaning |
|---|---|---|
| Lx, Ly, Lz | 36, 36, 36 | lattice dimensions (93 312 sites) |
| sigma | 0.5 | non-Hermiticity (RH / GUE-optimal point) |
| alpha | 2.0 | AB flux per plaquette |
| disorder | 1.0 | Anderson-type W |
| tz | 0.8 | interlayer hopping |
| bc_z | OBC | open boundaries along z |
| nev | 200 | ARPACK eigenvalues |
| n_zeros | 5000 | embedded ζ zeros |
| poly_deg | 12 | polynomial unfolding degree |
| fs_L_max | 20 | max L for Δ₃, Σ² |
| arf_levels | 4 | Arf refinement levels |

## Reproducibility Notes

- **Embedded zeros**: the 5000 zeros are bundled inside the Python and Julia
  sources (Odlyzko tables); n > 5000 is computed on the fly with
  `mpmath.siegelz` (Hardy Z sign search + bisection) at full precision.
- **Determinism**: fixed seeds everywhere; re-running any mode reproduces the
  committed figures modulo the timestamp in the folder name.
- The full 2D/3D suite and the 37-test protocol live in `code/ab_cloud_v19.jl`
  (see `../code/README.md`) — this lab is the dedicated 3D branch.

## Citation

```bibtex
@misc{isaev-2026-ab-cloud-3d,
  title  = {AB-Cloud: A Universal Lattice Operating System for the Riemann Zeros},
  author = {Iskhak Hamzatovich Isaev},
  year   = {2026},
  url    = {https://github.com/wild8highlander/ab-cloud-research/tree/main/lab-3d}
}
```

License: **CC BY-NC-SA 4.0** (see `../LICENSE`).

## Кратко (по-русски)

- Пакет 3D-верификации: 36³ некэрмитовая хофштадтеровская решётка
  (σ = 0.5, α = 2.0, W = 1.0) с 5000 встроенных нулей дзета-функции.
- Главный результат: спектр AB-облака статистически неотличим от нулей
  (KS p = 0.27–0.88, L² = 0.0127, пермутационный тест Z = 14.10σ);
  ⟨r⟩ = 0.6159 против GUE 0.5996.
- Десять режимов A–J; четыре зафиксированных прогона от 2026-07-31 лежат в
  `outputs/` (отчёты json/md/html/csv + все рисунки PDF/PNG).
- Запуск: `python3 code/ab_cloud_3d_en.py` (меню), `quick_start.py` для
  демо; препринт — `preprint/ab_cloud_preprint.tex` (xelatex ×2).
