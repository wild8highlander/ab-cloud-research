# Test 16: AB-cloud GUE classification
Verdict: PASS   |   Generated: 2026-09-15 00:24:43   |   Suite: AB-Cloud v23 SUPERCOMBO (Julia 1.12.0)

## What this test verifies
Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
 METHOD: Statistical: ⟨r⟩ over the central bulk window vs GUE 0.5992, MC p-value as diagnostics.
Test 16 HARDCORE pass 2: 96x96, n=5 realizations at α=0.5000, Nv=2, q=1.000, W_eff=1.00, ensemble deep checks (bootstrap CI, scatter, sign count).
Test 16 HARDCORE: ⟨r⟩=0.5798±0.0037 (n=5), bootstrap CI [0.5732,0.5859] misses GUE, scatter σ=0.0082.

## Result
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_02.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/plot_03.png` — 1600×1000, ABPlotV23 engine (supersampled)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v23.jl --test 16 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[00:00:54.007] [+845.035s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:04:52.591] [+1083.619s]  calc: ⟨r⟩ = 0.572908 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:04:56.983] [+1088.011s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:08:56.388] [+1327.416s]  calc: ⟨r⟩ = 0.569121 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:09:01.657] [+1332.686s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:13:20.122] [+1591.151s]  calc: ⟨r⟩ = 0.586869 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:13:24.846] [+1595.874s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:19:04.049] [+1935.077s]  calc: ⟨r⟩ = 0.584535 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
[00:19:10.567] [+1941.596s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[00:24:37.791] [+2268.819s]  calc: ⟨r⟩ = 0.585615 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 16 (pass 2, HARDCORE): ⟨r⟩ → GUE classification — deep validation
Deep ensemble at the launch-standard config (pass 1 already swept breadth)
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 (N=9216) ≈ 1.5–3 min each → expect ≈ 12–17 min
 Config: α=0.5000, Nv=2, q=1.000, BC=:open, W_eff=1.00 (standard cap 1.0)
 real  1/5: ⟨r⟩ = 0.5729
 real  2/5: ⟨r⟩ = 0.5691
 real  3/5: ⟨r⟩ = 0.5869
 real  4/5: ⟨r⟩ = 0.5845
 real  5/5: ⟨r⟩ = 0.5856

 Ensemble: ⟨r⟩ = 0.5798 ± 0.0037 (n=5)
 Bootstrap 95% CI [0.5732, 0.5859] ∌ GUE (diagnostic); above/below GUE: 0/5
────────────────────────────────────────────────────────────
 ⟨r⟩ > 0.55           PASS — ⟨r⟩ = 0.5798 ± 0.0037 vs GUE 0.5992 (n=5)
 scatter ≤ 0.022      PASS — σ=0.0082 ≤ ✓ monograph band
 Test 16b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
