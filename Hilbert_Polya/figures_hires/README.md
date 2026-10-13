# figures_hires/ — the 600 dpi originals

<p align="center"><img src="../assets/illustrations/ill_closing_credits.png" width="600" alt="The print gallery: every data figure of the series at 600 dpi, in two languages"/></p>

<p align="center"><img src="../assets/avatars/hp_hilbert.svg" width="110" alt="Hilbert beside the print-quality gallery"/></p>

*The publication gallery of the series: every data figure, print-quality,
bilingual, and generated deterministically from the committed verdicts.*

[← Back to the main README](../README.md)

## What this folder is

This folder is the **print-quality archive** of the data figures. Each
figure is a deterministic rendering of committed numbers from `data/` and
`computations/*/data/` — regenerate the world and these images come out
identical. The v1 series defined 16 figures × two languages
(`fig01…fig16_{ru,en}.png`); the v2.0 edition extended the gallery with
`fig17…fig25`, so 25 figures now ship per language under `ru/` and `en/`.

The theme of all originals is light — the printable one. Screen versions
(160 dpi) live in the per-campaign folders, `computations/*/figures/`;
this folder is what you cite, embed in a paper, or send to a printer.

## Contents

- `ru/` and `en/` — mirror galleries of 25 PNGs each, named
  `figNN_<slug>_{ru,en}.png`.
- The v1 run `fig01…fig16`: `fig01_zid` (the identity function Z_id),
  `fig02_gamma_ladder` (Γ-ladder closures), `fig03_argument` (argument
  principle to T = 1000), `fig04_gaps` (zero/gate gaps), `fig05_gates`
  (the 52-gate family), `fig06_trace` (the trace formula), `fig07_parts`
  (components of the pipeline), `fig08_rEF` (the heat projection r_EF),
  `fig09_handles` (the handle space), `fig10_gue_ext` (the extended C5
  family against the GUE null), `fig11_coloc` (prime-flow co-location),
  `fig12_psi` (the ψ-ladder), `fig13_dynamics` (wave-packet transport),
  `fig14_ladder` (the statistics ladder), `fig15_spinor` (spinor64),
  `fig16_map` (the bridge map).
- The v2 extension `fig17…fig25`: `fig17_nonlocal` (T11), `fig18_coloc`
  (C10 phase coding), `fig19_alphathird` (T13), `fig20_band5000` (T14),
  `fig21_blind` (T15), `fig22_anomaly` (T16), `fig23_dirichlet` (T17),
  `fig24_qinfo` (T18), `fig25_map` (the v2 bridge map).

All figures are determined by the data in data/.

## How to use it

```bash
# regenerate all figures from the committed verdicts
make figures            # 16 figures × ru/en @ 600 dpi
# the v2 targets extend the gallery and add the animations
make v2-figures         # scripts/make_figures_v2.py, scripts/make_animations_v2.py
```

- For a manuscript: take the `en/` (or `ru/`) file at 600 dpi as-is; the
  light theme is designed for print.
- For a quick look on screen, prefer the 160 dpi screen versions in
  `computations/*/figures/` — same content, lighter weight.
- To trace any pixel back to a number: each figure's generating script in
  `scripts/` reads only committed verdicts, so figure ↔ verdict JSON is a
  one-hop lookup.

## Conventions

- Naming: `figNN_<slug>_<lang>.png`; `NN` is stable across regenerations,
  and v2 numbering continues the v1 sequence without renumbering it.
- Languages are exact mirrors: `fig06_trace_ru.png` and
  `fig06_trace_en.png` carry identical data, differing only in captions
  and labels.
- Theme: light (print) only in this folder; screen variants inherit the
  same style at lower resolution.
- Determinism: no randomness beyond the seeded engine — two regenerations
  produce bit-identical PNGs.

## See also

- [../README.md](../README.md) — the main README, with the headline results these figures render
- [../figures/README.md](../figures/README.md) — logo, infographics and animations
- [../computations/](../computations/) — the screen-resolution copies per campaign
- [../data/README.md](../data/README.md) — the committed verdicts every figure is built from
