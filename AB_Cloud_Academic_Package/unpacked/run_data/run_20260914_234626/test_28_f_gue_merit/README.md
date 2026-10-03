# Test 28: f_GUE figure of merit — folder `test_28_f_gue_merit/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 03:33:19
**Verdicts (verbatim register):** WARN  
**Family:** STATISTICAL family (aggregate merit)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_28_f_gue_merit/](README.md)
## 1. What this folder is
Test 28 computes f_GUE — the fraction of the suite's spectral diagnostics that individually land on the GUE side of their pre-registered windows. It is the record's summary instrument: where Tests 4–14 and 16 judge one statistic at a time, Test 28 aggregates them into a single merit number for the reference configuration (HARDCORE pass 2 on the 96×96 lattice, Nv = 4).
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_28_f_gue_merit/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
An aggregate merit function is how a verification record protects itself from cherry-picking: instead of letting each diagnostic be judged in isolation, f_GUE asks what fraction of the whole battery points the same way. The audit-tier census credits the companion battery 28b with one failed sub-check out of two (WARN) — one of the four honest blemishes of the run that the monograph analyses in Part II and Appendix C rather than suppressing. The aggregate design also makes the test the natural cross-reference hub of the statistical block: every diagnostic that feeds f_GUE has its own folder in this archive, and the reader can trace the merit number back to its ingredients level by level. The monograph quotes f_GUE in the synthesis chapter when it summarises the spectral-layer verdict of the record as a whole.
## 3. What the test verifies (verbatim from the run's report)
> Statistical: fraction of spectral diagnostics consistent with GUE. METHOD: Statistical: fraction of spectral diagnostics consistent with GUE. Test 28 HARDCORE pass 2: 96x96, Nv=4, q=±1.0, W=1.0, n=5 realizations, per-realization f_GUE ensemble. Test 28 HARDCORE: ⟨f_GUE⟩=0.8658±0.0217 (n=5), CI [0.8284,0.9056], scatter σ=0.0485.
## 4. Verdict lines of the reference run (verbatim)
> Test 28: f_GUE=0.881, Σ²_data=0.6115 → WARN
> Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
## 5. Result line
```text
Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A28.docx` | 6.6 KB | Editable edition of the same report (Microsoft Word). |
| `report_A28.html` | 4.0 KB · 49 lines | Web edition of the same report (self-contained HTML). |
| `report_A28.md` | 3.6 KB · 59 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A28.pdf` | 5.4 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[03:10:53.854] [+12244.883s]  calc: Σ²(L=2.000) = 0.423997 (n_pos=8401, n_windows=3000, mean_count=2.01)
[03:10:54.866] [+12245.895s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:15:31.980] [+12523.008s]  calc: Σ²(L=2.000) = 0.663437 (n_pos=5530, n_windows=3000, mean_count=2.03)
[03:15:34.652] [+12525.680s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:20:07.777] [+12798.806s]  calc: Σ²(L=2.000) = 0.629287 (n_pos=5530, n_windows=3000, mean_count=2.02)
[03:20:10.729] [+12801.757s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:24:25.471] [+13056.499s]  calc: Σ²(L=2.000) = 0.620146 (n_pos=5530, n_windows=3000, mean_count=2.04)
[03:24:28.524] [+13059.553s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:28:44.729] [+13315.757s]  calc: Σ²(L=2.000) = 0.737871 (n_pos=5527, n_windows=3000, mean_count=2.04)
[03:28:47.518] [+13318.547s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:33:16.985] [+13588.014s]  calc: Σ²(L=2.000) = 0.526840 (n_pos=5530, n_windows=3000, mean_count=2.02)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 28 (pass 2, HARDCORE): f_GUE figure of merit — ensemble deep pass
n ≥ 5 realizations, per-realization f_GUE, ensemble verdict
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 → expect ≈ 12–17 min
 Config: 96x96, Nv=4, q=±1.00, α=0.5000, W=1.0 (hardcore standard: W=1, q=1, Nv=4)
 real  1/5: f_GUE = 0.8481
 real  2/5: f_GUE = 0.8697
 real  3/5: f_GUE = 0.8755
 real  4/5: f_GUE = 0.8008
 real  5/5: f_GUE = 0.9347

 Ensemble: ⟨f_GUE⟩ = 0.8658 ± 0.0217 | bootstrap CI [0.8284, 0.9056] ∋ 0.90 (diagnostic)
────────────────────────────────────────────────────────────
 ⟨f_GUE⟩ > 0.90       WARN — ⟨f_GUE⟩ = 0.8658 ± 0.0217 (n=5 of 5 finite)
 scatter < 0.10       PASS — σ=0.0485 stable across vortex layouts
 Test 28b [HARDCORE pass 2]: 2 sub-checks, 1 failed → WARN
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 28 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 28` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 28 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_27](../test_27_binary_chiral/README.md) · [test_29](../test_29_dirac_dip/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
