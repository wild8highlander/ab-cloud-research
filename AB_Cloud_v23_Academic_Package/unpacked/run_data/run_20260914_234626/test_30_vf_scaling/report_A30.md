# Test 30: Dirac cone vF scaling vs L
Verdict: PASS   |   Generated: 2026-09-15 04:40:07   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT-geometry: FIRST DISTINCT Dirac level above the zero tower ~ 1/L (the old ev[j0+1]-ev[j0] hit the valley-degenerate partner ~1e-15 → gaps 0.0); L/4∈ℤ grid up to t31_lmax; linear fit R².
 METHOD: EXACT-geometry: FIRST DISTINCT Dirac level above the zero tower ~ 1/L (the old ev[j0+1]-ev[j0] hit the valley-degenerate partner ~1e-15 → gaps 0.0); L/4∈ℤ grid up to t31_lmax; linear fit R².
Test 30 HARDCORE: 11-point fit R²=0.9999, v_F=1.9447, E₁·L cv=0.75%, zero tower 4 ∀L.

## Result
 Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 30 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[04:30:03.322] [+16994.351s]  build_ab_cloud_hamiltonian: 16x16 (N=256), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:04.976] [+16996.005s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:06.368] [+16997.396s]  build_ab_cloud_hamiltonian: 32x32 (N=1024), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:08.104] [+16999.132s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:10.730] [+17001.759s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:15.385] [+17006.413s]  build_ab_cloud_hamiltonian: 56x56 (N=3136), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:25.362] [+17016.391s]  build_ab_cloud_hamiltonian: 64x64 (N=4096), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:46.224] [+17037.252s]  build_ab_cloud_hamiltonian: 72x72 (N=5184), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:31:31.588] [+17082.616s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:32:56.543] [+17167.571s]  build_ab_cloud_hamiltonian: 88x88 (N=7744), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:35:25.008] [+17316.036s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 30 (pass 2, HARDCORE): Dirac cone velocity — dense-grid audit
────────────────────────────────────────────────────────────
 11-point mod-4 grid L=16…96, zero-tower check, E₁·L constancy
 ⚠ RUNTIME: 11 value-only diagonalizations, L up to 96 — expect ≈ 8–12 min
 L=16: E₁ = 0.765367 (E₁·L = 12.2459), zero_modes = 4, 0.5 s
 L=24: E₁ = 0.517638 (E₁·L = 12.4233), zero_modes = 4, 0.5 s
 L=32: E₁ = 0.390181 (E₁·L = 12.4858), zero_modes = 4, 0.8 s
 L=40: E₁ = 0.312869 (E₁·L = 12.5148), zero_modes = 4, 1.8 s
 L=48: E₁ = 0.261052 (E₁·L = 12.5305), zero_modes = 4, 3.9 s
 L=56: E₁ = 0.223929 (E₁·L = 12.5400), zero_modes = 4, 9.2 s
 L=64: E₁ = 0.196034 (E₁·L = 12.5462), zero_modes = 4, 19.8 s
 L=72: E₁ = 0.174311 (E₁·L = 12.5504), zero_modes = 4, 44.4 s
 L=80: E₁ = 0.156918 (E₁·L = 12.5535), zero_modes = 4, 83.8 s
 L=88: E₁ = 0.142678 (E₁·L = 12.5557), zero_modes = 4, 147.2 s
 L=96: E₁ = 0.130806 (E₁·L = 12.5574), zero_modes = 4, 277.7 s

 Fit: gap = 12.2188/L + 0.0054, R² = 0.999880, v_F = 1.9447 (π-flux target 2.0)
 E₁·L: mean = 12.5003, cv = 0.75% ≤ ✓ 5%
────────────────────────────────────────────────────────────
 R² > 0.95 (11 pts)   PASS — R² = 0.9999
 zero tower == 4 ∀L   PASS — |E| ≤ 1e-8 at every size
 E₁·L cv ≤ 5%         PASS — cv = 0.75% (Dirac law: E₁·L → 4π = const)
 Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
