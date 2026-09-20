# `run_20260917_084900_m3/` — Test 34, MODE 3 DEEP DIAG (Deep Diagnostics)
> Six diagnostic panels that dissect the confrontation residual: differential CDF, short-range repulsion zone, seed forensics, finite-size probe, bootstrap, and the full CDF comparison.

_Location: [unpacked/](../../README.md) › [run_data/](../README.md) › [run_20260917_084900_m3/](README.md)_

Where the MODE 2 run measured the confrontation, the MODE 3 DEEP DIAG run dissected it. Executed 45 minutes after the m2 ensemble on the same protocol (96×96 torus, 50,000 zeros, canonical ζ-side unfolding), this run produced the six diagnostic panels behind addendum chapter Add.4 of the monograph — each answering one specific question a sceptical referee would ask about the D ≈ 0.10 residual.

## The six panels

| Panel | Question it answers | Key value |
|---|---|---|
| `plot_01_cdf_differential.png` (+ `data_cdf_differential.csv`) | *Where* exactly do the CDFs diverge? Signed difference F_AB − F_ζ: max +0.0913 at s = 0.65, trough −0.059 at s ≈ 1.55, zero crossing s ≈ 1.05 | single realization |
| `plot_02_short_range.png` | Is level repulsion present in the s < 1.2 zone? | P(s < 0.5): AB 17.8% vs ζ 9.4% (single realization) |
| `plot_03_seed_forensics.png` | Is the residual a seed lottery? Same parameters, 5 seeds: D ∈ [0.0926, 0.1012], median 0.0954 | no seed lottery |
| `plot_04_lattice_scaling.png` | Does the residual grow or shrink with the lattice? D(L) = 0.1017 / 0.1017 / 0.1000 at L = 48 / 64 / 96 | **flat** |
| `plot_05_bootstrap.png` | How tight is d_GUE? Bootstrap, 300 resamples: 95% CI [0.0633, 0.0868] | tight |
| `plot_06_cdf.png` | The full CDF picture vs GUE / Poisson / ζ | AB left of ζ below s ≈ 1.05 |

## Interpretation (as documented in Add.4–Add.5)

The residual D ≈ 0.10 is **disorder-independent** (the W-sweep of Add.3), **size-independent** (D(L) flat), and **seed-stable** (forensics; leave-one-out spread 0.0010). The mixture analysis of the companion `analysis_addendum/` folder then accounts for it entirely as an effective Poisson admixture w* ≈ 0.25–0.28 in an otherwise GUE-class spectrum, with the post-fit residual equal to the GUE-matrix calibration floor. This folder ships the six PNG panels and the differential-CDF CSV; the README_original.md of the run is preserved alongside as shipped.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `README_original.md` | 1.4 KB · 20 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `data_cdf_differential.csv` | 12.4 KB · 302 lines | The signed CDF difference F_AB − F_ζ table behind the differential-CDF panel. |
| `plot_01_cdf_differential.png` | 45.9 KB · 1600x1000 | Differential CDF panel F_AB − F_ζ (max +0.0913 @ s=0.65; zero crossing s≈1.05). |
| `plot_02_short_range.png` | 52.6 KB · 1600x1000 | Short-range repulsion zone panel: P(s) for s < 1.2, AB vs ζ. |
| `plot_03_seed_forensics.png` | 39.6 KB · 1600x1000 | Seed forensics panel: 5 seeds, D ∈ [0.0926, 0.1012] — no seed lottery. |
| `plot_04_lattice_scaling.png` | 30.3 KB · 1600x1000 | Finite-size probe D(L) at L = 48/64/96 — flat. |
| `plot_05_bootstrap.png` | 43.6 KB · 1600x1000 | Bootstrap of d_GUE, 300 resamples, 95% CI [0.0633, 0.0868]. |
| `plot_06_cdf.png` | 48.1 KB · 1600x1000 | Full CDF comparison vs GUE/Poisson/ζ. |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../README.md](../../README.md)._