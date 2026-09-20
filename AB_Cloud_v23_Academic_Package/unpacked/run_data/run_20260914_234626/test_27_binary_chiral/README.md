# Test 27: Binary chiral symmetry at α=1/2 — folder `test_27_binary_chiral/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 03:09:45
**Verdicts (verbatim register):** PASS  
**Family:** EXACT (with statistical ζ-dictionary layer)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_27_binary_chiral/](README.md)
## 1. What this folder is
Test 27 is the v23.2-reworked binary chiral-symmetry certificate at α = 1/2. On the pure lattice the chiral defect must be exactly zero — and it is. The W > 0 row is retained as the honest breaker control. The rework's distinctive feature is the ζ-dictionary layer: pass 1 embeds 20,000 ζ zeros into the lattice dictionary for an honest statistical ⟨r⟩ verdict, while the HARDCORE pass embeds the full 50,000-zero dataset.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_27_binary_chiral/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
The chiral defect — the exact norm-based measure of how far the operator is from the AIII symmetry boundary — is the binary instrument: zero or not zero, with no intermediate verdict allowed. What elevates Test 27 beyond Test 18 is the dictionary construction: the ζ zeros are embedded into the lattice's spectral bookkeeping, and the spacing-ratio statistic of the resulting object is computed at two dataset depths. This is the framework's constructive answer to the standard objection that lattice spectra merely resemble random matrices: the ζ data are not compared with the lattice from the outside, they are carried inside its dictionary and the composite object is then audited. The two-depth design (20,000 for the primary pass, 50,000 for the audit) makes the embedding's stability visible in the same battery. The monograph's dictionary chapter presents this test as the constructive bridge between the statistical evidence (Tests 4–14, 16) and the exact lattice certificates (Tests 15, 17–26).
## 3. What the test verifies (verbatim from the run's report)
> EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification. METHOD: EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control. ζ-dictionary (v23.2 rework): pass 1 embeds 20,000 zeros (honest ⟨r⟩ verdict), HARDCORE embeds the full 50,000 with ±E pairing probes, ⟨r⟩ GUE-window + Poisson discrimination control, 5×10k block stationarity and KS GUE-vs-GOE classification. Test 27 ζ-DEEP (50k): pairing exact on the 100000-dim dictionary, ⟨r⟩ 0.6119 (GUE 0.5996), Poisson control 0.3864, block spread 0.0050, KS D_GUE 0.0216 vs D_GOE 0.0881. Test 27 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058), vortex 0.00e+00 (preserved), Coulomb W-scan 0.101→0.746 (ratio 7.42), ε-floor W-independent.
## 4. Verdict lines of the reference run (verbatim)
> Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS
## 5. Result line
```text
Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A27.docx` | 9.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A27.html` | 7.2 KB · 71 lines | Web edition of the same report (self-contained HTML). |
| `report_A27.md` | 6.7 KB · 81 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A27.pdf` | 9.3 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[03:07:31.877] [+12042.906s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:07:42.466] [+12053.494s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[03:07:57.316] [+12068.344s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
[03:08:09.555] [+12080.584s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 2 vortices, model=:monumental
[03:08:19.657] [+12090.685s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[03:08:33.394] [+12104.422s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 2 vortices, model=:monumental
[03:08:44.376] [+12115.405s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 2 vortices, model=:monumental
[03:08:58.626] [+12129.654s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 0 vortices, model=:monumental
[03:09:10.593] [+12141.621s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[03:09:21.957] [+12152.985s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 0 vortices, model=:monumental
[03:09:34.381] [+12165.410s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 0 vortices, model=:monumental
[03:09:43.051] [+12174.079s]  calc: KS D = 0.021619, p_asymptotic = 9.567870e-21 (n=49999, λ=4.8368)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 27 (pass 2, HARDCORE): binary chiral symmetry — deep audit
Exact row + ε_rms contract + vortex preservation + Coulomb W-scan
(launch-standard lattice, 96x96 in two-pass mode)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 11 builds + 11 S·H·S defect evals at 96x96 (Diagonal S, O(N²)) + ζ-50k deep statistics (O(n)) — ≈ 2–4 min
 H1 exact row (W=0, clean):     defect = 0.00e+00 < ✓ 1e-10
 H2 ε row (W=1.0, Nv=0):      defect = 5.77e-03 vs ε_rms = 0.0058 (analytic) ∈ [0.5, 2.0]× ✓
 H2v vortex row (Nv=2, W=0):    defect = 0.00e+00 < 1e-10 ✓ (bond phases PRESERVE AIII)
 W-scan (Nv=2) W=0.5: defect = 1.0052e-01
 W-scan (Nv=2) W=1.0: defect = 2.0010e-01
 W-scan (Nv=2) W=2.0: defect = 3.9425e-01
 W-scan (Nv=2) W=4.0: defect = 7.4620e-01
 H3 scan: monotone ✓, defect(W=4)/defect(W=0.5) = 7.42 ∈ [5, 12] ✓
 Nv=0 ε-floor diagnostic (residual ε is FIXED-amplitude):
 W-scan (Nv=0) W=0.5: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=1.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=2.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 W-scan (Nv=0) W=4.0: defect = 5.7704e-03 ≈ ε_rms (W-independent ✓)
 ζ-dictionary DEEP audit (pass 2) — full 50000-zero embedded dataset:
 Z1 monotone (50000 zeros): min Δγ = 0.029538 → OK
 Z2 ±E pairing (D=diag(±γₖ/2), 100000-dim): max|d+d_σ| = 0.0e+00, ‖D+ΓDΓ‖/‖D‖ = 0.00e+00, ‖Γ²v−v‖ = 0.0e+00 → EXACT AIII
 Z3 zero modes of the dictionary: 0 (AIII index anchor; min|γₖ| = 14.1347) → OK
 Z4 ⟨r⟩(49998 raw-gap ratios) = 0.6119 (GUE 0.5996; window ±0.020) vs Poisson control 0.3864 (same n, separation 0.225 > 0.15) → OK (GUE-class, discriminated)
 Z5 block stationarity (5×10k): ⟨r⟩ = 0.6147, 0.6121, 0.6120, 0.6097, 0.6109, spread = 0.0050 < 0.012 → OK
 Z6 KS: D_GUE = 0.021619 (< 0.030), D_GOE = 0.088053 → GUE-class ✓; depth diagnostic: no pass-1 baseline
────────────────────────────────────────────────────────────
 exact row < 1e-10    PASS — binary contract at α=1/2, W=0: 0.00e+00
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 ≈ analytic 2‖ε‖_F/‖H‖_F = 0.0058
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 Coulomb W-scan linear PASS — Nv=2: monotone, defect 0.101→0.746, ratio 7.42 ∈ [5, 12]
 ζ-dict exact ±E pairing PASS — 100k-dim dictionary: max|d+d_σ| = 0.0e+00, ‖D+ΓDΓ‖/‖D‖ = 0.00e+00, Γ² probe 0.0e+00, tower 0
 ζ-50k ⟨r⟩ GUE-window + control PASS — ⟨r⟩ = 0.6119 (GUE 0.5996 ±0.020), Poisson control 0.3864, separation 0.225 > 0.15
 ζ-50k block stationarity PASS — 5×10k blocks spread 0.0050 < 0.012
 ζ-50k KS GUE-class   PASS — D_GUE = 0.0216 < 0.030 and < D_GOE = 0.0881 (Poisson would be ≈0.28)
 Test 27b [HARDCORE pass 2]: 8 sub-checks, 0 failed → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 27 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 27` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 27 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_26](../test_26_pbc_torus/README.md) · [test_28](../test_28_f_gue_merit/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
