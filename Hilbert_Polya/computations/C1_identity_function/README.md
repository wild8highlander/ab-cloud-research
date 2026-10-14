# C1 · The identity function and the Γ-ladder

![version](https://img.shields.io/badge/version-2.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_critical_line.png" width="720" alt="The critical line: the identity function Z_id assembled from the Γ-ladder closures"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

*Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra ran the spectral pipeline, Agent Vera executed independent verification.*

> **Assembling the identity function Z_id(t) = e^{iθ(t)}ζ(½+it) from the algebraic closures of the Γ-frame; criteria K1–K4, K7; one honest refutation — the single modulus on the line is not elementary.**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Campaign | **C1 · The identity function and the Γ-ladder** — stages 1–2 of the five-stage map (algebra → graph), seeding stage 3 |
| Claim | assemble, on the critical line, a function whose zeros coincide with those of ζ **without using any zero data** — only elementary identities of the Γ-frame and ζ itself: Z_id(t) = e^{iθ(t)}ζ(½+it), real on the line and even in t |
| Verdict | composite verdict K1–K4, K7: **PASS (one refutation published)** — T1 *proven* (dps = 40; plus one honest refutation), T2 *proven*, K3 *confirmed*, K7 *reproduced* (informational) |
| Γ-ladder closures (K1) | residuals 1.27–2.59e-39 on a 401-point grid at dps = 40, threshold 1e-30 — nine orders of margin |
| Honest refutation | the single modulus \|Γ(¼+iu)\| on the line has no elementary form — structural mismatch 0.765 ≠ 1, "the line where the ladder stops closing" |
| Reality of Z_id (K2, T2) | max\|Im Z_id\| = 4.9e-29; thresholds 1e-20 (`results.json`) and 1e-25 (validation register); evenness deviation 9.856237674189225e-29 |
| Zeros (K3) | 79 of 79 on [0, 200] against the internal mpmath reference; max\|Δγ\| = 2.8e-14 (float64 comparison floor ≈ 2⁻⁴⁵) |
| Counting (K4, T3) | exact integers 3, 10, 29, 79 at the occupied probes; residuals ≤ 4.9e-28; `rh_in_block_pass` at all five probes |
| Gram points (K7) | 220 points, 4 sign violations — the classical exceptions (n = 126, 134, 195, 211) |
| Discipline | `free_parameters: 0` — nothing fitted; series seed 96; deterministic; runtime about two seconds |
| Key artifacts | `data/results.json` · `data/curve_Zid.npz` · `../data/c1_*.json` · `fig01_zid.png` + `fig02_gamma_ladder.png` (+ `_en` variants) · monographs ru/en in docx + pdf (7–9 pages) |
| External inputs | none — no external zero file needed; every criterion compares internally |
| One-line meaning | the algebraic envelope does not generate zeros — it merely wraps ζ in a smooth phase; whatever is true of Z_id is true by identity, and whatever Z_id cannot do, no rearrangement of the phase can do either |

Fastest reproduction (deterministic; the campaign tour runs in about two seconds and needs no zero file):

```bash
# a tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c1_identity.py

# CI guards: Γ-closures at dps = 40 below 1e-35; Z_id reality (K2)
python3 -m pytest tests/ -q

# independent verification: the IVP checks re-derive this campaign's numbers
bash independent_verification/RUN_ALL.sh
```

**About this edition.** This is the definitive English guide to campaign C1 — the single unified edition of this folder. Every number, verdict label, file name, command and threshold is preserved; everything else here is explanation: the mathematics behind the assembly, the reason each control exists, and the place of this campaign in the Hilbert–Pólya programme.

## Contents

1. [Quick reference card](#quick-reference-card)
2. [The question this campaign answers](#the-question-this-campaign-answers)
3. [Background: the five-stage map](#background-the-five-stage-map)
4. [The method, step by step](#the-method-step-by-step)
5. [The positive controls: why honesty requires them](#the-positive-controls-why-honesty-requires-them)
6. [Results](#results)
7. [How to read the numbers](#how-to-read-the-numbers)
8. [Interpretation: what C1 means for H1–H5](#interpretation-what-c1-means-for-h1h5)
9. [Reproduction](#reproduction)
10. [Data and figures](#data-and-figures)
11. [Verdict](#verdict)
12. [FAQ](#faq)
13. [Common misreadings](#common-misreadings)
14. [Glossary](#glossary)
15. [Historical notes on Gram's observation](#historical-notes-on-grams-observation)
16. [Appendix: provenance of every headline number](#appendix-provenance-of-every-headline-number)
17. [See also](#see-also)

---

## The question this campaign answers

<img src="../../assets/avatars/hp_riemann.svg" width="120" align="right" alt="Bernhard Riemann"/>

Can one assemble, on the critical line, a function whose zeros coincide with those of ζ without using any zero data — only elementary identities of the Γ-frame and ζ itself? This campaign answers yes, and that answer is the graph of the whole series: **Z_id(t) = e^{iθ(t)}ζ(½+it)**. But the answer fixes the boundary as well: the algebraic envelope does not generate zeros — it merely wraps ζ in a smooth phase. Whatever is true of Z_id is true by identity; whatever Z_id cannot do, no rearrangement of the phase can do either.

Agent Atlas opened the series here, with the graph rather than the operator: before any candidate Hamiltonian can be judged, the object to be matched must exist, be real, and carry no fitted constants. The campaign delivers exactly that in four moves — **T1 (proven)** the Γ-ladder closures, **T2 (proven)** the reality of Z_id, **K3 (confirmed)** the zero match, **K7 (reproduced)** the classical Gram exceptions — tabulated at a glance in the quick reference card above.

That boundary sentence is worth reading twice, because it is the honest core of the campaign. C1 is not a claim that the Riemann Hypothesis has been defeated by a change of phase; it is the construction of the cleanest possible *target object* — a real, even function whose zeros on the line are exactly the zeros of ζ — together with a measured account of what the construction can and cannot deliver.

**Why the rephasing is legitimate and what it buys.** On the line s = ½ + it the zeta function is complex-valued and its argument wanders. The functional equation, however, ties ζ(½+it) to its own complex conjugate: in the asymmetric form ζ(s) = χ(s)ζ(1−s) the factor χ satisfies χ(½+it) = e^{−2iθ(t)}, where

> θ(t) = Im ln Γ(¼+it/2) − (t/2)·ln π

is the Riemann–Siegel theta on its continuous branch. Substituting gives ζ(½+it) = e^{−2iθ(t)}·conj(ζ(½+it)); multiplying by e^{iθ(t)} yields Z_id(t) = conj(Z_id(t)). The function is **real on the line** — and by the same computation **even in t**. This is exactly the symmetry pattern ξ(s) = ξ(1−s) that the committed verdict cites as ingredient HL-4 (the T04 pattern of the Riemann bilinear relations). The campaign does not assume the conclusion; it measures it: max|Im Z_id| = 4.9e-29 across the scan (criterion K2, Theorem T2).

**Why zeros are preserved.** Because |e^{iθ(t)}| = 1, the rephasing neither creates nor destroys a single zero: the zero set of Z_id on the line is the zero set of ζ there. What the rephasing buys is the right currency for spectral comparison. Eigenvalues of a self-adjoint operator are real, and the crossings of a real function through the zero level can be counted, bracketed and bisected without complex bookkeeping. Z_id is therefore the graph-side object to which every later operator in the package is asked to match — and the phase that makes it real descends directly from the 1859 memoir: the Riemann avatar marks this lineage. The campaign's contribution is not the phase itself but its verified assembly with **zero fitted constants** (`free_parameters: 0` in the committed verdict).

**The three deliverables — and the one refusal.** The campaign proves the three Γ-ladder closures at dps = 40 (Theorem T1); it proves the reality of Z_id on the line (Theorem T2); it demonstrates that the zeros and the Gram interlace come out exactly as classical theory says (K3, K7); and it documents, in the same results table as the passes, the one form that computation refutes — an elementary closed form for the single modulus |Γ(¼+iu)| on the line, missed with structural mismatch 0.765 ≠ 1.

## Background: the five-stage map

<img src="../../assets/avatars/hp_hilbert.svg" width="120" align="right" alt="David Hilbert"/>

The Hilbert–Pólya programme asks a single question — can the nontrivial zeros of ζ be the spectrum of a self-adjoint operator? Hilbert's half of the programme supplies the question; C1 supplies the *object* whose spectrum any candidate answer must reproduce. In the package's five-stage map — **algebra → graph → counting → operator → trace** — C1 owns the first two stations outright and seeds the third:

| Stage | Object | What is proven | What is measured |
|---|---|---|---|
| 1 · Algebra | Γ-ladder: three closures | T1 (dps = 40, ~1e-39) | one refutation (K1) |
| 2 · Graph | Z_id(t) = e^{iθ(t)}ζ(½+it) | T2 (reality) | 79 zeros, Gram (K3, K7) |
| 3 · Counting | argument principle | T3 (pole calibration) | RH in the strip to T = 1000 |
| 4 · Operator | 87 gates of the lattice | — | H2: no relation (surrogate-null level) |
| 5 · Trace | Tr e^{−xH} vs explicit formula | T6 (for H_ξ) | H2 ≈ 1 order in the heat metric |

C1's committed verdict file (`data/results.json`, dated 2026-10-10, working precision dps 30) records the campaign's **assembly card** — which proven ingredients were combined. It is worth reading because it shows that nothing was fitted:

| Ingredient | Source | Content |
|---|---|---|
| HL-1 | T03/V6 | Γ-ladder: Γ(z)Γ(1−z) = π/sin πz ⇒ \|Γ(1/4+it/2)\|² = π/cosh(πt/2) |
| HL-2 | T02 | phase lattice arg P = 2π(ra+sb)/N ⇒ continuous phase θ(t) |
| HL-4 | T04 | Riemann bilinear relations — the symmetry pattern ξ(s) = ξ(1−s) |
| HL-5 | T01 | genus g(N) = (N−1)(N−2)/2 — a level ladder, kept as contrast |
| AC-2 | A6 | counting identity t/δ = N(t) + (t/2π − 7/8) |
| AC-3 | A7 | Σγ² = (T³/6π)(ln(T/2π) − 1/3) |

Assembled from these: **Z_id = e^{iθ(t)}·ζ(1/2+it)** — the real Hardy function (the HL-2 phase over the AC cloud) — and **Xi_id = ξ(1/2+it) = −½(t²+¼)·π^{−s/2}·Γ(s/2)·ζ(s)** with s = 1/2+it, the exact assembly of the completed ξ on the line. The verdict's `free_parameters` field reads 0.

Why must the algebraic stage come first? The honesty discipline of the package — *every constant is derived, none fitted* — has to begin somewhere, and it begins here. The phase θ(t) enters every downstream comparison: the rank-correlation pipeline of C3, the heat-trace projection of C4, the zero-coded operator H_ξ whose trace formula is Theorem T6. If the Γ-identities beneath θ(t) were fitted rather than proven, that fit would silently propagate into every later verdict. The K1 grid at dps = 40 against the 1e-30 threshold is the certificate that the algebra under the phase is exact — and the one honest refutation attached to K1 says precisely where elementary algebra stops: on the line, for the single modulus.

Pólya's half of the programme — the search for the operator — is exactly what C1 refuses to fake. The identity function is the perfect witness precisely because it is not an operator: it has no spectrum beyond its zero set, no eigenvectors, no dynamics. That emptiness is its value. When the later campaigns measure how far the 87 lattice gates sit from spectral identity, the distance is measured against something exact and non-generative, and the measured gap is therefore a clean statement about the gates rather than about the target.

## The method, step by step

The campaign core is `hpbridge/identity.py`; the committed verdict lives in `data/results.json` (duplicated as `../data/c1_*.json` in the shared registry). The pipeline, in order:

1. **The phase θ(t).** `identity.py` evaluates the Riemann–Siegel theta on its continuous branch, θ(t) = Im ln Γ(¼+it/2) − (t/2)·ln π, inside mpmath with ten guard digits above the caller's working precision (the routine raises the context to dps + 10 and restores it afterwards). The guard digits are what allow the last committed digit of every downstream quantity to be trusted.

2. **The Γ-ladder closures (K1).** Three identities are verified on a 401-point grid at dps = 40, each residual taken *relative* and compared with the threshold 1e-30:
   - **|Γ(½+iu)|² = π/cosh πu** — Euler's reflection Γ(z)Γ(1−z) = π/sin πz at z = ½+iu, where sin π(½+iu) = cosh πu (the edge Re s = 1 in the verdict's fields);
   - **|Γ(iu)|² = π/(u·sinh πu)** — the same reflection at z = iu combined with Γ(1−iu) = (−iu)Γ(−iu) (the edge Re s = 0);
   - **|Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu** — Legendre's duplication at z = ¼+iu, closed by the first identity at 2u (the line product).

3. **Assembly in two arithmetics.** Z_id(t) = e^{iθ(t)}ζ(½+it) is computed in mpmath at dps 25–40 inside and delivered in float64 at the interfaces. The crucial discipline: the phase is evaluated at raised precision and multiplied into ζ *before* any rounding to double. An early rounding at t ≈ 50 would leave imaginary debris near the 1e-16 level of float64 — five orders above what K2 in fact measures.

4. **Reality and evenness (K2).** A scan of the line records max|Im Z_id|, an evenness deviation, and the scale of the function at t = 50. The committed numbers: max|Im Z_id| = 4.9281188370946126e-29, evenness deviation 9.856237674189225e-29, scale 0.340735005955025, threshold 1e-20.

5. **Zeros by bisection (K3).** On [0, 200] the real function is sampled on a grid of step max(0.05, T/4000) at dps = 25; every sign change brackets a zero, and **80 bisection refinement steps** shrink each bracket before it is accepted. The 79 zeros found are then compared one-to-one against the internal mpmath reference cache.

6. **The argument-principle block (K4).** The zero count of ξ in the strip 0 < Re s < 2, 0 < Im s < T is evaluated as N(T) = 1 + Δarg/2π along the contour (2,0)→(2,T)→(0,T)→(0,0) with the pole s = 1 taken from above, at integration step 0.02, at five probe heights: T = 10.000000, 27.717867, 51.372077, 100.074523, 199.640031.

7. **Gram points (K7).** The roots of θ(g_n) = nπ for n = 1..220 are found with mpmath `findroot`; the sign of the real function Z_id is recorded at each g_n, and violations of the classical sign alternation are counted.

8. **Determinism and runtime.** The series seed is 96; the RNG streams are fixed (`engine/hamiltonian.py`). The whole campaign is deterministic and runs in about two seconds. The pytest suite guards the same identities in CI: `tests/test_gamma_closures.py` re-runs the three closures at dps = 40 below 1e-35 on u ∈ {0.5, 1.0, 2.0, 3.5}, and `tests/test_zid_reality.py` re-checks K2.

Agent Lyra ran the spectral pipeline that produces this sequence — the same eight steps, in the same order, every rerun — which is why the committed verdict can be re-read in seconds and the fresh recomputation stays optional.

## The positive controls: why honesty requires them

Every criterion in C1 is shaped like a control: a threshold fixed in advance, a measured value, a pass flag, and a provenance note. The rule they serve is stated in `independent_verification/PROTOCOL.md` (rule 2) and in `docs/validation.md`: *a negative verdict is valid only after a positive control by the same method*. C1 is the campaign where the positive side of that discipline is manufactured — it demonstrates exact identities exactly where identity is provable. The five committed criteria at a glance:

| Control | Guards | Threshold | Measured | Status |
|---|---|---|---|---|
| K1 Γ-ladder | exactness of the algebra under θ(t) | 1e-30 (dps 40) | 1.27–2.59e-39 | proven |
| K2 reality | legitimacy of spectral comparison | 1e-20 (results.json); 1e-25 (register) | 4.9e-29 | proven |
| K3 zeros | "zeros = ζ's zeros" demonstrated | 79 = 79 | max\|Δγ\| = 2.8e-14 | confirmed |
| K4 argument principle | calibrated counting (T3) | integers | residual ≤ 4.9e-28 | proven |
| K7 Gram | classical interlace, imperfections included | informational | 4 of 220 (classical) | reproduced |

- **K1 exists because the whole phase pipeline leans on Γ-identities.** If the closures drifted, θ(t) would be phase noise and Z_id would be a complex-valued function like any other, unfit for spectral comparison. Threshold 1e-30 at dps 40; measured 1.27–2.59e-39 — nine orders of margin.
- **K2 exists because reality is the property that makes the comparison to a self-adjoint spectrum legitimate at all.** A complex target could match an operator's eigenvalues only by coincidence of moduli; a real target can be matched crossing by crossing. Measured: 4.9e-29 against a committed threshold of 1e-20 (the series validation register lists T2 at 1e-25 — both cleared with room to spare).
- **K3 exists because "zeros coincide with ζ's zeros" must be demonstrated against a reference, not asserted.** The internal mpmath cache provides the reference: 79 of 79, max|Δγ| = 2.8e-14.
- **K4 carries its own built-in positive control.** At T = 10.000000 the strip contains no zeros at all, and the calibrated count returns N_strip = −1.8832666871680676e-31 — zero up to quadrature noise. A counting method that returns 0 on an empty block and exact integers (3, 10, 29, 79) on occupied blocks has *demonstrated* its calibration; that is Theorem T3, the pole calibration of the argument principle.
- **K7 reproduces known classical structure, imperfections included.** Exactly the four classical sign violations among the first 220 Gram points come out of the pipeline. A procedure that reproduces the literature's exceptions as well as its rules has passed a sharper test than one that reproduces only the rules; the criterion is explicitly informational.

And the discipline cuts both ways. Honesty rule no. 3 of the package — *statuses are not inflated* — requires the composite verdict to list its one refuted element in the same table as the passes of its five criteria. The structural mismatch 0.765 of the candidate elementary form for the single modulus is therefore part of the PASS, not hidden behind it: the K1 refutation is not a defeat but a calibration. The ladder closes elementarily only at the strip edges (Re s = 0 and Re s = 1) and through the Legendre pair product — exactly the product that enters the phase θ(t).

## Results

The campaign's headline table, numbers verbatim from the committed verdict:

| Quantity | Value | Status |
|---|---|---|
| Closure |Γ(½+iu)|² = π/cosh πu | residual 2.59e-39 (dps 40) | proven |
| Closure |Γ(iu)|² = π/(u·sinh πu) | residual 2.57e-39 | proven |
| Product |Γ(¼+iu)|·|Γ(¾+iu)| (Legendre) | residual 1.27e-39 | proven |
| Candidate form of the single modulus | structural mismatch 0.765 | refuted |
| Reality of Z_id (K2) | max|Im Z_id| = 4.9e-29 | proven |
| Z_id zeros on [0,200] vs mpmath (K3) | 79 zeros, max|Δγ| = 2.8e-14 | confirmed |
| Gram points (K7) | 220 points, 4 violations (classical) | reproduced |

Read it as two halves. The first three rows are T1 — the Γ-ladder: two edge closures at Re s = 0 and Re s = 1 and the Legendre pair product on the line, each verified at dps = 40 with residuals of 1.27–2.59e-39 against a threshold of 1e-30. The fourth row is the honest refutation: the candidate elementary form of the single modulus misses with structural mismatch 0.765 — not 1 — and the miss is published, not buried. The last three rows are the graph measurements: the imaginary part of Z_id on the line (K2), the zero match against the internal mpmath reference (K3), and the classical Gram interlace (K7), reproduced with exactly the four known violations among the 220 points.

### K1 — the three closures, in full precision

| Closure | Max relative residual (dps 40) |
|---|---|
| \|Γ(½+iu)\|² = π/cosh πu — edge Re s = 1 | 2.5896027595341725e-39 |
| \|Γ(iu)\|² = π/(u·sinh πu) — edge Re s = 0 | 2.5680114024923632e-39 |
| \|Γ(¼+iu)\|·\|Γ(¾+iu)\| = π√2/√cosh 2πu — Legendre pair, line | 1.2662422397767273e-39 |

The residuals are relative deviations accumulated over the 401-point grid; the committed threshold is 1e-30. The honest finding recorded with K1 states the boundary in one line: the modulus of the Γ-factor on the critical line is *not* elementary — "the line where the ladder stops closing". What *does* close on the line is the Legendre pair product, and it is exactly that product which enters the phase θ(t): the assembly uses precisely the algebra that survives.

### K2 — reality of Z_id

| Measured | Value |
|---|---|
| max\|Im Z_id\| | 4.9281188370946126e-29 |
| Evenness deviation (max) | 9.856237674189225e-29 |
| Scale of Z_id at t = 50 | 0.340735005955025 |
| Threshold | 1e-20 (committed results.json); 1e-25 (validation register) |

The evenness deviation is twice the imaginary residual to within rounding — the two measurements are facets of the same rephasing symmetry ξ(s) = ξ(1−s), so their ratio is a consistency check rather than an accident. The scale entry exists so the residual can be read *relatively*: against a function whose size at t = 50 is 0.34, an imaginary part of 4.9e-29 is a relative defect of order 1.4e-28. The source code records the same bound in its contract: reality (T2) holds to 5e-29 at dps = 30.

### K3 — the first zeros, found and referenced

| k | Z_id zero (bisection, dps 25) | mpmath reference |
|---|---|---|
| 1 | 14.134725142 | 14.134725142 |
| 2 | 21.022039639 | 21.022039639 |
| 3 | 25.01085758 | 25.01085758 |
| 4 | 30.424876126 | 30.424876126 |
| 5 | 32.935061588 | 32.935061588 |
| 6 | 37.586178159 | 37.586178159 |
| 7 | 40.918719012 | 40.918719012 |
| 8 | 43.327073281 | 43.327073281 |
| 9 | 48.005150881 | 48.005150881 |
| 10 | 49.773832478 | 49.773832478 |
| 11 | 52.970321478 | 52.970321478 |
| 12 | 56.446247697 | 56.446247697 |
| 13 | 59.347044003 | 59.347044003 |
| 14 | 60.831778525 | 60.831778525 |
| 15 | 65.112544048 | 65.112544048 |

On [0, 200] the bisection finds n_found = 79 zeros against n_reference = 79 — a match of counts first, of positions second. The committed verdict stores the first fifteen as a sample (both columns above are printed from it verbatim; they agree to the last digit shown). The committed positional deviation is max|Δγ| = 2.842170943040401e-14, quoted as 2.8e-14 in the headline table; as *How to read the numbers* explains, that figure is the float64 comparison floor, not the bisection's own precision.

### K4 — the argument principle in the block T ≤ 200

| T | N_strip | N_int | n_on_line | residual to integer | S(T) |
|---|---|---|---|---|---|
| 10.000000 | −1.8832666871680676e-31 | 0 | 0 | 1.8832666871680676e-31 | −0.023719897999744943 |
| 27.717867 | 3.0 | 3 | 3 | 7.099748146989106e-30 | −0.011257014922378815 |
| 51.372077 | 10.0 | 10 | 10 | 9.466330862652142e-30 | 0.12118278897296962 |
| 100.074523 | 29.0 | 29 | 29 | 4.1020767071492614e-29 | −0.03523614440404258 |
| 199.640031 | 79.0 | 79 | 79 | 4.922492048579114e-28 | 0.004919660612298083 |

The columns, in order: N_strip is the continuous argument count of ξ in the strip 0 < Re s < 2, 0 < Im s < T (contour (2,0)→(2,T)→(0,T)→(0,0), pole s = 1 from above, N(T) = 1 + Δarg/2π, step 0.02); N_int is its nearest integer; n_on_line is the number of Z_id zeros found on (0, T]; the residual is |N_strip − N_int|; S(T) is the remainder of the count against the Riemann–Siegel main term, whose smallness (|S| ≤ 0.121 here) is the classical fluctuation. The content of the table is the equality of the three middle columns at every probe: the number of zeros in the strip equals the number on the line, to residuals of at most 4.9e-28. That is RH verified *in the block*, and the `rh_in_block_pass` flag records it for all five probes. This block is the seed of stage 3; C2 extends the same calibrated machinery to T = 1000, where the count becomes 649 = 649.

### K7 — Gram points and the four violations

| n | g_n | Z_id(g_n) |
|---|---|---|
| 126 | 282.454721 | −0.027629 |
| 134 | 295.583907 | −0.0169 |
| 195 | 391.448202 | 0.023289 |
| 211 | 415.60146 | 0.38289 |

Of the first 220 Gram points (n = 1..220, θ(g_n) = nπ), these four violate the expected sign alternation. They are not discoveries of this campaign and not defects of it — they are the classical exceptions to Gram's law, known in the literature and compensated by Rosser's "good" Gram blocks in which the interlacing rights itself. Their magnitudes are small (the function barely misses the expected sign at n = 126, 134, 195; the largest deviation, 0.38289, occurs at n = 211, g = 415.60146). The criterion is explicitly informational: reproducing the exceptions is the point.

## How to read the numbers

- **dps** — decimal digits of precision in the mpmath arithmetic. The committed verdict's working default is dps 30; the K1 grid runs at dps 40; the zero hunt at dps 25; θ(t) adds ten guard digits above whatever context it is called in. "dps 40" means roughly forty significant decimal digits, with the guard digits protecting the last committed one.
- **Why 1e-39 matters.** At dps = 40 the rounding floor of the arithmetic is of order 1e-40 per elementary operation. A relative residual of 1.27–2.59e-39, accumulated over a 401-point grid and several Γ, π and cosh evaluations, is indistinguishable from that floor — meaning the identities hold *to within the arithmetic's own noise*. The committed threshold is 1e-30, so the measured margin is about nine orders; the series ledger (`results/RESULTS.md`, entries 1–4) quotes the same closures as "residuals 1.3–2.6e-39 (dps 40)".
- **How to read K2.** The bound 4.9e-29 is absolute; against the recorded scale of Z_id at t = 50 (0.340735005955025) it is a relative defect near 1.4e-28. float64 assembly alone would leave imaginary debris around 1e-16 — this is precisely why the campaign computes in two arithmetics and commits the mpmath one, multiplying the phase into ζ before any rounding to double.
- **How to read 2.8e-14 (K3).** The bisection itself runs at dps = 25; the comparison against the reference cache happens in float64, and 2.842170943040401e-14 ≈ 2⁻⁴⁵ is the spacing of double precision at arguments of size 100–200. The metric, not the zero-finding, is the limiter.
- **Signed zeros.** N_strip = −1.8832666871680676e-31 at T = 10.000000 is a *signed zero*: the count is zero, the sign is quadrature noise. Residuals of this size (1e-31) against a threshold register of 1e-20 for N(T) are the system working as designed.
- **The thresholds ledger.** `docs/validation.md` fixes the series' thresholds in advance: Γ-closures (T1) 1e-30 at dps 40, fact 1.3–2.6e-39; Z_id reality (T2) 1e-25, fact 4.9e-29. The committed `results.json` carries its own per-criterion thresholds (1e-30 for K1, 1e-20 for K2); the measured values clear both registers.

## Interpretation: what C1 means for H1–H5

The package's scorecard answers the five questions of the Hilbert–Pólya programme by measurement; it is reproduced here so C1's contributions can be located:

| Item | Question | Verdict | Basis |
|---|---|---|---|
| H1 | Self-adjointness | **YES** | Hermitian by construction; real spectrum at machine precision |
| H2 | Spectral identity (level n ↔ zero n) | **NO** | null level — D_nn 0.258 vs surrogate 0.26±0.01 (C3); ≈0.5 order by relative residual (C4); \|r_H7\| ≤ 0.043 (C5) |
| H3 | The GUE statistics class | **YES** | ⟨r⟩ = 0.60 at Nv ≥ 8; all of C5 in class |
| H4 | Dirac-type dynamics | **YES** | coherent packet, reflection, scattering; energy 1e-15 (C7) |
| H5 | Primes inside the operator | **NO** | ψ-ladder 0.972 for zeros, null zone for gates (C6) |

<p align="center"><img src="../../assets/illustrations/ill_vortex_lattice.png" width="720" alt="The vortex-lattice gates of stage 4, contrasted with the graph of stage 2"/></p>

C1 decides none of the five rows alone, but it touches all of them:

- **H1 (self-adjointness, YES).** C1 contributes the graph-side mirror of self-adjointness: the reality (T2) and evenness of Z_id at 4.9e-29. A real target function is what makes "eigenvalue ↔ zero" comparisons meaningful in the first place.
- **H2 (spectral identity, NO).** C1 supplies the boundary statement that the later campaigns then measure: *the algebraic envelope does not generate zeros — it merely wraps ζ in a smooth phase.* Whatever is true of Z_id is true by identity; whatever Z_id cannot do, no rearrangement of the phase can do either. When C3 and C5 find the gates at the surrogate-null level in the rank metric (best \|r_H7\| = 0.226 then ≤ 0.043) and C4's heat-trace projection shows ≈0.5 order, C1's lesson explains *why* such gaps were always going to be found: matching by identity is not matching by generation.
- **H3 (GUE class, YES).** The four Gram violations among 220 points are the classical trace of non-rigid interlacing — the zeros do not sit on the θ-lattice like beads on an abacus. The statistical campaigns turn that observation into the quantitative ⟨r⟩ = 0.60 at Nv ≥ 8; C1's Gram block is where the phenomenon first appears in the series.
- **H4 (Dirac dynamics, YES).** Not touched directly. The resonator is built and driven later (C7, coherent packet at energy 1e-15); C1's role is to have made the target function available.
- **H5 (primes inside the operator, NO).** C1 assembles Xi_id exactly — ξ(½+it) = −½(t²+¼)·π^{−s/2}·Γ(s/2)·ζ(s) — and it is precisely this completed ξ whose Hadamard structure the trace stage exploits: Theorem T6 proves the prime weight Λ(n)/√n lives in the heat trace of the zero-coded operator H_ξ (|ΔK| ≤ 1.2e-5) and in no gate. The exact assembly built here is what makes that later proof possible.

Theorem statuses attached to this campaign: **T1** — Γ-closures, *proven* (dps = 40; plus one honest refutation); **T2** — Im Z_id = 0, *proven*. The one refutation is the calibration mark of the campaign: it tells every future construction where elementary algebra ends — at the single modulus on the line — so that no one searches for an elementary form of |Γ(¼+iu)| again, and no one mistakes the Legendre pair product inside θ(t) for a lucky accident.

## Reproduction

```bash
# a tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c1_identity.py
```

The tour re-reads the committed verdict `data/c1_identity_verdict.json`, prints the pass flags and thresholds of every criterion block, re-derives the T1 closures at u = 1, 2, 3 and prints the max residual at dps = 40, and samples Z_id(17.3) at dps = 30, printing its real part and |Im|. The series seed is 96; the RNG streams are fixed (`engine/hamiltonian.py`). All dependencies are in `requirements.txt`.

The theorem machinery and the blind verification protocol:

```bash
python3 -m pytest tests/ -q
bash independent_verification/RUN_ALL.sh
```

The pytest suite re-runs the Γ-closures at dps = 40 below the test threshold 1e-35 and re-checks Z_id reality; the IVP checks of this campaign re-derive the same numbers independently. Nothing here needs the external Odlyzko zero file: every committed criterion compares against identities, against the internal mpmath cache, against integers, or against the classical Gram structure. The whole campaign is deterministic and runs in about two seconds.

## Data and figures

Figures of the campaign — the Russian variants:

| File | Where |
|---|---|
| `fig01_zid.png` | 600 dpi — `figures_hires/ru/fig01_zid.png`; screen — `figures/ru/` |
| `fig02_gamma_ladder.png` | 600 dpi — `figures_hires/ru/fig02_gamma_ladder.png`; screen — `figures/ru/` |

and the English variants:

| File | Where |
|---|---|
| `fig01_zid_en.png` | 600 dpi — `figures_hires/en/fig01_zid_en.png`; screen — `figures/en/` |
| `fig02_gamma_ladder_en.png` | 600 dpi — `figures_hires/en/fig02_gamma_ladder_en.png`; screen — `figures/en/` |

`fig01_zid` shows the identity function on the line — the real oscillation whose crossings are the zeros; `fig02_gamma_ladder` shows the Γ-ladder closures — the three algebraic curves that the residuals of K1 pin down at dps = 40.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`. The full monograph of this computation — statement, theorems, tables, figures, honest limitations — runs 7–9 pages, the same content in two languages.

Data:

| File | Content |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `data/curve_Zid.npz` | the stored Z_id curve sample |
| `../data/c1_*.json` | duplicate of the verdict in the shared registry |

Anatomy of `data/results.json`: a `meta` block (task "Task 7 — identity function (hodge-laboratory × ab-cloud-research) vs RH", date 2026-10-10, dps 30, the ingredient card HL-1/HL-2/HL-4/HL-5 and AC-2/AC-3, the assembled objects Z_id and Xi_id, `free_parameters: 0`); a `criteria` block with K1–K7 (measured values, thresholds, pass flags, provenance and honest findings); and a `verdict` block (K1–K4 true, composite true). The file additionally archives the K5 counting-identity and K6 second-moment blocks of the shared pipeline — `n_zeros` 2,001,052 up to T_max = 1132490.658714411, max|S| = 1.7993664555251598, and the final Σγ² relative deviation 8.811375917559696e-07 — whose campaign-level numbers the ledger reports under C2; C1's own composite verdict covers K1–K4 and K7 only.

## Verdict

**{'ru': 'композитный вердикт K1–K4, K7: PASS (одно опровержение опубликовано)', 'en': 'composite verdict K1–K4, K7: PASS (one refutation published)'}** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

<img src="../../assets/avatars/hp_agent_vera.svg" width="110" align="right" alt="Agent Vera"/>

The composite flag is true because K1, K2, K3 and K4 all clear their committed thresholds; K7 reproduces the classical 4-of-220 violation pattern and is scored informational; and the one refuted element — the candidate elementary form of the single modulus, structural mismatch 0.765 — is published in the same table as the passes rather than in a footnote. Agent Vera's verification stamp is the IVP block: the independent-verification protocol re-derives the closures and the reality bound without consulting the campaign's own intermediates, which is what makes the PASS a measured statement rather than a self-report.

## FAQ

**Q: Does Z_id prove the Riemann Hypothesis?**
A: No. The zeros of Z_id on the line coincide with ζ's zeros *by identity* — the coincidence is a rephasing, not a theorem about all zeros. The campaign's own boundary statement says exactly this: the algebraic envelope does not generate zeros. What C1 proves is T1 (the closures) and T2 (reality), and it measures how far the assembly reaches — no further.

**Q: If Z_id is just Hardy's Z(t), what is new here?**
A: Nothing in the function; everything in the assembly. The point is that θ(t) and the closures are derived inside the package from the Γ-frame with `free_parameters: 0` and verified at dps = 40 (residuals 1.27–2.59e-39), so the graph object of the whole series carries no fitted constants. The assembly card in `data/results.json` (HL-1, HL-2, HL-4, AC-2, AC-3) documents the lineage of every ingredient.

**Q: Why can't the single modulus |Γ(¼+iu)| be made elementary?**
A: Reflection closes Γ-pairs exactly at the strip edges Re s = 0 and Re s = 1; on the line only the product |Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu closes, through Legendre duplication. The computed candidate elementary form for the single modulus mismatches structurally: 0.765 ≠ 1. That is the "line where the ladder stops closing" — and the product that *does* close is exactly the one the phase θ(t) needs, which is why the refutation is also a calibration.

**Q: Are the four Gram violations a failure of the campaign?**
A: No — they are the classical failures of Gram's law itself (n = 126, 134, 195, 211 among the first 220 points), known in the literature and compensated by Rosser's "good" Gram blocks. Reproducing exactly these four, at exactly these magnitudes (the largest, 0.38289, at g = 415.60146), is the positive control of K7: the pipeline reproduces known structure including its imperfections. The criterion is informational.

**Q: Why does C1 not need the external zero file?**
A: Every committed criterion compares against something internal: K1 against algebra (threshold 1e-30), K2 against reality (4.9e-29), K3 against the internal mpmath reference cache (79/79, 2.8e-14), K4 against integers (residuals ≤ 4.9e-28), K7 against θ(g_n) = nπ. The standard Odlyzko zero list is used only by optional fresh campaigns elsewhere in the package; nothing in the committed C1 verdict depends on it.

**Q: What are the K5 and K6 blocks doing in C1's results.json?**
A: The committed verdict file archives the counting-identity (K5) and second-moment (K6) blocks of the shared pipeline — up to T_max = 1132490.658714411 with max|S| = 1.7993664555251598 and Σγ² relative deviation 8.8e-7. Their campaign-level numbers are reported under C2 in the ledger; C1's composite verdict covers K1–K4 and K7 only. The duplication is deliberate: one file, one registry entry, no orphan numbers.

## Common misreadings

| Misreading | Correction |
|---|---|
| "Z_id proves the Riemann Hypothesis" | It proves reality (T2) and exact algebra (T1); the zero coincidence holds on the line by rephasing and generates nothing. |
| "0.765 is a numerical residual" | It is the structural mismatch of the refuted candidate form for the single modulus \|Γ(¼+iu)\| — a published refutation, not an error. |
| "The 4 Gram violations are campaign defects" | They are the classical exceptions to Gram's law in this window; K7 reproduces them deliberately. |
| "C1 decided H2" | C1 built the graph side; the H2 verdict (NO) is measured in C3/C4/C5 (surrogate-null level; ≈0.5 order by residual; \|r_H7\| ≤ 0.043). |
| "2.8e-14 is the bisection precision" | It is the float64 comparison floor (≈ 2⁻⁴⁵ at γ ≈ 100–200); the bisection runs at dps = 25. |
| "K5/K6 numbers belong to C1's verdict" | They are archived in the same results.json but reported under C2; C1's composite covers K1–K4, K7. |

## Glossary

- **Γ-frame** — the lattice of Gamma-function identities (reflection, duplication and their shifts) from which the package derives every phase and modulus it uses.
- **Γ-ladder** — the three elementary closures of K1: |Γ(½+iu)|² = π/cosh πu, |Γ(iu)|² = π/(u·sinh πu), |Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu.
- **θ(t)** — the Riemann–Siegel theta, Im ln Γ(¼+it/2) − (t/2)·ln π, on its continuous branch; the phase that makes Z_id real.
- **Hardy function** — the real function Z(t) = e^{iθ(t)}ζ(½+it); here assembled as Z_id with zero fitted parameters.
- **Xi_id** — the exact assembly ξ(½+it) = −½(t²+¼)·π^{−s/2}·Γ(s/2)·ζ(s) on the line.
- **dps** — decimal digits of precision in mpmath; the campaign works at dps 25–40 with ten guard digits on θ(t).
- **Gram point** — a real g_n with θ(g_n) = nπ, computed here by mpmath `findroot` for n = 1..220.
- **Gram's law** — the classical heuristic that zeros interlace with the Gram lattice, i.e. that Z_id alternates sign from g_n to g_{n+1}; violated 4 times in 220 here, all classical.
- **Rosser good blocks** — stretches of the Gram lattice in which the interlacing rights itself after a violation, compensating the misses in pairs.
- **Argument principle / N(T)** — the zero count of ξ in the strip obtained from the change of argument along (2,0)→(2,T)→(0,T)→(0,0); N(T) = 1 + Δarg/2π with the pole s = 1 from above.
- **S(T)** — the remainder of N(T) against the Riemann–Siegel main term; |S| ≤ 1.8 is the series-wide register bound.
- **Bisection** — the zero-refinement scheme of K3: sign changes bracket a zero; 80 refinement steps shrink each bracket at dps = 25.
- **IVP** — the independent verification protocol of `independent_verification/`; the blind re-derivation stamp behind the composite verdict.

## Historical notes on Gram's observation

Jørgen Pedersen Gram computed zeros of ζ by hand at the turn of the twentieth century and published his note on the zeros of the zeta function in 1903; the lattice θ(g_n) = nπ now carries his name. Working with tables rather than code, Gram noticed that the zeros seemed to fall between his points in strict alternation — a heuristic so regular that it stood as a near-law for the low zeros and entered the literature as Gram's law. The heuristic survives in a refined form: the violations are real but rare and small, and they occur in patterns that the later computations of Rosser and colleagues organized into "good" blocks, in which the interlacing rights itself after every miss. The four violations this campaign reproduces among the first 220 Gram points — n = 126, 134, 195, 211 — are precisely the classical ones in this window, and their compensation by good blocks is why they carry no threat to the location of the zeros: Gram's law is about interlacing, not about where the zeros are. For the Hilbert–Pólya programme the observation has a modern reading: the slight, patterned looseness of the interlace is the first statistical hint that the zeros behave like eigenvalues of a chaotic system rather than like a rigid arithmetic lattice — the hint that C3 and C8 later quantify as the GUE class.

## Appendix: provenance of every headline number

Every headline number of this campaign, mapped to its source of record:

| Number | Source of record | Quoted as |
|---|---|---|
| 2.59e-39 / 2.57e-39 / 1.27e-39 | K1 block of `data/results.json` (full precision 2.5896027595341725e-39, 2.5680114024923632e-39, 1.2662422397767273e-39) | headline table; ledger entry 1 |
| 0.765 | K1 refutation, `structural mismatch` of the candidate form | headline table row 4 |
| 4.9e-29 | K2 `max_imZ` = 4.9281188370946126e-29 | headline table; ledger entry 2 quotes 4.93e-29 |
| 79 / 79; 2.8e-14 | K3 `n_found`, `n_reference`, `max_dev_gamma` = 2.842170943040401e-14 | headline table; ledger entry 3 |
| 220 / 4 | K7 `n_points` (n_range 1..220), `n_violations` | headline table; ledger entry 4 |
| 401-point grid; dps 40; 1e-30 | campaign method; `docs/validation.md` row 1 | method; how to read the numbers |
| 1e-20 / 1e-25 | K2 threshold in results.json; T2 row of the validation register | K2 table |
| seed 96; ~2 s | series seed (`engine/hamiltonian.py`); campaign runtime | reproduction |
| 7–9 pages | monograph volumes (ru/en, docx/pdf) | data and figures |

One rounding convention note, so no reader is confused by the ledger: the headline table rounds 4.9281188370946126e-29 down to 4.9e-29 while the living ledger prints 4.93e-29 — both are the same committed measurement, and the JSON file is the source of record. The package's reproducibility rule (`data/README.md`) requires any rerun of the campaigns to reproduce the committed values bit-for-bit, which is why every number above can be traced to exactly one file and one field name. If a value cannot be traced this way, it does not belong to the series; that discipline is the quiet backbone of the whole package, and C1 — the campaign with zero fitted parameters — is where it is easiest to see in full.

## See also

- [C2 · The argument principle](../C2_argument_principle/README.md) — the counting stage, from the K4 block here to RH in the strip verified to T = 1000 (649 = 649).
- [docs/theory.md](../../docs/theory.md) — the five-stage map, the resonator, and the logic of the H1–H5 scorecard.
- [results/RESULTS.md](../../results/RESULTS.md) — the living ledger of numbers; entries 1–4 of the main table belong to this campaign (2.59e-39 closures; 4.93e-29 reality; 79/79 zeros at max|Δγ| = 2.8e-14; 4-of-220 Gram).

---
*Hilbert Polya Bridge v2.0.0 · C1 · The identity function and the Γ-ladder*

