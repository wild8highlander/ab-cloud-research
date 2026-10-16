# Test 5: GUE KS test (high-T only) — folder `test_05_gue_ks_highT/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:53:09
**Verdicts (verbatim register):** WARN → PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_05_gue_ks_highT/](README.md)
## 1. What this folder is
Test 5 repeats the one-sample KS confrontation of Test 4 but restricts the analysis to the high-T tail of the spectrum, where GUE asymptotics are expected to hold best. The suite is candid about the data budget: the embedded dataset carries 50,000 zeros with T ≤ 40434, far below the T ≳ 10^6 regime where the asymptotic claims are sharpest, so the test is explicitly marked as data-limited rather than asymptotically conclusive.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_05_gue_ks_highT/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The motivation for a high-T cut is standard in the random-matrix literature: finite-height effects, the slow variation of the density of zeros, and the residual influence of the lower end of the spectrum can all bias a full-range test. By slicing the data at increasing height thresholds the suite probes whether agreement with the GUE surmise improves as the low-T contamination is removed. The primary pass recorded a best high-T p-value of 0.0 (the same finite-sample KS hypersensitivity documented in Test 4), and the governing HARDCORE pass-2 audit passed its two sub-checks. The monograph pairs this test with Test 11's height-resolved Anderson–Darling table: together they constitute the suite's honest statement that within the accessible window the distributional comparison is GUE-consistent, while the asymptotic regime remains the province of the larger external datasets referenced in the monograph's outlook chapter.
## 3. What the test verifies (verbatim from the run's report)
> Same, restricted to high T where GUE asymptotics hold better; still data-limited (embedded 50k zeros, T ≤ 40434 ≪ 10⁶). METHOD: Same, restricted to high T where GUE asymptotics hold better; still data-limited (embedded 50k zeros, T ≤ 40434 ≪ 10⁶).
## 4. Verdict lines of the reference run (verbatim)
> Test 5: Best high-T p-value=0.0 → WARN
> Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A05.docx` | 5.7 KB | Editable edition of the same report (Microsoft Word). |
| `report_A05.html` | 3.3 KB · 42 lines | Web edition of the same report (self-contained HTML). |
| `report_A05.md` | 3.0 KB · 52 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A05.pdf` | 4.5 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:53:09.330] [+380.358s]  calc: KS D = 0.021622, p_asymptotic = 9.563953e-21 (n=49989, λ=4.8368)
[23:53:09.526] [+380.554s]  calc: KS D = 0.021625, p_asymptotic = 9.718636e-21 (n=49958, λ=4.8360)
[23:53:09.533] [+380.561s]  calc: KS D = 0.021588, p_asymptotic = 1.254559e-20 (n=49853, λ=4.8228)
[23:53:09.538] [+380.566s]  calc: KS D = 0.021380, p_asymptotic = 4.135955e-20 (n=49523, λ=4.7605)
[23:53:09.542] [+380.570s]  calc: KS D = 0.021203, p_asymptotic = 2.142535e-19 (n=48525, λ=4.6733)
[23:53:09.547] [+380.575s]  calc: KS D = 0.020927, p_asymptotic = 8.613887e-18 (n=45603, λ=4.4714)
[23:53:09.551] [+380.579s]  calc: KS D = 0.020175, p_asymptotic = 1.325911e-13 (n=37230, λ=3.8952)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 5 (secondary, HARDCORE): Objection 2: GUE Spacing Statistics — dense high-T sweep
────────────────────────────────────────────────────────────
        T_min    N_zeros            D            p
           50      49990     0.021622     0.000000
          125      49959     0.021625     0.000000
          312      49854     0.021588     0.000000
          781      49524     0.021380     0.000000
         1953      48526     0.021203     0.000000
         4883      45604     0.020927     0.000000
        12207      37231     0.020175     0.000000
 T2 trend     : p(first)=9.564e-21 → p(last)=1.326e-13 (must not degrade); best p=1.326e-13 (info; primary governs)
 T3 top mean  : mean(s) at highest band = 1.0000 (limit |Δ|<0.02)
────────────────────────────────────────────────────────────
 T2 trend             PASS — p 9.564e-21 → 1.326e-13
 T3 top mean          PASS — mean = 1.0000
 Test 5 [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 5 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 5` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 5 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_04](../test_04_gue_ks_full/README.md) · [test_06](../test_06_chi2_hist/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
