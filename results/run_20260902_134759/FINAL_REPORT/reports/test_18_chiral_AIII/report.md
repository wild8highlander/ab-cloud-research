# Test 18: Chiral symmetry AIII at α=1/2
Verdict: PASS   |   Generated: 2026-09-02 15:12:06   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
 METHOD: EXACT: ||SHS+H||/||H|| ≈ 1e-16 on the pure lattice (W=0); W>0 is the honest breaker.
Test 18 HARDCORE: exact 0.00e+00, ε-row 5.77e-03 (ε_rms 0.0058, in window), vortex 0.00e+00 (preserved), S²=I 0.00e+00 (96x96 torus).

## Result
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 18 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[15:11:28.198] [+5003.481s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[15:11:40.131] [+5015.413s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 0 vortices, model=:monumental
[15:11:52.929] [+5028.211s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 2 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 18 (pass 2, HARDCORE): chiral symmetry AIII — deep audit
Exact row + ε_rms quantitative contract + vortex-preservation row +
S² = I operator sanity (launch-standard lattice)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 3 builds + 3 S·H·S defect evals at 96x96 (Diagonal S, O(N²)) — ≈ 1–2 min
 H1 exact row (α=1/2, W=0):      defect = 0.00e+00 < ✓ 1e-10
 H2 ε row (W=1.0, Nv=0):       defect = 5.77e-03 vs ε_rms = 0.0058 (analytic) ∈ [0.5, 2.0]× ✓
 H2v vortex row (Nv=2, W=0):     defect = 0.00e+00 < 1e-10 ✓ (bond phases PRESERVE AIII)
 H3 operator sanity: ‖S² − I‖/‖I‖ = 0.00e+00 < ✓ 1e-12
────────────────────────────────────────────────────────────
 exact row < 1e-10    PASS — ‖SHS+H‖/‖H‖ = 0.00e+00 at α=1/2, W=0
 ε_rms contract (W=1.0) PASS — defect 5.77e-03 vs analytic 2‖ε‖_F/‖H‖_F = 0.0058 (size-independent)
 vortices PRESERVE AIII PASS — defect = 0.00e+00 (Nv=2, q=±1.00, W=0) — bond phases; Byers-Yang for integer q
 S² = I               PASS — ‖S²−I‖/‖I‖ = 0.00e+00
 Test 18b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
