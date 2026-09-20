# Test 23: Complex fractal factor CF
Verdict: PASS   |   Generated: 2026-09-15 01:25:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Log-periodic factor — semi-statistical curve comparison.
 METHOD: Log-periodic factor — semi-statistical curve comparison.
Test 23 HARDCORE: |CF|−1 = 0.00e+00 (256-bit), β err 3.04e-16 (Float64) / 3.28e-05 (LaTeX), c_AB err 6.82e-06.

## Result
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 23 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 23 (pass 2, HARDCORE): complex fractal factor — 256-bit audit
────────────────────────────────────────────────────────────
 |CF| − 1 at 256-bit: 0.00e+00 (contract < 1e-30)
 β_imag: Float64 2.854032819406525 vs 256-bit 2.854032819406525 (|Δ| = 3.04e-16)
 β_imag vs LaTeX 2.854: |Δ| = 3.28e-05 (contract < 1e-3)
 c_AB = 1 − |CF_hard|: 0.020623 vs 0.02063 (|Δ| = 6.82e-06, contract < 1e-3)
────────────────────────────────────────────────────────────
 |CF| = 1 (1e-30)     PASS — pure-phase property at 256-bit: 0.00e+00
 β_imag anchors       PASS — Float64 |Δ|=3.04e-16; LaTeX 2.854 |Δ|=3.28e-05
 c_AB ≈ 0.02063       PASS — c_AB = 0.020623, |Δ| = 6.82e-06
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
