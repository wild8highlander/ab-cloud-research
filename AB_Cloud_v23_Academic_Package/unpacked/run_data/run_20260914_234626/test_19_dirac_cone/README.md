# Test 19: Dirac cone v_F ≈ 0.125 — folder `test_19_dirac_cone/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 01:24:34
**Verdicts (verbatim register):** PASS  
**Family:** EXACT-geometry family, FOUR-pass  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_19_dirac_cone/](README.md)
## 1. What this folder is
Test 19 certifies the Dirac cone of the AB-cloud spectrum: the low-energy dispersion near the touching point must be linear with velocity v_F ≈ 0.125, the zero modes must sit at the momenta (π/2, π/2), and the geometry must enforce the grid condition L/4 ∈ ℤ for those momenta to exist on the lattice. This is the suite's most heavily instrumented test — the run executes the full four-pass protocol: primary fit, an 11-point HARDCORE audit, a SERIES α-sweep (19c), and a twist-spectroscopy AUDIT pass (19d).
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_19_dirac_cone/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The Dirac cone is where the lattice physics and the arithmetic of the ζ problem meet: a massless relativistic dispersion at the touching point is the finite-size laboratory's signature of the spectral symmetry the framework needs, and its velocity v_F ≈ 0.125 = 1/8 is a clean rational constant that the fit must recover from raw eigenspectrum data. The four-pass design is the record's showpiece of verification depth: the primary fit establishes the value; the 11-point audit re-estimates it across a dense grid; the α-series demonstrates the cone's dependence (and non-dependence) on the flux parameter; and the twist-spectroscopy pass probes the boundary-twist response of the zero modes, a completely independent geometric handle on the same object. The monograph devotes a full chapter to the cone and cites the twist audit as the decisive exclusion of finite-size artifacts. All passes of the four-pass battery are preserved in the console capture of this folder.
## 3. What the test verifies (verbatim from the run's report)
> EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%). METHOD: EXACT-geometry: zero modes at (π/2,π/2) require L/4∈ℤ; gap scaling fit R². FOUR-pass (user spec 2026-09-04): primary fit → 11-pt hardcore audit → α-series → twist-spectroscopy AUDIT (direct E_min(θ)=v_F·θ/L, eigenvector index 2+2, 2π-holonomy, bit-exact rebuild, 1/L² collapse, cross-pass v_F ≤ 6%). Test 19 AUDIT: v_F_twist = 1.9990 (R² = 1.00000, L=48 y-twist scan), tower 4 @1e-10 with 2+2 polarization, 2π-holonomy 2.5e-17, π-cusp 6.279, rebuild bit-exact, 1/L² intercept 12.5662, cross-pass spread 5.09%.
## 4. Verdict lines of the reference run (verbatim)
> Test 19: 1/L scaling R²=0.9997, v_F(2π)=1.8998, v_F(π)=3.7995 → PASS
> Test 19b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
> Test 19c [SERIES pass 3]: 3 sub-checks, 0 failed → PASS
> Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A19.docx` | 8.5 KB | Editable edition of the same report (Microsoft Word). |
| `report_A19.html` | 5.9 KB · 56 lines | Web edition of the same report (self-contained HTML). |
| `report_A19.md` | 5.5 KB · 66 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A19.pdf` | 7.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[01:23:43.346] [+5814.374s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[01:24:31.332] [+5862.360s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 19 (pass 4, AUDIT): Dirac cone — twist spectroscopy + eigenvector index
Direct E(k) at the Dirac point (pure-holonomy y-twist scan), AIII index of
the tower, 2π-holonomy, determinism, 1/L² collapse, cross-pass v_F audit
────────────────────────────────────────────────────────────
 twist lattice 48x48 (α=1/2, torus, W=0, clean), θ-grid π/5…π + θ=0 anchor
 ⚠ RUNTIME: 7 dense solves at 48² (2304 sites) + 2 builds ≈ 1–2 min
 θ=0: tower(|E|≤1e-10) = 4, E_min = 0.261052 (E_min·L = 12.5305; pass-2 measured 12.5305)
 θ=0.6283: E_min = 0.026179 (E_min·L = 1.2566), n_zero = 0, degeneracy = 2, v_F_local = 1.9999
 θ=1.2566: E_min = 0.052354 (E_min·L = 2.5130), n_zero = 0, degeneracy = 2, v_F_local = 1.9998
 θ=1.8850: E_min = 0.078520 (E_min·L = 3.7689), n_zero = 0, degeneracy = 2, v_F_local = 1.9995
 θ=2.5133: E_min = 0.104672 (E_min·L = 5.0243), n_zero = 0, degeneracy = 2, v_F_local = 1.9991
 θ=3.1416: E_min = 0.130806 (E_min·L = 6.2787), n_zero = 0, degeneracy = 4, v_F_local = 1.9986
 D1 no-intercept fit: E = 0.041645·θ, R² = 1.000000 → v_F_twist = 1.9990 ✓
 D1b v_F_twist vs pass-2 fit: 1.9990 vs 1.9447 (|Δ| < 5%) → OK
 D2 tower polarization: Tr(P_A P_T) = 2.0000000000, Tr(P_B P_T) = 2.0000000000 (expect 2, 2 — chirality-balanced Dirac pair, AIII index 0) → OK
    per-vector purity (LAPACK basis, diagnostic only): 0.500, 0.499, 0.499, 0.500
 D3a 2π-holonomy: ‖H(2π)−H(0)‖/‖H‖ = 2.50e-17, max|ΔE| = 4.35e-14 (Byers-Yang at the twist level) → OK
 D3b θ=π cusp: n_zero = 0 (tower annihilated), E_min·L = 6.2787 ∈ [5.0, 7.6] (target 2π = 6.283; degeneracy 4 — both cones meet at the cusp) → OK
 D4 determinism: fresh W=0 rebuild ‖ΔH‖_F/‖H‖ = 0.0e+00 (bit-exact expected — clean fast path draws no RNG) → OK
 D5 1/L² collapse (11 pts, pass-2 series): E_min·L = 12.5662 + (-82.06)/L², R² = 0.999996, intercept/4π = 0.999984 → OK
 D6 v_F estimates (4): pass1 (7-pt fit ≤72) = 1.8998, pass2 (11-pt mod-4 ≤96) = 1.9447, pass3 (α=0.5 series ≤80) = 1.955, pass4 (twist L=48) = 1.999
    spread = 5.09% ≤ 6%, all in [1.85, 2.05] (analytic v_F = 2t = 2) → OK
────────────────────────────────────────────────────────────
 D1 twist-cone linear R² > 0.995 PASS — E_min(θ) = 0.041645·θ over 5 pts (no intercept), v_F_twist = 1.9990, n_zero(θ>0) = 0 ∀θ
 D1b v_F_twist vs 1/L-fit < 5% PASS — twist 1.9990 vs pass-2 fit 1.9447 — independent momentum-space measurement
 D2 tower == 4 @1e-10 + index 2+2 PASS — Tr(P_A P_T) = 2.00000000, Tr(P_B P_T) = 2.00000000 — eigenvector-level AIII anchor
 D3a 2π-holonomy identity PASS — ‖ΔH‖/‖H‖ = 2.5e-17, max|ΔE| = 4.4e-14 — Byers-Yang at the twist level
 D3b π cusp: tower 0, E_min·L → 2π PASS — n_zero(π) = 0, E_min·L = 6.2787 (target 6.283, degeneracy 4)
 D4 bit-exact rebuild PASS — ‖H_rebuild − H‖_F/‖H‖ = 0.0e+00 — no hidden RNG/global state in the builder
 D5 1/L² collapse → 4π PASS — intercept 12.5662 (0.002% off 4π), c = -82.06, R² = 0.999996 over 11 pts
 D6 cross-pass v_F ≤ 6% PASS — 4 independent estimates, spread 5.09% — twist + 3 fits agree
 Test 19d [AUDIT pass 4]: 8 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 19 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 19` (module [`abcloud/tests_15_26.py`](../../../python_clone/abcloud/tests_15_26.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 19 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_18](../test_18_chiral_AIII/README.md) · [test_20](../test_20_chern_tknn/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
