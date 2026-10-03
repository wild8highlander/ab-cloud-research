# Test 10: Cross-validation stability — folder `test_10_cross_validation/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:46
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_10_cross_validation/](README.md)
## 1. What this folder is
Test 10 is the stability station of the convergence block: the log-log fit of Test 7 is re-performed under cross-validation — the data are split, the fit is trained on one part and evaluated on the other, and the deviation between out-of-sample predictions and observations is measured. The primary pass reports a maximum deviation of 8.5% across the splits.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_10_cross_validation/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Cross-validation is borrowed from predictive modelling: a description of the data that only describes the data it was fitted to is worthless, and the split-half deviation is the cheapest way to demonstrate otherwise. For the convergence record the meaning is concrete — the power-law description of the Gram ladder's decay, fitted on early portions of the ladder, predicts the later portions to within 8.5%, which is the number the monograph quotes as the predictive stability of the convergence law within the accessible range. The HARDCORE pass-2 audit formalises the check with four sub-checks over alternative split geometries, all passed in-run, again re-anchoring b(50000) = 1.2126. Readers of Part II will find this test cited in the synthesis of the convergence triad as the bridge between descriptive accuracy (Tests 7–8) and predictive reliability (this test).
## 3. What the test verifies (verbatim from the run's report)
> Statistical stability of the fit under data splits. METHOD: Statistical stability of the fit under data splits.
## 4. Verdict lines of the reference run (verbatim)
> Test 10: Max deviation=8.5% → PASS
> Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A10.docx` | 4.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A10.html` | 2.5 KB · 34 lines | Web edition of the same report (self-contained HTML). |
| `report_A10.md` | 2.1 KB · 44 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A10.pdf` | 3.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 10 (secondary, HARDCORE): deep cross-validation audit
All sub-samples use index-aware Gram points (offset discipline)
────────────────────────────────────────────────────────────
 V1 deciles   : 0 local increases over 10 segment means (limit 0)
 V2 f-sweep   : dev(0.3)=0.0019 → dev(0.9)=0.0006 (must decrease)
                devs: 0.0019 / 0.0011 / 0.0005 / 0.0006
 V3 tripwire  : correct-offset tail b=1.1095, wrong-offset b=19559.2539 → +1762824.6% worse (limit ≥ 5%)
 V4 even-odd  : b_even=1.208457 vs full 1.212553, dev=0.34% (limit 10%)
────────────────────────────────────────────────────────────
 V1 deciles           PASS — 0 increases / 10 segments
 V2 f-convergence     PASS — dev 0.19% → 0.06%
 V3 offset tripwire   PASS — wrong offset +1762824.6% worse
 V4 even-odd          PASS — dev = 0.34%
 Test 10 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 10 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 10` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 10 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_09](../test_09_bootstrap_ci/README.md) · [test_11](../test_11_anderson_darling/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
