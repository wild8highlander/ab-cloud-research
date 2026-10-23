# docs/v2 — the version 2.0 documents

> **🧭 Navigation:** [docs/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_spectrum_emerge.png" width="600" alt="A spectrum emerging from the lattice: the v2.0 campaigns probing the operator that almost exists"/></p>

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="110" alt="Hilbert, sponsor of the operator programme"/></p>

*The v2.0 shelf: the map of the eight new campaigns, the new primitive with
the prime weight, the blindness of the spectrum to phase coding, and the
twisted trace formula for the Dirichlet class.*

[← Back to the main README](../../README.md)

## What this folder is

This folder documents **v2.0 — "The Operator That Almost Exists"**
(Oct 12, 2026): the second edition of the series, in which eight new
campaigns (C9–C16) execute the v1 roadmap (R1–R5) and add five new
measurements, yielding eight new theorems (T11–T18). The v1 shelf one
level up (`../`) holds the five-stage map and the shared methods; this
shelf holds what changed, what was newly proven, and how the v2 metrics
differ from the v1 conventions.

The zeta zeros of v2 are an internal mpmath cache — no external data
files at all — and every claim below is grounded in the committed
verdicts of the corresponding `computations/<ID>/data/` folders.

## Contents

| Document | Contents |
|----------|----------|
| `overview.md` | the v2 map (C9–C16 ↔ T11–T18) and the metric conventions |
| `nonlocal_primitive.md` | T11: formulation, proof, measurements |
| `phase_coding.md` | T12: classification of phase systems and the gauge triviality of χ4 |
| `dirichlet_pipeline.md` | T17: derivation of the twisted trace formula (Hadamard → Q_χ → tail) |

### The v2 map at a glance

| # | Campaign | Question | Answer | Theorem |
|---|----------|----------|--------|---------|
| C9 | nonlocal trace | does an operator with the prime weight in its trace exist by construction? | **yes** — any isospectral nonlocal one; the wall is locality | T11 |
| C10 | phase coding | does the spectrum see the rigid co-location? | co-location exact (4.4e-16), the spectrum is blind | T12 |
| C11 | α=1/3 | what is the arithmetic of the zero modes? | N₀ = 2L−6·[L≡0 (mod 12)], index −2 | T13 |
| C12 | band T=5000 | does the counting machine scale? | yes: N = 4520 = N_strip | T14 |
| C13 | blind families | is the H2 result stable against new designs? | yes (20 gates, the rank branch's null zone) | T15 |
| C14 | anomalies outside GUE | is there an exit from universality? | no; the pool is structured | T16 |
| C15 | Dirichlet L | is the rank-metric resolution limit universal? | yes; the trace formula carries χ(n)Λ(n)/√n, the rank branch stays at its limit | T17 |
| C16 | the quantum layer | what do entanglement and complexity see? | an echo of locality; no arithmetic | T18 |

### The v2 metric conventions

`overview.md` also records exactly what changed against v1, and why the
change does not touch the v1 verdicts:

1. **Zero reference** — the internal mpmath cache `../../data/zeros/` (800
   zeros, bit-for-bit reproducible); there are no external data files at
   all.
2. **Windows**: unfolded-vs-unfolded (PC0′ = an isospectral twin must give
   r = 1.000; in v1 the control was the file-vs-file pair).
3. **r_EF** — on detrended fluctuations (the raw v1 correlation catches
   the common trend of two smooth curves; the wide GUE null ±0.8 is
   thereby fixed).
4. **The constant B** — corrected (ln 2π → ln 4π); the v1 verdicts did
   not depend on the shipped literal.

## How to use it

- Start with `overview.md`: it is the contract of v2 — the map, the
  conventions, and the honest diff against v1.
- For the mathematical core of v2, read `nonlocal_primitive.md` (T11) —
  the primitive whose trace carries the prime weight by construction —
  and `dirichlet_pipeline.md` (T17), the twisted trace formula derived
  end-to-end: Hadamard → Q_χ → tail, the Dirichlet analogue of the v1
  document `../trace_formula.md`.
- `phase_coding.md` (T12) is the negative-result archetype of the series:
  the co-location can be made exact (4.4e-16 for any β), and the spectrum
  simply does not see it — the gauge triviality of χ4.
- Then replay the evidence itself: the eight drivers in `campaigns/`
  (`run_c9_nonlocal.py` … `run_c16_qinfo.py`) and the explorer's
  "Verdicts C9–C16" tab.

## Conventions

- Documents here follow the v2 naming: campaigns C9–C16, theorems
  T11–T18; figure numbering continues the v1 sequence (`fig17…fig25` in
  `figures_hires/`).
- Every number quoted in these documents is committed under
  `computations/<ID>/data/`; the documents cite, they do not replace.
- The v2 self-containment rule (no external data files) is absolute:
  any script that named the Odlyzko file in v1 now uses the internal
  cache.

## See also

- [../../README.md](../../README.md) — the main README with the v2 verdict table
- [../README.md](../README.md) — the v1 documentation shelf (theory, methods, trace_formula, validation)
- [../trace_formula.md](../trace_formula.md) — the v1 trace formula that T17 generalizes to the Dirichlet class
- [../../computations/](../../computations/) — the committed v2 verdicts C9–C16
- [../../campaigns/README.md](../../campaigns/README.md) — the v2 drivers run_c9…run_c16

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The version 2.0 documents: the second-generation theory and protocol texts that the v2 campaigns (C9–C16) follow.
