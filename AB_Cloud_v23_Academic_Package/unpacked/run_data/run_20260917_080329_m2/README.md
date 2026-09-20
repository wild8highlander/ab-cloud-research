# `run_20260917_080329_m2/` — Test 34, MODE 2 HARDCORE (Torus Ensemble, 20 Realizations)
> The September 2026 addendum's ensemble pass: 20 realizations on the 96×96 torus against 50,000 zeros — pooled D = 0.0970, composite GUE-CONSISTENT — with the full spacing arrays and the mixture-fit addendum.

_Location: [unpacked/](../../README.md) › [run_data/](../README.md) › [run_20260917_080329_m2/](README.md)_

This folder archives the **first independent re-examination of the Test 34 confrontation** after the v3.2 package freeze — the run behind addendum chapters Add.2–Add.5 of the monograph. The standalone laboratory (`../../lab_standalone/finite-size_lab.jl`, MODE 2 HARDCORE) executed a 20-realization ensemble on the 96×96 torus (Nv = 2, q = 1.0, α = 0.5, W = 1.0) against 50,000 Odlyzko zeros with the canonical ζ-side unfolding, pooling 91,360 lattice spacings against the ζ reference.

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
| composite verdict (v23) | **GUE-CONSISTENT** (c1/c2/c3 all OK) |

The composite verdict is the run's formal conclusion: all three criteria of the v23 composite test are satisfied — the same verdict class the reference run's Test 34 failed at primary tier, now reached with the corrected pipeline.

## What ships here

`FINAL_REPORT_B.md` (the laboratory's own report; renamed from `FINAL_REPORT.md`), `config_B.json` (the run configuration), `data_realizations_B.csv` (per-realization statistics, 20 rows), `data_R2.csv` (pooled R₂(s): AB and ζ blocks + GUE theory, s = 0.01…3.00), `data_spacings.csv` (the pooled unfolded spacing arrays — 91,360 AB spacings and 49,999 ζ spacings), `index_B.html` (the self-contained dashboard; renamed from `index.html`), two comparison plots, and [`analysis_addendum/`](analysis_addendum/README.md) with the post-processed mixture-fit analysis. Every file is described in this folder's contents table below.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `FINAL_REPORT_B.md` | 3.3 KB · 94 lines | The consolidated final report (Markdown) — all statistics, per-realization table, forensics and verdict blocks. |
| `README_original.md` | 1.5 KB · 31 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `config_B.json` | 393 B · 19 lines | The run configuration (JSON). |
| `data_R2.csv` | 7.6 KB · 301 lines | Pooled R₂(s) table: AB and ζ blocks + GUE theory, s = 0.01…3.00 step 0.02. |
| `data_realizations_B.csv` | 1.9 KB · 21 lines | Per-realization statistics table. |
| `data_spacings.csv` | 1.5 MB · 91361 lines | The pooled unfolded spacing arrays (91,360 AB spacings; 49,999 ζ spacings). |
| `index_B.html` | 6.9 KB · 85 lines | The run's self-contained dashboard (opens in any browser). |
| `plot_01_R2_comparison.png` | 51.0 KB · 1600x1000 | Pooled R₂(s) comparison figure: AB cloud vs ζ zeros vs GUE theory. |
| `plot_03_spacing_pdf.png` | 53.9 KB · 1600x1000 | Pooled spacing PDF comparison figure: AB cloud vs ζ zeros vs GUE surmise. |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`analysis_addendum/`](analysis_addendum/README.md) | 4 files | Mixture-fit post-processing of the m2 ensemble run |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../README.md](../../README.md)._