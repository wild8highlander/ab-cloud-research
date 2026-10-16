# Test 3: Convergence rate (power-law fit)
Verdict: PASS   |   Generated: 2026-09-02 13:48:50   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.
 METHOD: log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.

## Result
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 3 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 3 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep rate-law validation
────────────────────────────────────────────────────────────
 R1 dense power law: b(N) ≈ 7.3564·N^(-0.1737), R² = 0.988236 (limit 0.95)
 R2 alt 1/log N   : b(N) ≈ -0.2557 + 16.2185/log(N), R² = 0.997500
                   best of two laws: R² = 0.9975 (limit 0.95)
 R3 walk-forward  : median err 0.05%, max err 0.09% (limits 2%/5%)
 R4 α stability   : α_lower=0.2116 vs α_upper=0.1393, |Δα|=0.0723 (limit 0.2)
────────────────────────────────────────────────────────────
 R1 power-law R²      PASS — R² = 0.9882
 R2 best-law R²       PASS — R² = 0.9975
 R3 walk-forward      PASS — median 0.05%, max 0.09%
 R4 α stability       PASS — |Δα| = 0.0723
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
