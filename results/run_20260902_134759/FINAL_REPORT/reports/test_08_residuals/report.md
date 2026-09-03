# Test 8: Residual analysis of fit
Verdict: PASS   |   Generated: 2026-09-02 13:49:43   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Residual structure of the log-log fit — algebraic diagnostics.
 METHOD: Residual structure of the log-log fit — algebraic diagnostics.

## Result
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 8 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 8 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — dense residual audit
────────────────────────────────────────────────────────────
 E1 runs      : 3 runs over 10 doubling-grid residuals (expected 5.8 ± 6.0)
 E2 autocorr  : lag-1 = 0.6794, lag-2 = 0.0053 (sanity limit |r|<0.95)
 E3 scale     : dense residuals sd_first=0.04614, sd_second=0.04289, ratio=1.076 (limits 0.4–2.5)
────────────────────────────────────────────────────────────
 E1 runs              PASS — 3 vs 5.8 expected
 E2 autocorr          PASS — r1=0.679, r2=0.005
 E3 scale             PASS — ratio = 1.076
 E4 sign balance      PASS — 4+/-6
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
