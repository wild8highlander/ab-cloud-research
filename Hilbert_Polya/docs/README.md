# docs/ — the documentation of the series

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_critical_line.png" width="600" alt="The critical line as a spine running through the five stages of the Bridge"/></p>

<p align="center"><img src="../assets/avatars/hp_riemann.svg" width="110" alt="Riemann, guardian of the zeta zeros"/></p>

*Four compact documents carry the whole conceptual apparatus: the map, the
methods, the one fully derived theorem, and the registry of thresholds.*

[← Back to the main README](../README.md)

## What this folder is

This folder is the **theory and methods shelf** of the package. Where the
per-campaign folders in `computations/*/` tell the experimental story and
the monographs give the full-length treatment, the four documents here are
the reference layer a newcomer reads first and returns to constantly:

- the five-stage map that organizes everything (algebra → graph → counting
  → operator → trace);
- the unified measurement protocols shared by all campaigns;
- the complete derivation of the trace-formula theorem T6, the analytical
  centerpiece;
- the registry of thresholds and machine floors that turns raw numbers
  into verdicts.

## Contents

| Document | Contents |
|----------|------------|
| [theory.md](theory.md) | five-stage map, resonator, logic of the HP scorecard |
| [methods.md](methods.md) | pipelines: sweeps, statistics, sieves, trace |
| [trace_formula.md](trace_formula.md) | full derivation of Theorem T6 (Hadamard → Q(a) → sine transform) |
| [validation.md](validation.md) | thresholds, machine floors, registry of controls |
| [audit_v2.0.9.md](audit_v2.0.9.md) | the v2.0.9 audit: verdict-propagation completeness across the remaining runs (C7/C9/C11/C13/C15/C16, generators, explorer, the audit report, Th1/V07 of AB_Cloud_Quantum_Research) plus three real defects (V07 gap_orders formula, the C13 runner name, «16 gates» in fig25_map). This is the consolidated audit record — the earlier notes `metric_correction_v2.0.1.md` and `audit_v2.0.5.md`–`audit_v2.0.8.md` were retired in its favour |

Monographs (full, RU/EN, DOCX+PDF): monograph/ and computations/*/.

### What each document gives you

- **theory.md** defines the route of the series as five stations with the
  distance between neighbours measured at every joint: stage 1, algebra —
  the Γ-ladder with three closures (T1, dps = 40, residuals ~1e-39, plus
  one honest refutation); stage 2, graph — the identity function
  Z_id(t) = e^{iθ(t)}ζ(½+it) (T2, reality on the line); stage 3, counting
  — the argument principle (T3, pole calibration, RH verified in the strip
  up to T = 1000); stage 4, operator — the 87 lattice gates, where the gap
  H2 is measured at the surrogate-null level; stage 5, trace — Tr e^{−xH} against the
  explicit formula, with T6 proven for H_ξ and the gap ≈ 1 order in the
  heat metric. It also fixes the resonator construction (L×L lattice,
  protocol 24×24, hopping −t·e^{iφ}, flux 2πα·iy, vortex phases, disorder
  W) and the discipline of separating "dynamics on the line ½" (measured)
  from "line ½ = critical line" (conjecture).
- **methods.md** is the shared laboratory manual: the spectral gate
  pipeline (vortex configuration with seed 96 → `build_hamiltonian` →
  `eigvalsh`, driver evr → central band of 344 levels → polynomial
  unfolding, degree 6 → 3 → a window of exactly 200 levels with offset
  10), the zero-side sweep by the Riemann–von Mangoldt count
  N̄(γ) = γ/2π·ln(γ/2πe) + 5/8, the three statistics (r_H7, D_nn, KS),
  the prime sieve and the heat-trace pipeline, and the bit-exact base
  control: Nv = 0, W = 0.5, α = 0.5 reproduces the C3 `mean_spacing` CSV
  with |Δ| = 1.45e-16.
- **trace_formula.md** derives Theorem T6 end-to-end for the operator
  H_ξ = diag(±γ_n) used by campaign C4: the Hadamard product of ξ(s), the
  constant B = −0.023095708966…, the identity Q(a) and the sine transform
  that carries the Λ(n)/√n prime weight. All constants are derived, none
  fitted; verification: |ΔQ| ≤ 1.7e-12 (M0), |ΔK| ≤ 1.2e-5 (M1).
- **validation.md** is the referee's sheet: the threshold registry (for
  example Γ-closures 1e-30 against measured 1.3–2.6e-39; reality of Z_id
  1e-25 against 4.9e-29; the trace formula 5e-5 absolute against 1.2e-5;
  co-location 1e-13 against 1.35e-14; the ψ-ladder corr ≥ 0.95 against
  0.972; C3 reproduction 1e-10 against 1.45e-16) and the machine floors —
  the documented points where a metric goes blind and an absolute
  criterion must replace a relative one.

## How to use it

Read in this order as a newcomer:

```bash
# 1. the map, then the methods, then the theorem, then the thresholds
less docs/theory.md docs/methods.md docs/trace_formula.md docs/validation.md
```

- Before running anything: `theory.md` + `methods.md` tell you what every
  campaign measures and why the numbers mean what they claim.
- When reading a campaign folder (`computations/C1…C8`): keep
  `validation.md` open — every PASS/FAIL there is adjudicated by these
  thresholds.
- When studying the trace result (C4, T6): `trace_formula.md` is the
  self-contained derivation; the campaign README only reports the
  verification numbers.
- For the v2.0 additions (C9–C16, T11–T18), continue to
  [docs/v2/overview.md](v2/overview.md); the `v2/` folder also carries the
  theorem-level companions [v2/nonlocal_primitive.md](v2/nonlocal_primitive.md)
  (T11, the nonlocal trace primitive of C9),
  [v2/phase_coding.md](v2/phase_coding.md) (T12, classification of phase
  systems with co-location, C10) and
  [v2/dirichlet_pipeline.md](v2/dirichlet_pipeline.md) (T17, the twisted
  trace formula for L-functions, C15).

## Conventions

- The documents are bilingual in origin (RU with EN terminology); the
  monograph volumes in `monograph/` and `computations/*/` are the full
  RU/EN, DOCX+PDF renderings of the same content.
- Thresholds are always quoted as *threshold vs measured value*; the
  living ledger of actual numbers is `results/RESULTS.md`.
- Nothing here is a substitute for the monographs — `theory.md` itself
  states it is a map, not a replacement.

## See also

- [../README.md](../README.md) — the main README with the verdict table H1–H5
- [v2/overview.md](v2/overview.md) — the v2.0 map (C9–C16 ↔ T11–T18)
- [../results/](../results/) — RESULTS.md, the living ledger of numbers
- [../computations/](../computations/) — the per-campaign evidence these documents summarize
- [../monograph/](../monograph/) — the full theorem and appendix volumes

---

<!-- enriched-r3 -->

This folder is the **documentation shelf** of its module: the Markdown documents that explain theory, methods and protocol beyond what the READMEs carry. The documents are committed sources — rendered versions, where they exist, are generated from these files. Start with the module README for orientation, then read the documents in the order suggested there.

The documentation of the series: theory, methods and protocol documents in Markdown, referenced throughout the campaign and monograph layers.

**Subfolders:** `v2/`
