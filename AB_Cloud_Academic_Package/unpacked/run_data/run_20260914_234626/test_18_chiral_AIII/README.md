# Test 18: Chiral symmetry AIII at α=1/2 — folder `test_18_chiral_AIII/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:01:13
**Verdicts (verbatim register):** PASS  
**Family:** EXACT family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_18_chiral_AIII/](README.md)
## 1. What this folder is
Test 18 certifies chiral symmetry of class AIII at the self-dual flux α = 1/2 on the pure lattice (W = 0): the anti-commutator residual ||SHS + H||/||H|| must vanish, and the run reports ≈ 1e-16 — machine precision. The row at W > 0 is retained deliberately as 'the honest breaker': disorder is shown breaking the symmetry, demonstrating that the check can fail when it should.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_18_chiral_AIII/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Chiral (sublattice) symmetry of class AIII is the structural property that organises the zero modes and the spectral symmetry of the operator; at α = 1/2 the AB-cloud lattice sits exactly on this symmetry boundary. The certificate is computed as a norm ratio, so the verdict '1e-16' means the anti-commutator is zero to the last bit of floating-point arithmetic — an exact structural statement, not a statistical trend. Equally important is the negative control: with disorder switched on the same norm ratio visibly departs from zero, proving the instrument is live and the pure-lattice result is not a tautology of the measurement. The monograph's symmetry chapter pairs this test with Test 27 (the binary chiral check with its ζ-dictionary rework) as the two complementary certifications of the AIII structure, and the HARDCORE audit re-runs both the pure and the disordered rows.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker. METHOD: EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker. Test 18 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058, in window), vortex 0.00e+00 (preserved), S²=I 0.00e+00 (96x96 torus).
## 4. Verdict lines of the reference run (verbatim)
> Test 18: chiral defect (α=1/2)=0.0 [exp 0.000000], (α=1/3)=0.0058 [exp ≠0] → PASS
> Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A18.docx` | 5.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A18.html` | 3.3 KB · 38 lines | Web edition of the same report (self-contained HTML). |
| `report_A18.md` | 2.9 KB · 48 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A18.pdf` | 4.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[01:00:19.945] [+4410.973s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[01:00:35.975] [+4427.003s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[01:00:56.095] [+4447.123s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 18 (pass 2, HARDCORE): chiral symmetry AIII — deep audit
Exact row + ε_rms quantitative contract + vortex-preservation row +
S² = I operator sanity (launch-standard lattice)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 3 builds + 3 S·H·S defect evals at 96x96 (Diagonal S, O(N²)) — ≈ 1–2 min
 H1 exact row (α=1/2, W=0):      defect = 0.00e+00 < ✓ 1e-10
 H2 ε row (W=1.0, Nv=0):       defect = 5.77e-03 vs ε_rms = 0.0058 (analytic) ∈ [0.5, 2.0]× ✓
 H2v vortex row (Nv=2, W=0):     defect = 0.00e+00 < 1e-10 ✓ (bond phases PRESERVE AIII)
 H3 operator sanity: ‖S² − I‖/‖I‖ = 0.00e+00 < ✓ 1e-12
────────────────────────────────────────────────────────────
 exact row < 1e-10    PASS — ‖SHS+H‖/‖H‖ = 0.00e+00 at α=1/2, W=0
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 vs analytic 2‖ε‖_F/‖H‖_F = 0.0058 (size-independent)
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 S² = I               PASS — ‖S²−I‖/‖I‖ = 0.00e+00
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 18 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 18` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 18 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_17](../test_17_connes_self_duality/README.md) · [test_19](../test_19_dirac_cone/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
