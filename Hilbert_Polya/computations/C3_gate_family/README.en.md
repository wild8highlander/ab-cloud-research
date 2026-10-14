# C3 · The H7 Gate Family — international quick-reference

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="720" alt="A wall of 52 shutters cut into a dark lattice wall: each aperture is one vortex-cloud Hamiltonian, and none of them transmits the light pattern of the zeta zeros"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

<p align="center"><em>Curated by the Bridge avatar cast — Agent Atlas directed the gate designs, Agent Lyra measured the spectra, Agent Vera guarded the controls.</em></p>

> **TL;DR — 52 gates (Nv × q × W × α) on a 24×24 lattice with π flux; the spectral-identity question H2; permutation nulls; positive controls PC1/PC2; verdict: no identity — gates at the surrogate-null level of D_nn (0.0079 vs 0.0079 ± 0.0005 for random surrogates; v2.0.1).**

[← Back to the main README](../../README.md)

**Vital signs** (every number traceable to `data/results.json` or `data/gates_table.csv`):

| | |
|---|---|
| Family | 52 gate configurations, master seed 96 |
| Best rank correlation with the zeros | r_H7 = 0.226 (p = 0.169, Bonferroni 0.80) |
| Identity controls | PC1 r = 1.000000000 · PC2 r = 1.000000000000 |
| Detection floor | D_nn = 2.7e-14 (PC1) · 1.2e-10 (PC2) |
| Best gate vs surrogate null | ≈ 0.26 in D_nn — at saturation, indistinguishable from random |
| Verdict | H2 — NO (no identity), measured with PC1/PC2 |
| One-line reproduction | `python3 campaigns/run_c3_gates.py` |

## Contents

1. [The question](#1-the-question)
2. [What a gate is — one aperture in the shutter wall](#2-what-a-gate-is--one-aperture-in-the-shutter-wall)
3. [The 52-family design space](#3-the-52-family-design-space)
4. [The method step by step](#4-the-method-step-by-step)
5. [The positive controls PC1/PC2 — why a NO needs witnesses](#5-the-positive-controls-pc1pc2--why-a-no-needs-witnesses)
6. [Results](#6-results)
7. [How to read the numbers](#7-how-to-read-the-numbers)
8. [Interpretation — what H2 = NO does and does not say](#8-interpretation--what-h2--no-does-and-does-not-say)
9. [Reproduction](#9-reproduction)
10. [Data and figures](#10-data-and-figures)
11. [Verdict](#11-verdict)
12. [Glossary of gate terminology](#12-glossary-of-gate-terminology)
13. [FAQ](#13-faq)
14. [See also](#14-see-also)

---

## 1. The question

Campaign C3 asks the sharpest question the Hilbert–Pólya programme allows a
numerical experiment to ask. Not "do these lattices look GUE-like?" — that is
question H3, and the answer there is yes. Not "do the zeros obey RH in the
checked band?" — that belongs to other campaigns. C3 asks:

> Does a gate exist — a vortex-cloud configuration — whose spectrum is
> identical to the zeta zero spectrum under the correspondence
> **level n ↔ zero n**?

Identity is a stronger demand than any statistical resemblance. Statistics
survive reshuffling; identity does not. Operationally, C3 defines identity as
correlation **+1** between the unfolded gate spectrum and the unfolded zero
sequence — the value the same pipeline returns, to nine and twelve decimal
places, on the two positive controls where the correspondence holds by
construction. Everything short of +1 is graded against a *measured* chance
distribution, built from 64 shifted zero lists and 40 GUE matrices, so that
"close" is never a matter of taste.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Bernhard Riemann avatar"/></p>

*Riemann's zeros are the target pattern; the campaign's contribution is to
show, with certified instruments, how far the nearest lattice aperture sits
from transmitting it.*

The verdict, in one line: **no identity — the gates sit at the
surrogate-null saturation level of the D_nn metric (0.0079 vs 0.0079 ± 0.0005
for random surrogates; the identity controls' floors are machine precision,
not a scale — correction v2.0.1)** — with the controls proving the
measuring device works.

---

## 2. What a gate is — one aperture in the shutter wall

The hero image above is the campaign in one picture: a wall, and shutters cut
into it. Behind the wall stands the arithmetic of the zeta zeros; in front of
it, a family of 52 Hermitian lattice Hamiltonians. Each **gate** — Russian
"затвор", a shutter — is one aperture: open it (build the Hamiltonian,
diagonalise it) and some pattern of spectral light falls through. The
campaign's question is whether *any* aperture transmits the exact pattern of
the zeros, level for level.

A gate is not hardware. The source is explicit: the term is a construct of
this series, denoting a parametrised family of Hermitian Hamiltonians, not a
physical device. "Opening a shutter" means calling `eigvalsh`; the "light" is
the eigenvalue list.

What shapes the aperture is the **vortex cloud**. The underlying lattice is a
24×24 Hofstadter system — hoppings −t·e^{iφ} with Landau-gauge flux
φ_x = 2πα·iy on the x-links — decorated, on the y-links, with vortex phases
φ_y = Σ_k q_k(θ_j − θ_i)/2. Each vortex k carries a charge q_k and sits at a
position whose polar angle θ about the lattice centre is measured with atan2;
the protocol evaluates these angle differences raw, with no periodic wrapping
(the exact C3 protocol, part of the bit-exact reproduction contract). The
**vortex positions and charges are the handles** of the family — the knobs
that actually reshape the spectrum — and around them the protocol adds three
more: the vortex count Nv, the on-site disorder W, and the flux line α. The
campaign lives mostly on the self-dual line α = 1/2 (π flux per plaquette,
where the lattice realises a discretised massless Dirac equation — question
H4), with gates stressed off the line at α = 0.4.

Because the Hamiltonian is Hermitian by construction, every gate passes
question H1 (self-adjointness) for free: its spectrum is real to machine
precision. What no construction guarantees is *which* real numbers appear —
and that is precisely what H2 asks and C3 measures.

---

## 3. The 52-family design space

The committed family is tabulated in `data/gates_table.csv` (52 rows) and in
the `family` list of `data/results.json`. Its protocol tag is H7 — the rank
statistic r_H7 is named for it.

| Knob | Meaning | Values swept in C3 |
|---|---|---|
| Nv | number of vortices | 0, 2, 8, 16, 32 |
| q | vortex charge magnitude | 0.0, 0.5, 1.0 |
| W | on-site disorder strength | 0.0, 0.5, 1.0 |
| α | flux per plaquette | 0.4, 0.5 |

Quick reading notes:

- **52 unique configurations, master seed 96** — the vortex coordinates of
  every gate are fixed by that one seed; the family is split evenly, 26 gates
  on the half-flux line and 26 at α = 0.4.
- The **Nv = 0 rows** are vortex-free references — clean and disordered
  Hofstadter lattices — and provide the family's best candidate, which is
  itself a hint: decoration does not help.
- The sweep covers behaviours rather than favourites: vortex-rich and
  vortex-free, clean and disordered, on and off the self-dual line. The C3
  protocol froze the 52 configurations before any spectrum was scored; the
  extended handle set (twists, anisotropy, δα, staggered mass, vortex
  profile, charge signs) belongs to campaign C5 and is held at defaults here.

---

## 4. The method step by step

One deterministic pipeline, applied identically to all 52 gates, both null
ensembles, and both controls. Protocol constants: L = 24, K = 200,
poly_deg = 6, zero window starting at γ₀ = 500.309084942, null_shifts = 64,
null_gue = 40.

1. **Configure.** Vortices at cell centres, neutral charges (protocol
   wording), coordinates from the master-seed-96 stream.
2. **Decorate.** Landau-gauge flux on x-links, raw vortex angle differences
   on y-links, disorder W on site → Hermitian Hamiltonian
   (`engine/hamiltonian.py`).
3. **Diagonalise.** `eigvalsh` → 576 = 24² real eigenvalues.
4. **Band.** Keep the central 0.6 fraction of the spectrum: **344 levels**.
5. **Unfold.** Fit a **degree-6 polynomial** to the integrated density, divide
   it out, and take the innermost **200-level window** — unit mean spacing,
   trends removed, only the stochastic skeleton left.
6. **Zero side.** The smooth **Riemann–von Mangoldt count**; 200 consecutive
   zeros from γ₀ = 500.309084942, unfolded the same way.
7. **Score.** Three statistics on the pair of unfolded sequences:
   **r_H7** (correlation with linear ramps excluded; +1 would certify
   identity), **D_nn** (nearest-neighbour discrepancy after an optimised
   relative shift, always in [−1, 1] — no gate can lose on a technical
   misalignment), and **KS_sp** (Kolmogorov–Smirnov on the spacing
   distributions).
8. **Null clouds.** 64 shifted copies of the zero list (decoys, nullA) and 40
   GUE matrices (nullB) pass through steps 3–7 unchanged. Every p-value is
   then empirical: the fraction of the null cloud at least as identity-like
   as the gate, with the add-one convention.

Why ranks and not least squares: identity is an *ordering* statement. Rank
statistics with ramps removed respond to ordering and to nothing else, so a
smooth trend or a scale convention cannot fake correspondence; a least-squares
distance, by contrast, is dominated by exactly such artefacts. Under identity
the ranks align and r_H7 → +1; under chance the ranks look like the
permutation clouds — which is what all 52 gates do.

One caution printed on the box: the ⟨r⟩ = 0.32 level clustering of the clean
lattice is a **localization effect**, not kinship with ζ. Clustering has a
lattice mechanism of its own; the verdict does not mistake it for arithmetic.

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="120" alt="Agent Lyra avatar"/></p>

*Agent Lyra measured the spectra — one pass per gate, windows frozen in
advance, no statistic retuned after the fact.*

---

## 5. The positive controls PC1/PC2 — why a NO needs witnesses

An instrument that reports "nothing detected" is meaningless until it is shown
to detect. C3 therefore carries two positive controls through the identical
pipeline — same band, same unfolding, same statistics, same null machinery —
on inputs where the correspondence is true by construction. They are the
reason the negative verdict has force.

**PC1 · the spinor64 isospectral twins.** Two Hermitian Hamiltonians whose
spectra agree by an exact symmetry; the level-n ↔ level-n mapping is a
theorem, not a hypothesis. The pipeline certifies it:

| Quantity | PC1 value |
|---|---|
| r_H7 | 1.000000000 |
| D_nn | 2.7e-14 |
| max matched-eigenvalue deviation (max_dlambda) | 6.217248937900877e-15 |
| shift | 0.0 |

Matched eigenvalues agree to ~6e-15 — the noise floor of double precision.

**PC2 · the graph against the file.** The stage-2 identity function
Z_id(t) = e^{iθ(t)}ζ(½+it), sampled at its K = 79 zeros, is compared with the
committed zero file:

| Quantity | PC2 value |
|---|---|
| r_H7 | 1.000000000000 |
| D_nn | 1.2e-10 |
| max matched-zero deviation (max_dgamma) | 4.98147301186691e-10 |
| K (levels compared) | 79 |

The two controls calibrate the detection floor of the method: D_nn ≈ 1e-10
for graph-level identity, D_nn ≈ 1e-14 for operator-level identity. The best gate (by r_H7) reaches D_nn = 0.007914719356298686, the
family minimum is 0.006937508455596089. The distance between those
numbers is
the corrected headline of the series (anchored on the graph ↔ operator
comparison recorded in `results/RESULTS.md` and the theory map; against PC1
the separation is larger still). The gap is not a vagueness — it is the
reason "maybe the method just can't resolve identity" is unavailable here.

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="120" alt="Agent Vera avatar"/></p>

*Agent Vera guarded the controls: the verdict H2 = NO was admissible only
because PC1 and PC2 passed first — the pipeline demonstrably sees identity at
the 1e-14 level whenever identity exists.*

---

## 6. Results

### 6.1 Headline table (as committed)

| Quantity | Value | Status |
|---|---|---|
| Family | 52 unique configurations, master seed 96 | protocol C3 |
| Best r_H7 | 0.226 (p = 0.169, Bonferroni 0.80) | no identity |
| Decoys / GUE null | 0.026±0.140 / −0.014±0.127 | null zones |
| PC1 spinor64 twins | r = 1.000000000, D_nn = 2.7e-14 | method sees identity |
| PC2 graph ↔ file | r = 1.000000000000, D_nn = 1.2e-10 | method sees identity |
| Graph ↔ operator relation | none: D_nn at surrogate-null level | the series verdict |

*Family row.* The sweep is the protocol: 52 unique (Nv, q, W, α)
configurations on one master seed. Nothing was added, dropped, or retuned
after spectra were measured.

*Best r_H7 row.* 0.226 is the largest rank correlation any gate achieved with
the zero sequence; p = 0.169 is its empirical permutation p-value and 0.80
the family-wise Bonferroni figure. Inside the null zone, not outside it.

*Decoys / GUE null row.* The two chance distributions of r_H7: 0.026±0.140
from 64 shifted zero lists, −0.014±0.127 from 40 GUE matrices. The best gate
lives inside both.

*PC1 / PC2 rows.* The controls, at r = 1.000000000 and r = 1.000000000000 —
identity is visible to the method when present, down to D_nn = 2.7e-14 and
1.2e-10 respectively.

*Gap row.* Best gate D_nn (0.007914719356298686) versus the surrogate null
(0.0079 ± 0.0005): the null-level saturation that defines the series' verdict for H2.

### 6.2 The best gate in detail

From `verdict.best_gate` in `data/results.json` — a vortex-free Hofstadter
reference, (Nv, q, W, α) = (0, 0.0, 0.5, 0.5):

| Field | Value |
|---|---|
| mean_spacing | 0.011981804524559426 |
| r_H7 | 0.22641576150208137 |
| D_nn | 0.007914719356298686 |
| shift | 0.8 |
| KS_sp | 0.7336683417085427 |
| p_r | 0.16923076923076924 |
| p_D | 1.0 |
| p_KS | 1.0 |
| r_GUE_z | 1.8936817833815616 |

The three statistics disagree about this gate — best by r_H7, mid-pack by
D_nn, worst by KS_sp (its spacing distribution is farther from the zeros'
than every decoy's). Identity would move all three together; a fluctuation
moves one. And the winner being the *undecorated* lattice says, on its own,
that vortex decoration did not push the family toward the zeros.

### 6.3 The null zones

| Null ensemble | Composition | mean ± spread of r_H7 |
|---|---|---|
| Decoys (nullA) | 64 shifted zero lists (null_shifts = 64) | 0.026±0.140 |
| GUE null (nullB) | 40 GUE matrices (null_gue = 40) | −0.014±0.127 |

These clouds are the campaign's definition of "chance". The best gate's 0.226
sits within them (r_GUE_z = 1.8936817833815616 against the GUE cloud) —
ordinary fluctuation territory, a different universe from r = 1.000000000.

### 6.4 Across the whole family

Grounded in `data/gates_table.csv` (columns
`Nv,q,W,alpha,mean_spacing,r_H7,D_nn,shift,KS_sp,p_r,p_D,p_KS,r_GUE_z`):

| Statistic | min | max | notes |
|---|---|---|---|
| r_H7 | −0.168447299012455 | 0.22641576150208137 | 36 of 52 positive, 16 negative, 7 above +0.2 |
| D_nn | 0.006937508455596089 | 0.009221555365816578 | all within ±20% of the GUE surrogate null 0.0079 |
| mean_spacing | 0.011981804524559426 | 0.01272797005910956 | mild variation across gates |
| r_GUE_z | −1.2152397215832413 | 1.8936817833815616 | no outlier against the GUE null |

The smallest raw p-value anywhere in the table is p_D = 0.015384615384615385
(five gates: (8, 1.0, 0.0, 0.5), (8, 0.5, 1.0, 0.4), (8, 1.0, 1.0, 0.4),
(16, 1.0, 1.0, 0.4), (32, 1.0, 1.0, 0.4)); the Bonferroni correction consumes it several times over
before any claim of significance could start.

---

## 7. How to read the numbers

**p = 0.169 is a fraction of the null cloud, not a normal table lookup.**
With null_shifts = 64 decoys and the add-one convention, every p-value is
k/65: the count of decoys at least as identity-like as the gate, plus one,
over 65. The best gate's p_r = 0.16923076923076924 is exactly 11/65 — ten
shuffled zero lists beat or matched its r_H7. Read it plainly: under "no
identity", roughly one honest draw in six looks this identity-like.

**Bonferroni 0.80 is the look-elsewhere correction.** Scoring 52 gates × 3
statistics means many chances for a small p. The family's smallest raw
p-value, 1/65 = 0.015384615384615385, multiplied by the 52 tests, gives the
recorded family-wise floor `min_p_bonferroni` = **0.8**. After the
correction, nothing in the family is anywhere near significant — the
"no identity" conclusion is immune to selection effects.

**r_GUE_z is a z-score.** Distance, in GUE-null standard deviations, between
the gate's r_H7 and the GUE cloud's mean; +1.89 at best, negative for much of
the family. Useful for ranking, not a p-value.

**The floors are the fixed points of the reading.** Every interpretation
comes back to the same comparison: gates at D_nn ≈ 0.0078, surrogate nulls at 0.0079 ± 0.0005, controls at
1.2e-10 and 2.7e-14. p-values, z-scores and KS statistics all tell the same
story from different angles because the metric itself separates the two
regimes in one step: identity at machine precision, everything else at the
common 0.0079 saturation level ≈ 2/n (v2.0.1 correction — "orders" retired).

---

## 8. Interpretation — what H2 = NO does and does not say

**It says:** within the vortex-lattice class defined by (Nv, q, W, α), no
gate carries the zero spectrum. The recorded conclusion translates as: *no
gate is distinguishable from the permutation null model — H2 remains closed,
now with the method's power measured.* The "power measured" clause is the
point: the campaign quantifies what its own instrument can see (identity at
1e-10 to 1e-14) and reports the gates' position against the surrogate null
(at saturation — indistinguishable from random).

**It is measured three ways.** C3 is the rank-metric projection (null
orders); campaign C4 recasts the question thermally (≈0.5 order there); C5
confirms stability across the extended handle set. Three independent
projections of one question agree — the methodological core of the series.

**It is falsifiable.** A single gate from this class that, through the same
frozen pipeline, returns r_H7 ≈ 1 with D_nn at or below 1e-10 and a
permutation p surviving the 52-fold correction would overturn the verdict.
Register it first; let the controls re-certify the run; the claim would then
be unambiguous.

**It does not say:** that the Hilbert–Pólya programme fails, or that RH is
false, or that no operator can ever carry the zeros. The scope is local
lattice Hamiltonians with vortex phases; nonlocal constructions are an open
roadmap question. And the co-recorded verdicts frame the result precisely:
H1 YES (self-adjoint by construction), H3 YES (GUE statistics — universality,
which erases arithmetic and makes H2 hard), H4 YES (Dirac dynamics), H2 NO
(zeros encoded, not generated).

---

## 9. Reproduction

```bash
# tour of the verdict (~seconds, no zero file needed)
python3 campaigns/run_c3_gates.py
```

- The series seed is **96**; RNG streams are fixed in
  `engine/hamiltonian.py`, so vortex coordinates and disorder realisations
  are identical on every machine and every run.
- Vortex phases use **raw angle differences** — the exact C3 protocol; no
  wrapping shortcuts. This is part of the bit-exactness contract.
- Dependencies are pinned in `requirements.txt`; the tour needs no zeta zero
  file on input (the zero window, γ₀ = 500.309084942, K = 200, is committed
  protocol data).
- **Bit-exact solver protocol:** the engine's equivalence control replays the
  committed `mean_spacing` column for all gates — 52/52 bit-for-bit at
  |Δ| < 1e-10, with the recorded maximum deviation |Δ| = 1.45e-16 (the
  protocol reproduction credited to C4 in `results/RESULTS.md`). Any
  reimplementation that misses this tolerance is not running the C3 protocol.

---

## 10. Data and figures

### Figures

| File | Where |
|---|---|
| `fig05_gates_en.png` | 600 dpi — `figures_hires/en/fig05_gates_en.png`; screen — `figures/en/` |
| `fig05_gates.png` | 600 dpi — `figures_hires/ru/fig05_gates.png`; screen — `figures/ru/` |

### Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

The full monograph of this computation (statement, theorems, tables, figures,
honest limitations): 7–9 pages, the same content in both languages.

### Data

| File | Contents |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/gates_table.csv` | the 52-gate table (all statistics and p-values, one row per gate) |
| `data/` (npz/csv) | curves and tables |
| `../data/c3_*.json` | duplicate of the verdict in the shared registry |

`data/results.json` carries: `meta` (L = 24, K = 200, poly_deg = 6,
zero_window_gamma0 = 500.309084942, null_shifts = 64, null_gue = 40,
date 2026-10-10), the `family` list (52 gates), the null clouds `nullA` and
`nullB`, the controls `PC1_spinor_twins` and `PC2_graph`, and the `verdict`
block (n_gates = 52, best_gate, min_p_bonferroni = 0.8, identity_found =
false, pc1_r = 1.0, pc2_r = 1.0000000000000004). Independent re-checks live
in `independent_verification/` (the IVP checks of this campaign).

---

## 11. Verdict

**{'ru': 'Г2 — НЕТ (тождества нет), измерено с PC1/PC2', 'en': 'H2 — NO (no identity), measured with PC1/PC2'}** — details: `data/results.json`, the monograph, and
`independent_verification/` (the IVP checks of this campaign).

> H2 is a negative verdict, but the method earned it only after the positive
> controls: PC1/PC2 show the pipeline sees identity at the 1e-14 level when it
> exists. The term *gate* is a construct of this series; it denotes a
> parametrised family of Hermitian Hamiltonians, not a physical device.

---

## 12. Glossary of gate terminology

| Term | Meaning in this campaign |
|---|---|
| Gate (затвор, shutter) | A parametrised Hermitian Hamiltonian — a vortex-decorated Hofstadter lattice; an aperture in the shutter-wall metaphor, not a device. |
| Shutter wall | The family of all 52 apertures; opening one means diagonalising its Hamiltonian. |
| Vortex | A phase singularity pinned in the lattice; carries a charge q_k at a position with atan2 angle θ about the centre. |
| Handle | A knob of the family: Nv, q, W, α in C3; twists, anisotropy, δα, mass, profile, charge signs in C5. |
| π flux / self-dual line (α = 1/2) | Half a flux quantum per plaquette; the line where the lattice realises discretised massless Dirac dynamics (H4). |
| Unfolding | Dividing out a degree-6 polynomial fit to the integrated density so levels have unit mean spacing. |
| Ramps | Residual linear trends removed before correlating, so no smooth drift can fake correspondence. |
| r_H7 | Correlation of the unfolded gate and zero sequences, ramps excluded; +1 certifies the level-n ↔ zero-n identity. |
| D_nn | Nearest-neighbour discrepancy between unfolded sequences after an optimised shift in [−1, 1]; floors 2.7e-14 (PC1) and 1.2e-10 (PC2). |
| KS_sp | Kolmogorov–Smirnov statistic between the spacing distributions of the two sequences. |
| Decoys (nullA) | 64 shifted copies of the zero list — the empirical no-identity cloud for r_H7. |
| GUE null (nullB) | 40 Gaussian unitary ensemble matrices — the universality baseline. |
| Permutation p-value | k/65: the null fraction at least as identity-like as the gate, add-one convention. |
| Bonferroni 0.80 | 52 × (1/65): the family-wise floor after correcting for all tests. |
| mean_spacing | Mean level spacing of the central band (≈ 0.012); the column reproduced bit-for-bit in the equivalence control. |
| IVP | The independent verification protocol; its checks of C3 live in `independent_verification/`. |

---

## 13. FAQ

**Q1. What does the label H7 refer to?**
The protocol tag of this gate family; the rank statistic r_H7 is named after
it. The question the campaign tests is H2 of the series' tablet — spectral
identity — which is a different numbering and should not be confused with the
family tag.

**Q2. Why two null clouds instead of one formula?**
Because they answer different objections. The decoy cloud (shifted zero
lists) models "same zeros, broken correspondence" — exactly the alternative
that matters for identity. The GUE cloud models "generic universal spectrum".
A gate must escape both to claim anything; escaping neither, as all 52 do,
closes the question cleanly.

**Q3. The best gate is the vortex-free lattice. Does that mean vortices were
a dead end?**
Within this class and this protocol, yes as measured: the undecorated π-flux
reference (Nv, q, W, α) = (0, 0.0, 0.5, 0.5) tops the table at
r_H7 = 0.22641576150208137, and decoration never beats it. The campaign's
claim is about this family; C5 explores whether more handles change the
picture (they do not change the verdict).

**Q4. How does the null-level verdict here relate to C4's ≈0.5 order figure?**
Two metrics, one question. C3 measures the gap in the rank metric D_nn
(gates ≈ 0.26 against control floors of 1e-10 and 1e-14); C4 measures it in a
thermal (heat-kernel) metric, where the separation is ≈0.5 order. The theory
map records both projections, and their agreement in sign — both NO — is the
methodological point.

**Q5. Can I test my own configuration with this pipeline?**
Yes, under the same discipline: build the Hamiltonian with the documented
handles in `engine/hamiltonian.py`, keep the windows and unfolding frozen
(band 0.6 → 344 levels, degree-6 polynomial, K = 200 window), regenerate both
null clouds, run PC1/PC2 first, and apply the 52-fold multiplicity
correction appropriate to the number of candidates you score. A result
without the controls is not a C3-style result.

**Q6. Where is the line between what is measured and what is conjectured?**
Measured: the spectra, the statistics, the null clouds, the control floors,
the verdict for this class. Conjectural: identifying the α = 1/2 dynamics
line with the critical line Re(s) = 1/2 — the package keeps that bridge
explicit and separates it from everything measured here.

---

## 14. See also

- [C5 · Gates extended](../C5_gates_extended/README.md) — the extended handle
  set and the stability of H2 = NO across it.
- [C4 · Trace formula](../C4_trace_formula/README.md) — the thermal projection
  of the identity question and the |Δ| = 1.45e-16 protocol reproduction.
- [engine/README.md](../../engine/README.md) — Hamiltonian and solver modules,
  the raw-angle C3 protocol, and the 52/52 bit-exact equivalence control.
- [docs/theory.md](../../docs/theory.md) — the five-station map, the tablet
  H1–H5, and the package's claims and non-claims.

---

*Hilbert Polya Bridge v1.0.0 · C3 · The H7 gate family*

