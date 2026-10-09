# `code/julia/` — Suite Provenance Archive

![Julia](https://img.shields.io/badge/Julia-1.10%2B-9558B2?style=flat-square&logo=julia&logoColor=white)
![Status](https://img.shields.io/badge/status-provenance%20archive-blue?style=flat-square)

This subfolder preserves the **provenance copy of the canonical suite**, so
that every number in the reports can be traced to the exact code version
that produced it. Nothing here is required to run the project — use the
canonical suite [`../ab_cloud_v23.jl`](../ab_cloud_v23.jl) — but the folder
is kept for reproducibility archaeology.

## Files

| File | Lines | What it is |
|---|---|---|
| `ab_cloud_v23.jl` | 32 095 | byte-identical provenance copy of the canonical v23 suite (v3.3 line: TEST 34G geometry sweep + estimator-validity patch series) |

## Version lineage (historical)

The v19/v19_v1/v20/v21 historical sources that previously lived here were
consolidated in the "Hilbert Polya" cleanup commit; their role is
documented here so the provenance story stays complete:

| Version | What it contributed |
|---|---|
| **v19 (canonical of its era)** | the two-pass 37-test protocol with the fixed report engine (before the fixes, a `(kind, text)` tuple bug degraded all 37 verdicts to FAIL/WARN and silently skipped pass 2 — see `../../monographs/PACKAGE_README.md`, "v18 → v19") |
| **v19_v1** | introduced the embedded ζ-zero dataset (50 000 Odlyzko zeros as a literal Julia array); the extraction script wrote the standalone text file now used by the dashboard and all Test-38 ports |
| **v20** | extended diagnostics pass; intermediate between the suite and the monograph-v21 code state |
| **v21 / v21_v1** | the code state referenced by the original v21 monograph (including its spinor experiment) |
| **v23 (current)** | 39 registered tests; estimator-validity patch series (Patches A–G, v3.2) and the TEST 34G geometry sweep over seven closed surfaces (v3.3) |

The flagship-run artifacts of the v19 era remain committed under
[`../../results/run_20260902_134759/`](../../results/run_20260902_134759/)
exactly as produced, and the raw report log
[`../../results/ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt`](../../results/ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt)
documents that run line by line.

## Running the canonical suite

```bash
julia code/ab_cloud_v23.jl --test 1   # smoke run (~1 min)
julia code/ab_cloud_v23.jl --test all # full two-pass 39-test suite
```
