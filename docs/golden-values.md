---
title: Golden values — the frozen reference constants
---

# Golden values

[`verification/data/abcloud_golden.json`](https://github.com/wild8highlander/ab-cloud-research/blob/main/verification/data/abcloud_golden.json)
freezes **206 reference constants in 37 groups** — the exact numbers every
implementation of the 10-language verification stack (Python, Julia, C++,
Rust, Go, Haskell, Fortran, JavaScript, R, MATLAB) must reproduce. All of
them are searchable in the [dashboard's Golden values tab](https://github.com/wild8highlander/ab-cloud-research/tree/main/apps/ab-cloud-dashboard).

## Selected groups

| Group | What it freezes | Size |
|---|---|---|
| `D3` | Dyson–Mehta Δ₃(L) at L = 5, 10, 20, 50 | 4 |
| `K_zeros` | form-factor checkpoints K(t), t = 0.2…3.0 + RMS envelope | 6 |
| `S2` | number variance Σ²(L), L = 5…100 | 5 |
| `ad_zeros` | Byers–Yang flux defect A₂ = 61.4924… | 1 |
| `bN` | the b(N) ladder, N = 100…10000 (+offset variant) | 7 |
| `byers_yang` | max defect on the L = 8 loop | 1 |
| `gram_point` | Gram points g₁…g₁₀₀₀₀ | 8 |
| `gue2_cdf` / `gue2_pdf` | exact GUE CDF/PDF grids, s = 0.05…5.0 | 10 + 10 |
| `goe_cdf` | GOE CDF grid | 10 |
| `ham_*` | first eigenvalues of three frozen Hamiltonians (clean / open / 2-vortex) | 3 × 7 |
| `mon_entropy` | entanglement entropies over 36 (L, α, c, f) configurations | 36 |
| `rh_metrics` | ⟨r⟩, Δ₃, p, n_cb for two lattice runs | 12 |
| `topo_tee` | topological TEER observables | 18 |
| `ks_zeros` | Montgomery KS D and p vs the zeros | 2 |
| `meta` | provenance: γ₁, γ_N, Julia version, zeros file | 5 |

## How they are used

- every implementation loads the same JSON and compares with its own output
  under the tolerance protocol of `verification/`;
- the CI runs the quick protocol on every push;
- the dashboard's **Golden values** tab reads the same file (exported as
  `golden_values.json`) and offers search over group, key and value.

## Regenerating

The golden file is produced by the Julia suite itself
(`code/ab_cloud_full.jl`); it is frozen with the run manifests — it never
regenerates silently. To re-export the dashboard copy after a new suite run:
`python3 scripts/prepare-dashboard-data.py`.
