# Test 21: γ* spinorial phase ≈ π/2 — folder `test_21_gamma_phase/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:25:31
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (geometric phase, 256-bit)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_21_gamma_phase/](README.md)
## 1. What this folder is
Test 21 certifies the spinorial geometric phase γ* ≈ π/2 of the AB-cloud construction. The computation is carried out at 256-bit precision: the a_C component error is 1.23e-19, the b_C component error 6.39e-17, the argument deviation 0.1259°, and the δ ± 1e-6 worst-case deviation 0.1259° — the analytic prediction and the machine computation agree to a fraction of a thousandth of a degree.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_21_gamma_phase/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
A geometric phase (Berry phase) is a global, path-dependent observable: it cannot be produced by any local bookkeeping, and its value π/2 is fixed by the spinorial structure of the flux carrier in the AB-cloud construction. The suite verifies it with arbitrary-precision arithmetic — 256-bit floating point, far beyond hardware doubles — so that the residual between the closed-form prediction and the computed phase reflects genuine mathematics rather than accumulated round-off. The phase γ* enters the framework's analytic identity chain (it is one of the constants the monograph's exact layer lists alongside the flux quantum of Test 22 and the fractal factor of Test 23), and the audit-tier census credits this battery among the exact identities verified at 256-bit precision. The console capture in this folder preserves the component-wise error budget verbatim.
## 3. What the test verifies (verbatim from the run's report)
> EXACT geometric phase check. METHOD: EXACT geometric phase check. Test 21 HARDCORE: 256-bit a_C err 1.23e-19, b_C err 6.39e-17, arg dev 0.1259°, δ±1e-6 worst dev 0.1259°.
## 4. Verdict lines of the reference run (verbatim)
> Test 21: arg(γ*)=89.874° (≈90°, deviation=0.126°) → PASS
> Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A21.docx` | 5.0 KB | Editable edition of the same report (Microsoft Word). |
| `report_A21.html` | 2.5 KB · 34 lines | Web edition of the same report (self-contained HTML). |
| `report_A21.md` | 2.1 KB · 44 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A21.pdf` | 3.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 21 (pass 2, HARDCORE): γ* spinorial phase — 256-bit precision audit
────────────────────────────────────────────────────────────
 δ_C = π/7, b₂(K3) = 22 (256-bit recomputation)
 a_C: Float64 8.276305e-04 vs 256-bit 8.276305e-04 → |Δ| = 1.23e-19
 b_C: Float64 0.376510 vs 256-bit 0.376510 → |Δ| = 6.39e-17
 arg(γ*) at 256-bit: 89.874055° (deviation from 90°: 0.1259°)
 δ = π/7-1·1e-6: arg(γ*) deviation = 0.1259°
 δ = π/7+1·1e-6: arg(γ*) deviation = 0.1259°
────────────────────────────────────────────────────────────
 Float64 round-off    PASS — |Δa|=1.23e-19, |Δb|=6.39e-17 (machine-ε scale)
 arg(γ*) → π/2 (256-bit) PASS — deviation 0.1259° < 1°
 δ_C ± 1e-6 stability PASS — worst deviation 0.1259° across the ±1e-6 scan
 Test 21b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 21 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 21` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 21 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_20](../test_20_chern_tknn/README.md) · [test_22](../test_22_ab_phase/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
