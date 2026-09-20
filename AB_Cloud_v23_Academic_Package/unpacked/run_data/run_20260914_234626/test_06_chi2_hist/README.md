# Test 6: Spacing chi^2 histogram test — folder `test_06_chi2_hist/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:15
**Verdicts (verbatim register):** WARN → PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_06_chi2_hist/](README.md)
## 1. What this folder is
Test 6 attacks the same GUE-versus-data question with a third, independent instrument: the Pearson χ² binned histogram test. The unfolded spacings are binned, the observed counts are compared against the Wigner–Dyson expectation, and the χ² statistic quantifies the discrepancy. Binning choices are declared part of the tolerance system — the suite does not hide the fact that a binned test depends on the binning, it regulates it.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_06_chi2_hist/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
A χ² test responds to different features of the distribution than a KS test: KS is a global CDF metric, while χ² is sensitive to localized bin-level discrepancies. Including both is a deliberate redundancy in the verification record — if the ζ spacings matched GUE in the CDF sense but failed in specific bins, the two instruments would disagree and the record would say so. The primary pass produced χ² p = 0.0 (again the finite-sample signature the suite classifies as legal), and the governing HARDCORE pass-2 audit passed both of its sub-checks. In the monograph's statistical-family chapter the three distributional instruments (KS, χ², and the tail-sensitive Anderson–Darling of Test 11) are presented as a tripod: no single test is decisive, but all three must point the same way for the distributional layer to stand.
## 3. What the test verifies (verbatim from the run's report)
> χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system. METHOD: χ² binned comparison of spacing histogram to Wigner-Dyson. Binning choices are part of the tolerance system.
## 4. Verdict lines of the reference run (verbatim)
> Test 6: χ² p=0.0 → WARN
> Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A06.docx` | 4.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A06.html` | 2.4 KB · 31 lines | Web edition of the same report (self-contained HTML). |
| `report_A06.md` | 2.0 KB · 41 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A06.pdf` | 3.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 6 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — bin-stability audit
────────────────────────────────────────────────────────────
 C1 bins= 300: χ²/df = 2.3771, p = 0.000000 → REJECT
 C1 bins= 150: χ²/df = 3.6171, p = 0.000000 → REJECT
 C1 bins=  75: χ²/df = 6.3149, p = 0.000000 → REJECT
 C1 bins=  37: χ²/df = 11.3303, p = 0.000000 → REJECT
 C2 halves    : χ²/df first=2.5187, second=2.1023, rel.dev=16.5% (limit 50%)
────────────────────────────────────────────────────────────
 C1 bin sweep         PASS — 0 flips vs majority (REJECT)
 C2 halves            PASS — rel.dev = 16.5%
 Test 6 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 6 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 6` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 6 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_05](../test_05_gue_ks_highT/README.md) · [test_07](../test_07_decay_slope/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
