# `code/julia/` — Suite Provenance Archive

> **🧭 Navigation:** [code/](../README.md) · [Root README](../../README.md)

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The suite provenance archive of the Julia side: the committed source that documents where the flagship suite's Julia artifacts came from.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `ab_cloud_full.jl` | 2.1 MB | Julia source |

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
| `ab_cloud_full.jl` | 32 187 | byte-identical provenance copy of the canonical full suite (v3.3 line: TEST 34G geometry sweep + estimator-validity patch series) |


## Running the canonical suite

```bash
julia code/ab_cloud_full.jl --test 1   # smoke run (~1 min)
julia code/ab_cloud_full.jl --test all # full two-pass 39-test suite
```
