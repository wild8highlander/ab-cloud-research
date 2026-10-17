# TS1 · The phase cycle theorem

**Status:** proved (analytically) · **Certificate:** campaign ES1, verdict
PASS · **Documents:** `theorem_ts1_{ru,en}.{pdf,docx}` (4 documents with
the embedded tiled figure) · **Figure:** `figures/ts1_4dim_{lang}.png`
(2×2 "4 dimensions", 600 dpi).

## Statement

Let θ = π/k, k ∈ ℕ, and R: φ ↦ (φ + θ) mod 2π — the rotation of the circle
S¹, executed by the machine once per real-time step. Then:

1. the orbit of any point of the state lattice G_θ = {0, θ, 2θ, …} closes
   exactly after **N = 2k** steps (π/2 → 4, π/3 → 6, π/7 → 14);
2. the minimal angular gap between distinct states equals
   **2π/N = π/k** — that is, the phase step itself;
3. the lattice is uniform: the states divide the circle into N equal arcs.

Corollary: the capacity is log₂N bits per cycle (2.00 / 2.585 / 3.807
bits/step for the three models), while the step and the memory remain O(1).

## Derivation idea

The closure is a direct consequence of arithmetic: N·θ = 2k·(π/k) = 2π ≡ 0
(mod 2π). Minimality — if m·θ ≡ 0 (mod 2π), then m = 2kj ≥ 2k, so no
smaller period exists. The gap — neighboring lattice points differ by
exactly θ, and any other distance between states is a multiple of θ;
uniformity — the points {2πi/N} are the roots of unity. The full proof is
in the documents (the "Statement" section).

## The four dimensions of the certificate (ES1)

| Dimension | What is measured | Result |
|-----------|--------------|------|
| metric | the empirical minimal period of the state sequence | 4 / 6 / 14 = 2k exactly |
| per-instance behaviour | the series θ = π/k, k = 2…16 | N = 2k for all k |
| control | the uniformity of the lattice, the minimal gap | ≤ 8.9e-16 rad; gap = 2π/N (±1e-9) |
| threshold | the pre-registered tolerances C1–C4 | all PASS |

## Boundaries (honest)

The theorem certifies the closure of **the phase lattices of the chosen
models**. It states nothing about the physical realization of spinor
phases, about coherent carriers, about noise (that is ES5) and is not
connected to the Riemann hypothesis. The trade-off "capacity log₂N vs
robustness 1/k" is a property of the model, not an implementation defect.

## How to reproduce

```bash
python3 experiments/run_es1_cycles.py      # verdict data/es1_cycles_verdict.json
python3 make_figures.py                    # figures figures/{ru,en}/ts1_4dim_*.png
python3 make_theorem_docs.py TS1           # 4 documents
python3 -m pytest tests/ -q                # TS1 invariants
```
