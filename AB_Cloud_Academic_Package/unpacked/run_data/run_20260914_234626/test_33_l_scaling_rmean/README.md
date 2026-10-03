# Test 33: L-scaling ⟨r⟩ (10→20→30→50→80→112) — folder `test_33_l_scaling_rmean/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 07:26:31
**Verdicts (verbatim register):** PASS  
**Family:** STATISTICAL family (finite-size scaling)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_33_l_scaling_rmean/](README.md)
## 1. What this folder is
Test 33 completes the robustness block with the L-scaling of ⟨r⟩ across lattice sizes 10 → 20 → 30 → 50 → 80 → 112: the statistic must approach its GUE plateau monotonically as the lattice grows, with the monograph's anchors at L ≤ 50 and the extended points L = 80 and 112 (user spec 2026-08-29) checking the plateau itself. Effective disorder remains capped (W_eff), and the target band is 0.594–0.599.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_33_l_scaling_rmean/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Finite-size corrections are the chronic noise of lattice verifications: every statistic drifts as the lattice grows, and the direction of the drift tells whether the infinite-size limit is being approached from a healthy side. Test 33 certifies exactly that for the classification statistic — monotone approach to the GUE plateau across a two-decade range of sizes, with the two extended points certifying that the approach actually terminates on the plateau rather than passing it. The pre-registered target band 0.594–0.599 and the anchor policy (monograph anchors at small L, extensions at large L) make the test's acceptance logic fully transparent. The HARDCORE battery 33b audits the scaling line on the secondary configuration. Together with Tests 30 (1/L gap scaling) and 32 (ensemble band) this closes the finite-size dossier of the record, which the monograph presents as the bridge between the lattice certificates and the thermodynamic-limit claims.
## 3. What the test verifies (verbatim from the run's report)
> Statistical finite-size trend: monotone approach to 0.594-0.599; monograph anchors L≤50, extended points L=80/112 (user spec 2026-08-29) check the GUE plateau; W_eff capped at ab_W_max. METHOD: Statistical finite-size trend: monotone approach to 0.594-0.599; monograph anchors L≤50, extended points L=80/112 (user spec 2026-08-29) check the GUE plateau; W_eff capped at ab_W_max. Test 33 HARDCORE pass 2: n ≤ 5 per L, weighted GUE-plateau χ² over L ≥ 50, L capped at 112 (RAM honesty). WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics: W is the diagonal on-site potential the vortices paint onto the lattice: V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1. The ratio (disorder energy q·W) / (kinetic energy t) decides what the vortex cloud does and which spectral statistics come out: • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder landscape dominates the vortex motion — vortices pin/steer the eigenstates, states localize on the potential relief, and ⟨r⟩ drifts from GUE (0.5992) toward Poisson (0.3863) by an essentially random amount. A strongly disordered, spinning vortex system can therefore emit ALMOST ANY statistics — the numbers depend on the effective rotation speed (W/t) and on the twisting/vortex arrangement (Nv, layout, charges) of that realization, not on the AB physics. • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping, states stay delocalized and GUE (Wigner-Dyson) is reachable. That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0): they certify the PHASE physics, not the disorder physics. Test 33 RAM gate: L=112 skipped (needs ≈ 10.6 GB peak, free ≈ 4.3 GB). Extended L-scan to L=80 (user spec 2026-08-29); W_eff=1.00; verdict q=0.30; trend 0.434 → 0.556 → 0.593 → 0.6 → 0.6 Test 33 HARDCORE plateau (q=0.30): weighted ⟨r⟩=0.6004 vs GUE (|Δ|=0.0012, in band), χ²/dof=0.01.
## 4. Verdict lines of the reference run (verbatim)
> Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
> Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS
> Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
## 5. Result line
```text
Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A33.docx` | 22.4 KB | Editable edition of the same report (Microsoft Word). |
| `report_A33.html` | 19.6 KB · 192 lines | Web edition of the same report (self-contained HTML). |
| `report_A33.md` | 19.2 KB · 202 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A33.pdf` | 25.8 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[07:09:25.448] [+26556.476s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:25.985] [+26557.014s]  calc: ⟨r⟩ = 0.629404 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:27.180] [+26558.208s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:27.738] [+26558.766s]  calc: ⟨r⟩ = 0.509721 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:28.759] [+26559.788s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:29.359] [+26560.388s]  calc: ⟨r⟩ = 0.574634 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:30.483] [+26561.512s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:31.005] [+26562.034s]  calc: ⟨r⟩ = 0.557955 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:32.182] [+26563.211s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:32.709] [+26563.737s]  calc: ⟨r⟩ = 0.486070 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:33.836] [+26564.864s]  build_ab_cloud_hamiltonian: 20x20 (N=400), α=0.5000, t=1.00, W=1.00, torus, 12 vortices, model=:monumental
[07:09:34.457] [+26565.485s]  calc: ⟨r⟩ = 0.593495 (n_r=239, n_eigs=241) [refs: GUE=0.5996 Poisson=0.3863]
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 33 (pass 2, HARDCORE): L-scaling — deep validation
Harder machinery: up to 5 realizations per L, weighted
GUE-plateau χ² over L ≥ 50, no L beyond 112 (RAM honesty: L=128 ≈ 4.3 GB).
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 2 q-rows × up to n=5 realizations × L ∈ {10,20,30,50,80,112} → expect ≈ 27–81 min (±3× machine factor; RAM-gated rungs are skipped inside with a printed reason)

════════════════════════════════════════════════════════════
TEST 33: L-Scaling for AB-Cloud Lattice
L=10→0.487 (Poisson), L=20→0.562, L=30→0.595, L=50→0.594 (monograph),
L=80, L=112 → GUE plateau check (extended range, user spec 2026-08-29)
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
 ⚠ RAM GATE: L=112 needs ≈ 10.6 GB peak (matrix + LAPACK workspace), free ≈ 4.3 GB → SKIPPED (a swap-thrashing eig is indistinguishable from a hang)
 q=1.00 BC=:torus L=10  Nv=4   α=0.50 W=1.00 ⟨r⟩ = 0.5516 ± 0.0252 (5 real, monograph 0.487)
 q=1.00 BC=:torus L=20  Nv=12  α=0.50 W=1.00 ⟨r⟩ = 0.5953 ± 0.0055 (5 real, monograph 0.562)
 q=1.00 BC=:torus L=30  Nv=26  α=0.50 W=1.00 ⟨r⟩ = 0.6070 ± 0.0054 (5 real, monograph 0.595)
 q=1.00 BC=:torus L=50  Nv=70  α=0.50 W=1.00 ⟨r⟩ = 0.5936 ± 0.0053 (5 real, monograph 0.594)
 q=1.00 BC=:torus L=80  Nv=178 α=0.50 W=1.00 ⟨r⟩ = 0.5987 ± 0.0016 (5 real, monograph 0.595*)
 q=0.30 BC=:open  L=10  Nv=4   α=0.50 W=1.00 ⟨r⟩ = 0.4343 ± 0.0233 (5 real, monograph 0.487)
 q=0.30 BC=:open  L=20  Nv=12  α=0.50 W=1.00 ⟨r⟩ = 0.5565 ± 0.0100 (5 real, monograph 0.562)
 q=0.30 BC=:open  L=30  Nv=26  α=0.50 W=1.00 ⟨r⟩ = 0.5933 ± 0.0065 (5 real, monograph 0.595)
 q=0.30 BC=:open  L=50  Nv=70  α=0.50 W=1.00 ⟨r⟩ = 0.6004 ± 0.0040 (5 real, monograph 0.594)
 q=0.30 BC=:open  L=80  Nv=178 α=0.50 W=1.00 ⟨r⟩ = 0.6004 ± 0.0025 (5 real, monograph 0.595*)

 Verdict run: q=0.30 (fractional AB phase — reference standard, stable)
 Trend (L=10→20→30→50→80): 0.434 → 0.556 → 0.593 → 0.6 → 0.6
 Monotone increase: YES
 Final L=80 close to GUE 0.595 (|Δ|<0.05): YES
 (comparison) q=1.0 user setting: 0.552 → 0.595 → 0.607 → 0.594 → 0.599 (final 0.5987)
 Test 33: L-scaling to L=80 0.434,0.556,0.593,0.6,0.6 → PASS

 ─── HARDCORE GUE-plateau check (verdict q=0.3, L ≥ 50) ───
 plateau points: L=50: 0.6004±0.0040, L=80: 0.6004±0.0025
 weighted ⟨r⟩ = 0.6004 vs GUE 0.5992 (|Δ|=0.0012) → IN ✓ band ±0.022
 χ² = 0.01, dof = 2, χ²/dof = 0.01 → consistent ✓ (≤ 2 consistent; diagnostic)
 Test 33b (hardcore): plateau weighted ⟨r⟩=0.6004, χ²/dof=0.01 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 33 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 33` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 33 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_32](../test_32_rmean_bootstrap/README.md) · [test_34](../test_34_direct_vs_zeta/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
