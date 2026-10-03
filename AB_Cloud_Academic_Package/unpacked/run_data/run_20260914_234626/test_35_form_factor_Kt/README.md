# Test 35: Spectral form factor K(t) — folder `test_35_form_factor_Kt/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 08:17:49
**Verdicts (verbatim register):** WARN  
**Family:** STATISTICAL family (two-point form factor)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_35_form_factor_Kt/](README.md)
## 1. What this folder is
Test 35 extends the confrontation to the spectral form factor K(t): the raw Fourier statistic (1/n)|Σ e^{itε}|² of the unfolded levels is compared against the finite-box GUE reference K_box(t) = t·(1 − sinc(2πt)), with the RMS deviation over t ≥ 0.3 as the verdict statistic. The audit battery 35b carried two failed sub-checks of three (WARN) — the last of the run's four honest blemishes.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_35_form_factor_Kt/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The spectral form factor is the two-point correlation function in Fourier dress: where R₂(s) describes level correlations in the spacing domain, K(t) describes them in the time domain, and the two are Fourier twins. Its inclusion makes the confrontation layer complete — the ζ zeros and the lattice are compared in both representations, and the finite-box reference (rather than the infinite-volume asymptotics) keeps the comparison honest at the accessible system size. The 35b WARN is analysed in the monograph's Appendix C alongside the other three blemish batteries: the audit-tier sub-checks of the form-factor comparison were the record's most sensitive instrument to the same ζ-side unfolding issues that the v3.2 estimator audit resolved, and the September 2026 addendum's corrected-constants chapter (Add.6) revisits the reference side of this comparison. The monograph's form-factor chapter derives K_box from first principles and walks through the RMS verdict line preserved in this folder's console capture.
## 3. What the test verifies (verbatim from the run's report)
> Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3. METHOD: Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3. Test 35 HARDCORE pass 2: n=5 per-realization K(t), 33-point t-grid, ensemble mean verdict. Test 35 HARDCORE: ensemble RMS=0.6143, corr_box=0.6379, corr_ζ=0.8123, RMS scatter σ=0.1856.
## 4. Verdict lines of the reference run (verbatim)
> Test 35: K(t) ramp+plateau — RMS_GUE=0.4193, corr_GUE=0.8889 → WARN
> Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
## 5. Result line
```text
Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A35.docx` | 6.3 KB | Editable edition of the same report (Microsoft Word). |
| `report_A35.html` | 3.6 KB · 45 lines | Web edition of the same report (self-contained HTML). |
| `report_A35.md` | 3.2 KB · 55 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A35.pdf` | 4.9 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[07:55:52.491] [+29343.519s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[07:59:57.563] [+29588.591s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:04:08.314] [+29839.342s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:08:42.332] [+30113.360s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:13:04.889] [+30375.917s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 35 (pass 2, HARDCORE): spectral form factor K(t) — ensemble pass
n ≥ 5 per-realization K(t), 33-point t-grid, ensemble verdict
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 → expect ≈ 12–17 min
 real  1/5: RMS(K−K_box, t≥0.3) = 0.9199
 real  2/5: RMS(K−K_box, t≥0.3) = 0.8578
 real  3/5: RMS(K−K_box, t≥0.3) = 0.9671
 real  4/5: RMS(K−K_box, t≥0.3) = 0.7540
 real  5/5: RMS(K−K_box, t≥0.3) = 0.4999

 ENSEMBLE K(t): RMS(K_AB − K_box, t ≥ 0.3) = 0.6143 (target < 0.30)
 Corr(K_AB, K_box) = 0.6379 (target > 0.50) | Corr(K_AB, K_ζ) = 0.8123
 Per-realization RMS: mean 0.7998, scatter σ = 0.1856 > ✗ 0.15
────────────────────────────────────────────────────────────
 RMS < 0.30 (ensemble) WARN — ensemble-mean K(t), 33-point grid: 0.6143
 Corr > 0.50 (ensemble) PASS — Corr(K, K_box) = 0.6379
 RMS scatter ≤ 0.15   WARN — σ=0.1856 across 5 realizations
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 35 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 35` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 35 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_34](../test_34_direct_vs_zeta/README.md) · [test_36](../test_36_byte_robust/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
