<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-results%20·%20flagship-00E5FF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# ⭐ `run_20260902_134759` — the flagship v19 two-pass run

> **The 37-test two-pass run of 2026-09-02 (72×72 → 96×96, HARDCORE second pass, pass-3 series for tests 19/29/31) that monograph v22 is built on.**

This is **the** canonical artifact set of the v19 era: one folder, thirty-seven `test_NN_<name>/` experiment directories, and the consolidated `FINAL_REPORT/`. First pass closed at **32 PASS / 5 WARN** (the five statistical WARNs of the Wigner-surmise floor — tests 4, 5, 6, 11, 12, 28, 35 in the register semantics), the HARDCORE second pass re-examined every completion and closed **all PASS (77 verdict lines total)**, and a pass-3 series resolved the stragglers 19/29/31. Julia 1.12.0, 50 000 Odlyzko zeros.

Nothing in this folder has been regenerated or reformatted after the run — it is committed exactly as produced, which is what makes it a *reference*: any later run of `ab_cloud_full.jl` can be diffed against this one line by line. The sibling file [`ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt`](../ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt) holds the raw header/config dump, and the monographs in [`../../../monographs/`](../../../monographs/) cite their numbers from here.

## 🗺️ Anatomy of a test directory

Every `test_NN_<name>/` folder follows the same layout: `report.md` / `report.html` / `report.pdf` (the verdict, the estimator settings and the key numbers), and `logs/` with the raw computation stream. Tests that produced data tables ship them next to the report. Test numbering matches the register in the root README and in `docs/results.md`, so a register row that says *test 17* points at `test_17_*/report.md` in this folder.

## 🔁 Reproducing the run

Run `julia --project=. code/ab_cloud_full.jl` from the repository root (v23 is the current estimator-valid code state; the v19-era artifacts here were produced by the suite state documented in [`code/julia/`](../../../code/julia/)). A full two-pass run takes hours and is CPU-bound; `--quick` shrinks it for smoke tests. Any discrepancy against this folder is a bug report by the rules of [`CONTRIBUTING.md`](../../../CONTRIBUTING.md).

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| `FINAL_REPORT/` | folder | 6 items | consolidated final report (`final_report.md`/`.html`/`.pdf`/`.docx`) + `logs/` + per-test `reports/` — start here |
| [`index.html`](index.html) | HTML | 14.4 KB | interactive landing page for the whole run (per-test cards, verdicts, timings) |
| `test_01_bN_convergence/` | folder | 5 items | b(N) = 1.2126 at N = 50,000 — finite-size correction converged — ledger verdict `PASS` |
| `test_02_bN_monotonicity/` | folder | 5 items | 0 monotonicity violations across 499 windows — ledger verdict `PASS` |
| `test_03_bN_rate/` | folder | 5 items | power-law fit b(N) ≈ 7.0312 · N^(−0.1685), R² = 0.9895; 1/log alternative R² = 0.9994 — ledger verdict `PASS` |
| `test_04_gue_ks_full/` | folder | 5 items | full-range KS: D = 0.0881, p ≈ 0 — finite-T rejection is the expected behaviour — ledger verdict `FAIL/WARN → expected` |
| `test_05_gue_ks_highT/` | folder | 5 items | high-T cut T_min = 10³/10⁴: D = 0.0878 / 0.0866; true GUE needs T ≫ 10⁶ — ledger verdict `FAIL/WARN → expected` |
| `test_06_chi2_hist/` | folder | 5 items | χ² histogram at 150/300/600 bins: 6170 / 6276 / 6384 — same finite-T story — ledger verdict `FAIL/WARN → expected` |
| `test_07_decay_slope/` | folder | 5 items | decay slope −0.1504, 95% CI [−0.1594, −0.1414] — ledger verdict `PASS` |
| `test_08_residuals/` | folder | 5 items | Wald–Wolfowitz runs test: 3 runs (expected 5.8), residuals structureless — ledger verdict `PASS` |
| `test_09_bootstrap_ci/` | folder | 5 items | bootstrap slope −0.1746, 95% CI [−0.1895, −0.1552] — ledger verdict `PASS` |
| `test_10_cross_validation/` | folder | 5 items | max cross-validation deviation 8.5% — ledger verdict `PASS` |
| `test_11_anderson_darling/` | folder | 5 items | Anderson–Darling battery — 5 sub-checks, 0 failed (hardcore pass 2) — ledger verdict `PASS` |
| `test_12_two_sample_ks/` | folder | 5 items | two-sample KS D = 0.0233, p = 0.0105; pass 2: 3 sub-checks clean — ledger verdict `WARN → PASS` |
| `test_13_number_variance/` | folder | 5 items | number variance closer to GUE in **9 / 9** L-values — ledger verdict `PASS` |
| `test_14_spectral_rigidity/` | folder | 5 items | spectral rigidity Δ₃ closer to GUE in **9 / 9** L-values — ledger verdict `PASS` |
| `test_15_ab_construction/` | folder | 5 items | Hermiticity OK; τ_TRB = 0.1037; vortex flux −0.0 exact — ledger verdict `PASS` |
| `test_16_ab_gue_class/` | folder | 5 items | ⟨r⟩ = 0.594 at α = 0.5 — AB-cloud sits in the GUE class — ledger verdict `PASS` |
| `test_17_connes_self_duality/` | folder | 5 items | zero modes at α = 1/2: **4 (expected 4)**; C₁ = 2 — ledger verdict `PASS` |
| `test_18_chiral_AIII/` | folder | 5 items | chiral defect 0.0 at α = 1/2; 0.0058 at α = 1/3 (non-zero as required) — ledger verdict `PASS` |
| `test_19_dirac_cone/` | folder | 5 items | E_min ∝ 1/L with **R² = 0.9997**; v_F(2π) = 1.8998, v_F(π) = 3.7995 — ledger verdict `PASS` |
| `test_20_chern_tknn/` | folder | 5 items | C₁ anchors {1/4, 1/3, 1/5} = 1, 1, 1; min gap at α = 1/2 = 0.0 (Dirac touching) — ledger verdict `PASS` |
| `test_21_gamma_phase/` | folder | 5 items | arg(γ*) = 89.874° — deviation from 90° only **0.126°** — ledger verdict `PASS` |
| `test_22_ab_phase/` | folder | 5 items | Φ_AB = **0.4487989505 = π/7 (exact to all digits)** — ledger verdict `PASS` |
| `test_23_fractal_factor/` | folder | 5 items | closed-form factor = 1.0 by construction; c_AB = 0.02062 ≈ 0.02063 — ledger verdict `PASS` |
| `test_24_dirac_string_flux/` | folder | 5 items | vortex flux 1/1; **5040/5040** empty plaquettes, max defect 0.0 — ledger verdict `PASS` |
| `test_25_byers_yang/` | folder | 5 items | Byers–Yang: Δ(q = 1→0) = 0.0; sensitivity Δ(q = 0.3→0) = 0.0032 > 10⁻³ — ledger verdict `PASS` |
| `test_26_pbc_torus/` | folder | 5 items | periodic torus: flux −0.0, empty 5040/5183, ⟨r⟩ = 0.6009 — ledger verdict `PASS` |
| `test_27_binary_chiral/` | folder | 5 items | chiral defect 0.0 (W = 0) vs 0.0058 (W = 1.0) — disorder response verified — ledger verdict `PASS` |
| `test_28_f_gue_merit/` | folder | 5 items | f_GUE merit = 0.8704, Σ²_data = 0.6115 — ledger verdict `WARN` |
| `test_29_dirac_dip/` | folder | 5 items | DOS dip: ρ(α = 0.5) = 0.0193 vs 0.1944 off-point — **~10× dip** — ledger verdict `PASS` |
| `test_30_vf_scaling/` | folder | 5 items | Fermi-velocity scaling v_F = 1.798, R² = 0.9977 — ledger verdict `PASS` |
| `test_31_hatano_nelson/` | folder | 5 items | non-Hermitian control: max \ — ledger verdict `Im E\` |
| `test_32_rmean_bootstrap/` | folder | 5 items | ⟨r⟩ = 0.5991 ± 0.0075 (replica 0.5864 ± 0.003) vs GUE 0.5992 — ledger verdict `PASS` |
| `test_33_l_scaling_rmean/` | folder | 5 items | L-scaling to L = 80: 0.434 → 0.556 → 0.593 → 0.600 → 0.600; plateau 0.6004, χ²/dof = 0.01 — ledger verdict `PASS` |
| `test_34_direct_vs_zeta/` | folder | 5 items | direct-vs-ζ spectra: ⟨\ — ledger verdict `ΔR₂\` |
| `test_35_form_factor_Kt/` | folder | 5 items | form factor K(t) ramp+plateau: RMS 0.4193, correlation 0.8889; MC 7× faster via table — ledger verdict `WARN` |
| `test_36_byte_robust/` | folder | 5 items | byte-robust statistics: r₂₅₆ = 0.5756–0.5894, \ — ledger verdict `Δr\` |
| `test_37_half_factorial_gamma/` | folder | 5 items | (1/2)! = √π/2 (rel. err 0.0); 32/π² identity; ∫p₂ = 1; uniqueness ✓ — ledger verdict `PASS` |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../../LICENSE).*

</div>
