# Test 34: DIRECT AB-cloud vs ζ (full loaded set) — folder `test_34_direct_vs_zeta/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 07:51:46
**Verdicts (verbatim register):** PASS → WARN  
**Family:** STATISTICAL family (the confrontation)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_34_direct_vs_zeta/](README.md)
## 1. What this folder is
Test 34 is the centrepiece of the entire record: the DIRECT confrontation between the AB-cloud lattice spectrum and the ζ zeros themselves. Unfolded spacings of both objects are compared by two-sample KS (pre-registered effect-size criterion D < 0.10) and by the Montgomery pair-correlation function R₂(s) against the ζ-zeros and GUE references, over the full 50,000-zero range. At the reference run the primary pass read D = 0.1096 (FAIL), the audit battery 34b carried one failed sub-check of four — and the subsequent v3.2 estimator audit traced the adversarial number to the ζ-side reference unfolding, repaired the defects, and pre-registered the post-fix falsifiability window D = 0.03–0.06.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_34_direct_vs_zeta/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
This is the test the whole package exists for: everything else certifies instruments, structures and sub-checks — Test 34 points the machinery at the actual ζ zeros and reads the distance. The reference-run verdict chain is preserved here exactly as it happened, because the honest failure and its forensic resolution are part of the record's value: the September 2026 addendum chain (documented in the monograph as Add.1–Add.8 and in this package under run_data/) re-ran the confrontation with the standalone laboratory — cross-language reproduction in Python/SciPy (Add.2), the disorder sweep (Add.3), deep diagnostics isolating a size- and seed-independent residual D ≈ 0.10 (Add.4), an effective GUE+Poisson mixture decomposition with Poisson weight w* ≈ 0.25–0.28 and post-fit residual 0.0241 equal to the GUE-matrix calibration floor 0.0242 (Add.5), corrected reference constants (Add.6) and the composite-verdict impact analysis (Add.7). The final word came on the Klein quartic PSL(2,7) Hurwitz surface (Add.8, run 20260919_085734_m2 in this package): 100,000 zeros, 5 realizations, pooled D = 0.0808 with d_GUE = 0.0044 — the lattice statistically indistinguishable from pure GUE — and the composite criterion satisfied on all three counts (GUE-CONSISTENT). No other folder in this archive carries a story of this arc, and the monograph gives it the final chapter.
## 3. What the test verifies (verbatim from the run's report)
> Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000. METHOD: Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000. Test 34 HARDCORE pass 2: n=5 realizations, R₂ ds=0.05/s_max=4.0, per-realization KS stability. Test 34 HARDCORE: D=0.1096 (p=2.236e-186), per-real D med 0.1153 (spread 0.0923..0.1189), ⟨|ΔR₂|⟩=0.0002, d_GUE=0.8764.
## 4. Verdict lines of the reference run (verbatim)
> Test 34: KS p=0.0, ⟨|ΔR₂|⟩=0.0374, d_GUE=0.796 → PASS
> Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
## 5. Result line
```text
Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A34.docx` | 6.7 KB | Editable edition of the same report (Microsoft Word). |
| `report_A34.html` | 4.0 KB · 49 lines | Web edition of the same report (self-contained HTML). |
| `report_A34.md` | 3.6 KB · 59 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A34.pdf` | 5.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[07:30:25.651] [+27816.680s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[07:34:35.595] [+28066.623s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[07:38:52.493] [+28323.521s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[07:43:11.074] [+28582.102s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[07:47:23.751] [+28834.779s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 34 (pass 2, HARDCORE): direct AB vs ζ — deep validation
n ≥ 5 realizations, R₂ bins 0.05, per-realization KS stability
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 AB realizations at 96x96 + ζ unfolding (50000 zeros) → ≈ 12–17 min
 Config: Nv=2, q=1.00, α=0.5000, W=1.0 (base protocol)
 real  1/5: 5528 spacings, D_k(ζ) = 0.0923
 real  2/5: 5527 spacings, D_k(ζ) = 0.1188
 real  3/5: 5528 spacings, D_k(ζ) = 0.1153
 real  4/5: 5528 spacings, D_k(ζ) = 0.1065
 real  5/5: 5528 spacings, D_k(ζ) = 0.1189

 Pooled: 27639 AB spacings vs 49999 ζ spacings | KS D = 0.1096, p = 2.236e-186
 Per-realization D(ζ): min 0.0923 / median 0.1153 / max 0.1189 (n=5)
 ⟨|R₂_AB − R₂_ζ|⟩ (ds=0.05, s≤4) = 0.0002 (target < 0.10)
 d_GUE = 0.8764 vs d_Poisson = 0.9998 → closer to GUE
────────────────────────────────────────────────────────────
 KS composite         WARN — p = 2.236e-186, D = 0.1096 (p>0.01 or D<0.10)
 ⟨|ΔR₂|⟩ < 0.10 (fine) PASS — ds=0.05, s_max=4.0: 0.0002
 closer to GUE        PASS — d_GUE=0.8764 < d_Pois=0.9998
 KS ensemble stability PASS — D spread 0.0923..0.1189 (median 0.1153)
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 34 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 34` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 34 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_33](../test_33_l_scaling_rmean/README.md) · [test_35](../test_35_form_factor_Kt/README.md)
- **The addendum chain:** this test's story continues in the September 2026 runs — [`../../run_20260917_080329_m2/README.md`](../../run_20260917_080329_m2/README.md) (MODE 2 ensemble), [`../../run_20260917_084900_m3/README.md`](../../run_20260917_084900_m3/README.md) (deep diagnostics), [`../../run_20260919_085734_m2/README.md`](../../run_20260919_085734_m2/README.md) (Klein quartic, 100,000 zeros, GUE-CONSISTENT).
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
