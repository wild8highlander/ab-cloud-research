# Test 12: Real zeros vs GUE matrix
Verdict: FAIL   |   Generated: 2026-09-14 23:56:59   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Two-sample KS: data vs simulated GUE matrix spectrum.
 METHOD: Two-sample KS: data vs simulated GUE matrix spectrum.

## Result
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 12 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 12 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — 2KS symmetry audit
────────────────────────────────────────────────────────────
 Full: real n=8400 vs ref n=8400, D=0.026548, p=0.005252 (primary verdict governs)
 W1 ref split : D_vs_A=0.024405, D_vs_B=0.030238, |ΔD|=0.005833 (limit 0.02)
 W2 blocks    : 0/4 blocks agree with full verdict at α=0.01 (limit ≥ 3)
 W3 effect    : D_full=0.026548 < 2KS critical at α=0.01: 0.025151? NO
────────────────────────────────────────────────────────────
 W1 ref symmetry      PASS — |ΔD| = 0.005833
 W2 block agree       WARN — 0/4 agree
 W3 D bound           WARN — D 0.0265 vs crit 0.0252
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
