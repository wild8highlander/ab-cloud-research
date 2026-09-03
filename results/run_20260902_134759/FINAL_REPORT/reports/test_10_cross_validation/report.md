# Test 10: Cross-validation stability
Verdict: PASS   |   Generated: 2026-09-02 13:50:03   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Statistical stability of the fit under data splits.
 METHOD: Statistical stability of the fit under data splits.

## Result
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 10 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 10 (secondary, HARDCORE): deep cross-validation audit
All sub-samples use index-aware Gram points (offset discipline)
────────────────────────────────────────────────────────────
 V1 deciles   : 0 local increases over 10 segment means (limit 0)
 V2 f-sweep   : dev(0.3)=0.0019 → dev(0.9)=0.0006 (must decrease)
                devs: 0.0019 / 0.0011 / 0.0005 / 0.0006
 V3 tripwire  : correct-offset tail b=1.1095, wrong-offset b=19559.2539 → +1762824.6% worse (limit ≥ 5%)
 V4 even-odd  : b_even=1.208457 vs full 1.212553, dev=0.34% (limit 10%)
────────────────────────────────────────────────────────────
 V1 deciles           PASS — 0 increases / 10 segments
 V2 f-convergence     PASS — dev 0.19% → 0.06%
 V3 offset tripwire   PASS — wrong offset +1762824.6% worse
 V4 even-odd          PASS — dev = 0.34%
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
