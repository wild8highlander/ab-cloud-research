# Test 1: b(N) convergence table — folder `test_01_bN_convergence/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:46:52
**Verdicts (verbatim register):** PASS  
**Family:** EXACT-formula family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_01_bN_convergence/](README.md)
## 1. What this folder is
Test 1 opens the entire verification record with the suite's foundational convergence table. It tracks the quantity b(N) = (1/N) Σ|γ_k − γ̃_k| — the mean absolute deviation between the true Riemann ζ zeros γ_k and their Gram-point-based approximations γ̃_k — as the approximation set grows from small samples up to the full embedded 50,000-zero dataset. The headline number of the whole run, b(50000) = 1.2126, is produced here and reused by Tests 2, 3, 7, 8, 9 and 10.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_01_bN_convergence/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Gram-point ladder is the constructive heart of the AB-Cloud framework: it is the mechanism by which the ζ zeros are mirrored into the spectrum of the Aharonov–Bohm flux lattice operator. Before any statistics can be trusted, the record must show that this ladder behaves predictably as N grows. Test 1 therefore belongs to the EXACT-formula family: the tolerance scale is not a statistical band but the floating-point round-off floor itself, because each entry of the table is computed from closed-form expressions rather than from sampled data. In the run's two-pass protocol the primary verdict is followed by a HARDCORE pass-2 deep audit carrying eight individually lettered sub-checks (H0–H7), all of which passed in-run. The monograph dedicates Part II Chapter 1 to this test, and the b(N) = 1.2126 value at N = 50000 is quoted throughout Appendix A of the monograph as the reference constant of the reference run.
## 3. What the test verifies (verbatim from the run's report)
> b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off. METHOD: b(N) = (1/N)Σ|γ_k−γ̃_k| measures convergence of Gram-point approximations to true zeta zeros. EXACT-formula family: tolerance scale = floating-point round-off.
## 4. Verdict lines of the reference run (verbatim)
> Test 1: b(N=50000) = 1.2126 → PASS
> Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 1 [HARDCORE pass 2]: 8 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A01.docx` | 8.0 KB | Editable edition of the same report (Microsoft Word). |
| `report_A01.html` | 5.5 KB · 86 lines | Web edition of the same report (self-contained HTML). |
| `report_A01.md` | 5.1 KB · 96 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A01.pdf` | 8.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 1 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep validation
Same statistic b(N) = (1/N) Σ|γ_k − γ̃_k|, verified by 8 harder sub-checks
────────────────────────────────────────────────────────────
 H0 reproduce : max|b_direct − b_prefix| over 4 probes = 0.00e+00 (limit 1e-9)
 H1 dense scan: 40 checkpoints, N = 25 → 50000 (ratio 1.22)
            N             b(N)        Δ vs prev
           25     4.6101190361              ---
           30     4.3989811028    -0.2111379332
           37     4.1932852303    -0.2056958726
           45     3.9943669591    -0.1989182711
           55     3.8252166187    -0.1691503404
           67     3.6455743228    -0.1796422960
           82     3.4801726407    -0.1654016820
          100     3.3321638710    -0.1480087697
          122     3.1910285619    -0.1411353091
          149     3.0547427984    -0.1362857635
          182     2.9267044466    -0.1280383518
          222     2.8066104527    -0.1200939939
          271     2.6947048268    -0.1119056258
          331     2.5892260492    -0.1054787776
          404     2.4907320942    -0.0984939550
          493     2.3966440338    -0.0940880604
          601     2.3100937127    -0.0865503211
          733     2.2274677461    -0.0826259666
          894     2.1498825733    -0.0775851728
         1091     2.0754888256    -0.0743937476
         1331     2.0067062433    -0.0687825824
         1624     1.9405012929    -0.0662049503
         1981     1.8782421944    -0.0622590986
         2417     1.8197691194    -0.0584730750
         2949     1.7640375461    -0.0557315733
         3598     1.7111812347    -0.0528563114
         4390     1.6613158059    -0.0498654288
         5356     1.6137261550    -0.0475896509
         6534     1.5686043745    -0.0451217805
         7971     1.5258165855    -0.0427877890
         9725     1.4850058741    -0.0408107114
        11864     1.4460749475    -0.0389309266
        14474     1.4090310622    -0.0370438853
        17658     1.3736819777    -0.0353490845
        21543     1.3399113218    -0.0337706559
        26282     1.3076687539    -0.0322425680
        32064     1.2768213946    -0.0308473593
        39118     1.2473022976    -0.0295190970
        47724     1.2190083740    -0.0282939236
        50000     1.2125526773    -0.0064556968
 H2 monotone  : 0/39 consecutive pairs exceed the noise band (limit 2)
 H3 predict   : walk-forward one-step-ahead, best of 3 laws (power / 1·log⁻¹N / local secant)
                median err 0.05%, max err 0.09% (limits 2%/5%)
 H4 stationarity: head b(25000)=1.315628 | tail b(25000)=1.109478 | tail/head = 0.8433 (limit 1.25)
 H5 bootstrap : b(50000)=1.212553 | 95%CI [1.209765, 1.215265] (width 0.45% of b, limit 15%)
                threshold 2.00 − (b + 2σ/√N = 1.215350) = +0.784650 → verdict ROBUST
 H6 outliers  : peak |Δγ| = 9.0356 at k=1 (0.0% of Σd, limit 10%)
                top-5 share 0.1% | 1%-trimmed b deviates +1.13% from b (limit 15%)
 H7 Gram sanity: γ̃ strictly increasing over n=1..50000 → 0 violations (limit 0)
────────────────────────────────────────────────────────────
 H0 reproduce         PASS — worst |Δ| = 0.00e+00
 H1 dense scan        PASS — 40 checkpoints
 H2 monotone          PASS — 0 violations / 39 pairs
… (truncated at 60 of 66 lines; the complete capture is in [`logs/`](logs/README.md) and all four report files)
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 1 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 1` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 1 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
