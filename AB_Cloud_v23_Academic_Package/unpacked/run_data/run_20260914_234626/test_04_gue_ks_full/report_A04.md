# Test 4: GUE KS test (full range)
Verdict: PASS   |   Generated: 2026-09-14 23:52:57   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
STATISTICAL family: one-sample KS of zero spacings vs GUE Wigner surmise. p-values depend on sample size and T-range — finite-data effects are legal.
 METHOD: STATISTICAL family: one-sample KS of zero spacings vs GUE Wigner surmise. p-values depend on sample size and T-range — finite-data effects are legal.

## Result
 Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 4 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[23:52:57.718] [+368.746s]  calc: KS D = 0.021619, p_asymptotic = 9.567870e-21 (n=49999, λ=4.8368)
[23:52:57.719] [+368.748s]  calc: KS D = 0.029562, p_asymptotic = 3.479907e-05 (n=6251, λ=2.3408)
[23:52:57.720] [+368.748s]  calc: KS D = 0.025418, p_asymptotic = 6.066737e-04 (n=6250, λ=2.0125)
[23:52:57.721] [+368.749s]  calc: KS D = 0.021305, p_asymptotic = 6.745302e-03 (n=6251, λ=1.6870)
[23:52:57.721] [+368.750s]  calc: KS D = 0.027409, p_asymptotic = 1.619781e-04 (n=6251, λ=2.1704)
[23:52:57.722] [+368.750s]  calc: KS D = 0.022629, p_asymptotic = 3.252259e-03 (n=6251, λ=1.7919)
[23:52:57.723] [+368.751s]  calc: KS D = 0.019816, p_asymptotic = 1.453640e-02 (n=6251, λ=1.5691)
[23:52:57.723] [+368.751s]  calc: KS D = 0.019647, p_asymptotic = 1.581953e-02 (n=6250, λ=1.5556)
[23:52:57.724] [+368.753s]  calc: KS D = 0.019627, p_asymptotic = 1.595774e-02 (n=6251, λ=1.5542)
[23:52:57.728] [+368.756s]  calc: KS D = 0.024587, p_asymptotic = 1.427535e-13 (n=24999, λ=3.8904)
[23:52:57.729] [+368.758s]  calc: KS D = 0.018906, p_asymptotic = 3.369159e-08 (n=25000, λ=2.9916)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 4 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — deep KS audit
────────────────────────────────────────────────────────────
 Full range: N=49999 spacings, D=0.021619, p=0.000000 (report; primary verdict governs)
 K1 blocks    : D over 8 blocks: min=0.019627 max=0.029562, spread=0.009934 (limit 0.0101)
 K2 half split: D_first=0.024587, D_second=0.018906, |ΔD|=0.005681 (limit 0.02)
 K3 moments   : mean(s)=1.0000 (limit |Δ|<0.02), var(s)=0.1591 vs surmise 0.1781 (limit ±60%)
────────────────────────────────────────────────────────────
 K1 block homog       PASS — spread = 0.009934
 K2 half split        PASS — |ΔD| = 0.005681
 K3 moments           PASS — mean 1.0000, var 0.1591
 Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
