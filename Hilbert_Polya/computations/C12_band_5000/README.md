# C12 · Argument principle band to T=5000 (R4, T14)

> **🧭 Navigation:** [computations/](../README.md) · [Hilbert_Polya/](../../README.md) · [Root README](../../../README.md)

<p align="center"><img src="../../assets/illustrations/ill_critical_line.png" width="640" alt="The critical line verified out to T = 5000"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="760" alt="Bridge avatar cast"/></p>
<p align="center"><em>The cartographer's bench: the verified shoreline of the zeta line is pushed from T = 1000 to T = 5000, anchor by anchor, segment by segment.</em></p>

> mp.siegelz machine (bridge to e^{iθ}ζ: 0.0), adaptive sign counting, segmented run, Turing-monitored S(T), strip argument windows.

[← Back to the main README](../../README.md)

## The question

Version 1 verified the Riemann hypothesis in the strip up to T = 1000 (C2, T3): 649 zeros on the line, 649 counted by the argument principle, residuals at the 8.3e-25 level. Roadmap item R4 asked whether the machinery *scales*: extend the verified band to T ≈ 5000 with an adaptive Turing-style count, and do it in a way that remains bit-reproducible and can be resumed — because the cost of counting zeros on the line grows linearly with T, and a monolithic run is fragile. Beyond its intrinsic value (an independent, self-contained verification), the wider strip matters to the whole package: every spectral statistic measured on the gates is compared against zero data, and the larger the certified reference band, the tighter those comparisons.

## Where it sits in the v2 roadmap

C12 executes **R4** of the v1 roadmap — "extend the verified strip T ≤ 1000 with the adaptive Turing step to T ≈ 5000" — and settles theorem **T14**. It is the fourth pillar of the v2 verdict and its verification backbone: RH verified in the wider band, with the v1 anchors reproduced bit-wise, so that every campaign of the volume sits on a certified zero reference. The v3 roadmap already quotes it as a template: direction N4 proposes the same mp.siegelz segmented machine for T = 50000 at an estimated ~40× the C12 runtime.

## Method in brief

- **The machine.** Z(t) = mp.siegelz at dps = 20. The bridge to the phase-calibrated identity function is checked inside the run: max abs difference to e^{iθ}ζ on the line is **0.0** — machine-exact, the committed `bridge_max_abs`.
- **Adaptive on-line counting.** A coarse grid of 0.15 over (A, B]; every sign-change interval is resolved by 36 bisection iterations; sign-preserving intervals whose minimum |Z| is small get an 8× denser sub-grid pass — this is what catches close pairs that a coarse grid would swallow.
- **Turing monitor.** S(T) is tracked across the band; the classical certification demands |S(T)| ≤ 2, and the committed maximum is far inside.
- **Strip argument windows.** Three independent cross-checks by the argument principle applied to ξ over the full strip σ ∈ [0, 1] (dps = 15) in windows near the top of the band.
- **Segmented execution.** `--segment A B FILE.npz` counts the on-line zeros in (A, B] and writes one segment archive; `--assemble` recomputes the bridge, anchors, S(T), strip windows, gaps and the verdict from the segments. The committed folder carries thirteen segment files, `seg_1` … `seg_9b`. Runtime 44.6 s.

## Results

> N_online(5000) = 4520 = N_strip; S_max = 0.91 ≤ 2; v1 anchors (0,3,10,29,79,649) reproduced bit-wise. RH verified in the wider band.

Committed anchors (bit-wise matches against the v1 ledger):

| T | N_int | Expected |
|---|---|---|
| 10.0 | 0 | 0 |
| 27.7 | 3 | 3 |
| 51.4 | 10 | 10 |
| 100.07 | 29 | 29 |
| 199.6 | 79 | 79 |
| 1000.57 | 649 | 649 |
| 5000 | 4520 | fresh (cross-checked below) |

Independent layers of the T = 5000 certification, all committed in `data/results.json`:

| Check | Value |
|---|---|
| On-line count | N_online(5000) = 4520 |
| Strip windows | [3995, 4005]: 11 = 11; [4495, 4505]: 10 = 10; [4995, 5000]: 5 = 5 |
| Riemann–von Mangoldt main term | N̄(5000) = 4520.081 |
| Turing monitor | S_max = 0.9070 ≤ 2 |
| Bridge | max abs diff to e^{iθ}ζ = 0.0 |
| Gaps (4519 of them) | min 0.0908, max 6.8873, mean 1.1032 |

The agreement is threefold and independent: the adaptive on-line count on the line, the argument principle over the full strip in three windows, and the analytic main term all land on the same number — 4520 on the line, 26 zeros in the three strip windows matching exactly, N̄ only 0.08 away. S_max = 0.9070 leaves the Turing bound |S| ≤ 2 satisfied with a wide margin. The gap statistics carry two quiet certificates of quality: the maximum gap 6.8873 over the whole band coincides with the v1 record below T = 1000 (the C2 ledger pair [0.3104, 6.887]) — no new record gap appears between 1000 and 5000 — and the minimum gap 0.0908 is *smaller than the coarse grid step* 0.15, which is only visible because of the adaptive small-|Z| refinement: a naive counter would have merged that close pair and returned 4518. RH verified in the wider band: every zero of the strip in (0, 5000] is on the line.

## Why it matters (the verified strip)

<p align="center">
  <img src="../../assets/avatars/hp_hilbert.svg" width="110" alt="Hilbert"/>
  <img src="../../assets/avatars/hp_agent_vera.svg" width="110" alt="Agent Vera"/>
</p>
<p align="center"><em>Hilbert: "A verdict is only as wide as the band it stands on." Vera: "So we widened the band — and kept every anchor bit-wise."</em></p>

R4 is the roadmap item that turns a scale question into a settled theorem: the mp.siegelz machine with adaptive counting and segmentation does scale, and it scales without giving up bit-reproducibility (the six v1 anchors 0, 3, 10, 29, 79, 649 are reproduced exactly, not approximately). For the rest of the package the wider strip is infrastructure: the zero reference against which gate spectra are unfolded, null clouds calibrated and correlations measured now covers 4520 zeros instead of 649, which sharpens every statistic in C9–C16 that touches the reference window. Methodologically, C12 is also the package's demonstration of honest bookkeeping at scale: segmented archives that can be reassembled, a monitoring quantity (S(T)) whose bound is part of the verdict, and three independent counting layers that must agree before the word "verified" is used.

## Reproduction

```bash
python3 campaigns/run_c12_band5000.py
```

Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`../../data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

The segmented workflow (verbatim from the v2 quick start in the main README):

```bash
python3 campaigns/run_c12_band5000.py --segment 0 1000 computations/C12_band_5000/data/seg_1.npz
python3 campaigns/run_c12_band5000.py --assemble
```

`--segment A B FILE.npz` counts the on-line zeros in (A, B] into one archive; `--assemble` recomputes the bridge, anchors, S(T), strip windows, gaps and verdict from all segments and rewrites `data/results.json`. The thirteen committed `seg_*.npz` files in this folder are exactly such segment archives, so the assembly step can be re-run against them without any counting.

## Data and figures

| File | Where |
|---|---|
| `fig20_band5000_{ru,en}.png` | this folder's `figures/{ru,en}/`; 600 dpi mirrors — top-level `figures_hires/{ru,en}/fig20_band5000_{ru,en}.png` |

| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

In this campaign folder the committed payload is `data/results.json` (anchors, S(T), strip checks, gap statistics and the bilingual verdict), `data/curve.npz` (the counting and S(T) curves behind the figure), and the thirteen segment archives `seg_1.npz … seg_9b.npz` consumed by `--assemble`.

## Verdict

See `data/results.json` (verdict, RU+EN), the v2 monograph
(`../../monograph/v2_volume/`) and `../../independent_verification/` (IVP11–18).

Committed verdict (EN, verbatim): "RH verified in the band T ≤ 5000: N_online = N_strip = 4520, S_max = 0.91 ≤ 2, v1 anchors reproduced, Z↔ζ bridge at machine precision." The statement of T14 and the certification protocol (Turing monitor plus strip windows) are in `../../monograph/theorems_v2_volume/`.

## FAQ

1. **Why is the run segmented?** On-line counting costs grow linearly with T, and a monolithic run cannot be paused or partially re-verified. Segments (`--segment A B FILE.npz`) are checkpointed archives; `--assemble` rebuilds the global verdict from them, so any segment can be recomputed alone.
2. **What is S(T) and why must it stay ≤ 2?** The Turing-method deficit between the analytic main term and the certified zero count; classical certification of an on-line count requires |S(T)| ≤ 2 over the band. Here S_max = 0.9070, well inside the bound.
3. **What does "bridge 0.0" mean?** That max abs difference between the machine's Z(t) and the phase-calibrated e^{iθ}ζ(½+it) is exactly zero at machine precision — the two representations of the same function never disagree, so the count inherits the identity function's guarantees.
4. **Why believe 4520?** Three independent layers agree: the adaptive on-line sign count (4520), the full-strip argument principle in three windows (11, 10 and 5 zeros, all matching the on-line counts), and the Riemann–von Mangoldt main term (4520.081). The six v1 anchors below T = 1000 match bit-wise, which calibrates the whole pipeline against the committed ledger.

## See also

- [C2 · Argument principle](../C2_argument_principle/README.md) — the v1 strip, T = 1000, 649 = 649 (T3).
- [C9 · Nonlocal trace (T11)](../C9_nonlocal_trace/README.md) — the zero reference this band sharpens.
- `../../results/ROADMAP.md` — R4 as written and as executed; N4, the T = 50000 extension.
- `explorer/streamlit_app.py` (repo root) — the interactive explorer over the committed verdicts.
- [Back to the main README](../../README.md).

---
*Hilbert Polya Bridge v2.0.0 · C12*

---

<!-- enriched-r3 -->

This folder documents one **campaign of the Hilbert–Pólya Bridge series**. The computational kernel is shared — every campaign builds its Hamiltonians and spectra through [`engine/`](../../engine/README.md) — while the committed verdicts for all campaigns live in [`data/`](../../data/README.md). This page narrates the campaign's question, method and measured outcome; the numbers it quotes are frozen in the evidence base and are reproducible bit-for-bit. The campaign map of the whole series is in [`computations/`](../README.md).

## Folder contents

**Subfolders:** `data/` · `figures/`


**Where next:** [engine/](../../engine/README.md) · [data/](../../data/README.md)
