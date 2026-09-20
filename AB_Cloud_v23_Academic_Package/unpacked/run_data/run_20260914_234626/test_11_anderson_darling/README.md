# Test 11: Anderson-Darling test — folder `test_11_anderson_darling/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:56:52
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_11_anderson_darling/](README.md)
## 1. What this folder is
Test 11 deploys the Anderson–Darling test — the tail-sensitive general-purpose goodness-of-fit instrument — against the GUE Wigner surmise, over the full range and additionally in a height-resolved mode. The primary pass recorded A² = 61.4924 with a Monte-Carlo p-value of 0.0000, and the best high-T subrange (T > 31351) also rejected, p = 0.0000, with the full height-resolved table printed in the report.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_11_anderson_darling/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Anderson–Darling statistic weights the tails of the distribution far more heavily than the KS test, making it the sharpest of the three distributional instruments for detecting tail mismatches — precisely where level-repulsion signatures live. Its rejection at pass 1 is part of the honest record: with n = 49,999 the A² statistic can detect discrepancies of order 1/√n ≈ 0.5%, and the suite's own v3.2 estimator audit later traced the adversarial composite statistics of the run (including the distributional p-values of Tests 4–6 and 11) to the ζ-side reference unfolding, whose defects were located and repaired in the v3.2 patch series with a pre-registered post-fix falsifiability window. The governing HARDCORE pass-2 audit passed all five of its sub-checks, and the monograph presents this test together with its height-resolved table as the most transparent documentation of where in the spectrum the distributional pressure is highest.
## 3. What the test verifies (verbatim from the run's report)
> Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5) METHOD: Tail-sensitive GOF vs GUE surmise — full range + height-resolved asymptotic verdict (cf. Test 5)
## 4. Verdict lines of the reference run (verbatim)
> Test 11: A²=61.4924, MC p=0.0000 → WARN (best high-T subrange T>31351 also rejects, p=0.0000; see height-resolved table)
> Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A11.docx` | 179.2 KB | Editable edition of the same report (Microsoft Word). |
| `report_A11.html` | 176.8 KB · 3056 lines | Web edition of the same report (self-contained HTML). |
| `report_A11.md` | 176.5 KB · 3066 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A11.pdf` | 289.6 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:55:18.664] [+509.692s]  calc: A² = 61.492426 (n=49999)
[23:55:18.794] [+509.822s]  calc: A² = 0.384147 (n=49999)
[23:55:18.799] [+509.827s]  calc: A² = 1.108144 (n=49999)
[23:55:18.824] [+509.852s]  calc: A² = 0.302521 (n=49999)
[23:55:18.830] [+509.858s]  calc: A² = 0.593758 (n=49999)
[23:55:18.835] [+509.863s]  calc: A² = 0.413282 (n=49999)
[23:55:18.840] [+509.868s]  calc: A² = 1.868152 (n=49999)
[23:55:18.845] [+509.873s]  calc: A² = 0.975684 (n=49999)
[23:55:18.850] [+509.878s]  calc: A² = 1.017080 (n=49999)
[23:55:18.854] [+509.882s]  calc: A² = 0.809583 (n=49999)
[23:55:18.859] [+509.887s]  calc: A² = 0.503147 (n=49999)
[23:55:18.864] [+509.892s]  calc: A² = 0.822603 (n=49999)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 11 (secondary, HARDCORE): Objection 2 (extended): Advanced RMT Diagnostics — A² reproducibility audit
────────────────────────────────────────────────────────────
 Data: A² = 61.492426 (n=49999, cap=50000)
   MC(seed=0x11a1) progress: 500/1000
   MC(seed=0x11a1) progress: 1000/1000
   MC(seed=0x11a2) progress: 500/1000
   MC(seed=0x11a2) progress: 1000/1000
 A1 MC p seeds: p1=0.0000, p2=0.0000, |Δp|=0.0000 (limit 0.05, n_mc=1000)
 A2 halves    : A²_first=37.6468, A²_second=24.8662, rel.dev=33.9% (limit 50%)
                low-T/high-T trend: A²_first/A²_second = 1.51 (>1 → deviation concentrated at low T)
 A3 structure : A²/W² = 7.52 (W² = 8.1777; structural band 1–8)
 A4 ensemble  : 6 × 3500x3500 GUE, seeds 112–117 (diag est. ≈ 154 s)
   pooled n_ref=16800: mean 1.000171, std 0.4294 (law 0.4220, Δ +1.8%), A²_pooled = 2.4313
   floor scaled to n=49999: A² ≈ 7.2 vs data 61.5
   A5 two-sample MC: 250/1000
   A5 two-sample MC: 500/1000
   A5 two-sample MC: 750/1000
   A5 two-sample MC: 1000/1000
   A5 two-sample: A²(data vs ensemble CDF) = 104.6518, p(MC) = 0.0000 [n_mc=1000] → deviation CONFIRMED vs big-GUE reference
────────────────────────────────────────────────────────────
 A1 MC p stability    PASS — |Δp| = 0.0000
 A2 half split        PASS — rel.dev = 33.9%, low/high A² = 1.51
 A3 structure         PASS — A²/W² = 7.52
 A4 GUE floor         PASS — floor 7.2 vs data 61.5, std Δ +1.8%
 A5 two-sample        PASS — p = 0.0000, A² = 104.7
 Test 11 [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 11 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 11` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 11 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_10](../test_10_cross_validation/README.md) · [test_12](../test_12_two_sample_ks/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
