<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ computations/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# C13 · Blind families (R5, T15)

> **🧭 Navigation:** [computations/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="640" alt="Blind gate families at the shutter wall"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
*The cast before the blind trial: five families no v1 handle could have drawn, one pipeline they all must pass.*

> Five families absent from the v1 handle space: imaginary x-hoppings, golden quasiperiodic vortices, dimers, power-law hoppings, flux dithering. 20 gates, one pipeline, PC0' = 1.000; 17/20 in the GUE band, 3 at the edges.

[← Back to the main README](../../README.md)

## The question

Every v1 measurement of the H2 question walked the same corridor: the vortex-lattice gate family, deformed along the six handles that C5 added. A sceptic could argue the null result — no gate's rank correlation with the zeta zeros leaves the null zone — is a property of *that* family, not of local lattices at large. C13 answers on the objection's own terms: five families designed *outside* the v1 handle space, fixed before any ranking was computed, pushed through the v1 pipeline. One of the twenty gates escaping the rank branch's null zone would vindicate the objection; every gate landing in it dissolves the objection.

## Where it sits in the v2 roadmap

This campaign executes roadmap item **R5** and settles **Theorem T15** of the v2 layer "The Operator That Almost Exists". It closes the gate branch C3 → C5 → C8 → C13: the question measured, the answer stabilized across six handles, classified, now shown robust to blind design. With C14 it seals universality from both sides: C13 asks whether *new* designs can escape the rank branch's null zone, C14 whether *old* configurations can escape the GUE attractor. Neither exit exists.

## Method in brief

The resonator lattice (L = 24) is dressed with five blind handle families:

- **BF1 — imaginary x-hoppings**: complex phases on the x-bonds, Nv = 8/16/32, W = 0.0/0.5 (six gates);
- **BF2 — golden quasiperiodic vortices**: vortex positions on the golden-ratio chain instead of the integer grid (six gates);
- **BF3 — dimers**: pairwise-coupled cells, d = 6/8, seeds s11/s12 (four gates);
- **BF4 — power-law hoppings**: long-range couplings, Nv = 16/32 (two gates);
- **BF5 — flux dithering**: the flux α perturbed by 0.01/0.02 (two gates).

Hermiticity is verified gate by gate (`herm_dev = 0.0` for all twenty). One pipeline runs over all of them: the rank correlation r_H7 against the window of 800 internal-cache zeros, calibrated by 64 random shifts and 40 GUE surrogates; mean spacing ratios ⟨r⟩ with the hard GUE band (0.5996±0.03, C8 canon) and GUE z-scores; and the positive control PC0' — the isospectral twin, obliged to return r = 1.000 and doing so: the committed value is r = 0.9999999999999996.

<p align="center"><img src="../../assets/avatars/hp_agent_atlas.svg" width="110" alt="Agent Atlas"/></p>

## Results

All in the null zone of the rank branch: |r_H7| ≤ 0.040, min p = 0.29 (Bonferroni 5.85). GUE class: 17/20 inside the canonical band 0.5996±0.03, three families drift to the edges (⟨r⟩ = 0.550, 0.559, 0.649) with r_H7 z-scores within ±1 — statistically consistent with GUE, outside the hard band. The H2 result — the zeros' level — is robust to designs outside the v1 space.

The committed ledger makes the headline precise: the largest rank correlation among the twenty gates is |r_H7| = 0.0403 (`BF5_dither0.02`), the smallest p-value is 0.292, the Bonferroni floor is 5.85 — all recorded in the verdict alongside PC0' = 1.000. The cohort sits an order of magnitude below the best v1 gate (r_H7 = 0.226 in C3) and far below any identity threshold.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="110" alt="Riemann"/></p>
*Riemann holds the zero window steady: same 800 zeros, same rank metric — only the designs change.*

## Why it matters

Blind design removes the last methodological escape route from the H2 verdict. After C9/T11 localized the obstruction — the wall passes through locality, not the trace — the open question was whether "locality" meant merely *this* lattice. C13 answers: every local design the package can write down lands in the rank branch's null zone. The resolution limit is robust to blind design, which is what the roadmap demanded before it could be called a class property.

## Reproduction

```bash
python3 campaigns/run_c13_blind.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`../../data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).
The committed run completes in 7.1 s.

## Data and figures

| File | Where |
|---|---|
| `fig21_blind_{ru,en}.png` | this folder's `figures/{ru,en}/`; 600 dpi mirrors — top-level `figures_hires/{ru,en}/fig21_blind_{ru,en}.png` |
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

`data/results.json` carries the committed verdict (RU+EN), the twenty per-gate records (family, herm_dev, r_H7, shift, p-value, GUE z-score, ⟨r⟩) and the pipeline meta; `data/gates_table.csv` is the flat table behind `fig21_blind_{ru,en}.png`.

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`../../monograph/v2_volume/`) and `../../independent_verification/` (IVP11–18).

The committed English verdict reads: *"Blind protocol: 20 gates from 5 new families — all at the zeros' level — inside the GUE band (|r_H7| ≤ 0.040, min p = 0.292, Bonferroni 5.85 — the rank branch at its resolution limit); 17/20 inside the GUE band 0.5996±0.03, the rest at the edges/slightly outside (⟨r⟩ = 0.550–0.649; r_H7 z-scores all within ±1). The H2 result (the zeros' level) is robust to five independent designs outside the v1 handle space."*  *(v2.0.5: the earlier committed string said "all in the GUE class" — a hard-coded phrase that contradicted the per-gate `gue_class` flags, three of which are false; the correction is documented in the package's audit history, see `../../docs/audit_v2.0.9.md`.)*

## FAQ

**What does "blind" mean here — were the gates chosen at random?**
No. Blind means the five families and all parameters were fixed before the pipeline ran, and the pipeline was frozen in v1; no gate was tuned or dropped after its r_H7 was seen.

**Why does the header say PC0' = 1.000 while the ledger shows 0.9999999999999996?**
The same number at different printing precision: the headline rounds to three decimals, `data/results.json` stores the full double.

**Imaginary hoppings and power-law tails are far from Hofstadter — why does nothing change?**
Because the test is not the symmetry class but the *rank correlation with the zero sequence*. The blind families do drift statistically (⟨r⟩ = 0.550–0.649; three gates sit outside the hard C8 band 0.5996±0.03), yet their spectra carry no trace of the zero order.

**Does C13 prove that no Hilbert–Pólya operator exists?**
No — the package never claims otherwise. The rank limit survives every local design tested; with T11 the obstruction is architectural: locality itself, not any particular lattice.

## See also

- [C3 · Gate family](../C3_gate_family/README.md) — the original 52-gate measurement of the rank branch.
- [C5 · Gates extended](../C5_gates_extended/README.md) — the handle sweep, |r_H7| ≤ 0.097 (family Bonferroni 0.57).
- [C9 · Nonlocal trace primitive](../C9_nonlocal_trace/README.md) — the wall passes through locality, not the trace (T11).
- [C14 · Anomaly hunt](../C14_anomaly_hunt/README.md) — the companion scan inside the GUE attractor.
- `../../docs/v2/overview.md`, `../../monograph/v2_volume/`, `../../results/RESULTS.md` (row 27).

---
*Hilbert Polya Bridge v2.0.0 · C13*

---

<!-- enriched-r3 -->

This folder documents one **campaign of the Hilbert–Pólya Bridge series**. The computational kernel is shared — every campaign builds its Hamiltonians and spectra through [`engine/`](../../engine/README.md) — while the committed verdicts for all campaigns live in [`data/`](../../data/README.md). This page narrates the campaign's question, method and measured outcome; the numbers it quotes are frozen in the evidence base and are reproducible bit-for-bit. The campaign map of the whole series is in [`computations/`](../README.md).

## Folder contents

**Subfolders:** `data/` · `figures/`


**Where next:** [engine/](../../engine/README.md) · [data/](../../data/README.md)

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
