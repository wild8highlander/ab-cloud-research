# Test 28: f_GUE figure of merit
Verdict: FAIL   |   Generated: 2026-09-15 03:33:19   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: fraction of spectral diagnostics consistent with GUE.
 METHOD: Statistical: fraction of spectral diagnostics consistent with GUE.
Test 28 HARDCORE pass 2: 96x96, Nv=4, q=±1.0, W=1.0, n=5 realizations, per-realization f_GUE ensemble.
Test 28 HARDCORE: ⟨f_GUE⟩=0.8658±0.0217 (n=5), CI [0.8284,0.9056], scatter σ=0.0485.

## Result
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 28 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[03:10:53.854] [+12244.883s]  calc: Σ²(L=2.000) = 0.423997 (n_pos=8401, n_windows=3000, mean_count=2.01)
[03:10:54.866] [+12245.895s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:15:31.980] [+12523.008s]  calc: Σ²(L=2.000) = 0.663437 (n_pos=5530, n_windows=3000, mean_count=2.03)
[03:15:34.652] [+12525.680s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:20:07.777] [+12798.806s]  calc: Σ²(L=2.000) = 0.629287 (n_pos=5530, n_windows=3000, mean_count=2.02)
[03:20:10.729] [+12801.757s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:24:25.471] [+13056.499s]  calc: Σ²(L=2.000) = 0.620146 (n_pos=5530, n_windows=3000, mean_count=2.04)
[03:24:28.524] [+13059.553s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:28:44.729] [+13315.757s]  calc: Σ²(L=2.000) = 0.737871 (n_pos=5527, n_windows=3000, mean_count=2.04)
[03:28:47.518] [+13318.547s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:33:16.985] [+13588.014s]  calc: Σ²(L=2.000) = 0.526840 (n_pos=5530, n_windows=3000, mean_count=2.02)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 28 (pass 2, HARDCORE): f_GUE figure of merit — ensemble deep pass
n ≥ 5 realizations, per-realization f_GUE, ensemble verdict
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 → expect ≈ 12–17 min
 Config: 96x96, Nv=4, q=±1.00, α=0.5000, W=1.0 (hardcore standard: W=1, q=1, Nv=4)
 real  1/5: f_GUE = 0.8481
 real  2/5: f_GUE = 0.8697
 real  3/5: f_GUE = 0.8755
 real  4/5: f_GUE = 0.8008
 real  5/5: f_GUE = 0.9347

 Ensemble: ⟨f_GUE⟩ = 0.8658 ± 0.0217 | bootstrap CI [0.8284, 0.9056] ∋ 0.90 (diagnostic)
────────────────────────────────────────────────────────────
 ⟨f_GUE⟩ > 0.90       WARN — ⟨f_GUE⟩ = 0.8658 ± 0.0217 (n=5 of 5 finite)
 scatter < 0.10       PASS — σ=0.0485 stable across vortex layouts
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
```
