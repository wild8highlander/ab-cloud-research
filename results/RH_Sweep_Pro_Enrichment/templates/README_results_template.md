# Run {{RUN_NAME}}

> RH-Sweep PRO · AB cloud ↔ ζ zeros · {{SHORT_DESCRIPTION}}
> Date: {{DATE}} · Julia {{JULIA_VERSION}} · {{PLATFORM}}

## TL;DR

| Quantity | Value | Comment |
|:--|:--|:--|
| Best Score | {{SCORE}} / 100 | {{SCORE_MINUS_FLOOR}} above the GUE floor of the method |
| RMT tests | {{TESTS_PASSED}}/{{TESTS_TOTAL}} | {{FAILED_TESTS_LIST}} |
| Configuration | α = {{ALPHA}}, W = {{W}}, σ = {{SIGMA}} | vortices: {{N_VORTICES}} × {{LAYOUT}} |
| ⟨r⟩ | {{R_MEAN}} | R_GUE = 0.5996 · class {{R_CLASS}} |
| K corr(GUE) / corr(ζ) | {{K_GUE}} / {{K_ZETA}} | {{N_ZETA}} ζ zeros · {{N_EIGS}} eigenvalues |
| Lattice | L = {{L}} ({{MATRIX_DIM}}) · {{N_SEEDS}} realizations | N_AB/N_ζ = {{RATIO}} |

**One-line recommendation:** {{ONE_LINE_RECOMMENDATION}}

## Verdicts (11 tests)

- [{{X1}}] 1. ⟨r⟩ ≈ R_GUE (|d_GUE| < 0.05)
- [{{X2}}] 2. R₂(s) closer to GUE than to Poisson
- [{{X3}}] 3. K(t) correlates with K(ζ)
- [{{X4}}] 4. Σ²(L) closer to GUE than to Poisson
- [{{X5}}] 5. Δ₃(L) RMS < 0.5
- [{{X6}}] 6. p(s) RMS < 0.2
- [{{X7}}] 7. χ² Wigner < 0.5
- [{{X8}}] 8. Brody β ≈ 2.0 ± 0.5
- [{{X9}}] 9. Compressibility < 0.3
- [{{X10}}] 10. E(s=1) ≈ 0.171 ± 0.15
- [{{X11}}] 11. ⟨r̃⟩ ≈ 0.3602 ± 0.05

## What is in this folder

| Path | What it is |
|:--|:--|
| `plots/` | 01 — 6-panel comparison with GUE/Poisson/ζ; 02 — ζ inside the AB cloud; 05 — 7 panels of new metrics |
| `csv/metrics.csv` | one row per configuration: 37 columns — see `DATA_DICTIONARY.md` |
| `csv/ab_eigs.txt` | {{N_EIGS}} central eigenvalues (raw spectrum) |
| `csv/zeta_zeros.txt` | the ζ zeros used |
| `txt/report.txt` | console protocol of the run |
| `json/results.json` | the best point in machine-readable form |
| `config.json` | snapshot of all 35 RHConfig fields + environment |
| `manifest.sha256` | checksums of all files (integrity) |
| `curves/` | CSV metric curves — independent recomputation without Julia |
| `sensitivity/` | sweep history, parameter cuts, multi-seed significance |
| `gue_floor.json` | the GUE floor of the method on this sample |

## Reproduction

```bash
julia -e 'include("RH_Sweep_Pro_D.jl");
          cfg = preset_auto({{N_ZETA}});
          cfg.alpha = {{ALPHA}}; cfg.W = {{W}}; cfg.sigma = {{SIGMA}};
          cfg.output_dir = "{{RUN_NAME}}";
          run(cfg)'
```

The seed convention and determinism rules — `RUN_PROTOCOL.md`.
Reproducibility statement: byte-identical output only on the same
platform (Julia {{JULIA_VERSION}} + {{BLAS}}).

## Limitations

{{LIMITATIONS}}
<!-- example: a single point (not a scan) · one platform · N_ζ = 5000 of 13 661 ·
     N_v = 6 — the lower boundary of the working window · E(s=1) failed -->
