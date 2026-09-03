# Test 25: Byers-Yang theorem check
Verdict: PASS   |   Generated: 2026-09-02 16:39:23   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
 METHOD: EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
Test 25 HARDCORE: Byers-Yang Δ<1e-10 for 3 layouts × q∈{+1,+2,−1} on 96x96 → true; fractional q∈{0.3,0.5} Δ>1e-3 → true.

## Result
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 25 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[15:35:41.679] [+6456.961s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 0 vortices, model=:dirac
[15:41:02.317] [+6777.599s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:46:12.181] [+7087.464s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:51:19.675] [+7394.957s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[15:56:20.440] [+7695.722s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[16:02:24.284] [+8059.566s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[16:07:53.533] [+8388.815s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:13:03.640] [+8698.922s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:18:21.308] [+9016.591s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:23:36.816] [+9332.098s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:29:01.269] [+9656.551s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[16:34:17.440] [+9972.722s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 25 (pass 2, HARDCORE): Byers–Yang — multi-layout / multi-q audit
3 layouts × {+1, +2, −1} integer rows + fractional {0.3, 0.5} rows
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 12 value-only diagonalizations at 96x96 (N=9216) — expect ≈ 10–15 min
 layout 1, q=+1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, q=+2: Δ = 1.04e-14 < 1e-10 ✓
 layout 1, q=-1: Δ = 9.66e-15 < 1e-10 ✓
 layout 1, fractional q=0.3: Δ = 3.35e-03 > 1e-3 ✓ (genuine AB effect)
 layout 1, fractional q=0.5: Δ = 3.74e-03 > 1e-3 ✓ (genuine AB effect)
 layout 2, q=+1: Δ = 1.24e-14 < 1e-10 ✓
 layout 2, q=+2: Δ = 8.66e-15 < 1e-10 ✓
 layout 2, q=-1: Δ = 1.24e-14 < 1e-10 ✓
 layout 3, q=+1: Δ = 1.01e-14 < 1e-10 ✓
 layout 3, q=+2: Δ = 8.89e-15 < 1e-10 ✓
 layout 3, q=-1: Δ = 1.01e-14 < 1e-10 ✓
────────────────────────────────────────────────────────────
 integer q ∀layouts   PASS — Δ(q=+1,+2,−1 vs 0) < 1e-10 on 3 independent layouts
 fractional Δ > 1e-3  PASS — q ∈ {0.3, 0.5} keep the genuine AB effect
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
