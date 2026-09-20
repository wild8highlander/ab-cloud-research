# Test 5: GUE KS test (high-T only)
Verdict: PASS   |   Generated: 2026-09-14 23:53:09   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Same, restricted to high T where GUE asymptotics hold better; still data-limited (embedded 50k zeros, T ≤ 40434 ≪ 10⁶).
 METHOD: Same, restricted to high T where GUE asymptotics hold better; still data-limited (embedded 50k zeros, T ≤ 40434 ≪ 10⁶).

## Result
 Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 5 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[23:53:09.330] [+380.358s]  calc: KS D = 0.021622, p_asymptotic = 9.563953e-21 (n=49989, λ=4.8368)
[23:53:09.526] [+380.554s]  calc: KS D = 0.021625, p_asymptotic = 9.718636e-21 (n=49958, λ=4.8360)
[23:53:09.533] [+380.561s]  calc: KS D = 0.021588, p_asymptotic = 1.254559e-20 (n=49853, λ=4.8228)
[23:53:09.538] [+380.566s]  calc: KS D = 0.021380, p_asymptotic = 4.135955e-20 (n=49523, λ=4.7605)
[23:53:09.542] [+380.570s]  calc: KS D = 0.021203, p_asymptotic = 2.142535e-19 (n=48525, λ=4.6733)
[23:53:09.547] [+380.575s]  calc: KS D = 0.020927, p_asymptotic = 8.613887e-18 (n=45603, λ=4.4714)
[23:53:09.551] [+380.579s]  calc: KS D = 0.020175, p_asymptotic = 1.325911e-13 (n=37230, λ=3.8952)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 5 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — dense high-T sweep
────────────────────────────────────────────────────────────
        T_min    N_zeros            D            p
           50      49990     0.021622     0.000000
          125      49959     0.021625     0.000000
          312      49854     0.021588     0.000000
          781      49524     0.021380     0.000000
         1953      48526     0.021203     0.000000
         4883      45604     0.020927     0.000000
        12207      37231     0.020175     0.000000
 T2 trend     : p(first)=9.564e-21 → p(last)=1.326e-13 (must not degrade); best p=1.326e-13 (info; primary governs)
 T3 top mean  : mean(s) at highest band = 1.0000 (limit |Δ|<0.02)
────────────────────────────────────────────────────────────
 T2 trend             PASS — p 9.564e-21 → 1.326e-13
 T3 top mean          PASS — mean = 1.0000
 Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
