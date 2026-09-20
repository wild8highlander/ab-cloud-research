# Test 17: Connes self-duality α↔1/α — folder `test_17_connes_self_duality/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 00:55:45
**Verdicts (verbatim register):** PASS  
**Family:** EXACT family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_17_connes_self_duality/](README.md)
## 1. What this folder is
Test 17 verifies Connes self-duality: the isospectrality of the AB-cloud operator under the exchange α ↔ 1/α of the flux parameter. The spectrum at α and at 1/α must be identical to machine precision — an exact, tolerance-free requirement — and the HARDCORE pass at L = 24 additionally certifies the zero-mode census at the self-dual point α = 1/2: zero_modes(α=1/2) = 4, with the spectral defect measure reported alongside.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_17_connes_self_duality/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Connes' analytic approach to the Riemann hypothesis predicts a scaling symmetry α ↔ 1/α for the spectral side of any admissible Connes-type operator; in the AB-cloud framework this prediction becomes a concrete, machine-checkable isospectrality statement about the lattice Hamiltonian. Passing it at machine precision means the lattice construction realises the duality not approximately but exactly, level by level, across the entire spectrum. The self-dual point α = 1/2 is where the operator sits exactly on the AIII chiral-symmetry boundary (the regime probed independently by Tests 18 and 27), and the certified count of four zero modes there is the fingerprint of the Dirac tower that Tests 19, 29 and 30 investigate from other angles. The monograph's duality chapter treats this test as the exact-mathematics bridge between the statistical evidence and the analytic theory, and its HARDCORE pass re-certifies everything at L = 24 with the full census printed in the console capture.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: isospectrality under α ↔ 1/α to machine precision. METHOD: EXACT: isospectrality under α ↔ 1/α to machine precision. Test 17 HARDCORE L=24: zero_modes(α=1/2)=4, spectral defects 1.42e-15/1.66e-15, duality defect 3.62e-01. Test 17 HARDCORE L=48: zero_modes(α=1/2)=4, spectral defects 2.90e-15/2.41e-15, duality defect 3.65e-01. Test 17 HARDCORE L=96: zero_modes(α=1/2)=4, spectral defects 3.96e-15/3.24e-15, duality defect 3.66e-01.
## 4. Verdict lines of the reference run (verbatim)
> Test 17: zero_modes(α=1/2)=4 (expected 4) → PASS
> Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A17.docx` | 8.2 KB | Editable edition of the same report (Microsoft Word). |
| `report_A17.html` | 5.5 KB · 54 lines | Web edition of the same report (self-contained HTML). |
| `report_A17.md` | 5.1 KB · 64 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A17.pdf` | 7.0 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[00:32:11.030] [+2722.058s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[00:32:11.825] [+2722.853s]  heevr values-only solve: N=576 (α=0.5000, torus, W=0) — zero_modes + E→-E defect одним прогоном
[00:32:11.978] [+2723.006s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[00:32:12.540] [+2723.568s]  heevr values-only solve: N=576 (α=0.3333, torus, W=0) — spectral_symmetry_defect
[00:32:12.697] [+2723.725s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[00:32:13.231] [+2724.259s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[00:32:13.780] [+2724.808s]  heevr values-only solves ×2: N=576 (α=0.5000 open, W=4) + N=576 (α=2.0000 open, W=4) — connes_self_duality_defect
[00:32:14.746] [+2725.775s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[00:32:15.470] [+2726.498s]  heevr values-only solve: N=2304 (α=0.5000, torus, W=0) — zero_modes + E→-E defect одним прогоном
[00:32:20.921] [+2731.950s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[00:32:21.733] [+2732.761s]  heevr values-only solve: N=2304 (α=0.3333, torus, W=0) — spectral_symmetry_defect
[00:32:27.105] [+2738.133s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 17 (pass 2, HARDCORE): Connes self-duality — cross-size audit
Zero-mode invariant + spectral symmetries on the size ladder 24 → ab_nx
────────────────────────────────────────────────────────────
 L=24: zero_modes(α=1/2)=4 | spec.defect(1/2)=1.42e-15, (1/3)=1.66e-15 | duality=3.62e-01
 L=48: zero_modes(α=1/2)=4 | spec.defect(1/2)=2.90e-15, (1/3)=2.41e-15 | duality=3.65e-01
 L=96: zero_modes(α=1/2)=4 | spec.defect(1/2)=3.96e-15, (1/3)=3.24e-15 | duality=3.66e-01
 At α=1/3 the spectrum stays gapped at E=0 on these tori (base observation).
────────────────────────────────────────────────────────────
 zero_modes(1/2)=4 ∀L PASS — topological invariant holds on the whole ladder
 E→−E defect < 1e-10 ∀L PASS — α=1/2 and α=1/3, generic bipartite symmetry
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 17 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 17` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 17 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_16](../test_16_ab_gue_class/README.md) · [test_18](../test_18_chiral_AIII/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
