# Test 36: Byte-level robustness — folder `test_36_byte_robust/`
> AB-Cloud v23 SUPERCOMBO · reference run `run_20260914_234626` · Julia 1.12.0 · generated 2026-09-15 09:08:55
**Verdicts (verbatim register):** PASS  
**Family:** Mixed (statistical robustness at byte level)  
**Location:** [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [test_36_byte_robust/](README.md)
## 1. What this folder is
Test 36 is the reproducibility stress test: the ⟨r⟩ statistic is recomputed after the entire input pipeline is pushed through 256-level byte quantization, with 200,000 quantization bytes drawn under seed 12345 and the verdict taken as a multi-window average over the 120×1?? window geometry (sample accumulated to 25,000 eigenvalues in pass 1 and 50,000 in pass 2). The certified quantity is |Δr| — the largest statistic shift the quantization can induce.
This folder is the canonical, reading-friendly archive of the test inside the reference run. It holds the four-format report (`report.md/html/pdf/docx`), the timestamped computation log and raw console capture (in [`logs/`](logs/README.md)), and the figures (in [`plots/`](plots/README.md)). Raw provenance copies of the same report files and logs ship in the run's [`FINAL_REPORT/`](../FINAL_REPORT/README.md) (`reports/` and `logs/test_36_byte_robust/`), and the test's verdict lines are registered in `FINAL_REPORT/logs/results_verdicts.txt` — quoted verbatim in section 4 below.
## 2. Why this test matters
Every floating-point result in this archive ultimately depends on bytes flowing through a specific implementation, and Test 36 asks the impertinent question directly: how much of the verdict structure survives when the input precision is deliberately coarsened to byte level? The design quantizes at the 256-level granularity, accumulates the statistic over the full pass-2 eigenvalue budget, and averages over the window geometry so that no single window can swing the verdict. A small |Δr| certificate means the spectral classification is a property of the mathematics, not of the last bits of the input representation — the digital robustness that any independent reimplementer (see the Python clone shipped in this very package) implicitly relies on. The monograph's reproducibility chapter cites Test 36 beside the cross-language reproduction (Add.2) as the two pillars of the record's implementation-independence argument.
## 3. What the test verifies (verbatim from the run's report)
> Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max. METHOD: Mixed: |Δr| under 256-level quantization + RNG entropy (statistical). Sample accumulated to 25 000 (pass 1) / 50 000 (pass 2) eigenvalues; verdict = multi-window average over 120×15-eig windows (single window = diagnostic); W_eff capped at ab_W_max. WHY W (DISORDER) IS CAPPED AT W_max ≈ 1.0 — disorder → vortex motion → statistics: W is the diagonal on-site potential the vortices paint onto the lattice: V_i = Σ_k q_k·W / (r_ik²·N⁻¹ + 1),   hopping t = 1. The ratio (disorder energy q·W) / (kinetic energy t) decides what the vortex cloud does and which spectral statistics come out: • q·W ≳ t  (e.g. W=4, q=0.3 → V≈1.2 next to a core): the disorder landscape dominates the vortex motion — vortices pin/steer the eigenstates, states localize on the potential relief, and ⟨r⟩ drifts from GUE (0.5992) toward Poisson (0.3863) by an essentially random amount. A strongly disordered, spinning vortex system can therefore emit ALMOST ANY statistics — the numbers depend on the effective rotation speed (W/t) and on the twisting/vortex arrangement (Nv, layout, charges) of that realization, not on the AB physics. • q·W ≲ t  (W ≤ 1): the Aharonov-Bohm phases dominate the hopping, states stay delocalized and GUE (Wigner-Dyson) is reachable. That is why these tests measure at W_eff = min(cfg.ab_W, W_max = 1.0): they certify the PHASE physics, not the disorder physics. Sample: 55290 eigs (pass 2 (secondary), target 50000, reached=yes); W_eff=1.00. Byte robustness verdict = multi-window |Δ⟨r⟩|=0.0009 (tol 0.0200, 120 windows); single-window |Δr|=0.0061 (diagnostic).
## 4. Verdict lines of the reference run (verbatim)
> Test 36: byte robust — r_256=0.5894, |Δr|_multi=0.001 (120 windows), |Δr|_1win=0.012 (diag), H=7.9991 bits, χ²_z=-0.234, n=27997 → PASS
> Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
## 5. Result line
```text
Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
```
## 6. Complete contents inventory
| File | Size | Description |
|---|---|---|
| `report_A36.docx` | 24.9 KB | Editable edition of the same report (Microsoft Word). |
| `report_A36.html` | 22.3 KB · 224 lines | Web edition of the same report (self-contained HTML). |
| `report_A36.md` | 21.9 KB · 234 lines | The test's master report (Markdown): verification statement, verdicts, result line, plot inventory, full computation log and console capture. |
| `report_A36.pdf` | 29.9 KB | Print edition of the same report (PDF). |
## 7. Computation log — verbatim excerpt
```text
[08:25:16.507] [+31107.536s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:29:46.125] [+31377.154s]  t37 pass 2 (secondary) realization 1: central block 5529 eigs, accumulated 5529 (target 50000)
[08:29:47.423] [+31378.451s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:34:04.812] [+31635.840s]  t37 pass 2 (secondary) realization 2: central block 5529 eigs, accumulated 11058 (target 50000)
[08:34:05.610] [+31636.639s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:38:39.717] [+31910.745s]  t37 pass 2 (secondary) realization 3: central block 5529 eigs, accumulated 16587 (target 50000)
[08:38:40.698] [+31911.726s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:42:58.835] [+32169.863s]  t37 pass 2 (secondary) realization 4: central block 5529 eigs, accumulated 22116 (target 50000)
[08:42:59.617] [+32170.645s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:47:25.728] [+32436.756s]  t37 pass 2 (secondary) realization 5: central block 5529 eigs, accumulated 27645 (target 50000)
[08:47:26.636] [+32437.664s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[08:51:40.917] [+32691.946s]  t37 pass 2 (secondary) realization 6: central block 5529 eigs, accumulated 33174 (target 50000)
```
Every line is timestamped (`[HH:MM:SS.mmm] [+offset-s]`) with the cumulative wall-clock offset since session start; the offsets show exactly when this test executed inside the 26-hour session.
## 8. Console capture — verbatim
The console capture prints each lettered sub-check with its statistic, its pre-registered limit, and its outcome — the audit trail the monograph's Appendix A reproduces.
```text
════════════════════════════════════════════════════════════
TEST 36: Byte-level robustness — quantization + RNG entropy
 Verify ⟨r⟩ survives 256-level quantization + RNG byte uniformity
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
 Sample target: 50000 eigenvalues [pass 2 (secondary)] (cfg.ab37_n_eigs_pass2)
 Disorder: W = 1.00 = min(ab_W=4.00, W_max=1.00) → q·W = 1.00 vs hopping t = 1.0 → AB phases dominate (byte check tests the phase physics)
 realization  1/5, continuing (below target): +5529 central eigs → accumulated 5529 / 50000 (11%)
 realization  2/5, continuing (below target): +5529 central eigs → accumulated 11058 / 50000 (22%)
 realization  3/5, continuing (below target): +5529 central eigs → accumulated 16587 / 50000 (33%)
 realization  4/5, continuing (below target): +5529 central eigs → accumulated 22116 / 50000 (44%)
 realization  5/5, continuing (below target): +5529 central eigs → accumulated 27645 / 50000 (55%)
 realization  6/6, continuing (below target): +5529 central eigs → accumulated 33174 / 50000 (66%)
 realization  7/7, continuing (below target): +5529 central eigs → accumulated 38703 / 50000 (77%)
 realization  8/8, continuing (below target): +5529 central eigs → accumulated 44232 / 50000 (88%)
 realization  9/9, continuing (below target): +5529 central eigs → accumulated 49761 / 50000 (100%)
 realization 10/10: +5529 central eigs → accumulated 55290 / 50000 (111%)
 Raw ⟨r⟩ = 0.3879 (n=55288 spacings)
 Universality class: Poisson (d_GUE=0.2117, d_GOE=0.1428, d_GSE=0.2883, d_Poi=0.0016)
 (local window: n=15 central eigs, raw ⟨r⟩_local = 0.6571)

 (a) Byte-quantization robustness (256 levels):
 legacy single window (diagnostic): r_byte = 0.6631, raw_local = 0.6571, |Δr| = 0.0061
 multi-window average (decisive; 120 windows × 15 eigs):
 ⟨r⟩_raw = 0.5765, ⟨r⟩_byte = 0.5756, |Δ⟨r⟩| = 0.0009 (tol=0.0200) → PASS

 (b) RNG byte-entropy / uniformity:
 Shannon entropy = 7.9991 bits (target ≥ 7.9)
 χ²_z (CLT approx, df=255) = -0.2342 (|z|<3.0) → PASS
 Test 36: byte robust — r_256=0.5756, |Δr|_multi=0.0009 (120 windows), |Δr|_1win=0.0061 (diag), H=7.9991 bits, χ²_z=-0.234, n=55288 → PASS
```
## 9. How to reproduce
```text
julia ab_cloud_v23.jl --test 36 --no-two-pass   # single test, single pass
julia ab_cloud_v23.jl --test all                  # full suite, reference protocol
```
The same test ships in the Python clone: `python -m abcloud.cli --test 36` (module [`abcloud/tests_27_38.py`](../../../python_clone/abcloud/tests_27_38.py)).
## 10. Where this fits in the package
- **Monograph:** Chapter 36 of Part II (*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros"*) — the chapter number is the test number.
- **Final report:** the test's section in [`../FINAL_REPORT/README.md`](../FINAL_REPORT/README.md) (all 38 reports embedded inline).
- **Neighbours:** [test_35](../test_35_form_factor_Kt/README.md) · [test_37](../test_37_half_factorial_gamma/README.md)
---
_Package overview: [unpacked/](../../README.md) · Run archive: [../](../README.md) · GitHub edition of AB-Cloud v23 (v34)._
