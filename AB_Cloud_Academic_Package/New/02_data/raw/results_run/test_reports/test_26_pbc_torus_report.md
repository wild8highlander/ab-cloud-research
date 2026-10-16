# Test 26: PBC torus Dirac string
Verdict: PASS   |   Generated: 2026-09-02 17:09:01   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
 METHOD: Mixed: flux identities exact; ⟨r⟩ on 4 neutral vortices over the bulk window (statistical).
Test 26 HARDCORE pass 2: 96x96 torus, exhaustive artifact classification, n=5 ⟨r⟩ realizations at W_eff=1.00.
Test 26 HARDCORE: artifacts 9024 clean/0 wrap/0 unexplained; ⟨r⟩=0.5964±0.0021, scatter σ=0.0046.

## Result
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 26 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[16:40:42.418] [+10357.700s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.0000, t=1.00, W=4.00, torus, 1 vortices, model=:dirac
[16:40:53.375] [+10368.657s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:46:12.496] [+10687.778s]  calc: ⟨r⟩ = 0.600632 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:46:20.404] [+10695.686s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:52:34.013] [+11069.295s]  calc: ⟨r⟩ = 0.596193 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:52:40.045] [+11075.327s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[16:58:08.064] [+11403.346s]  calc: ⟨r⟩ = 0.600551 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[16:58:13.542] [+11408.824s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[17:03:35.614] [+11730.896s]  calc: ⟨r⟩ = 0.589380 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[17:03:41.561] [+11736.843s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[17:08:56.247] [+12051.529s]  calc: ⟨r⟩ = 0.595447 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 26 (pass 2, HARDCORE): PBC torus Dirac string — deep validation
Exhaustive artifact classification + ⟨r⟩ ensemble (n ≥ 5)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: flux scan (1 build) + n=5 ⟨r⟩ realizations at 96x96 → expect ≈ 12–17 min
 ⟨r⟩ row: α=0.5000, Nv=4 (base protocol), q=1.0000, W=1.00 = ab_w_eff (capped)
 H1 flux: vortex plaquette OK; empty plaquettes: 9024 clean, 0 wrap artifacts (0.0000), 191 seam (gauge holonomy, ix=96/iy=96), 0 unexplained
 real  1/5: ⟨r⟩ = 0.6006
 real  2/5: ⟨r⟩ = 0.5962
 real  3/5: ⟨r⟩ = 0.6006
 real  4/5: ⟨r⟩ = 0.5894
 real  5/5: ⟨r⟩ = 0.5954

 Ensemble: ⟨r⟩ = 0.5964 ± 0.0021 | bootstrap CI [0.5928, 0.5997] ∋ GUE | above/below: 2/3
────────────────────────────────────────────────────────────
 flux + artifacts     PASS — vortex OK; 9024 clean + 0 wrap(−2πq) + 191 seam holonomy; 0 unexplained
 ⟨r⟩ > 0.5 (ensemble) PASS — ⟨r⟩ = 0.5964 ± 0.0021 (n=5, base contract)
 scatter ≤ 0.022      PASS — σ=0.0046 ≤ ✓ monograph band
 hermiticity ∀real    PASS — verify_hermitian per realization
 Test 26b [HARDCORE pass 2]: 4 sub-checks, 0 failed → PASS
```
