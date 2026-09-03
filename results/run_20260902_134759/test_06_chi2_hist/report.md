# Test 6: Spacing chi^2 histogram test
Verdict: PASS   |   Generated: 2026-09-02 13:49:22   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.
 METHOD: χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.

## Result
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 6 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 6 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — bin-stability audit
────────────────────────────────────────────────────────────
 C1 bins= 300: χ²/df = 2.3771, p = 0.000000 → REJECT
 C1 bins= 150: χ²/df = 3.6171, p = 0.000000 → REJECT
 C1 bins=  75: χ²/df = 6.3149, p = 0.000000 → REJECT
 C1 bins=  37: χ²/df = 11.3303, p = 0.000000 → REJECT
 C2 halves    : χ²/df first=2.5187, second=2.1023, rel.dev=16.5% (limit 50%)
────────────────────────────────────────────────────────────
 C1 bin sweep         PASS — 0 flips vs majority (REJECT)
 C2 halves            PASS — rel.dev = 16.5%
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
