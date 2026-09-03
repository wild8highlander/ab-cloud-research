# Test 2: Monotonicity verification
Verdict: PASS   |   Generated: 2026-09-02 13:48:39   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).
 METHOD: Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).

## Result
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 2 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 2 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep monotonicity audit
────────────────────────────────────────────────────────────
 S1 strict band: 0/39 pairs violate (limit 0)
    segment      mean |Δγ|
    1-5001        1.629872
 5001-10001       1.328818
 10001-15001       1.248992
 15001-20001       1.201689
 20001-25000       1.168653
 25000-30000       1.143731
 30000-35000       1.123510
 35000-40000       1.106908
 40000-45000       1.092713
 45000-50000       1.080314
 S2 segments  : 0 local increases (limit 0)
 S3 new lows  : 40/40 checkpoints = 100% (limit ≥ 60%)
 S4 drawdown  : b(50000)=1.2126 vs b(25)=4.6101 → 73.7% decrease (limit ≥ 5%)
────────────────────────────────────────────────────────────
 S1 strict band       PASS — 0 violations / 39 pairs
 S2 segments          PASS — 0 increases / 10 segments
 S3 new lows          PASS — 100% of checkpoints
 S4 drawdown          PASS — 73.7% decrease
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
