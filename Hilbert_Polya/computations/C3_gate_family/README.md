# C3 · The H7 Gate Family — the definitive guide to the 52-gate vortex-lattice search

![version](https://img.shields.io/badge/version-2.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_vortex_lattice.png" width="720" alt="A 24×24 vortex lattice at half flux: charged vortices pin phase windings into a Hofstadter-type Hamiltonian, and the campaign asks whether any of the 52 shutters lets through the spectrum of the zeta zeros"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

<p align="center"><em>Curated by the Bridge avatar cast — Agent Atlas directed the gate designs, Agent Lyra measured the spectra, Agent Vera guarded the controls.</em></p>

> **TL;DR — 52 gates (Nv × q × W × α) on a 24×24 lattice with π flux; the spectral-identity question H2; permutation nulls; positive controls PC1/PC2; verdict: no identity — gates at the surrogate-null level of D_nn (0.0079 vs 0.0079 ± 0.0005 for random surrogates; v2.0.1).**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Claim under test | H2 — does a gate exist — a vortex-cloud configuration — whose spectrum is *identical* to the zeta zero spectrum under the correspondence **level n ↔ zero n**? |
| Verdict | H2 — NO (no identity), measured with PC1/PC2 |
| Family | 52 gate configurations, master seed 96 |
| Best rank correlation with the zeros | r_H7 = 0.226 (p = 0.169, Bonferroni 0.80) |
| Null zones (r_H7) | decoys 0.026±0.140 · GUE −0.014±0.127 |
| Identity controls | PC1 r = 1.000000000 · PC2 r = 1.000000000000 |
| Detection floor | D_nn = 2.7e-14 (PC1) · 1.2e-10 (PC2) |
| Best gate vs surrogate null | ≈ 0.0079 in D_nn — at saturation (≈2/n), indistinguishable from random |
| Best gate | vortex-free reference (Nv, q, W, α) = (0, 0.0, 0.5, 0.5) |
| One-line meaning | no gate is distinguishable from the permutation null model, while the pipeline sees identity at the 1e-14 level whenever it exists |

Reproduction at a glance:

```bash
# tour of the verdict (~seconds, no zero file needed)
python3 campaigns/run_c3_gates.py
# committed verdict of the campaign — data/results.json
# the 52-gate table (all statistics and p-values) — data/gates_table.csv
# 600 dpi figures — figures_hires/ru/fig05_gates.png · figures_hires/en/fig05_gates_en.png
# monographs — monograph_ru.docx · monograph_ru.pdf · monograph_en.docx · monograph_en.pdf
```

Every number in this card is traceable to `data/results.json` or `data/gates_table.csv`.

## Contents

- [Quick reference card](#quick-reference-card)
1. [The campaign question](#1-the-campaign-question)
2. [What a gate is — shutters, light, and vortex handles](#2-what-a-gate-is--shutters-light-and-vortex-handles)
3. [The 52-family design space](#3-the-52-family-design-space)
4. [The method step by step](#4-the-method-step-by-step)
5. [The positive controls PC1 and PC2 — why a NO needs witnesses](#5-the-positive-controls-pc1-and-pc2--why-a-no-needs-witnesses)
6. [Results](#6-results)
7. [How to read the numbers](#7-how-to-read-the-numbers)
8. [Interpretation — H2 = NO at the surrogate-null level](#8-interpretation--h2--no-at-the-surrogate-null-level)
9. [Reproduction](#9-reproduction)
10. [Data and figures](#10-data-and-figures)
11. [Verdict](#11-verdict)
12. [Glossary of gate terminology](#12-glossary-of-gate-terminology)
13. [FAQ](#13-faq)
14. [See also](#14-see-also)

---

## 1. The campaign question

The Hilbert–Pólya programme imagines the non-trivial zeros of the Riemann zeta
function as eigenvalues of a self-adjoint operator. Campaign C3 takes that
imagination literally and puts a concrete numerical question to a concrete
family of operators:

> Does a gate exist — a vortex-cloud configuration — whose spectrum is
> *identical* to the zeta zero spectrum under the correspondence
> **level n ↔ zero n**?

The operative word is *identical*. Spectral identity is strictly stronger than
a statistics match. Two unrelated Hermitian matrices can both look GUE-like in
their spacing distributions; that comparison says nothing about which level
sits where. Identity demands something far more brittle: after unfolding both
sequences to unit mean spacing, the n-th gate level must track the n-th zeta
zero across the whole comparison window, so that the correlation between the
two unfolded sequences is +1 — the value the pipeline in fact returns when it
is handed two copies of the same spectrum.

A +1 correlation cannot be approached gradually and honestly claimed
"almost". Either the correspondence holds level by level, or it does not hold
at all, and everything in between is noise. That is why C3 is designed as a
detection experiment rather than a fitting exercise:

- the family of candidate operators is swept broadly (52 gate configurations,
  Section 3);
- under the null hypothesis "no identity", the statistic r_H7 has a *measured*
  distribution, built from permutation controls (64 shifted zero lists and
  40 GUE matrices), so every gate can be scored against an empirical yardstick
  rather than an asymptotic formula;
- two positive controls are carried through the identical pipeline — the
  spinor64 isospectral twins (PC1) and the stage-2 graph against the committed
  zero file (PC2) — on which the method is *obliged* to see identity and does,
  at r = 1.000000000 and r = 1.000000000000 respectively — identity to nine and
twelve decimal places.

The verdict of the campaign is the third item of the bridge's scoreboard
(question H2 of the Hilbert–Pólya tablet): **no identity**, with the best gate sitting at the
saturation level of the D_nn metric (0.0079 — numerically the same as the
random-surrogate nulls 0.0079 ± 0.0005), infinitely far from identity in rank
but carrying no graded "distance": D_nn is a bounded metric (correction
v2.0.1). The rest of this document
explains what a gate is, how the measurement works, why the negative verdict
is trustworthy, and how to reproduce every number.

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="120" alt="David Hilbert avatar"/></p>

*Hilbert asked whether the zeros could be eigenvalues. C3 answers with a
measurement: for the 52-gate vortex family, they are not — and the instrument
that says so has been certified on controls where the answer is YES.*

---

## 2. What a gate is — shutters, light, and vortex handles

### The shutter metaphor

Picture a dark wall pierced by shutters, and behind it a lamp whose light is
the spectrum of the zeta zeros. Each **gate** is one shutter: an aperture whose
internal geometry decides which "colours" — which level positions — pass
through the wall. Opening a shutter means building the corresponding Hermitian
Hamiltonian and diagonalising it; photographing the arriving light means
reading off its eigenvalues, unfolding them, and comparing with the zeros.

No single shutter in this campaign transmits the zeta pattern. The wall,
however, is not decorative: the 52 apertures are placed so that the *family*
of transmitted patterns is broad enough that a trivial "no" would have been
surprising. The illustration `ill_shutter_wall.png` in the shared assets
depicts this wall of apertures; the hero image above shows one aperture opened
— the vortex lattice itself.

The word *gate* (Russian "затвор", shutter) is a construct of this series. It
denotes a parametrised family of Hermitian Hamiltonians, not a physical
device. No claim is made that such a lattice could be built in a laboratory
and interrogated with physical light; the "light" is always the eigenspectrum
computed by a deterministic solver.

### The vortex handles

Concretely, a gate is a 24×24 lattice whose hoppings carry phases, of two
kinds (all constructions live in `engine/hamiltonian.py`):

- **Landau-gauge flux** on x-links: φ_x = 2πα·iy, the Hofstadter construction,
  with α the flux per plaquette in units of the flux quantum. The series lives
  on the self-dual line α = 1/2 — π flux per plaquette — where the lattice
  realises a discretised massless Dirac equation (question H4 of the tablet);
  C3 additionally stresses gates off that line at α = 0.4.
- **Vortex phases** on y-links: φ_y = Σ_k q_k(θ_j − θ_i)/2, where the sum runs
  over the vortices k, q_k is the charge of vortex k, and θ is the polar angle
  of a link endpoint about the lattice centre (the atan2 angle). The C3
  protocol computes these angle differences *raw* — no periodic-wrapping
  shortcut — which is part of the bit-exact reproduction contract
  (Section 9).

The **vortex positions and charges are the handles**: the knobs a locksmith
can actually grab to reshape the transmitted spectrum. Around them, the
protocol fixes three more handles — the vortex count Nv, the on-site disorder
strength W, and the flux line α. A gate is therefore fully specified by the
quadruple (Nv, q, W, α) together with the vortex coordinates drawn from the
master seed. Everything else in the engine — twists (φx, φy), anisotropy
t_x/t_y, the flux shift δα, a staggered mass m, the vortex profile
(site/midpoint), and charge signs — belongs to the extended handle set of
campaign C5 and is held at its C3 default here.

One more property matters for the interpretation: a gate built this way is
Hermitian *by construction*, so its spectrum is real to machine precision —
this is the architectural fact behind verdict H1 (self-adjointness) of the
tablet. What a gate cannot guarantee is *which* real numbers it produces. That
is the entire content of H2, and it is what C3 measures.

---

## 3. The 52-family design space

The family is recorded in `data/gates_table.csv` (52 rows, one per gate) and
summarised in the `family` list of `data/results.json`. The protocol label of the family is H7, and
the rank statistic r_H7 takes its name from this tag.

| Knob | Meaning | Values swept in C3 |
|---|---|---|
| Nv | number of vortices decorating the lattice | 0, 2, 8, 16, 32 |
| q | vortex charge magnitude | 0.0, 0.5, 1.0 |
| W | on-site disorder strength | 0.0, 0.5, 1.0 |
| α | flux per plaquette | 0.4, 0.5 |

Reading the design space:

- The sweep contains **52 unique configurations** (protocol C3), drawn with a
  **master seed 96** that fixes the vortex coordinates for every gate; the
  half-flux line α = 1/2 and the off-line value α = 0.4 carry 26 gates each.
- Nv = 0 gates are the vortex-free references: clean or disordered Hofstadter
  lattices at π flux against which the decorated gates can be compared. The
  best gate of the family turns out to be one of these references
  (Section 6.2).
- q = 0 rows with Nv > 0 probe vortices whose charge magnitude vanishes — the
  phase decoration is present in the engine's bookkeeping but carries no
  winding weight.
- The full combinatorial grid over these four knobs is larger than 52; the C3
  protocol selects the committed 52 and freezes them. Nothing in the analysis
  adapts to the data after the fact: no gate was added, dropped, or retuned
  after its spectrum was measured.

<p align="center"><img src="../../assets/avatars/hp_agent_atlas.svg" width="120" alt="Agent Atlas avatar"/></p>

*Agent Atlas directed the gate designs: the point of the sweep is coverage of
behaviours — vortex-rich and vortex-free, clean and disordered, on and off the
self-dual line — not a search tuned to a favourite configuration.*

---

## 4. The method step by step

The pipeline is deterministic end to end; every step below is executed
identically for each of the 52 gates, for both null ensembles, and for both
positive controls. This is what makes the numbers comparable at all.

**Protocol constants:** L = 24, K = 200, poly_deg = 6, zero window starting at
γ₀ = 500.309084942, null_shifts = 64, null_gue = 40.

1. **Build the vortex configuration.** Vortices are placed at cell centres
   with neutral charges (the protocol wording of the source); their
   coordinates come from the master-seed-96 stream.
2. **Decorate the lattice.** Hoppings −t·e^{iφ} on the 24×24 lattice receive
   the Landau-gauge flux φ_x = 2πα·iy on x-links and the raw vortex angle
   differences on y-links, plus on-site disorder of strength W. The result is
   a Hermitian Hamiltonian (`engine/hamiltonian.py`).
3. **Diagonalise.** `eigvalsh` returns the real spectrum — 576 = 24²
   eigenvalues, real to machine precision by construction.
4. **Window the spectrum.** The central band holding a 0.6 fraction of the
   spectrum is retained: **344 levels** for L = 24.
5. **Unfold.** A **degree-6 polynomial** is fitted to the integrated density
   of the band and divides it out, flattening the sequence to unit mean
   spacing; the innermost **200-level window** (K = 200) is taken for
   comparison. Unfolding removes smooth trends so that only the *stochastic
   skeleton* of the spectrum remains.
6. **Prepare the zero side.** The comparison target is the smooth
   **Riemann–von Mangoldt count**: 200 consecutive zeta zeros, the window
   beginning at γ₀ = 500.309084942, unfolded the same way.
7. **Score.** Three statistics compare the two unfolded sequences:
   - **r_H7** — the correlation between the two sequences with linear ramps
     excluded; +1 would mean the level-n ↔ zero-n correspondence holds
     throughout the window;
   - **D_nn** — a nearest-neighbour discrepancy between the sequences,
     evaluated after optimising a relative shift (the per-gate optimum is
     recorded in the `shift` column and always lies in [−1, 1], so no gate can
     fail merely because of a global misalignment);
   - **KS_sp** — a Kolmogorov–Smirnov statistic on the spacing distributions.
8. **Build the null clouds.** Under "no identity" the statistic values are not
   assumed — they are generated:
   - **nullA, the decoys** — 64 shifted copies of the zero list, each
     correlated against the gate spectrum exactly as the true zero list would
     be (null_shifts = 64);
   - **nullB, the GUE null** — 40 matrices from the Gaussian unitary ensemble
     treated identically (null_gue = 40).
   A gate's p-value is then an *empirical* permutation p-value: the fraction
   of null members at least as identity-like as the gate, with the add-one
   convention (Section 7).

Two remarks on choices that are easy to misread.

**Why rank correlation and not least squares?** A least-squares fit between
two spectra is dominated by whatever smooth trend survives unfolding and by
the largest outliers; it can be made to look respectable by a dozen
well-placed levels. Rank statistics do the opposite: they are insensitive to
any monotone reparametrisation and respond only to the *ordering* of levels —
which is exactly what the level-n ↔ zero-n correspondence is about. If the
correspondence holds, the ranks align and r_H7 → +1; if it fails, the ranks
are as random as the permutation nulls. The "ramps excluded" clause removes
the last residual trend so that a slow drift cannot masquerade as
correspondence.

**The clean lattice is not a near miss.** The adjacent-gap clustering
⟨r⟩ = 0.32 of the clean lattice is a **localization effect**, not kinship with
ζ. Level clustering induced by localized modes is a lattice phenomenon with
its own mechanism; it should not be read as the gates "approaching" the zeta
statistics, and the verdict does not treat it that way.

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="120" alt="Agent Lyra avatar"/></p>

*Agent Lyra measured the spectra: one deterministic pass per gate, no
post-hoc window shopping — the 344-level band, the degree-6 unfolding and the
200-level window were fixed before any gate was scored.*

---

## 5. The positive controls PC1 and PC2 — why a NO needs witnesses

A negative verdict is only as strong as the instrument that produced it. A
pipeline that cannot detect identity when it is present would report "no
identity" on *any* input, and its NO would be worthless. C3 therefore ships
with two positive controls run through the identical pipeline — same window,
same unfolding, same statistics, same null machinery — on inputs where the
correct answer is known to be YES.

**PC1 — the spinor64 isospectral twins.** Two Hermitian Hamiltonians whose
spectra coincide by construction: an exact symmetry maps one operator onto the
other, so the level-n ↔ level-n correspondence is not a hypothesis but a
theorem. The pipeline reads:

| Quantity | PC1 value |
|---|---|
| r_H7 | 1.000000000 |
| D_nn | 2.7e-14 |
| max matched-eigenvalue deviation (max_dlambda) | 6.217248937900877e-15 |
| shift | 0.0 |

The matched eigenvalues agree to within ~6e-15 — a few units in the last place
of double precision. When identity exists, this pipeline does not merely
"tend to" see it; it certifies it at machine-noise level.

**PC2 — the graph against the file.** The stage-2 object of the bridge is the
identity function Z_id(t) = e^{iθ(t)}ζ(½+it), whose zero set encodes the zeta
zeros. PC2 feeds the graph, sampled at its K = 79 zeros, into the same
comparison machinery against the committed zero file:

| Quantity | PC2 value |
|---|---|
| r_H7 | 1.000000000000 |
| D_nn | 1.2e-10 |
| max matched-zero deviation (max_dgamma) | 4.98147301186691e-10 |
| K (levels compared) | 79 |

Again the correspondence is seen — this time at the 1e-10 level of D_nn,
limited by the numeric reconstruction of the graph rather than by the
statistics.

Together the controls calibrate the *detection floor* of the instrument:
D_nn ≈ 1e-10 (graph-level identity) and D_nn ≈ 1e-14 (operator-level
identity). Against the surrogate null the verdict is interpretable in one line: the
best any gate achieves is D_nn = 0.006937508455596089 — 0.88 of the GUE
surrogate level (0.0079 ± 0.0005), i.e. statistically indistinguishable from
random (v2.0.2 recompute; ratios to floors are category errors). The corrected
headline of the series (recorded in
`results/RESULTS.md` and the theory map) is anchored on the graph ↔ operator
comparison: the graph side reproduces the zeros at 1e-10, and no gate gets
below 0.0069 — the surrogate-null saturation level (≈2/n at n = 200).

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="120" alt="Agent Vera avatar"/></p>

*Agent Vera guarded the controls: PC1 and PC2 were registered before the gate
sweep was scored, and the negative verdict was allowed only because both
controls passed. An unfalsifiable NO was never on the table.*

---

## 6. Results

### 6.1 Headline table

| Quantity | Value | Status |
|---|---|---|
| Family | 52 unique configurations, master seed 96 | protocol C3 |
| Best r_H7 | 0.226 (p = 0.169, Bonferroni 0.80) | no identity |
| Decoys / GUE null | 0.026±0.140 / −0.014±0.127 | null zones |
| PC1 spinor64 twins | r = 1.000000000, D_nn = 2.7e-14 | method sees identity |
| PC2 graph ↔ file | r = 1.000000000000, D_nn = 1.2e-10 | method sees identity |
| Graph ↔ operator relation | none: D_nn at surrogate-null level | the series verdict |

### 6.2 The best gate

The strongest candidate of the family (from `verdict.best_gate` in
`data/results.json`) is a vortex-free Hofstadter reference, (Nv, q, W, α) =
(0, 0.0, 0.5, 0.5):

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

That the best of 52 gates is the *clean π-flux lattice* is itself
informative: adding vortices does not move the family toward the zeros. Note
also the internal disagreement of the statistics for this gate — it is the
best by r_H7, mid-pack by D_nn (p_D = 1.0 — the true zero window is not even
the best-matching window for this gate), and the *worst* by KS_sp
(p_KS = 1.0, i.e. its spacing distribution is farther from the zeros' than
every decoy's). A genuine identity would push all three statistics to their
extremes simultaneously; a fluctuation pushes one.

### 6.3 The null zones

The permutation machinery produced two null clouds for r_H7:

| Null ensemble | Composition | mean ± spread of r_H7 |
|---|---|---|
| Decoys (nullA) | 64 shifted zero lists (null_shifts = 64) | 0.026±0.140 |
| GUE null (nullB) | 40 GUE matrices (null_gue = 40) | −0.014±0.127 |

These are the "null zones" of the headline table: the range of r_H7 values
that pure chance produces when there is no identity. The best gate's 0.226
sits *inside* these zones — roughly 1.7 spread units above the decoy mean and
1.9 above the GUE mean (r_GUE_z = 1.8936817833815616) — comfortable, everyday
territory for a coincidence, and a different universe from the r = 1.000000000
that the controls register when identity is present.

### 6.4 Spread across the family

Across all 52 gates (from `data/gates_table.csv`, columns
`Nv,q,W,alpha,mean_spacing,r_H7,D_nn,shift,KS_sp,p_r,p_D,p_KS,r_GUE_z`):

| Statistic | min | max | notes |
|---|---|---|---|
| r_H7 | −0.168447299012455 | 0.22641576150208137 | 36 of 52 positive, 16 negative, 7 above +0.2 |
| D_nn | 0.006937508455596089 | 0.009221555365816578 | mean 0.0078 — at the surrogate-null level ≈ 2/n |
| mean_spacing | 0.011981804524559426 | 0.01272797005910956 | band density varies only mildly across gates |
| r_GUE_z | −1.2152397215832413 | 1.8936817833815616 | no gate is an outlier against the GUE null |

No gate in the family approaches identity by any statistic. The smallest raw
p-value anywhere in the table is p_D = 0.015384615384615385, attained by five
gates — (8, 1.0, 0.0, 0.5), (8, 0.5, 1.0, 0.4), (8, 1.0, 1.0, 0.4),
(16, 1.0, 1.0, 0.4) and (32, 1.0, 1.0, 0.4) — and even that minimum is consumed many times over by the
52-fold multiplicity correction (Section 7).

---

## 7. How to read the numbers

**p = 0.169 is an empirical permutation p-value.** The nullA decoy ensemble
has 64 members; with the add-one convention a p-value is
k/65 = k/(null_shifts + 1), where k counts the decoys at least as
identity-like as the gate plus one. The best gate's p_r = 0.16923076923076924
is exactly 11/65: ten of the 64 shuffled zero lists produced r_H7 ≥ 0.226,
and one more count is the gate itself. In plain words — if identity were
absent (as the null asserts), a value of r_H7 at least as large as the best
gate's would arise in roughly one sixth of honest draws. That is not evidence
of identity; it is the signature of an ordinary fluctuation.

**Bonferroni 0.80 is the multiplicity correction doing its job.** Fifty-two
gates were scored, and the smallest raw p-value anywhere in the family × all
three statistics is 1/65 = 0.015384615384615385. Multiplying by the 52 tests
gives the family-wise Bonferroni figure recorded in
`verdict.min_p_bonferroni`: **0.8**. Even the most extreme statistic of the
most extreme gate, after correcting for having looked 52 times, sits at 0.80 —
nowhere near any conventional significance threshold. The correction is what
makes the "no identity" conclusion immune to the look-elsewhere effect.

**r_GUE_z is a z-score, not a p-value.** For each gate, r_GUE_z measures how
many GUE-null standard deviations its r_H7 lies above the GUE mean. The best
gate's 1.8936817833815616 is unremarkable for a two-sided normal comparison,
and the family minimum is negative (−1.2152397215832413).

**D_nn saturates, and the gates sit exactly at the saturation level.**
Because the shift is optimised before D_nn is computed, a gate cannot plead a
global misalignment; and because PC1/PC2 certify floors of 1e-14 and 1e-10,
"we might just not be able to resolve identity" is off the table. The gates'
D_nn values (0.0069 to 0.0092) coincide with the surrogate nulls (nullA/nullB:
0.0070–0.0089): the metric separates *identity* from *everything else* in one
step and cannot grade distances among non-identical objects — the correction
of v2.0.1 that retired the "orders of magnitude" language.

**The null clouds are the fixed points of the reading.** Every interpretation
comes back to the same comparison: gates at D_nn ≈ 0.0078, surrogate nulls at
0.0079 ± 0.0005, controls at 1.2e-10 and 2.7e-14. p-values, z-scores and KS
statistics all tell the same story from different angles: the gates are
statistically indistinguishable from random — the binary content the old
"orders" phrasing obscured.

**The verdict is deliberately conservative in what it claims.** p_KS = 1.0 for
the best gate, ⟨r⟩ = 0.32 localization clustering on the clean lattice, and
the decoy/GUE null zones are all reported as measured. Nothing has been
rounded toward a more dramatic story in either direction.

---

## 8. Interpretation — H2 = NO at the surrogate-null level

**What was asked.** Question H2 of the Hilbert–Pólya tablet: is there a gate
whose spectrum *is* the zero spectrum, level by level?

**What was measured.** No. All 52 gates are statistically indistinguishable
from the permutation null model; the best candidate reaches
r_H7 = 0.22641576150208137 against a null zone of 0.026±0.140 (decoys) and
−0.014±0.127 (GUE), with family-wise Bonferroni 0.80. The conclusion recorded
in `data/results.json` translates as: *no gate is distinguishable from the
permutation null model — H2 remains closed, now with the method's power
measured*.

**What the verdict means operationally (corrected v2.0.1).** The instrument
has a demonstrated detection floor: D_nn = 2.7e-14 when handed two
isospectral operators (PC1) and 1.2e-10 when handed the graph against the
zero file (PC2). The gates sit at D_nn ≈ 7.8e-3 — *the same value as the
random surrogates* (nullA 0.0075 ± 0.0002, nullB 0.0079 ± 0.0005). The former reading —
"a factor of billions to trillions, the 9–10 order gap" — compared a
saturation level against a machine-precision floor and was a category error:
D_nn is bounded, no non-identical pair gets below ≈0.007 (≈2/n at n = 200), and a
random GUE matrix is "as far" from the zeros as any gate. The corrected statement: the
NO is *measured absence, not graded distance* — if a vortex gate in this
class were the Hilbert–Pólya operator, the pipeline would have returned
r ≈ 1 and D_nn ≤ 1e-10; instead every gate sits inside the random cloud.
The C4 cross-check (≈0.5 order by *relative residual* — a genuinely
unbounded metric) and C5's stability extension stand unchanged.

**Why the negative verdict is trustworthy.** Three independent guarantees: the
positive controls certify the detector (Section 5); the permutation nulls
certify the statistics (Section 7); and the protocol was frozen — 52 gates,
master seed 96, fixed windows — before scoring, so no gate was tuned after
seeing its p-value.

**What would falsify it.** The verdict is empirical and therefore falsifiable
in a precise way: any gate from this class that, run through the *same*
pipeline, yields r_H7 ≈ 1 with D_nn at or below the 1e-10 floor and a
permutation p-value that survives the 52-fold Bonferroni correction would
overturn H2 = NO. Registering the gate in advance and letting the controls
re-certify the pipeline would make such a claim unambiguous.

**What is *not* claimed.** The verdict applies to local lattice Hamiltonians
with vortex phases — the class defined in Section 3. It does not extend to
nonlocal constructions, which remain an open road-map item, and it is not a
statement about the Riemann Hypothesis itself. Nor does it contradict H3
(GUE statistics: YES): universality is exactly what erases arithmetic detail
from local spectra, and it is *why* the spectral-identity question is so hard
— every gate in the family looks generically GUE-like while carrying none of
the zeros' arithmetic.

---

## 9. Reproduction

The full verdict regenerates from a single deterministic command:

```bash
# tour of the verdict (~seconds, no zero file needed)
python3 campaigns/run_c3_gates.py
```

Notes on the protocol:

- The series seed is **96**; the RNG streams are fixed inside
  `engine/hamiltonian.py` — vortex coordinates, disorder realisations and any
  other stochastic input derive from those streams, never from ambient
  entropy.
- The vortex phases use **raw angle differences** (no wrapping shortcuts);
  this is part of the exact C3 protocol and is required for bit-level
  agreement.
- All dependencies are pinned in `requirements.txt`.
- The solver protocol is **bit-exact**: the equivalence control in the engine
  confirms that all 52 C3 gates reproduce the committed `mean_spacing` CSV
  column bit-for-bit — 52/52 gates at |Δ| < 1e-10, with the recorded maximum
  deviation |Δ| = 1.45e-16 (double-precision epsilon territory, verified in
  the protocol reproduction credited to C4 in `results/RESULTS.md`). Any
  reimplementation that misses this tolerance is not running the C3 protocol.
- The tour runs in seconds and does not require the zeta zero file on input;
  the zero window (γ₀ = 500.309084942, K = 200) is part of the committed
  protocol data.

---

## 10. Data and figures

### Figures

| File | Where |
|---|---|
| `fig05_gates.png` | 600 dpi — `figures_hires/ru/fig05_gates.png`; screen — `figures/ru/` |
| `fig05_gates_en.png` | 600 dpi — `figures_hires/en/fig05_gates_en.png`; screen — `figures/en/` |

### Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

The full monograph of this computation (statement, theorems, tables, figures,
honest limitations): 7–9 pages, the same content in both languages.

### Data

| File | Contents |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/gates_table.csv` | the 52-gate table (one row per gate; all statistics and p-values) |
| `data/` (npz/csv) | curves and tables |
| `../data/c3_*.json` | duplicate of the verdict in the shared registry |

Key fields of `data/results.json`: `meta` (L = 24, K = 200, poly_deg = 6,
zero_window_gamma0 = 500.309084942, null_shifts = 64, null_gue = 40,
date 2026-10-10), `family` (all 52 gates with every statistic), `nullA` /
`nullB` (the permutation clouds), `PC1_spinor_twins`, `PC2_graph`, and
`verdict` (n_gates = 52, best_gate, min_p_bonferroni = 0.8,
identity_found = false, pc1_r = 1.0, pc2_r = 1.0000000000000004).

Independent checks of this campaign live in `independent_verification/`
(the IVP protocol).

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

**Q1. Is a "gate" a physical shutter or device?**
No. The shutter picture is a metaphor for the mathematics: a gate is a
parametrised Hermitian Hamiltonian — a vortex-decorated Hofstadter lattice —
and "opening" it means diagonalising it. The source states this explicitly:
the term denotes a family of Hamiltonians, not a physical device.

**Q2. Does p = 0.169 mean the best gate is "close" to identity?**
No. It means the opposite: the best gate's r_H7 falls inside the measured
null zone (11/65 of permutation draws look at least as identity-like).
"Close" would be a p-value far *below* the corrected threshold together with
D_nn near the certified floors; the gates sit at the surrogate-null
saturation level (≈0.26) — as far from those floors as any random pair, and
not distinguishable from the null cloud (v2.0.1).

**Q3. Why rank correlation (r_H7) instead of comparing eigenvalues directly?**
Because identity is a statement about the level-n ↔ zero-n *correspondence*,
which is invariant to unfolding choices and is destroyed by nothing except a
wrong ordering. Rank statistics with ramps removed respond precisely to the
correspondence and are robust to monotone distortions; direct raw-level
comparisons would be dominated by arbitrary scale conventions.

**Q4. Why trust a negative result at all?**
Because the instrument is certified in both directions. PC1 (isospectral
twins, r = 1.000000000, D_nn = 2.7e-14) and PC2 (graph vs file,
r = 1.000000000000, D_nn = 1.2e-10) prove the pipeline detects identity at
machine precision when it exists; the permutation nulls prove the statistics
know what chance looks like. The NO is a measurement, with a floor, not an
absence of evidence.

**Q5. Does this disprove the Hilbert–Pólya programme or the Riemann
Hypothesis?**
Neither. The verdict is scoped to the local vortex-lattice class defined by
(Nv, q, W, α). Nonlocal constructions are explicitly left open in the
roadmap, and nothing here bears on the truth of RH. The programme's own
theory map records H2 = NO for this class alongside H3 = YES (GUE
statistics), H4 = YES (Dirac dynamics) — a resonator that is real, universal
and wave-like, whose zeros are encoded rather than generated.

**Q6. Why exactly 200 levels, 344 levels, degree 6?**
These are the frozen protocol constants of C3: the central 0.6 band of the
576 = 24² eigenvalues (344 levels), a degree-6 polynomial unfolding, and a
200-level window (K = 200) matched to 200 zeros from γ₀ = 500.309084942.
They were fixed before scoring; changing them post hoc would invalidate the
permutation nulls, which are built under the same protocol.

**Q7. What does the label H7 refer to?**
The protocol tag of this gate family; the rank statistic r_H7 is named after
it. The question the campaign tests is H2 of the series' tablet — spectral
identity — which is a different numbering and should not be confused with the
family tag.

**Q8. Why two null clouds instead of one formula?**
Because they answer different objections. The decoy cloud (shifted zero
lists) models "same zeros, broken correspondence" — exactly the alternative
that matters for identity. The GUE cloud models "generic universal spectrum".
A gate must escape both to claim anything; escaping neither, as all 52 do,
closes the question cleanly.

**Q9. The best gate is the vortex-free lattice. Does that mean vortices were
a dead end?**
Within this class and this protocol, yes as measured: the undecorated π-flux
reference (Nv, q, W, α) = (0, 0.0, 0.5, 0.5) tops the table at
r_H7 = 0.22641576150208137, and decoration never beats it. The campaign's
claim is about this family; C5 explores whether more handles change the
picture (they do not change the verdict).

**Q10. How does the null-level verdict here relate to C4's ≈0.5 order figure?**
Two metrics, one question. C3 measures the gap in the rank metric D_nn
(gates ≈ 0.26 against control floors of 1e-10 and 1e-14); C4 measures it in a
thermal (heat-kernel) metric, where the separation is ≈0.5 order. The theory
map records both projections, and their agreement in sign — both NO — is the
methodological point.

**Q11. Can I test my own configuration with this pipeline?**
Yes, under the same discipline: build the Hamiltonian with the documented
handles in `engine/hamiltonian.py`, keep the windows and unfolding frozen
(band 0.6 → 344 levels, degree-6 polynomial, K = 200 window), regenerate both
null clouds, run PC1/PC2 first, and apply the 52-fold multiplicity
correction appropriate to the number of candidates you score. A result
without the controls is not a C3-style result.

**Q12. Where is the line between what is measured and what is conjectured?**
Measured: the spectra, the statistics, the null clouds, the control floors,
the verdict for this class. Conjectural: identifying the α = 1/2 dynamics
line with the critical line Re(s) = 1/2 — the package keeps that bridge
explicit and separates it from everything measured here.

---

## 14. See also

- [C5 · Gates extended](../C5_gates_extended/README.md) — the extended handle
  set (twists, anisotropy, δα, mass, vortex profile, charge signs) and the
  stability of the H2 = NO verdict across it.
- [C4 · Trace formula](../C4_trace_formula/README.md) — the thermal projection
  of the same question: Tr e^{−xH} against the explicit formula, and the
  protocol-reproduction check |Δ| = 1.45e-16.
- [engine/README.md](../../engine/README.md) — the Hamiltonian and solver
  modules, the C3 raw-angle protocol, and the 52/52 bit-exact equivalence
  control.
- [docs/theory.md](../../docs/theory.md) — the five-station map of the bridge,
  the tablet of questions H1–H5, and what the package does and does not claim.

---

*Hilbert Polya Bridge v2.0.0 · C3 · The H7 gate family*

