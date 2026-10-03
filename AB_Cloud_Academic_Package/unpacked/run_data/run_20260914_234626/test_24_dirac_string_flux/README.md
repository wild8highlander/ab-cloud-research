# Test 24: Dirac string flux verification — folder `test_24_dirac_string_flux/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:26:46
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (flux quantization)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_24_dirac_string_flux/](README.md)
## 1. What this folder is
Test 24 verifies Dirac string flux quantization on the lattice: every plaquette pierced by a flux tube must carry exactly 2πq of flux (modulo 2π), with the tolerance scale set by the accumulated floating-point round-off across the lattice rather than by any statistical band. The certificate covers the full lattice plaquette by plaquette.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_24_dirac_string_flux/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Dirac strings are the invisible seams of a magnetic lattice: the flux they carry is unobservable modulo 2π, and the consistency of the whole gauge construction demands that every string carry exactly the right quantum. The suite audits this plaquette by plaquette — not on averages, not on samples — so the certificate is a census, and its tolerance is the round-off accumulation budget of the lattice computation itself. This test is one of the pillars the monograph's exact layer names explicitly ('hermiticity, flux quantization, Byers–Yang invariance, chiral pairing, zero-mode index — machine-zero residuals'), and it interlocks with Test 25 (Byers–Yang invariance of the spectrum under integer flux shifts) and Test 26 (the torus neutral-vortex configuration): quantized strings are the local statement, Byers–Yang its global spectral echo. The console capture preserves the per-plaquette audit output.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice. METHOD: EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice. Test 24 HARDCORE: 4-config full scan on 96x96, worst empty flux 8.88e-16, hermiticity true.
## 4. Verdict lines of the reference run (verbatim)
> Test 24: vortex flux OK=1/1, empty OK=5040/5040, max_empty=0.0 → PASS
> Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A24.docx` | 5.7 KB | Editable edition of the same report (Microsoft Word). |
| `report_A24.html` | 3.2 KB · 40 lines | Web edition of the same report (self-contained HTML). |
| `report_A24.md` | 2.9 KB · 50 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A24.pdf` | 4.4 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[01:26:05.603] [+5956.631s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:18.836] [+5969.864s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:28.248] [+5979.276s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:37.309] [+5988.338s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 24 (pass 2, HARDCORE): Dirac-string flux — exhaustive scan
Full plaquette scan × 4 configs: 2 positions × {+1, −1, +0.3}
────────────────────────────────────────────────────────────
 Lattice: 96x96 (N=9216 sites) — full plaquette scan × 4 configs
 cfg A (ix=32, iy=48, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg B (ix=64, iy=24, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A− (ix=32, iy=48, q=-1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A frac (ix=32, iy=48, q=+0.3): vortex 1/1, empty 9024/9024 → OK
 Max |flux| over ALL empty plaquettes and configs: 8.88e-16
────────────────────────────────────────────────────────────
 scan A q=+1.0        PASS — 9025/9025 plaquettes OK
 scan B q=+1.0        PASS — 9025/9025 plaquettes OK
 scan A− q=-1.0       PASS — 9025/9025 plaquettes OK
 scan A frac q=+0.3   PASS — 9025/9025 plaquettes OK
 hermiticity (all)    PASS — verify_hermitian per config
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 24 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 24` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 24 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_23](../test_23_fractal_factor/README.md) · [test_25](../test_25_byers_yang/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
