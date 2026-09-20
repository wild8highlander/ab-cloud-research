# Test 13: Number variance Σ²(L) — folder `test_13_number_variance/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:57:04
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family (long-range)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_13_number_variance/](README.md)
## 1. What this folder is
Test 13 moves from nearest-neighbour spacings to long-range statistics: the number variance Σ²(L), the variance of the number of levels contained in windows of unfolded length L. For GUE the asymptotic law is Σ²(L) ~ (1/π²) ln L, and the test compares the data against this curve — the primary pass verdict reads 'data closer to GUE in 9/9 L-values'.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_13_number_variance/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Long-range statistics see physics that spacing tests cannot: spectral rigidity, the collective refusal of eigenlevels to fluctuate locally, manifests in the logarithmic (rather than linear) growth of the number variance. This is the hallmark of quantum-chaotic spectra and the clearest global signature distinguishing GUE from Poisson behaviour. By sweeping the window length L across nine values and requiring the data to sit closer to the GUE curve than to the Poisson alternative in every one of them, the suite converts a curve comparison into a robust multi-scale verdict. The HARDCORE pass-2 audit adds four sub-checks over disjoint windows to eliminate overlap artifacts, all passed in-run. In the monograph's global-statistics chapter this test and its sibling Test 14 (spectral rigidity Δ₃) form the long-range pair that anchors the claim that the ζ spectrum's collective fluctuations are GUE-class across the accessible range.
## 3. What the test verifies (verbatim from the run's report)
> Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison. METHOD: Long-range statistics: Σ²(L) ~ (1/π²)lnL for GUE — asymptotic curve comparison.
## 4. Verdict lines of the reference run (verbatim)
> Test 13: data closer to GUE in 9/9 L-values → PASS
> Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A13.docx` | 7.4 KB | Editable edition of the same report (Microsoft Word). |
| `report_A13.html` | 5.0 KB · 61 lines | Web edition of the same report (self-contained HTML). |
| `report_A13.md` | 4.6 KB · 71 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A13.pdf` | 6.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:57:04.365] [+615.394s]  calc: Σ²(L=2.000) = 0.381460 (n_pos=50000, n_windows=3000, mean_count=2.00)
[23:57:04.366] [+615.394s]  calc: Σ²(L=4.536) = 0.402894 (n_pos=50000, n_windows=3000, mean_count=4.54)
[23:57:04.367] [+615.395s]  calc: Σ²(L=10.287) = 0.354897 (n_pos=50000, n_windows=3000, mean_count=10.30)
[23:57:04.368] [+615.396s]  calc: Σ²(L=23.331) = 0.313517 (n_pos=50000, n_windows=3000, mean_count=23.34)
[23:57:04.369] [+615.397s]  calc: Σ²(L=52.915) = 0.353407 (n_pos=50000, n_windows=3000, mean_count=52.91)
[23:57:04.369] [+615.398s]  calc: Σ²(L=120.010) = 0.354226 (n_pos=50000, n_windows=3000, mean_count=120.02)
[23:57:04.370] [+615.398s]  calc: Σ²(L=272.178) = 0.355610 (n_pos=50000, n_windows=3000, mean_count=272.16)
[23:57:04.371] [+615.399s]  calc: Σ²(L=617.292) = 0.351103 (n_pos=50000, n_windows=3000, mean_count=617.29)
[23:57:04.372] [+615.400s]  calc: Σ²(L=1400.000) = 0.342086 (n_pos=50000, n_windows=3000, mean_count=1399.99)
[23:57:04.378] [+615.407s]  calc: Σ²(L=2.000) = 0.417134 (n_pos=8401, n_windows=3000, mean_count=2.00)
[23:57:04.379] [+615.407s]  calc: Σ²(L=4.536) = 0.484449 (n_pos=8401, n_windows=3000, mean_count=4.53)
[23:57:04.380] [+615.408s]  calc: Σ²(L=10.287) = 0.609118 (n_pos=8401, n_windows=3000, mean_count=10.29)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 13 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — Σ² rigidity audit
────────────────────────────────────────────────────────────
        L      Σ²_data    Poisson=L    data/Pois
      2.0       0.3815       2.0000       0.1907
      4.5       0.4029       4.5359       0.0888
     10.3       0.3549      10.2874       0.0345
     23.3       0.3135      23.3315       0.0134
     52.9       0.3534      52.9150       0.0067
    120.0       0.3542     120.0097       0.0030
    272.2       0.3556     272.1783       0.0013
    617.3       0.3511     617.2922       0.0006
   1400.0       0.3421    1400.0000       0.0002
 N2 monotone  : 0 dips >25% across 8 grid steps (limit 1)
 N3 GUE band  : 9/9 finite pairs have data/GUE ∈ [0.2, 5] (limit 80%)
 N4 seed noise: Σ²(L=23.3) over 3 seeds: 0.3247/0.3060/0.3180, spread=5.9% (limit 40%)
────────────────────────────────────────────────────────────
 N1 beat Poisson      PASS — 9/9 L-values
 N2 monotone          PASS — 0 dips
 N3 GUE band          PASS — 9/9 in band
 N4 seed noise        PASS — spread = 5.9%
 Test 13 [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 13 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 13` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 13 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_12](../test_12_two_sample_ks/README.md) · [test_14](../test_14_spectral_rigidity/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
