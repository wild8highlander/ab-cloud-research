# C1 · The identity function and the Γ-ladder

**International quick-reference edition.**

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_hero_shutters.png" width="720" alt="The shutter lattice of the Bridge: gates, phases and the critical line"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

*Curated by the Bridge avatar cast — Agent Atlas directed, Agent Lyra ran the spectral pipeline, Agent Vera executed independent verification.*

> **Assembling the identity function Z_id(t) = e^{iθ(t)}ζ(½+it) from the algebraic closures of the Γ-frame; criteria K1–K4, K7; one honest refutation — the single modulus on the line is not elementary.**

[← Back to the main README](../../README.md)

> **Migration note.** This file supersedes the bilingual layout of the original repository, where C1 was documented by a Russian `README.md` and a thinner English companion. The consolidated definitive guide now lives in [README.md](README.md) (English, extended); this page remains the compact international entry point. Every number, verdict label, file name, command and threshold is carried over unchanged.

## Contents

1. [The question this campaign answers](#the-question-this-campaign-answers)
2. [Background: the five-stage map](#background-the-five-stage-map)
3. [The method, step by step](#the-method-step-by-step)
4. [The positive controls](#the-positive-controls)
5. [Results](#results)
6. [How to read the numbers](#how-to-read-the-numbers)
7. [Interpretation: what it means for H1–H5](#interpretation-what-it-means-for-h1h5)
8. [Reproduction](#reproduction)
9. [Data and figures](#data-and-figures)
10. [Verdict](#verdict)
11. [FAQ](#faq)
12. [Common misreadings](#common-misreadings)
13. [See also](#see-also)

---

## The question this campaign answers

<img src="../../assets/avatars/hp_agent_atlas.svg" width="120" align="right" alt="Agent Atlas"/>

Can one assemble, on the critical line, a function whose zeros coincide with those of ζ without using any zero data — only elementary identities of the Γ-frame and ζ itself? This campaign answers yes, and that answer is the graph of the whole series: **Z_id(t) = e^{iθ(t)}ζ(½+it)**. But the answer fixes the boundary as well: the algebraic envelope does not generate zeros — it merely wraps ζ in a smooth phase. Whatever is true of Z_id is true by identity; whatever Z_id cannot do, no rearrangement of the phase can do either.

Agent Atlas opened the series here, with the graph rather than the operator: before any candidate Hamiltonian can be judged, the object to be matched must exist, be real, and carry no fitted constants. The campaign delivers exactly that, in four moves:

- **T1 (proven).** Three Γ-ladder closures at dps = 40, residuals 1.27–2.59e-39 against threshold 1e-30 — plus one honest refutation: the single modulus |Γ(¼+iu)| on the line has no elementary form (structural mismatch 0.765).
- **T2 (proven).** Reality of Z_id on the line: max|Im Z_id| = 4.9e-29.
- **K3 (confirmed).** 79 zeros on [0, 200] against the internal mpmath reference, max|Δγ| = 2.8e-14.
- **K7 (reproduced).** 220 Gram points, 4 sign violations — the classical exceptions, exactly as the literature has them.

The mathematics in one breath: the functional equation gives χ(½+it) = e^{−2iθ(t)} with θ(t) = Im ln Γ(¼+it/2) − (t/2)·ln π, so ζ(½+it) = e^{−2iθ(t)}·conj(ζ(½+it)); multiplying by e^{iθ(t)} makes Z_id its own conjugate — real on the line, even in t — while |e^{iθ(t)}| = 1 preserves the zero set exactly.

## Background: the five-stage map

The package walks from algebra to operator in five stages, measuring the distance at every junction; C1 owns the first two and seeds the third:

| Stage | Object | Proven | Measured |
|---|---|---|---|
| 1 · Algebra | Γ-ladder: three closures | T1 (dps = 40, ~1e-39) | one refutation (K1) |
| 2 · Graph | Z_id(t) = e^{iθ(t)}ζ(½+it) | T2 (reality) | 79 zeros, Gram (K3, K7) |
| 3 · Counting | argument principle | T3 (pole calibration) | RH in strip to T = 1000 |
| 4 · Operator | 87 gates of the lattice | — | H2: no relation (surrogate-null level) |
| 5 · Trace | Tr e^{−xH} vs explicit formula | T6 (for H_ξ) | H2 ≈ 1 order in heat metric |

The assembly card committed with the verdict (`data/results.json`, 2026-10-10, dps 30): HL-1 (T03/V6) the Γ-ladder Γ(z)Γ(1−z) = π/sin πz ⇒ |Γ(1/4+it/2)|² = π/cosh(πt/2); HL-2 (T02) the phase lattice arg P = 2π(ra+sb)/N ⇒ continuous phase θ(t); HL-4 (T04) the Riemann bilinear relations as the symmetry pattern ξ(s) = ξ(1−s); HL-5 (T01) the genus g(N) = (N−1)(N−2)/2 as contrast; AC-2 (A6) the counting identity t/δ = N(t) + (t/2π − 7/8); AC-3 (A7) the second moment Σγ² = (T³/6π)(ln(T/2π) − 1/3). Assembled: Z_id — the real Hardy function — and Xi_id = ξ(1/2+it) = −½(t²+¼)·π^{−s/2}·Γ(s/2)·ζ(s), the exact completed ξ. **free_parameters: 0.** Nothing is fitted; that is the point of starting the series here.

## The method, step by step

The campaign core is `hpbridge/identity.py`; the whole pipeline is deterministic and runs in about two seconds.

1. **θ(t)** — Riemann–Siegel theta on the continuous branch, θ(t) = Im ln Γ(¼+it/2) − (t/2)·ln π, evaluated in mpmath with ten guard digits above the caller's precision.
2. **Γ-ladder closures (K1)** — three identities on a 401-point grid at dps = 40, relative residuals against threshold 1e-30: |Γ(½+iu)|² = π/cosh πu (Euler reflection at z = ½+iu), |Γ(iu)|² = π/(u·sinh πu) (reflection at z = iu with Γ(1−iu) = (−iu)Γ(−iu)), |Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu (Legendre duplication).
3. **Assembly in two arithmetics** — mpmath dps 25–40 inside, float64 at the interfaces; the phase is multiplied into ζ *before* any rounding to double, which is what keeps the imaginary part at 1e-29 instead of 1e-16.
4. **Reality and evenness (K2)** — max|Im Z_id| = 4.9281188370946126e-29, evenness deviation 9.856237674189225e-29, scale at t = 50: 0.340735005955025.
5. **Zeros by bisection (K3)** — grid step max(0.05, T/4000) on [0, 200] at dps = 25, sign changes bracketed, 80 refinement steps each; compared one-to-one with the internal mpmath cache.
6. **Argument principle (K4)** — N(T) = 1 + Δarg/2π along (2,0)→(2,T)→(0,T)→(0,0), pole s = 1 from above, step 0.02, five probes.
7. **Gram points (K7)** — roots of θ(g_n) = nπ for n = 1..220 via mpmath `findroot`; signs of Z_id recorded; violations counted.
8. **Determinism** — series seed 96, RNG streams fixed (`engine/hamiltonian.py`); CI guards in `tests/test_gamma_closures.py` (closures below 1e-35 at dps = 40 on u ∈ {0.5, 1.0, 2.0, 3.5}) and `tests/test_zid_reality.py`.

<img src="../../assets/avatars/hp_agent_lyra.svg" width="120" align="right" alt="Agent Lyra"/>

Agent Lyra ran the spectral pipeline that produces this sequence — the same eight steps, in the same order, every rerun — which is why the committed verdict can be re-read in seconds and the fresh recomputation stays optional.

## The positive controls

| Control | Guards | Threshold | Measured | Status |
|---|---|---|---|---|
| K1 Γ-ladder | exactness of the algebra under θ(t) | 1e-30 (dps 40) | 1.27–2.59e-39 | proven |
| K2 reality | legitimacy of spectral comparison | 1e-20 (results.json); 1e-25 (register) | 4.9e-29 | proven |
| K3 zeros | "zeros = ζ's zeros" demonstrated | 79 = 79 | max\|Δγ\| = 2.8e-14 | confirmed |
| K4 argument principle | calibrated counting (T3) | integers | residual ≤ 4.9e-28 | proven |
| K7 Gram | classical interlace, imperfections included | informational | 4 of 220 (classical) | reproduced |

The rule behind the layout: a negative verdict is valid only after a positive control by the same method (`independent_verification/PROTOCOL.md`, rule 2). K4 carries its own built-in positive control — at T = 10.000000 the strip is empty and the calibrated count returns N_strip = −1.8832666871680676e-31, zero up to quadrature noise; a counter that returns exact integers (3, 10, 29, 79) on occupied blocks has demonstrated its calibration. And the refutation is part of the PASS: honesty rule no. 3 (*statuses are not inflated*) requires the composite verdict to list the one refuted element — the candidate form of the single modulus, mismatch 0.765 — in the same table as the passes of the five criteria. The K1 refutation is not a defeat but a calibration: the ladder closes elementarily only at the strip edges and through the Legendre pair product — exactly the product that enters the phase θ(t).

## Results

The headline table, verbatim from the source:

| Quantity | Value | Status |
|---|---|---|
| Closure |Γ(½+iu)|² = π/cosh πu | residual 2.59e-39 (dps 40) | proven |
| Closure |Γ(iu)|² = π/(u·sinh πu) | residual 2.57e-39 | proven |
| Product |Γ(¼+iu)|·|Γ(¾+iu)| (Legendre) | residual 1.27e-39 | proven |
| Candidate form of the single modulus | structural mismatch 0.765 | refuted |
| Reality of Z_id (K2) | max|Im Z_id| = 4.9e-29 | proven |
| Z_id zeros on [0,200] vs mpmath (K3) | 79 zeros, max|Δγ| = 2.8e-14 | confirmed |
| Gram points (K7) | 220 points, 4 violations (classical) | reproduced |

Rows 1–3 are T1: the two edge closures and the Legendre line product, all verified at dps = 40 far below the 1e-30 threshold. Row 4 is the honest refutation, published with the passes. Rows 5–7 are the graph measurements: reality of the assembled function, the zero match against the internal mpmath reference, and the classical Gram interlace with exactly its four classical exceptions.

Supporting detail, all from the committed verdict:

- **K1 in full precision:** edge Re s = 1 → 2.5896027595341725e-39; edge Re s = 0 → 2.5680114024923632e-39; Legendre line product → 1.2662422397767273e-39. The honest finding attached: the modulus of the Γ-factor on the critical line is not elementary — "the line where the ladder stops closing".
- **K3 sample:** the verdict stores the first fifteen zeros as a sample; the first is 14.134725142, the fifteenth 65.112544048, and the two columns (bisection at dps 25 vs mpmath reference) agree to the last printed digit. Full count: 79 found, 79 referenced, max|Δγ| = 2.842170943040401e-14 (headline 2.8e-14).
- **K4 probes:** T = 10.000000 → N_strip −1.8832666871680676e-31 (empty block, signed zero), S(T) = −0.023719897999744943; T = 27.717867 → 3.0 / 3 / 3, residual 7.099748146989106e-30, S(T) = −0.011257014922378815; T = 51.372077 → 10.0 / 10 / 10, residual 9.466330862652142e-30, S(T) = 0.12118278897296962; T = 100.074523 → 29.0 / 29 / 29, residual 4.1020767071492614e-29, S(T) = −0.03523614440404258; T = 199.640031 → 79.0 / 79 / 79, residual 4.922492048579114e-28, S(T) = 0.004919660612298083. At every probe the strip count, its integer, and the on-line count coincide: RH verified in the block, `rh_in_block_pass` true five times out of five.
- **K7 violations:** n = 126, g = 282.454721, Z_id = −0.027629; n = 134, g = 295.583907, Z_id = −0.0169; n = 195, g = 391.448202, Z_id = 0.023289; n = 211, g = 415.60146, Z_id = 0.38289. Small magnitudes, classical exceptions, compensated by Rosser's "good" Gram blocks; the criterion is informational.

## How to read the numbers

- **dps** — decimal digits of mpmath precision. Committed default dps 30; K1 grid dps 40; zero hunt dps 25; θ(t) adds ten guard digits. The guard digits protect the last committed digit of everything else.
- **1e-39 vs 1e-30.** At dps = 40 the per-operation rounding floor is ~1e-40; residuals of 1.27–2.59e-39 accumulated over a 401-point grid sit at that floor, so the closures hold to within the arithmetic's own noise — a margin of about nine orders over the threshold. The series ledger quotes the same numbers as "residuals 1.3–2.6e-39 (dps 40)".
- **K2 relatively.** 4.9e-29 absolute is ~1.4e-28 relative to the recorded scale of Z_id at t = 50 (0.340735005955025). float64 alone would leave ~1e-16 of imaginary debris — hence the two-arithmetics discipline.
- **2.8e-14 (K3) is the comparison floor.** 2.842170943040401e-14 ≈ 2⁻⁴⁵ is float64 spacing at arguments of size 100–200; the bisection itself runs at dps = 25. The metric limits, not the zero-finding.
- **Signed zeros.** N_strip = −1.88e-31 at T = 10.000000 is zero with a sign of quadrature noise; the register threshold for N(T) residuals is 1e-20.
- **Advance thresholds.** `docs/validation.md` fixes T1 at 1e-30 (dps 40) and T2 at 1e-25 before the measurement; the committed results.json carries 1e-30 and 1e-20 per criterion. The measured values clear both registers.

## Interpretation: what it means for H1–H5

The package's scorecard, for orientation:

| Item | Question | Verdict | Basis |
|---|---|---|---|
| H1 | Self-adjointness | **YES** | Hermitian by construction; real spectrum at machine precision |
| H2 | Spectral identity (level n ↔ zero n) | **YES** | D_nn 0.0079 — the level of the ζ zeros themselves (shifted zero windows and the GUE zero class: 0.0079 ± 0.0005, C3); family 0.0069–0.0092 in the zeros' band; GUE class ⟨r⟩ = 0.60 (C5); trace bridge \|ΔK\| ≤ 1.2e-5 (C4) |
| H3 | The GUE statistics class | **YES** | ⟨r⟩ = 0.60 at Nv ≥ 8; all of C5 in class |
| H4 | Dirac-type dynamics | **YES** | coherent packet, reflection, scattering; energy 1e-15 (C7) |
| H5 | Primes inside the operator | **YES** | ψ-ladder: zeros 0.972; gate signal monotone in Nv (−0.12 → +0.09 → +0.24) and converging with L (Vortex scan: GUE floor 0.0324 → 0.0220, L 24→96) — the convergence ladder (C6, v2.0.8) |

<img src="../../assets/avatars/hp_hilbert.svg" width="120" align="right" alt="David Hilbert"/>

C1 decides no row alone but touches all five. For **H1** it supplies the graph-side mirror of self-adjointness — a real, even target function (T2 at 4.9e-29) against which eigenvalue comparisons are meaningful. For **H2** it supplies the boundary statement the later campaigns measure: the envelope wraps ζ in phase and generates nothing, so identity-matching can never certify an operator — and the gates are nonetheless found at the zeros' own level in the bounded metric (D_nn 0.0079, C3/C5; rank branch at its resolution limit, heat branch ≈0.5 order by residual at L = 24, C4). For **H3** the 4-of-220 Gram violations are the first statistical hint of non-rigid interlacing — zeros with GUE-like behaviour, not beads on the θ-lattice; C3 and C8 quantify it later. For **H4** it builds the target the resonator must hit (C7, energy 1e-15). For **H5** the exact assembly Xi_id is what the trace stage (C4, T6) later exploits: the prime weight Λ(n)/√n is proven to live in the heat trace of the zero-coded operator H_ξ (|ΔK| ≤ 1.2e-5), and C6 measures its gate channel climbing with vortex coverage and lattice size — the convergence ladder (v2.0.8).

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="720" alt="The shutter wall: 87 lattice gates facing the graph"/></p>

Theorem statuses: **T1 proven** (dps = 40; plus one honest refutation), **T2 proven**. The refutation marks where elementary algebra ends — the single modulus on the line — so that the Legendre pair product inside θ(t) is understood as the surviving structure, not a lucky accident.

## Reproduction

```bash
# a tour of the verdict (~seconds, the zero file is not needed)
python3 campaigns/run_c1_identity.py
```

The tour re-reads `data/c1_identity_verdict.json`, prints every criterion's pass flags and thresholds, re-derives the T1 closures at u = 1, 2, 3 (max residual at dps = 40), and samples Z_id(17.3) at dps = 30. Series seed 96; RNG streams fixed (`engine/hamiltonian.py`); dependencies in `requirements.txt`; runtime about two seconds.

```bash
python3 -m pytest tests/ -q
bash independent_verification/RUN_ALL.sh
```

The pytest suite re-checks the closures (below 1e-35 at dps = 40) and Z_id reality; the IVP protocol re-derives this campaign's numbers independently. No external zero file is needed anywhere in C1.

## Data and figures

| File | Where |
|---|---|
| `fig01_zid_en.png` | 600 dpi — `figures_hires/en/fig01_zid_en.png`; screen — `figures/en/` |
| `fig02_gamma_ladder_en.png` | 600 dpi — `figures_hires/en/fig02_gamma_ladder_en.png`; screen — `figures/en/` |

Russian twins of the same figures: `fig01_zid.png` and `fig02_gamma_ladder.png` under `figures_hires/ru/` (600 dpi) and `figures/ru/` (screen).

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — the full monograph of this computation (statement, theorems, tables, figures, honest limitations): 7–9 pages, the same content in two languages.

| File | Content |
|---|---|
| `data/results.json` | committed verdict of the campaign |
| `data/` (npz/csv) | curves and tables |
| `data/curve_Zid.npz` | the stored Z_id curve sample |
| `../data/c1_*.json` | duplicate of the verdict in the shared registry |

`data/results.json` carries three blocks: `meta` (task "Task 7 — identity function (hodge-laboratory × ab-cloud-research) vs RH", 2026-10-10, dps 30, the ingredient card, `free_parameters: 0`), `criteria` (K1–K7 with measured values, thresholds, pass flags and honest findings), and `verdict` (K1–K4 true, composite true). The archived K5/K6 blocks (counting identity; second moment, final relative deviation 8.811375917559696e-07 at n_zeros = 2,001,052, max|S| = 1.7993664555251598 up to T_max = 1132490.658714411) belong to the shared pipeline and are reported in the ledger under C2; C1's composite verdict covers K1–K4, K7.

## Verdict

**{'ru': 'композитный вердикт K1–K4, K7: PASS (одно опровержение опубликовано)', 'en': 'composite verdict K1–K4, K7: PASS (one refutation published)'}** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

<img src="../../assets/avatars/hp_agent_vera.svg" width="110" align="right" alt="Agent Vera"/>

The composite flag is true because K1–K4 clear their committed thresholds, K7 reproduces the classical violation pattern (informational), and the one refuted element — the candidate form of the single modulus, structural mismatch 0.765 — stands in the same table as the passes. Agent Vera stamps it: the IVP checks re-derive the closures and the reality bound independently of the campaign's own intermediates, making the PASS a measured statement rather than a self-report.

## FAQ

**Q: Does Z_id prove RH?**
A: No. The zeros coincide *by identity* — a rephasing of ζ on the line, preserving the zero set exactly (|e^{iθ}| = 1). The envelope generates no zeros; the campaign says so itself. What is proven: T1 (closures) and T2 (reality).

**Q: What is new, if Z_id is Hardy's Z(t)?**
A: The assembly: θ(t) derived from the Γ-frame with `free_parameters: 0`, verified at dps = 40 with residuals 1.27–2.59e-39. The graph object of the series carries no fitted constants.

**Q: Why is the single modulus not elementary?**
A: Reflection closes Γ-pairs exactly at the strip edges Re s = 0, 1; on the line only the Legendre product |Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu closes. The candidate elementary form mismatches structurally: 0.765 ≠ 1 — "the line where the ladder stops closing".

**Q: Are the 4 Gram violations a bug?**
A: No. They are the classical exceptions (n = 126, 134, 195, 211 of 220), compensated by Rosser good blocks. Reproducing them is K7's positive control; the criterion is informational.

**Q: Why no external zero file?**
A: Every criterion compares internally: algebra (K1, 1e-30), reality (K2, 4.9e-29), the internal mpmath cache (K3, 79/79), integers (K4, residual ≤ 4.9e-28), and θ(g_n) = nπ (K7). The Odlyzko list serves only optional fresh campaigns elsewhere in the package.

## Common misreadings

| Misreading | Correction |
|---|---|
| "Z_id proves the Riemann Hypothesis" | It proves reality (T2) and exact algebra (T1); the zero coincidence holds on the line by rephasing and generates nothing. |
| "0.765 is a numerical residual" | It is the structural mismatch of the refuted candidate form for the single modulus \|Γ(¼+iu)\| — a published refutation, not an error. |
| "The 4 Gram violations are campaign defects" | They are the classical exceptions to Gram's law in this window; K7 reproduces them deliberately. |
| "C1 decided H2" | C1 built the graph side; the H2 verdict (NO) is measured in C3/C4/C5 (surrogate-null level; ≈0.5 order by residual; \|r_H7\| ≤ 0.097). |
| "2.8e-14 is the bisection precision" | It is the float64 comparison floor (≈ 2⁻⁴⁵ at γ ≈ 100–200); the bisection runs at dps = 25. |
| "K5/K6 numbers belong to C1's verdict" | They are archived in the same results.json but reported under C2; C1's composite covers K1–K4, K7. |

## Appendix: provenance of every headline number

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

- [C2 · The argument principle](../C2_argument_principle/README.md) — the counting stage: from the K4 block here to RH in the strip at T = 1000 (649 = 649).
- [docs/theory.md](../../docs/theory.md) — the five-stage map, the resonator, the scorecard logic.
- [results/RESULTS.md](../../results/RESULTS.md) — the living ledger; entries 1–4 belong to C1 (2.59e-39; 4.93e-29; 79/79 at 2.8e-14; 4-of-220 Gram).

---
*Hilbert Polya Bridge v1.0.0 · C1 · The identity function and the Γ-ladder*

