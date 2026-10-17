# RH_Sweep_Pro_Enrichment — scientific enrichment kit for run folders

> Companion to `RH_Sweep_Pro_D.jl` (RH·SWEEP PRO v1.0) and the
> `Vortex_optimization` catalog (test 34). Release 1.0 · 2026-10-16.
> Russian full documentation: `README.md`. Bilingual glossary: report
> chapter 13.

## TL;DR

A typical RH-Sweep PRO run folder contains raw artifacts
(plots/csv/txt/json) but no scientific layer: no README, no data
dictionary, no metric curves, no GUE floor, no per-realization
significance, no integrity manifest. Additionally, in
RH_Sweep_Pro_D.jl v1.0 the functions `sweep_parameter`,
`save_sweep_results` and `sweep_all_parameters` are **called but never
defined**, so the PRO sweep modes crash with `UndefVarError`. This kit
fixes both problems:

- **Julia module** `julia/RH_Results_Enricher.jl` — repair functions
  for the sweep engine (patches D-1/D-2) plus automatic generation of
  P0/P1 artifacts (README, SUMMARY, data dictionary, config.json,
  SHA-256 manifest, curves/, sensitivity/, GUE floor, multi-seed);
- **templates/** — run README, data dictionary, run protocol with the
  test-34 seed convention, verification protocol;
- **monograph/** — PLOS-style chapter draft based on the verified run;
- **enriched_example/** — ready-to-merge files for the specific run
  `RH_Auto_5000_L64_s5_20261016_122739` (manifest computed from the
  actual archive);
- **report/** — full 23-page PDF report (Russian): run audit, gap
  analysis vs the test-34 standard, importance of every setting,
  enrichment plan, protocols, bilingual glossary.

## Verified run results (context)

| Quantity | Value |
|:--|:--|
| Configuration | α = 1/π ≈ 0.31831 · W = 2.0 · σ = 0.5 · L = 64 · 5 realizations |
| Composite score | 84.85 / 100 · tests 10/11 (RMT core 6/6) |
| ⟨r⟩ | 0.59999 (R_GUE = 0.5996; deviation 0.00039) |
| K corr(GUE) / corr(ζ) | 0.988 / 0.942 |
| N_AB / N_ζ | 6140 / 5000 (blocks B = 250) |
| Single FAIL | E(s=1) = 0.521 vs 0.171 → weakened level repulsion (β = 1.72) |

## Quick start

### A — I already have a run and cannot recompute

1. Copy the contents of
   `enriched_example/RH_Auto_5000_L64_s5_20261016_122739/` into your
   run folder (README, SUMMARY, dictionary, config.json, manifest).
2. For P1 artifacts (curves, GUE floor, significance, fresh manifest):

```bash
julia -e 'include("RH_Sweep_Pro_D.jl");
          include("RH_Results_Enricher.jl");
          include("julia/example_post_run.jl")'
```

### B — I will run new simulations

Three-line integration (details in `julia/INTEGRATION.md`):

```julia
include("RH_Results_Enricher.jl")                       # after using-block
# at the end of _final_run(), before return:
enrich_run(cfg, final_result, all_results, eigs_final, zeta_zeros;
           out_dir = cfg.output_dir)
# optionally, once after the run:
gue_floor_multi_report(cfg; n_floor_ens = 20, n_seeds_sig = 5)
```

Every new run then automatically receives README, SUMMARY, dictionary,
config.json and manifest; the sweep modes (`sweep_top10_pro`,
`sweep_combined_quick`, `sweep_all_parameters`) start working and
append an incremental point history to `sensitivity/`.

## Layout

```
RH_Sweep_Pro_Enrichment/
├── README.md / README_EN.md         ← package documentation (RU master / EN twin)
├── RH_Sweep_Pro_D.jl                ← the v1.0 sweep engine this kit repairs
├── SUMMARY.md / SUMMARY.json · DATA_DICTIONARY.md · manifest.sha256
├── julia/                           ← enricher module + integration guide
├── scripts/                         ← FIXED v1.1 engine, enricher copy, changelog
├── data/ · curves/ · figures/ · animations/  ← verified-run artifacts (P1 layer)
├── templates/                       ← README / dictionary / protocols
├── monograph/                       ← PLOS-style chapter draft (RU)
├── enriched_example/                ← ready P0 files for the verified run
└── report/                          ← full PDF report (RU, 23 pp.)
```

## Code defects closed by this kit

| ID | Defect | Fix |
|:--|:--|:--|
| D-1 | `sweep_parameter`, `save_sweep_results` undefined → `UndefVarError` | implementations shipped, signatures match call sites |
| D-2 | `sweep_all_parameters` advertised but missing | full 8×N sweep with incremental CSV logging |
| D-3 | ⟨r̃⟩ target mismatch: 0.3602 (test) vs 0.3997 (panel/plot) | unified to 0.3602 in templates and dictionary |
| D-5/D-6/D-7 | chi²-"p-value", weak K criterion, compressibility proxy | documented in the data dictionary and verification protocol |

## License and citation

Distributed under the ab-cloud-research repository license. When using,
cite the `Vortex_optimization` catalog (test 34) and this kit
(`RH_Sweep_Pro_Enrichment` v1.0).
