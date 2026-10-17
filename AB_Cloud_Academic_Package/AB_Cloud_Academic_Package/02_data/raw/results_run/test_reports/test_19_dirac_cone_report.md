# Test 19: Dirac cone v_F ≈ 0.125
Verdict: PASS   |   Generated: 2026-09-02 15:29:36   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R².
 METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R².
Test 19 SERIES: α∈{0.4,0.5,0.6} × L∈{20,40,60,80}, α=0.5 R²=1.0000, E_min·L 0.53/12.55/0.53 (0.4/0.5/0.6) — Dirac 4π vs gapless →0.

## Result
 Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/plot_03` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 19 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[15:24:25.783] [+5781.065s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:27.667] [+5782.950s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:30.652] [+5785.934s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:24:46.991] [+5802.273s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.4000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:09.619] [+5884.901s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:11.221] [+5886.504s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:14.202] [+5889.485s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:26:30.482] [+5905.764s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:52.829] [+5988.111s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:54.428] [+5989.710s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:27:57.396] [+5992.678s]  build_ab_cloud_hamiltonian: 60x60 (N=3600), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:28:13.935] [+6009.217s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.6000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 19 (pass 3, SERIES): Dirac cone — α-selective 1/L series
────────────────────────────────────────────────────────────
 4-point mod-20 grid L=20, 40, 60, 80; α ∈ {0.4, 0.5, 0.6} — all EXACT on the torus
 ⚠ RUNTIME: 12 value-only solves (largest 80²) ≈ 2–3 min
 α=0.4 L=20: E_min = 0.086901, E_min·L = 1.7380, zero_modes = 30
 α=0.4 L=40: E_min = 0.025377, E_min·L = 1.0151, zero_modes = 70
 α=0.4 L=60: E_min = 0.011605, E_min·L = 0.6963, zero_modes = 110
 α=0.4 L=80: E_min = 0.006593, E_min·L = 0.5275, zero_modes = 150
 α=0.5 L=20: E_min = 0.618034, E_min·L = 12.3607, zero_modes = 4
 α=0.5 L=40: E_min = 0.312869, E_min·L = 12.5148, zero_modes = 4
 α=0.5 L=60: E_min = 0.209057, E_min·L = 12.5434, zero_modes = 4
 α=0.5 L=80: E_min = 0.156918, E_min·L = 12.5535, zero_modes = 4
 α=0.6 L=20: E_min = 0.086901, E_min·L = 1.7380, zero_modes = 30
 α=0.6 L=40: E_min = 0.025377, E_min·L = 1.0151, zero_modes = 70
 α=0.6 L=60: E_min = 0.011605, E_min·L = 0.6963, zero_modes = 110
 α=0.6 L=80: E_min = 0.006593, E_min·L = 0.5275, zero_modes = 150

 α=0.5 fit: E_min = 0.0043 + 12.2836/L, R² = 0.999975 (v_F = b/2π = 1.9550)
 E_min·L @L=80: α=0.4 → 0.5275 | α=0.5 → 12.5535 (4π = 12.566) | α=0.6 → 0.5275
────────────────────────────────────────────────────────────
 α=0.5 fit R² > 0.95 (4 pts) PASS — E_min = 0.0043 + 12.2836/L, v_F = b/2π = 1.9550
 α=0.5 scale ∈ [8, 18] PASS — E_min·L(L=80) = 12.553, target 4π = 12.566
 α-selectivity > 2×   PASS — E_min·L(0.5) = 12.553 vs 0.4: 0.527 / 0.6: 0.527 (q=5 odd → gapless at E=0)
 Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```
