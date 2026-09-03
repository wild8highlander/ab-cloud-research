# Test 15: AB-cloud Hamiltonian construction
Verdict: PASS   |   Generated: 2026-09-02 14:03:25   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
 METHOD: Mixed: Hermiticity/τ_TRB are EXACT (machine-ε), ⟨r⟩ check is STATISTICAL.
Test 15 HARDCORE: full plaquette scan 96x96 (±-quartet), signed flux 4/4, empty 9021/9021, worst empty flux 0.00e+00.

## Result
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 15 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[14:03:14.215] [+909.497s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, open, 4 vortices, model=:dirac
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 15 (pass 2, HARDCORE): AB-cloud construction — deep validation
Full-lattice plaquette scan of the ±-quartet (all plaquettes, signed check)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: 1 build + O(N) plaquette scan at 96x96 (N=9216) — seconds
 Lattice: 96x96 open :dirac, α=0, quartet q=±1.00 → 9025 plaquettes scanned
 Vortex plaquettes (signed): 4/4 correct ✓
 Empty plaquettes clean (<1e-9): 9021/9021, worst |flux| = 0.00e+00
────────────────────────────────────────────────────────────
 full signed scan     PASS — 4/4 vortex plaquettes, 9021/9021 empty clean
 hermiticity          PASS — verify_hermitian on the quartet H
 Test 15b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
