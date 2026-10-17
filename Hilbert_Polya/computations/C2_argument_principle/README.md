# C2 · The argument principle up to T = 1000

![version](https://img.shields.io/badge/version-2.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_spectrum_emerge.png" width="720" alt="The zeta spectrum emerging over the critical line — dossier of campaign C2"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

<p align="center"><em>Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra counted, Agent Vera verified.</em></p>

> **Counting zeros in the critical strip without tables: the adaptive Turing step, the pole calibration (lemma T3), the arithmetic bridge 2.6e-26, RH verified in the strip: 649 = 649.**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Claim | below T = 1000 the critical strip and the critical line contain exactly the same zeros — decided by the argument principle alone, with no table of zeros consulted as an authority |
| Verdict | RH verified in the strip up to T = 1000 (649 = 649) |
| Instrument | the argument principle on the contour (2,0)→(2,T)→(0,T)→(0,0), the pole s = 1 bypassed from above by a small semicircle; N(T) = Δarg ξ / 2π |
| Headline counts | 649 = 649 at thirteen heights up to T ≈ 1000; anchors 0 / 3 / 10 / 29 / 79 / 649; winding residuals ≤ 8.3e-25 |
| Arithmetic bridge | \|ΔN\| = 2.6e-26 — the same contour in numpy and in mpmath at dps = 26, at T = 100.074522612 |
| Classical residual (K5) | S(T) ≤ 1.8 — maximum 1.7994 on [0, 1.13e6] |
| Gaps below T = 1000 | min 0.3104 · max 6.887 · mean 1.521 (Lehman–Odlyzko) |
| Second moment Σγ² (K6) | deviation 8.8e-7 from (T³/6π)(ln(T/2π)−1/3) — formula exact, no fitted constant |
| Anti-aliasing | double leaf condition \|wrap\| ≤ 0.3 AND length ≤ h_safe; the 2π aliasing trap (N=5 instead of 10) was found and fixed |
| One-line meaning | the campaign winds the argument of ξ around the strip and compares the strip count with the independent on-line count; the equality of the two counts at every probed height is the operationalisation of the Riemann Hypothesis below T = 1000 |

Reproduction at a glance (series seed 96; the tour needs no zero file and runs in seconds):

```bash
# guided tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c2_argument.py

# protocol-level cross-check of the committed numbers (not a re-count)
python3 -c "from hpbridge.validate import run_all; [print(r) for r in run_all()]"

# committed verdict of the campaign — data/results.json (registry duplicate ../data/c2_argument_verdict.json)
# numeric substrate of the figures — data/curve.npz · the S_curve block of data/results.json
# 600 dpi figures — figures_hires/ru/fig03_argument_ru.png · figures_hires/ru/fig04_gaps_ru.png
#                    figures_hires/en/fig03_argument_en.png · figures_hires/en/fig04_gaps_en.png
# monographs — monograph_ru.docx · monograph_ru.pdf · monograph_en.docx · monograph_en.pdf
```

Every number in this card is traceable to `data/results.json` (registry duplicate `../data/c2_argument_verdict.json`).

**About this edition.** This is the definitive English dossier of campaign C2 — the single unified edition of this folder. Every number, verdict label, file name and command below is taken verbatim from the committed sources of the repository, primarily `data/results.json` (the campaign verdict, duplicated in the common registry as `data/c2_argument_verdict.json`), the C2 monograph chapters (`monograph_ru` / `monograph_en`), and the registry `results/RESULTS.md`. Nothing is estimated, extrapolated or beautified: where the package reports a residual of 8.3e-25, the committed maximum is 8.271806125530277e-25, and this page says both.

## Contents

1. [Quick reference card](#quick-reference-card)
2. [The question](#sec-question)
3. [Background: the argument principle 101, and why adaptive](#sec-background)
4. [The method, step by step](#sec-method)
5. [The pole calibration: T3](#sec-t3)
6. [Results](#sec-results)
7. [How to read the numbers](#sec-read)
8. [The found-and-fixed episode: Σγ² as an honesty case study](#sec-honesty)
9. [Interpretation: RH in the strip versus global RH](#sec-interpretation)
10. [Reproduction](#sec-repro)
11. [Data and figures](#sec-data)
12. [Verdict](#sec-verdict)
13. [FAQ](#sec-faq)
14. [A short history of the argument principle in RH](#sec-history)
15. [Glossary](#sec-glossary)
16. [See also](#sec-see)

<a id="sec-question"></a>

## The question

How many zeta zeros lie in the critical strip below a height T, and are they all on the critical line? The campaign answers via the argument principle: the contour (2,0)→(2,T)→(0,T)→(0,0) bypassing the pole s = 1 from above gives N(T) = Δarg ξ / 2π, and this number is compared with the count of on-line zeros found independently. The equality N_strip = N_line at each height is the operationalisation of the Riemann Hypothesis; at thirteen heights up to T ≈ 1000 it holds.

<img src="../../assets/avatars/hp_riemann.svg" width="120" align="right" alt="Bernhard Riemann"/>

That single sentence compresses the whole campaign, so it is worth unpacking. The critical strip is the vertical band 0 < Re s < 1 of the complex plane; a "height" T means the horizontal level Im s = T. The Riemann Hypothesis (RH) asserts that every non-trivial zero of ζ(s) sits exactly on the middle line Re s = ½ of that strip. Counting is the oldest and most robust way to test this: if one can show that the strip below height T contains exactly N zeros, and that exactly N zeros lie on the line Re s = ½ below the same height, then — for that interval — RH is verified, because the two sets must coincide. No analytic number theory beyond the argument principle is needed; no table of zeros is consulted as an authority.

This is why the campaign is deliberately table-free. In the Hilbert–Pólya programme the zeros are destined to become the spectrum of a self-adjoint operator; before any spectrum can be compared against them, the zeros themselves must be counted by an independent, self-contained instrument. A table would smuggle in an external authority. The argument principle needs only the ability to evaluate ξ(s) along a contour — and, as campaign C1 established for the phase θ(t) and the identity graph Z_id(t) = e^{iθ(t)}ζ(½+it), the components of the counting machine are already verified inside the package: C1 closed the Γ-ladder at machine precision (max residual 2.59e-39 at dps 40), proved the reality of Z_id (T2), and matched its first 79 zeros against mpmath with max|Δγ| = 2.8e-14 (criterion K3). C2 adds the third station of the bridge map — counting — as summarised in `docs/theory.md`: *stage 3 · Counting — the argument principle — T3 (pole calibration) — RH in the strip up to T = 1000*. Downstream, the spectral campaigns C3–C5 need exactly this kind of independent, machine-verified zero account to compare spectra against.

The headline outcome, stated once here and dissected for the rest of this page: **at all thirteen heights up to T ≈ 1000 the strip count equals the line count, ending at 649 = 649, with every winding number within 8.3e-25 of an integer.** The equality is a test rather than a tautology — it can only come out positive if both computations are right — and thirteen times out of thirteen below T ≈ 1000, it did.

<a id="sec-background"></a>

## Background: the argument principle 101, and why adaptive

### The principle

For a function f meromorphic inside and on a closed contour C, with no zeros or poles on C itself, the argument principle states

> (1/2πi) ∮_C f′(s)/f(s) ds = Z − P = Δarg f / 2π,

where Z and P are the numbers of zeros and poles of f inside C, counted with multiplicity, and Δarg f is the total accumulated change of the argument of f as one traverses C once counter-clockwise. The equality of the contour integral of the logarithmic derivative with the winding number of f(C) around the origin is one of the workhorses of complex analysis; applied to the Riemann xi-function it turns zero-counting into a bookkeeping problem for a phase.

The Riemann ξ-function, ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s), is entire: the factor ½ s(s−1) cancels the simple pole of ζ at s = 1 and tames the trivial zeros at the negative even integers. Hence P = 0 inside any contour, and the winding number of ξ along the boundary equals the number of ξ-zeros enclosed — which are exactly the non-trivial zeros of ζ. The rectangle (2,0)→(2,T)→(0,T)→(0,0), closed back along the real axis, encloses precisely the zeros of the strip with 0 < Im s < T. This is the contour of campaign C2, reproduced verbatim from the committed meta block of the verdict: *contour: "(2,0)→(2,T)→(0,T)→(0,0), pole s=1 from above, N=Δarg/2π"*.

Counting zeros becomes measuring a phase — the oldest trick in the Riemann trade, and still the most trustworthy.

### The pole at s = 1 and the detour

<img src="../../assets/avatars/hp_hilbert.svg" width="120" align="right" alt="David Hilbert"/>

One subtlety is visible already in the contour description. The closing segment of the rectangle runs along the real axis from (0,0) to (2,0) — straight through s = 1, where ξ′/ξ has a simple pole with residue +1 (the pole of ζ, cancelled in ξ itself but not in its logarithmic derivative). A contour cannot pass through a singularity of its integrand. The standard remedy, and the one used here, is to detour around s = 1 by a small semicircle in the upper half-plane. Whether that detour adds or removes a full unit from the final count is exactly the subject of lemma T3 — the calibration that this campaign had to get right before any of its numbers meant anything; it is treated in its own section below.

### Why the step must be adaptive

The second subtlety is numerical. The density of zeros at height t grows like (1/2π) ln(t/2π), and the argument of ξ along the horizontal edge of the contour winds correspondingly faster as T grows: the total winding is N(T) ≈ (T/2π) ln(T/2π) − T/2π + 7/8. A quadrature that samples the argument at a fixed step in t will eventually alias — two consecutive samples may differ by more than half a turn, and a full revolution of the phase slips through the mesh unnoticed, silently undercounting N by an integer. The classical cure goes back to Alan Turing's 1953 computations: subdivide recursively until, on every elementary arc, the argument change is provably smaller than a half-turn, so that no full turn can hide between samples.

The package implements this as a **recursively adaptive Turing step with a double leaf condition**: recursion stops on an arc only when *both* |wrap| ≤ 0.3 (the wrapped argument increment is small) *and* the arc length is ≤ h_safe, where h_safe is estimated from bounds on |ζ′/ζ| at the given height. The first bound prevents an unnoticed revolution; the second prevents a nearly-cancelling pair of large swings on a steep segment — the very failure mode that produced the campaign's instructive 2π aliasing trap, recorded in the results table with the honest status "found and fixed".

The aliasing trap deserves one sentence of respect, because it is the reason the campaign trusts itself. With a single leaf condition the first version of the counter returned N = 5 instead of 10 at T ≈ 51.4 — it lost exactly half the zeros, all to silently missed turns. The error was not caught by inspecting the code but by cross-checking: the residual S(T) computed from the (wrong) count disagreed with the file-based count, exposing the shift. The cure — the second half of the double leaf condition — is the difference between a counter that is fast and a counter that is right. The methods document `docs/methods.md` registers the final design in one line: *campaign C2 counting — recursively adaptive Turing step with a double leaf condition; two arithmetics (numpy / mpmath dps 26) with the 2.6e-26 bridge*.

<a id="sec-method"></a>

## The method, step by step

The canonical method paragraph of the campaign, verbatim:

> A two-tier implementation: a numpy branch with a recursively adaptive step (the double leaf condition: |wrap| ≤ 0.3 AND length ≤ h_safe from the |ζ′/ζ| bounds) and an mpmath branch at dps = 26 for reference heights. The pole is bypassed from above by a small semicircle; by lemma T3 the additive +1 is NOT applied — its absence is verified by the S(T) cross-check and the anchors of the zero file.

Unfolded into an executable recipe, the campaign proceeds as follows.

1. **Fix the height set.** Thirteen heights are committed in the meta block of the verdict (run dated 2026-10-10, task "Task 8a — K4 up to T≈1000, adaptive Turing step", dps = 26, refine = 0.3): 10.0, 27.717866853, 51.372076978, 100.074522612, 199.64003080999998, 300.744825758, 400.91217423850003, 499.444933686, 600.57388855, 699.714417304, 800.629291337, 900.3543122345, 1000.5705270975. The first three are the *anchors* of the campaign; the remaining ten are the *blocks* that carry the verification up to T ≈ 1000.
2. **March the contour.** The right edge climbs from (2,0) to (2,T), the top edge runs from (2,T) to (0,T), the left edge descends from (0,T) to (0,0); the near-real closing segment detours around s = 1 from above by a small semicircle. On σ = 2 and σ = 0 the integrand is tame; almost all of the winding happens on the two horizontal edges and is dominated by the top one.
3. **Sample and accumulate.** At each sample the integrand ξ (evaluated through ζ) contributes its argument increment; increments are wrapped into a principal branch, which is why the leaf threshold is naturally expressed as |wrap| ≤ 0.3 — comfortably below the half-turn at which wrapping becomes ambiguous.
4. **Recurse where needed.** Any arc failing the double leaf condition (|wrap| ≤ 0.3 AND length ≤ h_safe) is bisected and processed recursively; h_safe comes from bounds on |ζ′/ζ|, so the step tightens automatically wherever the logarithmic derivative is large — near zeros and near the pole.
5. **Close the winding.** The wrapped increments sum to Δarg ξ along the whole contour; N_strip = Δarg ξ / 2π. By lemma T3 no +1 is added (see the next section).
6. **Round and compare.** N_strip is rounded to N_int and compared with n_on_line_file — the number of zeros on Re s = ½ below the same height, taken from the package's committed zero registry, i.e. independently of the winding computation. The pass condition is N_int = n_on_line_file with residual_to_int within tolerance.
7. **Cross-check with the smooth count.** In parallel, S_arg = N_strip − N̄(T) is computed against the Riemann–von Mangoldt smooth count N̄(T), and S_file = N_line − N̄(T) against the file count. The two estimates of the same classical residual agree to 1e-13 or better at every height (for example at T = 1000.570527 they are −0.07662397292694866 and −0.07662397292699552), and both stay well inside the classical ±1.8 envelope. This is the tripwire that caught both the +1 calibration error and the aliasing trap.
8. **Bridge the arithmetics.** At the reference height T = 100.074522612 (the bridge_T of the meta block) the entire contour is recomputed in mpmath at dps = 26 and compared with the numpy branch: N_fp = 29.0 versus N_mp = 29.0, delta = 2.5849394142282115e-26 — the celebrated 2.6e-26 arithmetic bridge. The fast branch's integer is thereby certified as machine-exact, not merely plausible.

The cost profile is part of the committed record and worth stating, because "verification up to T = 1000" sounds expensive and is not: the per-height ζ-evaluation counts run from 2145 (T ≈ 27.7) through 2209, 4258, 8482, 16929, 16932, 16913, 33825, 33825, 33826, 33831 to 67617 (T ≈ 900.4 and T ≈ 1000.6), and the committed runtimes from 0.23 s to 25.24 s per height — roughly 105 seconds in total for the whole thirteen-height campaign. Note the non-monotonicity at the low end: T = 10 needed 16913 evaluations, more than T ≈ 27.7 or T ≈ 51.4, because near the real axis the contour must resolve the pole detour and the first zero with a much finer mesh. The adaptive machinery earns its keep.

<a id="sec-t3"></a>

## The pole calibration: T3

Everything in C2 rests on a sign. The lemma, stated verbatim as in the monograph:

> **Lemma T3 (pole calibration).** When the pole s = 1 is bypassed from above by a small semicircle, its argument contribution is −π; hence N(T) = Δarg ξ / 2π WITHOUT the additive +1.

> **Proof.** ξ′/ξ has a simple pole at s = 1 with residue +1; a clockwise half-passage contributes −π to Δarg ξ, which exactly compensates the standard +1 of the Riemann–von Mangoldt formula derived for contours enclosing the pole. Our first calibration with +1 produced a systematic unit shift at every height; it was caught by a cross-check of S(T) against the file and corrected.

Why this matters enough to be a numbered theorem of the package: the textbook formula N(T) = (T/2π) ln(T/2π) − T/2π + 7/8 + S(T) + 1 — with its characteristic "+1" — is derived for a contour that encloses the pole s = 1 in its interior, so the pole contributes a full turn. The C2 contour deliberately *excludes* the pole by detouring above it: the small semicircle is traversed clockwise (right-to-left along the top of the point s = 1), a half-turn, worth exactly −π in the argument of ξ — half of the −2πi log contribution of a residue +1 pole. The half-turn removes exactly the unit that the "+1" would add. Dropping the detour's effect and keeping the +1 (or vice versa) shifts **every** N(T) by exactly 1 — an error of the kind that no amount of numerical precision can repair, because it is not a rounding error but a bookkeeping error: the count would be perfectly precise and perfectly wrong.

The campaign's first calibration made precisely this mistake and documents it honestly: with the +1 applied, a systematic unit shift appeared at every height. It was caught not by belief but by the S(T) cross-check — the residual computed against the file count was off by one everywhere, which is impossible for a correct counter — and corrected; a uniform shift by one is the signature of a calibration error, not of noise. The corrected calibration is then positively certified by the anchors: at T = 10 the committed winding is N_strip = −5.142573567093604e-28, i.e. zero to 27 decimal places, matching n_on_line_file = 0; a spurious +1 would have insisted on 1 = 0. The same certifying logic appears in the verdict of the independent verification protocol, where IVP04 checks the anchors 0/3/10/29/79/649 and passes. T3 is thus the cheapest theorem of the series and one of the most load-bearing: it is the difference between counting the zeros of the strip and counting the zeros of the strip plus one imaginary zero that lives only in a misapplied formula.

<a id="sec-results"></a>

## Results

### Headline table (verbatim)

| Quantity | Value | Status |
|---|---|---|
| Anchors N(T) | 0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649 | = n_line |
| Arithmetic bridge fp ↔ mpmath (T = 100.07) | \|ΔN\| = 2.6e-26 | machine rigour |
| Residual S(T) on [0, 1.13e6] | maximum 1.7994 (within ±1.8) | classics reproduced |
| Second moment Σγ² (K6) | deviation from (T³/6π)(ln(T/2π)−1/3) = 8.8e-7 | formula exact |
| Gaps below T = 1000 | min 0.3104 · max 6.887 · mean 1.521 | Lehman–Odlyzko |
| The 2π aliasing trap | first version lost turns (N=5 instead of 10) | found and fixed |

Each row, unpacked:

- **Anchors N(T) = n_line.** The listing 0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649 is the sequence of strip counts N_int at the campaign heights; at every one of them it equals the independent on-line count n_on_line_file. The values 0/3/10/29/79 together with the terminal 649 are exactly the anchor set re-checked by the independent verification protocol (IVP04).
- **Arithmetic bridge \|ΔN\| = 2.6e-26.** The same contour at T = 100.07 computed in two arithmetics agrees to 2.5849394142282115e-26. "Machine rigour" is the status because the integer 29 is thereby pinned to a window eight orders of magnitude tighter than any conceivable rounding ambiguity: the count is not approximately 29, it is 29.
- **Residual S(T) on [0, 1.13e6] — classics reproduced.** The classical residual S(T) = N(T) − N̄(T), computed against the von Mangoldt counting identity (criterion K5), was evaluated over the extended interval [0, 1.13e6] — the same span as the second-moment criterion K6 below — and peaks at 1.7994, inside the classical ±1.8 bound. The independent verification protocol re-checks the bound as IVP05 (threshold S(T) ≤ 1.8, measured 1.8, PASS).
- **Second moment Σγ² (K6), formula exact.** The sum of squared zero ordinates matches the continuum formula (T³/6π)(ln(T/2π)−1/3) to relative deviation 8.8e-7 with not one fitted constant. The row's status is a summary of the campaign's most instructive episode — the 4π³ factor error — told in its own section below.
- **Gaps below T = 1000 — Lehman–Odlyzko.** The 649 zeros below T = 1000 have neighbouring gaps with minimum 0.3104, maximum 6.887 and mean 1.521, the opening members of the famous Lehman–Odlyzko sequence of gap statistics. Committed details: min_gap = 0.3104307050000443 at T = 750.655950362, max_gap = 6.887314496999998 at T = 14.134725142, mean_gap = 1.5210753802700616.
- **The 2π aliasing trap — found and fixed.** The first version of the adaptive counter lost full turns on steep segments and returned N = 5 instead of 10 at T ≈ 51.4; the double leaf condition was the cure. "Found and fixed" is a status label the package earns, not decorates itself with.

### The full anchor registry

The committed verdict `data/results.json` (registry duplicate `data/c2_argument_verdict.json`) holds the complete thirteen-height record. Reproduced verbatim:

| Height T | N (strip) | n on line | Residual to integer | S_arg | S_file | ζ-evals | Runtime (s) |
|---|---|---|---|---|---|---|---|
| 10.0 | −5.142573567093604e-28 | 0 | 5.142573567093604e-28 | −0.023719897999744943 | −0.023719897999744832 | 16913 | 1.5946590900421143 |
| 27.717866853 | 3.0 | 3 | 3.2311742677852644e-27 | −0.011257014921764532 | −0.011257014921764341 | 2145 | 0.22529864311218262 |
| 51.372076978 | 10.0 | 10 | 0.0 | 0.12118278887043062 | 0.12118278887042955 | 2209 | 0.25295114517211914 |
| 100.074522612 | 29.0 | 29 | 0.0 | −0.0352361444205391 | −0.03523614442054068 | 4258 | 0.6447761058807373 |
| 199.64003080999998 | 79.0 | 79 | 0.0 | 0.004919660600110632 | 0.004919660600108955 | 8482 | 1.7196199893951416 |
| 300.744825758 | 138.0 | 138 | 0.0 | −0.17034760086815656 | −0.1703476008681548 | 16929 | 4.042997121810913 |
| 400.91217423850003 | 202.0 | 202 | 0.0 | −0.24180189079660733 | −0.24180189079660863 | 16932 | 4.497040510177612 |
| 499.444933686 | 269.0 | 269 | 4.1359030627651384e-25 | −0.20013275667741084 | −0.20013275667741937 | 33825 | 9.857929706573486 |
| 600.57388855 | 341.0 | 341 | 4.1359030627651384e-25 | −0.1559531445659736 | −0.15595314456601272 | 33825 | 10.535053491592407 |
| 699.714417304 | 414.0 | 414 | 4.1359030627651384e-25 | −0.3430531529818248 | −0.34305315298183814 | 33826 | 10.929907321929932 |
| 800.629291337 | 491.0 | 491 | 4.1359030627651384e-25 | −0.14194041703505927 | −0.1419404170350731 | 33831 | 11.542756795883179 |
| 900.3543122345 | 569.0 | 569 | 8.271806125530277e-25 | −0.03029991046962854 | −0.030299910469693714 | 67617 | 24.295958518981934 |
| 1000.5705270975 | 649.0 | 649 | 8.271806125530277e-25 | −0.07662397292694866 | −0.07662397292699552 | 67617 | 25.240369081497192 |

Every row carries `"pass": true`; the first three rows additionally carry `"anchor": true`. The committed verdict object closes with `anchors_pass: true`, `all_blocks_pass: true`, `rh_verified_in_block_T: 1000.0`, `N_1000: 649`. The first three heights also appear, rounded, in the monograph's Table 1 — the argument-principle anchors excerpt (T / N (strip) / n on line / residual): 10.00 / 0 / 0 / 5.1e-28; 27.72 / 3 / 3 / 3.2e-27; 51.37 / 10 / 10 / 0.0; 100.07 / 29 / 29 / 0.0; 199.64 / 79 / 79 / 0.0; 500.45 / 269 / 269 / 4.1e-25; 1000.57 / 649 / 649 / 8.3e-25.

<img src="../../assets/avatars/hp_agent_lyra.svg" width="120" align="right" alt="Agent Lyra"/>

Reading the registry as a whole: the equality N_strip = n_on_line_file holds at all thirteen heights; the largest deviation of a winding number from its integer is 8.271806125530277e-25 (at T ≈ 900.4 and T ≈ 1000.6), quoted in prose as "residuals ≤ 8.3e-25"; the S_arg and S_file columns agree to 1e-13 or better everywhere, and both remain far inside the ±1.8 classical envelope, with the largest magnitude in this table −0.3430531529818248 at T ≈ 699.7. Note the shape of the S_arg column: all values sit between −0.3430531529818248 and +0.12118278887043062, far inside ±1.8 — small residuals of the *right* size, oscillating the *classical* way, are themselves evidence. The committed control points +0.38/+0.34/+0.79/+0.50 (from the monograph, criterion K5) reproduce the classical oscillations of the residual against the smooth count; a buggy counter produces residuals that are either huge or suspiciously tame, never this texture.

### The bridge

| Field | Value |
|---|---|
| Bridge height (bridge_T) | 100.074522612 |
| N_fp (numpy branch) | 29.0 |
| N_mp (mpmath branch, dps = 26) | 29.0 |
| delta | 2.5849394142282115e-26 |
| bridge_ok | true |

A float64 counter can be fast and wrong in ways that are hard to see from inside itself. The bridge is the campaign's answer to the question any numerical auditor should then ask: how do you know your double-precision counter is not artifacts all the way down? Recomputing the same contour in an arithmetic with 26 significant digits and obtaining agreement to 2.6e-26 pins the winding number between the two arithmetics so tightly that the integer it rounds to is not in doubt — and since the anchor heights show the same equality against the file, the certification propagates.

### Gaps below T = 1000

| Field | Value |
|---|---|
| n (zeros below T = 1000) | 649 |
| min_gap | 0.3104307050000443 |
| argmin_gap_T | 750.655950362 |
| max_gap | 6.887314496999998 |
| argmax_gap_T | 14.134725142 |
| mean_gap | 1.5210753802700616 |

The 649 zeros have 648 neighbouring gaps. The largest one opens immediately after the first zero: the committed fields give argmax_gap_T = 14.134725142 and max_gap = 6.887314496999998, and indeed 14.134725142 + 6.887314497 = 21.022039639 — the second zero. The smallest gap 0.3104307050000443 occurs at T = 750.655950362, the closest approach of two consecutive zeros below the height limit. Why do gap statistics belong in a counting campaign's headline table? Because the *shape* of the gap distribution is the classical meeting point between counting and the GUE story: after unfolding (rescaling by the local density ≈ (1/2π) ln(t/2π)), random-matrix predictions say the mean spacing is 1 with level repulsion at zero; the raw mean 1.521 below T = 1000 is exactly what the growing density implies, and the [0.3104, 6.887] spread is the texture that the spectral campaigns downstream (C3–C5, C8, with ⟨r⟩ = 0.60 at Nv ≥ 8 and the Dyson trinity of statistics) confront with random-matrix nulls. The row's label "Lehman–Odlyzko" credits the classical literature on these very statistics; C2 supplies the trusted zero list those comparisons stand on.

<a id="sec-read"></a>

## How to read the numbers

The verdict JSON is the campaign's contract with its readers, and its field names are designed to be read without the code:

- **N_strip** — the winding number of ξ along the contour, as a float. At T = 10 it is −5.142573567093604e-28: zero, to an accuracy that itself testifies the counter is unbiased.
- **N_int** — the nearest integer to N_strip; the campaign's strip count.
- **n_on_line_file** — the number of zeros on Re s = ½ below the same height, taken from the committed zero registry, i.e. a *different* computation. The pass condition is N_int = n_on_line_file; RH-in-the-strip is the statement that this equality is not an accident at any height.
- **residual_to_int** — |N_strip − N_int|. The campaign's headline precision claim "residuals ≤ 8.3e-25" is the maximum of this column (8.271806125530277e-25).
- **S_arg / S_file** — the classical residual S(T) = N − N̄ computed from the winding count and from the file count respectively. Their mutual agreement to ≤ 1e-13 certifies that the two counting routes see the same zeros; their magnitude ≲ 0.4 certifies that both agree with the smooth Riemann–von Mangoldt count within the classical S(T) behaviour (bounded in the campaign's extended check by 1.7994 ≤ 1.8 on [0, 1.13e6]).
- **n_zeta_evals / runtime_s** — the cost of the height: from 2145 evaluations / 0.23 s at T ≈ 27.7 to 67617 / 25.24 s at T ≈ 1000.6.
- **meta.refine = 0.3** — the |wrap| leaf threshold of the adaptive step; **meta.dps = 26** — the reference arithmetic's precision; **meta.contour** — the contour string with the pole bypass record.
- **bridge fields** — N_fp, N_mp, delta at bridge_T = 100.074522612; **gaps_below_1000 fields** — n, min/max/mean gap and their argmin/argmax locations, as tabulated above.

Two distinct "≤" claims must not be conflated: **8.3e-25** is the machine-precision residual of winding numbers against integers (arithmetic quality), while **±1.8** is the classical analytic bound within which the residual S(T) oscillates (mathematical content, criterion K5). The first says the counter is honest; the second says what it counted matches a century of theory. The campaign needed both to pass, and both did.

<a id="sec-honesty"></a>

## The found-and-fixed episode: Σγ² as an honesty case study

Criterion K6 closes the second moment: Σ γ_n² — the sum of the squared ordinates of the zeros up to T = 1 132 490.66 — is compared with the continuum prediction (T³/6π)(ln(T/2π) − 1/3). The committed agreement is a relative deviation of 8.8e-7, without a single fitted constant. On its face this is one more exact formula verified at machine scale; the history of the criterion is why it is one of the most valuable entries in the whole package.

The first version of the second-moment formula **carried a factor error of 4π³ ≈ 124**. It was not found by proof-reading and not by a referee: it was found *through the mismatch with the data* — the computed sum sat near a factor of 4π³ away from the prediction, a discrepancy far too large to blame on tolerance or rounding, and far too structured to ignore. The factor was corrected, and the deviation collapsed to 8.8e-7. The episode is registered in the package's honesty registry in `results/RESULTS.md`: *the Σγ² multiplier error (4π³) found and fixed, documented in C2* — and the campaign's own honest-notes blockquote preserves the lesson verbatim:

> The K6 story is instructive: the first version of the second-moment formula carried a factor error of 4π³ ≈ 124, found through the mismatch with the data; the final agreement is a property of the formula, not a fit.

Three things make this a model case rather than an embarrassment. First, **the error was discoverable**: because the prediction (T³/6π)(ln(T/2π) − 1/3) has no free parameters, a wrong constant cannot hide — it can only produce a mismatch, and the mismatch pointed at 4π³ specifically. Second, **the fix is verifiable in the direction that matters**: the final 8.8e-7 agreement is a property of the corrected *formula*, not the result of tuning anything to the data; there is no fitted constant whose removal would break the agreement. Third, **the failure is part of the published record**: the same package that reports "formula exact" reports, one table row earlier, "found and fixed" — the badge "statuses-honest" in the header of this README is a commitment that such episodes are registered, not laundered — errors are recorded in the same tables as successes, with the same typographic prominence. It is the same culture that in C1 published the refutation K1 of a candidate Γ-form rather than quietly dropping it.

For the reader calibrating their own trust: the correct inference from this section is not "the package once erred" but "the package's cross-checks are strong enough that a factor-124 error could not survive them". The S(T) cross-check caught the +1 calibration error and the aliasing trap; the parameter-free K6 comparison caught the 4π³ factor. The same campaign that reports "found and fixed" for the aliasing trap reports "formula exact" for the corrected K6; a reader who trusts the second should trust it *because* of the first. Every error the campaign has ever had, it found by confrontation with independent numbers.

<a id="sec-interpretation"></a>

## Interpretation: RH in the strip versus global RH

What is claimed, precisely:

- Below T = 1000, the number of zeta zeros in the critical strip equals the number on the critical line: **649 = 649**, certified at thirteen heights, with winding residuals ≤ 8.3e-25 and the arithmetic bridge |ΔN| = 2.6e-26.
- The counting machinery is internally consistent to machine precision (numpy ↔ mpmath) and externally consistent with the classical theory (S(T) within ±1.8; control points +0.38/+0.34/+0.79/+0.50 reproduce the classical oscillations of the residual).
- The three stages of the series tested so far — phase (C1), counting (C2), zero registry — agree component by component below T = 1000.

What is *not* claimed, stated with the same precision (the theory map's section "What is not claimed" is the package's standing instruction):

- **This is not a proof of RH.** Verification in the strip up to T = 1000 is a finite check, not an asymptotic statement; the honest-notes blockquote of the source README says exactly this: *verification in the strip up to T = 1000 is not a proof of RH for all heights; it is the honest boundary below which the counting agrees component by component*.
- **No operator is claimed.** The Hilbert–Pólya identity — a self-adjoint operator whose spectrum *is* the zero sequence — remains open; the package's own verdicts on its lattice "gates" are negative on spectral identity (H2: NO, measured three times in C3/C4/C5) while positive on the GUE universality class (H3). Counting zeros is a prerequisite for such comparisons, not a substitute for them.
- **The lattice line α = ½ is not the critical line by fiat.** The identification of the resonator's self-dual line with Re s = ½ is a conjectural bridge, and the package keeps "dynamics on line ½" (measured) separate from "line ½ = critical line" (conjecture).
- **The IVP does not recompute C2.** The independent verification protocol checks the anchors (IVP04: 0/3/10/29/79/649) and the S(T) bound (IVP05: S(T) ≤ 1.8, fact 1.8) against committed values; it does not re-run the heavy campaign, whose reproducibility rests on the fixed seed and bit-for-bit re-run obligation.

<img src="../../assets/avatars/hp_polya.svg" width="120" align="right" alt="George Pólya"/>

The machinery, however, scales. Campaign C12 (v2 series) re-deploys the C2 machine — the adaptive argument principle with the Turing-step bridge — an order of magnitude higher: in the band up to T = 5000 it obtains N_online = N_strip = 4520 against the smooth count N̄(5000) = 4520.08, with S_max = 0.91 (theorem T14) — an order of magnitude in height and a sevenfold count relative to C2. The pattern is the intended one: the same calibrated instrument, moved up the critical line, keeps returning equal counts — which is what a correct counter, and only a correct counter, can do.

<a id="sec-repro"></a>

## Reproduction

The committed tour of the verdict, verbatim from the source README:

```bash
# guided tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c2_argument.py
```

The script replays the committed verdict `data/c2_argument_verdict.json` and prints, line by line: each anchor and block with its integer count, residual and on-line count; the arithmetic bridge with |ΔN| = 2.6e-26 at T = 100.074523; and the gap summary below T = 1000 (649 zeros, gaps [0.3104, 6.887] with mean 1.521). It needs no zero file and runs in seconds.

The full campaign environment: series seed — **96**; the RNG streams are fixed (`engine/hamiltonian.py`); all dependencies are listed in `requirements.txt`. The reference environment of the release run (as recorded by the independent verification protocol) is Python 3.12, numpy 2.1, scipy 1.14, mpmath 1.3. The registry rule of the package applies in full: *a repeated run of the campaigns must reproduce the committed values bit-for-bit* (see `data/README.md`).

For the protocol-level cross-check of this campaign's committed numbers (not a re-count):

```bash
python3 -c "from hpbridge.validate import run_all; [print(r) for r in run_all()]"
```

Relevant protocol rows: **IVP04** — anchors of the argument principle, expected 0/3/10/29/79/649, measured 0/3/10/29/79/649, PASS; **IVP05** — count against the smooth count N̄, threshold S(T) ≤ 1.8, measured 1.8, PASS.

<a id="sec-data"></a>

## Data and figures

| File | Where |
|---|---|
| `fig03_argument_ru.png` | 600 dpi — `figures_hires/ru/fig03_argument_ru.png`; screen — `figures/ru/` |
| `fig04_gaps_ru.png` | 600 dpi — `figures_hires/ru/fig04_gaps_ru.png`; screen — `figures/ru/` |
| `fig03_argument_en.png` | 600 dpi — `figures_hires/en/fig03_argument_en.png`; screen — `figures/en/` |
| `fig04_gaps_en.png` | 600 dpi — `figures_hires/en/fig04_gaps_en.png`; screen — `figures/en/` |

Figure captions as in the monograph: *N(T) (copper) against the smooth count N̄(T) (teal) and the residual S(T) (dashed, right axis): the anchors sit on the curve*; and *nearest-neighbour zero gaps below T = 1000: mean 1.521, minimum 0.3104, maximum 6.887*. The numeric substrate of both figures is committed alongside the verdict: `data/curve.npz` and the `S_curve` block of `data/results.json` (the sampled T-grid from 17.5783823905 to 995.3049633675 with its curve values).

Monographs — the full monograph of this computation (setting, theorems, tables, figures, honest limitations): `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — 7–9 pages, the same content in two languages.

| File | Contents |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c2_*.json` | duplicate of the verdict in the common registry |

(The concrete registry duplicate is `../data/c2_argument_verdict.json`; the glob in the table is the source's own notation.) The zero registry used for the independent on-line counts lives under `../../data/zeros/` in the package root — the same mpmath-built caches against which campaign C1 matched its 79 zeros with max|Δγ| = 2.8e-14.

<a id="sec-verdict"></a>

## Verdict

**RH verified in the strip up to T = 1000 (649 = 649)** — details: `data/results.json`, the monograph, and `independent_verification/` (the IVP checks of this campaign).

The verdict label is reproduced in full, bilingual, exactly as committed — the package archives its verdicts verbatim in the language pair they were made in. The components of the claim, one line each: thirteen heights, thirteen equalities N_strip = n_line; terminal count 649 = 649; winding residuals ≤ 8.3e-25; arithmetic bridge 2.6e-26; S(T) ≤ 1.8 over [0, 1.13e6]; Σγ² deviation 8.8e-7; gaps [0.3104, 6.887] with mean 1.521; the two traps (+1 calibration, 2π aliasing) found and fixed.

<a id="sec-faq"></a>

## FAQ

**In one sentence — what did C2 establish?**
That below T = 1000 the critical strip and the critical line contain exactly the same zeros — 649 = 649 — measured by an argument-principle counter that is calibrated at the pole (T3), alias-proof (double leaf condition), and machine-certified (bridge 2.6e-26).

**Does 649 = 649 prove the Riemann Hypothesis?**
No. It proves — in the literal, machine-checked sense — that below T = 1000 no zero of ζ lies off the critical line, because the strip and the line hold exactly the same count at every probed height. RH is a statement about *all* heights. The package's own honest notes draw the boundary: this is the honest limit below which the counting agrees component by component, nothing more.

**Why is the additive +1 not applied when the pole is bypassed?**
Because the detour above s = 1 is a clockwise half-turn contributing −π to Δarg ξ, which cancels exactly the +1 that the Riemann–von Mangoldt formula reserves for contours enclosing the pole (lemma T3). Applying both adds a phantom zero to every height — the systematic unit shift that the first calibration exhibited and the S(T) cross-check exposed.

**What exactly is "the arithmetic bridge"?**
The same contour, counted twice in different arithmetics: numpy float64 (fast branch) and mpmath dps = 26 (reference branch) at T = 100.074522612. Result: N_fp = 29.0, N_mp = 29.0, |ΔN| = 2.5849394142282115e-26. The bridge certifies that the fast branch's integer is a property of ξ, not of floating-point noise. And the anchors reproduce the registry counts 0/3/10 independently of the winding.

**What are K4, K5 and K6?**
The campaign's three criteria: K4 — the argument-principle count is consistent (the 649 = 649 machinery); K5 — the von Mangoldt counting identity holds, with S(T) within ±1.8 (peak 1.7994); K6 — the second moment Σγ² matches (T³/6π)(ln(T/2π)−1/3) to 8.8e-7.

**How did the first version lose half the zeros at T ≈ 51?**
Step aliasing: with a single leaf condition, arcs on steep segments could hide a full 2π revolution between samples, and the counter returned N = 5 instead of 10 at T ≈ 51.4. The cross-check of S(T) against the file count exposed the missing turns; the double leaf condition — |wrap| ≤ 0.3 AND arc length ≤ h_safe from |ζ′/ζ| bounds — made the failure mode impossible. Status in the results table: found and fixed.

**Where do the on-line counts come from — are they independent?**
Yes. n_on_line_file comes from the package's committed zero registry, not from the winding computation; the registry itself was validated in C1, where the first 79 zeros of Z_id on [0, 200] matched mpmath with max|Δγ| = 2.8e-14 (criterion K3). The campaign's central equality is therefore a two-way agreement between genuinely different computations.

**How expensive is a reproduction?**
The committed tour (`python3 campaigns/run_c2_argument.py`) replays the verdict in seconds without touching the zero file. A fresh re-count of all thirteen heights cost about 105 seconds in total in the reference run (sum of the committed runtime_s fields, from 0.23 s to 25.24 s per height). The fixed seed 96 and the fixed RNG streams make the re-run bit-for-bit.

**What if I want more than the tour?**
Read `data/results.json` field by field — the "How to read the numbers" section above is the key — and run the full re-count with the fixed seed 96 for a bit-for-bit reproduction; the complete registry table and the history of the method are earlier on this page.

<a id="sec-history"></a>

## A short history of the argument principle in RH

The counting argument is the oldest quantitative thread of the Riemann literature, and C2 consciously works a well-worn vein. Riemann's 1859 memoir already framed the zeros through the argument of ζ along large contours, and von Mangoldt's 1895 work turned the heuristic into the explicit counting formula N(T) = (T/2π) ln(T/2π) − T/2π + 7/8 + S(T), whose residual S(T) is the same object this campaign bounds by 1.8. In the 1910s Backlund carried out the first substantial argument-principle counts and established the discipline of cross-checking counts against the sign pattern on the line — the ancestor of this campaign's S_arg versus S_file agreement.

The modern shape of the method — compute the count directly by the argument principle, combine it with verified knowledge about individual zeros, and let the two certify each other — is Turing's, from his 1953 zeta computations; the "adaptive Turing step" of this campaign is named for that inheritance. The mid-century and later refinements associated with Lehman and Odlyzko pushed the counts higher and, crucially, made the statistics of the gaps — the Lehman–Odlyzko sequence this README quotes in its gaps row — a standard diagnostic of the zero distribution, eventually feeding the Montgomery–Odlyzko confluence of zeta statistics with random-matrix theory, the GUE connection that the spectral campaigns of this package (C3–C5, C8) probe from the operator side.

What the historical continuum did with mainframes and hand-checking, C2 does with a recursively adaptive step, two arithmetics and a committed JSON: the same principle, the same residual, the same trap-avoidance — but with every intermediate value archived and every error registered. That is the actual novelty claimed here: not a new theorem, but a new *auditability* of a classical instrument.

<a id="sec-glossary"></a>

## Glossary

| Term | Meaning in this campaign |
|---|---|
| Critical strip | The band 0 < Re s < 1; non-trivial zeros of ζ live here. |
| Critical line | Re s = ½; RH asserts all non-trivial zeros lie on it. |
| ξ(s) | Riemann xi-function, ½s(s−1)π^{−s/2}Γ(s/2)ζ(s); entire, zeros = non-trivial zeros of ζ. |
| N(T) | Number of zeros in the strip with 0 < Im s < T; here obtained as N_strip = Δarg ξ / 2π. |
| N̄(T) | The smooth Riemann–von Mangoldt count (T/2π) ln(T/2π) − T/2π + 7/8. |
| S(T) | N(T) − N̄(T); the classical residual, bounded in the campaign's check by 1.7994 ≤ 1.8 on [0, 1.13e6]. |
| γ_n | The ordinate of the n-th zero on the critical line; Σγ² is their second moment (criterion K6). |
| Contour | The rectangle (2,0)→(2,T)→(0,T)→(0,0) with a small semicircular detour above s = 1. |
| Adaptive Turing step | Recursive bisection of contour arcs; leaf condition |wrap| ≤ 0.3 AND length ≤ h_safe. |
| h_safe | Arc-length ceiling derived from bounds on |ζ′/ζ|; the anti-aliasing guard. |
| Arithmetic bridge | numpy-vs-mpmath recomputation of the same contour; committed |ΔN| = 2.6e-26 at T = 100.07. |
| Anchor / block | The first three heights (T = 10, 27.72, 51.37) / the remaining ten heights of the run. |
| n_on_line_file | On-line zero count from the committed zero registry; the independent half of the equality. |
| K4 / K5 / K6 | Campaign criteria: argument-principle consistency; von Mangoldt counting identity (S(T) ≤ 1.8); second moment Σγ². |
| Gate (zatvor) | Lattice Hamiltonian of the package's resonator; counted and compared against zeros in C3–C5, not here. |
| GUE | Gaussian unitary ensemble; the random-matrix class whose spacing statistics the zero gaps are compared against downstream. |
| IVP | Independent verification protocol; rows IVP04 (anchors) and IVP05 (S(T) ≤ 1.8) cover this campaign. |

<a id="sec-see"></a>

## See also

- [C1 · The identity function Z(t)](../C1_identity_function/README.md) — the phase and the graph this campaign counts zeros on; criteria K1–K4, K7.
- [docs/theory.md](../../docs/theory.md) — the five-stage map of the bridge; stage 3 is this campaign.
- [results/RESULTS.md](../../results/RESULTS.md) — the living registry of numbers; rows 5–8 are C2's.
- [independent_verification/RESULTS.md](../../independent_verification/RESULTS.md) — IVP04 and IVP05, the protocol-level cross-checks.
- [C12 · Band T = 5000](../C12_band_5000/README.md) — the same counting machine, ten times higher (theorem T14).

---
*Hilbert Polya Bridge v2.0.0 · C2 · The argument principle up to T = 1000*
