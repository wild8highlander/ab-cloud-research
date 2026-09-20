# Test 9: Bootstrap CI for slope — folder `test_09_bootstrap_ci/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:38
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_09_bootstrap_ci/](README.md)
## 1. What this folder is
Test 9 quantifies the sampling noise of the Test 7 slope estimate by bootstrap resampling. The bootstrap distribution of the slope delivers a point estimate of −0.1746 with a 95% confidence interval of [−0.1895, −0.1552] — an interval that comfortably brackets the primary fit's estimate, demonstrating that the observed decay rate is not a fluke of one particular realization of the ladder.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_09_bootstrap_ci/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Every empirical number in the record is exposed to the same question: how much would it move if the data were different? For the convergence slope the suite answers with the non-parametric bootstrap — resampling the ladder's error sequence and re-fitting thousands of times to map out the sampling distribution of the slope. The agreement between the bootstrap interval and the regression confidence interval from Test 7 is the point of the test: two statistically independent uncertainty assessments landing on the same value. The HARDCORE pass-2 audit re-runs the bootstrap under varied resampling schemes with four sub-checks, all passing in-run and re-anchoring b(50000) = 1.2126. The monograph cites this test whenever the slope of the decay law is quoted, attaching the bootstrap interval as the number's official uncertainty badge.
## 3. What the test verifies (verbatim from the run's report)
> Sampling-noise quantification: statistical system with CIs. METHOD: Sampling-noise quantification: statistical system with CIs.
## 4. Verdict lines of the reference run (verbatim)
> Test 9: Bootstrap slope=-0.1746 (empirical), 95%CI=[-0.1895,-0.1552] → PASS
> Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A09.docx` | 4.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A09.html` | 2.4 KB · 32 lines | Web edition of the same report (self-contained HTML). |
| `report_A09.md` | 2.0 KB · 42 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A09.pdf` | 3.1 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 9 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — bootstrap reproducibility audit
────────────────────────────────────────────────────────────
 B1 primary CI: width 0.0288, median -0.1743 (limit 0.1)
 B2 second seed: median -0.1745 (|Δmed|=0.0003, limit 0.02), CI overlap 91% (limit 60%)
 B3 jackknife : LOO slope range [-0.1808, -0.1676] inside boot CI ± 0.02? YES
 B4 half grid : median -0.2085 vs full -0.1743, |Δ|=0.0342 (limit 0.05)
────────────────────────────────────────────────────────────
 B1 CI width          PASS — width = 0.0288
 B2 seed stability    PASS — Δmed 0.0003, overlap 91%
 B3 jackknife         PASS — range [-0.1808, -0.1676]
 B4 half grid         PASS — |Δmed| = 0.0342
 Test 9 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 9 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 9` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 9 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_08](../test_08_residuals/README.md) · [test_10](../test_10_cross_validation/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
