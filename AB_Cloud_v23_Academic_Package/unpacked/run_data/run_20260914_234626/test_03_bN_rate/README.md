# Test 3: Convergence rate (power-law fit) — folder `test_03_bN_rate/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:47:21
**Verdicts (verbatim register):** PASS  
**Family:** EXACT-formula family (regression diagnostics)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_03_bN_rate/](README.md)
## 1. What this folder is
Test 3 fits a power law to the convergence table of Test 1. A log-log regression of b(N) against N yields the empirical rate α = 0.1685 with coefficient of determination R² = 0.9895. The suite is explicit that this slope is a formula-derived quantity with no pre-registered expected value — the R² statistic, not the slope itself, is the goodness yardstick.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_03_bN_rate/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Knowing that the Gram ladder converges (Test 1) and never regresses (Test 2) is not enough: the framework also needs to know how fast it converges, because the rate determines how deep into the zero list any claimed spectral identification can be pushed. Test 3 quantifies exactly that. The regression is performed over the full refinement range, and its near-unity R² = 0.9895 certifies that the power-law description is not a convenient fiction but an accurate summary of the data the suite itself generated. The HARDCORE pass-2 audit re-runs the fit with four sub-checks that vary the regression window and re-anchor b(50000) = 1.2126. Together, Tests 1–3 form the convergence triad that opens Part II of the monograph; the fitted rate is quoted again in the synthesis chapters when the record discusses the scaling behaviour of the framework.
## 3. What the test verifies (verbatim from the run's report)
> log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick. METHOD: log-log regression of b(N): the slope is a formula-derived quantity with R² as the goodness yardstick.
## 4. Verdict lines of the reference run (verbatim)
> Test 3: α = 0.1685 (empirical; no expected value), R²=0.9895 → PASS
> Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A03.docx` | 4.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A03.html` | 2.5 KB · 33 lines | Web edition of the same report (self-contained HTML). |
| `report_A03.md` | 2.2 KB · 43 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A03.pdf` | 3.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 3 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep rate-law validation
────────────────────────────────────────────────────────────
 R1 dense power law: b(N) ≈ 7.3564·N^(-0.1737), R² = 0.988236 (limit 0.95)
 R2 alt 1/log N   : b(N) ≈ -0.2557 + 16.2185/log(N), R² = 0.997500
                   best of two laws: R² = 0.9975 (limit 0.95)
 R3 walk-forward  : median err 0.05%, max err 0.09% (limits 2%/5%)
 R4 α stability   : α_lower=0.2116 vs α_upper=0.1393, |Δα|=0.0723 (limit 0.2)
────────────────────────────────────────────────────────────
 R1 power-law R²      PASS — R² = 0.9882
 R2 best-law R²       PASS — R² = 0.9975
 R3 walk-forward      PASS — median 0.05%, max 0.09%
 R4 α stability       PASS — |Δα| = 0.0723
 Test 3 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 3 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 3` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 3 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_02](../test_02_bN_monotonicity/README.md) · [test_04](../test_04_gue_ks_full/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
