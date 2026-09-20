# `run_20260914_234626/` — The Reference Run: All 38 Tests, Complete Archive
> The 26.04-hour interactive session of 14–16 September 2026 that produced the entire verification record: 38 test folders, the four-format FINAL_REPORT, the 9,921-line consolidated log, and the verdict register.

_Location: [unpacked/](../../README.md) › [run_data/](../README.md) › [run_20260914_234626/](README.md)_

This is the reference run of the AB-Cloud v23 SUPERCOMBO suite — the archive against which every chapter of the monograph's Part II is read. It was executed in a single interactive session beginning 2026-09-14 23:46, running 93,748 seconds (26.04 hours) on Julia 1.12.0, on the primary 72×72 lattice with the two-pass protocol (secondary 96×96 for the HARDCORE audits) and the full 50,000-zero dataset embedded. The run's index page ships as `index_A.html` (renamed from `index.html`; the self-contained dashboard renders in any browser).

## The protocol in one paragraph

Each of the 38 tests ran twice. The **primary pass** produced the test's headline statistics and a first verdict. The **HARDCORE pass 2** — the deep-audit tier — re-derived the verdict through harder, often lattice-independent checks on the secondary configuration, decomposing each test into individually lettered sub-checks (H0–H7, K1–K3, S1–S4, R1–R4, Z1–Z5, …) with pre-registered limits. Tests 19, 29 and 31 added **SERIES pass-3** sweeps, and Test 19 a **pass-4 twist AUDIT**. The outcome census: 79 verdict entries — 66 PASS / 13 FAIL at the primary tier — and an audit tier of 35 batteries with 127 individually logged sub-checks of which 121 passed in-run. The four batteries carrying failed audit sub-checks (12b, 28b, 34b, 35b) are the run's honest blemishes, analysed in the monograph's Appendix C and resolved by the v3.2 estimator audit.

## What each test folder contains

Every `test_XX_<slug>/` folder ships four report formats (`report.md`, `.html`, `.pdf`, `.docx` — each with its own README at folder level), a `logs/` folder (the timestamped computation log and the raw console capture), and a `plots/` folder (60 PNG figures and 36 animations across the run). Every folder in this archive — including each `logs/` and `plots/` subfolder — carries its own detailed README. The FINAL_REPORT subfolder gathers the consolidated master report (all 38 test reports embedded inline), the one-file execution log, the verdict register, and the raw per-test copies.

## The 38 tests at a glance

| # | Folder | Test | Verdicts (pass 1 → 2) |
|---|---|---|---|
| 1 | [`test_01_bN_convergence/`](test_01_bN_convergence/README.md) | b(N) convergence table | PASS |
| 2 | [`test_02_bN_monotonicity/`](test_02_bN_monotonicity/README.md) | Monotonicity verification | PASS |
| 3 | [`test_03_bN_rate/`](test_03_bN_rate/README.md) | Convergence rate (power-law fit) | PASS |
| 4 | [`test_04_gue_ks_full/`](test_04_gue_ks_full/README.md) | GUE KS test (full range) | WARN → PASS |
| 5 | [`test_05_gue_ks_highT/`](test_05_gue_ks_highT/README.md) | GUE KS test (high-T only) | WARN → PASS |
| 6 | [`test_06_chi2_hist/`](test_06_chi2_hist/README.md) | Spacing chi^2 histogram test | WARN → PASS |
| 7 | [`test_07_decay_slope/`](test_07_decay_slope/README.md) | Decay slope (log-log regression) | PASS |
| 8 | [`test_08_residuals/`](test_08_residuals/README.md) | Residual analysis of fit | PASS |
| 9 | [`test_09_bootstrap_ci/`](test_09_bootstrap_ci/README.md) | Bootstrap CI for slope | PASS |
| 10 | [`test_10_cross_validation/`](test_10_cross_validation/README.md) | Cross-validation stability | PASS |
| 11 | [`test_11_anderson_darling/`](test_11_anderson_darling/README.md) | Anderson-Darling test | PASS |
| 12 | [`test_12_two_sample_ks/`](test_12_two_sample_ks/README.md) | Real zeros vs GUE matrix | WARN |
| 13 | [`test_13_number_variance/`](test_13_number_variance/README.md) | Number variance Σ²(L) | PASS |
| 14 | [`test_14_spectral_rigidity/`](test_14_spectral_rigidity/README.md) | Spectral rigidity Δ₃(L) | PASS |
| 15 | [`test_15_ab_construction/`](test_15_ab_construction/README.md) | AB-cloud Hamiltonian construction | PASS |
| 16 | [`test_16_ab_gue_class/`](test_16_ab_gue_class/README.md) | AB-cloud GUE classification | PASS |
| 17 | [`test_17_connes_self_duality/`](test_17_connes_self_duality/README.md) | Connes self-duality α↔1/α | PASS |
| 18 | [`test_18_chiral_AIII/`](test_18_chiral_AIII/README.md) | Chiral symmetry AIII at α=1/2 | PASS |
| 19 | [`test_19_dirac_cone/`](test_19_dirac_cone/README.md) | Dirac cone v_F ≈ 0.125 | PASS |
| 20 | [`test_20_chern_tknn/`](test_20_chern_tknn/README.md) | TKNN Chern number C₁=1 (gapped anchors) | PASS |
| 21 | [`test_21_gamma_phase/`](test_21_gamma_phase/README.md) | γ* spinorial phase ≈ π/2 | PASS |
| 22 | [`test_22_ab_phase/`](test_22_ab_phase/README.md) | AB phase Φ_AB = π/7 = δ_C | PASS |
| 23 | [`test_23_fractal_factor/`](test_23_fractal_factor/README.md) | Complex fractal factor CF | PASS |
| 24 | [`test_24_dirac_string_flux/`](test_24_dirac_string_flux/README.md) | Dirac string flux verification | PASS |
| 25 | [`test_25_byers_yang/`](test_25_byers_yang/README.md) | Byers-Yang theorem check | PASS |
| 26 | [`test_26_pbc_torus/`](test_26_pbc_torus/README.md) | PBC torus Dirac string | PASS |
| 27 | [`test_27_binary_chiral/`](test_27_binary_chiral/README.md) | Binary chiral symmetry at α=1/2 | PASS |
| 28 | [`test_28_f_gue_merit/`](test_28_f_gue_merit/README.md) | f_GUE figure of merit | WARN |
| 29 | [`test_29_dirac_dip/`](test_29_dirac_dip/README.md) | Dirac dip in DOS at α=1/2 | PASS → WARN |
| 30 | [`test_30_vf_scaling/`](test_30_vf_scaling/README.md) | Dirac cone vF scaling vs L | PASS |
| 31 | [`test_31_hatano_nelson/`](test_31_hatano_nelson/README.md) | Hatano-Nelson non-Hermitian skin | PASS |
| 32 | [`test_32_rmean_bootstrap/`](test_32_rmean_bootstrap/README.md) | Multi-realization ⟨r⟩ bootstrap | PASS |
| 33 | [`test_33_l_scaling_rmean/`](test_33_l_scaling_rmean/README.md) | L-scaling ⟨r⟩ (10→20→30→50→80→112) | PASS |
| 34 | [`test_34_direct_vs_zeta/`](test_34_direct_vs_zeta/README.md) | DIRECT AB-cloud vs ζ (full loaded set) | PASS → WARN |
| 35 | [`test_35_form_factor_Kt/`](test_35_form_factor_Kt/README.md) | Spectral form factor K(t) | WARN |
| 36 | [`test_36_byte_robust/`](test_36_byte_robust/README.md) | Byte-level robustness | PASS |
| 37 | [`test_37_half_factorial_gamma/`](test_37_half_factorial_gamma/README.md) | (1/2)! via Γ — half-factorial & GUE normalization | PASS |
| 38 | [`test_38_curie_point/`](test_38_curie_point/README.md) | Curie point of the vortex-flux lattice magnet (v23 three-pass) | — |

## Reproduction

```bash
julia ab_cloud_v23.jl --test all          # full suite, reference protocol
julia ab_cloud_v23.jl --test 33 --no-two-pass   # single test, single pass
```

(With the v3.3 source, Test 39 / TEST 34G adds the seven-surface geometry sweep.) Single-test timings range from seconds (Tests 1–3) to hours (Tests 34–36); the reference session's per-test wall times are visible in the timestamped consolidated log.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `index_A.html` | 14.8 KB · 83 lines | The run's self-contained dashboard (opens in any browser). |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`FINAL_REPORT/`](FINAL_REPORT/README.md) | 4 files, 2 subfolders | See its README |
| [`test_01_bN_convergence/`](test_01_bN_convergence/README.md) | 4 files, 2 subfolders | Test 1 — b(N) convergence table (PASS) |
| [`test_02_bN_monotonicity/`](test_02_bN_monotonicity/README.md) | 4 files, 2 subfolders | Test 2 — Monotonicity verification (PASS) |
| [`test_03_bN_rate/`](test_03_bN_rate/README.md) | 4 files, 2 subfolders | Test 3 — Convergence rate (power-law fit) (PASS) |
| [`test_04_gue_ks_full/`](test_04_gue_ks_full/README.md) | 4 files, 2 subfolders | Test 4 — GUE KS test (full range) (WARN → PASS) |
| [`test_05_gue_ks_highT/`](test_05_gue_ks_highT/README.md) | 4 files, 2 subfolders | Test 5 — GUE KS test (high-T only) (WARN → PASS) |
| [`test_06_chi2_hist/`](test_06_chi2_hist/README.md) | 4 files, 2 subfolders | Test 6 — Spacing chi^2 histogram test (WARN → PASS) |
| [`test_07_decay_slope/`](test_07_decay_slope/README.md) | 4 files, 2 subfolders | Test 7 — Decay slope (log-log regression) (PASS) |
| [`test_08_residuals/`](test_08_residuals/README.md) | 4 files, 2 subfolders | Test 8 — Residual analysis of fit (PASS) |
| [`test_09_bootstrap_ci/`](test_09_bootstrap_ci/README.md) | 4 files, 2 subfolders | Test 9 — Bootstrap CI for slope (PASS) |
| [`test_10_cross_validation/`](test_10_cross_validation/README.md) | 4 files, 2 subfolders | Test 10 — Cross-validation stability (PASS) |
| [`test_11_anderson_darling/`](test_11_anderson_darling/README.md) | 4 files, 2 subfolders | Test 11 — Anderson-Darling test (PASS) |
| [`test_12_two_sample_ks/`](test_12_two_sample_ks/README.md) | 4 files, 2 subfolders | Test 12 — Real zeros vs GUE matrix (WARN) |
| [`test_13_number_variance/`](test_13_number_variance/README.md) | 4 files, 2 subfolders | Test 13 — Number variance Σ²(L) (PASS) |
| [`test_14_spectral_rigidity/`](test_14_spectral_rigidity/README.md) | 4 files, 2 subfolders | Test 14 — Spectral rigidity Δ₃(L) (PASS) |
| [`test_15_ab_construction/`](test_15_ab_construction/README.md) | 4 files, 2 subfolders | Test 15 — AB-cloud Hamiltonian construction (PASS) |
| [`test_16_ab_gue_class/`](test_16_ab_gue_class/README.md) | 4 files, 2 subfolders | Test 16 — AB-cloud GUE classification (PASS) |
| [`test_17_connes_self_duality/`](test_17_connes_self_duality/README.md) | 4 files, 2 subfolders | Test 17 — Connes self-duality α↔1/α (PASS) |
| [`test_18_chiral_AIII/`](test_18_chiral_AIII/README.md) | 4 files, 2 subfolders | Test 18 — Chiral symmetry AIII at α=1/2 (PASS) |
| [`test_19_dirac_cone/`](test_19_dirac_cone/README.md) | 4 files, 2 subfolders | Test 19 — Dirac cone v_F ≈ 0.125 (PASS) |
| [`test_20_chern_tknn/`](test_20_chern_tknn/README.md) | 4 files, 2 subfolders | Test 20 — TKNN Chern number C₁=1 (gapped anchors) (PASS) |
| [`test_21_gamma_phase/`](test_21_gamma_phase/README.md) | 4 files, 2 subfolders | Test 21 — γ* spinorial phase ≈ π/2 (PASS) |
| [`test_22_ab_phase/`](test_22_ab_phase/README.md) | 4 files, 2 subfolders | Test 22 — AB phase Φ_AB = π/7 = δ_C (PASS) |
| [`test_23_fractal_factor/`](test_23_fractal_factor/README.md) | 4 files, 2 subfolders | Test 23 — Complex fractal factor CF (PASS) |
| [`test_24_dirac_string_flux/`](test_24_dirac_string_flux/README.md) | 4 files, 2 subfolders | Test 24 — Dirac string flux verification (PASS) |
| [`test_25_byers_yang/`](test_25_byers_yang/README.md) | 4 files, 2 subfolders | Test 25 — Byers-Yang theorem check (PASS) |
| [`test_26_pbc_torus/`](test_26_pbc_torus/README.md) | 4 files, 2 subfolders | Test 26 — PBC torus Dirac string (PASS) |
| [`test_27_binary_chiral/`](test_27_binary_chiral/README.md) | 4 files, 2 subfolders | Test 27 — Binary chiral symmetry at α=1/2 (PASS) |
| [`test_28_f_gue_merit/`](test_28_f_gue_merit/README.md) | 4 files, 2 subfolders | Test 28 — f_GUE figure of merit (WARN) |
| [`test_29_dirac_dip/`](test_29_dirac_dip/README.md) | 4 files, 2 subfolders | Test 29 — Dirac dip in DOS at α=1/2 (PASS → WARN) |
| [`test_30_vf_scaling/`](test_30_vf_scaling/README.md) | 4 files, 2 subfolders | Test 30 — Dirac cone vF scaling vs L (PASS) |
| [`test_31_hatano_nelson/`](test_31_hatano_nelson/README.md) | 4 files, 2 subfolders | Test 31 — Hatano-Nelson non-Hermitian skin (PASS) |
| [`test_32_rmean_bootstrap/`](test_32_rmean_bootstrap/README.md) | 4 files, 2 subfolders | Test 32 — Multi-realization ⟨r⟩ bootstrap (PASS) |
| [`test_33_l_scaling_rmean/`](test_33_l_scaling_rmean/README.md) | 4 files, 2 subfolders | Test 33 — L-scaling ⟨r⟩ (10→20→30→50→80→112) (PASS) |
| [`test_34_direct_vs_zeta/`](test_34_direct_vs_zeta/README.md) | 4 files, 2 subfolders | Test 34 — DIRECT AB-cloud vs ζ (full loaded set) (PASS → WARN) |
| [`test_35_form_factor_Kt/`](test_35_form_factor_Kt/README.md) | 4 files, 2 subfolders | Test 35 — Spectral form factor K(t) (WARN) |
| [`test_36_byte_robust/`](test_36_byte_robust/README.md) | 4 files, 1 subfolders | Test 36 — Byte-level robustness (PASS) |
| [`test_37_half_factorial_gamma/`](test_37_half_factorial_gamma/README.md) | 4 files, 2 subfolders | Test 37 — (1/2)! via Γ — half-factorial & GUE normalization (PASS) |
| [`test_38_curie_point/`](test_38_curie_point/README.md) | 4 files, 2 subfolders | Test 38 — Curie point of the vortex-flux lattice magnet (v23 three-pass) (—) |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../README.md](../../README.md)._