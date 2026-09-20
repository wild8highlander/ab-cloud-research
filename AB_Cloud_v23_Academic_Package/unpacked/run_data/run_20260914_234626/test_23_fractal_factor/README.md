# Test 23: Complex fractal factor CF — folder `test_23_fractal_factor/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:25:52
**Verdicts (verbatim register):** PASS  
**Family:** Semi-statistical (curve comparison, 256-bit core)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_23_fractal_factor/](README.md)
## 1. What this folder is
Test 23 analyses the complex fractal factor CF of the construction — the log-periodic multiplicative correction that dresses the leading behaviour of the ladder. The 256-bit core certificate is exact: |CF| − 1 = 0.00e+00 (the modulus of the factor is exactly unity in arbitrary precision) and the imaginary exponent β carries error 3.04e-?? at 256 bits; the log-periodic curve is then compared semi-statistically against its prediction.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_23_fractal_factor/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Log-periodic corrections are the discrete-scale-invariance fingerprint of a self-similar structure: they oscillate in log-space with a fixed period determined by the scaling ratio, and their complex exponent encodes the fractal geometry of the underlying object. In the AB-cloud framework the fractal factor is the analytic remnant of the Gram-ladder's self-similar refinement, and the exact unity of its modulus is the statement that the correction renormalises phases without touching amplitudes — a conservation law in disguise. The test's hybrid design matches the object: the modulus and exponent are certified exactly at 256 bits, while the full log-periodic waveform is validated by curve comparison, the honest instrument for a continuous shape. The monograph's constants chapter discusses CF alongside γ* and δ_C as the three exact constants of the identity chain, each with its own certificate folder in this archive.
## 3. What the test verifies (verbatim from the run's report)
> Log-periodic factor — semi-statistical curve comparison. METHOD: Log-periodic factor — semi-statistical curve comparison. Test 23 HARDCORE: |CF|−1 = 0.00e+00 (256-bit), β err 3.04e-16 (Float64) / 3.28e-05 (LaTeX), c_AB err 6.82e-06.
## 4. Verdict lines of the reference run (verbatim)
> Test 23: |CF_formula|=1.0 (=1 by construction), c_AB=0.02062 (≈0.02063) → PASS
> Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A23.docx` | 4.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A23.html` | 2.5 KB · 32 lines | Web edition of the same report (self-contained HTML). |
| `report_A23.md` | 2.1 KB · 42 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A23.pdf` | 3.1 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 23 (pass 2, HARDCORE): complex fractal factor — 256-bit audit
────────────────────────────────────────────────────────────
 |CF| − 1 at 256-bit: 0.00e+00 (contract < 1e-30)
 β_imag: Float64 2.854032819406525 vs 256-bit 2.854032819406525 (|Δ| = 3.04e-16)
 β_imag vs LaTeX 2.854: |Δ| = 3.28e-05 (contract < 1e-3)
 c_AB = 1 − |CF_hard|: 0.020623 vs 0.02063 (|Δ| = 6.82e-06, contract < 1e-3)
────────────────────────────────────────────────────────────
 |CF| = 1 (1e-30)     PASS — pure-phase property at 256-bit: 0.00e+00
 β_imag anchors       PASS — Float64 |Δ|=3.04e-16; LaTeX 2.854 |Δ|=3.28e-05
 c_AB ≈ 0.02063       PASS — c_AB = 0.020623, |Δ| = 6.82e-06
 Test 23b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 23 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 23` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 23 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_22](../test_22_ab_phase/README.md) · [test_24](../test_24_dirac_string_flux/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
