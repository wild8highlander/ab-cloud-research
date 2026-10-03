# Test 4: GUE KS test (full range) — folder `test_04_gue_ks_full/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:52:57
**Verdicts (verbatim register):** WARN → PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_04_gue_ks_full/](README.md)
## 1. What this folder is
Test 4 is the first distributional test of the record and the first direct confrontation between the ζ-zero spacing statistics and the GUE (Gaussian Unitary Ensemble) Wigner surmise. A one-sample Kolmogorov–Smirnov test is applied to the full unfolded spacing set (n = 49,999 spacings over the entire embedded range), yielding D = 0.021619 with asymptotic p = 9.57e-21 — a small D against a formally tiny p, which the suite flags and manages as a finite-data effect: at this sample size the KS p-value is hypersensitive, and p-values 'depend on sample size and T-range — finite-data effects are legal'.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_04_gue_ks_full/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
This is the test that addresses Montgomery's pair-correlation conjecture head-on: if the ζ zeros behave like GUE eigenlevels, their unfolded nearest-neighbour spacings should follow the Wigner surmise of the GUE ensemble. The suite's design philosophy is visible in the lettered K-sub-checks of the console capture: K1 splits the range into 8 blocks and requires the KS statistic to be homogeneous across them (spread 0.009934 against a limit of 0.0101); K2 re-runs the test on the two halves of the dataset and requires the D values to agree (|ΔD| = 0.005681 against a 0.02 limit); K3 checks the empirical moments of the unfolded spacings (mean exactly 1.0000; variance 0.1591 against the surmise value 0.1781 within a ±60% band). The primary pass-1 verdict was a p-value-driven WARN, but the pre-registered HARDCORE pass-2 audit — the verdict that governs in the composite algebra — passed all three sub-checks. The v3.2 estimator audit later revisited the ζ-side unfolding that produced the small p-values (see the Test 34 story and Appendix C of the monograph).
## 3. What the test verifies (verbatim from the run's report)
> STATISTICAL family: one-sample KS of zero spacings vs GUE Wigner surmise. p-values depend on sample size and T-range — finite-data effects are legal. METHOD: STATISTICAL family: one-sample KS of zero spacings vs GUE Wigner surmise. p-values depend on sample size and T-range — finite-data effects are legal.
## 4. Verdict lines of the reference run (verbatim)
> Test 4: KS D=0.0216, p=0.0 → WARN
> Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A04.docx` | 6.0 KB | Editable edition of the same report (Microsoft Word). |
| `report_A04.html` | 3.6 KB · 41 lines | Web edition of the same report (self-contained HTML). |
| `report_A04.md` | 3.2 KB · 51 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A04.pdf` | 4.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:52:57.718] [+368.746s]  calc: KS D = 0.021619, p_asymptotic = 9.567870e-21 (n=49999, λ=4.8368)
[23:52:57.719] [+368.748s]  calc: KS D = 0.029562, p_asymptotic = 3.479907e-05 (n=6251, λ=2.3408)
[23:52:57.720] [+368.748s]  calc: KS D = 0.025418, p_asymptotic = 6.066737e-04 (n=6250, λ=2.0125)
[23:52:57.721] [+368.749s]  calc: KS D = 0.021305, p_asymptotic = 6.745302e-03 (n=6251, λ=1.6870)
[23:52:57.721] [+368.750s]  calc: KS D = 0.027409, p_asymptotic = 1.619781e-04 (n=6251, λ=2.1704)
[23:52:57.722] [+368.750s]  calc: KS D = 0.022629, p_asymptotic = 3.252259e-03 (n=6251, λ=1.7919)
[23:52:57.723] [+368.751s]  calc: KS D = 0.019816, p_asymptotic = 1.453640e-02 (n=6251, λ=1.5691)
[23:52:57.723] [+368.751s]  calc: KS D = 0.019647, p_asymptotic = 1.581953e-02 (n=6250, λ=1.5556)
[23:52:57.724] [+368.753s]  calc: KS D = 0.019627, p_asymptotic = 1.595774e-02 (n=6251, λ=1.5542)
[23:52:57.728] [+368.756s]  calc: KS D = 0.024587, p_asymptotic = 1.427535e-13 (n=24999, λ=3.8904)
[23:52:57.729] [+368.758s]  calc: KS D = 0.018906, p_asymptotic = 3.369159e-08 (n=25000, λ=2.9916)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 4 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — deep KS audit
────────────────────────────────────────────────────────────
 Full range: N=49999 spacings, D=0.021619, p=0.000000 (report; primary verdict governs)
 K1 blocks    : D over 8 blocks: min=0.019627 max=0.029562, spread=0.009934 (limit 0.0101)
 K2 half split: D_first=0.024587, D_second=0.018906, |ΔD|=0.005681 (limit 0.02)
 K3 moments   : mean(s)=1.0000 (limit |Δ|<0.02), var(s)=0.1591 vs surmise 0.1781 (limit ±60%)
────────────────────────────────────────────────────────────
 K1 block homog       PASS — spread = 0.009934
 K2 half split        PASS — |ΔD| = 0.005681
 K3 moments           PASS — mean 1.0000, var 0.1591
 Test 4 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 4 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 4` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 4 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_03](../test_03_bN_rate/README.md) · [test_05](../test_05_gue_ks_highT/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
