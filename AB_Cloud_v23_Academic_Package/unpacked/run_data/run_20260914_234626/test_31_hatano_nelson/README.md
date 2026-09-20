# Test 31: Hatano-Nelson non-Hermitian skin — folder `test_31_hatano_nelson/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 05:29:51
**Verdicts (verbatim register):** PASS  
**Family:** Deterministic non-Hermitian family, SERIES  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_31_hatano_nelson/](README.md)
## 1. What this folder is
Test 31 pushes the suite into non-Hermitian territory with the Hatano–Nelson configuration: the lattice is loaded with asymmetric hopping, and the test certifies the deterministic spectral response — the count and pattern of complex (non-real) eigenvalues that the non-Hermitian skin effect must produce. The SERIES pass 31c sweeps the asymmetry parameter across a fine grid.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_31_hatano_nelson/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Hatano–Nelson model is the canonical laboratory of non-Hermitian topology: asymmetrised hopping drives every eigenvalue off the real axis and piles the eigenstates at the boundary — the skin effect. For the AB-cloud record this battery plays a specific falsification role: the Hermitian certificates of Tests 15–27 are meaningful only if the instrument can detect their violation, and a genuinely non-Hermitian deformation is the sharpest possible violation. The deterministic verdict (an exact count/pattern check, not a statistical trend) shows the suite's machinery responding correctly to the deformation, and the SERIES sweep maps the transition boundary. The monograph's robustness chapter uses this test — alongside the disorder controls of Tests 18, 27 and 32–33 — to document that the statistical and exact instruments of the record are live probes rather than rubber stamps. The 31c fine sweep is preserved verbatim in the console capture.
## 3. What the test verifies (verbatim from the run's report)
> Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern. METHOD: Deterministic non-Hermitian spectral property: complex eigenvalue count/pattern. Test 31 SERIES: n=5 realizations × σ∈{0.5,0.6,0.7,0.8} @48x48, n_cx mean 0,2225,2281,2295, ⟨r⟩ 0.8953→0.9253, max|Im| 0.3184→0.9576.
## 4. Verdict lines of the reference run (verbatim)
> Test 31: max|Im(E)|=0.6397, ⟨r⟩_NH=0.8938 → PASS
> Test 31b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
> Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A31.docx` | 10.1 KB | Editable edition of the same report (Microsoft Word). |
| `report_A31.html` | 7.4 KB · 83 lines | Web edition of the same report (self-contained HTML). |
| `report_A31.md` | 7.0 KB · 93 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A31.pdf` | 9.9 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[05:25:20.846] [+20311.875s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[05:25:24.130] [+20315.159s]  calc: ⟨r⟩_NN = 0.894102 (n=2304, Poisson-box ref NaN, 10 clouds)
[05:25:39.893] [+20330.922s]  calc: ⟨r⟩_NN = 0.907204 (n=2304, Poisson-box ref 0.851687, 10 clouds)
[05:25:56.656] [+20347.685s]  calc: ⟨r⟩_NN = 0.925299 (n=2304, Poisson-box ref 0.852026, 10 clouds)
[05:26:13.442] [+20364.470s]  calc: ⟨r⟩_NN = 0.930754 (n=2304, Poisson-box ref 0.850043, 10 clouds)
[05:26:14.212] [+20365.240s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[05:26:17.814] [+20368.842s]  calc: ⟨r⟩_NN = 0.887760 (n=2304, Poisson-box ref NaN, 10 clouds)
[05:26:33.688] [+20384.716s]  calc: ⟨r⟩_NN = 0.910544 (n=2304, Poisson-box ref 0.852173, 10 clouds)
[05:26:50.420] [+20401.449s]  calc: ⟨r⟩_NN = 0.923175 (n=2304, Poisson-box ref 0.852783, 10 clouds)
[05:27:06.833] [+20417.861s]  calc: ⟨r⟩_NN = 0.930952 (n=2304, Poisson-box ref 0.850774, 10 clouds)
[05:27:07.596] [+20418.624s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[05:27:11.143] [+20422.171s]  calc: ⟨r⟩_NN = 0.898821 (n=2304, Poisson-box ref NaN, 10 clouds)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 31 (pass 3, SERIES): Hatano–Nelson — realization ensemble
────────────────────────────────────────────────────────────
 Ensemble: n=5 realizations × σ ∈ {0.5, 0.6, 0.7, 0.8}, γ = 5.0
 Lattice: 48x48 (N=2304), W_eff = 1.00 (standard), Nv=4 neutral, q=±1.00
 ⚠ RUNTIME: 15 zgeev + 5 heevr rows at 48² ≈ 1–2 min
 real 1/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8941 (2.9 s)
 real 1/5 σ=0.6: n_complex =  2243, max|Im| = 0.3195, ⟨r⟩NN = 0.9072 (15.5 s)
 real 1/5 σ=0.7: n_complex =  2283, max|Im| = 0.6397, ⟨r⟩NN = 0.9253 (16.8 s)
 real 1/5 σ=0.8: n_complex =  2298, max|Im| = 0.9602, ⟨r⟩NN = 0.9308 (16.8 s)
 real 2/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8878 (3.2 s)
 real 2/5 σ=0.6: n_complex =  2237, max|Im| = 0.3194, ⟨r⟩NN = 0.9105 (15.9 s)
 real 2/5 σ=0.7: n_complex =  2297, max|Im| = 0.6396, ⟨r⟩NN = 0.9232 (16.7 s)
 real 2/5 σ=0.8: n_complex =  2299, max|Im| = 0.9598, ⟨r⟩NN = 0.9310 (16.4 s)
 real 3/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8988 (3.1 s)
 real 3/5 σ=0.6: n_complex =  2147, max|Im| = 0.3147, ⟨r⟩NN = 0.8788 (15.6 s)
 real 3/5 σ=0.7: n_complex =  2239, max|Im| = 0.6319, ⟨r⟩NN = 0.8882 (17.2 s)
 real 3/5 σ=0.8: n_complex =  2274, max|Im| = 0.9501, ⟨r⟩NN = 0.8920 (17.0 s)
 real 4/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8977 (3.1 s)
 real 4/5 σ=0.6: n_complex =  2260, max|Im| = 0.3199, ⟨r⟩NN = 0.9035 (16.4 s)
 real 4/5 σ=0.7: n_complex =  2300, max|Im| = 0.6399, ⟨r⟩NN = 0.9233 (16.6 s)
 real 4/5 σ=0.8: n_complex =  2303, max|Im| = 0.9601, ⟨r⟩NN = 0.9355 (16.2 s)
 real 5/5 σ=0.5: n_complex =     0, max|Im| = 0.0000, ⟨r⟩NN = 0.8982 (3.1 s)
 real 5/5 σ=0.6: n_complex =  2237, max|Im| = 0.3183, ⟨r⟩NN = 0.9061 (16.2 s)
 real 5/5 σ=0.7: n_complex =  2287, max|Im| = 0.6381, ⟨r⟩NN = 0.9201 (17.1 s)
 real 5/5 σ=0.8: n_complex =  2303, max|Im| = 0.9578, ⟨r⟩NN = 0.9372 (17.9 s)

 Ensemble means: σ=0.5: n_cx=0.0, max|Im|=0.00e+00, ⟨r⟩=0.8953
 σ=0.8: n_cx=2295.4, max|Im|=0.9576, ⟨r⟩=0.9253 | Poisson-box baseline ≈ 0.8500
 S1 anchor: OK ✓ | S2 sweep: OK ✓ | S3 ⟨r⟩ rise: OK ✓ (0.8953→0.9253) | S4 max|Im| grow: OK ✓ (0.3184→0.9576)
────────────────────────────────────────────────────────────
 σ=0.5 Hermitian ∀real PASS — n_complex = 0 and max|Im| < 1e-10 in all 5 realizations
 n_complex > 0 ∀(σ,k) PASS — every non-Hermitian row (5 × 3) develops complex eigenvalues
 ⟨r⟩ rises with σ (2-D repulsion) PASS — ensemble mean 0.8953 (σ=0.5, line) → 0.9253 (σ=0.8, area)
 max|Im| grows with σ PASS — ensemble mean 0.3184 (σ=0.6) → 0.9576 (σ=0.8), g = (σ−½)·ln|γ|
 Test 31c [SERIES pass 3]: 4 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 31 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 31` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 31 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_30](../test_30_vf_scaling/README.md) · [test_32](../test_32_rmean_bootstrap/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
