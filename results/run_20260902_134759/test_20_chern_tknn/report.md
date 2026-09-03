# Test 20: TKNN Chern number C₁=1 (gapped anchors)
Verdict: PASS   |   Generated: 2026-09-02 15:30:18   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
 METHOD: EXACT: FHS C₁=+1 on the MAGNETIC BZ (q×q Harper; anchors α=1/4,1/3,1/5); α=1/2 = Dirac touching, per-band C undefined — touching-ladder rungs need L ≡ 0 (mod 4) so (π/2,π/2) lies on the k-grid; sub-second by design (q×q cells).
Test 20 HARDCORE: anchors 1/4,1/3,1/5 → +1 ✓; ladder 12..72 → 1,1,1,1,1,1; α=1/2 touching ∀L, mass branch 0 ✓.

## Result
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/plot_02` (.png 600dpi / .svg / .pdf)
- `plots/plot_03` (.png 600dpi / .svg / .pdf)
- `plots/plot_04` (.png 600dpi / .svg / .pdf)
- `plots/plot_05` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 20 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 20 (pass 2, HARDCORE): TKNN Chern number — deep audit
Anchors {1/4, 1/3, 1/5} + size ladder 12→72 + α=1/2 touching audit
────────────────────────────────────────────────────────────
 α=1/4: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.646
 α=1/3: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.268
 α=1/5: C₁ = +1 (12-pt grid) → +1 (24-pt grid) ✓, min gap 1.554
 α=1/3 ladder L=12 (  48 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=18 ( 108 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=24 ( 192 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=36 ( 432 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=48 ( 768 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/3 ladder L=72 (1728 k-points): C₁ = +1, min gap 1.268 ✓
 α=1/2 L=12: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=16: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=24: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=48: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 L=72: bare min gap = 5.48e-16 (touching), singular links 0
 α=1/2 mass branch (24×12 grid): C(m=+0.3) = +0 (gap 0.435), C(m=−0.3) = +0 (gap 0.435) ✓
────────────────────────────────────────────────────────────
 anchors C₁=+1 {1/4,1/3,1/5} PASS — TKNN Diophantine t₁=+1, grid-converged 12→24 points
 ladder C₁=+1, L=12..72 PASS — magnetic-BZ FHS on L = 12/18/24/36/48/72 (α=1/3)
 α=1/2 Dirac touching + branch PASS — bare gap ≈ 1e-16 ∀L (rungs L ≡ 0 mod 4 — Dirac points on-grid); mass-regularized C₁ = 0 (chirality-balanced)
 Test 20b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
