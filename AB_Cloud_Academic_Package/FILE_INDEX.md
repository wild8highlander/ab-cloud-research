# FILE_INDEX — Every File in This Package, Described

This index lists **every file** of the GitHub edition of the AB-Cloud v23 package (v34): the preserved original ZIP and the complete unpacked tree. For each file: its published path, its size, its original name when the published name differs (see the renaming policy below), and a one-line description. Folder-level documentation lives in each folder's `README.md`; the package overview is [`README.md`](README.md).

## The original ZIP

| File | Size | Description |
|---|---|---|
| `zip_archive/AB_Cloud_v23_Full_Package_Academic_v34.zip` | 38.8 MB | The original submission package (v34 freeze), preserved bit-for-bit. SHA-256: `3febd8b0761777822bc1cd0f3f423f4d01672b79b059f456d4cf1a412a4b2100`. Detailed: [zip_archive/README.md](zip_archive/README.md). |

## Renaming policy (unique filenames edition)

The original ZIP reuses some basenames across folders (`report.md` in every test folder, `plot_01.png`, `index.html`, …). Published names are made **globally unique** by appending a location code before the extension: `A04` = reference run, test 04; `A04L`/`A04P` = its logs/plots subfolders; `AFL`/`AFR` = FINAL_REPORT raw logs/reports; `P1`/`P2` = the two preprints; `PC`/`PCA`/`PCAD` = Python clone paths; `MG`/`FT`/`LS` = Monograph/fonts/lab_standalone; `B`, `BA`, `C`, `D`, `DL` = the September 2026 addendum runs. Files with package-unique names are published unchanged. The two documentation names `README.md` (generated for every folder) and `README_original.md` (originals preserved) are exempt by design. Complete mapping below.

## Unpacked tree — complete listing

| Published path | Size | Original name (if renamed) | Description |
|---|---|---|---|
| `AB_Cloud_v23_Academic_Essence.docx` | 2.0 MB | — | The Academic Essence companion — editable Microsoft Word edition. |
| `AB_Cloud_v23_Academic_Essence.pdf` | 4.2 MB | — | The Academic Essence companion — PDF edition: the framework's academic account in fourteen chapters, bilingual EN + RU annotation, v3.2 audit resolution and Add.8 integrated. |
| `AB_Cloud_v23_Monograph_ROOT.docx` | 3.1 MB | — | The monograph — editable Microsoft Word edition (TOC updates via right-click → Update Field). |
| `AB_Cloud_v23_Monograph_ROOT.pdf` | 11.1 MB | — | The monograph — PDF edition (cover, abstract, TOC, Parts I–III with 38 test chapters and 46 figures, references, Appendices A–E, September 2026 addendum Add.1–Add.8). |
| `README.md` | 7.5 KB | `unpacked/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `README_original.md` | 8.2 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `SHA256SUMS.txt` | 85.1 KB | — | The original v34 freeze's SHA-256 checksum register (original filenames). |
| `cover_design_source.html` | 3.4 KB | — | Editable HTML source of the PDF cover design (uses the fonts shipped in fonts/). |
| `cover_letter.docx` | 38.3 KB | — | Cover letter to the Editor-in-Chief — editable Word edition. |
| `cover_letter.pdf` | 36.2 KB | — | Cover letter to the Editor-in-Chief — PDF edition (references the repository, the run archive and the Zenodo DOI). |
| `journal_recommendations.md` | 10.7 KB | — | Interdisciplinary journal short-list: scope fit, APCs, code/data policies, registration steps, GitHub integration. |
| `run_20260914_234626.zip` | 4.6 MB | — | The original run archive of the reference run, preserved exactly as shipped. |
| `submission_checklist.md` | 4.5 KB | — | Pre-submission checklist: venue selection, TOC refresh, reviewer slots. |
| `submission_forms.pdf` | 42.5 KB | — | Journal submission forms: CRediT contributions, declarations, funding, data availability, ethics, author summary, licence. |
| `Monograph/AB_Cloud_v23_Monograph_MG.docx` | 3.1 MB | — | The monograph — editable Microsoft Word edition (TOC updates via right-click → Update Field). |
| `Monograph/AB_Cloud_v23_Monograph_MG.pdf` | 11.1 MB | — | The monograph — PDF edition (cover, abstract, TOC, Parts I–III with 38 test chapters and 46 figures, references, Appendices A–E, September 2026 addendum Add.1–Add.8). |
| `Monograph/README.md` | 3.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `fonts/README.md` | 3.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa0ZL7SUc.woff2` | 18.3 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2` | 47.1 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1pL7SUc.woff2` | 18.6 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa25L7SUc.woff2` | 83.1 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2JL7SUc.woff2` | 25.4 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2ZL7SUc.woff2` | 11.0 KB | — | WOFF2 web-font binary (subset). |
| `fonts/UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2pL7SUc.woff2` | 10.0 KB | — | WOFF2 web-font binary (subset). |
| `fonts/fonts.css` | 14.5 KB | — | Generated stylesheet declaring all 40 @font-face entries of the Inter and Playfair Display families with their unicode ranges. |
| `fonts/fonts_local.css` | 12.9 KB | — | The localised stylesheet (relative font URLs) linked by cover_design_source.html — enables fully offline cover rendering. |
| `fonts/nuFiD-vYSZviVYUb_rj3ij__anPXDTLYgFE_.woff2` | 20.6 KB | — | WOFF2 web-font binary (subset). |
| `fonts/nuFiD-vYSZviVYUb_rj3ij__anPXDTPYgFE_.woff2` | 8.9 KB | — | WOFF2 web-font binary (subset). |
| `fonts/nuFiD-vYSZviVYUb_rj3ij__anPXDTjYgFE_.woff2` | 20.7 KB | — | WOFF2 web-font binary (subset). |
| `fonts/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgA.woff2` | 37.5 KB | — | WOFF2 web-font binary (subset). |
| `lab_standalone/README.md` | 4.6 KB | `unpacked/lab_standalone/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `lab_standalone/README_original.md` | 2.5 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `lab_standalone/ab_cloud_v23.jl` | 2.1 MB | — | The full SUPERCOMBO verification suite, v3.3 working copy — all 38 tests, HARDCORE audits, TEST 34G geometry sweep (Test 39); the Appendix B source of the monograph. |
| `lab_standalone/finite-size_lab.jl` | 233.2 KB | — | The Test 34 standalone laboratory, v1.3 — modes 1–5, eight geometries incl. PSL(2,27); produced the three September 2026 runs. |
| `lab_standalone/hp_audit_standalone.jl` | 310.8 KB | — | HP·MERIDIAN v24.1-SA — the standalone Hilbert–Pólya deep-audit module (menu h tests). |
| `preprint/README.md` | 3.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `preprint/appendix_b_code.pdf` | 1.5 MB | — | Appendix B as a standalone listing — the complete v3.3 source, 32,095 lines, 225 pages. |
| `preprint/monograph_preprint.pdf` | 3.6 MB | — | The monograph preprint — compiled PDF (305 pages, Add.8 included). |
| `preprint/monograph_preprint.tex` | 267.9 KB | — | The monograph preprint — complete LaTeX source (PLOS-style single column; compiles with tectonic). |
| `preprint/addendum_figures/README.md` | 2.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `preprint/addendum_figures/fig_add1_w_sweep_en_P1A.png` | 472.0 KB | — | Addendum figure 1 — the disorder (W) sweep: the confrontation distance stays flat as disorder grows (Add.3). |
| `preprint/addendum_figures/fig_add2_mixture_en_P1A.png` | 426.8 KB | — | Addendum figure 2 — the effective GUE+Poisson mixture decomposition; post-fit residual 0.0241 vs the GUE-matrix calibration floor 0.0242 (Add.5). |
| `preprint2/README.md` | 2.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `preprint2/academic_essence_preprint.pdf` | 2.1 MB | — | The Academic Essence preprint — compiled PDF (53 pages, Add.8 included). |
| `preprint2/academic_essence_preprint.tex` | 140.7 KB | — | The Academic Essence preprint — complete LaTeX source. |
| `preprint2/addendum_figures/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `preprint2/addendum_figures/fig_add1_w_sweep_en_P2A.png` | 472.0 KB | — | Addendum figure 1 — the disorder (W) sweep: the confrontation distance stays flat as disorder grows (Add.3). |
| `preprint2/addendum_figures/fig_add2_mixture_en_P2A.png` | 426.8 KB | — | Addendum figure 2 — the effective GUE+Poisson mixture decomposition; post-fit residual 0.0241 vs the GUE-matrix calibration floor 0.0242 (Add.5). |
| `python_clone/README.md` | 3.5 KB | `unpacked/python_clone/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `python_clone/README_original.md` | 6.2 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `python_clone/pyproject.toml` | 516 B | — | Python packaging metadata for the abcloud clone. |
| `python_clone/requirements.txt` | 52 B | — | Python dependencies of the clone (NumPy/SciPy/matplotlib). |
| `python_clone/abcloud/README.md` | 3.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `python_clone/abcloud/__init__.py` | 521 B | — | Package initialisation for the abcloud clone. |
| `python_clone/abcloud/cli.py` | 3.6 KB | — | The clone's command-line interface (--list, --test N|a-b|all, --no-two-pass, --zeros, --full, --out). |
| `python_clone/abcloud/core.py` | 25.1 KB | — | The clone's statistics engine: Gram ladder, unfolding, KS/χ²/AD, ⟨r⟩, Σ²(L), Δ₃(L), R₂(s), form factor, bootstrap/Monte-Carlo machinery. |
| `python_clone/abcloud/report.py` | 12.3 KB | — | The clone's report writer and plot engine — emits per-test reports and the master final_report in the Julia suite's layout. |
| `python_clone/abcloud/runner.py` | 7.5 KB | — | The clone's two-pass orchestrator: primary verdicts, HARDCORE pass-2 audits, composite verdict algebra. |
| `python_clone/abcloud/tests_01_14.py` | 26.4 KB | — | Batteries 1–14: the convergence triad, the distributional family, decay-law robustness, long-range RMT statistics. |
| `python_clone/abcloud/tests_15_26.py` | 30.1 KB | — | Batteries 15–26: AB construction certificates, GUE classification, the exact duality/symmetry/flux/topology layer. |
| `python_clone/abcloud/tests_27_38.py` | 25.9 KB | — | Batteries 27–38: binary-chiral dictionary, merit aggregate, scaling/robustness, the direct confrontation, form factor, byte robustness, Γ identities, Curie point. |
| `python_clone/abcloud/data/README.md` | 2.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `python_clone/abcloud/data/zeta_zeros_50000.txt` | 770.7 KB | — | The embedded dataset: the first 50,000 non-trivial ζ zeros (Odlyzko-sourced), one ordinate per line — byte-identical input for both implementations. |
| `run_data/AUDIT_DATA.md` | 5.5 KB | — | The audit-tier reading guide for the run archives: census, per-test navigation, how to verify any number in the monograph. |
| `run_data/README.md` | 3.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/README.md` | 12.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/index_A.html` | 14.8 KB | — | The run's self-contained dashboard (opens in any browser). |
| `run_data/run_20260914_234626/FINAL_REPORT/README.md` | 3.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/final_report.docx` | 252.3 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/final_report.html` | 142.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/final_report.pdf` | 195.5 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/final_report_AF.md` | 133.5 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/README.md` | 7.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/computation_log_full.txt` | 798.3 KB | — | Plain-text file (12478 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/full_run_log.txt` | 674.5 KB | — | Plain-text file (9921 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/results_verdicts.txt` | 5.4 KB | — | Plain-text file (83 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/computation_log_XX.txt` | 131 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/stdout_capture_XX.txt` | 4.0 KB | — | Plain-text file (66 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/computation_log_XX.txt` | 134 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (24 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/computation_log_XX.txt` | 141 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/computation_log_XX.txt` | 1.2 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/computation_log_XX.txt` | 812 B | — | Plain-text file (10 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (17 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/computation_log_XX.txt` | 137 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/stdout_capture_XX.txt` | 1.1 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/computation_log_XX.txt` | 141 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (13 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/computation_log_XX.txt` | 133 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/stdout_capture_XX.txt` | 1.1 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/computation_log_XX.txt` | 131 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (13 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/computation_log_XX.txt` | 136 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/stdout_capture_XX.txt` | 1.3 KB | — | Plain-text file (15 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/computation_log_XX.txt` | 173.8 KB | — | Plain-text file (3014 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/stdout_capture_XX.txt` | 1.9 KB | — | Plain-text file (27 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/computation_log_XX.txt` | 134 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/stdout_capture_XX.txt` | 1.1 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/computation_log_XX.txt` | 2.3 KB | — | Plain-text file (24 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/stdout_capture_XX.txt` | 1.6 KB | — | Plain-text file (22 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/computation_log_XX.txt` | 1.3 KB | — | Plain-text file (15 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (20 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/computation_log_XX.txt` | 251 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/stdout_capture_XX.txt` | 1.1 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/computation_log_XX.txt` | 1.3 KB | — | Plain-text file (13 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/stdout_capture_XX.txt` | 1.3 KB | — | Plain-text file (18 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/computation_log_XX.txt` | 2.9 KB | — | Plain-text file (24 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/computation_log_XX.txt` | 529 B | — | Plain-text file (6 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/stdout_capture_XX.txt` | 1.5 KB | — | Plain-text file (16 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/computation_log_XX.txt` | 386 B | — | Plain-text file (5 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/stdout_capture_XX.txt` | 3.6 KB | — | Plain-text file (33 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/computation_log_XX.txt` | 151 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/stdout_capture_XX.txt` | 2.1 KB | — | Plain-text file (24 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/computation_log_XX.txt` | 138 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/computation_log_XX.txt` | 138 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/computation_log_XX.txt` | 135 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/stdout_capture_XX.txt` | 1.1 KB | — | Plain-text file (12 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/computation_log_XX.txt` | 642 B | — | Plain-text file (7 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (17 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/computation_log_XX.txt` | 1.6 KB | — | Plain-text file (15 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/stdout_capture_XX.txt` | 1.5 KB | — | Plain-text file (20 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/computation_log_XX.txt` | 1.5 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/stdout_capture_XX.txt` | 1.6 KB | — | Plain-text file (20 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/computation_log_XX.txt` | 1.8 KB | — | Plain-text file (16 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/stdout_capture_XX.txt` | 3.3 KB | — | Plain-text file (36 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/computation_log_XX.txt` | 1.4 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/stdout_capture_XX.txt` | 1.2 KB | — | Plain-text file (17 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/computation_log_XX.txt` | 1.6 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/stdout_capture_XX.txt` | 2.1 KB | — | Plain-text file (26 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/computation_log_XX.txt` | 1.6 KB | — | Plain-text file (14 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/stdout_capture_XX.txt` | 1.8 KB | — | Plain-text file (24 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/computation_log_XX.txt` | 2.8 KB | — | Plain-text file (28 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/stdout_capture_XX.txt` | 3.1 KB | — | Plain-text file (36 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/computation_log_XX.txt` | 4.8 KB | — | Plain-text file (43 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/stdout_capture_XX.txt` | 5.9 KB | — | Plain-text file (84 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/computation_log_XX.txt` | 12.3 KB | — | Plain-text file (103 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/stdout_capture_XX.txt` | 4.3 KB | — | Plain-text file (53 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/computation_log_XX.txt` | 812 B | — | Plain-text file (8 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/stdout_capture_XX.txt` | 1.6 KB | — | Plain-text file (22 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/computation_log_XX.txt` | 798 B | — | Plain-text file (8 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (19 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/computation_log_XX.txt` | 15.7 KB | — | Plain-text file (145 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/stdout_capture_XX.txt` | 3.6 KB | — | Plain-text file (46 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/computation_log_XX.txt` | 162 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/stdout_capture_XX.txt` | 1.4 KB | — | Plain-text file (15 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/computation_log_XX.txt` | 172 B | — | Plain-text file (4 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/stdout_capture_XX.txt` | 7.0 KB | — | Plain-text file (135 lines). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/README.md` | 6.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.docx` | 8.0 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.html` | 5.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.md` | 5.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.pdf` | 8.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.docx` | 5.1 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.html` | 2.7 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.md` | 2.4 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.pdf` | 4.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.docx` | 4.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.html` | 2.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.md` | 2.2 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.pdf` | 3.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.docx` | 6.0 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.html` | 3.6 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.md` | 3.2 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.pdf` | 4.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.docx` | 5.7 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.html` | 3.3 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.md` | 3.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.pdf` | 4.5 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.docx` | 4.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.html` | 2.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.md` | 2.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.pdf` | 3.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.docx` | 4.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.html` | 2.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.md` | 2.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.pdf` | 3.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.docx` | 4.7 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.html` | 2.3 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.md` | 1.9 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.pdf` | 3.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.docx` | 4.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.html` | 2.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.md` | 2.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.pdf` | 3.1 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.docx` | 4.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.html` | 2.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.md` | 2.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.pdf` | 3.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.docx` | 179.2 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.html` | 176.8 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.md` | 176.5 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.pdf` | 289.6 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.docx` | 4.7 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.html` | 2.3 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.md` | 1.9 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.pdf` | 3.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.docx` | 7.4 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.html` | 5.0 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.md` | 4.6 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.pdf` | 6.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.docx` | 6.2 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.html` | 3.8 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.md` | 3.4 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.pdf` | 5.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.docx` | 5.1 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.html` | 2.6 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.md` | 2.2 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.pdf` | 3.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.docx` | 6.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.html` | 4.2 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.md` | 3.8 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.pdf` | 5.5 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.docx` | 8.2 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.html` | 5.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.md` | 5.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.pdf` | 7.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.docx` | 5.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.html` | 3.3 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.md` | 2.9 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.pdf` | 4.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.docx` | 8.5 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.html` | 5.9 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.md` | 5.5 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.pdf` | 7.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.docx` | 6.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.html` | 4.1 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.md` | 3.6 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.pdf` | 5.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.docx` | 5.0 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.html` | 2.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.md` | 2.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.pdf` | 3.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.docx` | 4.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.html` | 2.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.md` | 2.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.pdf` | 3.2 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.docx` | 4.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.html` | 2.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.md` | 2.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.pdf` | 3.1 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.docx` | 5.7 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.html` | 3.2 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.md` | 2.9 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.pdf` | 4.4 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.docx` | 6.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.html` | 4.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.md` | 4.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.pdf` | 5.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.docx` | 7.0 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.html` | 4.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.md` | 4.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.pdf` | 5.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.docx` | 9.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.html` | 7.2 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.md` | 6.7 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.pdf` | 9.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.docx` | 6.6 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.html` | 4.0 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.md` | 3.6 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.pdf` | 5.4 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.docx` | 7.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.html` | 5.1 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.md` | 4.7 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.pdf` | 6.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.docx` | 7.6 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.html` | 5.0 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.md` | 4.6 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.pdf` | 6.5 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.docx` | 10.1 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.html` | 7.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.md` | 7.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.pdf` | 9.9 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.docx` | 16.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.html` | 13.9 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.md` | 13.5 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.pdf` | 18.9 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.docx` | 22.4 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.html` | 19.6 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.md` | 19.2 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.pdf` | 25.8 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.docx` | 6.7 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.html` | 4.0 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.md` | 3.6 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.pdf` | 5.3 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.docx` | 6.3 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.html` | 3.6 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.md` | 3.2 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.pdf` | 4.9 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.docx` | 24.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.html` | 22.3 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.md` | 21.9 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.pdf` | 29.9 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.docx` | 5.9 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.html` | 3.4 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.md` | 3.0 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.pdf` | 4.1 KB | — | PDF document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.docx` | 11.8 KB | — | Microsoft Word document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.html` | 9.5 KB | — | HTML document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.md` | 9.1 KB | — | Markdown document. |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.pdf` | 15.0 KB | — | PDF document. |
| `run_data/run_20260914_234626/test_01_bN_convergence/README.md` | 8.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_01_bN_convergence/report_A01.docx` | 8.0 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_01_bN_convergence/report_A01.html` | 5.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_01_bN_convergence/report_A01.md` | 5.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_01_bN_convergence/report_A01.pdf` | 8.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_01_bN_convergence/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_01_bN_convergence/logs/computation_log_A01L.txt` | 131 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_01_bN_convergence/logs/stdout_capture_A01L.txt` | 4.0 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/README.md` | 1.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/animation_A01P.gif` | 19.0 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_01_A01P.png` | 52.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_02_A01P.png` | 48.3 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/README.md` | 6.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.docx` | 5.1 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.html` | 2.7 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.md` | 2.4 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.pdf` | 4.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/logs/computation_log_A02L.txt` | 134 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/logs/stdout_capture_A02L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/plots/animation_A02P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/plots/plot_01_A02P.png` | 47.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_03_bN_rate/README.md` | 5.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_03_bN_rate/report_A03.docx` | 4.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_03_bN_rate/report_A03.html` | 2.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_03_bN_rate/report_A03.md` | 2.2 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_03_bN_rate/report_A03.pdf` | 3.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_03_bN_rate/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_03_bN_rate/logs/computation_log_A03L.txt` | 141 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_03_bN_rate/logs/stdout_capture_A03L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_03_bN_rate/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_03_bN_rate/plots/animation_A03P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_03_bN_rate/plots/plot_01_A03P.png` | 47.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/README.md` | 7.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.docx` | 6.0 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.html` | 3.6 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.md` | 3.2 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.pdf` | 4.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/logs/README.md` | 2.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/logs/computation_log_A04L.txt` | 1.2 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_04_gue_ks_full/logs/stdout_capture_A04L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_04_gue_ks_full/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/plots/animation_A04P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_04_gue_ks_full/plots/plot_01_A04P.png` | 47.2 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/README.md` | 6.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.docx` | 5.7 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.html` | 3.3 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.md` | 3.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.pdf` | 4.5 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/logs/README.md` | 2.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/logs/computation_log_A05L.txt` | 812 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/logs/stdout_capture_A05L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/plots/animation_A05P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/plots/plot_01_A05P.png` | 47.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_06_chi2_hist/README.md` | 5.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_06_chi2_hist/report_A06.docx` | 4.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_06_chi2_hist/report_A06.html` | 2.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_06_chi2_hist/report_A06.md` | 2.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_06_chi2_hist/report_A06.pdf` | 3.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_06_chi2_hist/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_06_chi2_hist/logs/computation_log_A06L.txt` | 137 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_06_chi2_hist/logs/stdout_capture_A06L.txt` | 1.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_06_chi2_hist/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_06_chi2_hist/plots/animation_A06P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_06_chi2_hist/plots/plot_01_A06P.png` | 47.5 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_07_decay_slope/README.md` | 6.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_07_decay_slope/report_A07.docx` | 4.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_07_decay_slope/report_A07.html` | 2.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_07_decay_slope/report_A07.md` | 2.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_07_decay_slope/report_A07.pdf` | 3.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_07_decay_slope/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_07_decay_slope/logs/computation_log_A07L.txt` | 141 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_07_decay_slope/logs/stdout_capture_A07L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_07_decay_slope/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_07_decay_slope/plots/animation_A07P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_07_decay_slope/plots/plot_01_A07P.png` | 47.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_08_residuals/README.md` | 5.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_08_residuals/report_A08.docx` | 4.7 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_08_residuals/report_A08.html` | 2.3 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_08_residuals/report_A08.md` | 1.9 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_08_residuals/report_A08.pdf` | 3.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_08_residuals/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_08_residuals/logs/computation_log_A08L.txt` | 133 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_08_residuals/logs/stdout_capture_A08L.txt` | 1.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_08_residuals/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_08_residuals/plots/animation_A08P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_08_residuals/plots/plot_01_A08P.png` | 47.9 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/README.md` | 5.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.docx` | 4.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.html` | 2.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.md` | 2.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.pdf` | 3.1 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/logs/computation_log_A09L.txt` | 131 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/logs/stdout_capture_A09L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/plots/animation_A09P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/plots/plot_01_A09P.png` | 47.9 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_10_cross_validation/README.md` | 5.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_10_cross_validation/report_A10.docx` | 4.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_10_cross_validation/report_A10.html` | 2.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_10_cross_validation/report_A10.md` | 2.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_10_cross_validation/report_A10.pdf` | 3.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_10_cross_validation/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_10_cross_validation/logs/computation_log_A10L.txt` | 136 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_10_cross_validation/logs/stdout_capture_A10L.txt` | 1.3 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_10_cross_validation/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_10_cross_validation/plots/animation_A10P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_10_cross_validation/plots/plot_01_A10P.png` | 47.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_11_anderson_darling/README.md` | 7.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_11_anderson_darling/report_A11.docx` | 179.2 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_11_anderson_darling/report_A11.html` | 176.8 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_11_anderson_darling/report_A11.md` | 176.5 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_11_anderson_darling/report_A11.pdf` | 289.6 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_11_anderson_darling/logs/README.md` | 2.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_11_anderson_darling/logs/computation_log_A11L.txt` | 173.8 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_11_anderson_darling/logs/stdout_capture_A11L.txt` | 1.9 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_11_anderson_darling/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_11_anderson_darling/plots/animation_A11P.gif` | 10.1 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_11_anderson_darling/plots/plot_01_A11P.png` | 48.0 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/README.md` | 5.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.docx` | 4.7 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.html` | 2.3 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.md` | 1.9 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.pdf` | 3.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/logs/computation_log_A12L.txt` | 134 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_12_two_sample_ks/logs/stdout_capture_A12L.txt` | 1.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_12_two_sample_ks/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/plots/animation_A12P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_12_two_sample_ks/plots/plot_01_A12P.png` | 46.9 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_13_number_variance/README.md` | 7.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_13_number_variance/report_A13.docx` | 7.4 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_13_number_variance/report_A13.html` | 5.0 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_13_number_variance/report_A13.md` | 4.6 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_13_number_variance/report_A13.pdf` | 6.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_13_number_variance/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_13_number_variance/logs/computation_log_A13L.txt` | 2.3 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_13_number_variance/logs/stdout_capture_A13L.txt` | 1.6 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_13_number_variance/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_13_number_variance/plots/animation_A13P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_13_number_variance/plots/plot_01_A13P.png` | 47.7 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/README.md` | 7.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.docx` | 6.2 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.html` | 3.8 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.md` | 3.4 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.pdf` | 5.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/logs/README.md` | 2.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/logs/computation_log_A14L.txt` | 1.3 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/logs/stdout_capture_A14L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/plots/animation_A14P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/plots/plot_01_A14P.png` | 47.1 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_15_ab_construction/README.md` | 6.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_15_ab_construction/report_A15.docx` | 5.1 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_15_ab_construction/report_A15.html` | 2.6 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_15_ab_construction/report_A15.md` | 2.2 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_15_ab_construction/report_A15.pdf` | 3.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_15_ab_construction/logs/README.md` | 2.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_15_ab_construction/logs/computation_log_A15L.txt` | 251 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_15_ab_construction/logs/stdout_capture_A15L.txt` | 1.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_15_ab_construction/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_15_ab_construction/plots/animation_A15P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_15_ab_construction/plots/plot_01_A15P.png` | 47.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/README.md` | 7.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.docx` | 6.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.html` | 4.2 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.md` | 3.8 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.pdf` | 5.5 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/logs/computation_log_A16L.txt` | 1.3 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_16_ab_gue_class/logs/stdout_capture_A16L.txt` | 1.3 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/animation_A16P.gif` | 27.8 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_01_A16P.png` | 59.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_02_A16P.png` | 71.5 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_03_A16P.png` | 47.5 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/README.md` | 7.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.docx` | 8.2 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.html` | 5.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.md` | 5.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.pdf` | 7.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/logs/README.md` | 2.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/logs/computation_log_A17L.txt` | 2.9 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_17_connes_self_duality/logs/stdout_capture_A17L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_17_connes_self_duality/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/plots/animation_A17P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_17_connes_self_duality/plots/plot_01_A17P.png` | 47.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/README.md` | 6.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.docx` | 5.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.html` | 3.3 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.md` | 2.9 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.pdf` | 4.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/logs/computation_log_A18L.txt` | 529 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_18_chiral_AIII/logs/stdout_capture_A18L.txt` | 1.5 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_18_chiral_AIII/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/plots/animation_A18P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_18_chiral_AIII/plots/plot_01_A18P.png` | 47.9 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_19_dirac_cone/README.md` | 9.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_19_dirac_cone/report_A19.docx` | 8.5 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_19_dirac_cone/report_A19.html` | 5.9 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_19_dirac_cone/report_A19.md` | 5.5 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_19_dirac_cone/report_A19.pdf` | 7.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_19_dirac_cone/logs/README.md` | 2.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_19_dirac_cone/logs/computation_log_A19L.txt` | 386 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_19_dirac_cone/logs/stdout_capture_A19L.txt` | 3.6 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/animation_A19P.gif` | 28.9 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_01_A19P.png` | 62.0 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_02_A19P.png` | 59.0 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_03_A19P.png` | 48.5 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_20_chern_tknn/README.md` | 7.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_20_chern_tknn/report_A20.docx` | 6.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_20_chern_tknn/report_A20.html` | 4.1 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_20_chern_tknn/report_A20.md` | 3.6 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_20_chern_tknn/report_A20.pdf` | 5.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_20_chern_tknn/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_20_chern_tknn/logs/computation_log_A20L.txt` | 151 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_20_chern_tknn/logs/stdout_capture_A20L.txt` | 2.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/animation_A20P.gif` | 26.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_01_A20P.png` | 52.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_02_A20P.png` | 50.2 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_03_A20P.png` | 49.8 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_04_A20P.png` | 65.3 KB | — | Supplementary figure 4 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_05.png` | 47.4 KB | — | Supplementary figure 5 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_21_gamma_phase/README.md` | 5.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_21_gamma_phase/report_A21.docx` | 5.0 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_21_gamma_phase/report_A21.html` | 2.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_21_gamma_phase/report_A21.md` | 2.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_21_gamma_phase/report_A21.pdf` | 3.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_21_gamma_phase/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_21_gamma_phase/logs/computation_log_A21L.txt` | 138 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_21_gamma_phase/logs/stdout_capture_A21L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_21_gamma_phase/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_21_gamma_phase/plots/animation_A21P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_21_gamma_phase/plots/plot_01_A21P.png` | 47.3 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_22_ab_phase/README.md` | 5.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_22_ab_phase/report_A22.docx` | 4.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_22_ab_phase/report_A22.html` | 2.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_22_ab_phase/report_A22.md` | 2.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_22_ab_phase/report_A22.pdf` | 3.2 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_22_ab_phase/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_22_ab_phase/logs/computation_log_A22L.txt` | 138 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_22_ab_phase/logs/stdout_capture_A22L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_22_ab_phase/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_22_ab_phase/plots/animation_A22P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_22_ab_phase/plots/plot_01_A22P.png` | 47.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_23_fractal_factor/README.md` | 6.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_23_fractal_factor/report_A23.docx` | 4.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_23_fractal_factor/report_A23.html` | 2.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_23_fractal_factor/report_A23.md` | 2.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_23_fractal_factor/report_A23.pdf` | 3.1 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_23_fractal_factor/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_23_fractal_factor/logs/computation_log_A23L.txt` | 135 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_23_fractal_factor/logs/stdout_capture_A23L.txt` | 1.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_23_fractal_factor/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_23_fractal_factor/plots/animation_A23P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_23_fractal_factor/plots/plot_01_A23P.png` | 47.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/README.md` | 6.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.docx` | 5.7 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.html` | 3.2 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.md` | 2.9 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.pdf` | 4.4 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/logs/computation_log_A24L.txt` | 642 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/logs/stdout_capture_A24L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/plots/animation_A24P.gif` | 10.1 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/plots/plot_01_A24P.png` | 48.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_25_byers_yang/README.md` | 7.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_25_byers_yang/report_A25.docx` | 6.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_25_byers_yang/report_A25.html` | 4.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_25_byers_yang/report_A25.md` | 4.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_25_byers_yang/report_A25.pdf` | 5.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_25_byers_yang/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_25_byers_yang/logs/computation_log_A25L.txt` | 1.6 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_25_byers_yang/logs/stdout_capture_A25L.txt` | 1.5 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_25_byers_yang/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_25_byers_yang/plots/animation_A25P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_25_byers_yang/plots/plot_01_A25P.png` | 47.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_26_pbc_torus/README.md` | 7.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_26_pbc_torus/report_A26.docx` | 7.0 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_26_pbc_torus/report_A26.html` | 4.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_26_pbc_torus/report_A26.md` | 4.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_26_pbc_torus/report_A26.pdf` | 5.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_26_pbc_torus/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_26_pbc_torus/logs/computation_log_A26L.txt` | 1.5 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_26_pbc_torus/logs/stdout_capture_A26L.txt` | 1.6 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_26_pbc_torus/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_26_pbc_torus/plots/animation_A26P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_26_pbc_torus/plots/plot_01_A26P.png` | 48.0 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_27_binary_chiral/README.md` | 10.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_27_binary_chiral/report_A27.docx` | 9.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_27_binary_chiral/report_A27.html` | 7.2 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_27_binary_chiral/report_A27.md` | 6.7 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_27_binary_chiral/report_A27.pdf` | 9.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_27_binary_chiral/logs/README.md` | 2.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_27_binary_chiral/logs/computation_log_A27L.txt` | 1.8 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_27_binary_chiral/logs/stdout_capture_A27L.txt` | 3.3 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/animation_A27P.gif` | 30.0 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_01_A27P.png` | 92.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_02_A27P.png` | 54.1 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_03_A27P.png` | 48.5 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/README.md` | 7.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.docx` | 6.6 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.html` | 4.0 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.md` | 3.6 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.pdf` | 5.4 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/logs/computation_log_A28L.txt` | 1.4 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_28_f_gue_merit/logs/stdout_capture_A28L.txt` | 1.2 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/README.md` | 1.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/animation_A28P.gif` | 15.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_01_A28P.png` | 66.1 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_02_A28P.png` | 47.3 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_29_dirac_dip/README.md` | 8.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_29_dirac_dip/report_A29.docx` | 7.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_29_dirac_dip/report_A29.html` | 5.1 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_29_dirac_dip/report_A29.md` | 4.7 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_29_dirac_dip/report_A29.pdf` | 6.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_29_dirac_dip/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_29_dirac_dip/logs/computation_log_A29L.txt` | 1.6 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_29_dirac_dip/logs/stdout_capture_A29L.txt` | 2.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/README.md` | 1.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/animation_A29P.gif` | 23.4 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_01_A29P.png` | 64.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_02_A29P.png` | 55.6 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_03_A29P.png` | 56.7 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_04_A29P.png` | 47.6 KB | — | Supplementary figure 4 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_30_vf_scaling/README.md` | 8.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_30_vf_scaling/report_A30.docx` | 7.6 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_30_vf_scaling/report_A30.html` | 5.0 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_30_vf_scaling/report_A30.md` | 4.6 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_30_vf_scaling/report_A30.pdf` | 6.5 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_30_vf_scaling/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_30_vf_scaling/logs/computation_log_A30L.txt` | 1.6 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_30_vf_scaling/logs/stdout_capture_A30L.txt` | 1.8 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/animation_A30P.gif` | 31.1 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_01_A30P.png` | 58.9 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_02_A30P.png` | 47.3 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_03_A30P.png` | 47.4 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/README.md` | 9.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.docx` | 10.1 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.html` | 7.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.md` | 7.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.pdf` | 9.9 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/logs/computation_log_A31L.txt` | 2.8 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_31_hatano_nelson/logs/stdout_capture_A31L.txt` | 3.1 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/animation_A31P.gif` | 22.3 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_01_A31P.png` | 62.3 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_02_A31P.png` | 57.3 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_03_A31P.png` | 58.8 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_04_A31P.png` | 48.1 KB | — | Supplementary figure 4 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/README.md` | 12.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.docx` | 16.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.html` | 13.9 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.md` | 13.5 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.pdf` | 18.9 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/computation_log_A32L.txt` | 4.8 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/stdout_capture_A32L.txt` | 5.9 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/animation_A32P.gif` | 5.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/plot_01_A32P.png` | 47.6 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/README.md` | 12.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.docx` | 22.4 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.html` | 19.6 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.md` | 19.2 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.pdf` | 25.8 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/computation_log_A33L.txt` | 12.3 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/stdout_capture_A33L.txt` | 4.3 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/README.md` | 1.4 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/animation_A33P.gif` | 10.1 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/plot_01_A33P.png` | 53.5 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/README.md` | 8.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.docx` | 6.7 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.html` | 4.0 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.md` | 3.6 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.pdf` | 5.3 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/README.md` | 2.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/computation_log_A34L.txt` | 812 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/stdout_capture_A34L.txt` | 1.6 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/README.md` | 1.7 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/animation_A34P.gif` | 26.7 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_01_A34P.png` | 61.4 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_02_A34P.png` | 56.8 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_03_A34P.png` | 47.5 KB | — | Supplementary figure 3 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/README.md` | 7.1 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.docx` | 6.3 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.html` | 3.6 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.md` | 3.2 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.pdf` | 4.9 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/logs/computation_log_A35L.txt` | 798 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/logs/stdout_capture_A35L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/README.md` | 1.6 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/animation_A35P.gif` | 17.9 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_01_A35P.png` | 68.8 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_02_A35P.png` | 46.9 KB | — | Supplementary figure 2 of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_36_byte_robust/README.md` | 11.8 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_36_byte_robust/report_A36.docx` | 24.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_36_byte_robust/report_A36.html` | 22.3 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_36_byte_robust/report_A36.md` | 21.9 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_36_byte_robust/report_A36.pdf` | 29.9 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_36_byte_robust/logs/README.md` | 2.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_36_byte_robust/logs/computation_log_A36L.txt` | 15.7 KB | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_36_byte_robust/logs/stdout_capture_A36L.txt` | 3.6 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_36_byte_robust/plots/README.md` | 1.3 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/README.md` | 7.0 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.docx` | 5.9 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.html` | 3.4 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.md` | 3.0 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.pdf` | 4.1 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/computation_log_A37L.txt` | 162 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/stdout_capture_A37L.txt` | 1.4 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/animation_A37P.gif` | 11.2 KB | — | Animated reveal of this test's figure(s). |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/plot_01_A37P.png` | 47.3 KB | — | Primary result figure of the test (ABPlotV23 engine, supersampled). |
| `run_data/run_20260914_234626/test_38_curie_point/README.md` | 8.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_38_curie_point/report_A38.docx` | 11.8 KB | — | Editable edition of the same report (Microsoft Word). |
| `run_data/run_20260914_234626/test_38_curie_point/report_A38.html` | 9.5 KB | — | Web edition of the same report (self-contained HTML). |
| `run_data/run_20260914_234626/test_38_curie_point/report_A38.md` | 9.1 KB | — | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `run_data/run_20260914_234626/test_38_curie_point/report_A38.pdf` | 15.0 KB | — | Print edition of the same report (PDF). |
| `run_data/run_20260914_234626/test_38_curie_point/logs/README.md` | 1.9 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_38_curie_point/logs/computation_log_A38L.txt` | 172 B | — | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `run_data/run_20260914_234626/test_38_curie_point/logs/stdout_capture_A38L.txt` | 7.0 KB | — | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |
| `run_data/run_20260914_234626/test_38_curie_point/plots/README.md` | 1.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260914_234626/test_38_curie_point/plots/t38_curie_panels.png` | 131.9 KB | — | Multi-panel summary figure of the Curie-point battery: order parameter, susceptibility and the GUE/GOE lean across the transition. |
| `run_data/run_20260917_080329_m2/FINAL_REPORT_B.md` | 3.3 KB | — | The consolidated final report (Markdown) — all statistics, per-realization table, forensics and verdict blocks. |
| `run_data/run_20260917_080329_m2/README.md` | 3.6 KB | `unpacked/run_data/run_20260917_080329_m2/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260917_080329_m2/README_original.md` | 1.5 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `run_data/run_20260917_080329_m2/config_B.json` | 393 B | — | The run configuration (JSON). |
| `run_data/run_20260917_080329_m2/data_R2.csv` | 7.6 KB | — | Pooled R₂(s) table: AB and ζ blocks + GUE theory, s = 0.01…3.00 step 0.02. |
| `run_data/run_20260917_080329_m2/data_realizations_B.csv` | 1.9 KB | — | Per-realization statistics table. |
| `run_data/run_20260917_080329_m2/data_spacings.csv` | 1.5 MB | — | The pooled unfolded spacing arrays (91,360 AB spacings; 49,999 ζ spacings). |
| `run_data/run_20260917_080329_m2/index_B.html` | 6.9 KB | — | The run's self-contained dashboard (opens in any browser). |
| `run_data/run_20260917_080329_m2/plot_01_R2_comparison.png` | 51.0 KB | — | Pooled R₂(s) comparison figure: AB cloud vs ζ zeros vs GUE theory. |
| `run_data/run_20260917_080329_m2/plot_03_spacing_pdf.png` | 53.9 KB | — | Pooled spacing PDF comparison figure: AB cloud vs ζ zeros vs GUE surmise. |
| `run_data/run_20260917_080329_m2/analysis_addendum/README.md` | 3.2 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260917_080329_m2/analysis_addendum/fig_add1_w_sweep_en_BA.png` | 472.0 KB | — | Addendum figure 1 — the disorder (W) sweep: the confrontation distance stays flat as disorder grows (Add.3). |
| `run_data/run_20260917_080329_m2/analysis_addendum/fig_add2_mixture_en_BA.png` | 426.8 KB | — | Addendum figure 2 — the effective GUE+Poisson mixture decomposition; post-fit residual 0.0241 vs the GUE-matrix calibration floor 0.0242 (Add.5). |
| `run_data/run_20260917_080329_m2/analysis_addendum/m3_mixture_fit_summary.json` | 902 B | — | Single-realization mixture-fit summary for the MODE 3 diagnostics run (companion to the pooled summary). |
| `run_data/run_20260917_080329_m2/analysis_addendum/pooled_mixture_fit_summary.json` | 990 B | — | Pooled mixture-fit summary: w* = 0.281 KS / 0.247 L2, residual 0.0241, bootstrap CI [0.0744, 0.0798], short-range fractions, differential extrema. |
| `run_data/run_20260917_084900_m3/README.md` | 3.5 KB | `unpacked/run_data/run_20260917_084900_m3/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260917_084900_m3/README_original.md` | 1.4 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `run_data/run_20260917_084900_m3/data_cdf_differential.csv` | 12.4 KB | — | The signed CDF difference F_AB − F_ζ table behind the differential-CDF panel. |
| `run_data/run_20260917_084900_m3/plot_01_cdf_differential.png` | 45.9 KB | — | Differential CDF panel F_AB − F_ζ (max +0.0913 @ s=0.65; zero crossing s≈1.05). |
| `run_data/run_20260917_084900_m3/plot_02_short_range.png` | 52.6 KB | — | Short-range repulsion zone panel: P(s) for s < 1.2, AB vs ζ. |
| `run_data/run_20260917_084900_m3/plot_03_seed_forensics.png` | 39.6 KB | — | Seed forensics panel: 5 seeds, D ∈ [0.0926, 0.1012] — no seed lottery. |
| `run_data/run_20260917_084900_m3/plot_04_lattice_scaling.png` | 30.3 KB | — | Finite-size probe D(L) at L = 48/64/96 — flat. |
| `run_data/run_20260917_084900_m3/plot_05_bootstrap.png` | 43.6 KB | — | Bootstrap of d_GUE, 300 resamples, 95% CI [0.0633, 0.0868]. |
| `run_data/run_20260917_084900_m3/plot_06_cdf.png` | 48.1 KB | — | Full CDF comparison vs GUE/Poisson/ζ. |
| `run_data/run_20260919_085734_m2/FINAL_REPORT_D.md` | 3.5 KB | — | The consolidated final report (Markdown) — all statistics, per-realization table, forensics and verdict blocks. |
| `run_data/run_20260919_085734_m2/README.md` | 3.7 KB | `unpacked/run_data/run_20260919_085734_m2/README_original.md` | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260919_085734_m2/README_original.md` | 1.7 KB | — | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `run_data/run_20260919_085734_m2/config_D.json` | 1.6 KB | — | The run configuration (JSON). |
| `run_data/run_20260919_085734_m2/data_realizations_D.csv` | 481 B | — | Per-realization statistics table. |
| `run_data/run_20260919_085734_m2/logs/README.md` | 2.5 KB | — | Folder documentation (generated for this GitHub edition). |
| `run_data/run_20260919_085734_m2/logs/console_capture_raw.txt` | 11.1 KB | — | The raw console capture as received (IM-wrapped progress lines; final blocks complete). |
| `run_data/run_20260919_085734_m2/logs/console_output.txt` | 3.1 KB | — | The cleaned console protocol: config header, per-realization table, pooled line, forensics, composite verdict (complete blocks). |

## Register of renamed files

| Original path (in the ZIP) | Published path |
|---|---|
| `AB_Cloud_v23_Monograph.docx` | `unpacked/AB_Cloud_v23_Monograph_ROOT.docx` |
| `AB_Cloud_v23_Monograph.pdf` | `unpacked/AB_Cloud_v23_Monograph_ROOT.pdf` |
| `Monograph/AB_Cloud_v23_Monograph.docx` | `unpacked/Monograph/AB_Cloud_v23_Monograph_MG.docx` |
| `Monograph/AB_Cloud_v23_Monograph.pdf` | `unpacked/Monograph/AB_Cloud_v23_Monograph_MG.pdf` |
| `README.md` | `unpacked/README_original.md` |
| `lab_standalone/README.md` | `unpacked/lab_standalone/README_original.md` |
| `preprint/addendum_figures/fig_add1_w_sweep_en.png` | `unpacked/preprint/addendum_figures/fig_add1_w_sweep_en_P1A.png` |
| `preprint/addendum_figures/fig_add2_mixture_en.png` | `unpacked/preprint/addendum_figures/fig_add2_mixture_en_P1A.png` |
| `preprint2/addendum_figures/fig_add1_w_sweep_en.png` | `unpacked/preprint2/addendum_figures/fig_add1_w_sweep_en_P2A.png` |
| `preprint2/addendum_figures/fig_add2_mixture_en.png` | `unpacked/preprint2/addendum_figures/fig_add2_mixture_en_P2A.png` |
| `python_clone/README.md` | `unpacked/python_clone/README_original.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/final_report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/final_report_AF.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_01_bN_convergence/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_02_bN_monotonicity/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_03_bN_rate/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_04_gue_ks_full/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_05_gue_ks_highT/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_06_chi2_hist/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_07_decay_slope/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_08_residuals/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_09_bootstrap_ci/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_10_cross_validation/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_11_anderson_darling/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_12_two_sample_ks/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_13_number_variance/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_14_spectral_rigidity/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_15_ab_construction/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_16_ab_gue_class/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_17_connes_self_duality/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_18_chiral_AIII/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_19_dirac_cone/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_20_chern_tknn/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_21_gamma_phase/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_22_ab_phase/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_23_fractal_factor/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_24_dirac_string_flux/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_25_byers_yang/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_26_pbc_torus/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_27_binary_chiral/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_28_f_gue_merit/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_29_dirac_dip/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_30_vf_scaling/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_31_hatano_nelson/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_32_rmean_bootstrap/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_33_l_scaling_rmean/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_34_direct_vs_zeta/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_35_form_factor_Kt/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_36_byte_robust/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_37_half_factorial_gamma/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/computation_log.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/computation_log_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/logs/test_38_curie_point/stdout_capture_XX.txt` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_01_bN_convergence/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_02_bN_monotonicity/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_03_bN_rate/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_04_gue_ks_full/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_05_gue_ks_highT/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_06_chi2_hist/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_07_decay_slope/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_08_residuals/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_09_bootstrap_ci/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_10_cross_validation/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_11_anderson_darling/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_12_two_sample_ks/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_13_number_variance/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_14_spectral_rigidity/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_15_ab_construction/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_16_ab_gue_class/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_17_connes_self_duality/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_18_chiral_AIII/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_19_dirac_cone/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_20_chern_tknn/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_21_gamma_phase/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_22_ab_phase/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_23_fractal_factor/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_24_dirac_string_flux/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_25_byers_yang/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_26_pbc_torus/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_27_binary_chiral/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_28_f_gue_merit/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_29_dirac_dip/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_30_vf_scaling/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_31_hatano_nelson/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_32_rmean_bootstrap/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_33_l_scaling_rmean/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_34_direct_vs_zeta/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_35_form_factor_Kt/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_36_byte_robust/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_37_half_factorial_gamma/report_XX.pdf` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report.docx` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.docx` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report.html` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.html` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report.md` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.md` |
| `run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report.pdf` | `unpacked/run_data/run_20260914_234626/FINAL_REPORT/reports/test_38_curie_point/report_XX.pdf` |
| `run_data/run_20260914_234626/index.html` | `unpacked/run_data/run_20260914_234626/index_A.html` |
| `run_data/run_20260914_234626/test_01_bN_convergence/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/logs/computation_log_A01L.txt` |
| `run_data/run_20260914_234626/test_01_bN_convergence/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/logs/stdout_capture_A01L.txt` |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/plots/animation_A01P.gif` |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_01_A01P.png` |
| `run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/plots/plot_02_A01P.png` |
| `run_data/run_20260914_234626/test_01_bN_convergence/report.docx` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/report_A01.docx` |
| `run_data/run_20260914_234626/test_01_bN_convergence/report.html` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/report_A01.html` |
| `run_data/run_20260914_234626/test_01_bN_convergence/report.md` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/report_A01.md` |
| `run_data/run_20260914_234626/test_01_bN_convergence/report.pdf` | `unpacked/run_data/run_20260914_234626/test_01_bN_convergence/report_A01.pdf` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/logs/computation_log_A02L.txt` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/logs/stdout_capture_A02L.txt` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/plots/animation_A02P.gif` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/plots/plot_01_A02P.png` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report.docx` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.docx` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report.html` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.html` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report.md` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.md` |
| `run_data/run_20260914_234626/test_02_bN_monotonicity/report.pdf` | `unpacked/run_data/run_20260914_234626/test_02_bN_monotonicity/report_A02.pdf` |
| `run_data/run_20260914_234626/test_03_bN_rate/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/logs/computation_log_A03L.txt` |
| `run_data/run_20260914_234626/test_03_bN_rate/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/logs/stdout_capture_A03L.txt` |
| `run_data/run_20260914_234626/test_03_bN_rate/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/plots/animation_A03P.gif` |
| `run_data/run_20260914_234626/test_03_bN_rate/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/plots/plot_01_A03P.png` |
| `run_data/run_20260914_234626/test_03_bN_rate/report.docx` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/report_A03.docx` |
| `run_data/run_20260914_234626/test_03_bN_rate/report.html` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/report_A03.html` |
| `run_data/run_20260914_234626/test_03_bN_rate/report.md` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/report_A03.md` |
| `run_data/run_20260914_234626/test_03_bN_rate/report.pdf` | `unpacked/run_data/run_20260914_234626/test_03_bN_rate/report_A03.pdf` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/logs/computation_log_A04L.txt` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/logs/stdout_capture_A04L.txt` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/plots/animation_A04P.gif` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/plots/plot_01_A04P.png` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report.docx` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.docx` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report.html` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.html` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report.md` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.md` |
| `run_data/run_20260914_234626/test_04_gue_ks_full/report.pdf` | `unpacked/run_data/run_20260914_234626/test_04_gue_ks_full/report_A04.pdf` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/logs/computation_log_A05L.txt` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/logs/stdout_capture_A05L.txt` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/plots/animation_A05P.gif` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/plots/plot_01_A05P.png` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report.docx` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.docx` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report.html` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.html` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report.md` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.md` |
| `run_data/run_20260914_234626/test_05_gue_ks_highT/report.pdf` | `unpacked/run_data/run_20260914_234626/test_05_gue_ks_highT/report_A05.pdf` |
| `run_data/run_20260914_234626/test_06_chi2_hist/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/logs/computation_log_A06L.txt` |
| `run_data/run_20260914_234626/test_06_chi2_hist/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/logs/stdout_capture_A06L.txt` |
| `run_data/run_20260914_234626/test_06_chi2_hist/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/plots/animation_A06P.gif` |
| `run_data/run_20260914_234626/test_06_chi2_hist/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/plots/plot_01_A06P.png` |
| `run_data/run_20260914_234626/test_06_chi2_hist/report.docx` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/report_A06.docx` |
| `run_data/run_20260914_234626/test_06_chi2_hist/report.html` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/report_A06.html` |
| `run_data/run_20260914_234626/test_06_chi2_hist/report.md` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/report_A06.md` |
| `run_data/run_20260914_234626/test_06_chi2_hist/report.pdf` | `unpacked/run_data/run_20260914_234626/test_06_chi2_hist/report_A06.pdf` |
| `run_data/run_20260914_234626/test_07_decay_slope/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/logs/computation_log_A07L.txt` |
| `run_data/run_20260914_234626/test_07_decay_slope/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/logs/stdout_capture_A07L.txt` |
| `run_data/run_20260914_234626/test_07_decay_slope/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/plots/animation_A07P.gif` |
| `run_data/run_20260914_234626/test_07_decay_slope/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/plots/plot_01_A07P.png` |
| `run_data/run_20260914_234626/test_07_decay_slope/report.docx` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/report_A07.docx` |
| `run_data/run_20260914_234626/test_07_decay_slope/report.html` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/report_A07.html` |
| `run_data/run_20260914_234626/test_07_decay_slope/report.md` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/report_A07.md` |
| `run_data/run_20260914_234626/test_07_decay_slope/report.pdf` | `unpacked/run_data/run_20260914_234626/test_07_decay_slope/report_A07.pdf` |
| `run_data/run_20260914_234626/test_08_residuals/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_08_residuals/logs/computation_log_A08L.txt` |
| `run_data/run_20260914_234626/test_08_residuals/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_08_residuals/logs/stdout_capture_A08L.txt` |
| `run_data/run_20260914_234626/test_08_residuals/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_08_residuals/plots/animation_A08P.gif` |
| `run_data/run_20260914_234626/test_08_residuals/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_08_residuals/plots/plot_01_A08P.png` |
| `run_data/run_20260914_234626/test_08_residuals/report.docx` | `unpacked/run_data/run_20260914_234626/test_08_residuals/report_A08.docx` |
| `run_data/run_20260914_234626/test_08_residuals/report.html` | `unpacked/run_data/run_20260914_234626/test_08_residuals/report_A08.html` |
| `run_data/run_20260914_234626/test_08_residuals/report.md` | `unpacked/run_data/run_20260914_234626/test_08_residuals/report_A08.md` |
| `run_data/run_20260914_234626/test_08_residuals/report.pdf` | `unpacked/run_data/run_20260914_234626/test_08_residuals/report_A08.pdf` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/logs/computation_log_A09L.txt` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/logs/stdout_capture_A09L.txt` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/plots/animation_A09P.gif` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/plots/plot_01_A09P.png` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report.docx` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.docx` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report.html` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.html` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report.md` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.md` |
| `run_data/run_20260914_234626/test_09_bootstrap_ci/report.pdf` | `unpacked/run_data/run_20260914_234626/test_09_bootstrap_ci/report_A09.pdf` |
| `run_data/run_20260914_234626/test_10_cross_validation/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/logs/computation_log_A10L.txt` |
| `run_data/run_20260914_234626/test_10_cross_validation/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/logs/stdout_capture_A10L.txt` |
| `run_data/run_20260914_234626/test_10_cross_validation/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/plots/animation_A10P.gif` |
| `run_data/run_20260914_234626/test_10_cross_validation/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/plots/plot_01_A10P.png` |
| `run_data/run_20260914_234626/test_10_cross_validation/report.docx` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/report_A10.docx` |
| `run_data/run_20260914_234626/test_10_cross_validation/report.html` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/report_A10.html` |
| `run_data/run_20260914_234626/test_10_cross_validation/report.md` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/report_A10.md` |
| `run_data/run_20260914_234626/test_10_cross_validation/report.pdf` | `unpacked/run_data/run_20260914_234626/test_10_cross_validation/report_A10.pdf` |
| `run_data/run_20260914_234626/test_11_anderson_darling/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/logs/computation_log_A11L.txt` |
| `run_data/run_20260914_234626/test_11_anderson_darling/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/logs/stdout_capture_A11L.txt` |
| `run_data/run_20260914_234626/test_11_anderson_darling/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/plots/animation_A11P.gif` |
| `run_data/run_20260914_234626/test_11_anderson_darling/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/plots/plot_01_A11P.png` |
| `run_data/run_20260914_234626/test_11_anderson_darling/report.docx` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/report_A11.docx` |
| `run_data/run_20260914_234626/test_11_anderson_darling/report.html` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/report_A11.html` |
| `run_data/run_20260914_234626/test_11_anderson_darling/report.md` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/report_A11.md` |
| `run_data/run_20260914_234626/test_11_anderson_darling/report.pdf` | `unpacked/run_data/run_20260914_234626/test_11_anderson_darling/report_A11.pdf` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/logs/computation_log_A12L.txt` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/logs/stdout_capture_A12L.txt` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/plots/animation_A12P.gif` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/plots/plot_01_A12P.png` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report.docx` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.docx` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report.html` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.html` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report.md` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.md` |
| `run_data/run_20260914_234626/test_12_two_sample_ks/report.pdf` | `unpacked/run_data/run_20260914_234626/test_12_two_sample_ks/report_A12.pdf` |
| `run_data/run_20260914_234626/test_13_number_variance/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/logs/computation_log_A13L.txt` |
| `run_data/run_20260914_234626/test_13_number_variance/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/logs/stdout_capture_A13L.txt` |
| `run_data/run_20260914_234626/test_13_number_variance/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/plots/animation_A13P.gif` |
| `run_data/run_20260914_234626/test_13_number_variance/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/plots/plot_01_A13P.png` |
| `run_data/run_20260914_234626/test_13_number_variance/report.docx` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/report_A13.docx` |
| `run_data/run_20260914_234626/test_13_number_variance/report.html` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/report_A13.html` |
| `run_data/run_20260914_234626/test_13_number_variance/report.md` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/report_A13.md` |
| `run_data/run_20260914_234626/test_13_number_variance/report.pdf` | `unpacked/run_data/run_20260914_234626/test_13_number_variance/report_A13.pdf` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/logs/computation_log_A14L.txt` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/logs/stdout_capture_A14L.txt` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/plots/animation_A14P.gif` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/plots/plot_01_A14P.png` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report.docx` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.docx` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report.html` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.html` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report.md` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.md` |
| `run_data/run_20260914_234626/test_14_spectral_rigidity/report.pdf` | `unpacked/run_data/run_20260914_234626/test_14_spectral_rigidity/report_A14.pdf` |
| `run_data/run_20260914_234626/test_15_ab_construction/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/logs/computation_log_A15L.txt` |
| `run_data/run_20260914_234626/test_15_ab_construction/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/logs/stdout_capture_A15L.txt` |
| `run_data/run_20260914_234626/test_15_ab_construction/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/plots/animation_A15P.gif` |
| `run_data/run_20260914_234626/test_15_ab_construction/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/plots/plot_01_A15P.png` |
| `run_data/run_20260914_234626/test_15_ab_construction/report.docx` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/report_A15.docx` |
| `run_data/run_20260914_234626/test_15_ab_construction/report.html` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/report_A15.html` |
| `run_data/run_20260914_234626/test_15_ab_construction/report.md` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/report_A15.md` |
| `run_data/run_20260914_234626/test_15_ab_construction/report.pdf` | `unpacked/run_data/run_20260914_234626/test_15_ab_construction/report_A15.pdf` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/logs/computation_log_A16L.txt` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/logs/stdout_capture_A16L.txt` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/plots/animation_A16P.gif` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_01_A16P.png` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_02_A16P.png` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/plots/plot_03_A16P.png` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report.docx` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.docx` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report.html` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.html` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report.md` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.md` |
| `run_data/run_20260914_234626/test_16_ab_gue_class/report.pdf` | `unpacked/run_data/run_20260914_234626/test_16_ab_gue_class/report_A16.pdf` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/logs/computation_log_A17L.txt` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/logs/stdout_capture_A17L.txt` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/plots/animation_A17P.gif` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/plots/plot_01_A17P.png` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report.docx` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.docx` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report.html` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.html` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report.md` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.md` |
| `run_data/run_20260914_234626/test_17_connes_self_duality/report.pdf` | `unpacked/run_data/run_20260914_234626/test_17_connes_self_duality/report_A17.pdf` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/logs/computation_log_A18L.txt` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/logs/stdout_capture_A18L.txt` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/plots/animation_A18P.gif` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/plots/plot_01_A18P.png` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report.docx` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.docx` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report.html` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.html` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report.md` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.md` |
| `run_data/run_20260914_234626/test_18_chiral_AIII/report.pdf` | `unpacked/run_data/run_20260914_234626/test_18_chiral_AIII/report_A18.pdf` |
| `run_data/run_20260914_234626/test_19_dirac_cone/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/logs/computation_log_A19L.txt` |
| `run_data/run_20260914_234626/test_19_dirac_cone/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/logs/stdout_capture_A19L.txt` |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/plots/animation_A19P.gif` |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_01_A19P.png` |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_02_A19P.png` |
| `run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/plots/plot_03_A19P.png` |
| `run_data/run_20260914_234626/test_19_dirac_cone/report.docx` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/report_A19.docx` |
| `run_data/run_20260914_234626/test_19_dirac_cone/report.html` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/report_A19.html` |
| `run_data/run_20260914_234626/test_19_dirac_cone/report.md` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/report_A19.md` |
| `run_data/run_20260914_234626/test_19_dirac_cone/report.pdf` | `unpacked/run_data/run_20260914_234626/test_19_dirac_cone/report_A19.pdf` |
| `run_data/run_20260914_234626/test_20_chern_tknn/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/logs/computation_log_A20L.txt` |
| `run_data/run_20260914_234626/test_20_chern_tknn/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/logs/stdout_capture_A20L.txt` |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/plots/animation_A20P.gif` |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_01_A20P.png` |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_02_A20P.png` |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_03_A20P.png` |
| `run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_04.png` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/plots/plot_04_A20P.png` |
| `run_data/run_20260914_234626/test_20_chern_tknn/report.docx` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/report_A20.docx` |
| `run_data/run_20260914_234626/test_20_chern_tknn/report.html` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/report_A20.html` |
| `run_data/run_20260914_234626/test_20_chern_tknn/report.md` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/report_A20.md` |
| `run_data/run_20260914_234626/test_20_chern_tknn/report.pdf` | `unpacked/run_data/run_20260914_234626/test_20_chern_tknn/report_A20.pdf` |
| `run_data/run_20260914_234626/test_21_gamma_phase/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/logs/computation_log_A21L.txt` |
| `run_data/run_20260914_234626/test_21_gamma_phase/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/logs/stdout_capture_A21L.txt` |
| `run_data/run_20260914_234626/test_21_gamma_phase/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/plots/animation_A21P.gif` |
| `run_data/run_20260914_234626/test_21_gamma_phase/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/plots/plot_01_A21P.png` |
| `run_data/run_20260914_234626/test_21_gamma_phase/report.docx` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/report_A21.docx` |
| `run_data/run_20260914_234626/test_21_gamma_phase/report.html` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/report_A21.html` |
| `run_data/run_20260914_234626/test_21_gamma_phase/report.md` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/report_A21.md` |
| `run_data/run_20260914_234626/test_21_gamma_phase/report.pdf` | `unpacked/run_data/run_20260914_234626/test_21_gamma_phase/report_A21.pdf` |
| `run_data/run_20260914_234626/test_22_ab_phase/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/logs/computation_log_A22L.txt` |
| `run_data/run_20260914_234626/test_22_ab_phase/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/logs/stdout_capture_A22L.txt` |
| `run_data/run_20260914_234626/test_22_ab_phase/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/plots/animation_A22P.gif` |
| `run_data/run_20260914_234626/test_22_ab_phase/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/plots/plot_01_A22P.png` |
| `run_data/run_20260914_234626/test_22_ab_phase/report.docx` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/report_A22.docx` |
| `run_data/run_20260914_234626/test_22_ab_phase/report.html` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/report_A22.html` |
| `run_data/run_20260914_234626/test_22_ab_phase/report.md` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/report_A22.md` |
| `run_data/run_20260914_234626/test_22_ab_phase/report.pdf` | `unpacked/run_data/run_20260914_234626/test_22_ab_phase/report_A22.pdf` |
| `run_data/run_20260914_234626/test_23_fractal_factor/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/logs/computation_log_A23L.txt` |
| `run_data/run_20260914_234626/test_23_fractal_factor/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/logs/stdout_capture_A23L.txt` |
| `run_data/run_20260914_234626/test_23_fractal_factor/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/plots/animation_A23P.gif` |
| `run_data/run_20260914_234626/test_23_fractal_factor/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/plots/plot_01_A23P.png` |
| `run_data/run_20260914_234626/test_23_fractal_factor/report.docx` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/report_A23.docx` |
| `run_data/run_20260914_234626/test_23_fractal_factor/report.html` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/report_A23.html` |
| `run_data/run_20260914_234626/test_23_fractal_factor/report.md` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/report_A23.md` |
| `run_data/run_20260914_234626/test_23_fractal_factor/report.pdf` | `unpacked/run_data/run_20260914_234626/test_23_fractal_factor/report_A23.pdf` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/logs/computation_log_A24L.txt` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/logs/stdout_capture_A24L.txt` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/plots/animation_A24P.gif` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/plots/plot_01_A24P.png` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report.docx` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.docx` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report.html` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.html` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report.md` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.md` |
| `run_data/run_20260914_234626/test_24_dirac_string_flux/report.pdf` | `unpacked/run_data/run_20260914_234626/test_24_dirac_string_flux/report_A24.pdf` |
| `run_data/run_20260914_234626/test_25_byers_yang/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/logs/computation_log_A25L.txt` |
| `run_data/run_20260914_234626/test_25_byers_yang/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/logs/stdout_capture_A25L.txt` |
| `run_data/run_20260914_234626/test_25_byers_yang/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/plots/animation_A25P.gif` |
| `run_data/run_20260914_234626/test_25_byers_yang/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/plots/plot_01_A25P.png` |
| `run_data/run_20260914_234626/test_25_byers_yang/report.docx` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/report_A25.docx` |
| `run_data/run_20260914_234626/test_25_byers_yang/report.html` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/report_A25.html` |
| `run_data/run_20260914_234626/test_25_byers_yang/report.md` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/report_A25.md` |
| `run_data/run_20260914_234626/test_25_byers_yang/report.pdf` | `unpacked/run_data/run_20260914_234626/test_25_byers_yang/report_A25.pdf` |
| `run_data/run_20260914_234626/test_26_pbc_torus/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/logs/computation_log_A26L.txt` |
| `run_data/run_20260914_234626/test_26_pbc_torus/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/logs/stdout_capture_A26L.txt` |
| `run_data/run_20260914_234626/test_26_pbc_torus/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/plots/animation_A26P.gif` |
| `run_data/run_20260914_234626/test_26_pbc_torus/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/plots/plot_01_A26P.png` |
| `run_data/run_20260914_234626/test_26_pbc_torus/report.docx` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/report_A26.docx` |
| `run_data/run_20260914_234626/test_26_pbc_torus/report.html` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/report_A26.html` |
| `run_data/run_20260914_234626/test_26_pbc_torus/report.md` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/report_A26.md` |
| `run_data/run_20260914_234626/test_26_pbc_torus/report.pdf` | `unpacked/run_data/run_20260914_234626/test_26_pbc_torus/report_A26.pdf` |
| `run_data/run_20260914_234626/test_27_binary_chiral/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/logs/computation_log_A27L.txt` |
| `run_data/run_20260914_234626/test_27_binary_chiral/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/logs/stdout_capture_A27L.txt` |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/plots/animation_A27P.gif` |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_01_A27P.png` |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_02_A27P.png` |
| `run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/plots/plot_03_A27P.png` |
| `run_data/run_20260914_234626/test_27_binary_chiral/report.docx` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/report_A27.docx` |
| `run_data/run_20260914_234626/test_27_binary_chiral/report.html` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/report_A27.html` |
| `run_data/run_20260914_234626/test_27_binary_chiral/report.md` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/report_A27.md` |
| `run_data/run_20260914_234626/test_27_binary_chiral/report.pdf` | `unpacked/run_data/run_20260914_234626/test_27_binary_chiral/report_A27.pdf` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/logs/computation_log_A28L.txt` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/logs/stdout_capture_A28L.txt` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/plots/animation_A28P.gif` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_01_A28P.png` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/plots/plot_02_A28P.png` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report.docx` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.docx` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report.html` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.html` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report.md` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.md` |
| `run_data/run_20260914_234626/test_28_f_gue_merit/report.pdf` | `unpacked/run_data/run_20260914_234626/test_28_f_gue_merit/report_A28.pdf` |
| `run_data/run_20260914_234626/test_29_dirac_dip/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/logs/computation_log_A29L.txt` |
| `run_data/run_20260914_234626/test_29_dirac_dip/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/logs/stdout_capture_A29L.txt` |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/plots/animation_A29P.gif` |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_01_A29P.png` |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_02_A29P.png` |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_03_A29P.png` |
| `run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_04.png` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/plots/plot_04_A29P.png` |
| `run_data/run_20260914_234626/test_29_dirac_dip/report.docx` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/report_A29.docx` |
| `run_data/run_20260914_234626/test_29_dirac_dip/report.html` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/report_A29.html` |
| `run_data/run_20260914_234626/test_29_dirac_dip/report.md` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/report_A29.md` |
| `run_data/run_20260914_234626/test_29_dirac_dip/report.pdf` | `unpacked/run_data/run_20260914_234626/test_29_dirac_dip/report_A29.pdf` |
| `run_data/run_20260914_234626/test_30_vf_scaling/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/logs/computation_log_A30L.txt` |
| `run_data/run_20260914_234626/test_30_vf_scaling/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/logs/stdout_capture_A30L.txt` |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/plots/animation_A30P.gif` |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_01_A30P.png` |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_02_A30P.png` |
| `run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/plots/plot_03_A30P.png` |
| `run_data/run_20260914_234626/test_30_vf_scaling/report.docx` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/report_A30.docx` |
| `run_data/run_20260914_234626/test_30_vf_scaling/report.html` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/report_A30.html` |
| `run_data/run_20260914_234626/test_30_vf_scaling/report.md` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/report_A30.md` |
| `run_data/run_20260914_234626/test_30_vf_scaling/report.pdf` | `unpacked/run_data/run_20260914_234626/test_30_vf_scaling/report_A30.pdf` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/logs/computation_log_A31L.txt` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/logs/stdout_capture_A31L.txt` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/plots/animation_A31P.gif` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_01_A31P.png` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_02_A31P.png` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_03_A31P.png` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_04.png` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/plots/plot_04_A31P.png` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report.docx` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.docx` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report.html` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.html` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report.md` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.md` |
| `run_data/run_20260914_234626/test_31_hatano_nelson/report.pdf` | `unpacked/run_data/run_20260914_234626/test_31_hatano_nelson/report_A31.pdf` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/computation_log_A32L.txt` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/logs/stdout_capture_A32L.txt` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/animation_A32P.gif` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/plots/plot_01_A32P.png` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report.docx` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.docx` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report.html` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.html` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report.md` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.md` |
| `run_data/run_20260914_234626/test_32_rmean_bootstrap/report.pdf` | `unpacked/run_data/run_20260914_234626/test_32_rmean_bootstrap/report_A32.pdf` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/computation_log_A33L.txt` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/logs/stdout_capture_A33L.txt` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/animation_A33P.gif` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/plots/plot_01_A33P.png` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report.docx` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.docx` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report.html` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.html` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report.md` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.md` |
| `run_data/run_20260914_234626/test_33_l_scaling_rmean/report.pdf` | `unpacked/run_data/run_20260914_234626/test_33_l_scaling_rmean/report_A33.pdf` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/computation_log_A34L.txt` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/logs/stdout_capture_A34L.txt` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/animation_A34P.gif` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_01_A34P.png` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_02_A34P.png` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_03.png` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/plots/plot_03_A34P.png` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report.docx` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.docx` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report.html` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.html` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report.md` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.md` |
| `run_data/run_20260914_234626/test_34_direct_vs_zeta/report.pdf` | `unpacked/run_data/run_20260914_234626/test_34_direct_vs_zeta/report_A34.pdf` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/logs/computation_log_A35L.txt` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/logs/stdout_capture_A35L.txt` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/plots/animation_A35P.gif` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_01_A35P.png` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_02.png` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/plots/plot_02_A35P.png` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report.docx` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.docx` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report.html` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.html` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report.md` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.md` |
| `run_data/run_20260914_234626/test_35_form_factor_Kt/report.pdf` | `unpacked/run_data/run_20260914_234626/test_35_form_factor_Kt/report_A35.pdf` |
| `run_data/run_20260914_234626/test_36_byte_robust/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/logs/computation_log_A36L.txt` |
| `run_data/run_20260914_234626/test_36_byte_robust/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/logs/stdout_capture_A36L.txt` |
| `run_data/run_20260914_234626/test_36_byte_robust/report.docx` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/report_A36.docx` |
| `run_data/run_20260914_234626/test_36_byte_robust/report.html` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/report_A36.html` |
| `run_data/run_20260914_234626/test_36_byte_robust/report.md` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/report_A36.md` |
| `run_data/run_20260914_234626/test_36_byte_robust/report.pdf` | `unpacked/run_data/run_20260914_234626/test_36_byte_robust/report_A36.pdf` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/computation_log_A37L.txt` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/logs/stdout_capture_A37L.txt` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/animation.gif` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/animation_A37P.gif` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/plot_01.png` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/plots/plot_01_A37P.png` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report.docx` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.docx` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report.html` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.html` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report.md` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.md` |
| `run_data/run_20260914_234626/test_37_half_factorial_gamma/report.pdf` | `unpacked/run_data/run_20260914_234626/test_37_half_factorial_gamma/report_A37.pdf` |
| `run_data/run_20260914_234626/test_38_curie_point/logs/computation_log.txt` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/logs/computation_log_A38L.txt` |
| `run_data/run_20260914_234626/test_38_curie_point/logs/stdout_capture.txt` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/logs/stdout_capture_A38L.txt` |
| `run_data/run_20260914_234626/test_38_curie_point/report.docx` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/report_A38.docx` |
| `run_data/run_20260914_234626/test_38_curie_point/report.html` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/report_A38.html` |
| `run_data/run_20260914_234626/test_38_curie_point/report.md` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/report_A38.md` |
| `run_data/run_20260914_234626/test_38_curie_point/report.pdf` | `unpacked/run_data/run_20260914_234626/test_38_curie_point/report_A38.pdf` |
| `run_data/run_20260917_080329_m2/FINAL_REPORT.md` | `unpacked/run_data/run_20260917_080329_m2/FINAL_REPORT_B.md` |
| `run_data/run_20260917_080329_m2/README.md` | `unpacked/run_data/run_20260917_080329_m2/README_original.md` |
| `run_data/run_20260917_080329_m2/analysis_addendum/fig_add1_w_sweep_en.png` | `unpacked/run_data/run_20260917_080329_m2/analysis_addendum/fig_add1_w_sweep_en_BA.png` |
| `run_data/run_20260917_080329_m2/analysis_addendum/fig_add2_mixture_en.png` | `unpacked/run_data/run_20260917_080329_m2/analysis_addendum/fig_add2_mixture_en_BA.png` |
| `run_data/run_20260917_080329_m2/config.json` | `unpacked/run_data/run_20260917_080329_m2/config_B.json` |
| `run_data/run_20260917_080329_m2/data_realizations.csv` | `unpacked/run_data/run_20260917_080329_m2/data_realizations_B.csv` |
| `run_data/run_20260917_080329_m2/index.html` | `unpacked/run_data/run_20260917_080329_m2/index_B.html` |
| `run_data/run_20260917_084900_m3/README.md` | `unpacked/run_data/run_20260917_084900_m3/README_original.md` |
| `run_data/run_20260919_085734_m2/FINAL_REPORT.md` | `unpacked/run_data/run_20260919_085734_m2/FINAL_REPORT_D.md` |
| `run_data/run_20260919_085734_m2/README.md` | `unpacked/run_data/run_20260919_085734_m2/README_original.md` |
| `run_data/run_20260919_085734_m2/config.json` | `unpacked/run_data/run_20260919_085734_m2/config_D.json` |
| `run_data/run_20260919_085734_m2/data_realizations.csv` | `unpacked/run_data/run_20260919_085734_m2/data_realizations_D.csv` |

Checksums of every published file: [`SHA256SUMS_unpacked.txt`](SHA256SUMS_unpacked.txt). The original freeze's own register (original names) ships at `unpacked/SHA256SUMS.txt`.
