# Test 20: TKNN Chern number C₁=1 (gapped anchors) — folder `test_20_chern_tknn/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:25:02
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (topological invariant)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_20_chern_tknn/](README.md)
## 1. What this folder is
Test 20 computes the TKNN Chern number of the AB-cloud bands and certifies C₁ = +1 on the magnetic Brillouin zone. The construction uses the Fuhs–Hatsugai–Suzuki (FHS) projector method on the q×q Harper grid; the gapped anchor points α = 1/4, 1/3, 1/5 carry the exact integer invariant, while α = 1/2 is correctly identified as the Dirac touching where the per-band Chern number is undefined — the touching-ladder rungs require L ≡ 0 (mod 4) so that the touching momentum (π/2, π/2) lies on the grid.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_20_chern_tknn/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
A Chern number is a topological integer: it cannot drift, bend, or almost-agree — the FHS computation either lands on the exact integer or it does not, which makes this test one of the hardest possible falsification instruments in the record. The result C₁ = +1 identifies the AB-cloud bands as Chern bands with unit Chern number, the same topology that underlies the integer quantum Hall effect, and ties the framework to the vast machine of topological band theory. The test's treatment of α = 1/2 is as informative as its gapped verdicts: at the touching point the concept of a per-band Chern number genuinely breaks down, and the suite's handling of the ladder rungs — requiring the grid to respect the touching momentum — demonstrates that the topological bookkeeping is being done correctly rather than conveniently. The monograph's topology chapter builds on this certificate when introducing the chiral and streaming probes of Tests 18, 24 and 27.
## 3. What the test verifies (verbatim from the run's report)
> EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells). METHOD: EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells). Test 20 HARDCORE: anchors 1/4,1/3,1/5 → +1 ✓; ladder 12..72 → 1,1,1,1,1,1; α=1/2 touching ∀L, mass branch 0 ✓.
## 4. Verdict lines of the reference run (verbatim)
> Test 20: C₁ anchors {1/4,1/3,1/5}=1,1,1 [exp 1,1,1], α=1/2 min gap=0.0 (Dirac touching), mass branch C=0/0 → PASS
> Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A20.docx` | 6.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A20.html` | 4.1 KB · 48 lines | Web edition of the same report (self-contained HTML). |
| `report_A20.md` | 3.6 KB · 58 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A20.pdf` | 5.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
(no log_comp entries)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 20 (pass 2, HARDCORE): TKNN Chern number — deep audit
Anchors {1/4, 1/3, 1/5} + size ladder 12→72 + α=1/2 touching audit
────────────────────────────────────────────────────────────
 α=1/4: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.646
 α=1/3: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.268
 α=1/5: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.554
 α=1/3 ladder L=12 (  48 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=18 ( 108 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=24 ( 192 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=36 ( 432 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=48 ( 768 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=72 (1728 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/2 L=12: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=16: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=24: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=48: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=72: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 mass branch (24×12 grid): C(m=+0.3) = +0 (gap 0.435), C(m=−0.3) = +0 (gap 0.435) ✓
────────────────────────────────────────────────────────────
 anchors C₁=+1 {1/4,1/3,1/5} PASS — TKNN Diophantine t₁=+1, grid-converged 12→24 points
 ladder C₁=+1, L=12..72 PASS — magnetic-BZ FHS on L = 12/18/24/36/48/72 (α=1/3)
 α=1/2 Dirac touching + branch PASS — bare gap ≈ 1e-16 ∀L (rungs L ≡ 0 mod 4 — Dirac points on-grid); mass-regularized C₁ = 0 (chirality-balanced)
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 20 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 20` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 20 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_19](../test_19_dirac_cone/README.md) · [test_21](../test_21_gamma_phase/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
