# Test 2: Monotonicity verification — folder `test_02_bN_monotonicity/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:47:15
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (algebraic consistency)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_02_bN_monotonicity/](README.md)
## 1. What this folder is
Test 2 checks a binary algebraic property of the Gram ladder: monotonicity. Along the refinement sequence the value of b(N) must never increase — each refinement step is required to leave the approximation no worse than before. The primary pass reports the definitive line 'Monotonicity violations: 0 / 499': across 499 successive refinement pairs not a single violation was registered.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_02_bN_monotonicity/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Monotonicity is the cheapest falsifiable alarm the framework has. If the Gram-point refinement ever made the approximation worse, the whole constructive story built on the ladder would be suspect, and every downstream statistic (Tests 4–14) would be measuring a moving target. Because the check is purely algebraic, its verdict is binary and carries no statistical caveats: 499 monitored transitions, zero regressions. In the HARDCORE pass-2 audit the test adds four further sub-checks that re-derive the monotonicity property on the secondary 96×96 lattice configuration and re-confirm the anchor value b(50000) = 1.2126. The monograph treats this test together with Test 1 as the 'algebraic pair' that closes the constructive layer of the verification record before the statistical layer begins.
## 3. What the test verifies (verbatim from the run's report)
> Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict). METHOD: Checks b(N) does not increase along the refinement sequence — an algebraic consistency property (binary verdict).
## 4. Verdict lines of the reference run (verbatim)
> Test 2: Monotonicity violations: 0 / 499 → PASS
> Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
## 5. Result line
```text
Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A02.docx` | 5.1 KB | Editable edition of the same report (Microsoft Word). |
| `report_A02.html` | 2.7 KB · 43 lines | Web edition of the same report (self-contained HTML). |
| `report_A02.md` | 2.4 KB · 53 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A02.pdf` | 4.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 2 (secondary, HARDCORE): Objection 1: b(N) Convergence — deep monotonicity audit
────────────────────────────────────────────────────────────
 S1 strict band: 0/39 pairs violate (limit 0)
    segment      mean |Δγ|
    1-5001        1.629872
 5001-10001       1.328818
 10001-15001       1.248992
 15001-20001       1.201689
 20001-25000       1.168653
 25000-30000       1.143731
 30000-35000       1.123510
 35000-40000       1.106908
 40000-45000       1.092713
 45000-50000       1.080314
 S2 segments  : 0 local increases (limit 0)
 S3 new lows  : 40/40 checkpoints = 100% (limit ≥ 60%)
 S4 drawdown  : b(50000)=1.2126 vs b(25)=4.6101 → 73.7% decrease (limit ≥ 5%)
────────────────────────────────────────────────────────────
 S1 strict band       PASS — 0 violations / 39 pairs
 S2 segments          PASS — 0 increases / 10 segments
 S3 new lows          PASS — 100% of checkpoints
 S4 drawdown          PASS — 73.7% decrease
 Test 2 [HARDCORE pass 2]: 4 sub-checks, 0 failed, b(50000)=1.2126 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 2 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 2` (module [`abcloud/tests_01_14.py`](../../../python_clone/abcloud/tests_01_14.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 2 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_01](../test_01_bN_convergence/README.md) · [test_03](../test_03_bN_rate/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
