# Test 17: Connes self-duality α↔1/α
Verdict: PASS   |   Generated: 2026-09-02 15:07:36   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: isospectrality under α ↔ 1/α to machine precision.
 METHOD: EXACT: isospectrality under α ↔ 1/α to machine precision.
Test 17 HARDCORE L=24: zero_modes(α=1/2)=4, spectral defects 1.42e-15/1.66e-15, duality defect 3.62e-01.
Test 17 HARDCORE L=48: zero_modes(α=1/2)=4, spectral defects 2.90e-15/2.41e-15, duality defect 3.65e-01.
Test 17 HARDCORE L=96: zero_modes(α=1/2)=4, spectral defects 3.96e-15/3.24e-15, duality defect 3.66e-01.

## Result
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 17 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
[14:40:55.756] [+3171.039s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:40:59.296] [+3174.578s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:00.067] [+3175.349s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:00.859] [+3176.141s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:01.457] [+3176.739s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:02.710] [+3177.992s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:08.135] [+3183.417s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:13.525] [+3188.807s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:41:19.476] [+3194.758s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:20.433] [+3195.715s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:41:32.373] [+3207.655s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:46:45.944] [+3521.226s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:52:04.211] [+3839.493s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3333, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[14:57:25.070] [+4160.352s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
[14:57:36.057] [+4171.339s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=2.0000, t=1.00, W=4.00, open, 0 vortices, model=:monumental
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 17 (pass 2, HARDCORE): Connes self-duality — cross-size audit
Zero-mode invariant + spectral symmetries on the size ladder 24 → ab_nx
────────────────────────────────────────────────────────────
 L=24: zero_modes(α=1/2)=4 | spec.defect(1/2)=1.42e-15, (1/3)=1.66e-15 | duality=3.62e-01
 L=48: zero_modes(α=1/2)=4 | spec.defect(1/2)=2.90e-15, (1/3)=2.41e-15 | duality=3.65e-01
 L=96: zero_modes(α=1/2)=4 | spec.defect(1/2)=3.96e-15, (1/3)=3.24e-15 | duality=3.66e-01
 At α=1/3 the spectrum stays gapped at E=0 on these tori (base observation).
────────────────────────────────────────────────────────────
 zero_modes(1/2)=4 ∀L PASS — topological invariant holds on the whole ladder
 E→−E defect < 1e-10 ∀L PASS — α=1/2 and α=1/3, generic bipartite symmetry
 Test 17b [HARDCORE pass 2]: 2 sub-checks, 0 failed → PASS
```
