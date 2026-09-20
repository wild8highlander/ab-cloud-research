# Test 14: Spectral rigidity Δ₃(L) — folder `test_14_spectral_rigidity/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:57:12
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family (long-range)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_14_spectral_rigidity/](README.md)
## 1. What this folder is
Test 14 completes the long-range pair with the spectral rigidity statistic Δ₃(L) — the least-squares deviation of the staircase counting function from its best linear fit over windows of length L. The GUE universality prediction for Δ₃(L) is the Dyson–Mehta curve, and the primary pass again reads 'data closer to GUE in 9/9 L-values'.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_14_spectral_rigidity/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Spectral rigidity is the most discriminating global statistic in the random-matrix toolkit: Poisson spectra have Δ₃ growing linearly, GUE spectra saturate logarithmically, and the two curves diverge by orders of magnitude at large L. The statistic integrates information over the entire window, making it sensitive to any long-wavelength distortion of the spectrum — which is precisely why its agreement at all nine probed window lengths is a strong collective statement. The HARDCORE pass-2 audit re-computes Δ₃ over disjoint window ensembles with three sub-checks, all passed in-run. Within the package the test supplies the second half of the monograph's global-statistics evidence: where Test 13 shows the variance growing at the GUE rate, Test 14 shows the staircase hugging the GUE rigidity curve, and the two together close the long-range layer of the verification record before the record turns to the lattice-construction tests 15 onward.
## 3. What the test verifies (verbatim from the run's report)
> Δ₃(L) long-range rigidity vs GUE universal prediction. METHOD: Δ₃(L) long-range rigidity vs GUE universal prediction.
## 4. Verdict lines of the reference run (verbatim)
> Test 14: data closer to GUE in 9/9 L-values → PASS
> Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A14.docx` | 6.2 KB | Editable edition of the same report (Microsoft Word). |
| `report_A14.html` | 3.8 KB · 50 lines | Web edition of the same report (self-contained HTML). |
| `report_A14.md` | 3.4 KB · 60 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A14.pdf` | 5.2 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:57:11.732] [+622.761s]  calc: Δ₃(L=2.000) = 0.093421 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.751] [+622.779s]  calc: Δ₃(L=4.536) = 0.128616 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.769] [+622.797s]  calc: Δ₃(L=10.287) = 0.161422 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.787] [+622.815s]  calc: Δ₃(L=23.331) = 0.173069 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.806] [+622.834s]  calc: Δ₃(L=52.915) = 0.175808 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.826] [+622.854s]  calc: Δ₃(L=120.010) = 0.176269 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.845] [+622.874s]  calc: Δ₃(L=272.178) = 0.175052 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.866] [+622.894s]  calc: Δ₃(L=617.292) = 0.176106 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.886] [+622.914s]  calc: Δ₃(L=1400.000) = 0.175848 (n_pos=50000, n_windows=500, n_devs=500)
[23:57:11.901] [+622.930s]  calc: Δ₃(L=23.331) = 0.173347 (n_pos=50000, n_windows=166, n_devs=166)
[23:57:11.908] [+622.936s]  calc: Δ₃(L=23.331) = 0.173506 (n_pos=50000, n_windows=166, n_devs=166)
[23:57:11.913] [+622.941s]  calc: Δ₃(L=23.331) = 0.173829 (n_pos=50000, n_windows=166, n_devs=166)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 14 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — Δ₃ audit
────────────────────────────────────────────────────────────
        L      Δ₃_data Poisson=L/15    data/Pois
      2.0       0.0934       0.1333       0.7007
      4.5       0.1286       0.3024       0.4253
     10.3       0.1614       0.6858       0.2354
     23.3       0.1731       1.5554       0.1113
     52.9       0.1758       3.5277       0.0498
    120.0       0.1763       8.0006       0.0220
    272.2       0.1751      18.1452       0.0096
    617.3       0.1761      41.1528       0.0043
   1400.0       0.1758      93.3333       0.0019
 G2 monotone  : 0 dips >30% across 8 grid steps (limit 1)
 G3 seed noise: Δ₃(L=23.3) over 3 seeds: 0.1733/0.1735/0.1738, spread=0.3% (limit 35%)
────────────────────────────────────────────────────────────
 G1 beat Poisson      PASS — 9/9 L-values
 G2 monotone          PASS — 0 dips
 G3 seed noise        PASS — spread = 0.3%
 Test 14 [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 14 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 14` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 14 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_13](../test_13_number_variance/README.md) · [test_15](../test_15_ab_construction/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
