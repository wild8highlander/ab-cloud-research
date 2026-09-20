# Run 20260917_080329_m2 — Test 34 standalone laboratory, MODE 2 HARDCORE

* Generated 2026-09-17 08:03:30 · Julia 1.12.0 · threads 1
* Model: 96×96 torus, Nv = 2, q = 1.0, α = 0.5, W = 1.0 · 50,000 Odlyzko zeros, canonical ζ-side unfolding
* Ensemble: 20 realizations × 4,568 spacings = 91,360 pooled · seeds 20260976802863…20260976804782

## Headline statistics

| metric | value |
|---|---|
| pooled two-sample KS D vs ζ | **0.0970** |
| pooled p-value | 2.325e-264 |
| d_GUE / d_Pois | 0.0768 / 0.2108 |
| R₂ plateau (1.0–2.0) | 0.9531 |
| ensemble median D / IQR | 0.0991 / 0.0042 |
| leave-one-out D spread | 0.0010 (STABLE) |
| MAD outliers | [18] |
| composite verdict (v23) | GUE-CONSISTENT (c1/c2/c3 all OK) |

## Files

* `FINAL_REPORT.md`, `config.json` — the lab's own report and configuration
* `data_realizations.csv` — per-realization statistics (20 rows)
* `data_R2.csv` — pooled R₂(s): two stacked blocks (AB, ζ) + GUE theory, s = 0.01…3.00 step 0.02
* `data_spacings.csv` — the pooled unfolded spacing arrays (s_AB: 91,360; s_zeta: 49,999)
* `index.html` — the lab's self-contained dashboard
* `plot_01_R2_comparison.png`, `plot_03_spacing_pdf.png` — pooled comparison plots
* `analysis_addendum/` — post-processing for the September 2026 addendum: pooled GUE+Poisson
  mixture fit (`pooled_mixture_fit_summary.json`: w* = 0.281 KS / 0.247 L2, residual 0.0241),
  500-resample bootstrap CI for d_GUE [0.0744, 0.0798], and the two addendum figures
  (English-labelled) embedded in the manuscript/preprints.
