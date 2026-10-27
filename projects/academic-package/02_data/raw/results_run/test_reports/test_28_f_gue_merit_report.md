# Test 28: f_GUE figure of merit
Verdict: FAIL   |   Generated: 2026-09-02 17:39:02   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Statistical: fraction of spectral diagnostics consistent with GUE.
 METHOD: Statistical: fraction of spectral diagnostics consistent with GUE.
Test 28 HARDCORE pass 2: 96x96, Nv=4, q=±1.0, W=1.0, n=5 realizations, per-realization f_GUE ensemble.
Test 28 HARDCORE: ⟨f_GUE⟩=0.8553±0.0214 (n=5), CI [0.8184,0.8946], scatter σ=0.0479.

## Result
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 28 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[17:13:08.712] [+12303.994s]  calc: Σ²(L=2.000) = 0.404688 (n_pos=9601, n_windows=3000, mean_count=1.99)
[17:13:09.363] [+12304.645s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:18:15.462] [+12610.744s]  calc: Σ²(L=2.000) = 0.663437 (n_pos=5530, n_windows=3000, mean_count=2.03)
[17:18:19.349] [+12614.631s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:23:20.729] [+12916.011s]  calc: Σ²(L=2.000) = 0.629287 (n_pos=5530, n_windows=3000, mean_count=2.02)
[17:23:26.725] [+12922.007s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:28:20.247] [+13215.529s]  calc: Σ²(L=2.000) = 0.620146 (n_pos=5530, n_windows=3000, mean_count=2.04)
[17:28:26.188] [+13221.470s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:33:37.233] [+13532.515s]  calc: Σ²(L=2.000) = 0.737871 (n_pos=5527, n_windows=3000, mean_count=2.04)
[17:33:43.480] [+13538.762s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[17:38:57.213] [+13852.495s]  calc: Σ²(L=2.000) = 0.526840 (n_pos=5530, n_windows=3000, mean_count=2.02)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 28 (pass 2, HARDCORE): f_GUE figure of merit — ensemble deep pass
n ≥ 5 realizations, per-realization f_GUE, ensemble verdict
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 → expect ≈ 12–17 min
 Config: 96x96, Nv=4, q=±1.00, α=0.5000, W=1.0 (hardcore standard: W=1, q=1, Nv=4)
 real  1/5: f_GUE = 0.8378
 real  2/5: f_GUE = 0.8592
 real  3/5: f_GUE = 0.8649
 real  4/5: f_GUE = 0.7911
 real  5/5: f_GUE = 0.9234

 Ensemble: ⟨f_GUE⟩ = 0.8553 ± 0.0214 | bootstrap CI [0.8184, 0.8946] ∌ 0.90 (diagnostic)
────────────────────────────────────────────────────────────
 ⟨f_GUE⟩ > 0.90       WARN — ⟨f_GUE⟩ = 0.8553 ± 0.0214 (n=5 of 5 finite)
 scatter < 0.10       PASS — σ=0.0479 stable across vortex layouts
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
```
