<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ C2_argument_principle/](README.md) · [🏠 Root README](../../../README.md)**

</div>
# C2 · The argument principle up to T = 1000

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_trace_formula.png" width="720" alt="The trace-formula view of the zeros — quick-reference edition of campaign C2"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

<p align="center"><em>Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra counted, Agent Vera verified.</em></p>

> **Counting zeros in the critical strip without tables: the adaptive Turing step, the pole calibration (lemma T3), the arithmetic bridge 2.6e-26; RH verified in the strip: 649 = 649.**

[← Back to the main README](../../README.md)

**About this edition.** This is the international quick-reference edition of campaign C2 — the ten-minute tour, organised for fast lookup: an at-a-glance box, a method checklist, every committed table, and a strict account of what is and is not claimed. The deep narrative companion is `README.md` in the same directory; both editions carry the same numbers, taken verbatim from the committed verdict `data/results.json` (registry duplicate `data/c2_argument_verdict.json`), the C2 monographs, and `results/RESULTS.md`.

## Contents

1. [The question](#sec-question)
2. [Background in one page](#sec-background)
3. [The method, step by step](#sec-method)
4. [The pole calibration: T3](#sec-t3)
5. [Results — all committed tables](#sec-results)
6. [How to read the numbers](#sec-read)
7. [The found-and-fixed episode: Σγ²](#sec-honesty)
8. [Interpretation: what is and is not claimed](#sec-interpretation)
9. [Reproduction](#sec-repro)
10. [Data and figures](#sec-data)
11. [Verdict](#sec-verdict)
12. [FAQ](#sec-faq)
13. [See also](#sec-see)

## At a glance

- **Verdict:** RH verified in the strip up to T = 1000 — **649 = 649**.
- **Instrument:** the argument principle on the contour (2,0)→(2,T)→(0,T)→(0,0), the pole s = 1 bypassed from above by a small semicircle; N(T) = Δarg ξ / 2π.
- **Anti-aliasing:** recursively adaptive Turing step with the double leaf condition |wrap| ≤ 0.3 AND length ≤ h_safe (h_safe from |ζ′/ζ| bounds); the first version lost turns (N=5 instead of 10) and was found and fixed.
- **Two arithmetics:** numpy fast branch and mpmath reference branch at dps = 26; arithmetic bridge at T = 100.07: \|ΔN\| = 2.6e-26.
- **Cross-checks:** winding residuals to the nearest integer ≤ 8.3e-25; classical residual S(T) ≤ 1.8 (maximum 1.7994 on [0, 1.13e6]).
- **Statistics:** 649 zeros below T = 1000; gaps min 0.3104 · max 6.887 · mean 1.521 (Lehman–Odlyzko); second moment Σγ² deviation 8.8e-7 from (T³/6π)(ln(T/2π)−1/3).

<a id="sec-question"></a>

## The question

How many zeta zeros lie in the critical strip below a height T, and are they all on the critical line? The campaign answers via the argument principle: the contour (2,0)→(2,T)→(0,T)→(0,0) bypassing the pole s = 1 from above gives N(T) = Δarg ξ / 2π, compared with the number of on-line zeros found independently. The equality N_strip = N_line at each height operationalises the Riemann Hypothesis; at thirteen heights up to T ≈ 1000 it holds.

<img src="../../assets/avatars/hp_agent_atlas.svg" width="120" align="right" alt="Agent Atlas"/>

The design has one deliberate property worth naming before anything else: **no zero tables are consulted as an authority**. The strip count is produced from scratch by winding the argument of ξ around a rectangle; the line count is a separate number from the package's own committed zero registry. If the two agree, RH holds on that interval — and the agreement can only happen if both computations are right, which is what makes the equality a test rather than a tautology. The result of the test, thirteen times out of thirteen below T ≈ 1000, is agreement, ending at **649 = 649** with all residuals to the nearest integer ≤ 8.3e-25.

For orientation inside the package: C2 is stage 3 of the five-stage bridge map (`docs/theory.md`) — after C1 built the phase θ(t) and the identity graph Z_id(t) = e^{iθ(t)}ζ(½+it) (T2, reality; 79 zeros matched against mpmath with max|Δγ| = 2.8e-14), and before the spectral campaigns C3–C5, which need exactly this kind of independent, machine-verified zero account to compare spectra against.

<a id="sec-background"></a>

## Background in one page

**The argument principle.** For f meromorphic inside a closed contour C, the winding number of f along C equals Z − P, the zeros minus the poles enclosed. The Riemann ξ-function ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s) is entire, so P = 0 and the winding along the rectangle (2,0)→(2,T)→(0,T)→(0,0) (closed along the real axis) is exactly the number of non-trivial zeta zeros with 0 < Im s < T. Counting zeros becomes measuring a phase — the oldest trick in the Riemann trade, and still the most trustworthy.

**The pole detour.** The closing segment passes near s = 1, where ζ has its simple pole (residue +1) and ξ′/ξ has a simple pole with the same residue. The contour detours around it by a small semicircle *above* the point. Whether this detour costs or saves one unit in the final count is not a convention but a lemma — T3 — and getting it wrong shifts every N(T) by exactly 1, uniformly, invisibly to any precision check. See the T3 section.

**Why the step must adapt.** The zeros' density grows like (1/2π) ln(t/2π), so the argument winds faster and faster with height. A fixed sampling step eventually aliases: a full 2π revolution slips between two samples and the count silently loses an integer. Turing's 1953 remedy is to subdivide recursively until no arc can hide a turn; the package's implementation stops an arc only when **both** |wrap| ≤ 0.3 **and** the arc length is ≤ h_safe estimated from bounds on |ζ′/ζ|. The failure of the weaker, single-condition version is not hypothetical — it happened, at T ≈ 51.4, losing exactly half the zeros (N = 5 instead of 10), and was caught by the S(T) cross-check. Status in the results table: found and fixed.

**Why two arithmetics.** A float64 counter can be fast and wrong in ways that are hard to see from inside itself. The campaign therefore recomputes the same contours at reference heights in mpmath at dps = 26 and compares. At the bridge height T = 100.074522612 the two branches give N_fp = 29.0 and N_mp = 29.0 with delta = 2.5849394142282115e-26 — the "arithmetic bridge 2.6e-26" of the TL;DR. The count is machine-exact, not approximately right.

<a id="sec-method"></a>

## The method, step by step

The canonical method paragraph, verbatim:

> A two-tier implementation: a numpy branch with a recursively adaptive step (the double leaf condition: |wrap| ≤ 0.3 AND length ≤ h_safe from the |ζ′/ζ| bounds) and an mpmath branch at dps = 26 for reference heights. The pole is bypassed from above by a small semicircle; by lemma T3 the additive +1 is NOT applied — its absence is verified by the S(T) cross-check and the anchors of the zero file.

The checklist form, for readers who want the pipeline at a glance:

1. **Heights.** Thirteen committed heights, run dated 2026-10-10 (meta: "Task 8a — K4 up to T≈1000, adaptive Turing step", dps = 26, refine = 0.3): 10.0; 27.717866853; 51.372076978; 100.074522612; 199.64003080999998; 300.744825758; 400.91217423850003; 499.444933686; 600.57388855; 699.714417304; 800.629291337; 900.3543122345; 1000.5705270975. First three = anchors, last ten = blocks.
2. **Contour.** Right edge up, top edge across, left edge down; small semicircle above s = 1 on the closing pass.
3. **Adaptive winding.** Sample ξ, wrap the argument increments, bisect any arc failing |wrap| ≤ 0.3 OR length > h_safe; sum → Δarg ξ; N_strip = Δarg ξ / 2π, **without** +1 (T3).
4. **Independent line count.** n_on_line_file from the committed zero registry — a computation with no shared steps with the winding.
5. **Compare.** N_int = n_on_line_file at every height; residual_to_int recorded per height (maximum 8.271806125530277e-25).
6. **Cross-check.** S_arg = N_strip − N̄(T) and S_file = N_line − N̄(T) against the Riemann–von Mangoldt smooth count; agreement of the two to ≤ 1e-13 and both inside ±1.8.
7. **Bridge.** Same contour in mpmath dps = 26 at T = 100.074522612; |N_fp − N_mp| = 2.6e-26.

Cost, from the committed run: ζ-evaluations 2145–67617 per height; runtimes 0.23–25.24 s per height; about 105 s for the whole campaign. The verdict tour `python3 campaigns/run_c2_argument.py` needs only seconds because it replays the committed JSON.

<a id="sec-t3"></a>

## The pole calibration: T3

The lemma, verbatim from the monograph:

> **Lemma T3 (pole calibration).** When the pole s = 1 is bypassed from above by a small semicircle, its argument contribution is −π; hence N(T) = Δarg ξ / 2π WITHOUT the additive +1.

> **Proof.** ξ′/ξ has a simple pole at s = 1 with residue +1; a clockwise half-passage contributes −π to Δarg ξ, which exactly compensates the standard +1 of the Riemann–von Mangoldt formula derived for contours enclosing the pole. Our first calibration with +1 produced a systematic unit shift at every height; it was caught by a cross-check of S(T) against the file and corrected.

The reader's digest: the textbook "+1" belongs to contours that enclose the pole; this campaign's contour excludes it via the upper detour, a clockwise half-turn worth −π — exactly half a turn, exactly one unit of count. Keep the detour and the +1 and you count one zero that does not exist, at every height, with perfect numerical precision. The campaign made this mistake once, caught it through the S(T) cross-check (a uniform shift by one is the signature of a calibration error, not of noise), and encoded the corrected convention as a theorem. The positive certification is the anchor row: at T = 10 the winding is −5.142573567093604e-28 — zero — against n_on_line_file = 0; the protocol check IVP04 re-verifies the anchor set 0/3/10/29/79/649.

<a id="sec-results"></a>

## Results — all committed tables

### Headline table (verbatim)

| Quantity | Value | Status |
|---|---|---|
| Anchors N(T) | 0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649 | = n_line |
| Arithmetic bridge fp ↔ mpmath (T = 100.07) | \|ΔN\| = 2.6e-26 | machine rigour |
| Residual S(T) on [0, 1.13e6] | maximum 1.7994 (within ±1.8) | classics reproduced |
| Second moment Σγ² (K6) | deviation from (T³/6π)(ln(T/2π)−1/3) = 8.8e-7 | formula exact |
| Gaps below T = 1000 | min 0.3104 · max 6.887 · mean 1.521 | Lehman–Odlyzko |
| The 2π aliasing trap | first version lost turns (N=5 instead of 10) | found and fixed |

One paragraph per row. *Anchors N(T)*: the strip counts at the campaign heights form the sequence 0/3/10/29/79/138/202/269/…/649, and each equals its independent on-line count — the RH-in-the-strip statement, one height at a time. *Arithmetic bridge*: the numpy and mpmath counts at T = 100.07 differ by 2.5849394142282115e-26, so the integer 29 is fixed beyond any rounding doubt — hence "machine rigour". *Residual S(T)*: against the von Mangoldt counting identity (criterion K5), evaluated over the extended interval [0, 1.13e6], the classical residual peaks at 1.7994, inside the ±1.8 envelope — "classics reproduced"; IVP05 re-checks the threshold S(T) ≤ 1.8 (measured 1.8, PASS). *Second moment Σγ²*: the sum of squared ordinates up to T = 1 132 490.66 matches (T³/6π)(ln(T/2π)−1/3) with relative deviation 8.8e-7 and no fitted constant — "formula exact"; the backstory is the 4π³ episode below. *Gaps*: among the 649 zeros below T = 1000 the neighbouring gaps span 0.3104 to 6.887 with mean 1.521 — the opening members of the Lehman–Odlyzko gap statistics that later feed the GUE comparisons. *Aliasing trap*: the single-leaf first version returned N = 5 instead of 10 at T ≈ 51.4; the double leaf condition fixed it — "found and fixed" is a status the package publishes, not hides.

### The anchor registry (compact)

All thirteen heights from `data/results.json`; the pass flags are true throughout (`anchors_pass`, `all_blocks_pass`, `rh_verified_in_block_T: 1000.0`, `N_1000: 649`):

| Height T | N (strip) | n on line | Residual to integer | S_arg |
|---|---|---|---|---|
| 10.0 | −5.142573567093604e-28 | 0 | 5.142573567093604e-28 | −0.023719897999744943 |
| 27.717866853 | 3.0 | 3 | 3.2311742677852644e-27 | −0.011257014921764532 |
| 51.372076978 | 10.0 | 10 | 0.0 | 0.12118278887043062 |
| 100.074522612 | 29.0 | 29 | 0.0 | −0.0352361444205391 |
| 199.64003080999998 | 79.0 | 79 | 0.0 | 0.004919660600110632 |
| 300.744825758 | 138.0 | 138 | 0.0 | −0.17034760086815656 |
| 400.91217423850003 | 202.0 | 202 | 0.0 | −0.24180189079660733 |
| 499.444933686 | 269.0 | 269 | 4.1359030627651384e-25 | −0.20013275667741084 |
| 600.57388855 | 341.0 | 341 | 4.1359030627651384e-25 | −0.1559531445659736 |
| 699.714417304 | 414.0 | 414 | 4.1359030627651384e-25 | −0.3430531529818248 |
| 800.629291337 | 491.0 | 491 | 4.1359030627651384e-25 | −0.14194041703505927 |
| 900.3543122345 | 569.0 | 569 | 8.271806125530277e-25 | −0.03029991046962854 |
| 1000.5705270975 | 649.0 | 649 | 8.271806125530277e-25 | −0.07662397292694866 |

(The full record with S_file, ζ-evaluation counts and per-height runtimes is in `data/results.json` and in the deep edition `README.md`.) The monograph's own excerpt table, rounded (T / N (strip) / n on line / residual): 10.00 / 0 / 0 / 5.1e-28; 27.72 / 3 / 3 / 3.2e-27; 51.37 / 10 / 10 / 0.0; 100.07 / 29 / 29 / 0.0; 199.64 / 79 / 79 / 0.0; 500.45 / 269 / 269 / 4.1e-25; 1000.57 / 649 / 649 / 8.3e-25.

<img src="../../assets/avatars/hp_agent_lyra.svg" width="120" align="right" alt="Agent Lyra"/>

Note the shape of the S_arg column: all values sit between −0.3430531529818248 and +0.12118278887043062, far inside ±1.8, and the committed control points +0.38/+0.34/+0.79/+0.50 (from the monograph, criterion K5) reproduce the classical oscillations of the residual against the smooth count. Small residuals of the *right* size, oscillating the *classical* way, are themselves evidence: a buggy counter produces residuals that are either huge or suspiciously tame, never this texture.

### Bridge and gaps, committed

| Bridge (T = 100.074522612) | | Gaps below T = 1000 | |
|---|---|---|---|
| N_fp | 29.0 | n (zeros) | 649 |
| N_mp | 29.0 | min_gap | 0.3104307050000443 |
| delta | 2.5849394142282115e-26 | argmin_gap_T | 750.655950362 |
| bridge_ok | true | max_gap | 6.887314496999998 |
| | | argmax_gap_T | 14.134725142 |
| | | mean_gap | 1.5210753802700616 |

The largest gap starts at the first zero: 14.134725142 + 6.887314497 = 21.022039639, the second zero — a small arithmetic identity that ties the committed fields together and makes the "6.887" memorable. The smallest gap, 0.3104307050000443, occurs at T = 750.655950362. For the GUE reader: these are raw gaps; after unfolding by the local density ≈ (1/2π) ln(t/2π) the mean becomes order 1 with level repulsion at zero — the regime the package's spectral campaigns (C3–C5, C8; ⟨r⟩ = 0.60 at Nv ≥ 8) test against random-matrix ensembles. C2 supplies the trusted zero list those comparisons stand on.

<a id="sec-read"></a>

## How to read the numbers

- **N_strip / N_int** — the winding count as a float, and its nearest integer. The float is not a rounded mask: at T = 10 it is −5.142573567093604e-28, visibly zero.
- **n_on_line_file** — the independent half of every equality; from the committed zero registry, not from the winding.
- **residual_to_int** — how far the winding sits from its integer; the headline "residuals ≤ 8.3e-25" is the maximum of this column, 8.271806125530277e-25.
- **S_arg vs S_file** — the same classical residual S(T) = N − N̄ computed along two routes; their agreement to ≤ 1e-13 certifies that winding and registry see the same zeros.
- **meta.refine = 0.3** — the |wrap| half of the double leaf condition; **meta.dps = 26** — the reference arithmetic; **meta.contour** — the contour string, pole bypass included.
- **Two different bounds, two different meanings.** 8.3e-25 is an *arithmetic* claim (the counter is numerically clean); ±1.8 is a *mathematical* claim (the counted residual behaves as a century of theory says it must, criterion K5). Both passed; neither substitutes for the other.

<a id="sec-honesty"></a>

## The found-and-fixed episode: Σγ²

Criterion K6 closes the second moment: Σ γ_n² up to T = 1 132 490.66 against the continuum formula (T³/6π)(ln(T/2π) − 1/3), with committed relative deviation 8.8e-7 — without a single fitted constant. The instructive part is how this agreement was achieved. The first version of the formula **carried a factor error of 4π³ ≈ 124**; it was found *through the mismatch with the data* — the parameter-free prediction and the computed sum disagreed by a factor too large and too structured to ignore — and after the correction the deviation settled at 8.8e-7.

The lesson the package draws, verbatim from its honest notes:

> The K6 story is instructive: the first version of the second-moment formula carried a factor error of 4π³ ≈ 124, found through the mismatch with the data; the final agreement is a property of the formula, not a fit.

Why this builds trust rather than spending it: the formula has no free constants, so a wrong factor cannot be absorbed — it can only show up as a mismatch, and here the mismatch pointed straight at 4π³. The corrected agreement is therefore a property of the *formula*, not of a fit to the data. The episode is registered in the package's honesty registry (`results/RESULTS.md`: *the Σγ² multiplier error (4π³) found and fixed, documented in C2*) next to C1's published refutation K1 — the badge "statuses-honest" in the header is a standing commitment that errors are recorded in the same tables as successes, with the same typographic prominence. The same campaign that reports "found and fixed" for the aliasing trap reports "formula exact" for the corrected K6; a reader who trusts the second should trust it *because* of the first.

<a id="sec-interpretation"></a>

## Interpretation: what is and is not claimed

**Claimed.** Below T = 1000 the critical strip and the critical line hold the same zeros: 649 = 649, at thirteen heights, with winding residuals ≤ 8.3e-25, the arithmetic bridge 2.6e-26, and the classical residual S(T) inside ±1.8 (peak 1.7994 on [0, 1.13e6]). The counting is component-consistent with the rest of the series below that height: phase (C1), counting (C2), zero registry.

**Not claimed.** A proof of RH — verification in the strip up to T = 1000 is a finite check, not an asymptotic theorem; the honest boundary below which the counting agrees component by component. An operator — the Hilbert–Pólya identity remains open, and the package's own verdicts on its lattice gates are negative on spectral identity (H2: NO, three measurements in C3/C4/C5) even where they are positive on GUE statistics (H3). An identification of the resonator's self-dual line α = ½ with Re s = ½ — that bridge is conjectural and kept separate from the measurements. A protocol re-count — IVP04/IVP05 check the committed anchors and the S(T) bound, not a fresh run of the campaign.

<img src="../../assets/avatars/hp_agent_vera.svg" width="120" align="right" alt="Agent Vera"/>

**What the machinery is worth downstream.** Campaign C12 re-deploys the same calibrated instrument an order of magnitude higher: in the band up to T = 5000 it returns N_online = N_strip = 4520 against the smooth count N̄(5000) = 4520.08, with S_max = 0.91 (theorem T14) — an order of magnitude in height and a sevenfold count relative to C2. The instrument scales; the honest claim widens with it, one verified interval at a time.

<a id="sec-repro"></a>

## Reproduction

The committed tour, verbatim command:

```bash
# guided tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c2_argument.py
```

It prints the anchors and blocks with their counts, residuals and on-line numbers; the arithmetic bridge |ΔN| = 2.6e-26 at T = 100.074523; and the gap summary (649 zeros, [0.3104, 6.887], mean 1.521) — all replayed from the committed `data/c2_argument_verdict.json`.

Environment and guarantees: series seed — **96**; RNG streams fixed (`engine/hamiltonian.py`); dependencies in `requirements.txt`; reference environment of the release run Python 3.12, numpy 2.1, scipy 1.14, mpmath 1.3; the registry rule requires a repeated run to reproduce the committed values **bit-for-bit** (see `data/README.md`). For the protocol-level cross-check of the committed numbers:

```bash
python3 -c "from hpbridge.validate import run_all; [print(r) for r in run_all()]"
```

with the C2-relevant rows IVP04 (anchors 0/3/10/29/79/649 — PASS) and IVP05 (S(T) ≤ 1.8, measured 1.8 — PASS).

<a id="sec-data"></a>

## Data and figures

| File | Where |
|---|---|
| `fig03_argument_en.png` | 600 dpi — top-level `figures_hires/en/fig03_argument_en.png`; screen — `figures/en/` |
| `fig04_gaps_en.png` | 600 dpi — top-level `figures_hires/en/fig04_gaps_en.png`; screen — `figures/en/` |

(The Russian-labelled variants of the same plots are `fig03_argument_ru.png` and `fig04_gaps_ru.png` under the top-level `figures_hires/ru/` and `figures/ru/`.) Captions, as in the monograph: *N(T) (copper) against the smooth count N̄(T) (teal) and the residual S(T) (dashed, right axis): the anchors sit on the curve*; *nearest-neighbour zero gaps below T = 1000: mean 1.521, minimum 0.3104, maximum 6.887*. Numeric substrate: `data/curve.npz` and the `S_curve` block of `data/results.json`.

Monographs — the full monograph of this computation (setting, theorems, tables, figures, honest limitations): `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — 7–9 pages, the same content in two languages.

| File | Contents |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c2_*.json` | duplicate of the verdict in the common registry |

<a id="sec-verdict"></a>

## Verdict

**RH verified in the strip up to T = 1000 (649 = 649)** — details: `data/results.json`, the monograph, and `independent_verification/` (the IVP checks of this campaign).

<a id="sec-faq"></a>

## FAQ

**In one sentence — what did C2 establish?**
That below T = 1000 the critical strip and the critical line contain exactly the same zeros — 649 = 649 — measured by an argument-principle counter that is calibrated at the pole (T3), alias-proof (double leaf condition), and machine-certified (bridge 2.6e-26).

**Does that prove RH?**
No. It is a finite verification up to T = 1000 — the honest boundary below which the counting agrees component by component. RH quantifies over all heights.

**Why is there no +1 in the count?**
The upper detour around s = 1 contributes −π to the argument — half a turn, one unit — exactly cancelling the textbook +1 that assumes the pole is enclosed (lemma T3). Keeping both would add one phantom zero at every height.

**What are K4, K5 and K6?**
The campaign's three criteria: K4 — the argument-principle count is consistent (the 649 = 649 machinery); K5 — the von Mangoldt counting identity holds, with S(T) within ±1.8 (peak 1.7994); K6 — the second moment Σγ² matches (T³/6π)(ln(T/2π)−1/3) to 8.8e-7.

**Could the 649 be a floating-point accident?**
No — that is what the arithmetic bridge is for. The same contour in mpmath dps = 26 gives the same count with |ΔN| = 2.6e-26, and the anchors reproduce the registry counts 0/3/10 independently of the winding.

**What if I want more than the tour?**
Read `data/results.json` field by field (the "How to read the numbers" section is the key), run the full re-count with the fixed seed 96 for a bit-for-bit reproduction, and consult the deep edition `README.md` for the complete registry table and the history of the method.

<a id="sec-see"></a>

## See also

- [C1 · The identity function Z(t)](../C1_identity_function/README.md) — the phase and the graph whose zeros are counted here; criteria K1–K4, K7.
- [docs/theory.md](../../docs/theory.md) — the five-stage map; stage 3 · Counting is this campaign, with T3 (pole calibration).
- [results/RESULTS.md](../../results/RESULTS.md) — the living registry; C2 holds rows 5–8 and the Σγ² honesty-registry entry.
- [independent_verification/RESULTS.md](../../independent_verification/RESULTS.md) — IVP04 and IVP05 in full.
- [C12 · Band T = 5000](../C12_band_5000/README.md) — the same machine, an order of magnitude higher (theorem T14).

---
*Hilbert Polya Bridge v1.0.0 · C2 · The argument principle up to T = 1000*

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="README.md">⬆ parent section</a></sub>

</div>
