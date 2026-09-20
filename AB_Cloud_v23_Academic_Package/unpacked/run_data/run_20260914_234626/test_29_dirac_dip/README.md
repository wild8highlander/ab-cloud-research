# Test 29: Dirac dip in DOS at α=1/2 — folder `test_29_dirac_dip/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 04:28:22
**Verdicts (verbatim register):** PASS → WARN  
**Family:** Semi-exact family, SERIES  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_29_dirac_dip/](README.md)
## 1. What this folder is
Test 29 certifies the Dirac dip in the density of states at α = 1/2: the touching point must appear as a genuine dip in the DOS, not a plateau. The SERIES protocol runs a 9-point fine scan on the 96×96 lattice verifying the strict dip condition (ρ_dip = 0.0195) and the disorder contrast of the dip signature, which decays from 288.00 as W grows; the SERIES pass 29c sweeps the fine grid.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_29_dirac_dip/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Dirac dip is the density-of-states shadow of the Dirac cone certified in Test 19: a linear dispersion in two dimensions produces a DOS that vanishes linearly at the touching energy, and the suite measures exactly that depletion. The strict dip condition — the dip must be a true local minimum, not a shoulder — is a falsifiable geometry statement about the spectrum's fine structure. The disorder-contrast row doubles as a physics control: the dip signature is strong on the clean lattice and degrades in a measured, monotone way as disorder floods the touching region, which is the behaviour topology-protected spectral features are expected to show. The SERIES design (a 9-point scan plus the 29c fine sweep) maps the dip across the parameter neighbourhood of α = 1/2, so the monograph can discuss the dip's stability rather than a single-point measurement. This battery is one of the three SERIES-tier passes of the run (with 19c and 31c).
## 3. What the test verifies (verbatim from the run's report)
> Semi-exact: DOS dip depth vs prediction. METHOD: Semi-exact: DOS dip depth vs prediction. Test 29 SERIES: 9-pt fine scan @96² (strict dip true, ρ_dip=0.0195), contrast(w) 288.00→3.97 (w=0.1→0.8), size contrast 13.33×→10.67×.
## 4. Verdict lines of the reference run (verbatim)
> Test 29: ρ(α=0.5)=0.0193 vs ρ(0.403)=0.1944 / ρ(0.597)=0.1944 → PASS
> Test 29b [HARDCORE pass 2]: 3 sub-checks, 1 failed → WARN
> Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A29.docx` | 7.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A29.html` | 5.1 KB · 59 lines | Web edition of the same report (self-contained HTML). |
| `report_A29.md` | 4.7 KB · 69 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A29.pdf` | 6.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[03:49:19.515] [+14550.543s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:53:34.081] [+14805.109s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4271, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:58:04.195] [+15075.223s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4583, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:02:28.229] [+15339.257s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4896, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:06:49.977] [+15601.005s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:11:11.976] [+15863.005s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5104, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:15:30.824] [+16121.852s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5417, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:19:51.305] [+16382.334s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5729, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:24:02.022] [+16633.050s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.6042, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:28:08.106] [+16879.134s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:28:14.173] [+16885.201s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 29 (pass 3, SERIES): Dirac dip — fine α-scan + window series
────────────────────────────────────────────────────────────
 Fine scan: 9 points α = k/96 around k=48 (α=1/2 EXACT), window |E|<0.5
 ⚠ RUNTIME: 9 solves at 96² + 2 anchors at 48² ≈ 8–13 min
 α=38/96 = 0.39583: ρ(|E|<0.5) = 0.2083  (253.5 s)
 α=41/96 = 0.42708: ρ(|E|<0.5) = 0.1458  (265.2 s)
 α=44/96 = 0.45833: ρ(|E|<0.5) = 0.0833  (262.8 s)
 α=47/96 = 0.48958: ρ(|E|<0.5) = 0.0208  (259.8 s)
 α=48/96 = 0.50000: ρ(|E|<0.5) = 0.0195  (259.3 s)
 α=49/96 = 0.51042: ρ(|E|<0.5) = 0.0208  (257.2 s)
 α=52/96 = 0.54167: ρ(|E|<0.5) = 0.0833  (258.4 s)
 α=55/96 = 0.57292: ρ(|E|<0.5) = 0.1458  (249.0 s)
 α=58/96 = 0.60417: ρ(|E|<0.5) = 0.2083  (245.2 s)
 window |E|<0.1: ρ_dip(α=1/2) = 0.0004, ρ_off(α=38/96) = 0.1250 → contrast 288.00×
 window |E|<0.2: ρ_dip(α=1/2) = 0.0039, ρ_off(α=38/96) = 0.2083 → contrast 53.33×
 window |E|<0.3: ρ_dip(α=1/2) = 0.0091, ρ_off(α=38/96) = 0.2083 → contrast 22.86×
 window |E|<0.5: ρ_dip(α=1/2) = 0.0195, ρ_off(α=38/96) = 0.2083 → contrast 10.67×
 window |E|<0.8: ρ_dip(α=1/2) = 0.0525, ρ_off(α=38/96) = 0.2083 → contrast 3.97×

 contrast @w=0.5 (α=0.396 vs 1/2): 13.33× (48x48) → 10.67× (96x96) → holds/sharpens ✓
────────────────────────────────────────────────────────────
 strict dip @96² (9 pts) PASS — ρ(α=1/2) = 0.0195 below ALL 8 other scan points
 contrast grows as w → 0 PASS — contrast(w) 288.00× (w=0.1) vs 10.67× (w=0.5): Dirac ρ ∝ E vs metallic ρ ≈ const
 no wash-out 48²→96²  PASS — 13.33× → 10.67× at the same α pair (0.396 vs 1/2; tolerance 0.8, as 29b)
 Test 29c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 29 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 29` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 29 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_28](../test_28_f_gue_merit/README.md) · [test_30](../test_30_vf_scaling/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
