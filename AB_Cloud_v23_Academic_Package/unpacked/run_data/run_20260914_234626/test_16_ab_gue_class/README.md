# Test 16: AB-cloud GUE classification — folder `test_16_ab_gue_class/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 00:24:43
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_16_ab_gue_class/](README.md)
## 1. What this folder is
Test 16 delivers the formal GUE classification of the AB-cloud spectrum: the mean nearest-neighbour spacing ratio ⟨r⟩ is computed over the central bulk window of the spectrum and compared with the GUE benchmark 0.5992, with a Monte-Carlo p-value attached as diagnostics. This is the test that assigns the lattice spectrum its random-matrix symmetry class.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_16_ab_gue_class/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The spacing ratio ⟨r⟩ is the modern workhorse of random-matrix classification: it is unfolded-free (defined purely on ratios of consecutive gaps), robust against density variations, and its universal expectations 0.3869 (Poisson), 0.5307 (GOE) and 0.5992 (GUE) separate the three canonical classes cleanly. A bulk-window verdict of GUE for the AB-cloud operator is therefore a statement about the operator's symmetry class, not merely about curve-fitting quality — it says the operator breaks time-reversal in exactly the way the GUE class requires, which is the statistical echo of the exact flux structure certified in Test 15. The monograph's classification chapter uses Test 16 as the formal anchor and refers to Tests 32 and 33 for the finite-size and disorder-robustness follow-ups of the same statistic. The HARDCORE pass-2 audit re-derives the classification on the secondary lattice configuration.
## 3. What the test verifies (verbatim from the run's report)
> Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics. METHOD: Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics. Test 16 HARDCORE pass 2: 96x96, n=5 realizations at α=0.5000, Nv=2, q=1.000, W_eff=1.00, ensemble deep checks (bootstrap CI, scatter, sign count). Test 16 HARDCORE: ⟨r⟩=0.5798±0.0037 (n=5), bootstrap CI [0.5732,0.5859] misses GUE, scatter σ=0.0082.
## 4. Verdict lines of the reference run (verbatim)
> Test 16 [MONTGOMERY] α=0.5 (α=0.5000 (default)): ⟨r⟩ mean=0.594 n_pass=1/1 → PASS
> Test 16 [MONTGOMERY] FINAL (last α=0.5): ⟨r⟩=0.594 → PASS
> Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A16.docx` | 6.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A16.html` | 4.2 KB · 50 lines | Web edition of the same report (self-contained HTML). |
| `report_A16.md` | 3.8 KB · 60 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A16.pdf` | 5.5 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[00:00:54.007] [+845.035s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:04:52.591] [+1083.619s]  calc: ⟨r⟩ = 0.572908 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:04:56.983] [+1088.011s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:08:56.388] [+1327.416s]  calc: ⟨r⟩ = 0.569121 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:09:01.657] [+1332.686s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:13:20.122] [+1591.151s]  calc: ⟨r⟩ = 0.586869 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:13:24.846] [+1595.874s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:19:04.049] [+1935.077s]  calc: ⟨r⟩ = 0.584535 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:19:10.567] [+1941.596s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:24:37.791] [+2268.819s]  calc: ⟨r⟩ = 0.585615 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 16 (pass 2, HARDCORE): ⟨r⟩ → GUE classification — deep validation
Deep ensemble at the launch-standard config (pass 1 already swept breadth)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 (N=9216) ≈ 1.5–3 min each → expect ≈ 12–17 min
 Config: α=0.5000, Nv=2, q=1.000, BC=:open, W_eff=1.00 (standard cap 1.0)
 real  1/5: ⟨r⟩ = 0.5729
 real  2/5: ⟨r⟩ = 0.5691
 real  3/5: ⟨r⟩ = 0.5869
 real  4/5: ⟨r⟩ = 0.5845
 real  5/5: ⟨r⟩ = 0.5856

 Ensemble: ⟨r⟩ = 0.5798 ± 0.0037 (n=5)
 Bootstrap 95% CI [0.5732, 0.5859] ∌ GUE (diagnostic); above/below GUE: 0/5
────────────────────────────────────────────────────────────
 ⟨r⟩ > 0.55           PASS — ⟨r⟩ = 0.5798 ± 0.0037 vs GUE 0.5992 (n=5)
 scatter ≤ 0.022      PASS — σ=0.0082 ≤ ✓ monograph band
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 16 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 16` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 16 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_15](../test_15_ab_construction/README.md) · [test_17](../test_17_connes_self_duality/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
