# Test 24: Dirac string flux verification
Verdict: PASS   |   Generated: 2026-09-15 01:26:46   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
 METHOD: EXACT: plaquette flux = 2πq (mod 2π); tolerance = round-off accumulation across the lattice.
Test 24 HARDCORE: 4-config full scan on 96x96, worst empty flux 8.88e-16, hermiticity true.

## Result
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 24 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[01:26:05.603] [+5956.631s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:18.836] [+5969.864s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:28.248] [+5979.276s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
[01:26:37.309] [+5988.338s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 1 vortices, model=:dirac
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 24 (pass 2, HARDCORE): Dirac-string flux — exhaustive scan
Full plaquette scan × 4 configs: 2 positions × {+1, −1, +0.3}
────────────────────────────────────────────────────────────
 Lattice: 96x96 (N=9216 sites) — full plaquette scan × 4 configs
 cfg A (ix=32, iy=48, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg B (ix=64, iy=24, q=+1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A− (ix=32, iy=48, q=-1.0): vortex 1/1, empty 9024/9024 → OK
 cfg A frac (ix=32, iy=48, q=+0.3): vortex 1/1, empty 9024/9024 → OK
 Max |flux| over ALL empty plaquettes and configs: 8.88e-16
────────────────────────────────────────────────────────────
 scan A q=+1.0        PASS — 9025/9025 plaquettes OK
 scan B q=+1.0        PASS — 9025/9025 plaquettes OK
 scan A− q=-1.0       PASS — 9025/9025 plaquettes OK
 scan A frac q=+0.3   PASS — 9025/9025 plaquettes OK
 hermiticity (all)    PASS — verify_hermitian per config
 Test 24b [HARDCORE pass 2]: 5 sub-checks, 0 failed → PASS
```
