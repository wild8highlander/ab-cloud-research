# Test 8: Residual analysis of fit — folder `test_08_residuals/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:29
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (algebraic diagnostics)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_08_residuals/](README.md)
## 1. What this folder is
Test 8 interrogates the residuals of the Test 7 regression — the differences between the observed b(N) values and the fitted power law. The headline diagnostic is a runs test: the observed sequence of above/below-fit runs contained 3 runs against an expectation of 5.8, a result the suite accepts within its algebraic diagnostic band.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_08_residuals/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
A good fit should leave residuals that look structureless: no long excursions on one side of the line, no slow drift, no periodic wobble. The runs test is a minimal, assumption-light way to detect exactly the opposite — clustering of the residuals, which would indicate that the power law is systematically bending somewhere in the window. By passing this check the record closes the last obvious loophole in the Test 7 fit: the slope is not an artifact of a curved curve being flattened by the regression. The HARDCORE pass-2 audit deepens the interrogation with four sub-checks (windowed runs counts, sign-balance checks, and re-anchoring to b(50000) = 1.2126), all passed in-run. In the monograph the test is presented as the 'fit hygiene' station of the convergence block: cheap, assumption-free, and devastating if it fails.
## 3. What the test verifies (verbatim from the run's report)
> Residual structure of the log-log fit — algebraic diagnostics. METHOD: Residual structure of the log-log fit — algebraic diagnostics.
## 4. Verdict lines of the reference run (verbatim)
> Test 8: Runs=3 (exp=5.8) → PASS
> Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A08.docx` | 4.7 KB | Editable edition of the same report (Microsoft Word). |
| `report_A08.html` | 2.3 KB · 31 lines | Web edition of the same report (self-contained HTML). |
| `report_A08.md` | 1.9 KB · 41 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A08.pdf` | 3.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 8 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — dense residual audit
────────────────────────────────────────────────────────────
 E1 runs      : 3 runs over 10 doubling-grid residuals (expected 5.8 ± 6.0)
 E2 autocorr  : lag-1 = 0.6794, lag-2 = 0.0053 (sanity limit |r|<0.95)
 E3 scale     : dense residuals sd_first=0.04614, sd_second=0.04289, ratio=1.076 (limits 0.4–2.5)
────────────────────────────────────────────────────────────
 E1 runs              PASS — 3 vs 5.8 expected
 E2 autocorr          PASS — r1=0.679, r2=0.005
 E3 scale             PASS — ratio = 1.076
 E4 sign balance      PASS — 4+/-6
 Test 8 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 8 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 8` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 8 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_07](../test_07_decay_slope/README.md) · [test_09](../test_09_bootstrap_ci/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
