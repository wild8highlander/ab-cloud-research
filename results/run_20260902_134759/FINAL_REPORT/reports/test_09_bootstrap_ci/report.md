# Test 9: Bootstrap CI for slope
Verdict: PASS   |   Generated: 2026-09-02 13:49:53   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Sampling-noise quantification: statistical system with CIs.
 METHOD: Sampling-noise quantification: statistical system with CIs.

## Result
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 9 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 9 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — bootstrap reproducibility audit
────────────────────────────────────────────────────────────
 B1 primary CI: width 0.0288, median -0.1743 (limit 0.1)
 B2 second seed: median -0.1745 (|Δmed|=0.0003, limit 0.02), CI overlap 91% (limit 60%)
 B3 jackknife : LOO slope range [-0.1808, -0.1676] inside boot CI ± 0.02? YES
 B4 half grid : median -0.2085 vs full -0.1743, |Δ|=0.0342 (limit 0.05)
────────────────────────────────────────────────────────────
 B1 CI width          PASS — width = 0.0288
 B2 seed stability    PASS — Δmed 0.0003, overlap 91%
 B3 jackknife         PASS — range [-0.1808, -0.1676]
 B4 half grid         PASS — |Δmed| = 0.0342
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
