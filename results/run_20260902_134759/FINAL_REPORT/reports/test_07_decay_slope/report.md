# Test 7: Decay slope (log-log regression)
Verdict: PASS   |   Generated: 2026-09-02 13:49:32   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².
 METHOD: Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².

## Result
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 7 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 7 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — deep slope validation
────────────────────────────────────────────────────────────
 D1 slope     : -0.1504, 95%CI [-0.1594, -0.1414] (width 0.0179), R²=0.9954 (limits 0.1 / 0.9)
 D2 stability : slope_lo=-0.1752, slope_hi=-0.1385, |Δ|=0.0367 (limit 0.15)
 D3 walk-fwd  : median err 0.05%, max err 0.09% (limits 2%/5%)
 D4 bootstrap : slope=-0.1504 inside boot 95%CI [-0.1621, -0.1378]? YES
────────────────────────────────────────────────────────────
 D1 slope CI          PASS — width 0.0179, R² 0.9954
 D2 stability         PASS — |Δslope| = 0.0367
 D3 walk-forward      PASS — median 0.05%, max 0.09%
 D4 boot vs CI        PASS — CI [-0.1621, -0.1378]
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
