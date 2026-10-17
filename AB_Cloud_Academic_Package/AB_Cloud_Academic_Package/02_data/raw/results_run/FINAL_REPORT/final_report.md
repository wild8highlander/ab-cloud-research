# FINAL REPORT — AB-Cloud v19 — full 37-test verification suite
Generated: 2026-09-02 23:33:46   |   Julia 1.12.0   |   wall duration: 35146.0 s (585.8 min)   |   Suite: AB-Cloud v19
Author: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701) | DOI 10.5281/zenodo.21825394 | github.com/wild8highlander/research-papers

## What this folder is
FINAL_REPORT is the LAST folder of the run and gathers ALL run information: the master report (this document, in md/html/pdf), COPIES of every test's report files (reports/), COPIES of every test's computation log and console capture (logs/), the full session computation log and the one-line verdict list. Heavy plot artifacts (png/svg/pdf/gif) stay in each test's own folder ../test_XX_<slug>/plots/ — the per-test tables below point there.

## How to reproduce
Full suite:        julia ab_cloud_v19.jl --test all
Single test:       julia ab_cloud_v19.jl --test 33 --no-two-pass
Disorder cap:      --ab-w-max 1.0   (Tests 32/33/36 use W_eff = min(ab_W, W_max))
Test 36 targets:   --ab37-n-eigs-pass1 25000 --ab37-n-eigs-pass2 50000
Labs: main menu 'l' (Physics Lab), 'd3' (3D Lab); every experiment writes its own report into the same run folder.

## Configuration snapshot (end-of-run values)

```text
zeros_count           = 50000  (source: auto)
lattice primary       = 72x72  Nv=[4]  q=[1.0]
lattice secondary     = 96x96  Nv=[2]  (two-pass=true, primary-only=false)
third pass (SERIES)   = true  (Tests 19/29/31 → 19c/29c/31c real report series)
alpha                 = ab_alpha=0.5, ab_alpha_test16=0.5
disorder              = ab_W=4, ab_W_max=1  → W_eff(Tests 32/33/36)=1.00
test33 comparison row = W_cmp=0.50, Nv_cmp=144
realizations          = ab_n_realizations=5, center_fraction=0.6
byte robustness       = tol=0.02, n_bytes=200000, seed=12345, T37 targets: pass1=25000 / pass2=50000 eigs
lab                   = L=72, α=0.5, W=4, q=1, Nv=4, random/torus/monumental, seed=12345
3d                    = L=10, α=0.5, tz=1, W=0, mass=0, boundary=:torus, lines=0 q=1, seed=777
reporting             = enabled=true, dir=results, dpi=600, formats=md,html,pdf,docx
```

## Verdicts — 77 tests: 66 PASS, 0 WARN, 11 FAIL, 0 DONE
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
Test 12  [FAIL] two_sample_ks —  Test 12: 2-sample KS D=0.0233, p=0.010547 → WARN
Test 12  [PASS] two_sample_ks —  Test 12 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
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
Test 27  [PASS] binary_chiral —  Test 27: chiral defect (W=0) = 0.0, (W=1.0) = 0.0058 → PASS
Test 27  [PASS] binary_chiral —  Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
Test 28  [FAIL] f_gue_merit —  Test 28: f_GUE=0.8704, Σ²_data=0.6115 → WARN
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

## Execution steps (computation-log section markers)

```text
[13:48:04.797] [+  0.079s] ▸ run_all_tests START
[13:48:04.880] [+  0.162s] ▸ Test 1 — pass 1 (primary: standard implementation)
[13:48:05.591] [+  0.873s]  pass 1 result: PASS (elapsed: 0.71s)
[13:48:05.591] [+  0.873s] ▸ Test 1 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:27.985] [+ 23.267s]  pass 2 result: PASS (elapsed: 22.39s)
[13:48:27.985] [+ 23.267s]  Test 1 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:28.733] [+ 24.015s] ▸ Test 2 — pass 1 (primary: standard implementation)
[13:48:39.425] [+ 34.707s]  pass 1 result: PASS (elapsed: 10.69s)
[13:48:39.425] [+ 34.707s] ▸ Test 2 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:49.127] [+ 44.409s]  pass 2 result: PASS (elapsed: 9.70s)
[13:48:49.128] [+ 44.410s]  Test 2 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:48:49.817] [+ 45.099s] ▸ Test 3 — pass 1 (primary: standard implementation)
[13:48:50.148] [+ 45.430s]  pass 1 result: PASS (elapsed: 0.33s)
[13:48:50.148] [+ 45.430s] ▸ Test 3 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:48:59.449] [+ 54.732s]  pass 2 result: PASS (elapsed: 9.30s)
[13:48:59.449] [+ 54.732s]  Test 3 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:00.140] [+ 55.422s] ▸ Test 4 — pass 1 (primary: standard implementation)
[13:49:00.316] [+ 55.598s]  pass 1 result: FAIL/WARN (elapsed: 0.18s)
[13:49:00.316] [+ 55.598s] ▸ Test 4 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:09.999] [+ 65.282s]  pass 2 result: PASS (elapsed: 9.68s)
[13:49:09.999] [+ 65.282s]  Test 4 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:10.710] [+ 65.993s] ▸ Test 5 — pass 1 (primary: standard implementation)
[13:49:11.198] [+ 66.480s]  pass 1 result: FAIL/WARN (elapsed: 0.49s)
[13:49:11.198] [+ 66.480s] ▸ Test 5 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:21.050] [+ 76.332s]  pass 2 result: PASS (elapsed: 9.85s)
[13:49:21.050] [+ 76.333s]  Test 5 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:21.798] [+ 77.080s] ▸ Test 6 — pass 1 (primary: standard implementation)
[13:49:22.162] [+ 77.444s]  pass 1 result: FAIL/WARN (elapsed: 0.36s)
[13:49:22.162] [+ 77.444s] ▸ Test 6 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:31.754] [+ 87.036s]  pass 2 result: PASS (elapsed: 9.59s)
[13:49:31.754] [+ 87.036s]  Test 6 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[13:49:32.468] [+ 87.751s] ▸ Test 7 — pass 1 (primary: standard implementation)
[13:49:32.709] [+ 87.991s]  pass 1 result: PASS (elapsed: 0.24s)
[13:49:32.709] [+ 87.992s] ▸ Test 7 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:42.167] [+ 97.449s]  pass 2 result: PASS (elapsed: 9.46s)
[13:49:42.167] [+ 97.449s]  Test 7 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:42.913] [+ 98.196s] ▸ Test 8 — pass 1 (primary: standard implementation)
[13:49:43.153] [+ 98.436s]  pass 1 result: PASS (elapsed: 0.24s)
[13:49:43.154] [+ 98.436s] ▸ Test 8 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:49:52.662] [+107.944s]  pass 2 result: PASS (elapsed: 9.51s)
[13:49:52.662] [+107.944s]  Test 8 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:49:53.350] [+108.632s] ▸ Test 9 — pass 1 (primary: standard implementation)
[13:49:53.580] [+108.862s]  pass 1 result: PASS (elapsed: 0.23s)
[13:49:53.580] [+108.862s] ▸ Test 9 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:50:02.811] [+118.093s]  pass 2 result: PASS (elapsed: 9.23s)
[13:50:02.811] [+118.093s]  Test 9 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:50:03.524] [+118.806s] ▸ Test 10 — pass 1 (primary: standard implementation)
[13:50:03.792] [+119.074s]  pass 1 result: PASS (elapsed: 0.27s)
[13:50:03.792] [+119.074s] ▸ Test 10 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[13:50:13.786] [+129.068s]  pass 2 result: PASS (elapsed: 9.99s)
[13:50:13.786] [+129.068s]  Test 10 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[13:50:14.508] [+129.790s] ▸ Test 11 — pass 1 (primary: standard implementation)
[14:00:20.704] [+735.986s]  pass 1 result: FAIL/WARN (elapsed: 606.20s)
[14:00:20.704] [+735.986s] ▸ Test 11 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:24.336] [+859.618s]  pass 2 result: PASS (elapsed: 123.63s)
[14:02:24.336] [+859.618s]  Test 11 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[14:02:25.804] [+861.086s] ▸ Test 12 — pass 1 (primary: standard implementation)
[14:02:26.074] [+861.356s]  pass 1 result: FAIL/WARN (elapsed: 0.27s)
[14:02:26.074] [+861.356s] ▸ Test 12 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:40.228] [+875.510s]  pass 2 result: PASS (elapsed: 14.15s)
[14:02:40.228] [+875.510s]  Test 12 two-pass summary: pass1=FAIL pass2=PASS (hardcore) → OVERALL FAIL
[14:02:41.217] [+876.499s] ▸ Test 13 — pass 1 (primary: standard implementation)
[14:02:41.638] [+876.920s]  pass 1 result: PASS (elapsed: 0.42s)
[14:02:41.638] [+876.920s] ▸ Test 13 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:02:54.599] [+889.881s]  pass 2 result: PASS (elapsed: 12.96s)
[14:02:54.599] [+889.881s]  Test 13 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[14:02:55.465] [+890.747s] ▸ Test 14 — pass 1 (primary: standard implementation)
[14:02:56.116] [+891.398s]  pass 1 result: PASS (elapsed: 0.65s)
[14:02:56.116] [+891.399s] ▸ Test 14 — pass 2 (secondary: HARDCORE deep validation, no lattice dependence)
[14:03:09.104] [+904.386s]  pass 2 result: PASS (elapsed: 12.99s)
[14:03:09.104] [+904.386s]  Test 14 two-pass summary: pass1=PASS pass2=PASS (hardcore) → OVERALL PASS
[14:03:09.964] [+905.246s] ▸ Test 15 — pass 1 (primary: 72×72, Nv=[4])
[14:03:13.350] [+908.633s]  pass 1 result: PASS (elapsed: 3.39s)
[14:03:13.351] [+908.633s] ▸ Test 15 — pass 2 (secondary: 96×96, Nv=[2])
[14:03:36.815] [+932.097s]  pass 2 result: PASS (elapsed: 23.46s)
[14:03:36.815] [+932.097s]  Test 15 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[14:03:37.649] [+932.931s] ▸ Test 16 — pass 1 (primary: 72×72, Nv=[4])
[14:03:38.066] [+933.348s] ▸ Test 16 single-α: α=0.500000 (α=0.5000 (default))
[14:06:52.544] [+1127.826s]  pass 1 result: PASS (elapsed: 194.89s)
[14:06:52.544] [+1127.826s] ▸ Test 16 — pass 2 (secondary: 96×96, Nv=[2])
[14:32:42.865] [+2678.147s]  pass 2 result: PASS (elapsed: 1550.32s)
[14:32:42.865] [+2678.147s]  Test 16 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[14:32:43.885] [+2679.167s] ▸ Test 17 — pass 1 (primary: 72×72, Nv=[4])
[14:40:55.746] [+3171.028s]  pass 1 result: PASS (elapsed: 491.86s)
[14:40:55.747] [+3171.029s] ▸ Test 17 — pass 2 (secondary: 96×96, Nv=[2])
[15:07:52.727] [+4788.010s]  pass 2 result: PASS (elapsed: 1616.97s)
[15:07:52.728] [+4788.011s]  Test 17 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:07:56.207] [+4791.489s] ▸ Test 18 — pass 1 (primary: 72×72, Nv=[4])
[15:11:23.405] [+4998.687s]  pass 1 result: PASS (elapsed: 207.20s)
[15:11:23.405] [+4998.687s] ▸ Test 18 — pass 2 (secondary: 96×96, Nv=[2])
[15:12:20.943] [+5056.225s]  pass 2 result: PASS (elapsed: 57.54s)
[15:12:20.943] [+5056.225s]  Test 18 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:12:22.027] [+5057.309s] ▸ Test 19 — pass 1 (primary: 72×72, Nv=[4])
[15:13:36.901] [+5132.184s]  pass 1 result: PASS (elapsed: 74.87s)
[15:13:36.902] [+5132.184s] ▸ Test 19 — pass 2 (secondary: 96×96, Nv=[2])
[15:24:25.778] [+5781.060s]  pass 2 result: PASS (elapsed: 648.88s)
[15:24:25.778] [+5781.060s] ▸ Test 19 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[15:30:16.835] [+6132.117s] ▸ Test 20 — pass 1 (primary: 72×72, Nv=[4])
[15:30:17.548] [+6132.830s]  pass 1 result: PASS (elapsed: 0.71s)
[15:30:17.548] [+6132.830s] ▸ Test 20 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:17.642] [+6192.924s]  pass 2 result: PASS (elapsed: 60.09s)
[15:31:17.643] [+6192.925s]  Test 20 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:18.615] [+6193.897s] ▸ Test 21 — pass 1 (primary: 72×72, Nv=[4])
[15:31:19.032] [+6194.314s]  pass 1 result: PASS (elapsed: 0.42s)
[15:31:19.032] [+6194.314s] ▸ Test 21 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:32.783] [+6208.065s]  pass 2 result: PASS (elapsed: 13.75s)
[15:31:32.783] [+6208.065s]  Test 21 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:33.746] [+6209.029s] ▸ Test 22 — pass 1 (primary: 72×72, Nv=[4])
[15:31:33.960] [+6209.243s]  pass 1 result: PASS (elapsed: 0.21s)
[15:31:33.960] [+6209.243s] ▸ Test 22 — pass 2 (secondary: 96×96, Nv=[2])
[15:31:47.778] [+6223.061s]  pass 2 result: PASS (elapsed: 13.82s)
[15:31:47.778] [+6223.061s]  Test 22 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:31:48.745] [+6224.028s] ▸ Test 23 — pass 1 (primary: 72×72, Nv=[4])
[15:31:49.126] [+6224.408s]  pass 1 result: PASS (elapsed: 0.38s)
[15:31:49.126] [+6224.408s] ▸ Test 23 — pass 2 (secondary: 96×96, Nv=[2])
[15:32:02.675] [+6237.958s]  pass 2 result: PASS (elapsed: 13.55s)
[15:32:02.676] [+6237.958s]  Test 23 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:32:03.588] [+6238.870s] ▸ Test 24 — pass 1 (primary: 72×72, Nv=[4])
[15:32:05.403] [+6240.686s]  pass 1 result: PASS (elapsed: 1.82s)
[15:32:05.404] [+6240.686s] ▸ Test 24 — pass 2 (secondary: 96×96, Nv=[2])
[15:33:11.749] [+6307.032s]  pass 2 result: PASS (elapsed: 66.35s)
[15:33:11.750] [+6307.032s]  Test 24 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[15:33:12.904] [+6308.186s] ▸ Test 25 — pass 1 (primary: 72×72, Nv=[4])
[15:35:40.787] [+6456.069s]  pass 1 result: PASS (elapsed: 147.88s)
[15:35:40.787] [+6456.069s] ▸ Test 25 — pass 2 (secondary: 96×96, Nv=[2])
[16:39:40.082] [+10295.364s]  pass 2 result: PASS (elapsed: 3839.29s)
[16:39:40.082] [+10295.365s]  Test 25 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[16:39:41.352] [+10296.634s] ▸ Test 26 — pass 1 (primary: 72×72, Nv=[4])
[16:40:40.734] [+10356.016s]  pass 1 result: PASS (elapsed: 59.38s)
[16:40:40.734] [+10356.016s] ▸ Test 26 — pass 2 (secondary: 96×96, Nv=[2])
[17:09:15.511] [+12070.794s]  pass 2 result: PASS (elapsed: 1714.78s)
[17:09:15.511] [+12070.794s]  Test 26 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[17:09:16.249] [+12071.531s] ▸ Test 27 — pass 1 (primary: 72×72, Nv=[4])
[17:09:30.084] [+12085.366s]  pass 1 result: PASS (elapsed: 13.84s)
[17:09:30.085] [+12085.367s] ▸ Test 27 — pass 2 (secondary: 96×96, Nv=[2])
[17:12:14.164] [+12249.446s]  pass 2 result: PASS (elapsed: 164.08s)
[17:12:14.164] [+12249.446s]  Test 27 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[17:12:15.173] [+12250.455s] ▸ Test 28 — pass 1 (primary: 72×72, Nv=[4])
[17:13:08.708] [+12303.990s]  pass 1 result: FAIL/WARN (elapsed: 53.54s)
[17:13:08.708] [+12303.991s] ▸ Test 28 — pass 2 (secondary: 96×96, Nv=[2])
[17:39:36.656] [+13891.939s]  pass 2 result: FAIL/WARN (elapsed: 1587.95s)
[17:39:36.657] [+13891.939s]  Test 28 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[17:39:37.904] [+13893.186s] ▸ Test 29 — pass 1 (primary: 72×72, Nv=[4])
[17:42:15.059] [+14050.341s]  pass 1 result: PASS (elapsed: 157.15s)
[17:42:15.059] [+14050.341s] ▸ Test 29 — pass 2 (secondary: 96×96, Nv=[2])
[17:57:50.396] [+14985.678s]  pass 2 result: FAIL/WARN (elapsed: 935.34s)
[17:57:50.396] [+14985.678s] ▸ Test 29 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[18:45:06.539] [+17821.821s] ▸ Test 30 — pass 1 (primary: 72×72, Nv=[4])
[18:47:06.232] [+17941.514s]  pass 1 result: PASS (elapsed: 119.69s)
[18:47:06.232] [+17941.514s] ▸ Test 30 — pass 2 (secondary: 96×96, Nv=[2])
[18:59:11.075] [+18666.357s]  pass 2 result: PASS (elapsed: 724.84s)
[18:59:11.078] [+18666.360s]  Test 30 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[18:59:12.283] [+18667.565s] ▸ Test 31 — pass 1 (primary: 72×72, Nv=[4])
[19:03:17.582] [+18912.864s]  pass 1 result: PASS (elapsed: 245.30s)
[19:03:17.582] [+18912.864s] ▸ Test 31 — pass 2 (secondary: 96×96, Nv=[2])
[19:58:20.555] [+22215.837s]  pass 2 result: PASS (elapsed: 3302.97s)
[19:58:20.555] [+22215.837s] ▸ Test 31 — pass 3 (tertiary: SERIES — real report series, 96×96 regime)
[20:04:51.687] [+22606.969s] ▸ Test 32 — pass 1 (primary: 72×72, Nv=[4])
[20:13:27.441] [+23122.723s]  pass 1 result: PASS (elapsed: 515.75s)
[20:13:27.441] [+23122.723s] ▸ Test 32 — pass 2 (secondary: 96×96, Nv=[2])
[21:02:32.804] [+26068.086s]  pass 2 result: PASS (elapsed: 2945.36s)
[21:02:32.804] [+26068.086s]  Test 32 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[21:02:33.557] [+26068.839s] ▸ Test 33 — pass 1 (primary: 72×72, Nv=[4])
[21:18:17.750] [+27013.032s]  pass 1 result: PASS (elapsed: 944.19s)
[21:18:17.750] [+27013.032s] ▸ Test 33 — pass 2 (secondary: 96×96, Nv=[2])
[21:33:01.262] [+27896.544s]  pass 2 result: PASS (elapsed: 883.51s)
[21:33:01.262] [+27896.544s]  Test 33 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[21:33:02.273] [+27897.555s] ▸ Test 34 — pass 1 (primary: 72×72, Nv=[4])
[21:37:02.924] [+28138.206s]  pass 1 result: PASS (elapsed: 240.65s)
[21:37:02.924] [+28138.206s] ▸ Test 34 — pass 2 (secondary: 96×96, Nv=[2])
[22:04:23.597] [+29778.879s]  pass 2 result: FAIL/WARN (elapsed: 1640.67s)
[22:04:23.600] [+29778.882s]  Test 34 two-pass summary: pass1=PASS pass2=FAIL → OVERALL FAIL
[22:04:24.906] [+29780.188s] ▸ Test 35 — pass 1 (primary: 72×72, Nv=[4])
[22:09:08.652] [+30063.934s]  pass 1 result: FAIL/WARN (elapsed: 283.74s)
[22:09:08.653] [+30063.936s] ▸ Test 35 — pass 2 (secondary: 96×96, Nv=[2])
[22:37:01.653] [+31736.935s]  pass 2 result: FAIL/WARN (elapsed: 1673.00s)
[22:37:01.654] [+31736.936s]  Test 35 two-pass summary: pass1=FAIL pass2=FAIL → OVERALL FAIL
[22:37:02.779] [+31738.061s] ▸ Test 36 — pass 1 (primary: 72×72, Nv=[4])
[22:45:52.588] [+32267.870s]  pass 1 result: PASS (elapsed: 529.81s)
[22:45:52.588] [+32267.870s] ▸ Test 36 — pass 2 (secondary: 96×96, Nv=[2])
[23:33:00.768] [+35096.050s]  pass 2 result: PASS (elapsed: 2828.18s)
[23:33:00.768] [+35096.050s]  Test 36 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
[23:33:02.097] [+35097.379s] ▸ Test 37 — pass 1 (primary: 72×72, Nv=[4])
[23:33:21.765] [+35117.048s]  pass 1 result: PASS (elapsed: 19.67s)
[23:33:21.766] [+35117.048s] ▸ Test 37 — pass 2 (secondary: 96×96, Nv=[2])
[23:33:39.517] [+35134.799s]  pass 2 result: PASS (elapsed: 17.75s)
[23:33:39.517] [+35134.799s]  Test 37 two-pass summary: pass1=PASS pass2=PASS → OVERALL PASS
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
test_12_two_sample_ks  [PASS]  reports/ + logs/ copied; plots live in ../test_12_two_sample_ks/plots/
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
test_27_binary_chiral  [PASS]  reports/ + logs/ copied; plots live in ../test_27_binary_chiral/plots/
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
```
Log files: logs/full_execution_log.txt (console tee, suite runs), logs/computation_log.txt / computation_log_full.txt (every computation), logs/results_verdicts.txt (one-line verdicts), logs/test_XX_*/ (per-test).
Run index: ../index.html — verdict table with direct links to every per-test report.
