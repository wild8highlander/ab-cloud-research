# Test 30: Dirac cone vF scaling vs L — folder `test_30_vf_scaling/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 04:40:07
**Verdicts (verbatim register):** PASS  
**Family:** EXACT-geometry family  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_30_vf_scaling/](README.md)
## 1. What this folder is
Test 30 measures the finite-size scaling of the Dirac velocity: the first distinct spectral level above the zero tower must approach the touching point as ~ 1/L. The suite notes a subtle rework — the older probe using ev[j0+1] − ev[j0] hit the valley-degenerate partner at ~1e-15 and read zero gaps, so the test now targets the first distinct Dirac level — with the L/4 ∈ ℤ grid enforced up to t31_lmax and a linearity verdict on the 1/L law.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_30_vf_scaling/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Scaling tests are where finite-size numerics face their sternest audit: a genuine relativistic touching point produces gaps that shrink as exactly 1/L on a clean geometry, while any lattice artifact produces its own characteristic (typically slower or erratic) scaling. The rework documented in the test's own description is a case study in verification hygiene: the suite discovered that its original gap probe had been reading a degenerate partner level — a measurement of the wrong object — and replaced it with the first distinct level, re-validating the whole scaling line. The linearity verdict on the 1/L law across the enforced L ≡ 0 (mod 4) grid is the certificate that the touching point is a genuine Dirac point of the continuum limit, not a finite-size accident. The monograph's finite-size chapter pairs this test with Test 19 (the cone itself) and Test 33 (the ⟨r⟩ scaling) as the record's three scaling certificates.
## 3. What the test verifies (verbatim from the run's report)
> EXACT-geometry: FIRST DISTINCT Dirac level above the zero tower ~ 1/L (the old ev[j0+1]-ev[j0] hit the valley-degenerate partner ~1e-15 → gaps 0.0); L/4∈ℤ grid up to t31_lmax; linear fit R². METHOD: EXACT-geometry: FIRST DISTINCT Dirac level above the zero tower ~ 1/L (the old ev[j0+1]-ev[j0] hit the valley-degenerate partner ~1e-15 → gaps 0.0); L/4∈ℤ grid up to t31_lmax; linear fit R². Test 30 HARDCORE: 11-point fit R²=0.9999, v_F=1.9447, E₁·L cv=0.75%, zero tower 4 ∀L.
## 4. Verdict lines of the reference run (verbatim)
> Test 30: v_F=1.798, R²=0.9977 → PASS
> Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A30.docx` | 7.6 KB | Editable edition of the same report (Microsoft Word). |
| `report_A30.html` | 5.0 KB · 56 lines | Web edition of the same report (self-contained HTML). |
| `report_A30.md` | 4.6 KB · 66 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A30.pdf` | 6.5 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[04:30:03.322] [+16994.351s]  build_ab_cloud_hamiltonian: 16x16 (N=256), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:04.976] [+16996.005s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:06.368] [+16997.396s]  build_ab_cloud_hamiltonian: 32x32 (N=1024), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:08.104] [+16999.132s]  build_ab_cloud_hamiltonian: 40x40 (N=1600), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:10.730] [+17001.759s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:15.385] [+17006.413s]  build_ab_cloud_hamiltonian: 56x56 (N=3136), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:25.362] [+17016.391s]  build_ab_cloud_hamiltonian: 64x64 (N=4096), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:46.224] [+17037.252s]  build_ab_cloud_hamiltonian: 72x72 (N=5184), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:31:31.588] [+17082.616s]  build_ab_cloud_hamiltonian: 80x80 (N=6400), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:32:56.543] [+17167.571s]  build_ab_cloud_hamiltonian: 88x88 (N=7744), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:35:25.008] [+17316.036s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 30 (pass 2, HARDCORE): Dirac cone velocity — dense-grid audit
────────────────────────────────────────────────────────────
 11-point mod-4 grid L=16…96, zero-tower check, E₁·L constancy
 ⚠ RUNTIME: 11 value-only diagonalizations, L up to 96 — expect ≈ 8–12 min
 L=16: E₁ = 0.765367 (E₁·L = 12.2459), zero_modes = 4, 0.5 s
 L=24: E₁ = 0.517638 (E₁·L = 12.4233), zero_modes = 4, 0.5 s
 L=32: E₁ = 0.390181 (E₁·L = 12.4858), zero_modes = 4, 0.8 s
 L=40: E₁ = 0.312869 (E₁·L = 12.5148), zero_modes = 4, 1.8 s
 L=48: E₁ = 0.261052 (E₁·L = 12.5305), zero_modes = 4, 3.9 s
 L=56: E₁ = 0.223929 (E₁·L = 12.5400), zero_modes = 4, 9.2 s
 L=64: E₁ = 0.196034 (E₁·L = 12.5462), zero_modes = 4, 19.8 s
 L=72: E₁ = 0.174311 (E₁·L = 12.5504), zero_modes = 4, 44.4 s
 L=80: E₁ = 0.156918 (E₁·L = 12.5535), zero_modes = 4, 83.8 s
 L=88: E₁ = 0.142678 (E₁·L = 12.5557), zero_modes = 4, 147.2 s
 L=96: E₁ = 0.130806 (E₁·L = 12.5574), zero_modes = 4, 277.7 s

 Fit: gap = 12.2188/L + 0.0054, R² = 0.999880, v_F = 1.9447 (π-flux target 2.0)
 E₁·L: mean = 12.5003, cv = 0.75% ≤ ✓ 5%
────────────────────────────────────────────────────────────
 R² > 0.95 (11 pts)   PASS — R² = 0.9999
 zero tower == 4 ∀L   PASS — |E| ≤ 1e-8 at every size
 E₁·L cv ≤ 5%         PASS — cv = 0.75% (Dirac law: E₁·L → 4π = const)
 Test 30b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 30 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 30` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 30 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_29](../test_29_dirac_dip/README.md) · [test_31](../test_31_hatano_nelson/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
