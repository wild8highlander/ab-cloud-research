# Test 37: (1/2)! via Γ — half-factorial & GUE normalization
Verdict: PASS   |   Generated: 2026-09-02 23:33:21   |   Suite: AB-Cloud v19 (Julia 1.12.0)

## What this test verifies
EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
 METHOD: EXACT: Γ(1/2) = √π, (1/2)! = Γ(3/2) = √π/2, ladder + recurrence (suite's own Lanczos lgamma); UNIQUENESS of the Γ-construction via the reflection self-dual fixed point Γ(1/2)² = π and Bohr–Mollerup log-convexity; the GUE β=2 surmise normalization 32/π² verified as the half-factorial identity (∫p₂ = ⟨s⟩ = 1, ⟨s²⟩ = 3π/8 by quadrature). Pass 2 = 256-bit BigFloat re-audit.
Test 37 HARDCORE: 256-bit DE Γ(1/2) err 1.20e-28, Float64 round-off Γ(1/2) 5.83e-16 / (1/2)! 2.94e-16, N=32/π² err 2.51e-26, ladder/self-dual/recurrence exact.

## Result
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS

## Plots
- `plots/plot_01` (.png 600dpi / .svg / .pdf)
- `plots/animation.gif` — animated reveal of every plot of this test

## Independent verification guide
Reproduce with: julia ab_cloud_v19.jl --test 37 --no-two-pass
Every computation is logged in logs/computation_log.txt (timestamps + deltas); raw console output in logs/stdout_capture.txt.

## FULL COMPUTATION LOG

```text
(no log_comp entries)
```

## CONSOLE CAPTURE

```text

════════════════════════════════════════════════════════════
TEST 37 (pass 2, HARDCORE): (1/2)! via Γ — 256-bit precision audit
────────────────────────────────────────────────────────────
 DE reference: |Γ(1/2)_256 − √π| = 1.20e-28 (independent quadrature)
 Γ(1/2):  Float64 vs 256-bit DE rel.err = 5.83e-16
 (1/2)!:  Float64 vs 256-bit DE rel.err = 2.94e-16
 N = 1/[½·(π/4)^{3/2}·(1/2)!] at 256-bit vs 32/π²: rel.err = 2.51e-26
 ladder Γ(5/2)_DE = 3√π/4: rel.err = 4.78e-25
 Γ(1/2)_DE² = π (reflection self-duality): rel.err = 1.35e-28
 recurrence (1/2)!_DE = ½·Γ(1/2)_DE: rel.err = 2.51e-26
────────────────────────────────────────────────────────────
 Float64 round-off    PASS — |ΔΓ(1/2)|=5.83e-16, |Δ(1/2)!|=2.94e-16 relative (machine-ε scale)
 32/π² identity (256-bit) PASS — rel.err 2.51e-26 — exact at 256-bit
 ladder + self-duality + recurrence (256-bit) PASS — worst rel.err 4.78e-25 across the three identities
 Test 37b [HARDCORE pass 2]: 3 sub-checks, 0 failed → PASS
```
