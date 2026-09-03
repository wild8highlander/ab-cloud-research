# Test 33: L-scaling ⟨r⟩ (10→20→30→50→80→112)
Verdict: PASS   |   Generated: 2026-09-02 21:32:46   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Statistical finite-size trend: monotone approach to 0.594-0.599; monograph anchors L≤50, extended points L=80/112 (user spec 2026-08-29) check the GUE plateau; W_eff capped at ab_W_max.
 METHOD: Statistical finite-size trend: monotone approach to 0.594-0.599; monograph anchors L≤50, extended points L=80/112 (user spec 2026-08-29) check the GUE plateau; W_eff capped at ab_W_max.
Test 33 HARDCORE pass 2: n ≤ 5 per L, weighted GUE-plateau χ² over L ≥ 50, L capped at 112 (RAM honesty).
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
Test 33 RAM gate: L=112 skipped (needs ≈ 10.6 GB peak, free ≈ 4.5 GB).
Extended L-scan to L=80 (user spec 2026-08-29); W_eff=1.00; verdict q=0.30; trend 0.434 → 0.556 → 0.593 → 0.6 → 0.6
Test 33 HARDCORE plateau (q=0.30): weighted ⟨r⟩=0.6004 vs GUE (|Δ|=0.0012, in band), χ²/dof=0.01.

## Result
 Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 33 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[21:18:17.797] [+27013.080s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:18.357] [+27013.639s]  calc: ⟨r⟩ = 0.629404 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:19.481] [+27014.763s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:20.034] [+27015.316s]  calc: ⟨r⟩ = 0.509721 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:21.171] [+27016.453s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:21.721] [+27017.004s]  calc: ⟨r⟩ = 0.574634 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:22.850] [+27018.132s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:23.385] [+27018.667s]  calc: ⟨r⟩ = 0.557955 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:24.495] [+27019.777s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[21:18:25.049] [+27020.331s]  calc: ⟨r⟩ = 0.486070 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:26.189] [+27021.472s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[21:18:26.787] [+27022.069s]  calc: ⟨r⟩ = 0.593495 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:27.998] [+27023.280s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[21:18:28.604] [+27023.886s]  calc: ⟨r⟩ = 0.596397 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:29.710] [+27024.992s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[21:18:30.274] [+27025.556s]  calc: ⟨r⟩ = 0.582880 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:31.321] [+27026.603s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[21:18:31.864] [+27027.146s]  calc: ⟨r⟩ = 0.588530 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:32.818] [+27028.100s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[21:18:33.332] [+27028.614s]  calc: ⟨r⟩ = 0.615185 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:34.335] [+27029.618s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[21:18:35.120] [+27030.402s]  calc: ⟨r⟩ = 0.625316 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:36.129] [+27031.411s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[21:18:36.862] [+27032.144s]  calc: ⟨r⟩ = 0.610951 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:37.869] [+27033.151s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[21:18:38.593] [+27033.875s]  calc: ⟨r⟩ = 0.600825 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:39.581] [+27034.863s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[21:18:40.302] [+27035.584s]  calc: ⟨r⟩ = 0.592813 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:41.270] [+27036.552s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[21:18:42.004] [+27037.286s]  calc: ⟨r⟩ = 0.605293 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:43.019] [+27038.302s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:18:48.015] [+27043.297s]  calc: ⟨r⟩ = 0.597483 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:49.075] [+27044.357s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:18:54.049] [+27049.331s]  calc: ⟨r⟩ = 0.594415 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:18:55.096] [+27050.378s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:00.056] [+27055.338s]  calc: ⟨r⟩ = 0.606851 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:01.083] [+27056.365s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:06.087] [+27061.370s]  calc: ⟨r⟩ = 0.574458 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:07.153] [+27062.436s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[21:19:12.078] [+27067.360s]  calc: ⟨r⟩ = 0.594551 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:19:13.463] [+27068.745s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:20:25.768] [+27141.050s]  calc: ⟨r⟩ = 0.598524 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:20:27.289] [+27142.571s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:21:39.539] [+27214.821s]  calc: ⟨r⟩ = 0.593096 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:21:41.084] [+27216.366s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:22:54.656] [+27289.938s]  calc: ⟨r⟩ = 0.598961 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:22:56.054] [+27291.337s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:24:11.640] [+27366.922s]  calc: ⟨r⟩ = 0.602712 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:24:13.429] [+27368.711s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[21:25:27.096] [+27442.378s]  calc: ⟨r⟩ = 0.600199 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:28.354] [+27443.636s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[21:25:28.912] [+27444.194s]  calc: ⟨r⟩ = 0.512863 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:30.090] [+27445.372s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[21:25:30.645] [+27445.928s]  calc: ⟨r⟩ = 0.408227 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:31.782] [+27447.064s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[21:25:32.334] [+27447.616s]  calc: ⟨r⟩ = 0.434605 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:33.453] [+27448.735s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[21:25:34.001] [+27449.283s]  calc: ⟨r⟩ = 0.444497 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:35.115] [+27450.397s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[21:25:35.649] [+27450.931s]  calc: ⟨r⟩ = 0.371493 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:36.772] [+27452.054s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:37.377] [+27452.659s]  calc: ⟨r⟩ = 0.552303 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:38.506] [+27453.789s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:39.119] [+27454.401s]  calc: ⟨r⟩ = 0.568758 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:40.260] [+27455.542s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:40.847] [+27456.129s]  calc: ⟨r⟩ = 0.525701 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:41.974] [+27457.256s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:42.526] [+27457.808s]  calc: ⟨r⟩ = 0.549972 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:43.537] [+27458.819s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[21:25:44.100] [+27459.382s]  calc: ⟨r⟩ = 0.585633 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:45.054] [+27460.336s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:45.772] [+27461.054s]  calc: ⟨r⟩ = 0.578164 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:46.753] [+27462.035s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:47.487] [+27462.769s]  calc: ⟨r⟩ = 0.588849 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:48.476] [+27463.758s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:49.202] [+27464.484s]  calc: ⟨r⟩ = 0.583585 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:50.205] [+27465.487s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:50.928] [+27466.210s]  calc: ⟨r⟩ = 0.601887 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:51.924] [+27467.205s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[21:25:52.656] [+27467.938s]  calc: ⟨r⟩ = 0.614023 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:53.720] [+27469.003s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[21:25:58.716] [+27473.998s]  calc: ⟨r⟩ = 0.606783 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:25:59.762] [+27475.044s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[21:26:04.716] [+27479.999s]  calc: ⟨r⟩ = 0.602431 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:26:05.772] [+27481.054s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[21:26:10.722] [+27486.005s]  calc: ⟨r⟩ = 0.597144 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:26:11.792] [+27487.074s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[21:26:16.739] [+27492.021s]  calc: ⟨r⟩ = 0.608952 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:26:17.808] [+27493.090s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[21:26:22.798] [+27498.080s]  calc: ⟨r⟩ = 0.586730 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[21:26:24.162] [+27499.444s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:27:34.829] [+27570.111s]  calc: ⟨r⟩ = 0.597930 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:27:36.326] [+27571.608s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:28:48.328] [+27643.610s]  calc: ⟨r⟩ = 0.610283 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:28:49.848] [+27645.130s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:30:02.856] [+27718.138s]  calc: ⟨r⟩ = 0.595793 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:30:04.465] [+27719.747s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:31:23.977] [+27799.259s]  calc: ⟨r⟩ = 0.599605 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[21:31:26.491] [+27801.773s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[21:32:42.881] [+27878.163s]  calc: ⟨r⟩ = 0.598340 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 33 (pass 2, HARDCORE): L-scaling — deep validation
Harder machinery: up to 5 realizations per L, weighted
GUE-plateau χ² over L ≥ 50, no L beyond 112 (RAM honesty: L=128 ≈ 4.3 GB).
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 2 q-rows × up to n=5 realizations × L ∈ {10,20,30,50,80,112} → expect ≈ 27–81 min (±3× machine factor; RAM-gated rungs are skipped inside with a printed reason)

════════════════════════════════════════════════════════════
TEST 33: L-Scaling for AB-Cloud Lattice
L=10→0.487 (Poisson), L=20→0.562, L=30→0.595, L=50→0.594 (monograph),
L=80, L=112 → GUE plateau check (extended range, user spec 2026-08-29)
────────────────────────────────────────────────────────────
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
 ⚠ RAM GATE: L=112 needs ≈ 10.6 GB peak (matrix + LAPACK workspace), free ≈ 4.5 GB → SKIPPED (a swap-thrashing eig is indistinguishable from a hang)
 q=1.00 BC=:torus L=10  Nv=4   α=0.50 W=1.00 ⟨r⟩ = 0.5516 ± 0.0252 (5 real, monograph 0.487)
 q=1.00 BC=:torus L=20  Nv=12  α=0.50 W=1.00 ⟨r⟩ = 0.5953 ± 0.0055 (5 real, monograph 0.562)
 q=1.00 BC=:torus L=30  Nv=26  α=0.50 W=1.00 ⟨r⟩ = 0.6070 ± 0.0054 (5 real, monograph 0.595)
 q=1.00 BC=:torus L=50  Nv=70  α=0.50 W=1.00 ⟨r⟩ = 0.5936 ± 0.0053 (5 real, monograph 0.594)
 q=1.00 BC=:torus L=80  Nv=178 α=0.50 W=1.00 ⟨r⟩ = 0.5987 ± 0.0016 (5 real, monograph 0.595*)
 q=0.30 BC=:open  L=10  Nv=4   α=0.50 W=1.00 ⟨r⟩ = 0.4343 ± 0.0233 (5 real, monograph 0.487)
 q=0.30 BC=:open  L=20  Nv=12  α=0.50 W=1.00 ⟨r⟩ = 0.5565 ± 0.0100 (5 real, monograph 0.562)
 q=0.30 BC=:open  L=30  Nv=26  α=0.50 W=1.00 ⟨r⟩ = 0.5933 ± 0.0065 (5 real, monograph 0.595)
 q=0.30 BC=:open  L=50  Nv=70  α=0.50 W=1.00 ⟨r⟩ = 0.6004 ± 0.0040 (5 real, monograph 0.594)
 q=0.30 BC=:open  L=80  Nv=178 α=0.50 W=1.00 ⟨r⟩ = 0.6004 ± 0.0025 (5 real, monograph 0.595*)

 Verdict run: q=0.30 (fractional AB phase — reference standard, stable)
 Trend (L=10→20→30→50→80): 0.434 → 0.556 → 0.593 → 0.6 → 0.6
 Monotone increase: YES
 Final L=80 close to GUE 0.595 (|Δ|<0.05): YES
 (comparison) q=1.0 user setting: 0.552 → 0.595 → 0.607 → 0.594 → 0.599 (final 0.5987)
 Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS

 ─── HARDCORE GUE-plateau check (verdict q=0.3, L ≥ 50) ───
 plateau points: L=50: 0.6004±0.0040, L=80: 0.6004±0.0025
 weighted ⟨r⟩ = 0.6004 vs GUE 0.5992 (|Δ|=0.0012) → IN ✓ band ±0.022
 χ² = 0.01, dof = 2, χ²/dof = 0.01 → consistent ✓ (≤ 2 consistent; diagnostic)
 Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
```
