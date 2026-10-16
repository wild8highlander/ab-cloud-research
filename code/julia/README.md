# `code/julia/` — Suite Provenance Archive

![Julia](https://img.shields.io/badge/Julia-1.10%2B-9558B2?style=flat-square&logo=julia&logoColor=white)
![Status](https://img.shields.io/badge/status-provenance%20archive-blue?style=flat-square)

This subfolder preserves the **provenance copy of the canonical suite**, so
that every number in the reports can be traced to the exact code version
that produced it. Nothing here is required to run the project — use the
canonical suite [`../ab_cloud_full.jl`](../ab_cloud_full.jl) — but the folder
is kept for reproducibility archaeology.

## Files

| File | Lines | What it is |
|---|---|---|
| `ab_cloud_full.jl` | 32 095 | byte-identical provenance copy of the canonical full suite (v3.3 line: TEST 34G geometry sweep + estimator-validity patch series) |


## Running the canonical suite

```bash
julia code/ab_cloud_full.jl --test 1   # smoke run (~1 min)
julia code/ab_cloud_full.jl --test all # full two-pass 39-test suite
```
