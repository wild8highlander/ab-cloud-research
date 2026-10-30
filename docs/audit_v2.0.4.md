# Rigidity-slope audit — v2.0.4

This page anchors the **rigidity-slope audit**: the check that the spectral
rigidity Δ₃(L) of the AB-cloud spectrum grows with the slope predicted for
the GUE universality class, rather than the Poisson expectation.

## What is checked

- The measured **slope of Δ₃(L)** over the accessible L range, with a
  confidence interval, in the main suite
  ([Test 7](https://github.com/wild8highlander/ab-cloud-research/blob/main/code/ab_cloud_full.jl)
  of `code/ab_cloud_full.jl`).
- A bootstrap re-estimation of the same slope
  (suite Test 9), so the headline number does not rest on a single estimator.
- The full Δ₃(L) curve itself, plotted against the GUE reference.

## Where the artifacts are

- Run reports and plots:
  [`results/Test 1-37 ab_cloud_full.jl/run_20260902_134759/`](https://github.com/wild8highlander/ab-cloud-research/tree/main/results/Test%201-37%20ab_cloud_full.jl)
- Per-test `report.md` / `report.pdf` / `report.html` files with the numeric
  verdicts and computation logs.

## Reproduce it yourself

The dashboard's **Live ζ statistics** tab computes the number variance
Σ²(L) and the rigidity Δ₃(L) of the first 50,000 Odlyzko zeros directly in
your browser — no installation needed — and the
[verification package](verification.md) re-implements the same diagnostics
in ten languages.
