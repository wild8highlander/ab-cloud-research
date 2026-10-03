# FINAL REPORT — AB-Cloud v23 SUPERCOMBO — interactive session
Generated: 2026-09-16 01:48:55   |   Julia 1.12.0   |   wall duration: 93748.1 s (1562.5 min)   |   Suite: AB-Cloud v20
Author: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701) | DOI 10.5281/zenodo.21825394 | github.com/wild8highlander/research-papers

## What this folder is
FINAL_REPORT is the LAST folder of the run and gathers ALL run information: the master report (this document, in md/html/pdf/docx) — which since v23.5 EMBEDS every test's full report inline (see 'Full per-test reports' below), so the whole run reads from ONE document — and the consolidated ONE-FILE log logs/full_run_log.txt (every test's computation log + console capture). Raw copies of every test's report files (reports/) and logs (logs/) are kept as before; heavy plot artifacts (png/gif) stay in each test's own folder ../test_XX_<slug>/plots/ — the per-test tables below point there.

## How to reproduce
Full suite:        julia ab_cloud_v20.jl --test all
Single test:       julia ab_cloud_v20.jl --test 33 --no-two-pass
Disorder cap:      --ab-w-max 1.0   (Tests 32/33/36 use W_eff = min(ab_W, W_max))
Test 36 targets:   --ab37-n-eigs-pass1 25000 --ab37-n-eigs-pass2 50000
Labs: main menu 'l' (Physics Lab), 'd3' (3D Lab); every experiment writes its own report into the same run folder.

## Configuration snapshot (end-of-run values)

```text
zeros_count           = 50000  (source: auto)
lattice primary       = 72x72  Nv=[4]  q=[1.0]
lattice secondary     = 96x96  Nv=[2]  (two-pass=true, primary-only=false)
third pass (SERIES)   = true  (Tests 19/29/31 → 19c/29c/31c series; Test 19 also runs pass 4 → 19d twist AUDIT)
alpha                 = ab_alpha=0.5, ab_alpha_test16=0.5
disorder              = ab_W=4, ab_W_max=1  → W_eff(Tests 32/33/36)=1.00
test33 comparison row = W_cmp=0.50, Nv_cmp=144
realizations          = ab_n_realizations=5, center_fraction=0.6
byte robustness       = tol=0.02, n_bytes=200000, seed=12345, T37 targets: pass1=25000 / pass2=50000 eigs
lab                   = L=72, α=0.5, W=4, q=1, Nv=4, random/torus/monumental, seed=12345
3d                    = L=20, α=0.5, tz=1, W=0, mass=0, boundary=:torus, lines=0 q=1, seed=777
reporting             = enabled=true, dir=results, dpi=600, formats=md,html,pdf,docx
```

## Verdicts — 79 tests: 66 PASS, 0 WARN, 13 FAIL, 0 DONE
Test 1   [PASS] bN_convergence —  Test 1: b(N=50000) = 1.2126 → PASS
Test 1   [PASS] bN_convergence —  Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2: Monotonicity violations: 0 / 499 → PASS
Test 2   [PASS] bN_monotonicity —  Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 3   [PASS] bN_rate —  Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
Test 3   [PASS] bN_rate —  Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 4   [FAIL] gue_ks_full —  Test 4: KS D=0.0216, p=0.0 → WARN
Test 4   [PASS] gue_ks_full —  Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 5   [FAIL] gue_ks_highT —  Test 5: Best high-T p-value=0.0 → WARN
Test 5   [PASS] gue_ks_highT —  Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 6   [FAIL] chi2_hist —  Test 6: χ² p=0.0 → WARN
Test 6   [PASS] chi2_hist —  Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 7   [PASS] decay_slope —  Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
Test 7   [PASS] decay_slope —  Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 8   [PASS] residuals —  Test 8: Runs=3 (exp=5.8) → PASS
Test 8   [PASS] residuals —  Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 9   [PASS] bootstrap_ci —  Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
Test 9   [PASS] bootstrap_ci —  Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 10  [PASS] cross_validation —  Test 10: Max deviation=8.5% → PASS
Test 10  [PASS] cross_validation —  Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
Test 11  [FAIL] anderson_darling —  Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
Test 11  [PASS] anderson_darling —  Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 12  [FAIL] two_sample_ks —  Test 12: 2-sample KS D=0.0265, p=0.005252 → WARN
Test 12  [FAIL] two_sample_ks —  Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
Test 13  [PASS] number_variance —  Test 13: data closer to GUE in 9/9 L-values → PASS
Test 13  [PASS] number_variance —  Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 14  [PASS] spectral_rigidity —  Test 14: data closer to GUE in 9/9 L-values → PASS
Test 14  [PASS] spectral_rigidity —  Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 15  [PASS] ab_construction —  Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
Test 15  [PASS] ab_construction —  Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 16  [PASS] ab_gue_class —  Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
Test 16  [PASS] ab_gue_class —  Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 17  [PASS] connes_self_duality —  Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
Test 17  [PASS] connes_self_duality —  Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 18  [PASS] chiral_AIII —  Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
Test 18  [PASS] chiral_AIII —  Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
Test 19  [PASS] dirac_cone —  Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 19  [PASS] dirac_cone —  Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS
Test 20  [PASS] chern_tknn —  Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
Test 20  [PASS] chern_tknn —  Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 21  [PASS] gamma_phase —  Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
Test 21  [PASS] gamma_phase —  Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 22  [PASS] ab_phase —  Test 22: Φ_AB=0.4487989505 = π/7 (exact) → PASS
Test 22  [PASS] ab_phase —  Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 23  [PASS] fractal_factor —  Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
Test 23  [PASS] fractal_factor —  Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 24  [PASS] dirac_string_flux —  Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
Test 24  [PASS] dirac_string_flux —  Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
Test 25  [PASS] byers_yang —  Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
Test 25  [PASS] byers_yang —  Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 26  [PASS] pbc_torus —  Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
Test 26  [PASS] pbc_torus —  Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 27  [FAIL] binary_chiral — EXCEPTION: UndefVarError: `R_POISSON` not defined in `Main`
Suggestion: check for spelling errors or missing imports.
Test 27  [PASS] binary_chiral —  Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS
Test 28  [FAIL] f_gue_merit —  Test 28: f_GUE=0.881, Σ²_data=0.6115 → WARN
Test 28  [FAIL] f_gue_merit —  Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
Test 29  [FAIL] dirac_dip —  Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
Test 29  [PASS] dirac_dip —  Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
Test 30  [PASS] vf_scaling —  Test 30: v_F=1.798, R²=0.9977 → PASS
Test 30  [PASS] vf_scaling —  Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
Test 31  [PASS] hatano_nelson —  Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 31  [PASS] hatano_nelson —  Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
Test 32  [PASS] rmean_bootstrap —  Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
Test 33  [PASS] l_scaling_rmean —  Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
Test 34  [PASS] direct_vs_zeta —  Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
Test 34  [FAIL] direct_vs_zeta —  Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
Test 35  [FAIL] form_factor_Kt —  Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
Test 36  [PASS] byte_robust —  Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37: (1/2)!=√π/2 [rel.err 0.0], 32/π² [rel.err 0.0], ∫p₂=1 [|Δ|=0.0], uniqueness ✓ → PASS
Test 37  [PASS] half_factorial_gamma —  Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
Test 38  [PASS] curie_point —  Test 38 (v23 three-pass) t38: PASS · Curie 3-pass (72²+96²+38c) — 486.9 min, 346 spectra in cache

## Execution steps (computation-log section markers)

```text
[23:46:49.053] [+  0.081s] ▸ run_all_tests START
[23:46:49.141] [+  0.170s] ▸ Test 1 — pass 1 (primary: standard implementation)
[23:46:50.101] [+  1.129s]  pass 1 result: PASS (elapsed: 0.96s)
[23:46:50.101] [+  1.129s] ▸ Test 1 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:47:03.102] [+ 14.130s]  pass 2 result: PASS (elapsed: 13.00s)
[23:47:03.102] [+ 14.130s]  Test 1 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:47:03.751] [+ 14.779s] ▸ Test 2 — pass 1 (primary: standard implementation)
[23:47:14.727] [+ 25.755s]  pass 1 result: PASS (elapsed: 10.98s)
[23:47:14.727] [+ 25.755s] ▸ Test 2 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:47:20.626] [+ 31.654s]  pass 2 result: PASS (elapsed: 5.90s)
[23:47:20.626] [+ 31.654s]  Test 2 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:47:21.277] [+ 32.305s] ▸ Test 3 — pass 1 (primary: standard implementation)
[23:47:21.598] [+ 32.627s]  pass 1 result: PASS (elapsed: 0.32s)
[23:47:21.598] [+ 32.627s] ▸ Test 3 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:47:27.415] [+ 38.443s]  pass 2 result: PASS (elapsed: 5.82s)
[23:47:27.415] [+ 38.444s]  Test 3 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:47:28.065] [+ 39.093s] ▸ Test 4 — pass 1 (primary: standard implementation)
[23:52:57.704] [+368.732s]  pass 1 result: FAIL/WARN (elapsed: 329.64s)
[23:52:57.704] [+368.733s] ▸ Test 4 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:06.749] [+377.777s]  pass 2 result: PASS (elapsed: 9.04s)
[23:53:06.749] [+377.778s]  Test 4 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[23:53:08.419] [+379.447s] ▸ Test 5 — pass 1 (primary: standard implementation)
[23:53:09.153] [+380.181s]  pass 1 result: FAIL/WARN (elapsed: 0.73s)
[23:53:09.153] [+380.182s] ▸ Test 5 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:14.150] [+385.178s]  pass 2 result: PASS (elapsed: 5.00s)
[23:53:14.150] [+385.178s]  Test 5 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[23:53:14.998] [+386.026s] ▸ Test 6 — pass 1 (primary: standard implementation)
[23:53:15.580] [+386.609s]  pass 1 result: FAIL/WARN (elapsed: 0.58s)
[23:53:15.581] [+386.609s] ▸ Test 6 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:20.392] [+391.421s]  pass 2 result: PASS (elapsed: 4.81s)
[23:53:20.392] [+391.421s]  Test 6 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[23:53:21.221] [+392.249s] ▸ Test 7 — pass 1 (primary: standard implementation)
[23:53:21.563] [+392.591s]  pass 1 result: PASS (elapsed: 0.34s)
[23:53:21.563] [+392.591s] ▸ Test 7 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:28.609] [+399.637s]  pass 2 result: PASS (elapsed: 7.05s)
[23:53:28.609] [+399.637s]  Test 7 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:53:29.433] [+400.462s] ▸ Test 8 — pass 1 (primary: standard implementation)
[23:53:29.703] [+400.731s]  pass 1 result: PASS (elapsed: 0.27s)
[23:53:29.703] [+400.731s] ▸ Test 8 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:36.917] [+407.945s]  pass 2 result: PASS (elapsed: 7.21s)
[23:53:36.917] [+407.945s]  Test 8 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:53:37.821] [+408.849s] ▸ Test 9 — pass 1 (primary: standard implementation)
[23:53:38.031] [+409.059s]  pass 1 result: PASS (elapsed: 0.21s)
[23:53:38.031] [+409.059s] ▸ Test 9 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:44.802] [+415.831s]  pass 2 result: PASS (elapsed: 6.77s)
[23:53:44.803] [+415.831s]  Test 9 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:53:45.593] [+416.622s] ▸ Test 10 — pass 1 (primary: standard implementation)
[23:53:46.068] [+417.096s]  pass 1 result: PASS (elapsed: 0.47s)
[23:53:46.068] [+417.096s] ▸ Test 10 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:53:53.027] [+424.056s]  pass 2 result: PASS (elapsed: 6.96s)
[23:53:53.027] [+424.056s]  Test 10 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:53:53.811] [+424.839s] ▸ Test 11 — pass 1 (primary: standard implementation)
[23:55:18.654] [+509.682s]  pass 1 result: FAIL/WARN (elapsed: 84.84s)
[23:55:18.654] [+509.682s] ▸ Test 11 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:56:58.575] [+609.604s]  pass 2 result: PASS (elapsed: 99.92s)
[23:56:58.575] [+609.604s]  Test 11 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[23:56:59.260] [+610.289s] ▸ Test 12 — pass 1 (primary: standard implementation)
[23:56:59.394] [+610.422s]  pass 1 result: FAIL/WARN (elapsed: 0.13s)
[23:56:59.394] [+610.422s] ▸ Test 12 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:57:03.401] [+614.429s]  pass 2 result: FAIL/WARN (elapsed: 4.01s)
[23:57:03.401] [+614.429s]  Test 12 two-pass summary: pass1=FAIL pass2=FAIL (hardcore) → OVERALL FAIL
[23:57:04.082] [+615.110s] ▸ Test 13 — pass 1 (primary: standard implementation)
[23:57:04.357] [+615.385s]  pass 1 result: PASS (elapsed: 0.27s)
[23:57:04.357] [+615.385s] ▸ Test 13 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:57:10.480] [+621.508s]  pass 2 result: PASS (elapsed: 6.12s)
[23:57:10.480] [+621.508s]  Test 13 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:57:11.199] [+622.227s] ▸ Test 14 — pass 1 (primary: standard implementation)
[23:57:11.705] [+622.733s]  pass 1 result: PASS (elapsed: 0.51s)
[23:57:11.705] [+622.733s] ▸ Test 14 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[23:57:18.173] [+629.201s]  pass 2 result: PASS (elapsed: 6.47s)
[23:57:18.173] [+629.201s]  Test 14 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[23:57:18.882] [+629.910s] ▸ Test 15 — pass 1 (primary: 72×72, Nv=[4])
[23:57:22.443] [+633.472s]  pass 1 result: PASS (elapsed: 3.56s)
[23:57:22.444] [+633.472s] ▸ Test 15 — pass 2 (secondary: 96×96, Nv=[2])
[23:57:36.325] [+647.353s]  pass 2 result: PASS (elapsed: 13.88s)
[23:57:36.325] [+647.353s]  Test 15 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[23:57:37.019] [+648.047s] ▸ Test 16 — pass 1 (primary: 72×72, Nv=[4])
[23:57:37.289] [+648.317s] ▸ Test 16 single-α: α=0.500000 (α=0.5000 (default))
[00:00:52.674] [+843.702s]  pass 1 result: PASS (elapsed: 195.66s)
[00:00:52.674] [+843.702s] ▸ Test 16 — pass 2 (secondary: 96×96, Nv=[2])
[00:25:09.091] [+2300.119s]  pass 2 result: PASS (elapsed: 1456.42s)
[00:25:09.091] [+2300.119s]  Test 16 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[00:25:10.161] [+2301.189s] ▸ Test 17 — pass 1 (primary: 72×72, Nv=[4])
[00:32:11.010] [+2722.038s]  pass 1 result: PASS (elapsed: 420.85s)
[00:32:11.010] [+2722.039s] ▸ Test 17 — pass 2 (secondary: 96×96, Nv=[2])
[00:55:53.775] [+4144.804s]  pass 2 result: PASS (elapsed: 1422.76s)
[00:55:53.777] [+4144.805s]  Test 17 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[00:55:58.273] [+4149.301s] ▸ Test 18 — pass 1 (primary: 72×72, Nv=[4])
[01:00:13.907] [+4404.936s]  pass 1 result: PASS (elapsed: 255.63s)
[01:00:13.908] [+4404.936s] ▸ Test 18 — pass 2 (secondary: 96×96, Nv=[2])
[01:01:22.413] [+4473.442s]  pass 2 result: PASS (elapsed: 68.51s)
[01:01:22.413] [+4473.442s]  Test 18 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:01:23.562] [+4474.590s] ▸ Test 19 — pass 1 (primary: 72×72, Nv=[4])
[01:03:00.683] [+4571.711s]  pass 1 result: PASS (elapsed: 97.12s)
[01:03:00.683] [+4571.711s] ▸ Test 19 — pass 2 (secondary: 96×96, Nv=[2])
[01:16:29.739] [+5380.767s]  pass 2 result: PASS (elapsed: 809.06s)
[01:16:29.739] [+5380.768s] ▸ Test 19 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[01:23:43.291] [+5814.319s] ▸ Test 19 — pass 4 (quaternary: AUDIT — twist spectroscopy + eigenvector index, 96×96 regime)
[01:25:00.806] [+5891.834s] ▸ Test 20 — pass 1 (primary: 72×72, Nv=[4])
[01:25:01.663] [+5892.692s]  pass 1 result: PASS (elapsed: 0.86s)
[01:25:01.664] [+5892.692s] ▸ Test 20 — pass 2 (secondary: 96×96, Nv=[2])
[01:25:29.607] [+5920.635s]  pass 2 result: PASS (elapsed: 27.94s)
[01:25:29.607] [+5920.635s]  Test 20 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:25:30.660] [+5921.689s] ▸ Test 21 — pass 1 (primary: 72×72, Nv=[4])
[01:25:31.071] [+5922.099s]  pass 1 result: PASS (elapsed: 0.41s)
[01:25:31.071] [+5922.099s] ▸ Test 21 — pass 2 (secondary: 96×96, Nv=[2])
[01:25:40.268] [+5931.297s]  pass 2 result: PASS (elapsed: 9.20s)
[01:25:40.268] [+5931.297s]  Test 21 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:25:41.304] [+5932.332s] ▸ Test 22 — pass 1 (primary: 72×72, Nv=[4])
[01:25:41.570] [+5932.599s]  pass 1 result: PASS (elapsed: 0.27s)
[01:25:41.571] [+5932.599s] ▸ Test 22 — pass 2 (secondary: 96×96, Nv=[2])
[01:25:50.745] [+5941.774s]  pass 2 result: PASS (elapsed: 9.17s)
[01:25:50.745] [+5941.774s]  Test 22 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:25:51.801] [+5942.829s] ▸ Test 23 — pass 1 (primary: 72×72, Nv=[4])
[01:25:52.306] [+5943.334s]  pass 1 result: PASS (elapsed: 0.51s)
[01:25:52.306] [+5943.334s] ▸ Test 23 — pass 2 (secondary: 96×96, Nv=[2])
[01:26:01.167] [+5952.195s]  pass 2 result: PASS (elapsed: 8.86s)
[01:26:01.167] [+5952.195s]  Test 23 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:26:02.205] [+5953.233s] ▸ Test 24 — pass 1 (primary: 72×72, Nv=[4])
[01:26:04.492] [+5955.520s]  pass 1 result: PASS (elapsed: 2.29s)
[01:26:04.492] [+5955.520s] ▸ Test 24 — pass 2 (secondary: 96×96, Nv=[2])
[01:26:53.431] [+6004.459s]  pass 2 result: PASS (elapsed: 48.94s)
[01:26:53.431] [+6004.459s]  Test 24 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[01:26:54.375] [+6005.403s] ▸ Test 25 — pass 1 (primary: 72×72, Nv=[4])
[01:29:45.658] [+6176.686s]  pass 1 result: PASS (elapsed: 171.28s)
[01:29:45.658] [+6176.687s] ▸ Test 25 — pass 2 (secondary: 96×96, Nv=[2])
[02:34:42.641] [+10073.669s]  pass 2 result: PASS (elapsed: 3896.98s)
[02:34:42.641] [+10073.669s]  Test 25 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[02:34:43.847] [+10074.876s] ▸ Test 26 — pass 1 (primary: 72×72, Nv=[4])
[02:35:51.050] [+10142.078s]  pass 1 result: PASS (elapsed: 67.20s)
[02:35:51.050] [+10142.078s] ▸ Test 26 — pass 2 (secondary: 96×96, Nv=[2])
[03:07:11.089] [+12022.117s]  pass 2 result: PASS (elapsed: 1880.04s)
[03:07:11.089] [+12022.117s]  Test 26 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[03:07:12.359] [+12023.387s] ▸ Test 27 — pass 1 (primary: 72×72, Nv=[4])
[03:07:30.520] [+12041.549s]  pass 1 result: FAIL/WARN (elapsed: 18.16s)
[03:07:30.520] [+12041.549s] ▸ Test 27 — pass 2 (secondary: 96×96, Nv=[2])
[03:10:06.429] [+12197.457s]  pass 2 result: PASS (elapsed: 155.91s)
[03:10:06.429] [+12197.457s]  Test 27 two-pass summary: pass1=FAIL pass2=PASS → OVERALL FAIL
[03:10:07.363] [+12198.391s] ▸ Test 28 — pass 1 (primary: 72×72, Nv=[4])
[03:10:53.830] [+12244.858s]  pass 1 result: FAIL/WARN (elapsed: 46.47s)
[03:10:53.830] [+12244.859s] ▸ Test 28 — pass 2 (secondary: 96×96, Nv=[2])
[03:33:32.361] [+13603.389s]  pass 2 result: FAIL/WARN (elapsed: 1358.53s)
[03:33:32.361] [+13603.389s]  Test 28 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[03:33:33.339] [+13604.367s] ▸ Test 29 — pass 1 (primary: 72×72, Nv=[4])
[03:35:42.492] [+13733.520s]  pass 1 result: PASS (elapsed: 129.15s)
[03:35:42.492] [+13733.520s] ▸ Test 29 — pass 2 (secondary: 96×96, Nv=[2])
[03:49:18.967] [+14549.996s]  pass 2 result: FAIL/WARN (elapsed: 816.48s)
[03:49:18.968] [+14549.996s] ▸ Test 29 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[04:28:43.626] [+16914.654s] ▸ Test 30 — pass 1 (primary: 72×72, Nv=[4])
[04:30:03.314] [+16994.342s]  pass 1 result: PASS (elapsed: 79.69s)
[04:30:03.314] [+16994.342s] ▸ Test 30 — pass 2 (secondary: 96×96, Nv=[2])
[04:40:31.149] [+17622.177s]  pass 2 result: PASS (elapsed: 627.83s)
[04:40:31.149] [+17622.178s]  Test 30 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[04:40:32.099] [+17623.127s] ▸ Test 31 — pass 1 (primary: 72×72, Nv=[4])
[04:43:47.935] [+17818.964s]  pass 1 result: PASS (elapsed: 195.84s)
[04:43:47.936] [+17818.964s] ▸ Test 31 — pass 2 (secondary: 96×96, Nv=[2])
[05:25:20.799] [+20311.827s]  pass 2 result: PASS (elapsed: 2492.86s)
[05:25:20.799] [+20311.827s] ▸ Test 31 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[05:30:07.638] [+20598.666s] ▸ Test 32 — pass 1 (primary: 72×72, Nv=[4])
[05:37:37.908] [+21048.937s]  pass 1 result: PASS (elapsed: 450.27s)
[05:37:37.909] [+21048.937s] ▸ Test 32 — pass 2 (secondary: 96×96, Nv=[2])
[06:47:24.642] [+25235.670s]  pass 2 result: PASS (elapsed: 4186.73s)
[06:47:24.642] [+25235.671s]  Test 32 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[06:47:25.815] [+25236.844s] ▸ Test 33 — pass 1 (primary: 72×72, Nv=[4])
[07:09:25.403] [+26556.431s]  pass 1 result: PASS (elapsed: 1319.59s)
[07:09:25.404] [+26556.432s] ▸ Test 33 — pass 2 (secondary: 96×96, Nv=[2])
[07:26:40.230] [+27591.258s]  pass 2 result: PASS (elapsed: 1034.83s)
[07:26:40.230] [+27591.258s]  Test 33 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[07:26:41.241] [+27592.269s] ▸ Test 34 — pass 1 (primary: 72×72, Nv=[4])
[07:30:23.296] [+27814.324s]  pass 1 result: PASS (elapsed: 222.06s)
[07:30:23.296] [+27814.324s] ▸ Test 34 — pass 2 (secondary: 96×96, Nv=[2])
[07:52:07.208] [+29118.237s]  pass 2 result: FAIL/WARN (elapsed: 1303.91s)
[07:52:07.209] [+29118.237s]  Test 34 two-pass summary: pass1=PASS pass2=FAIL → OVERALL FAIL
[07:52:08.147] [+29119.176s] ▸ Test 35 — pass 1 (primary: 72×72, Nv=[4])
[07:55:51.681] [+29342.709s]  pass 1 result: FAIL/WARN (elapsed: 223.53s)
[07:55:51.681] [+29342.709s] ▸ Test 35 — pass 2 (secondary: 96×96, Nv=[2])
[08:18:03.989] [+30675.017s]  pass 2 result: FAIL/WARN (elapsed: 1332.31s)
[08:18:03.989] [+30675.017s]  Test 35 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[08:18:04.978] [+30676.007s] ▸ Test 36 — pass 1 (primary: 72×72, Nv=[4])
[08:25:15.606] [+31106.634s]  pass 1 result: PASS (elapsed: 430.63s)
[08:25:15.607] [+31106.636s] ▸ Test 36 — pass 2 (secondary: 96×96, Nv=[2])
[09:08:55.777] [+33726.806s]  pass 2 result: PASS (elapsed: 2620.17s)
[09:08:55.778] [+33726.806s]  Test 36 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[09:08:56.803] [+33727.831s] ▸ Test 37 — pass 1 (primary: 72×72, Nv=[4])
[09:09:07.239] [+33738.267s]  pass 1 result: PASS (elapsed: 10.44s)
[09:09:07.239] [+33738.267s] ▸ Test 37 — pass 2 (secondary: 96×96, Nv=[2])
[09:09:14.797] [+33745.826s]  pass 2 result: PASS (elapsed: 7.56s)
[09:09:14.797] [+33745.826s]  Test 37 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[09:09:15.732] [+33746.760s] ▸ Test 38 — pass 1 (primary: 72×72, Nv=[4])
[17:16:11.648] [+61287.429s]  pass 1 result: PASS (elapsed: 27540.67s)
```

## Artifact map

```text
test_01_bN_convergence [PASS]  reports/ + logs/ copied; plots live in ../test_01_bN_convergence/plots/
test_01_bN_convergence [PASS]  reports/ + logs/ copied; plots live in ../test_01_bN_convergence/plots/
test_02_bN_monotonicity [PASS]  reports/ + logs/ copied; plots live in ../test_02_bN_monotonicity/plots/
test_02_bN_monotonicity [PASS]  reports/ + logs/ copied; plots live in ../test_02_bN_monotonicity/plots/
test_03_bN_rate        [PASS]  reports/ + logs/ copied; plots live in ../test_03_bN_rate/plots/
test_03_bN_rate        [PASS]  reports/ + logs/ copied; plots live in ../test_03_bN_rate/plots/
test_04_gue_ks_full    [FAIL]  reports/ + logs/ copied; plots live in ../test_04_gue_ks_full/plots/
test_04_gue_ks_full    [PASS]  reports/ + logs/ copied; plots live in ../test_04_gue_ks_full/plots/
test_05_gue_ks_highT   [FAIL]  reports/ + logs/ copied; plots live in ../test_05_gue_ks_highT/plots/
test_05_gue_ks_highT   [PASS]  reports/ + logs/ copied; plots live in ../test_05_gue_ks_highT/plots/
test_06_chi2_hist      [FAIL]  reports/ + logs/ copied; plots live in ../test_06_chi2_hist/plots/
test_06_chi2_hist      [PASS]  reports/ + logs/ copied; plots live in ../test_06_chi2_hist/plots/
test_07_decay_slope    [PASS]  reports/ + logs/ copied; plots live in ../test_07_decay_slope/plots/
test_07_decay_slope    [PASS]  reports/ + logs/ copied; plots live in ../test_07_decay_slope/plots/
test_08_residuals      [PASS]  reports/ + logs/ copied; plots live in ../test_08_residuals/plots/
test_08_residuals      [PASS]  reports/ + logs/ copied; plots live in ../test_08_residuals/plots/
test_09_bootstrap_ci   [PASS]  reports/ + logs/ copied; plots live in ../test_09_bootstrap_ci/plots/
test_09_bootstrap_ci   [PASS]  reports/ + logs/ copied; plots live in ../test_09_bootstrap_ci/plots/
test_10_cross_validation [PASS]  reports/ + logs/ copied; plots live in ../test_10_cross_validation/plots/
test_10_cross_validation [PASS]  reports/ + logs/ copied; plots live in ../test_10_cross_validation/plots/
test_11_anderson_darling [FAIL]  reports/ + logs/ copied; plots live in ../test_11_anderson_darling/plots/
test_11_anderson_darling [PASS]  reports/ + logs/ copied; plots live in ../test_11_anderson_darling/plots/
test_12_two_sample_ks  [FAIL]  reports/ + logs/ copied; plots live in ../test_12_two_sample_ks/plots/
test_12_two_sample_ks  [FAIL]  reports/ + logs/ copied; plots live in ../test_12_two_sample_ks/plots/
test_13_number_variance [PASS]  reports/ + logs/ copied; plots live in ../test_13_number_variance/plots/
test_13_number_variance [PASS]  reports/ + logs/ copied; plots live in ../test_13_number_variance/plots/
test_14_spectral_rigidity [PASS]  reports/ + logs/ copied; plots live in ../test_14_spectral_rigidity/plots/
test_14_spectral_rigidity [PASS]  reports/ + logs/ copied; plots live in ../test_14_spectral_rigidity/plots/
test_15_ab_construction [PASS]  reports/ + logs/ copied; plots live in ../test_15_ab_construction/plots/
test_15_ab_construction [PASS]  reports/ + logs/ copied; plots live in ../test_15_ab_construction/plots/
test_16_ab_gue_class   [PASS]  reports/ + logs/ copied; plots live in ../test_16_ab_gue_class/plots/
test_16_ab_gue_class   [PASS]  reports/ + logs/ copied; plots live in ../test_16_ab_gue_class/plots/
test_17_connes_self_duality [PASS]  reports/ + logs/ copied; plots live in ../test_17_connes_self_duality/plots/
test_17_connes_self_duality [PASS]  reports/ + logs/ copied; plots live in ../test_17_connes_self_duality/plots/
test_18_chiral_AIII    [PASS]  reports/ + logs/ copied; plots live in ../test_18_chiral_AIII/plots/
test_18_chiral_AIII    [PASS]  reports/ + logs/ copied; plots live in ../test_18_chiral_AIII/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_19_dirac_cone     [PASS]  reports/ + logs/ copied; plots live in ../test_19_dirac_cone/plots/
test_20_chern_tknn     [PASS]  reports/ + logs/ copied; plots live in ../test_20_chern_tknn/plots/
test_20_chern_tknn     [PASS]  reports/ + logs/ copied; plots live in ../test_20_chern_tknn/plots/
test_21_gamma_phase    [PASS]  reports/ + logs/ copied; plots live in ../test_21_gamma_phase/plots/
test_21_gamma_phase    [PASS]  reports/ + logs/ copied; plots live in ../test_21_gamma_phase/plots/
test_22_ab_phase       [PASS]  reports/ + logs/ copied; plots live in ../test_22_ab_phase/plots/
test_22_ab_phase       [PASS]  reports/ + logs/ copied; plots live in ../test_22_ab_phase/plots/
test_23_fractal_factor [PASS]  reports/ + logs/ copied; plots live in ../test_23_fractal_factor/plots/
test_23_fractal_factor [PASS]  reports/ + logs/ copied; plots live in ../test_23_fractal_factor/plots/
test_24_dirac_string_flux [PASS]  reports/ + logs/ copied; plots live in ../test_24_dirac_string_flux/plots/
test_24_dirac_string_flux [PASS]  reports/ + logs/ copied; plots live in ../test_24_dirac_string_flux/plots/
test_25_byers_yang     [PASS]  reports/ + logs/ copied; plots live in ../test_25_byers_yang/plots/
test_25_byers_yang     [PASS]  reports/ + logs/ copied; plots live in ../test_25_byers_yang/plots/
test_26_pbc_torus      [PASS]  reports/ + logs/ copied; plots live in ../test_26_pbc_torus/plots/
test_26_pbc_torus      [PASS]  reports/ + logs/ copied; plots live in ../test_26_pbc_torus/plots/
test_27_binary_chiral  [FAIL]  reports/ + logs/ copied; plots live in ../test_27_binary_chiral/plots/
test_27_binary_chiral  [PASS]  reports/ + logs/ copied; plots live in ../test_27_binary_chiral/plots/
test_28_f_gue_merit    [FAIL]  reports/ + logs/ copied; plots live in ../test_28_f_gue_merit/plots/
test_28_f_gue_merit    [FAIL]  reports/ + logs/ copied; plots live in ../test_28_f_gue_merit/plots/
test_29_dirac_dip      [PASS]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_29_dirac_dip      [FAIL]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_29_dirac_dip      [PASS]  reports/ + logs/ copied; plots live in ../test_29_dirac_dip/plots/
test_30_vf_scaling     [PASS]  reports/ + logs/ copied; plots live in ../test_30_vf_scaling/plots/
test_30_vf_scaling     [PASS]  reports/ + logs/ copied; plots live in ../test_30_vf_scaling/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_31_hatano_nelson  [PASS]  reports/ + logs/ copied; plots live in ../test_31_hatano_nelson/plots/
test_32_rmean_bootstrap [PASS]  reports/ + logs/ copied; plots live in ../test_32_rmean_bootstrap/plots/
test_32_rmean_bootstrap [PASS]  reports/ + logs/ copied; plots live in ../test_32_rmean_bootstrap/plots/
test_33_l_scaling_rmean [PASS]  reports/ + logs/ copied; plots live in ../test_33_l_scaling_rmean/plots/
test_33_l_scaling_rmean [PASS]  reports/ + logs/ copied; plots live in ../test_33_l_scaling_rmean/plots/
test_34_direct_vs_zeta [PASS]  reports/ + logs/ copied; plots live in ../test_34_direct_vs_zeta/plots/
test_34_direct_vs_zeta [FAIL]  reports/ + logs/ copied; plots live in ../test_34_direct_vs_zeta/plots/
test_35_form_factor_Kt [FAIL]  reports/ + logs/ copied; plots live in ../test_35_form_factor_Kt/plots/
test_35_form_factor_Kt [FAIL]  reports/ + logs/ copied; plots live in ../test_35_form_factor_Kt/plots/
test_36_byte_robust    [PASS]  reports/ + logs/ copied; plots live in ../test_36_byte_robust/plots/
test_36_byte_robust    [PASS]  reports/ + logs/ copied; plots live in ../test_36_byte_robust/plots/
test_37_half_factorial_gamma [PASS]  reports/ + logs/ copied; plots live in ../test_37_half_factorial_gamma/plots/
test_37_half_factorial_gamma [PASS]  reports/ + logs/ copied; plots live in ../test_37_half_factorial_gamma/plots/
test_38_curie_point    [PASS]  reports/ + logs/ copied; plots live in ../test_38_curie_point/plots/
```
Log files: logs/full_run_log.txt (THE consolidated log: every test's computation log + console capture in one file), logs/computation_log.txt / computation_log_full.txt (every computation), logs/results_verdicts.txt (one-line verdicts), logs/test_XX_*/ (per-test).
Run index: ../index.html — verdict table with direct links to every per-test report.

## Full per-test reports (gathered inline — one-file read of the whole run)
Every test's full report (method, verdict-table content, plot list, verification guide) is embedded below in run order. Computation logs and console captures are consolidated separately in logs/full_run_log.txt — the run's single log file (user request 2026-09-06: everything readable from two files: this report + that log).
# Test 1 — bN_convergence   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:46:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.
 METHOD: b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.

## Result
 Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 1 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 1 — bN_convergence   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:46:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.
 METHOD: b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.

## Result
 Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 1 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 2 — bN_monotonicity   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:47:15   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).
 METHOD: Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).

## Result
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 2 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 2 — bN_monotonicity   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:47:15   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).
 METHOD: Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).

## Result
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 2 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 3 — bN_rate   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:47:21   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.
 METHOD: log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.

## Result
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 3 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 3 — bN_rate   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:47:21   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.
 METHOD: log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.

## Result
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 3 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 4 — gue_ks_full   [FAIL]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 4 — gue_ks_full   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 5 — gue_ks_highT   [FAIL]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 5 — gue_ks_highT   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 6 — chi2_hist   [FAIL]
Verdict: PASS   |   Generated: 2026-09-14 23:53:15   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.
 METHOD: χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.

## Result
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 6 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 6 — chi2_hist   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:15   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.
 METHOD: χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.

## Result
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 6 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 7 — decay_slope   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:21   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².
 METHOD: Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².

## Result
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 7 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 7 — decay_slope   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:21   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².
 METHOD: Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².

## Result
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 7 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 8 — residuals   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:29   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Residual structure of the log-log fit — algebraic diagnostics.
 METHOD: Residual structure of the log-log fit — algebraic diagnostics.

## Result
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 8 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 8 — residuals   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:29   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Residual structure of the log-log fit — algebraic diagnostics.
 METHOD: Residual structure of the log-log fit — algebraic diagnostics.

## Result
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 8 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 9 — bootstrap_ci   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:38   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Sampling-noise quantification: statistical system with CIs.
 METHOD: Sampling-noise quantification: statistical system with CIs.

## Result
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 9 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 9 — bootstrap_ci   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:38   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Sampling-noise quantification: statistical system with CIs.
 METHOD: Sampling-noise quantification: statistical system with CIs.

## Result
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 9 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 10 — cross_validation   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical stability of the fit under data splits.
 METHOD: Statistical stability of the fit under data splits.

## Result
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 10 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 10 — cross_validation   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:53:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical stability of the fit under data splits.
 METHOD: Statistical stability of the fit under data splits.

## Result
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 10 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 11 — anderson_darling   [FAIL]
Verdict: PASS   |   Generated: 2026-09-14 23:56:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)
 METHOD: Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)

## Result
 Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 11 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 11 — anderson_darling   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:56:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)
 METHOD: Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)

## Result
 Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 11 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 12 — two_sample_ks   [FAIL]
Verdict: FAIL   |   Generated: 2026-09-14 23:56:59   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Two-sample KS: data vs simulated GUE matrix spectrum.
 METHOD: Two-sample KS: data vs simulated GUE matrix spectrum.

## Result
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 12 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 12 — two_sample_ks   [FAIL]
Verdict: FAIL   |   Generated: 2026-09-14 23:56:59   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Two-sample KS: data vs simulated GUE matrix spectrum.
 METHOD: Two-sample KS: data vs simulated GUE matrix spectrum.

## Result
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 12 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 13 — number_variance   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:04   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.
 METHOD: Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.

## Result
 Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 13 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 13 — number_variance   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:04   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.
 METHOD: Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.

## Result
 Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 13 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 14 — spectral_rigidity   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:12   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Δ₃(L) long-range rigidity vs GUE universal prediction.
 METHOD: Δ₃(L) long-range rigidity vs GUE universal prediction.

## Result
 Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 14 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 14 — spectral_rigidity   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:12   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Δ₃(L) long-range rigidity vs GUE universal prediction.
 METHOD: Δ₃(L) long-range rigidity vs GUE universal prediction.

## Result
 Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 14 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 15 — ab_construction   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:32   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
 METHOD: Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
Test 15 HARDCORE: full plaquette scan 96x96 (±-quartet), signed flux 4/4, empty 9021/9021, worst empty flux 0.00e+00.

## Result
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 15 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 15 — ab_construction   [PASS]
Verdict: PASS   |   Generated: 2026-09-14 23:57:32   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
 METHOD: Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
Test 15 HARDCORE: full plaquette scan 96x96 (±-quartet), signed flux 4/4, empty 9021/9021, worst empty flux 0.00e+00.

## Result
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 15 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 16 — ab_gue_class   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 00:24:43   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
 METHOD: Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
Test 16 HARDCORE pass 2: 96x96, n=5 realizations at α=0.5000, Nv=2, q=1.000, W_eff=1.00, ensemble deep checks (bootstrap CI, scatter, sign count).
Test 16 HARDCORE: ⟨r⟩=0.5798±0.0037 (n=5), bootstrap CI [0.5732,0.5859] misses GUE, scatter σ=0.0082.

## Result
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 16 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 16 — ab_gue_class   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 00:24:43   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
 METHOD: Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
Test 16 HARDCORE pass 2: 96x96, n=5 realizations at α=0.5000, Nv=2, q=1.000, W_eff=1.00, ensemble deep checks (bootstrap CI, scatter, sign count).
Test 16 HARDCORE: ⟨r⟩=0.5798±0.0037 (n=5), bootstrap CI [0.5732,0.5859] misses GUE, scatter σ=0.0082.

## Result
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 16 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 17 — connes_self_duality   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 00:55:45   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: isospectrality under α ↔ 1/α to machine precision.
 METHOD: EXACT: isospectrality under α ↔ 1/α to machine precision.
Test 17 HARDCORE L=24: zero_modes(α=1/2)=4, spectral defects 1.42e-15/1.66e-15, duality defect 3.62e-01.
Test 17 HARDCORE L=48: zero_modes(α=1/2)=4, spectral defects 2.90e-15/2.41e-15, duality defect 3.65e-01.
Test 17 HARDCORE L=96: zero_modes(α=1/2)=4, spectral defects 3.96e-15/3.24e-15, duality defect 3.66e-01.

## Result
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 17 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 17 — connes_self_duality   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 00:55:45   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: isospectrality under α ↔ 1/α to machine precision.
 METHOD: EXACT: isospectrality under α ↔ 1/α to machine precision.
Test 17 HARDCORE L=24: zero_modes(α=1/2)=4, spectral defects 1.42e-15/1.66e-15, duality defect 3.62e-01.
Test 17 HARDCORE L=48: zero_modes(α=1/2)=4, spectral defects 2.90e-15/2.41e-15, duality defect 3.65e-01.
Test 17 HARDCORE L=96: zero_modes(α=1/2)=4, spectral defects 3.96e-15/3.24e-15, duality defect 3.66e-01.

## Result
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 17 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 18 — chiral_AIII   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:01:13   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
 METHOD: EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
Test 18 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058, in window), vortex 0.00e+00 (preserved), S²=I 0.00e+00 (96x96 torus).

## Result
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 18 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 18 — chiral_AIII   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:01:13   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
 METHOD: EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
Test 18 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058, in window), vortex 0.00e+00 (preserved), S²=I 0.00e+00 (96x96 torus).

## Result
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 18 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 19 — dirac_cone   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:24:34   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
 METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
Test 19 AUDIT: v_F_twist = 1.9990 (R² = 1.00000, L=48 y-twist scan), tower 4 @1e-10 with 2+2 polarization, 2π-holonomy 2.5e-17, π-cusp 6.279, rebuild bit-exact, 1/L² intercept 12.5662, cross-pass spread 5.09%.

## Result
 Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 19 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 19 — dirac_cone   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:24:34   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
 METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
Test 19 AUDIT: v_F_twist = 1.9990 (R² = 1.00000, L=48 y-twist scan), tower 4 @1e-10 with 2+2 polarization, 2π-holonomy 2.5e-17, π-cusp 6.279, rebuild bit-exact, 1/L² intercept 12.5662, cross-pass spread 5.09%.

## Result
 Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 19 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 19 — dirac_cone   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:24:34   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
 METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
Test 19 AUDIT: v_F_twist = 1.9990 (R² = 1.00000, L=48 y-twist scan), tower 4 @1e-10 with 2+2 polarization, 2π-holonomy 2.5e-17, π-cusp 6.279, rebuild bit-exact, 1/L² intercept 12.5662, cross-pass spread 5.09%.

## Result
 Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 19 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 19 — dirac_cone   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:24:34   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
 METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%).
Test 19 AUDIT: v_F_twist = 1.9990 (R² = 1.00000, L=48 y-twist scan), tower 4 @1e-10 with 2+2 polarization, 2π-holonomy 2.5e-17, π-cusp 6.279, rebuild bit-exact, 1/L² intercept 12.5662, cross-pass spread 5.09%.

## Result
 Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 19 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 20 — chern_tknn   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:02   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
 METHOD: EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
Test 20 HARDCORE: anchors 1/4,1/3,1/5 → +1 ✓; ladder 12..72 → 1,1,1,1,1,1; α=1/2 touching ∀L, mass branch 0 ✓.

## Result
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_05.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 20 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 20 — chern_tknn   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:02   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
 METHOD: EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
Test 20 HARDCORE: anchors 1/4,1/3,1/5 → +1 ✓; ladder 12..72 → 1,1,1,1,1,1; α=1/2 touching ∀L, mass branch 0 ✓.

## Result
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_05.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 20 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 21 — gamma_phase   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:31   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT geometric phase check.
 METHOD: EXACT geometric phase check.
Test 21 HARDCORE: 256-bit a_C err 1.23e-19, b_C err 6.39e-17, arg dev 0.1259°, δ±1e-6 worst dev 0.1259°.

## Result
 Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 21 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 21 — gamma_phase   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:31   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT geometric phase check.
 METHOD: EXACT geometric phase check.
Test 21 HARDCORE: 256-bit a_C err 1.23e-19, b_C err 6.39e-17, arg dev 0.1259°, δ±1e-6 worst dev 0.1259°.

## Result
 Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 21 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 22 — ab_phase   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:42   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT flux-phase identity.
 METHOD: EXACT flux-phase identity.
Test 22 HARDCORE: 256-bit rational identity true, Float64 err 1.75e-17, flux linearity p=1..3 true.

## Result
 Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 22 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 22 — ab_phase   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:42   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT flux-phase identity.
 METHOD: EXACT flux-phase identity.
Test 22 HARDCORE: 256-bit rational identity true, Float64 err 1.75e-17, flux linearity p=1..3 true.

## Result
 Test 22b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 22 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 23 — fractal_factor   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Log-periodic factor — semi-statistical curve comparison.
 METHOD: Log-periodic factor — semi-statistical curve comparison.
Test 23 HARDCORE: |CF|−1 = 0.00e+00 (256-bit), β err 3.04e-16 (Float64) / 3.28e-05 (LaTeX), c_AB err 6.82e-06.

## Result
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 23 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 23 — fractal_factor   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:25:52   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Log-periodic factor — semi-statistical curve comparison.
 METHOD: Log-periodic factor — semi-statistical curve comparison.
Test 23 HARDCORE: |CF|−1 = 0.00e+00 (256-bit), β err 3.04e-16 (Float64) / 3.28e-05 (LaTeX), c_AB err 6.82e-06.

## Result
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 23 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 24 — dirac_string_flux   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:26:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
 METHOD: EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
Test 24 HARDCORE: 4-config full scan on 96x96, worst empty flux 8.88e-16, hermiticity true.

## Result
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 24 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 24 — dirac_string_flux   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 01:26:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
 METHOD: EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
Test 24 HARDCORE: 4-config full scan on 96x96, worst empty flux 8.88e-16, hermiticity true.

## Result
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 24 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 25 — byers_yang   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 02:34:35   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
 METHOD: EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
Test 25 HARDCORE: Byers-Yang Δ<1e-10 for 3 layouts × q∈{+1,+2,−1} on 96x96 → true; fractional q∈{0.3,0.5} Δ>1e-3 → true.

## Result
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 25 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 25 — byers_yang   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 02:34:35   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
 METHOD: EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
Test 25 HARDCORE: Byers-Yang Δ<1e-10 for 3 layouts × q∈{+1,+2,−1} on 96x96 → true; fractional q∈{0.3,0.5} Δ>1e-3 → true.

## Result
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 25 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 26 — pbc_torus   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 03:07:01   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
 METHOD: Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
Test 26 HARDCORE pass 2: 96x96 torus, exhaustive artifact classification, n=5 ⟨r⟩ realizations at W_eff=1.00.
Test 26 HARDCORE: artifacts 9024 clean/0 wrap/0 unexplained; ⟨r⟩=0.5964±0.0021, scatter σ=0.0046.

## Result
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 26 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 26 — pbc_torus   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 03:07:01   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
 METHOD: Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
Test 26 HARDCORE pass 2: 96x96 torus, exhaustive artifact classification, n=5 ⟨r⟩ realizations at W_eff=1.00.
Test 26 HARDCORE: artifacts 9024 clean/0 wrap/0 unexplained; ⟨r⟩=0.5964±0.0021, scatter σ=0.0046.

## Result
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 26 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 27 — binary_chiral   [FAIL]
Verdict: PASS   |   Generated: 2026-09-15 03:09:45   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification.
 METHOD: EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification.
Test 27 ζ-DEEP (50k): pairing exact on the 100000-dim dictionary, ⟨r⟩ 0.6119 (GUE 0.5996), Poisson control 0.3864, block spread 0.0050, KS D_GUE 0.0216 vs D_GOE 0.0881.
Test 27 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058), vortex 0.00e+00 (preserved), Coulomb W-scan 0.101→0.746 (ratio 7.42), ε-floor W-independent.

## Result
 Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 27 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 27 — binary_chiral   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 03:09:45   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification.
 METHOD: EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification.
Test 27 ζ-DEEP (50k): pairing exact on the 100000-dim dictionary, ⟨r⟩ 0.6119 (GUE 0.5996), Poisson control 0.3864, block spread 0.0050, KS D_GUE 0.0216 vs D_GOE 0.0881.
Test 27 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058), vortex 0.00e+00 (preserved), Coulomb W-scan 0.101→0.746 (ratio 7.42), ε-floor W-independent.

## Result
 Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 27 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 28 — f_gue_merit   [FAIL]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 28 — f_gue_merit   [FAIL]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 29 — dirac_dip   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 29 — dirac_dip   [FAIL]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 29 — dirac_dip   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 30 — vf_scaling   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 30 — vf_scaling   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 31 — hatano_nelson   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 05:29:51   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
 METHOD: Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
Test 31 SERIES: n=5 realizations × σ∈{0.5,0.6,0.7,0.8} @48x48, n_cx mean 0,2225,2281,2295, ⟨r⟩ 0.8953→0.9253, max|Im| 0.3184→0.9576.

## Result
 Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 31 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 31 — hatano_nelson   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 05:29:51   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
 METHOD: Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
Test 31 SERIES: n=5 realizations × σ∈{0.5,0.6,0.7,0.8} @48x48, n_cx mean 0,2225,2281,2295, ⟨r⟩ 0.8953→0.9253, max|Im| 0.3184→0.9576.

## Result
 Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 31 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 31 — hatano_nelson   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 05:29:51   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
 METHOD: Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern.
Test 31 SERIES: n=5 realizations × σ∈{0.5,0.6,0.7,0.8} @48x48, n_cx mean 0,2225,2281,2295, ⟨r⟩ 0.8953→0.9253, max|Im| 0.3184→0.9576.

## Result
 Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_04.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 31 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 32 — rmean_bootstrap   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 06:47:18   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion.
 METHOD: Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion.
Test 32 HARDCORE pass 2: 96x96, n≥5 per row, comparison-row Nv=256 (anchor density), ensemble deep checks (bootstrap CI, scatter, sign count).
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
Effective disorder: W_eff = 1.00 = min(ab_W=4.00, ab_W_max=1.00); disorder energy q·W_eff = 1.00 vs hopping t = 1.0
Comparison row q=0.300: W_row=0.50, Nv_row=256 → ⟨r⟩=0.6012 ± 0.0015; nearest class GUE (d_GOE=0.0705, d_GUE=0.0016, d_Poi=0.2149); vortex density 2.78% vs monograph anchor 2.78%.
Test 32 HARDCORE row q=1.000: n=5, bootstrap CI [0.5838, 0.5892] misses GUE; scatter σ=0.0034 (within band).
Test 32 HARDCORE row q=0.300: n=5, bootstrap CI [0.5999, 0.6026] misses GUE; scatter σ=0.0017 (within band).

## Result
 Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 32 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 32 — rmean_bootstrap   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 06:47:18   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion.
 METHOD: Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion.
Test 32 HARDCORE pass 2: 96x96, n≥5 per row, comparison-row Nv=256 (anchor density), ensemble deep checks (bootstrap CI, scatter, sign count).
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
Effective disorder: W_eff = 1.00 = min(ab_W=4.00, ab_W_max=1.00); disorder energy q·W_eff = 1.00 vs hopping t = 1.0
Comparison row q=0.300: W_row=0.50, Nv_row=256 → ⟨r⟩=0.6012 ± 0.0015; nearest class GUE (d_GOE=0.0705, d_GUE=0.0016, d_Poi=0.2149); vortex density 2.78% vs monograph anchor 2.78%.
Test 32 HARDCORE row q=1.000: n=5, bootstrap CI [0.5838, 0.5892] misses GUE; scatter σ=0.0034 (within band).
Test 32 HARDCORE row q=0.300: n=5, bootstrap CI [0.5999, 0.6026] misses GUE; scatter σ=0.0017 (within band).

## Result
 Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 32 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 33 — l_scaling_rmean   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 33 — l_scaling_rmean   [PASS]
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
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 34 — direct_vs_zeta   [PASS]
Verdict: FAIL   |   Generated: 2026-09-15 07:51:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
 METHOD: Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
Test 34 HARDCORE pass 2: n=5 realizations, R₂ ds=0.05/s_max=4.0, per-realization KS stability.
Test 34 HARDCORE: D=0.1096 (p=2.236e-186), per-real D med 0.1153 (spread 0.0923..0.1189), ⟨|ΔR₂|⟩=0.0002, d_GUE=0.8764.

## Result
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 34 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 34 — direct_vs_zeta   [FAIL]
Verdict: FAIL   |   Generated: 2026-09-15 07:51:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
 METHOD: Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
Test 34 HARDCORE pass 2: n=5 realizations, R₂ ds=0.05/s_max=4.0, per-realization KS stability.
Test 34 HARDCORE: D=0.1096 (p=2.236e-186), per-real D med 0.1153 (spread 0.0923..0.1189), ⟨|ΔR₂|⟩=0.0002, d_GUE=0.8764.

## Result
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 34 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 35 — form_factor_Kt   [FAIL]
Verdict: FAIL   |   Generated: 2026-09-15 08:17:49   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
 METHOD: Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
Test 35 HARDCORE pass 2: n=5 per-realization K(t), 33-point t-grid, ensemble mean verdict.
Test 35 HARDCORE: ensemble RMS=0.6143, corr_box=0.6379, corr_ζ=0.8123, RMS scatter σ=0.1856.

## Result
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 35 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 35 — form_factor_Kt   [FAIL]
Verdict: FAIL   |   Generated: 2026-09-15 08:17:49   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
 METHOD: Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
Test 35 HARDCORE pass 2: n=5 per-realization K(t), 33-point t-grid, ensemble mean verdict.
Test 35 HARDCORE: ensemble RMS=0.6143, corr_box=0.6379, corr_ζ=0.8123, RMS scatter σ=0.1856.

## Result
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 35 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 36 — byte_robust   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 09:08:55   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max.
 METHOD: Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max.
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
Sample: 55290 eigs (pass 2 (secondary), target 50000, reached=yes); W_eff=1.00.
Byte robustness verdict = multi-window |Δ⟨r⟩|=0.0009 (tol 0.0200, 120 windows); single-window |Δr|=0.0061 (diagnostic).

## Result
 Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS

## Plots
(no plots queued by this pass — physics series live in the HARDCORE pass-2 report: hc_verdict_table queues a sub-check verdict map there, and the deep-audit tests queue their own scan charts; the retired stdout scraper no longer fabricates filler charts)

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 36 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 36 — byte_robust   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 09:08:55   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max.
 METHOD: Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max.
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
Sample: 55290 eigs (pass 2 (secondary), target 50000, reached=yes); W_eff=1.00.
Byte robustness verdict = multi-window |Δ⟨r⟩|=0.0009 (tol 0.0200, 120 windows); single-window |Δr|=0.0061 (diagnostic).

## Result
 Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS

## Plots
(no plots queued by this pass — physics series live in the HARDCORE pass-2 report: hc_verdict_table queues a sub-check verdict map there, and the deep-audit tests queue their own scan charts; the retired stdout scraper no longer fabricates filler charts)

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 36 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 37 — half_factorial_gamma   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 09:09:07   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
 METHOD: EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
Test 37 HARDCORE: 256-bit DE Γ(1/2) err 1.20e-28, Float64 round-off Γ(1/2) 5.83e-16 / (1/2)! 2.94e-16, N=32/π² err 2.51e-26, ladder/self-dual/recurrence exact.

## Result
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 37 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 37 — half_factorial_gamma   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 09:09:07   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
 METHOD: EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
Test 37 HARDCORE: 256-bit DE Γ(1/2) err 1.20e-28, Float64 round-off Γ(1/2) 5.83e-16 / (1/2)! 2.94e-16, N=32/π² err 2.51e-26, ladder/self-dual/recurrence exact.

## Result
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 37 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
# Test 38 — curie_point   [PASS]
Verdict: PASS   |   Generated: 2026-09-15 17:16:11   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
STATISTICAL+EXACT (v22.2 three-pass rewrite): order parameter Λ(T)=⟨ln[p_GUE(s)/p_GOE(s)]⟩ — the KL lean — on Chebyshev-unfolded spacings of a paired-realization vortex-flux lattice; Debye–Waller thermal screening w(T)=exp(−σ1·T/2) melts the TRS-breaking flux. 38a main curve + V1 p-value-grade sampler calibration; 38b hardcore lattice (A1..A7, exact negative controls: no-flux, static dephasing); 38c reviewer ladder C1..C5 (density scan, Binder/FSS staircase 24→96, shared-curve disclosure, refine bound, crossover terminology). Spectrum cache (CSV, resumable), --t38-cap budget, six-panel journal figure. T*(L) is a finite-L crossover scale (half-decay convention).
 METHOD: STATISTICAL+EXACT (v22.2 three-pass rewrite): order parameter Λ(T)=⟨ln[p_GUE(s)/p_GOE(s)]⟩ — the KL lean — on Chebyshev-unfolded spacings of a paired-realization vortex-flux lattice; Debye–Waller thermal screening w(T)=exp(−σ1·T/2) melts the TRS-breaking flux. 38a main curve + V1 p-value-grade sampler calibration; 38b hardcore lattice (A1..A7, exact negative controls: no-flux, static dephasing); 38c reviewer ladder C1..C5 (density scan, Binder/FSS staircase 24→96, shared-curve disclosure, refine bound, crossover terminology). Spectrum cache (CSV, resumable), --t38-cap budget, six-panel journal figure. T*(L) is a finite-L crossover scale (half-decay convention).

## Result
 Test 38 (v23 three-pass) t38: PASS · Curie 3-pass (72²+96²+38c) — 486.9 min, 346 spectra in cache

## Plots
- `plots/t38_curie_panels.png` — Test 38 — Curie point (38a + 38b + 38c) (journal-engine multi-panel figure)

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 38 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.
(computation log + console capture of this test → logs/full_run_log.txt — the run's single consolidated log file)
