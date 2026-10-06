# AB-Cloud Dirac Laboratory — Run Report

**Run started:** 2026-10-06 08:10:31  |  **Elapsed:** 2.1 min  |  **Mode:** FULL  |  **Suite:** Dirac Lab v1.0 (Python)  |  **Seed:** 96

Suite purpose: connect the AB-cloud programme (parent repo, tests 19/29/30) to the Dirac equation — continuum limit, zero-mode index physics, Berry topology, relativistic Landau levels, real-time Dirac phenomena, and the ζ-decorated Dirac operator bridge with its chiral-protection mechanism.

## Verdict ledger

| Test | Title | Verdict | Checks |
|---|---|---|---|
| D1 | Continuum limit — the lattice IS a Dirac equation | **PASS** | 5/5 |
| D2 | Zero-mode tower & index content | **PASS** | 4/4 |
| D3 | Berry phase π of the Dirac cone | **PASS** | 4/4 |
| D4 | Relativistic Landau levels (√n ladder) | **PASS** | 5/5 |
| D5 | Klein tunneling (real time) | **PASS** | 4/4 |
| D6 | Zitterbewegung (real time) | **PASS** | 2/2 |
| D7 | ζ-decorated Dirac operator — the bridge | **PASS** | 5/5 |
| D8 | Chiral protection (AIII) — why D7 works | **PASS** | 4/4 |

**Summary: 8/8 tests PASS.**

## D1: Continuum limit — the lattice IS a Dirac equation

**Verdict: PASS**

- ✓ **D1a Bloch bands match analytic π-flux Dirac** — max|ΔE| = 2.66e-15
- ✓ **D1b E₁ ∝ 1/L with R² ≥ 0.999** — R² = 0.999891
- ✓ **D1b v_F = slope/2π ≈ 2t (±5%, finite-size; parent: 1.9447)** — v_F = 1.9347 vs 2.0
- ✓ **D1b E₁·L → 4π (±1.5%)** — E₁·L = 12.4695 vs 4π = 12.5664 — parent test 30: 12.55
- ✓ **D1c lattice tower = analytic Dirac shells** — max nearest-shell distance = 1.06e-03 over 32 levels

## D2: Zero-mode tower & index content

**Verdict: PASS**

- ✓ **D2 tower = 4 ∀L (L/4∈ℤ)** — L16:4; L20:4; L24:4; L28:4; L32:4; L40:4; L48:4
- ✓ **D2 {H,Γ} = 0 machine precision** — worst 0.0e+00
- ✓ **D2 tower pinned: max|E_zero| < 1e-9** — worst 7.81e-15
- ✓ **D2 Γ-polarity of tower = 0 (2× Γ+ , 2× Γ−)** — L16:+0; L20:+0; L24:+0; L28:+0; L32:+0; L40:+0; L48:+0

## D3: Berry phase π of the Dirac cone

**Verdict: PASS**

- ✓ **D3 Wilson loop around cone (r=0.2) → |γ| = π** — γ = +3.141592653590
- ✓ **D3 Wilson loop around cone (r=0.35) → |γ| = π** — γ = +3.141592653590
- ✓ **D3 control loop #1 (no cone inside) → γ ≡ 0 (mod 2π)** — γ = +0.00e+00
- ✓ **D3 control loop #2 (no cone inside) → γ ≡ 0 (mod 2π)** — γ = +0.00e+00

## D4: Relativistic Landau levels (√n ladder)

**Verdict: PASS**

- ✓ **D4 Dirac ladder: R²(E²∝n) ≥ 0.9998 ∀B** — B0.02:0.999987; B0.035:0.999936; B0.05:0.999846
- ✓ **D4 Dirac slope/(2B) ∈ [0.93, 1.05] ∀B (lattice-regularization deficit O(Bn), documented in monograph §6)** — B0.02:0.9755; B0.035:0.9523; B0.05:0.9330
- ✓ **D4 Schrödinger ladder: R²(E∝n) ≥ 0.9999 ∀B** — B0.02:0.999964; B0.035:0.999949; B0.05:0.999986
- ✓ **D4 discrimination: quad-fit wins for Dirac, lin-fit for Schrödinger** — B0.02: D 0.99999>0.98966, S 0.99996>0.94817; B0.035: D 0.99994>0.98903, S 0.99995>0.95016; B0.05: D 0.99985>0.98822, S 0.99999>0.94831
- ✓ **D4 lattice n=0 LL pinned at E=0** — n0 = 64 vs α′L² = 32 (×1 or ×2: valley/parity structure)

## D5: Klein tunneling (real time)

**Verdict: PASS**

- ✓ **D5 Klein supertansmission: T_Dirac(0°) ≥ 0.80 while barrier is classically forbidden (E₀ < V₀)** — T_Dirac(0°) = 0.9777
- ✓ **D5 Dirac ≫ Schrödinger at normal incidence (≥ 10×)** — T_Schr(0°) = 0.0010 (tunneling-suppressed)
- ✓ **D5 angular suppression: T_Dirac monotone ↓ within noise** — 0°:0.978; 30°:0.350; 45°:0.055; 60°:0.005
- ✓ **D5 strong suppression at 60° (T(60°) ≤ 0.6·T(0°))** — T(60°)/T(0°) = 0.005

## D6: Zitterbewegung (real time)

**Verdict: PASS**

- ✓ **D6 Zitterbewegung ω = 2E (Dirac box, ±1.5%)** — ratio = 0.999583
- ✓ **D6 torus interband dipole oscillates at ω = 2E₁ (±4%)** — ratio = 0.9998

## D7: ζ-decorated Dirac operator — the bridge

**Verdict: PASS**

- ✓ **D7 CLEAN baseline: tower = 4 ∀L (Dirac zero modes, ties D2)** — L32:4; L40:4; L48:4
- ✓ **D7 chiral skeleton survives ζ decoration: {H,Γ} = 0 ∀L** — L32:0.0e+00; L40:0.0e+00; L48:0.0e+00 (E↔−E pairing audited in D8)
- ✓ **D7 statistics move toward GUE: ⟨r⟩_ζ − ⟨r⟩_clean ≥ +0.04** — L32:+0.1321; L40:+0.0934; L48:+0.1937
- ✓ **D7 ⟨r⟩_ζ ≥ 0.56 (GUE approach, theory 0.5992)** — L32:0.6080; L40:0.6084; L48:0.6050
- ✓ **D7 Dirac low-energy scale survives (near-zero reservoir ≥ 8)** — L32:18; L40:24; L48:24

## D8: Chiral protection (AIII) — why D7 works

**Verdict: PASS**

- ✓ **D8 {H,Γ} = 0 under ζ decoration (machine precision)** — ||{H,Γ}|| = 0.00e+00
- ✓ **D8 bipartite (no same-sublattice hopping)** — max = 0.0e+00
- ✓ **D8 E ↔ −E spectral symmetry < 1e-10** — max = 4.00e-15 over 800 pairs
- ✓ **D8 zero-mode content is chiral-multiplet-consistent (even n_zero; clean tower=4 documented as index-0 fragile in D7)** — n_zero = 0 (ζ decoration splits the clean 4-tower into ±E valley pairs — chiral symmetry survives, exact pinning is a clean-limit signature)

## Reproducibility

```bash
python3 code/dirac_lab.py            # full suite (this run)
python3 code/dirac_lab.py --quick    # fast check
julia code/dirac_lab_cross.jl        # independent Julia cross-check
```

Environment: numpy 2.1.3, Python 3.11+; deterministic seed 96; all Hamiltonians built from the parent-repository conventions (Landau gauge 2πα·x on y-hops; monumental atan smooth vortex gauge on vertical bonds, factor 0.5; density-scaled vortex count round(25·L²/900)).
