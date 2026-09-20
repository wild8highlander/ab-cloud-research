# Test 32: Multi-realization ⟨r⟩ bootstrap — folder `test_32_rmean_bootstrap/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 06:47:18
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family (ensemble)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_32_rmean_bootstrap/](README.md)
## 1. What this folder is
Test 32 subjects the GUE classification statistic ⟨r⟩ to a multi-realization ensemble with bootstrap: the reference configuration is re-realised with independent disorder draws and the spacing-ratio mean is certified against the monograph §11.1 tolerance band 0.5992 ± 0.022, with the confidence interval printed as diagnostics. Effective disorder is capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drown the signal being certified.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_32_rmean_bootstrap/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
A single realization of a disordered lattice proves little about the configuration: the honest question is what the statistic does across the disorder ensemble. Test 32 answers it for the classification statistic — the same ⟨r⟩ that Test 16 certified on one configuration is here re-drawn realization after realization, bootstrapped, and certified inside the pre-registered band. The disorder cap is the test's methodological signature: the suite refuses to let strong disorder dilute the signal, capping W_eff at 1.0 for this and the two neighbouring scaling tests so that the ensemble measures the physics of the reference point rather than the physics of the disorder itself. The HARDCORE audit-tier battery 30b–33b carries the ensemble audit for this block. The monograph's robustness chapter cites Test 32 as the ensemble-grade confirmation of the classification verdict, with Tests 33 (size scaling) and 28 (aggregate merit) as its companions.
## 3. What the test verifies (verbatim from the run's report)
> Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion. METHOD: Statistical: ⟨r⟩ = 0.5992 ± 0.022 (tolerance band = monograph §11.1); CI printed as diagnostics. Effective disorder capped: W_eff = min(ab_W, ab_W_max ≤ 1.0) — disorder must not drive the vortex motion. Test 32 HARDCORE pass 2: 96x96, n≥5 per row, comparison-row Nv=256 (anchor density), ensemble deep checks (bootstrap CI, scatter, sign count). WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics: W is the diagonal on-site potential the vortices paint onto the lattice: V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1. The ratio (disorder energy q·W) / (kinetic energy t) decides what the vortex cloud does and which spectral statistics come out: • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder landscape dominates the vortex motion — vortices pin/steer the eigenstates, states localize on the potential relief, and ⟨r⟩ drifts from GUE (0.5992) toward Poisson (0.3863) by an essentially random amount. A strongly disordered, spinning vortex system can therefore emit ALMOST ANY statistics — the numbers depend on the effective rotation speed (W/t) and on the twisting/vortex arrangement (Nv, layout, charges) of that realization, not on the AB physics. • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping, states stay delocalized and GUE (Wigner-Dyson) is reachable. That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0): they certify the PHASE physics, not the disorder physics. Effective disorder: W_eff = 1.00 = min(ab_W=4.00, ab_W_max=1.00); disorder energy q·W_eff = 1.00 vs hopping t = 1.0 Comparison row q=0.300: W_row=0.50, Nv_row=256 → ⟨r⟩=0.6012 ± 0.0015; nearest class GUE (d_GOE=0.0705, d_GUE=0.0016, d_Poi=0.2149); vortex density 2.78% vs monograph anchor 2.78%. Test 32 HARDCORE row q=1.000: n=5, bootstrap CI [0.5838, 0.5892] misses GUE; scatter σ=0.0034 (within band). Test 32 HARDCORE row q=0.300: n=5, bootstrap CI [0.5999, 0.6026] misses GUE; scatter σ=0.0017 (within band).
## 4. Verdict lines of the reference run (verbatim)
> Test 32: ⟨r⟩=0.5991±0.0075 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
> Test 32: ⟨r⟩=0.5864±0.003 (q=1.0, n=5, W=1.0) vs GUE 0.5992 → PASS
> Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 32b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A32.docx` | 16.8 KB | Editable edition of the same report (Microsoft Word). |
| `report_A32.html` | 13.9 KB · 164 lines | Web edition of the same report (self-contained HTML). |
| `report_A32.md` | 13.5 KB · 174 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A32.pdf` | 18.9 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[05:37:38.247] [+21049.276s]  realization 1/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[05:37:39.194] [+21050.222s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[05:43:04.004] [+21375.032s]  calc: ⟨r⟩ = 0.581975 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[05:43:09.335] [+21380.363s]  realization 1/5 (q=1.000): ⟨r⟩=0.5820 in 331.1 s (bulk 5529 levels)
[05:43:09.342] [+21380.371s]  realization 2/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[05:43:10.694] [+21381.722s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[05:50:47.327] [+21838.355s]  calc: ⟨r⟩ = 0.584950 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[05:50:51.753] [+21842.782s]  realization 2/5 (q=1.000): ⟨r⟩=0.5849 in 462.4 s (bulk 5529 levels)
[05:50:51.761] [+21842.789s]  realization 3/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[05:50:53.212] [+21844.240s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[05:58:02.624] [+22273.652s]  calc: ⟨r⟩ = 0.588113 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[05:58:06.971] [+22277.999s]  realization 3/5 (q=1.000): ⟨r⟩=0.5881 in 435.2 s (bulk 5529 levels)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 32 (pass 2, HARDCORE): ⟨r⟩ bootstrap — deep validation
Harder machinery: n ≥ 5 realizations/row, comparison row
held at monograph anchor density on the current lattice, ensemble
stability checks (bootstrap CI, realization scatter, sign count).
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 2 rows × n=5 realizations at 96x96 → expect ≈ 9–14 min (measured t(L) ≈ 56·(L/96)⁶ s per eig)
 H2: comparison-row Nv rescaled to anchor density 2.78% of 96x96 → Nv=256 (was 144)

════════════════════════════════════════════════════════════
TEST 32: ⟨r⟩ bootstrap over independent realizations
Target: ⟨r⟩ = 0.5992 ± 0.022 vs GUE 0.5992 (machine-precision match)
────────────────────────────────────────────────────────────
 WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics:
  W is the diagonal on-site potential the vortices paint onto the lattice:
      V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1.
  The ratio (disorder energy q·W) / (kinetic energy t) decides what the
  vortex cloud does and which spectral statistics come out:
   • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder
     landscape dominates the vortex motion — vortices pin/steer the
     eigenstates, states localize on the potential relief, and ⟨r⟩ drifts
     from GUE (0.5992) toward Poisson (0.3863) by an essentially random
     amount. A strongly disordered, spinning vortex system can therefore
     emit ALMOST ANY statistics — the numbers depend on the effective
     rotation speed (W/t) and on the twisting/vortex arrangement (Nv,
     layout, charges) of that realization, not on the AB physics.
   • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping,
     states stay delocalized and GUE (Wigner-Dyson) is reachable.
  That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0):
  they certify the PHASE physics, not the disorder physics.
 ℹ️ NOTE: cfg.ab_q_list[1] = 1.0 is INTEGER.
 Pure Dirac-string model: integer flux is unobservable (Byers-Yang)
 → real H → GOE ceiling. The :monumental smooth gauge: phases are
 generically complex for ANY q → GUE reachable with the user's q.
 Primary verdict uses q=1.0; q=0.3 is also run for comparison.

 [q=1.000] Torus gauge-compatible (q·(2-Nx)=-94 ∈ ℤ) → using :torus BC

 Bootstrap config: 96x96, Nv=2, q=±1.000, α=0.5000, W=1.00 (cap 1.00, min(cfg.ab_W, W_max)), BC=:torus, n_real=5
 Disorder check: q·W = 1.00 vs hopping t = 1.0 → AB phases dominate (GUE reachable)
 Vortex phase model: :monumental (complex smooth-gauge phases → GUE reachable for any q)
 NOTE: this is bootstrap row 1/2 — a FULL second set of 5 realizations; the verdict comes from row 1 (the configured q).
 realization 1/5: ⟨r⟩ = 0.5820
 realization 2/5: ⟨r⟩ = 0.5849
 realization 3/5: ⟨r⟩ = 0.5881
 realization 4/5: ⟨r⟩ = 0.5909
 realization 5/5: ⟨r⟩ = 0.5862
 ⟨r⟩ = 0.5864 ± 0.0030 (95% CI [0.5835, 0.5894]) [GUE=0.5996, Pois=0.3863]
 Deviation from GUE 0.5992: -0.0128 (2.13%)
 [q=0.300] Torus not gauge-compatible (q·(2-Nx)=-28.2000 ∉ ℤ) → using :open BC
 [comparison-row overrides] W=0.50 (ab_W_cmp, cap 1.00), Nv=256 (ab_nv_cmp) (primary row: W=1.00, Nv=2)

 Bootstrap config: 96x96, Nv=256, q=±0.300, α=0.5000, W=0.50 (cap 1.00, ab_W_cmp), BC=:open, n_real=5
 Disorder check: q·W = 0.15 vs hopping t = 1.0 → AB phases dominate (GUE reachable)
 Vortex phase model: :monumental (complex smooth-gauge phases → GUE reachable for any q)
 NOTE: this is bootstrap row 2/2 — a FULL second set of 5 realizations; the verdict comes from row 1 (the configured q).
 realization 1/5: ⟨r⟩ = 0.5993
 realization 2/5: ⟨r⟩ = 0.6037
 realization 3/5: ⟨r⟩ = 0.6001
 realization 4/5: ⟨r⟩ = 0.6018
… (truncated at 60 of 84 lines; the complete capture is in [`logs/`](logs/README.md) and all four report files)
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 32 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 32` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 32 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_31](../test_31_hatano_nelson/README.md) · [test_33](../test_33_l_scaling_rmean/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
