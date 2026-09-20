# Run 20260917_084900_m3 — Test 34 standalone laboratory, MODE 3 DEEP DIAG

* Generated 2026-09-17 08:49 · Julia 1.12.0 · same model parameters as the m2 run

## Diagnostics

| plot | content | key value |
|---|---|---|
| `plot_01_cdf_differential.png` (+ `data_cdf_differential.csv`) | signed CDF difference F_AB − F_ζ, single realization | max +0.0913 @ s = 0.65; zero crossing s ≈ 1.05; trough −0.059 @ s ≈ 1.55 |
| `plot_02_short_range.png` | P(s) in the repulsion zone s < 1.2 | P(s < 0.5): AB 17.8% vs ζ 9.4% (single realization) |
| `plot_03_seed_forensics.png` | same parameters, 5 seeds | D ∈ [0.0926, 0.1012], median 0.0954 — no seed lottery |
| `plot_04_lattice_scaling.png` | finite-size probe D(L) | **0.1017 / 0.1017 / 0.1000 at L = 48 / 64 / 96 — flat** |
| `plot_05_bootstrap.png` | bootstrap of d_GUE, 300 resamples | 95% CI [0.0633, 0.0868] |
| `plot_06_cdf.png` | CDF vs GUE/Poisson/ζ | AB left of ζ below s ≈ 1.05 |

Interpretation (manuscript addendum, sections Add.4–Add.5): the distance D ≈ 0.10 is
disorder-independent (W-sweep), size-independent (D(L) flat), seed-stable (forensics,
LOO spread 0.0010), and is fully accounted for by an effective Poisson admixture
w* ≈ 0.25–0.28 in an otherwise GUE-class spectrum; after the mixture fit the residual
(0.0233 single / 0.0241 pooled) equals the GUE-matrix-vs-ζ calibration floor (0.0242).
