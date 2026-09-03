# Test 12: Real zeros vs GUE matrix
Verdict: PASS   |   Generated: 2026-09-02 14:02:26   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Two-sample KS: data vs simulated GUE matrix spectrum.
 METHOD: Two-sample KS: data vs simulated GUE matrix spectrum.

## Result
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 12 --no-two-pass
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
 Full: real n=9600 vs ref n=9600, D=0.023333, p=0.010547 (primary verdict governs)
 W1 ref split : D_vs_A=0.028542, D_vs_B=0.020729, |ΔD|=0.007812 (limit 0.02)
 W2 blocks    : 4/4 blocks agree with full verdict at α=0.01 (limit ≥ 3)
 W3 effect    : D_full=0.023333 < 2KS critical at α=0.01: 0.023527? YES
────────────────────────────────────────────────────────────
 W1 ref symmetry      PASS — |ΔD| = 0.007812
 W2 block agree       PASS — 4/4 agree
 W3 D bound           PASS — D 0.0233 vs crit 0.0235
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
