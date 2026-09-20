# Test 26: PBC torus Dirac string — folder `test_26_pbc_torus/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 03:07:01
**Verdicts (verbatim register):** PASS  
**Family:** Mixed (EXACT + STATISTICAL)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_26_pbc_torus/](README.md)
## 1. What this folder is
Test 26 assembles the Dirac string bookkeeping on the periodic torus: the flux identities are verified exactly, and the ⟨r⟩ spacing-ratio statistic is computed over the bulk window for the configuration of 4 neutral vortices — vortices whose individual flux quanta cancel in neutral combinations — to certify that the global topological neutralisation behaves as the construction requires.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_26_pbc_torus/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
On a torus, global constraints meet local flux rules: the total flux through the torus must vanish modulo the relevant quantum, and the configuration that satisfies this constraint most naturally is a set of neutral vortex combinations. The test certifies both layers — the exact flux identities that the neutral configuration must respect, and the statistical health (⟨r⟩ over the bulk) of the spectrum the neutralised lattice produces. The design echoes Test 16's classification logic but on a topologically non-trivial global background, checking that bulk universality survives the torus wrapping and the neutral-vortex seam structure. The monograph's torus chapter uses this test to close the flux-topology block (Tests 24–26) before the record moves to the binary-chiral rework of Test 27 and the aggregate statistics of Test 28. The HARDCORE audit re-certifies the configuration on the secondary lattice.
## 3. What the test verifies (verbatim from the run's report)
> Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical). METHOD: Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical). Test 26 HARDCORE pass 2: 96x96 torus, exhaustive artifact classification, n=5 ⟨r⟩ realizations at W_eff=1.00. Test 26 HARDCORE: artifacts 9024 clean/0 wrap/0 unexplained; ⟨r⟩=0.5964±0.0021, scatter σ=0.0046.
## 4. Verdict lines of the reference run (verbatim)
> Test 26: flux_v=-0.0 [exp -0.0], empty_ok=5040/5183, herm=OK, ⟨r⟩=0.6009 → PASS
> Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A26.docx` | 7.0 KB | Editable edition of the same report (Microsoft Word). |
| `report_A26.html` | 4.4 KB · 51 lines | Web edition of the same report (self-contained HTML). |
| `report_A26.md` | 4.0 KB · 61 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A26.pdf` | 5.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[02:35:52.402] [+10143.430s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, torus, 1 vortices, model=:dirac
[02:36:04.354] [+10155.382s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[02:41:24.785] [+10475.813s]  calc: ⟨r⟩ = 0.600632 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[02:41:31.414] [+10482.443s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[02:47:55.044] [+10866.072s]  calc: ⟨r⟩ = 0.596193 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[02:47:58.346] [+10869.375s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[02:54:12.143] [+11243.171s]  calc: ⟨r⟩ = 0.600551 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[02:54:15.944] [+11246.972s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[03:00:22.789] [+11613.818s]  calc: ⟨r⟩ = 0.589380 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[03:00:28.175] [+11619.203s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[03:06:55.993] [+12007.021s]  calc: ⟨r⟩ = 0.595447 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 26 (pass 2, HARDCORE): PBC torus Dirac string — deep validation
Exhaustive artifact classification + ⟨r⟩ ensemble (n ≥ 5)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: flux scan (1 build) + n=5 ⟨r⟩ realizations at 96x96 → expect ≈ 12–17 min
 ⟨r⟩ row: α=0.5000, Nv=4 (base protocol), q=1.0000, W=1.00 = ab_w_eff (capped)
 H1 flux: vortex plaquette OK; empty plaquettes: 9024 clean, 0 wrap artifacts (0.0000), 191 seam (gauge holonomy, ix=96/iy=96), 0 unexplained
 real  1/5: ⟨r⟩ = 0.6006
 real  2/5: ⟨r⟩ = 0.5962
 real  3/5: ⟨r⟩ = 0.6006
 real  4/5: ⟨r⟩ = 0.5894
 real  5/5: ⟨r⟩ = 0.5954

 Ensemble: ⟨r⟩ = 0.5964 ± 0.0021 | bootstrap CI [0.5928, 0.5997] ∋ GUE | above/below: 2/3
────────────────────────────────────────────────────────────
 flux + artifacts     PASS — vortex OK; 9024 clean + 0 wrap(−2πq) + 191 seam holonomy; 0 unexplained
 ⟨r⟩ > 0.5 (ensemble) PASS — ⟨r⟩ = 0.5964 ± 0.0021 (n=5, base contract)
 scatter ≤ 0.022      PASS — σ=0.0046 ≤ ✓ monograph band
 hermiticity ∀real    PASS — verify_hermitian per realization
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 26 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 26` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 26 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_25](../test_25_byers_yang/README.md) · [test_27](../test_27_binary_chiral/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
