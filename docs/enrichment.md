---
title: Enrichment run RH_Auto_5000_L64_s5
---

# Enrichment run RH_Auto_5000_L64_s5

The post-run enrichment froze the deepest diagnostic pass of the programme
(2026-10-17): seven curves, five GIF animations and a 23-page report, all
committed under
[`results/RH_Sweep_Pro_Enrichment/`](https://github.com/wild8highlander/ab-cloud-research/tree/main/results/RH_Sweep_Pro_Enrichment)
and drawn live in the [dashboard's Enrichment tab](https://github.com/wild8highlander/ab-cloud-research/tree/main/apps/ab-cloud-dashboard).

## Headline

| Quantity | Value | Reference |
|---|---|---|
| Configuration | α = 1/π, W = 2.0, σ = 0.5, L = 64, 5 seeds | `SUMMARY.json.best_config` |
| Volume | 6,140 eigenvalues × 5,000 ζ zeros | per-seed spectra |
| Composite score | **84.846 / 100** | tests 10/11, RMT core 6/6 |
| ⟨r⟩ per seed | **0.59999** | GUE 0.5996, Δr = 0.00039 |
| Ratio class | GUE | d_GUE 0.00039 « d_GOE 0.064 |
| K(t) correlation | 0.9417 (ζ) / 0.9882 (GUE) | form factor |
| R² RMS | **0.020975** vs GUE; 0.258933 vs Poisson | per-seed |
| Only failed test | E(s=1) = 0.521 (exact-GUE target 0.171) | weaker level repulsion on the p(s) tail |

## The GUE error floor

A GUE simulation of the same volume split into two halves and pushed through
the *same* pipeline (poly-unfold deg 5 → blocks of 250 → KDE bw = 0.15)
deviates from itself by R² RMS **0.025557** — the method's own noise floor
(method Т34 `gue_control`). The run's per-seed R² RMS of 0.020975 lies
**below** that floor: the AB-cloud is statistically indistinguishable from a
GUE realization of the same volume.

The file-level (union-of-5-seeds) metrics differ from the per-seed ones for a
known reason: `csv/ab_eigs.txt` is the globally sorted union of 5 seeds, so
post-hoc statistics over the file read the m = 5 superposition
(⟨r⟩ = 0.3912, ⟨r̃⟩ = 0.2527). A GUE union simulation reproduces exactly this
(⟨r⟩ = 0.393 ± 0.004, ⟨r̃⟩ = 0.253). The enricher's fix writes per-seed
spectra to `csv/seeds/ab_eigs_seed{k}.txt` (patch P10).

## Key finding, kept traceable

> `csv/ab_eigs.txt` is saved globally sorted = union of 5 seeds. Post-hoc
> metrics over the file show the m = 5 superposition; the per-seed metrics of
> the run (results.json) were computed **before** sorting.

## Artifacts

- `data/` — metrics.csv (38 columns), results.json, config.json,
  gue_control.json, assets.npz, zeta_zeros.txt, ab_eigs.txt;
- `curves/` — R₂(s), K(t), Σ²(L), Δ₃(L), p(s)+E(s), the ratio histogram,
  the superposition ⟨r⟩(m);
- `figures/` + `animations/` — 7 new figures, 5 GIF animations;
- `report/` — the run report and the 23-page PDF;
- `monograph/MONOGRAPH_CHAPTER_RU.md` — the chapter draft;
- `julia/` — `RH_Results_Enricher.jl` and the fixed sweep engine
  `RH_Sweep_Pro_D_FIXED.jl` (10 patches, D-1…D-7, P10).

## In the dashboard

The browser tabs read the frozen JSON exports of this run — no numerics are
re-run in the browser on those tabs:

- **Enrichment run** — all seven curves, AB vs ζ vs GUE vs Poisson;
- **Metrics ×38** — the full sweep table, regrouped;
- **GUE control** — the error floor and the superposition check.

To regenerate the JSON after a new suite run:
`python3 scripts/prepare-dashboard-data.py` (numpy required; the generated
files are committed, so readers never need Python).
