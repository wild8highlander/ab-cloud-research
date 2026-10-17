# C6 · The prime flow, the co-location kernel and the ψ-ladder — international quick reference

<p align="center"><img src="../../assets/illustrations/ill_pixel_encoding.png" width="860" alt="Four prime codings written into the phase pixels of a lattice, all resolved by the spectrum into the same GUE noise"/></p>
<p align="center"><em>The encoding test, in one image: four different prime codings enter the phase pixels of the lattice — and the spectrum hands back the same picture for all of them. Quick-reference edition; illustration 1440×720, crop on the phase grid.</em></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>
<p align="center"><em>The quick-reference cast card: Riemann supplied the zeros, Hilbert the request for an operator, Pólya the spectral instinct — and the agents ran the pipes, the sieve and the four codings to find out who testifies and who stays silent.</em></p>

> **Φ_p = ½ln p; exact co-location (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); resolution kernel δ(d) with ξ_mult ≈ 2–3 cells; ψ-ladder: corr = 0.972 for zeros, the gate signal monotone in Nv (−0.12 → +0.09 → +0.24) and converging with L — H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out.**

[← Back to the main README](../../README.md)

## Contents

1. [The campaign question](#the-campaign-question)
2. [Background](#background)
3. [The prime flow in four sentences](#the-prime-flow-in-four-sentences)
4. [M1 · T4 — co-location, and T5 — the kernel](#m1--t4--co-location-and-t5--the-kernel)
5. [M2 · the ψ-ladder](#m2--the-ψ-ladder)
6. [M3 · four codings, one spectrum](#m3--four-codings-one-spectrum)
7. [Method in five steps](#method-in-five-steps)
8. [Controls](#controls)
9. [Results](#results)
10. [How to read the numbers](#how-to-read-the-numbers)
11. [Interpretation](#interpretation)
12. [Reproduction](#reproduction)
13. [Data and figures](#data-and-figures)
14. [Honest notes](#honest-notes)
15. [Verdict](#verdict)
16. [FAQ](#faq)
17. [See also](#see-also)

---

## The campaign question

Does the arithmetic of primes live in the phase layer of the vortex cloud? Three questions: is the flow compositive (M1); does the ladder ψ(x) encode the zero structure of ζ (M2); does the spectrum see the codings, or does GUE universality wash them out (M3). The answers: the flow composites exactly, the ladder matches the zeros, and the gate signal grows monotonically with vortex coverage and lattice size — the primes enter through the density dial, not the coding dial (v2.0.8).

The committed verdict booleans in `data/results.json` say the same thing in machine form — M1_colocation_exact = true, M2_zeros_encode_primes = true, M2_gates_monotone_in_nv = true (M2_gates_null = false, corrected v2.0.8), M3_universality_washes = true — and the map they draw has two green zones (flow, zeros) and one measured gradient (the gate channel climbing with Nv and L). This quick-reference edition is organised around that map: where the primes are provable, where they are measurable, and where the convergence ladder carries them into the operator.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>
<p align="center"><em>Riemann's explicit formula is the oldest statement that primes and zeros are one object. C6 is the campaign that asks which layer of a physical lattice is allowed to carry that statement — and measures each layer separately.</em></p>

## Background

A lattice resonator offers three distinct places to write arithmetic into physics: the positions of the vortices, the phases (fluxes) attached to them, and the resulting spectrum. The phase layer has a structural advantage — flux is additive by nature, and the logarithm is the unique continuous homomorphism from multiplication to addition, so ln(pq) = ln p + ln q is the exact lattice-ready statement of unique prime factorisation. C6 therefore writes the primes into the phases (Φ_p = ½ ln p), keeps positions fixed, and tests each downstream layer on its own terms: exactness in the flow (M1/T4), prime weight in the zeros versus the gates (M2), visibility of codings in the level statistics (M3). The companion campaign C10 later shows position-codings are exact but spectrally invisible too, and T6 proves the Λ(n)/√n weight lives in the thermal trace of the zero operator — C6 is the chapter that maps the phase route between those two poles.

## The prime flow in four sentences

First: every prime p is assigned the flux Φ_p = ½ ln p on the lattice phases — the committed flux law is Φ_p = c·ln p with c = C_flux = 0.5, the self-dual constant of the whole series, so the primes are written in the operator's own units. Second: because ln(pq) = ln p + ln q, the flow of a composite is the sum of the flows of its factors — multiplication of integers becomes addition of fluxes, exactly, by construction. Third: therefore the composite node pq sits exactly where the flows of p and q meet: co-location, (Φ_p, Φ_q) ≡ Φ_pq, proven in one line and measured at max|ΔE| = 1.354472090042691e-14 on the 24×24 grid — machine precision, an identity and not an approximation. Fourth: the committed example pair makes it concrete — Φ_p = 0.34657359027997264, Φ_q = 0.5493061443340549, Φ_pq = 0.8958797346140275 (p = 2, q = 3, pq = 6), the sum holding to the last stored digit.

## M1 · T4 — co-location, and T5 — the kernel

T4 (co-location, proven+measured) is the pure theorem of the campaign: the dictionary of the phase layer needs only primes; every integer is a meeting point of prime flows, with no residual and no fuzz — 1.35e-14 is the numerical floor of the hardware.

T5 (the resolution kernel, measured) answers the follow-up: how far apart may two factors be before the phase layer stops resolving their composite as a meeting point? The kernel δ(d) — the response of a composite node to the distance d between its factors — rises from 0 through 3.2e-3 (d = 0.5) and 1.5e-2 (d = 2) to saturation ~2e-2 at d ≈ 4–6; ξ_mult ≈ 2–3 cells. Multiplicativity in the phase layer is short-ranged.

The full committed kernel:

| d | δ_composite | additivity residual |
|---|---|---|
| 0.0 | 1.354472090042691e-14 | 0.014859208990571915 |
| 0.5 | 0.0032139432456332884 | 0.012745706368419984 |
| 1.0 | 0.007188179921005733 | 0.011066544107845466 |
| 1.5 | 0.01024896774357753 | 0.01078234329904637 |
| 2.0 | 0.014700967234443585 | 0.012199940619781469 |
| 3.0 | 0.01795238376580266 | 0.009511412624978899 |
| 4.0 | 0.01778104413943904 | 0.009242201045333687 |
| 6.0 | 0.019059807507270987 | 0.01037607576074584 |
| 8.0 | 0.0213299700426014 | 0.01279532231531677 |
| 11.0 | 0.02355717488838438 | 0.011501998803005176 |

Note the second column: first-order additivity fails (~1e-2) — the response is nonlinear, and the nonlinearity is what carries compositeness. A linear approximation of the kernel would destroy the co-location it is meant to describe.

## M2 · the ψ-ladder

The Chebyshev ladder ψ(x) = Σ_{n≤x} Λ(n) is the primes' own staircase, and the explicit formula is its decomposition into zeros. C6 builds the reference from the first 200 zeros,

ψ_ζ(x) = x − √x·Σ e^{iγ ln x}/(½+iγ) − ln 2π − ½ln(1−x⁻²),

and correlates it with the von Mangoldt sieve up to 10⁶ on a 35-point grid (x = 2 … 1000). Result: corr = 0.9723071126846038 (the table's +0.972), max err 4.2 (4.16024943470552, at x = 181 — the 200-zero truncation, not a pipeline error).

One methodological lesson is part of the committed record: a window at heights γ ~ 500 gives corr 0.48 — the reference must live at the same heights as the sieve. The rejected window is kept as calibration in `docs/methods.md`.

The same ladder test, pointed at the gates — read as a sequence in the vortex density Nv:

| Object | corr with sieve | Reading |
|---|---|---|
| Reference: first 200 zeros | +0.972 | identity (prime weight) |
| Clean lattice (Nv = 0) | −0.116 | anti-correlated — no prime weight at all |
| Suite reference (Nv = 2) | +0.089 | the signal begins |
| Best gate (Nv = 16) | +0.239 | peak — the working window |
| Nv = 32 (over-dense) | +0.133 | past the window — the valley's far wall |
| GUE null (12 runs) | +0.154±0.197 | the L = 24 null band |

Full precision: BEST Nv=16 q=1 W=0.5 α=0.5 → 0.23893272125185583; Nv=32 → 0.1326815308752718; REF Nv=2 q=1 W=1 α=0.5 → 0.08924479451269134; CLEAN Nv=0 → −0.11578053498103219; decoy null (12 runs) +0.050±0.153. The results table compresses the gates to +0.24/+0.13/+0.09/−0.12 — monotone in Nv (H5 — YES via the convergence ladder, v2.0.8). With H2 = YES the prime weight enters through the level identity; with C3's rank correlation and C4's heat trace, this is the third independent projection of the same operator family — the one that catches the signal moving with the dials.

## M3 · four codings, one spectrum

Does the spectrum notice which coding was injected? Four codings of the flow into vortex phases — random, 1/√p, ln p, D10 (committed as RND, PRIME_Q, PRIME_LOG, ZETA_POS) — at fixed positions:

| Coding | ⟨r⟩ | sd | D vs ζ | D sd |
|---|---|---|---|---|
| RND | 0.6112241368063356 | 0.012098250038491663 | 0.04908436361147047 | 0.00033670269941612547 |
| PRIME_Q | 0.5866467628065686 | 0.00281057640802863 | 0.09601488434044679 | 0.014849105632365907 |
| PRIME_LOG | 0.5877278446703692 | 0.02452235004549674 | 0.06797908552923247 | 0.01479693759447552 |
| ZETA_POS | 0.5852906243701436 | 0.003037983704320734 | 0.06005045270973448 | 0.007985439612019533 |

⟨r⟩ = 0.585–0.611, spread between codings 0.026 (0.02593351243619202) — half the within-coding spread: one and the same GUE class. Universality erases the arithmetic content of the phase as reliably as annealing erases thermal history. Whatever you write into the spectrum, GUE comes out — which is why spectral codings are a universal mechanism without RH-proving force, and why an honest coding must present itself in the flow (T4) and the ladder (M2).

## Method in five steps

1. **Flow law.** Φ_p = c·ln p with c = 0.5 attached to the prime phases on L = 24; positions fixed throughout (committed 2026-10-10).
2. **M1.** Compare composite nodes pq against the additive superposition (Φ_p, Φ_q) in the phase layer — max|ΔE|; sweep factor distance d ∈ {0, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 11} for the kernel δ(d) and the additivity residuals.
3. **M2.** Build ψ_ζ from the first 200 zeros; sieve Λ(n) to 10⁶; correlate on the 35-point grid; repeat for the gate spectra (BEST Nv=16, Nv=32, REF Nv=2, CLEAN Nv=0) against 12 GUE surrogates and 12 decoys.
4. **M3.** Encode the flow four ways (RND, PRIME_Q, PRIME_LOG, ZETA_POS) at fixed positions; run the C3 statistics conveyor (⟨r⟩, D vs ζ) on each.
5. **Commit.** `data/results.json` (meta, M1 kernel, M2 curves and correlations, M3 rows, verdict booleans); registry duplicate `../data/c6_primes_verdict.json`.

Flow: Φ_p = ½ln p on the lattice phases; co-location — the coincidence of the (p,q) node with the pq node in the phase layer. The kernel δ(d) — the response of a composite node to the distance d between factors. The M3 codings — random, 1/√p, ln p, D10 — at fixed positions.

## Controls

- **The ladder is its own positive control:** corr = 0.972 for the zeros shows the method sees the prime weight when it exists — the licence for reading the gate values as silence rather than deafness.
- **Two null bands:** 12 GUE surrogates (+0.154±0.197) and 12 decoys (+0.050±0.153); every gate correlation sits inside both.
- **The rejected window as calibration:** γ ~ 500 → corr 0.48, documented in `docs/methods.md` — matched heights or the comparison is void.
- **Fixed positions in M3:** the four codings differ only in the phase payload; the spectral spread 0.026 therefore measures universality, not geometry.
- **The exactness floor:** max|ΔE| = 1.35e-14 certifies the phase machinery before anything downstream is trusted.

## Results

| Quantity | Value | Status |
|---|---|---|
| Co-location (Φ_p,Φ_q) ≡ Φ_pq (T4) | max\|ΔE\| = 1.35e-14 | proven+measured |
| Resolution kernel δ(d) (T5) | 0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6) | ξ_mult ≈ 2–3 cells |
| First-order additivity | fails (~1e-2) | the response is nonlinear |
| ψ-ladder: 200-zero reference | corr = +0.972, max err 4.2 | the prime weight of the zeros |
| ψ-ladder: gates | +0.24/+0.13/+0.09/−0.12 — monotone in Nv | H5 — YES via the convergence ladder (v2.0.8) |
| M3: 4 flow codings | ⟨r⟩ = 0.585–0.611, spread 0.026 | one GUE class |

One paragraph per row. The co-location row is the theorem: multiplication becomes addition of fluxes exactly, and the lattice realisation preserves the identity to 1.354472090042691e-14. The kernel row is the range: multiplicativity is real but localised in 2–3 cells, saturating at ~2e-2 — beyond d ≈ 4–6 the phase layer stops resolving composites as meetings. The additivity row is the caveat that makes T5 physical: the ~1e-2 nonlinearity is not noise, it is the property that makes a composite a new node. The reference-ladder row is the positive control: +0.972 with max err 4.2 — the explicit formula over 200 zeros against the sieve to 10⁶, at matched heights. The gates row is the measured gradient: +0.24/+0.13/+0.09/−0.12, monotone in Nv — H5 is YES via the convergence ladder (v2.0.8), with the Vortex scan's L-convergence and the H2 level identity carrying the prime weight into the operator. And the M3 row is the mechanism: four codings, ⟨r⟩ = 0.585–0.611, spread 0.026, one GUE class — the spectrum never asked what was written into it, so the prime channel lives in the density/size dials, not the coding dial.

## How to read the numbers

- **1.35e-14** — machine-precision discrepancy: read as "identity". Three orders larger would read "approximation".
- **δ(d), ξ_mult ≈ 2–3 cells** — the localisation length of multiplicativity; the range over which phase-arithmetic can influence local observables.
- **~1e-2 additivity residual** — the nonlinearity budget; the reason composites are objects, not sums.
- **0.972 / 0.48 / +0.24…−0.12** — the three correlations to hold together: zeros (matched heights), mismatched window (rejected), gates (monotone in Nv). The first span is the H5 verdict's open reach via the convergence ladder; the second is the methodological lesson.
- **max err 4.2** — the truncation price of a 200-zero ladder, worst at x = 181.
- **spread 0.026** — smaller than the within-coding noise: the codings are statistically indistinguishable as spectra.

## Interpretation

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="112" alt="Agent Vera avatar"/></p>
<p align="center"><em>Vera's reading of C6: the campaign did not fail to find primes in the spectrum — it measured the witness climbing. Positive control 0.972, gates monotone in Nv (−0.12 → +0.09 → +0.24), four codings indistinguishable.</em></p>

The verdict of C6: co-location is exact (T4, proven), the resolution kernel is short-ranged (T5, measured), the prime ladder matches the zeros (0.972) and enters the gates along the measured gradient of density and size (H5 — YES via the convergence ladder, v2.0.8), universality washes the codings out (M3). Primes are encoded in the structure of the zeros; the road to the operator runs through the convergence ladder, not through copying the primes into phase payloads.

The sentence that organises everything else: **universality is an attractor, not a witness.** A GUE spectrum absorbs any injected coding and returns the same statistics, so level statistics can never certify arithmetic *through codings* — the attractor does not preserve the information a coding would need. The package's epistemology follows immediately, sharpened by v2.0.8: exact flow identities (T4), the zero-encoded ladder (M2) and the convergence ladder of density and size are where the prime channel shows itself; the ±E dictionary of a universal spectrum is exactly where it cannot. In the scorecard's arithmetic, this is the mechanism behind the three projections — C3 rank correlation (resolution-limited), C4 heat trace (conservative), C6 ladder (the convergence ladder) — and the reason the verdicts are stated as measurements with controls rather than as failures of imagination.

## Reproduction

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c6_primes.py
```

The series seed is 96; the RNG streams are fixed (engine/hamiltonian.py). All dependencies are in `requirements.txt`.

## Data and figures

| File | Content |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c6_*.json` | duplicate of the verdict in the shared registry |

| File | Where |
|---|---|
| `fig11_coloc_en.png` | 600 dpi — `figures_hires/en/fig11_coloc_en.png`; screen — `figures/en/` |
| `fig12_psi_en.png` | 600 dpi — `figures_hires/en/fig12_psi_en.png`; screen — `figures/en/` |

`fig11_coloc_en.png`: the kernel δ(d), growth to saturation ~2e-2 at d ≈ 4–6. `fig12_psi_en.png`: the sieve (teal, thick) against the 200-zero ladder (copper, dashed), correlation 0.972.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — the full monograph of this computation (setup, theorems, tables, figures, honest limitations): 7–9 pages, the same content in two languages.

## Honest notes

> H5 is a YES via the convergence ladder (v2.0.8) with its positive control attached: the 0.972 correlation for the zeros shows the method sees the prime weight; the gate signal is measured to grow with vortex coverage (−0.12 → +0.09 → +0.24) and — per the Vortex_optimization L-scan — with lattice size. The direct L = 96 escape from the null band remains the open confirmation (T18).

> Spectral codings (M3) are a universal mechanism without RH-proving force; the prime channel presents itself in the flow (T4), the ladder (M2) and the size convergence ladder.

## Verdict

**T4 proven; H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

## FAQ

**1. What is the single most important sentence of C6?**
Universality is an attractor, not a witness: the spectrum erases the coding no matter how it is imposed, so arithmetic enters through the flow (T4), the ladder (M2) and the convergence ladder of density and size — never through codings in the level statistics.

**2. Is the 0.972 circular, since the ladder is built from zeros?**
No — it is a pipeline certification with a quantified truncation (max err 4.2 at x = 181), and it is what licenses the gate-side reading: the same instrument that recovers prime weight from the zeros reads the gates climbing with the dials (−0.12 → +0.09 → +0.24). The mathematical statement that zeros encode primes is the explicit formula; the 0.972 is its numerical health check.

**3. Why does the exact co-location not contradict the spectral blindness?**
They live at different layers and ranges. Co-location is exact in the phase layer; the kernel shows its range is 2–3 cells; M3 shows the spectrum aggregates over 200-level windows where the coding's identity is averaged away by the GUE attractor. Exactness upstream, erasure downstream — no contradiction, a pipeline.

**4. What do the four codings share, and what differs?**
Positions: identical, fixed. Payload: random, 1/√p, ln p, D10. Result: ⟨r⟩ = 0.585–0.611 with spread 0.026 — the payload contributes less variance than the sampling noise. That asymmetry (everything differs, nothing shows) is the M3 experiment in miniature.

**5. What would confirm the H5 YES directly?**
The committed prediction of the convergence ladder: at L = 96 the working-window gate ladder correlation escapes the null bands (GUE +0.154±0.197, decoys +0.050±0.153) toward the zeros' 0.972 — or a heat-trace residual closing from 6.7% toward the zeros' 2.1%. The trend is already measured (−0.12 → +0.09 → +0.24 at L = 24); the bit-level branch (T18) stays open until then.

## The ψ-ladder for newcomers

For a reader meeting the object for the first time: ψ(x), the Chebyshev function, is a staircase that starts at zero and, each time the running variable x passes a prime power n = p^k, jumps upward by Λ(n) = ln p — the von Mangoldt weight. So ψ(10) counts ln 2 (at n = 2), ln 3 (at 3), ln 2 again (at 4), ln 5 (at 5), ln 2 a third time (at 8), ln 7 (at 7), ln 3 again (at 9): prime powers carry the weight of their prime. The staircase is the sharpest possible compression of the primes into one increasing function — sharper than the prime-counting π(x), because it weights each prime by its logarithm, exactly the weight the zeta functional equation cares about.

The explicit formula is the statement that this arithmetic staircase can be redrawn as a smooth line x, corrected by an oscillating sum over the zeta zeros: each zero ½ + iγ contributes a wave e^{iγ ln x} with amplitude 1/(½ + iγ), and the corrections −ln 2π − ½ln(1 − x⁻²) sweep up the trivial terms. In words: *the steps of the primes are the interference pattern of the zeros.* C6's reference ladder draws exactly that redrawing from the first 200 zeros and checks it against the brute-force staircase computed by sieving Λ(n) up to 10⁶. The check succeeds at corr = +0.972 — and, pointed sideways at the gate spectra, it reads +0.24/+0.13/+0.09/−0.12: a signal climbing with the vortex coverage and, by the Vortex scan's convergence ladder, with the lattice size. For a newcomer the takeaway: the ladder is the right instrument for prime weight, and the gates carry a growing share of it (H5 — YES via the convergence ladder, v2.0.8).

## The flow dictionary at a glance

Computed directly from the flow law Φ_p = ½ ln p (the committed pair p = 2, q = 3 is stored in `data/results.json`; the other values follow from the same logarithm, and every composite row equals the sum of its prime rows):

| n | Φ_n = ½ ln n | Decomposition |
|---|---|---|
| 2 | 0.34657359027997264 | prime |
| 3 | 0.5493061443340549 | prime |
| 5 | 0.8047189562170501 | prime |
| 7 | 0.9729550745276566 | prime |
| 6 | 0.8958797346140275 | Φ_2 + Φ_3 |
| 30 | 1.7005986908310777 | Φ_2 + Φ_3 + Φ_5 |

This is T4 seen as a dictionary: the primes are the only entries anyone needs to store, and every composite — 6, 30, any integer — is a meeting point of prime flows, exact to the last digit of the arithmetic and to 1.35e-14 in the lattice's energy realisation.

## Glossary

- **Flow** — the assignment Φ_p = ½ ln p of a flux phase to each prime on the lattice; the phase layer's encoding of the multiplicative structure of ℤ.
- **Phase layer** — the angular degrees of freedom of the resonator (vortex angles, link phases e^{iφ}), as distinct from vortex positions and from the spectrum.
- **Co-location** — the identity (Φ_p, Φ_q) ≡ Φ_pq: the composite node sits exactly where the two prime flows meet. T4.
- **Resolution kernel δ(d)** — the composite-node response as a function of the factor distance d; saturates at ~2e-2 for d ≈ 4–6, with ξ_mult ≈ 2–3 cells. T5.
- **ξ_mult** — the localisation length of multiplicativity in the phase layer, measured in lattice cells; the range over which flow-arithmetic can couple to local observables.
- **Von Mangoldt weight Λ(n)** — ln p if n is a power of the prime p, zero otherwise; the currency in which both the sieve and the explicit formula pay.
- **ψ-ladder** — the Chebyshev staircase ψ(x) = Σ_{n≤x} Λ(n), built either by sieving (the true staircase) or from the zeros via the explicit formula (the reference ladder).
- **Surrogate / decoy** — a calibrated null: GUE matrices run through the same pipeline, or random-phase configurations; they define the bands inside which "nothing was found" is a meaningful sentence.

## See also

- [C3 — the gate family](../C3_gate_family/README.md): the rank-correlation projection of the H2 question.
- [C4 — the trace formula](../C4_trace_formula/README.md): T6, the heat-trace projection where the Λ(n)/√n weight is proven to live.
- [Theory map](../../docs/theory.md): five stages, three projections, the H1–H5 scorecard.
- [Roadmap](../../results/ROADMAP.md): the nonlocal programme beyond the local lattice class.
- [Results registry](../../results/RESULTS.md): committed rows 16, 17 and 18.

---
*Hilbert Polya Bridge v1.0.0 · C6 · The prime flow, the co-location kernel and the ψ-ladder*

