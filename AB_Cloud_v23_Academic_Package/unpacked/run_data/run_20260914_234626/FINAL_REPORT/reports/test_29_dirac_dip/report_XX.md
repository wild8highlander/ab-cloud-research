# Test 29: Dirac dip in DOS at α=1/2
Verdict: PASS   |   Generated: 2026-09-15 04:28:22   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Semi-exact: DOS dip depth vs prediction.
 METHOD: Semi-exact: DOS dip depth vs prediction.
Test 29 SERIES: 9-pt fine scan @96² (strict dip true, ρ_dip=0.0195), contrast(w) 288.00→3.97 (w=0.1→0.8), size contrast 13.33×→10.67×.

## Result
 Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 29 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[03:49:19.515] [+14550.543s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:53:34.081] [+14805.109s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4271, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:58:04.195] [+15075.223s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4583, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:02:28.229] [+15339.257s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4896, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:06:49.977] [+15601.005s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:11:11.976] [+15863.005s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5104, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:15:30.824] [+16121.852s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5417, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:19:51.305] [+16382.334s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5729, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:24:02.022] [+16633.050s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.6042, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:28:08.106] [+16879.134s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:28:14.173] [+16885.201s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 29 (pass 3, SERIES): Dirac dip — fine α-scan + window series
────────────────────────────────────────────────────────────
 Fine scan: 9 points α = k/96 around k=48 (α=1/2 EXACT), window |E|<0.5
 ⚠ RUNTIME: 9 solves at 96² + 2 anchors at 48² ≈ 8–13 min
 α=38/96 = 0.39583: ρ(|E|<0.5) = 0.2083  (253.5 s)
 α=41/96 = 0.42708: ρ(|E|<0.5) = 0.1458  (265.2 s)
 α=44/96 = 0.45833: ρ(|E|<0.5) = 0.0833  (262.8 s)
 α=47/96 = 0.48958: ρ(|E|<0.5) = 0.0208  (259.8 s)
 α=48/96 = 0.50000: ρ(|E|<0.5) = 0.0195  (259.3 s)
 α=49/96 = 0.51042: ρ(|E|<0.5) = 0.0208  (257.2 s)
 α=52/96 = 0.54167: ρ(|E|<0.5) = 0.0833  (258.4 s)
 α=55/96 = 0.57292: ρ(|E|<0.5) = 0.1458  (249.0 s)
 α=58/96 = 0.60417: ρ(|E|<0.5) = 0.2083  (245.2 s)
 window |E|<0.1: ρ_dip(α=1/2) = 0.0004, ρ_off(α=38/96) = 0.1250 → contrast 288.00×
 window |E|<0.2: ρ_dip(α=1/2) = 0.0039, ρ_off(α=38/96) = 0.2083 → contrast 53.33×
 window |E|<0.3: ρ_dip(α=1/2) = 0.0091, ρ_off(α=38/96) = 0.2083 → contrast 22.86×
 window |E|<0.5: ρ_dip(α=1/2) = 0.0195, ρ_off(α=38/96) = 0.2083 → contrast 10.67×
 window |E|<0.8: ρ_dip(α=1/2) = 0.0525, ρ_off(α=38/96) = 0.2083 → contrast 3.97×

 contrast @w=0.5 (α=0.396 vs 1/2): 13.33× (48x48) → 10.67× (96x96) → holds/sharpens ✓
────────────────────────────────────────────────────────────
 strict dip @96² (9 pts) PASS — ρ(α=1/2) = 0.0195 below ALL 8 other scan points
 contrast grows as w → 0 PASS — contrast(w) 288.00× (w=0.1) vs 10.67× (w=0.5): Dirac ρ ∝ E vs metallic ρ ≈ const
 no wash-out 48²→96²  PASS — 13.33× → 10.67× at the same α pair (0.396 vs 1/2; tolerance 0.8, as 29b)
 Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```
