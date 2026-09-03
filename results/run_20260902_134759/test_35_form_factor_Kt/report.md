# Test 35: Spectral form factor K(t)
Verdict: FAIL   |   Generated: 2026-09-02 22:36:30   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
 METHOD: Statistical: raw (1/n)|Σe^{itε}|² vs finite-box GUE reference K_box(t)=t(1−sinc(2πt)); RMS over t≥0.3.
Test 35 HARDCORE pass 2: n=5 per-realization K(t), 33-point t-grid, ensemble mean verdict.
Test 35 HARDCORE: ensemble RMS=0.6143, corr_box=0.6379, corr_ζ=0.8123, RMS scatter σ=0.1856.

## Result
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 35 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[22:09:09.750] [+30065.032s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:14:37.106] [+30392.388s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:19:44.711] [+30699.993s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:24:48.414] [+31003.696s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
[22:30:51.804] [+31367.086s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 2 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 35 (pass 2, HARDCORE): spectral form factor K(t) — ensemble pass
n ≥ 5 per-realization K(t), 33-point t-grid, ensemble verdict
────────────────────────────────────────────────────────────
 ⚠ RUNTIME: n=5 realizations at 96x96 → expect ≈ 12–17 min
 real  1/5: RMS(K−K_box, t≥0.3) = 0.9199
 real  2/5: RMS(K−K_box, t≥0.3) = 0.8578
 real  3/5: RMS(K−K_box, t≥0.3) = 0.9671
 real  4/5: RMS(K−K_box, t≥0.3) = 0.7540
 real  5/5: RMS(K−K_box, t≥0.3) = 0.4999

 ENSEMBLE K(t): RMS(K_AB − K_box, t ≥ 0.3) = 0.6143 (target < 0.30)
 Corr(K_AB, K_box) = 0.6379 (target > 0.50) | Corr(K_AB, K_ζ) = 0.8123
 Per-realization RMS: mean 0.7998, scatter σ = 0.1856 > ✗ 0.15
────────────────────────────────────────────────────────────
 RMS < 0.30 (ensemble) WARN — ensemble-mean K(t), 33-point grid: 0.6143
 Corr > 0.50 (ensemble) PASS — Corr(K, K_box) = 0.6379
 RMS scatter ≤ 0.15   WARN — σ=0.1856 across 5 realizations
 Test 35b [HARDCORE pass 2]: 3 sub-checks, 2 failed → WARN
```
