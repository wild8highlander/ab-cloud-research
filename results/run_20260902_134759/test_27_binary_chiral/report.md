# Test 27: Binary chiral symmetry at α=1/2
Verdict: PASS   |   Generated: 2026-09-02 17:11:46   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control.
 METHOD: EXACT: defect 0 on pure lattice; W>0 row is the honest breaker control.
Test 27 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058), vortex 0.00e+00 (preserved), Coulomb W-scan 0.101→0.746 (ratio 7.42), ε-floor W-independent.

## Result
 Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 27 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[17:09:31.246] [+12086.528s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[17:09:41.157] [+12096.439s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[17:09:55.379] [+12110.661s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
[17:10:08.671] [+12123.951s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 2 vortices, model=:monumental
[17:10:18.050] [+12133.332s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[17:10:34.693] [+12149.975s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 2 vortices, model=:monumental
[17:10:48.183] [+12163.465s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 2 vortices, model=:monumental
[17:11:01.755] [+12177.037s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.50, torus, 0 vortices, model=:monumental
[17:11:12.887] [+12188.169s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[17:11:24.557] [+12199.839s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=2.00, torus, 0 vortices, model=:monumental
[17:11:34.547] [+12209.830s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, torus, 0 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 27 (pass 2, HARDCORE): binary chiral symmetry — deep audit
Exact row + ε_rms contract + vortex preservation + Coulomb W-scan
(launch-standard lattice, 96x96 in two-pass mode)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 11 builds + 11 S·H·S defect evals at 96x96 (Diagonal S, O(N²)) — ≈ 2–4 min
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
────────────────────────────────────────────────────────────
 exact row < 1e-10    PASS — binary contract at α=1/2, W=0: 0.00e+00
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 ≈ analytic 2‖ε‖_F/‖H‖_F = 0.0058
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 Coulomb W-scan linear PASS — Nv=2: monotone, defect 0.101→0.746, ratio 7.42 ∈ [5, 12]
 Test 27b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
