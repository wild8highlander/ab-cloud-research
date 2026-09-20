# Test 25: Byers-Yang theorem check
Verdict: PASS   |   Generated: 2026-09-15 02:34:35   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
 METHOD: EXACT: spectra identical for q and q+1 (Δ~1e-15); fractional q must DIFFER (non-neutral config).
Test 25 HARDCORE: Byers-Yang Δ<1e-10 for 3 layouts × q∈{+1,+2,−1} on 96x96 → true; fractional q∈{0.3,0.5} Δ>1e-3 → true.

## Result
 Test 25b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 25 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[01:29:46.459] [+6177.487s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 0 vortices, model=:dirac
[01:35:14.706] [+6505.734s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:40:55.414] [+6846.443s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:46:20.418] [+7171.446s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[01:51:30.629] [+7481.657s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[01:56:54.159] [+7805.187s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 1 vortices, model=:dirac
[02:02:23.302] [+8134.330s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:07:47.600] [+8458.629s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:13:15.445] [+8786.473s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:18:29.329] [+9100.357s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:23:43.775] [+9414.803s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
[02:29:13.016] [+9744.044s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=0.00, open, 4 vortices, model=:dirac
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
