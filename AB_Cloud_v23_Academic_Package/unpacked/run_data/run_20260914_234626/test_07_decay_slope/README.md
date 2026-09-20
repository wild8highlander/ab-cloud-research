# Test 7: Decay slope (log-log regression) — folder `test_07_decay_slope/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:21
**Verdicts (verbatim register):** PASS  
**Family:** EXACT-formula family (regression diagnostics)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_07_decay_slope/](README.md)
## 1. What this folder is
Test 7 measures how the Gram-ladder deviation b(N) decays at large N by fitting a straight line in log-log space to the large-T portion of the convergence table. The primary pass reports slope = −0.1504 with a 95% confidence interval of [−0.1594, −0.1414], the suite marking the slope as empirical — the fit's quality, not agreement with a pre-set constant, is what is audited.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_07_decay_slope/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The large-N decay of the approximation error is the quantity that determines how far up the zero ladder the framework's constructive identification remains numerically meaningful. A power-law decay (a straight line on a log-log plot) with a stable, tightly-bounded slope is the signature of a controlled approximation scheme; an erratic or steepening decay would signal an approach to a numerical noise floor rather than a genuine asymptotic regime. The HARDCORE pass-2 audit adds four sub-checks that re-fit the slope on shifted windows and re-verify the anchor value b(50000) = 1.2126, all passing in-run. The monograph's Chapter 7 uses this result — together with the bootstrap reproduction in Test 9 and the residual diagnostics of Test 8 — to argue that the decay regime observed within the accessible range is stable and well-described, while explicitly labelling the slope an empirical characteristic of the current ladder implementation.
## 3. What the test verifies (verbatim from the run's report)
> Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R². METHOD: Large-T decay of b(N): formula family (slope≈−0.5), verified via linear regression with R².
## 4. Verdict lines of the reference run (verbatim)
> Test 7: Slope=-0.1504 (empirical), 95%CI=[-0.1594,-0.1414] → PASS
> Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A07.docx` | 4.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A07.html` | 2.5 KB · 32 lines | Web edition of the same report (self-contained HTML). |
| `report_A07.md` | 2.1 KB · 42 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A07.pdf` | 3.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 7 (secondary, HARDCORE): Objection 3: Large-T Decay Rate — deep slope validation
────────────────────────────────────────────────────────────
 D1 slope     : -0.1504, 95%CI [-0.1594, -0.1414] (width 0.0179), R²=0.9954 (limits 0.1 / 0.9)
 D2 stability : slope_lo=-0.1752, slope_hi=-0.1385, |Δ|=0.0367 (limit 0.15)
 D3 walk-fwd  : median err 0.05%, max err 0.09% (limits 2%/5%)
 D4 bootstrap : slope=-0.1504 inside boot 95%CI [-0.1621, -0.1378]? YES
────────────────────────────────────────────────────────────
 D1 slope CI          PASS — width 0.0179, R² 0.9954
 D2 stability         PASS — |Δslope| = 0.0367
 D3 walk-forward      PASS — median 0.05%, max 0.09%
 D4 boot vs CI        PASS — CI [-0.1621, -0.1378]
 Test 7 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 7 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 7` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 7 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_06](../test_06_chi2_hist/README.md) · [test_08](../test_08_residuals/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
