# Test 34: DIRECT AB-cloud vs ζ (full loaded set)
Verdict: FAIL   |   Generated: 2026-09-02 22:03:38   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
 METHOD: Statistical: unfolded-spacing KS (effect size D<0.10) + Montgomery R₂(s) vs ζ-zeros and GUE. full 50k range, not ζ-5000.
Test 34 HARDCORE pass 2: n=5 realizations, R₂ ds=0.05/s_max=4.0, per-realization KS stability.
Test 34 HARDCORE: D=0.1096 (p=2.236e-186), per-real D med 0.1153 (spread 0.0923..0.1189), ⟨|ΔR₂|⟩=0.0002, d_GUE=0.8764.

## Result
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/plot_03` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 34 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[21:37:05.355] [+28140.637s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:41:58.186] [+28433.468s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:47:07.004] [+28742.286s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:52:23.759] [+29059.041s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[21:57:55.738] [+29391.021s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 34 (pass 2, HARDCORE): direct AB vs ζ — deep validation
n ≥ 5 realizations, R₂ bins 0.05, per-realization KS stability
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 AB realizations at 96x96 + ζ unfolding (50000 zeros) → ≈ 12–17 min
 Config: Nv=2, q=1.00, α=0.5000, W=1.0 (base protocol)
 real  1/5: 5528 spacings, D_k(ζ) = 0.0923
 real  2/5: 5527 spacings, D_k(ζ) = 0.1188
 real  3/5: 5528 spacings, D_k(ζ) = 0.1153
 real  4/5: 5528 spacings, D_k(ζ) = 0.1065
 real  5/5: 5528 spacings, D_k(ζ) = 0.1189

 Pooled: 27639 AB spacings vs 49999 ζ spacings | KS D = 0.1096, p = 2.236e-186
 Per-realization D(ζ): min 0.0923 / median 0.1153 / max 0.1189 (n=5)
 ⟨|R₂_AB − R₂_ζ|⟩ (ds=0.05, s≤4) = 0.0002 (target < 0.10)
 d_GUE = 0.8764 vs d_Poisson = 0.9998 → closer to GUE
────────────────────────────────────────────────────────────
 KS composite         WARN — p = 2.236e-186, D = 0.1096 (p>0.01 or D<0.10)
 ⟨|ΔR₂|⟩ < 0.10 (fine) PASS — ds=0.05, s_max=4.0: 0.0002
 closer to GUE        PASS — d_GUE=0.8764 < d_Pois=0.9998
 KS ensemble stability PASS — D spread 0.0923..0.1189 (median 0.1153)
 Test 34b [HARDCORE pass 2]: 4 sub-checks, 1 failed → WARN
```
