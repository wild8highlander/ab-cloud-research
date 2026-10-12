# C13 · Blind families (R5, T15)

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="640" alt="Blind gate families at the shutter wall"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
*The cast before the blind trial: five families no v1 handle could have drawn, one pipeline they all must pass.*

> Five families absent from the v1 handle space: imaginary x-hoppings, golden quasiperiodic vortices, dimers, power-law hoppings, flux dithering. 20 gates, one pipeline, PC0' = 1.000.

[← Back to the main README](../../README.md)

## The question

Every v1 measurement of the H2 gap walked the same corridor: the vortex-lattice gate family, deformed along the six handles that C5 added. A sceptic could argue the null result — no gate spectrum correlates with the zeta zeros — is a property of *that* family, not of local lattices at large. C13 answers on the objection's own terms: five families designed *outside* the v1 handle space, fixed before any ranking was computed, pushed through the v1 pipeline. One of the twenty gates escaping the null zone would vindicate the objection; every gate landing in it dissolves the objection.

## Where it sits in the v2 roadmap

This campaign executes roadmap item **R5** and settles **Theorem T15** of the v2 layer "The Operator That Almost Exists". It closes the gate branch C3 → C5 → C8 → C13: the gap measured, stabilized across six handles, classified, now shown robust to blind design. With C14 it seals universality from both sides: C13 asks whether *new* designs can escape the null zone, C14 whether *old* configurations can escape the GUE attractor. Neither exit exists.

## Method in brief

The resonator lattice (L = 24) is dressed with five blind handle families:

- **BF1 — imaginary x-hoppings**: complex phases on the x-bonds, Nv = 8/16/32, W = 0.0/0.5 (six gates);
- **BF2 — golden quasiperiodic vortices**: vortex positions on the golden-ratio chain instead of the integer grid (six gates);
- **BF3 — dimers**: pairwise-coupled cells, d = 6/8, seeds s11/s12 (four gates);
- **BF4 — power-law hoppings**: long-range couplings, Nv = 16/32 (two gates);
- **BF5 — flux dithering**: the flux α perturbed by 0.01/0.02 (two gates).

Hermiticity is verified gate by gate (`herm_dev = 0.0` for all twenty). One pipeline runs over all of them: the rank correlation r_H7 against the window of 800 internal-cache zeros, calibrated by 64 random shifts and 40 GUE surrogates; mean gap ratios ⟨r⟩ and GUE z-scores; and the positive control PC0' — the isospectral twin, obliged to return r = 1.000 and doing so: the committed value is r = 0.9999999999999996.

<p align="center"><img src="../../assets/avatars/hp_agent_atlas.svg" width="110" alt="Agent Atlas"/></p>

## Results

All in the null zone: |r_H7| ≤ 0.040, min p = 0.29, GUE class intact. The H2 gap is robust to designs outside the v1 space.

The committed ledger makes the headline precise: the largest rank correlation among the twenty gates is |r_H7| = 0.0403 (`BF5_dither0.02`), the smallest p-value is 0.292, the Bonferroni floor is 5.85 — all recorded in the verdict alongside PC0' = 1.000. The cohort sits an order of magnitude below the best v1 gate (r_H7 = 0.226 in C3) and far below any identity threshold.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="110" alt="Riemann"/></p>
*Riemann holds the zero window steady: same 800 zeros, same rank metric — only the designs change.*

## Why it matters

Blind design removes the last methodological escape route from the H2 verdict. After C9/T11 localized the obstruction — the wall passes through locality, not the trace — the open question was whether "locality" meant merely *this* lattice. C13 answers: every local design the package can write down lands in the null zone. The gap is robust to blind design, which is what the roadmap demanded before it could be called a class property.

## Reproduction

```bash
python3 campaigns/run_c13_blind_families.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).
The committed run completes in 7.1 s.

## Data and figures

| File | Where |
|---|---|
| `fig21_blind.png` | 600 dpi — `figures_hires/ru|en/fig21_blind_ru|en.png`; copy in `figures/ru|en/` |
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

`data/results.json` carries the committed verdict (RU+EN), the twenty per-gate records (family, herm_dev, r_H7, shift, p-value, GUE z-score, ⟨r⟩) and the pipeline meta; `data/gates_table.csv` is the flat table behind `fig21_blind.png`.

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

The committed English verdict reads: *"Blind protocol: 20 gates from 5 new families — all in the null zone (|r_H7| ≤ 0.040, min p = 0.292, Bonferroni 5.85), all in the GUE class. The H2 gap is robust to five independent designs outside the v1 handle space."*

## FAQ

**What does "blind" mean here — were the gates chosen at random?**
No. Blind means the five families and all parameters were fixed before the pipeline ran, and the pipeline was frozen in v1; no gate was tuned or dropped after its r_H7 was seen.

**Why does the header say PC0' = 1.000 while the ledger shows 0.9999999999999996?**
The same number at different printing precision: the headline rounds to three decimals, `data/results.json` stores the full double.

**Imaginary hoppings and power-law tails are far from Hofstadter — why does nothing change?**
Because the test is not the symmetry class but the *rank correlation with the zero sequence*. The blind families do drift statistically (⟨r⟩ ≈ 0.55–0.65), yet their spectra carry no trace of the zero order.

**Does C13 prove that no Hilbert–Pólya operator exists?**
No — the package never claims otherwise. The gap survives every local design tested; with T11 the obstruction is architectural: locality itself, not any particular lattice.

## See also

- [C3 · Gate family](../C3_gate_family/README.md) — the original 52-gate measurement of the gap.
- [C5 · Gates extended](../C5_gates_extended/README.md) — six handle dimensions, |r_H7| ≤ 0.043.
- [C9 · Nonlocal trace primitive](../C9_nonlocal_trace/README.md) — the wall passes through locality, not the trace (T11).
- [C14 · Anomaly hunt](../C14_anomaly_hunt/README.md) — the companion scan inside the GUE attractor.
- `docs/v2/overview.md`, `monograph/v2_volume/`, `results/RESULTS.md` (row 27).

---
*Hilbert Polya Bridge v2.0.0 · C13*
