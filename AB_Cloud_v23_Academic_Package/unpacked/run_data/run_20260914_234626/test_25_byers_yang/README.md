# Test 25: Byers-Yang theorem check — folder `test_25_byers_yang/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 02:34:35
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (spectral invariance)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_25_byers_yang/](README.md)
## 1. What this folder is
Test 25 certifies the Byers–Yang theorem on the AB-cloud lattice: the full spectrum must be exactly invariant under an integer shift of the threading flux, q → q + 1, with the spectral distance Δ reported at ~1e-15; and, in the same battery, fractional flux values must produce genuinely different spectra — the negative control that proves the invariance is not a numerical artifact.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_25_byers_yang/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Byers–Yang theorem is the deep periodicity of flux physics: shifting the total flux through a ring by one quantum h/e returns every observable to its starting value, a fact at the root of flux quantization and the Aharonov–Bohm effect's topology. On the lattice the theorem becomes a statement about entire eigenspectra, and the suite verifies it as such — comparing sorted spectra level by level at machine precision, not merely their low-lying edges. The fractional-flux control row is the test's intellectual core: a numerical coincidence could mimic invariance at the checked points, but only genuinely broken invariance at fractional fluxes distinguishes real periodicity from an accidental flat comparison. The monograph lists Byers–Yang invariance among the machine-zero exact certificates of the run, and the HARDCORE audit re-runs the comparison on the secondary lattice.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config). METHOD: EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config). Test 25 HARDCORE: Byers-Yang Δ<1e-10 for 3 layouts × q∈{+1,+2,−1} on 96x96 → true; fractional q∈{0.3,0.5} Δ>1e-3 → true.
## 4. Verdict lines of the reference run (verbatim)
> Test 25: Δ(q=1→0)=0.0 [exp ~0], Δ(q=0.3→0)=0.0032 [exp >1e-3] → PASS
> Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A25.docx` | 6.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A25.html` | 4.4 KB · 51 lines | Web edition of the same report (self-contained HTML). |
| `report_A25.md` | 4.0 KB · 61 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A25.pdf` | 5.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[01:29:46.459] [+6177.487s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 0 vortices, model=:dirac
[01:35:14.706] [+6505.734s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:40:55.414] [+6846.443s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:46:20.418] [+7171.446s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:51:30.629] [+7481.657s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[01:56:54.159] [+7805.187s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[02:02:23.302] [+8134.330s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:07:47.600] [+8458.629s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:13:15.445] [+8786.473s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:18:29.329] [+9100.357s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:23:43.775] [+9414.803s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:29:13.016] [+9744.044s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 25 (pass 2, HARDCORE): Byers–Yang — multi-layout / multi-q audit
3 layouts × {+1, +2, −1} integer rows + fractional {0.3, 0.5} rows
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 12 value-only diagonalizations at 96x96 (N=9216) — expect ≈ 10–15 min
 layout 1, q=+1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, q=+2: Δ = 1.04e-14 < 1e-10 ✓
 layout 1, q=-1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, fractional q=0.3: Δ = 3.35e-03 > 1e-3 ✓ (genuine AB effect)
 layout 1, fractional q=0.5: Δ = 3.74e-03 > 1e-3 ✓ (genuine AB effect)
 layout 2, q=+1: Δ = 1.24e-14 < 1e-10 ✓
 layout 2, q=+2: Δ = 8.66e-15 < 1e-10 ✓
 layout 2, q=-1: Δ = 1.24e-14 < 1e-10 ✓
 layout 3, q=+1: Δ = 1.01e-14 < 1e-10 ✓
 layout 3, q=+2: Δ = 8.89e-15 < 1e-10 ✓
 layout 3, q=-1: Δ = 1.01e-14 < 1e-10 ✓
────────────────────────────────────────────────────────────
 integer q ∀layouts   PASS — Δ(q=+1,+2,−1 vs 0) < 1e-10 on 3 independent layouts
 fractional Δ > 1e-3  PASS — q ∈ {0.3, 0.5} keep the genuine AB effect
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 25 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 25` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 25 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_24](../test_24_dirac_string_flux/README.md) · [test_26](../test_26_pbc_torus/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
