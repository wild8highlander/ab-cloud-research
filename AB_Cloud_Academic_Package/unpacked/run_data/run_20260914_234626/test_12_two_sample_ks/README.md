# Test 12: Real zeros vs GUE matrix — folder `test_12_two_sample_ks/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:56:59
**Verdicts (verbatim register):** WARN  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_12_two_sample_ks/](README.md)
## 1. What this folder is
Test 12 replaces the theoretical surmise with a live opponent: a simulated GUE matrix spectrum. A two-sample Kolmogorov–Smirnov test compares the unfolded ζ-zero spacings against the spacings of eigenlevels drawn from an explicitly constructed GUE matrix ensemble, reporting D = 0.0265 with p = 0.005252 at pass 1 and a split verdict at the HARDCORE audit (2 of 3 sub-checks failed → WARN).
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_12_two_sample_ks/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
This is the record's only head-to-head meeting between the ζ data and actual random matrices rather than analytic formulae, and its honest outcome is part of what makes the package credible: it is one of the four audit-tier batteries carrying failed sub-checks (12b in the audit census), and the monograph analyses it rather than burying it. The two-sample design removes the surmise's small-n approximations from the equation — whatever the simulated matrix spectrum does, finite-size included, the data are compared against it directly. The outcome fed directly into the v3.2 estimator audit: the ζ-side unfolding used at reference-run time was identified as the dominant contributor to the residual two-sample distance, the defect was repaired, and the post-fix falsifiable window (D = 0.03–0.06) was pre-registered in Appendix C. The September 2026 addendum chain (Add.2, Add.5, Add.8) then demonstrated in the standalone laboratory and on the Klein quartic that the confrontation lands inside that window with the corrected pipeline.
## 3. What the test verifies (verbatim from the run's report)
> Two-sample KS: data vs simulated GUE matrix spectrum. METHOD: Two-sample KS: data vs simulated GUE matrix spectrum.
## 4. Verdict lines of the reference run (verbatim)
> Test 12: 2-sample KS D=0.0265, p=0.005252 → WARN
> Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
## 5. Result line
```text
Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A12.docx` | 4.7 KB | Editable edition of the same report (Microsoft Word). |
| `report_A12.html` | 2.3 KB · 31 lines | Web edition of the same report (self-contained HTML). |
| `report_A12.md` | 1.9 KB · 41 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A12.pdf` | 3.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 12 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — 2KS symmetry audit
────────────────────────────────────────────────────────────
 Full: real n=8400 vs ref n=8400, D=0.026548, p=0.005252 (primary verdict governs)
 W1 ref split : D_vs_A=0.024405, D_vs_B=0.030238, |ΔD|=0.005833 (limit 0.02)
 W2 blocks    : 0/4 blocks agree with full verdict at α=0.01 (limit ≥ 3)
 W3 effect    : D_full=0.026548 < 2KS critical at α=0.01: 0.025151? NO
────────────────────────────────────────────────────────────
 W1 ref symmetry      PASS — |ΔD| = 0.005833
 W2 block agree       WARN — 0/4 agree
 W3 D bound           WARN — D 0.0265 vs crit 0.0252
 Test 12 [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 12 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 12` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 12 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_11](../test_11_anderson_darling/README.md) · [test_13](../test_13_number_variance/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
