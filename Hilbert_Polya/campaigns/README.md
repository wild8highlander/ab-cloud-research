# campaigns/ — the verdict excursions

<p align="center"><img src="../assets/illustrations/ill_shutter_wall.png" width="600" alt="A wall of lattice shutters, one gate per campaign of the Bridge series"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>

*The excursion layer of the series: from the Γ-ladder of C1 to the qinfo
layer of C16, every committed verdict can be replayed in seconds — the
shutters are already built, the zeros already counted.*

[← Back to the main README](../README.md)

## What this folder is

This folder holds the **driver layer** of the Hilbert–Pólya Bridge: one thin,
self-contained Python script per campaign. The v1 core is *eight scripts
`run_c1…run_c8`*: they print the verdict from the committed data and
recompute the cheap invariants — in seconds, with no zero file needed. The
v2.0 edition added the drivers `run_c9…run_c16`, so the complete roster
C1–C16 now lives here, one script per campaign.

Each script serves two purposes:

1. **Excursion mode (default).** It reads the committed verdict from
   `data/` (v1) or from its own `computations/<ID>/data/` folder (v2) and
   prints the verdict — the campaign's answer, its positive controls, and
   its headline numbers. Nothing is recomputed that is not cheap; a
   newcomer replays the entire evidence base of the study without any
   external data file.
2. **Fresh recomputation (optional).** The expensive parts of the v1
   campaigns need the ζ zero file, whose path is set by `ZFILE` in the
   scripts; the committed verdicts themselves never depend on it.

In the five-stage map of the series (algebra → graph → counting → operator
→ trace) these scripts are the measurement end-points: C1 stands on the
algebra and graph stages (the Γ-ladder and the identity function Z_id),
C2 is the counting stage (the argument principle to T = 1000), C3–C5 and
C8 are the operator stage (the gate family, its extended handles, and the
statistics ladder), C4 and C6–C7 close the operator and trace stages (the
Guinand–Weil trace formula, the prime-flow co-location, the wave-packet
transport), and the v2 scripts C9–C16 execute the v2 roadmap that produces
theorems T11–T18.

## Contents

| Script | Campaign | Stage and subject |
|--------|----------|-------------------|
| `run_c1_identity.py` | C1 | algebra + graph: Γ-ladder closures K1–K7, reality of Z_id, zeros, Gram |
| `run_c2_argument.py` | C2 | counting: argument principle to T = 1000, anchors 0/3/10/29/79/649, S(T), gaps, bridge |
| `run_c3_gates.py` | C3 | operator: 52 gates, zeros, PC1/PC2 |
| `run_c4_trace_formula.py` | C4 | trace: M0/M1/M2, PC0, the trace-metric gap |
| `run_c5_gates_ext.py` | C5 | operator: 35+2 extended gates, six new handles |
| `run_c6_primes.py` | C6 | primes: co-location, kernel δ(d), ψ-ladder, codings |
| `run_c7_dynamics.py` | C7 | dynamics: trajectories ⟨x⟩(t), transport |
| `run_c8_stats_ladder.py` | C8 | statistics: ladder of 11 channels, spinor64 |
| `run_c9_nonlocal.py` | C9 | v2 · T11 — nonlocal trace |
| `run_c10_phase_coded.py` | C10 | v2 · T12 — phase coding |
| `run_c11_alphathird.py` | C11 | v2 · T13 — α = 1/3 zero modes |
| `run_c12_band5000.py` | C12 | v2 · T14 — band T = 5000 |
| `run_c13_blind.py` | C13 | v2 · T15 — blind families |
| `run_c14_anomaly.py` | C14 | v2 · T16 — anomaly hunt |
| `run_c15_dirichlet.py` | C15 | v2 · T17 — Dirichlet L |
| `run_c16_qinfo.py` | C16 | v2 · T18 — qinfo layer |
| `run_c17_blind_phaseB.py` | C17 | v3 · N7 фаза B — слепой прогон на замкнутой плотности явной формулы (простые + θ → J → канва Q22 → хеш → нули как предсказание) |

## How to use it

The one-minute tour over all committed v1 verdicts (no zero file needed):

```bash
make tour
```

or any single excursion directly:

```bash
python3 campaigns/run_c1_identity.py
python3 campaigns/run_c2_argument.py
python3 campaigns/run_c3_gates.py
python3 campaigns/run_c4_trace_formula.py
python3 campaigns/run_c5_gates_ext.py
python3 campaigns/run_c6_primes.py
python3 campaigns/run_c7_dynamics.py
python3 campaigns/run_c8_stats_ladder.py
```

The v2 drivers are run individually (they are self-sufficient — no external
data file at all):

```bash
python3 campaigns/run_c9_nonlocal.py
python3 campaigns/run_c10_phase_coded.py
python3 campaigns/run_c11_alphathird.py
python3 campaigns/run_c12_band5000.py --segment 0 1000 computations/C12_band_5000/data/seg_1.npz
python3 campaigns/run_c12_band5000.py --assemble
python3 campaigns/run_c13_blind.py
python3 campaigns/run_c14_anomaly.py
python3 campaigns/run_c15_dirichlet.py
python3 campaigns/run_c16_qinfo.py
```

Fresh recomputation of the v1 campaigns is by choice and requires the zero
file: set its path as `ZFILE` in the campaign scripts.

## Conventions

- One script = one campaign = one headline verdict; every number a script
  prints is either read from committed JSON or recomputed bit-for-bit from
  seeded routines (the seed discipline lives in `engine/hamiltonian.py`).
- Excursion mode is offline and deterministic: identical runs print
  identical verdicts on any machine.
- The v1 verdict JSONs are committed in `data/`; the v2 verdicts live in
  their per-campaign folders under `computations/<ID>/data/`.
- Scripts are written to be read: each is a compact, linear protocol — the
  executable form of the corresponding chapter in `computations/<ID>/`.

## See also

- [../README.md](../README.md) — the main map of the package
- [../data/README.md](../data/README.md) — the committed verdicts these scripts print
- [../engine/README.md](../engine/README.md) — the resonator kernel the recomputations call
- [../computations/](../computations/) — one folder per campaign: READMEs, monographs, figures, data
- [../docs/README.md](../docs/README.md) — theory, methods, trace formula, validation
