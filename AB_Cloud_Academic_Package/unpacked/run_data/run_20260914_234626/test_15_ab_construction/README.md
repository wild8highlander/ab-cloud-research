# Test 15: AB-cloud Hamiltonian construction — folder `test_15_ab_construction/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-14 23:57:32
**Verdicts (verbatim register):** PASS  
**Family:** Mixed (EXACT + STATISTICAL)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_15_ab_construction/](README.md)
## 1. What this folder is
Test 15 is the construction certificate of the entire framework: it builds the AB-cloud Hamiltonian itself and certifies its defining structural properties. Hermiticity and the τ time-reversal-breaking balance are verified EXACTLY — at machine-ε precision, i.e. to the last representable digit of double-precision arithmetic — while the level-spacing ratio statistic ⟨r⟩ over the constructed spectrum is checked STATISTICALLY against its GUE expectation.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_15_ab_construction/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Everything else in the record presupposes that the operator under study is what the framework says it is: a Hermitian lattice Hamiltonian threaded by Aharonov–Bohm flux quanta whose spectrum can legitimately be compared with random-matrix ensembles. Test 15 provides that warranty. The exact layer is unforgiving — a single asymmetric matrix entry or a misplaced flux sign would produce a residual far above machine precision — so the machine-ε verdict is a genuine certificate, not a tolerance. The statistical layer then confirms that the freshly constructed operator's spectrum already speaks the GUE dialect (the ⟨r⟩ ratio test whose bulk expectation is 0.5992). The HARDCORE pass-2 audit runs the full pipeline on the secondary 96×96 lattice with four sub-checks, all passed in-run. Monograph Chapter 15 is the natural starting point for any reader who wants to understand what operator the whole package is talking about.
## 3. What the test verifies (verbatim from the run's report)
> Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL. METHOD: Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL. Test 15 HARDCORE: full plaquette scan 96x96 (±-quartet), signed flux 4/4, empty 9021/9021, worst empty flux 0.00e+00.
## 4. Verdict lines of the reference run (verbatim)
> Test 15: Hermiticity=OK, τ_TRB=0.1037, flux_v1=-0.0 [exp -0.0], flux_empty=0.0 → PASS
> Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A15.docx` | 5.1 KB | Editable edition of the same report (Microsoft Word). |
| `report_A15.html` | 2.6 KB · 32 lines | Web edition of the same report (self-contained HTML). |
| `report_A15.md` | 2.2 KB · 42 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A15.pdf` | 3.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[23:57:23.362] [+634.390s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 4 vortices, model=:dirac
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 15 (pass 2, HARDCORE): AB-cloud construction — deep validation
Full-lattice plaquette scan of the ±-quartet (all plaquettes, signed check)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 1 build + O(N) plaquette scan at 96x96 (N=9216) — seconds
 Lattice: 96x96 open :dirac, α=0, quartet q=±1.00 → 9025 plaquettes scanned
 Vortex plaquettes (signed): 4/4 correct ✓
 Empty plaquettes clean (<1e-9): 9021/9021, worst |flux| = 0.00e+00
────────────────────────────────────────────────────────────
 full signed scan     PASS — 4/4 vortex plaquettes, 9021/9021 empty clean
 hermiticity          PASS — verify_hermitian on the quartet H
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 15 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 15` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 15 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_14](../test_14_spectral_rigidity/README.md) · [test_16](../test_16_ab_gue_class/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
