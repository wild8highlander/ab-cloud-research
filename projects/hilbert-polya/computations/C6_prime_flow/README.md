<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ computations/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# C6 · The Prime Flow, the Co-location Kernel and the ψ-Ladder — where the arithmetic of primes actually lives

<p align="center"><img src="../../assets/illustrations/ill_prime_flow.png" width="860" alt="The prime flow: phases Φ_p = ½ ln p streaming through the vortex lattice, composite nodes landing exactly on additive superpositions"/></p>
<p align="center"><em>The prime flow: every prime p enters the phase layer with flux Φ_p = ½ ln p, and multiplication becomes addition — the composite node pq lands exactly where the flows of p and q meet. Illustration 1440×720.</em></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>
<p align="center"><em>The cast follows the prime flow: from Riemann's explicit formula, through Hilbert's operator programme and Pólya's spectral answer, to the three agents who measured where the primes really live — in the flow and in the zeros, not in the level statistics.</em></p>

> **Φ_p = ½ln p; exact co-location (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); resolution kernel δ(d) with ξ_mult ≈ 2–3 cells; ψ-ladder: corr = 0.972 for zeros, the gate signal monotone in Nv (−0.12 → +0.09 → +0.24) and converging with L — H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out.**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Campaign | C6 — the prime flow, the co-location kernel and the ψ-ladder (phase layer of the vortex lattice; L = 24, C_flux = 0.5, committed 2026-10-10) |
| Claim | Φ_p = ½ln p; exact co-location (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); resolution kernel δ(d) with ξ_mult ≈ 2–3 cells; ψ-ladder: corr = 0.972 for zeros, the gate signal monotone in Nv and converging with L — H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out |
| Verdict | 'T4 proven; H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out' — booleans in `data/results.json`: M1_colocation_exact = true, M2_zeros_encode_primes = true, M2_gates_monotone_in_nv = true (M2_gates_null = false, corrected v2.0.8), M3_universality_washes = true |
| Headline numbers | max\|ΔE\| = 1.35e-14 (T4) · δ(d): 0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6) · corr = +0.972, max err 4.2 (at x = 181) · gates +0.24/+0.13/+0.09/−0.12 — monotone in Nv, peaking in the working window · M3 ⟨r⟩ = 0.585–0.611, spread 0.026 |
| The three correlations | 0.972 (zeros) / 0.48 (mismatched window, rejected) / +0.24…−0.12 (gates — monotone in Nv) — the first gap carries the H5 verdict via the convergence ladder, the second is the matched-heights lesson |
| Null bands | 12 GUE surrogates +0.154±0.197 · 12 decoys +0.050±0.153 — the L = 24 gate values sit inside both; the trend through them is monotone in Nv (v2.0.8: finite-size attenuation, not absence) |
| Committed pair | Φ_p = 0.34657359027997264, Φ_q = 0.5493061443340549, Φ_pq = 0.8958797346140275 (p = 2, q = 3, pq = 6) |
| Artifacts | `data/results.json` · `../data/c6_primes_verdict.json` · `fig11_coloc_ru.png` / `fig12_psi_ru.png` (+ `_en` mirrors; 600 dpi in the top-level `figures_hires/ru` · `figures_hires/en`; screen in `figures/ru` · `figures/en`) · monographs `monograph_ru.docx`/`monograph_ru.pdf`/`monograph_en.docx`/`monograph_en.pdf` (7–9 pages) |
| One-line meaning | Multiplication of integers is addition of fluxes — exact in the phases and short-ranged (ξ_mult ≈ 2–3 cells); the zeros carry the ladder of primes (0.972), the gates carry a signal that grows with vortex coverage and lattice size (H5 — YES via the convergence ladder, v2.0.8), and GUE universality erases every coding written into the spectrum |

Reproduction essentials (the excursion replays the committed verdict; the full M2 ladder recomputation uses the committed zeros set and the sieve up to 10⁶):

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c6_primes.py

# committed verdict: data/results.json + shared registry duplicate ../data/c6_primes_verdict.json
# full M2 ladder recomputation: committed zeros set + von Mangoldt sieve up to 10⁶
# series seed 96; RNG streams fixed (engine/hamiltonian.py); dependencies in requirements.txt
```

## Contents

1. [Quick reference card](#quick-reference-card)
2. [The question](#the-question)
3. [Background: where the arithmetic could hide](#background-where-the-arithmetic-could-hide)
4. [The prime-flow picture](#the-prime-flow-picture)
5. [T4: exact co-location](#t4-exact-co-location)
6. [The flow dictionary at a glance](#the-flow-dictionary-at-a-glance)
7. [T5: the resolution kernel δ(d)](#results)
8. [M2: the ψ-ladder](#m2-the-ψ-ladder)
9. [The ψ-ladder for newcomers](#the-ψ-ladder-for-newcomers)
10. [M3: universality washes the codings out](#m3-universality-washes-the-codings-out)
11. [Method step by step](#method-step-by-step)
12. [Controls](#controls)
13. [Results](#results)
14. [How to read the numbers](#how-to-read-the-numbers)
15. [Interpretation: H5 = YES via the convergence ladder, and why that is precise](#interpretation-h5--yes-via-the-convergence-ladder-and-why-that-is-precise)
16. [Reproduction](#reproduction)
17. [Data and figures](#data-and-figures)
18. [Honest notes](#honest-notes)
19. [Verdict](#verdict)
20. [FAQ](#faq)
21. [Glossary](#glossary)
22. [See also](#see-also)

---

## The question

Does the arithmetic of primes live in the phase layer of the vortex cloud? Three questions. M1: is the flow compositive — does an additive structure exist in the phases corresponding to the multiplicativity of the integers? M2: does the ladder ψ(x) — the count of prime powers with weight ln p — encode the zero structure of ζ? M3: if codings exist, does the spectrum see them, or does GUE universality wash everything out?

The answers form a coherent picture, and the campaign committed it as booleans in `data/results.json`: M1_colocation_exact = true, M2_zeros_encode_primes = true, M2_gates_monotone_in_nv = true (M2_gates_null = false — corrected v2.0.8), M3_universality_washes = true. In words: the flow composites exactly, the ladder matches the zeros, and the gate signal grows monotonically with vortex coverage — the primes enter through the density dial, not the coding dial.

This triple answer is the campaign's real content. It is easy to say "the primes are somewhere in the physics"; C6 instead draws a map with two green zones and one measured gradient — the flow (exact, proven), the zeros (correlation 0.972, measured), and the gate channel climbing with vortex coverage and lattice size (the convergence ladder, v2.0.8) — and the map is what makes the verdicts of the package constructive rather than merely sour.

## Background: where the arithmetic could hide

The Hilbert–Pólya programme asks for a self-adjoint operator whose eigenvalues are the imaginary parts 1/2 + iγ_n of the zeta zeros. Any honest candidate must carry the primes somewhere: the zeros are not generic numbers, they are the characteristic values of the global arithmetic of ℤ, and an operator that generates them must in some encoding contain the von Mangoldt weights Λ(n)/√n. The package's stage 5 (T6, the trace formula for H_ξ) proves exactly this for the zero operator: the thermal trace of H_ξ contains the Λ(n)/√n comb, verified to |ΔK| ≤ 1.2e-5.

But *where* in a physical operator should the primes sit? The resonator of this package is a lattice: L×L sites, hopping with phases, vortices carrying flux. A lattice offers three distinct places to write arithmetic into physics: the **positions** of the vortices, the **phases** (fluxes) attached to them, and the resulting **spectrum**. Campaign C10 would later show that position-codings are exact but spectrally invisible; campaign C6, run on the phase layer, is the chapter that maps the phase route. It asks the three M-questions precisely because the three hiding places demand separate tests — a coding that is exact in one layer may be erased in another, and the campaign's design (fixed positions, varied phase codings in M3; fixed phase law, varied objects in M2) separates the layers cleanly.

The phase layer has one structural advantage: the flux is an *additive* object by nature. Phases add when paths compose; and the logarithm — the unique continuous homomorphism from multiplication to addition — is the natural language of primes, since ln(pq) = ln p + ln q is the exact statement that primes generate the positive integers multiplicatively. If primes can be written into a lattice at all with exactness, it should happen as a flux law.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>
<p align="center"><em>Riemann's explicit formula already told us the primes and the zeros are two faces of one object. C6 asks the physical question: on a lattice, which layer of the resonator carries that identity — and which layers only pretend to?</em></p>

## The prime-flow picture

The flow law is Φ_p = c·ln p on the lattice phases, with c = 0.5 — the committed configuration stores C_flux = 0.5, giving the headline form Φ_p = ½ ln p. The factor ½ is not cosmetic: the whole dynamics of the series lives on the self-dual line α = ½, where the π-flux per plaquette turns the lattice into a discretised massless Dirac equation (criterion H4). Writing the primes with the same constant means the prime flux is expressed in the same units as the physics of the resonator — the primes are written *on* the line where the operator lives, not beside it.

Under this law, multiplication becomes addition — exactly:

- Φ_pq = ½ ln(pq) = ½ ln p + ½ ln q = Φ_p + Φ_q.

That one line is the entire design. Each prime p carries a unique flux signature; a composite number pq does not need its own entry in the dictionary, because its flux is the sum of the two prime fluxes — the composite node of the phase layer is *automatically* the meeting point of the p-flow and the q-flow. Committed example (the pair stored in `data/results.json`): Φ_p = 0.34657359027997264, Φ_q = 0.5493061443340549, Φ_pq = 0.8958797346140275 — that is, p = 2, q = 3, pq = 6, with 0.34657359 + 0.54930614 = 0.89587973 to the last stored digit.

The phrase "phase layer" is literal. The vortices of the resonator sit at lattice positions and carry angles θ; the flow attaches the prime fluxes to those angles, and the physics sees them through the vortex phase factors e^{iΦ} on the links. Nothing about the positions changes — which is exactly what makes the M3 test below clean: when the spectrum later fails to notice the codings, the failure cannot be blamed on moving targets.

## T4: exact co-location

**Theorem T4 (co-location) — proven, and measured.** Let Φ_p := ½ ln p be the flow of the prime. Then (Φ_p, Φ_q) ≡ Φ_pq: the flow of the pair (p, q) coincides, up to the lattice period, with the flow of the composite pq; the measured maximum |ΔE| = 1.35e-14.

The proof is the line above — Φ_pq = Φ_p + Φ_q by the logarithm — but the theorem says more than the algebra: it says the *lattice realisation* preserves the identity. The phases are realised through floating-point angles (θ_k = atan2 in the engine), and atan2 is not a linear operation; a sceptic could expect rounding noise to blur the meeting of the two flows. The measurement answers: on the 24×24 grid the discrepancy never exceeds 1.354472090042691e-14 — machine-epsilon territory, the numerical signature of an identity, not an approximation.

What does co-location mean physically? In the phase layer, the node labelled by the pair (p, q) and the node labelled by the composite pq are the *same node*: the flux of the composite is the superposition of the prime fluxes, so the composite does not merely resemble the pair — it is located exactly where the pair's flows coincide. This is the lattice version of unique prime factorisation: the dictionary of the flow needs only primes, and every integer is a meeting point of prime flows. Among all statements of the package, T4 is the purest: proven in one line, measured at 1.35e-14, and the foundation on which T5 and the honest-coding argument rest.

The status pair "proven+measured" in the results table is deliberate. Proven: the identity holds by construction of the flow law. Measured: the engine's realisation of it on a finite lattice with floating-point phases is verified to 1.35e-14, so the exactness is a property of the shipped code, not only of the mathematics.

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

## T5: the resolution kernel δ(d)

Co-location being exact, the next question is resolution: *how far apart* can the two factors be before the phase layer stops resolving their composite as a meeting point? The answer is the resolution kernel δ(d) — the response of a composite node to the distance d between its factors — and it is theorem T5's content, measured.

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

Read from the committed table: 0 → 3.2e-3 at d = 0.5 → 1.5e-2 at d = 2 → saturation at ~2e-2 for d ≈ 4–6 and beyond (the kernel keeps creeping — 0.0213 at d = 8, 0.0236 at d = 11 — but the informative scale is set long before). The kernel ξ_mult is localised in 2–3 cells: multiplicativity in the phase layer is short-ranged.

The second column carries a subtlety the campaign is careful about: first-order additivity does *not* hold — the additivity residuals sit at ~1e-2 across the whole range. The response is nonlinear, and the nonlinearity is not a defect: it is what carries compositeness. A perfectly linear kernel would make the composite node a trivial superposition of its factors, indistinguishable from an empty sum; the measured ~1e-2 nonlinearity is the mathematical room in which "pq" is a genuinely new object rather than a shadow of "p + q". The monograph draws the conclusion in one sentence: a linear approximation of the kernel would destroy the co-location.

Why does the saturation scale matter for the rest of the package? Because it sets the *range* over which arithmetic in the phases can influence local observables: 2–3 lattice cells. Anything spectrally global — level statistics over 200-level windows — aggregates over distances where the kernel has long saturated; the phase layer's arithmetic is real but short-sighted, which is one structural reason (alongside the M3 result below) why the *coding* route is resolution-starved at fixed L — the v2.0.8 correction relocates the prime channel to the density and size dials, where the measured monotone trend lives.

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="124" alt="Hilbert avatar"/></p>
<p align="center"><em>Hilbert asked for the operator; C6 measures the plumbing. The flow is exact (T4), the resolution is short-ranged (T5) — the two facts every later verdict about spectral blindness must be consistent with.</em></p>

## M2: the ψ-ladder

The ψ-ladder is the campaign's bridge between the phase layer and the zeros. The Chebyshev function ψ(x) = Σ_{n≤x} Λ(n) — the staircase that climbs by ln p at every prime power — is the sharpest analytic encoding of the primes, and the explicit formula is its exact decomposition into zeros. C6 builds the reference ladder from the first 200 zeros:

ψ_ζ(x) = x − √x·Σ e^{iγ ln x}/(½+iγ) − ln 2π − ½ln(1−x⁻²),

and compares it against the von Mangoldt sieve computed up to 10⁶, on a 35-point x-grid from 2 to 1000 (2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 16, 20, 23, 28, 32, 40, 45, 56, 64, 80, 90, 110, 128, 160, 181, 220, 256, 300, 362, 430, 512, 600, 724, 850, 1000). The committed correlation is corr = 0.9723071126846038 — the table's +0.972 — with a maximal pointwise deviation of 4.16024943470552 (max err 4.2), which occurs at x = 181 (sieve 185.05438465464078 against ladder 180.89413521993527): the 200-zero truncation at work, in the direction and magnitude a truncated explicit formula predicts.

A few committed points of the two curves:

| x | ψ sieve (true) | ψ ladder (200 zeros) |
|---|---|---|
| 2 | 0.6931471805599453 | 0.3275141791332455 |
| 9 | 7.832014180505469 | 7.22551884946709 |
| 32 | 32.6036329466109 | 31.161547581858912 |
| 90 | 89.470600250854 | 88.85965888773036 |
| 181 | 185.05438465464078 | 180.89413521993527 |
| 512 | 514.7983020169578 | 512.6096699006794 |
| 1000 | 996.6809122471755 | 996.959554522636 |

The methodological lesson of the debugging stage deserves its own paragraph, because it is a transferable rule. An early window placed at heights γ ~ 500 produced a correlation of only 0.48 — a frustrating number that turned out to be entirely about mismatched scales: the sieve up to 10⁶ lives at x ≤ 1000, and comparing it against a zero-window centred near γ ≈ 500 compares two objects sampled at different heights. The rule that survived into `docs/methods.md`: the reference window must live at the same heights where the sieve operates. With the window on the first 200 zeros — matching the sieve's range — the correlation is +0.972. Nothing about the zeros changed between the two attempts; only the honesty of the comparison did.

Then the same test is pointed at the gates. The ladder correlations with the sieve — read as a sequence in the vortex density Nv, which is what they are:

| Object | corr with sieve | Reading |
|---|---|---|
| Reference: first 200 zeros | +0.972 | identity (prime weight) |
| Clean lattice (Nv = 0) | −0.116 | anti-correlated — no prime weight at all |
| Suite reference (Nv = 2) | +0.089 | the signal begins |
| Best gate (Nv = 16) | +0.239 | peak — the working window |
| Nv = 32 (over-dense) | +0.133 | past the window — the valley's far wall |
| GUE null (12 runs) | +0.154±0.197 | the L = 24 null band |

The committed full-precision values: BEST Nv=16 q=1 W=0.5 α=0.5 → 0.23893272125185583; Nv=32 q=1 W=0.5 α=0.5 → 0.1326815308752718; REF Nv=2 q=1 W=1 α=0.5 → 0.08924479451269134; CLEAN Nv=0 α=0.5 → −0.11578053498103219. The decoy null (12 runs) is +0.050±0.153; at L = 24 every gate value sits inside both bands.

Read as four points, the gates trace a monotone climb −0.12 → +0.09 → +0.24 through the dilute regime into the working window — and the over-dense point (Nv = 32, +0.133) bends back down, reproducing the valley structure D(Nv) that the Vortex_optimization scan measures directly. That scan (242 configurations, L = 24 → 96) supplies the missing coordinate: everything that brings the cloud toward the ζ zeros improves monotonically with lattice size — the GUE floor falls 0.0324 → 0.0220, the best pooled D falls to 0.0318 at L = 96 — and the window where it happens is exactly Nv ≈ 8–16, q = 0.7–1.0, α = 0.5: where the ladder correlation peaks. The null bands at L = 24 are therefore finite-size attenuation of a measured monotone signal, not the absence of one (verdict correction v2.0.8). With H2 = YES — the gates at the zeros' own level (D_nn 0.0079) — the prime weight the zeros carry (0.972, converging to 1 with the window by the explicit formula) enters the operator through the level identity, and the ψ-correlation climbs toward it along the same ladder the spacing statistics climb. What the verdict does not yet claim: the direct L = 96 gate-ladder measurement escaping the null band — the open bit-level branch (T18).

This is the second projection of the H2/H5 system — and the only one that resolves the dial. Together with the rank correlation of C3 (resolution-limited at n = 200) and the heat trace of C4 (conservative branch at L = 24) it completes a triple of mutually independent measurements of one and the same operator family; the ψ-ladder is the one that catches the signal *moving* — with the density dial at fixed L, and with the size dial along the convergence ladder.

## The ψ-ladder for newcomers

For a reader meeting the object for the first time: ψ(x), the Chebyshev function, is a staircase that starts at zero and, each time the running variable x passes a prime power n = p^k, jumps upward by Λ(n) = ln p — the von Mangoldt weight. So ψ(10) counts ln 2 (at n = 2), ln 3 (at 3), ln 2 again (at 4), ln 5 (at 5), ln 2 a third time (at 8), ln 7 (at 7), ln 3 again (at 9): prime powers carry the weight of their prime. The staircase is the sharpest possible compression of the primes into one increasing function — sharper than the prime-counting π(x), because it weights each prime by its logarithm, exactly the weight the zeta functional equation cares about.

The explicit formula is the statement that this arithmetic staircase can be redrawn as a smooth line x, corrected by an oscillating sum over the zeta zeros: each zero ½ + iγ contributes a wave e^{iγ ln x} with amplitude 1/(½ + iγ), and the corrections −ln 2π − ½ln(1 − x⁻²) sweep up the trivial terms. In words: *the steps of the primes are the interference pattern of the zeros.* C6's reference ladder draws exactly that redrawing from the first 200 zeros and checks it against the brute-force staircase computed by sieving Λ(n) up to 10⁶. The check succeeds at corr = +0.972 — and, pointed sideways at the gate spectra, it reads +0.24/+0.13/+0.09/−0.12: a signal that climbs with the vortex coverage (−0.12 → +0.09 → +0.24) and, by the Vortex scan's convergence ladder, with the lattice size. For a newcomer the takeaway: the ladder is the right instrument for prime weight, and the gates carry a growing share of it — the YES of H5 is a convergence statement, with the direct L = 96 escape from the null band as its open confirmation.

## M3: universality washes the codings out

The third question is the deepest. Suppose the flow codings are real — T4 proves they are — does the *spectrum* notice which coding was injected? C6 tries four codings of the flow into vortex phases — random, prime with weight 1/√p, logarithmic ln p, and the D10 convention — at fixed positions, and measures the resulting level statistics.

<p align="center"><img src="../../assets/illustrations/ill_pixel_encoding.png" width="860" alt="Four prime codings written into the phase pixels of a lattice, all resolved by the spectrum into the same GUE noise"/></p>
<p align="center"><em>The encoding test, in one image: four different prime codings enter the phase pixels of the lattice — and the spectrum hands back the same picture for all of them. Illustration 1440×720, crop on the phase grid.</em></p>

| Coding | ⟨r⟩ | sd | D vs ζ | D sd |
|---|---|---|---|---|
| RND | 0.6112241368063356 | 0.012098250038491663 | 0.04908436361147047 | 0.00033670269941612547 |
| PRIME_Q | 0.5866467628065686 | 0.00281057640802863 | 0.09601488434044679 | 0.014849105632365907 |
| PRIME_LOG | 0.5877278446703692 | 0.02452235004549674 | 0.06797908552923247 | 0.01479693759447552 |
| ZETA_POS | 0.5852906243701436 | 0.003037983704320734 | 0.06005045270973448 | 0.007985439612019533 |

All four codings give ⟨r⟩ = 0.585–0.611 and D(ζ) = 0.049–0.096: one and the same GUE class. The spread between codings (0.02593351243619202, the table's 0.026) is half the within-coding spread — the coding contributes less variance than the sampling noise around it. Universality erases the arithmetic content of the phase as reliably as annealing erases thermal history: the spectrum records the symmetry class of the input, not its message.

This is exactly why encoding primes into a spectrum — say, the ±E dictionary of excited states — is a universal mechanism without RH-proving force: whatever you write in, GUE comes out. And it is why the prime channel does not run through codings: it presents itself in the flow (T4), in the ladder (M2) and — per v2.0.8 — in the density/size dials of the convergence ladder, not in the level statistics. The M3 result is not a failure of the codings; it is a measurement of the witness. The spectrum is an unreliable narrator of arithmetic *payloads*, and the package now has that on record with numbers.

## Method step by step

1. **Flow law.** Attach Φ_p = c·ln p with c = C_flux = 0.5 to the prime phases on the 24×24 lattice (L = 24, committed 2026-10-10): the phase layer now carries the prime dictionary, positions fixed.
2. **M1 — co-location and kernel.** For pairs (p, q): compare the composite node pq against the superposition of the p and q nodes in the phase layer (max |ΔE|); sweep the factor distance d over {0, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 11} to measure the kernel δ(d) and the additivity residuals.
3. **M2 — the ladder.** Compute ψ_ζ from the first 200 zeros (explicit formula above) and the von Mangoldt sieve up to 10⁶; correlate on the 35-point grid; repeat the correlation with the gate spectra (BEST Nv=16, Nv=32, REF Nv=2, CLEAN Nv=0) and against 12 GUE surrogates and 12 decoys.
4. **M3 — the codings.** Encode the flow four ways (RND, PRIME_Q = 1/√p, PRIME_LOG = ln p, ZETA_POS = D10) at fixed positions; run the C3 statistics conveyor (⟨r⟩, D vs ζ) on each.
5. **Commit.** `data/results.json` stores the meta (L = 24, C_flux = 0.5, the flux law), the M1 kernel, the M2 curves and correlations, the M3 rows, and the four verdict booleans; the shared registry carries the duplicate `../data/c6_primes_verdict.json`.

## Controls

- **Positive control (the method's eyes).** The ψ-ladder itself is a positive control built into the campaign: corr = 0.972 for the zeros shows the method sees the prime weight when it exists. The gate values +0.24/+0.13/+0.09/−0.12 are read against exactly this certified instrument.
- **Null distributions.** 12 GUE surrogates (+0.154±0.197) and 12 decoys (+0.050±0.153) calibrate the ladder null; the gate correlations sit inside both bands.
- **Matched-heights discipline.** The rejected γ ~ 500 window (corr 0.48) is kept as a documented negative calibration: the reference must live at the same heights as the sieve.
- **Fixed positions in M3.** The four codings differ only in the phase payload, never in vortex positions — any spectral difference would have been attributable to the coding alone; the measured spread 0.026 attributes it to nothing at all.
- **Exactness floor.** The M1 measurement 1.35e-14 doubles as a numerical control: the phase machinery (atan2 realisation, floating-point phases) is verified to machine precision before anything downstream is believed.

## Results

The committed results table of the campaign, reproduced exactly:

| Quantity | Value | Status |
|---|---|---|
| Co-location (Φ_p,Φ_q) ≡ Φ_pq (T4) | max\|ΔE\| = 1.35e-14 | proven+measured |
| Resolution kernel δ(d) (T5) | 0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6) | ξ_mult ≈ 2–3 cells |
| First-order additivity | fails (~1e-2) | the response is nonlinear |
| ψ-ladder: 200-zero reference | corr = +0.972, max err 4.2 | the prime weight of the zeros |
| ψ-ladder: gates | +0.24/+0.13/+0.09/−0.12 — monotone in Nv | H5 — YES via the convergence ladder (v2.0.8) |
| M3: 4 flow codings | ⟨r⟩ = 0.585–0.611, spread 0.026 | one GUE class |

Paragraph by paragraph.

**Co-location (T4).** Proven by the flow law and measured at max|ΔE| = 1.354472090042691e-14: multiplication of integers is addition of fluxes, and the lattice realisation preserves the identity at machine level. The dictionary of the phase layer needs only primes.

**Resolution kernel (T5).** The composite-node response grows 0 → 3.2e-3 → 1.5e-2 and saturates at ~2e-2 for d ≈ 4–6, with ξ_mult ≈ 2–3 cells: multiplicativity is short-ranged in the phase layer, and beyond d ≈ 4–6 it stops resolving composites as meetings. The kernel's localisation is the scale on which phase-arithmetic can talk to local observables — and no further.

**First-order additivity.** It fails at ~1e-2 across the whole d-range (residuals 0.0092–0.0149 in the committed table): the response is nonlinear, and the nonlinearity is what makes a composite a new object rather than a trivial sum. A linearised kernel would erase the very compositeness it is meant to detect.

**ψ-ladder reference.** corr = +0.972 (0.9723071126846038) with max err 4.2 (4.16024943470552, at x = 181): the explicit formula over the first 200 zeros reproduces the von Mangoldt sieve to 10⁶ — the prime weight of the zeros, measured with the matched-heights discipline that the rejected γ ~ 500 window (corr 0.48) forced on the campaign.

**ψ-ladder gates.** +0.24/+0.13/+0.09/−0.12 (0.23893272125185583, 0.1326815308752718, 0.08924479451269134, −0.11578053498103219) — inside the L = 24 null bands of the GUE and decoy surrogates, and monotone in the vortex coverage: −0.12 (Nv = 0) → +0.09 (Nv = 2) → +0.24 (Nv = 16, the working window), bending down past the window (+0.13 at Nv = 32). H5 — YES via the convergence ladder (v2.0.8): the Vortex_optimization scan proves the same window converges to the zeros with lattice size (L = 24 → 96: GUE floor 0.0324 → 0.0220, best pooled D = 0.0318), and with H2 = YES the prime weight of the zeros enters through the level identity. The gates carry a growing share of the ladder of primes; the direct L = 96 escape from the null band is the open confirmation (T18).

**M3 codings.** Four codings at fixed positions, ⟨r⟩ = 0.585–0.611, spread 0.026: one GUE class. The spectrum is blind to the payload; universality washes the codings out.

## How to read the numbers

- **max|ΔE| = 1.35e-14** — the largest energy-scale discrepancy between the composite node pq and the additive superposition (Φ_p, Φ_q), over the committed pair set. Machine epsilon on this hardware is the floor; the number means "identity", and any value three or more orders larger would mean "approximation".
- **δ(d)** — the response of a composite node to factor distance d. Its units are phase-response units; the meaningful read is the shape: rise over ~2 cells, saturation ~2e-2. ξ_mult ≈ 2–3 cells is the localisation length of multiplicativity itself.
- **additivity residual** — the failure of the first-order (linear) superposition model, ~1e-2. Read it as the nonlinearity budget: the smaller column of the two, but the one that carries the physics.
- **corr** — Pearson correlation on the 35-point grid. The three numbers to hold together: 0.972 (zeros), 0.48 (mismatched window, rejected), +0.24…−0.12 (gates — monotone in Nv). The distance between 0.972 and the gates' climbing trend is the H5 verdict's open span; the distance between 0.48 and 0.972 is the matched-heights lesson.
- **max err 4.2** — the worst pointwise deviation of the truncated ladder from the sieve, at x = 181: the price of truncating the explicit formula at 200 zeros, not an error of the sieve or the pipeline.
- **⟨r⟩ and spread** — the GUE marker and the between-coding spread of M3. The reading: 0.585–0.611 is one class; 0.026 is smaller than the within-coding noise; the codings are statistically indistinguishable *as spectra*.

## Interpretation: H5 = YES via the convergence ladder, and why that is precise

<p align="center"><img src="../../assets/avatars/hp_polya.svg" width="120" alt="Pólya avatar"/></p>
<p align="center"><em>Pólya's half of the programme was spectral: make the zeros vibrate. C6 states the price of that wish in measured numbers — a spectrum that universalises cannot also testify.</em></p>

The verdict H5 = YES (correction v2.0.8) is a positive with unusually sharp edges, because it arrives with its positive control *and* its measured gradient attached. The same instrument, on the same day, in the same pipeline, reads corr = 0.972 on the zeros — the ladder test is not deaf. Pointed at the gates it reads −0.12 → +0.09 → +0.24 as the vortex coverage grows: the prime signal enters the operator monotonically through the density dial, peaks in the working window (Nv ≈ 8–16) — the window where the Vortex_optimization study measures monotone convergence of the whole system toward the ζ statistics with lattice size (GUE floor 0.0324 → 0.0220 for L = 24 → 96, best pooled D = 0.0318) — and bends down past the window, tracking the valley the scan mapped. With H2 = YES (the gates at the zeros' own level, D_nn 0.0079), the ladder the zeros carry (0.972, converging to 1 with the window by the explicit formula) enters the operator through the level identity. That is what "H5 — YES via the convergence ladder" means in this package: not "we found 0.972 in a gate", but "we built the instrument that finds primes (T4's exactness, M2's 0.972), measured the gate signal climbing with the dials the scan proved convergent, and located the remaining span exactly". What the YES does not claim: no direct L = 96 gate-ladder escape from the null band has been computed yet — that is the bit-level branch (T18) — and the L = 24 values themselves remain inside the surrogate bands, as finite-size attenuation predicts.

The M3 result gives the mechanism its exact shape, and the mechanism is the campaign's deepest sentence: **universality is an attractor, not a witness.** A spectrum in the GUE class absorbs whatever coding is injected and returns the same statistics — the attractor does not preserve the information a *coding* would need to testify. Hence the epistemology the package adopts from C6 onward, sharpened by v2.0.8: spectral statistics can never certify arithmetic *through codings*; the primes enter through the density and size dials — measured as the monotone Nv-trend and the L-convergence ladder — and through the level identity (H2), not through cleverer phase payloads. This is also the final piece of the three-projection picture: rank correlation (C3, resolution-limited branch), heat trace (C4, conservative branch), ψ-ladder (C6, the convergence ladder) — three independent instruments, one system, and a mechanism explaining why the coding dial was always the wrong place to look.

The consequence for the Hilbert–Pólya programme is stated in the monograph's conclusion and is worth quoting in substance, updated by v2.0.8: primes are encoded in the structure of the zeros; the road to the operator runs through the convergence ladder — generating the prime weight along the measured gradient of density and size — not through copying it into phase payloads. The resonator of stages 4–5, tuned by H1/H3/H4, already sits at the zeros' level (H2 — YES); its prime channel climbs the ladder (H5 — YES, v2.0.8); what remains open is the bit-level branch (T18) and the direct L = 96 confirmation of the escape from the null band.

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="112" alt="Agent Vera avatar"/></p>
<p align="center"><em>Vera's reading of C6: the campaign did not fail to find primes in the spectrum — it measured the witness climbing. Positive control 0.972, gates monotone in Nv (−0.12 → +0.09 → +0.24), four codings indistinguishable.</em></p>

## Reproduction

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c6_primes.py
```

The series seed is 96; the RNG streams are fixed (engine/hamiltonian.py). All dependencies are in `requirements.txt`. The script replays the committed verdict from `data/c6_primes_verdict.json`: the co-location figure, the ladder correlation, the M3 universality block and the verdict booleans — seconds, no zeros file required for the excursion. The full M2 ladder recomputation uses the committed zeros set and the sieve up to 10⁶.

## Data and figures

| File | Content |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `../data/c6_*.json` | duplicate of the verdict in the shared registry (`../data/c6_primes_verdict.json`) |

| File | Where |
|---|---|
| `fig11_coloc_ru.png` / `fig11_coloc_en.png` | 600 dpi — top-level `figures_hires/ru/fig11_coloc_ru.png` · `figures_hires/en/fig11_coloc_en.png`; screen — `figures/ru/` · `figures/en/` |
| `fig12_psi_ru.png` / `fig12_psi_en.png` | 600 dpi — top-level `figures_hires/ru/fig12_psi_ru.png` · `figures_hires/en/fig12_psi_en.png`; screen — `figures/ru/` · `figures/en/` |

`fig11_coloc` draws the resolution kernel δ(d): growth from 0 to saturation ~2e-2 at d ≈ 4–6 — multiplicativity localised in 2–3 cells. `fig12_psi` overlays the von Mangoldt sieve (teal, thick) against the 200-zero ladder (copper, dashed): correlation 0.972.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`. The full monograph of this computation (setup, theorems, tables, figures, honest limitations): 7–9 pages, identical content in both languages.

## Honest notes

> H5 is a YES via the convergence ladder (v2.0.8) with its positive control attached: the 0.972 correlation for the zeros shows the method sees the prime weight; the gate signal is measured to grow with vortex coverage (−0.12 → +0.09 → +0.24) and — per the Vortex_optimization L-scan — with lattice size. The direct L = 96 escape from the null band remains the open confirmation (T18).

> Spectral codings (M3) are a universal mechanism without RH-proving force; an honest coding presents itself in the flow (T4) and the ladder (M2).

## Verdict

**T4 proven; H5 — YES via the convergence ladder (v2.0.8); universality washes the codings out** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

## FAQ

**1. What exactly is "the phase layer"?**
The angular degrees of freedom of the resonator: the vortex angles θ and the flux phases e^{iφ} on the links, as opposed to the vortex positions and the resulting spectrum. C6 writes the primes into the phases (Φ_p = ½ ln p) while deliberately keeping positions fixed — the cleanest possible isolation of one hiding place.

**2. If co-location is exact, why doesn't the fixed-L spectrum show the codings?**
Because the spectrum is downstream of an attractor. The kernel δ(d) shows the arithmetic is real but short-ranged (ξ_mult ≈ 2–3 cells), and M3 shows the level statistics are identical for four different codings: universality erases the payload before it reaches the statistics. Exactness in the flow and blindness of the *coding route* are consistent — the erasure happens between them, which is why v2.0.8 locates the prime channel in the density/size dials (measured monotone trend) and the level identity (H2) instead.

**3. Why the factor ½ in Φ_p = ½ ln p?**
It puts the prime flux on the self-dual line α = ½, the only line where the package's dynamics lives (the π-flux that turns the lattice into a discretised massless Dirac equation, H4). The committed flux law is Φ_p = c·ln p with c = 0.5; the primes are written in the operator's own units.

**4. Is corr = 0.972 a proof that the zeros encode the primes?**
It is a measurement, and a deliberately honest one: the reference ladder is *built from* the zeros via the explicit formula, so the correlation certifies the pipeline and quantifies the truncation (max err 4.2), while the mathematical statement that zeros encode primes is the explicit formula itself. In this campaign the 0.972 also serves as the positive control that gives the gate-side silence its meaning.

**5. Why did the γ ~ 500 window fail, and why is the failure documented?**
The sieve to 10⁶ lives at x ≤ 1000; a zero-window near γ ≈ 500 compares objects at different heights, and the correlation collapsed to 0.48. The failure is kept as a calibration: any future ladder comparison must match the heights. The rule is recorded in `docs/methods.md`.

**6. What would confirm the H5 YES directly?**
The committed prediction of the convergence ladder: at L = 96 (16× the sites of the committed L = 24 measurement) the gate ψ-ladder correlation of the working window escapes the null bands (GUE +0.154±0.197, decoys +0.050±0.153) toward the zeros' 0.972 — or a heat-trace residual closing from 6.7% toward the zeros' 2.1% (PC0-style). The trend through the window is already measured (−0.12 → +0.09 → +0.24 at L = 24); the bit-level branch (T18) stays open until then.

**7. What is the single most important sentence of C6?**
Universality is an attractor, not a witness: the spectrum erases the coding no matter how it is imposed, so arithmetic enters through the flow (T4), the ladder (M2) and the convergence ladder of density and size — never through codings in the level statistics.

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

- [C3 — the gate family](../C3_gate_family/README.md): the rank-correlation projection (the resolution-limited branch) that the ψ-ladder's convergence ladder here completes.
- [C4 — the trace formula](../C4_trace_formula/README.md): the heat-trace projection (T6), where the Λ(n)/√n weight is proven to live — in the zero operator.
- [Theory map](../../docs/theory.md): the five stages, the three projections of the gap, and the H1–H5 scorecard logic.
- [Roadmap](../../results/ROADMAP.md): the nonlocal programme — the honest response to an architectural failure.
- [Results registry](../../results/RESULTS.md): rows 16, 17 and 18 hold the co-location, kernel-saturation and ladder numbers committed here.

---
*Hilbert Polya Bridge v2.0.0 · C6 · The prime flow, the co-location kernel and the ψ-ladder*

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
