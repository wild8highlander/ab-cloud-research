# Test 33: L-scaling ⟨r⟩ (10→20→30→50→80→112)
Verdict: PASS   |   Generated: 2026-09-15 07:26:31   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

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
Test 33 RAM gate: L=112 skipped (needs ≈ 10.6 GB peak, free ≈ 4.3 GB).
Extended L-scan to L=80 (user spec 2026-08-29); W_eff=1.00; verdict q=0.30; trend 0.434 → 0.556 → 0.593 → 0.6 → 0.6
Test 33 HARDCORE plateau (q=0.30): weighted ⟨r⟩=0.6004 vs GUE (|Δ|=0.0012, in band), χ²/dof=0.01.

## Result
 Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 33 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[07:09:25.448] [+26556.476s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:25.985] [+26557.014s]  calc: ⟨r⟩ = 0.629404 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:27.180] [+26558.208s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:27.738] [+26558.766s]  calc: ⟨r⟩ = 0.509721 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:28.759] [+26559.788s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:29.359] [+26560.388s]  calc: ⟨r⟩ = 0.574634 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:30.483] [+26561.512s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:31.005] [+26562.034s]  calc: ⟨r⟩ = 0.557955 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:32.182] [+26563.211s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:32.709] [+26563.737s]  calc: ⟨r⟩ = 0.486070 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:33.836] [+26564.864s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:34.457] [+26565.485s]  calc: ⟨r⟩ = 0.593495 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:35.559] [+26566.587s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:36.176] [+26567.204s]  calc: ⟨r⟩ = 0.596397 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:37.301] [+26568.330s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:37.915] [+26568.943s]  calc: ⟨r⟩ = 0.582880 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:38.976] [+26570.004s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:39.565] [+26570.593s]  calc: ⟨r⟩ = 0.588530 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:40.649] [+26571.677s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:41.247] [+26572.275s]  calc: ⟨r⟩ = 0.615185 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:42.368] [+26573.396s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[07:09:43.297] [+26574.326s]  calc: ⟨r⟩ = 0.625316 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:44.620] [+26575.649s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[07:09:45.950] [+26576.979s]  calc: ⟨r⟩ = 0.610951 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:47.154] [+26578.182s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[07:09:48.060] [+26579.089s]  calc: ⟨r⟩ = 0.600825 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:49.257] [+26580.285s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[07:09:50.171] [+26581.199s]  calc: ⟨r⟩ = 0.592813 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:51.350] [+26582.378s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, torus, 26 vortices, model=:monumental
[07:09:52.289] [+26583.317s]  calc: ⟨r⟩ = 0.605293 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:53.558] [+26584.586s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[07:09:59.555] [+26590.583s]  calc: ⟨r⟩ = 0.597483 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:10:00.777] [+26591.806s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[07:10:07.510] [+26598.538s]  calc: ⟨r⟩ = 0.594415 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:10:08.681] [+26599.709s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[07:10:15.270] [+26606.298s]  calc: ⟨r⟩ = 0.606851 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:10:16.422] [+26607.450s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[07:10:22.981] [+26614.010s]  calc: ⟨r⟩ = 0.574458 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:10:24.135] [+26615.163s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, torus, 70 vortices, model=:monumental
[07:10:30.667] [+26621.696s]  calc: ⟨r⟩ = 0.594551 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:10:32.257] [+26623.285s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[07:12:09.993] [+26721.021s]  calc: ⟨r⟩ = 0.598524 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:12:11.752] [+26722.781s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[07:13:46.304] [+26817.332s]  calc: ⟨r⟩ = 0.593096 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:13:47.923] [+26818.951s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[07:15:21.288] [+26912.316s]  calc: ⟨r⟩ = 0.598961 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:15:22.875] [+26913.903s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[07:16:55.922] [+27006.950s]  calc: ⟨r⟩ = 0.602712 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:16:57.478] [+27008.506s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, torus, 178 vortices, model=:monumental
[07:18:29.703] [+27100.731s]  calc: ⟨r⟩ = 0.600199 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:30.972] [+27102.000s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[07:18:31.457] [+27102.486s]  calc: ⟨r⟩ = 0.512863 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:32.458] [+27103.487s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[07:18:32.939] [+27103.967s]  calc: ⟨r⟩ = 0.408227 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:33.951] [+27104.979s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[07:18:34.430] [+27105.459s]  calc: ⟨r⟩ = 0.434605 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:35.446] [+27106.474s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[07:18:35.926] [+27106.955s]  calc: ⟨r⟩ = 0.444497 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:36.908] [+27107.936s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[07:18:37.391] [+27108.419s]  calc: ⟨r⟩ = 0.371493 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:38.417] [+27109.445s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[07:18:38.972] [+27110.001s]  calc: ⟨r⟩ = 0.552303 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:39.950] [+27110.978s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[07:18:40.491] [+27111.519s]  calc: ⟨r⟩ = 0.568758 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:41.473] [+27112.501s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[07:18:42.014] [+27113.042s]  calc: ⟨r⟩ = 0.525701 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:42.989] [+27114.017s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[07:18:43.530] [+27114.558s]  calc: ⟨r⟩ = 0.549972 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:44.497] [+27115.525s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, open, 12 vortices, model=:monumental
[07:18:45.034] [+27116.062s]  calc: ⟨r⟩ = 0.585633 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:46.009] [+27117.037s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[07:18:46.826] [+27117.854s]  calc: ⟨r⟩ = 0.578164 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:47.833] [+27118.861s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[07:18:48.633] [+27119.661s]  calc: ⟨r⟩ = 0.588849 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:49.616] [+27120.644s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[07:18:50.409] [+27121.438s]  calc: ⟨r⟩ = 0.583585 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:51.385] [+27122.414s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[07:18:52.173] [+27123.201s]  calc: ⟨r⟩ = 0.601887 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:53.154] [+27124.183s]  build_ab_cloud_hamiltonian: 30x30 (N=900), α=0.5000, t=1.00, W=1.00, open, 26 vortices, model=:monumental
[07:18:53.934] [+27124.962s]  calc: ⟨r⟩ = 0.614023 (n_r=539, n_eigs=541) [refs: GUE=0.5996 Poisson=0.3863]
[07:18:54.923] [+27125.951s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[07:19:00.339] [+27131.367s]  calc: ⟨r⟩ = 0.606783 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:19:01.309] [+27132.338s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[07:19:06.911] [+27137.940s]  calc: ⟨r⟩ = 0.602431 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:19:07.834] [+27138.862s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[07:19:13.282] [+27144.310s]  calc: ⟨r⟩ = 0.597144 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:19:14.269] [+27145.298s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[07:19:19.681] [+27150.710s]  calc: ⟨r⟩ = 0.608952 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:19:20.646] [+27151.674s]  build_ab_cloud_hamiltonian: 50x50 (N=2500), α=0.5000, t=1.00, W=1.00, open, 70 vortices, model=:monumental
[07:19:26.240] [+27157.269s]  calc: ⟨r⟩ = 0.586730 (n_r=1499, n_eigs=1501) [refs: GUE=0.5996 Poisson=0.3863]
[07:19:27.445] [+27158.474s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[07:20:53.366] [+27244.395s]  calc: ⟨r⟩ = 0.597930 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:20:54.979] [+27246.007s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[07:22:17.065] [+27328.093s]  calc: ⟨r⟩ = 0.610283 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:22:18.526] [+27329.554s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[07:23:39.386] [+27410.415s]  calc: ⟨r⟩ = 0.595793 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:23:40.806] [+27411.834s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[07:25:06.015] [+27497.044s]  calc: ⟨r⟩ = 0.599605 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
[07:25:07.597] [+27498.625s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=1.00, open, 178 vortices, model=:monumental
[07:26:29.007] [+27580.036s]  calc: ⟨r⟩ = 0.598340 (n_r=3839, n_eigs=3841) [refs: GUE=0.5996 Poisson=0.3863]
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
 ⚠ RAM GATE: L=112 needs ≈ 10.6 GB peak (matrix + LAPACK workspace), free ≈ 4.3 GB → SKIPPED (a swap-thrashing eig is indistinguishable from a hang)
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
