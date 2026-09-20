# `FINAL_REPORT/logs/` — The Consolidated Logs and the Verdict Register
> The run's complete execution record in three files — the 9,921-line consolidated log, the full computation register, the one-line verdict register — plus the 38 per-test raw log folders.

_Location: [unpacked/](../../../../README.md) › [run_data/](../../../README.md) › [run_20260914_234626/](../../README.md) › [FINAL_REPORT/](../README.md) › [logs/](README.md)_

This folder is the reference run's **complete execution record**. Three consolidated files cover the whole session, and 38 per-test folders preserve each test's raw log pair exactly as the test wrote them.

## The three consolidated files

**`full_run_log.txt` (9,921 lines).** The one-file execution log: every test's computation log and console capture, in execution order, each line timestamped with the wall-clock offset from session start. This is the file to grep when the question is "what exactly happened, and when, during those 26 hours" — the monograph's data guide (Appendix E) uses it as the primary navigation layer over the run.

**`computation_log_full.txt`.** The complete register of `log_comp()` entries — every individual computation the suite logged, without the console interleaving. Pure numbers: statistics, residuals, p-values, in calculation order.

**`results_verdicts.txt`.** The one-line verdict register: all 79 verdict entries (66 PASS / 13 FAIL), each on its own line with its verbatim statistic. This is the canonical verdict list that the monograph's Appendix A.2 reproduces and that every test-folder README in this repository quotes from.

## The per-test raw folders

`test_XX_<slug>/` preserves the raw pair (`computation_log.txt`, `stdout_capture.txt`) for each test — the same files that ship inside the test's own folder under the parent run directory. They are kept here as shipped so that the FINAL_REPORT's inline embeddings can be checked against untouched originals; the published (renamed) copies carry the `AFL` location code, and each folder has its own README with the log's statistics and excerpt.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_full.txt` | 798.3 KB · 12478 lines | Plain-text file (12478 lines). |
| `full_run_log.txt` | 674.5 KB · 9921 lines | Plain-text file (9921 lines). |
| `results_verdicts.txt` | 5.4 KB · 83 lines | Plain-text file (83 lines). |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`test_01_bN_convergence/`](test_01_bN_convergence/README.md) | 2 files | Raw computation log + console capture of Test 1 (provenance set) |
| [`test_02_bN_monotonicity/`](test_02_bN_monotonicity/README.md) | 2 files | Raw computation log + console capture of Test 2 (provenance set) |
| [`test_03_bN_rate/`](test_03_bN_rate/README.md) | 2 files | Raw computation log + console capture of Test 3 (provenance set) |
| [`test_04_gue_ks_full/`](test_04_gue_ks_full/README.md) | 2 files | Raw computation log + console capture of Test 4 (provenance set) |
| [`test_05_gue_ks_highT/`](test_05_gue_ks_highT/README.md) | 2 files | Raw computation log + console capture of Test 5 (provenance set) |
| [`test_06_chi2_hist/`](test_06_chi2_hist/README.md) | 2 files | Raw computation log + console capture of Test 6 (provenance set) |
| [`test_07_decay_slope/`](test_07_decay_slope/README.md) | 2 files | Raw computation log + console capture of Test 7 (provenance set) |
| [`test_08_residuals/`](test_08_residuals/README.md) | 2 files | Raw computation log + console capture of Test 8 (provenance set) |
| [`test_09_bootstrap_ci/`](test_09_bootstrap_ci/README.md) | 2 files | Raw computation log + console capture of Test 9 (provenance set) |
| [`test_10_cross_validation/`](test_10_cross_validation/README.md) | 2 files | Raw computation log + console capture of Test 10 (provenance set) |
| [`test_11_anderson_darling/`](test_11_anderson_darling/README.md) | 2 files | Raw computation log + console capture of Test 11 (provenance set) |
| [`test_12_two_sample_ks/`](test_12_two_sample_ks/README.md) | 2 files | Raw computation log + console capture of Test 12 (provenance set) |
| [`test_13_number_variance/`](test_13_number_variance/README.md) | 2 files | Raw computation log + console capture of Test 13 (provenance set) |
| [`test_14_spectral_rigidity/`](test_14_spectral_rigidity/README.md) | 2 files | Raw computation log + console capture of Test 14 (provenance set) |
| [`test_15_ab_construction/`](test_15_ab_construction/README.md) | 2 files | Raw computation log + console capture of Test 15 (provenance set) |
| [`test_16_ab_gue_class/`](test_16_ab_gue_class/README.md) | 2 files | Raw computation log + console capture of Test 16 (provenance set) |
| [`test_17_connes_self_duality/`](test_17_connes_self_duality/README.md) | 2 files | Raw computation log + console capture of Test 17 (provenance set) |
| [`test_18_chiral_AIII/`](test_18_chiral_AIII/README.md) | 2 files | Raw computation log + console capture of Test 18 (provenance set) |
| [`test_19_dirac_cone/`](test_19_dirac_cone/README.md) | 2 files | Raw computation log + console capture of Test 19 (provenance set) |
| [`test_20_chern_tknn/`](test_20_chern_tknn/README.md) | 2 files | Raw computation log + console capture of Test 20 (provenance set) |
| [`test_21_gamma_phase/`](test_21_gamma_phase/README.md) | 2 files | Raw computation log + console capture of Test 21 (provenance set) |
| [`test_22_ab_phase/`](test_22_ab_phase/README.md) | 2 files | Raw computation log + console capture of Test 22 (provenance set) |
| [`test_23_fractal_factor/`](test_23_fractal_factor/README.md) | 2 files | Raw computation log + console capture of Test 23 (provenance set) |
| [`test_24_dirac_string_flux/`](test_24_dirac_string_flux/README.md) | 2 files | Raw computation log + console capture of Test 24 (provenance set) |
| [`test_25_byers_yang/`](test_25_byers_yang/README.md) | 2 files | Raw computation log + console capture of Test 25 (provenance set) |
| [`test_26_pbc_torus/`](test_26_pbc_torus/README.md) | 2 files | Raw computation log + console capture of Test 26 (provenance set) |
| [`test_27_binary_chiral/`](test_27_binary_chiral/README.md) | 2 files | Raw computation log + console capture of Test 27 (provenance set) |
| [`test_28_f_gue_merit/`](test_28_f_gue_merit/README.md) | 2 files | Raw computation log + console capture of Test 28 (provenance set) |
| [`test_29_dirac_dip/`](test_29_dirac_dip/README.md) | 2 files | Raw computation log + console capture of Test 29 (provenance set) |
| [`test_30_vf_scaling/`](test_30_vf_scaling/README.md) | 2 files | Raw computation log + console capture of Test 30 (provenance set) |
| [`test_31_hatano_nelson/`](test_31_hatano_nelson/README.md) | 2 files | Raw computation log + console capture of Test 31 (provenance set) |
| [`test_32_rmean_bootstrap/`](test_32_rmean_bootstrap/README.md) | 2 files | Raw computation log + console capture of Test 32 (provenance set) |
| [`test_33_l_scaling_rmean/`](test_33_l_scaling_rmean/README.md) | 2 files | Raw computation log + console capture of Test 33 (provenance set) |
| [`test_34_direct_vs_zeta/`](test_34_direct_vs_zeta/README.md) | 2 files | Raw computation log + console capture of Test 34 (provenance set) |
| [`test_35_form_factor_Kt/`](test_35_form_factor_Kt/README.md) | 2 files | Raw computation log + console capture of Test 35 (provenance set) |
| [`test_36_byte_robust/`](test_36_byte_robust/README.md) | 2 files | Raw computation log + console capture of Test 36 (provenance set) |
| [`test_37_half_factorial_gamma/`](test_37_half_factorial_gamma/README.md) | 2 files | Raw computation log + console capture of Test 37 (provenance set) |
| [`test_38_curie_point/`](test_38_curie_point/README.md) | 2 files | Raw computation log + console capture of Test 38 (provenance set) |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../../../README.md](../../../../README.md)._