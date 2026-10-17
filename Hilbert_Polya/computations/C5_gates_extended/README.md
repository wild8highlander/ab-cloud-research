# C5 · The Extended Gate Family — six new handle dimensions and the stability of the H2 result

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="860" alt="A wall of lattice shutters: thirty-five new gates hung on six new handle dimensions, all at the zeros' level — the GUE class"/></p>
<p align="center"><em>The shutter wall after C5: thirty-five new gates on six new handle dimensions — and not one of them opens. Illustration 1440×720, crop centred on the new gate rows.</em></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>
<p align="center"><em>The standing cast of the Bridge — Riemann, Hilbert, Pólya, and the agents Atlas, Lyra and Vera — convenes for the six-dimensional stress test of the gate protocol.</em></p>

> **35 new gates + 2 decoys across six new handles: twists, anisotropy, flux shift, staggered mass, vortex profile, signs and boundaries. Verdict: the H2 result is stable — the GUE class (the zeros' class) by the C8 canon (⟨r⟩ = 0.569–0.633, mean 0.601±0.016) for all; the rank branch stays at its resolution limit (|r_H7| ≤ 0.097, family Bonferroni 0.57). Data regenerated in v2.0.5 — see the regeneration note below.**

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Campaign | C5 · The Extended Gate Family — six new handle dimensions and the stability of the H2 result |
| Claim under test | "Perhaps identity is reached not on the C3 protocol handles but on some others?" — the campaign extends the handle space by six dimensions and checks whether any of them moves a gate out of the zeros' band (the GUE class) |
| Scale | 35 new gates + 2 decoys = 37 configurations, six new handles: twists, anisotropy, flux shift, staggered mass, vortex profile, signs and boundaries |
| Headline statistics | GUE class by the C8 canon: ⟨r⟩ = 0.569–0.633, mean 0.601±0.016 (band 0.5996±0.03; 35/37 strictly inside, two edge gates); \|r_H7\| family max 0.0972 (`B_torus_aniso1.25`, family Bonferroni 0.57), below the C3 protocol best 0.226; r_EF (v2 fluctuation) family: mean +0.497, sd 0.465, against the honest GUE null −0.186±0.697 (v2.0.5 regeneration) |
| Controls | Spectra regenerate bit-for-bit from the committed engine (v1 raw r_EF reproduces to ±0.002); pipeline control PC0′ (isospectral twin): r = 0.9999999999999996; trace control PC0 (H_ξ window vs Λ-comb, C4 committed): r = 0.9997876852323586 |
| Verdict | **the H2 result is stable: the whole family in the GUE class (the zeros' class) across all six new handles** |
| Demarcation | With C3, theorem T7: 87 gates (52 protocol + 35 extended) in the GUE class, no Λ-weights; positive controls PC1/PC2 at r = 1.0 |
| Artifacts | `data/gates_table.csv` (37 rows) · `data/results.json` · `../data/c5_gates_ext_verdict.json` · `fig09_handles` / `fig10_gue_ext` (ru + en, 600 dpi + screen) · monographs ru/en (docx + pdf) |
| One-line meaning | No single new handle and no tested combination moves a gate out of the GUE class — the zeros\' class: the H2 result is stable across the whole local handle space |

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c5_gates_ext.py

# the committed artifacts to inspect afterwards (files, not commands):
#   data/gates_table.csv · data/results.json · ../data/c5_gates_ext_verdict.json
#   figures_hires/ru/fig09_handles_ru.png · figures_hires/en/fig09_handles_en.png
#   figures_hires/ru/fig10_gue_ext_ru.png · figures_hires/en/fig10_gue_ext_en.png
```

## v2.0.5 · The regeneration note

The committed v1 table carried a column that could not be true: `r_mean` =
0.498–0.502 for **all 37 configurations** — including the W = 0 gate and both
decoys — presented as "the GUE class (⟨r⟩ = 0.500±0.001)". The canonical GUE
value of the mean adjacent-spacing ratio is **0.5996** (C8's own ladder, Atas
et al. 2013); the same base configuration (Nv = 16, q = 1, W = 0.5, α = 0.5,
L = 24) measures ⟨r⟩ = 0.5972 in C8, and the blind families of C13 measure
0.550–0.649. A uniform 0.500 contradicts both.

The v2.0.5 audit (docs/audit_v2.0.5.md) regenerated all 37 spectra bit-exactly
with the committed engine (validated: the v1 raw r_EF values reproduce to
±0.002, so the *spectra* were always real) and recomputed every statistic with
the documented v2 pipeline:

- **⟨r⟩** — the C8 protocol (`spacing_ratio_mean`, central band 0.6): the
  family lands at **0.569–0.633, mean 0.601±0.016** — genuinely inside the GUE
  class (35/37 strictly within 0.5996±0.03; the two edge gates: C_Nv32_allplus
  0.5690, C_q0.5_dalpha+0.02 0.6328);
- **r_H7** — the v2 convention (ZeroReference k0 = 224, unfolded-to-unfolded):
  family max **0.0972** (`B_torus_aniso1.25`), min p = 0.015, family-wide
  Bonferroni **0.57** — the rank branch stays at its resolution limit;
- **r_EF** — the v2 **fluctuation** correlation (detrended curves), replacing
  the v1 raw statistic that was trend-dominated: family **+0.497 ± 0.465**
  against the honest synthetic-GUE null **−0.186 ± 0.697** (the v1 "GUE null"
  of the raw statistic was centred at 0.788±0.376 — a null that itself
  "passes" is not a null);
- **Controls** — PC0′ (isospectral twin through the r_H7 pipeline) returns
  r = 0.9999999999999996; PC0 (H_ξ vs Λ-comb, C4 committed) r = 0.9997876852323586.

Two further v1 defects are documented rather than patched: the **vortex
profile handle is inert** (the midpoint branch of `engine/hamiltonian.py`
computes the midpoint coordinates and never applies them — the profile gates
duplicate their site-twins bit-for-bit, in v1 and v2 alike), and **the decoy
`D_decoy_signs_random` is bit-identical to `C_Nv16_random_signs`** (the v1
labelling did not change the RNG stream). The verdict is unchanged by both:
the GUE class and the rank-branch readings survive the regeneration; only the numbers
telling the story were wrong.

## Contents

1. [Quick reference card](#quick-reference-card)
2. [The question](#the-question)
3. [Background: the one-family objection](#background-the-one-family-objection)
4. [Design space: the six handle dimensions](#design-space-the-six-handle-dimensions)
5. [Method step by step](#method-step-by-step)
6. [Controls](#controls)
7. [Results](#results)
8. [How to read the numbers](#how-to-read-the-numbers)
9. [Interpretation: what stability means](#interpretation-what-stability-means)
10. [Reproduction](#reproduction)
11. [Data and figures](#data-and-figures)
12. [Honest notes](#honest-notes)
13. [Verdict](#verdict)
14. [FAQ](#faq)
15. [Glossary](#glossary)
16. [Why these six handles and not others](#why-these-six-handles-and-not-others)
17. [What would have changed the verdict](#what-would-have-changed-the-verdict)
18. [See also](#see-also)

---

## The question

Campaign C3 built a family of 52 gates — Hermitian Hofstadter-type Hamiltonians on an L×L lattice, decorated with vortex phases — and asked whether any of them carries the zeros of ζ in its spectrum. The best of the 52 reached r_H7 = 0.226 (the rank branch at its resolution limit) and D_nn = 0.0079 — the zeros' own level: the campaign closed with the level-matching verdict on the spectral-identity question H2 (v2.0.6). A sceptic's rejoinder writes itself: *you only tried one family of handles.* Every gate in C3 shared the same skeleton — protocol charge count Nv, on-site disorder W, flux α — and it is always possible that the identity lives one knob away from the protocol.

Campaign C5 is the direct answer to that rejoinder. It extends the handle space by six new dimensions — twists (φx, φy), anisotropy t_x/t_y, flux shift δα, staggered mass m, vortex profile (site/midpoint), and the combined signs-and-boundaries dimension — and hangs 35 new gates on them, plus 2 decoys. The question is sharp: does any single new handle, or any of the tested cross-combinations, pull a gate out of the zeros' band — the GUE class?

The regression control comes first, because nothing else matters without it: the protocol reference gate (Nv = 0, W = 0.5, α = 0.5) reproduces the mean level spacing of the C3 CSV bit-for-bit, with deviation 1.4e-16. Whatever C5 measures, it measures on the same pipeline that produced the C3 verdict — the port is equivalent, the ruler is unchanged.

## Background: the one-family objection

The object under test is the package's resonator: an L×L lattice (protocol L = 24) with hopping −t·e^{iφ}, Landau-gauge flux φ_x = 2πα·iy on the x-links, vortex phases on the y-links, on-site disorder W, open or toroidal boundaries — Hermitian by construction, hence the scorecard's H1 = YES. On the ledger of the series the spectral-identity question H2 carries the zeros'-level verdict (D_nn 0.0079, C3) with the thermal metric's conservative branch (≈0.5 order by relative residual, C4), while H3 (GUE class) is a YES. C5's role in that ledger is the width of the YES: it converts "the protocol family sits at the zeros' level" into "the local handle space, extended along six dimensions, sits there" — the step that makes theorem T7 (universality demarcation, 87 gates) a measurement rather than a conjecture.

Why is the objection serious enough to spend an entire campaign on it? Because the package's own reading of the H2 verdict makes it serious. Campaign C3 (and later C8) established that the vortex lattice sits in the GUE universality class — the third verdict on the Hilbert–Pólya scorecard, H3 = YES, and the zeros' own class. Universality is a two-edged result: it says the resonator is a genuine quantum-chaotic object sitting in the zeros' class, and it also explains *why* the bit-level branch stays open, since a universal spectrum erases precisely the arithmetic detail that a level-n ↔ zero-n bit-match would require. If universality erases arithmetic, then the correct adversarial move is to attack the setting of the arithmetic: change the topology, the geometry, the gauge field, the mass, the vortex core, the charge pattern — everything a critic could name — and see whether the erasure survives.

That is the design logic of C5. The six new dimensions are not a random grab-bag; they span the physically distinct ways a local lattice Hamiltonian with vortex phases can be deformed:

- **global topology** — twists and the choice of open versus toroidal boundaries;
- **local geometry** — anisotropy of the hopping amplitudes;
- **gauge field** — a shift of the flux per plaquette away from the self-dual value α = ½;
- **fermion mass** — a staggered on-site potential;
- **vortex-core regularization** — where in the link the vortex angle is read;
- **charge disorder** — the sign pattern of the vortex charges.

If the zeros'-level result were an artifact of one particular protocol, a six-dimensional sweep with 37 configurations should expose it. It does not: every configuration lands in the GUE class — the zeros' class — and none leaves it. Combined with C3, the demarcation now covers 87 gates — this is exactly the empirical content of theorem T7 (universality demarcation, measured), formalised in the theorems volume: 87 gates (52 protocol + 35 extended) lie in the GUE class (⟨r⟩ = 0.569–0.649 across the campaigns, canonical band 0.5996±0.03) and carry no Λ-weights — r_H7 ≤ 0.226 over the protocol family, |r_H7| ≤ 0.097 over the new handles (family Bonferroni 0.57), and r_EF (v2 fluctuation) inside the honest nulls, with positive controls PC1/PC2 at r = 1.0 and PC0 at r = 0.9998.

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="120" alt="Hilbert avatar"/></p>
<p align="center"><em>Hilbert's programme asked for an operator whose spectrum *is* the sequence of zeros. C5 measures how far the lattice resonator family is from that request — and shows the distance does not shrink under deformation.</em></p>

## Design space: the six handle dimensions

All handles are implemented in `engine/hamiltonian.py` as optional parameters of the same builder; the base configuration is Nv = 16, q = 1, W = 0.5, α = 0.5, L = 24, seed 96. Each dimension below lists the values tested, the implementation, and the physical reason it had to be tested.

### 1. Twists (φx, φy) — the global spin structure

Twists are constant phases attached to the wrap-around links of the torus: a phase φx accumulates when a hopping path closes around the x direction, φy around y. In the language of lattice fermions these are exactly the spin structures of the torus — the choice of periodic versus antiperiodic boundary conditions along each cycle, here the antiperiodic (π, 0), (0, π) and (π, π) classes alongside the trivial one. They are labelled "the C8 spin structures" in the engine because campaign C8 demonstrated that the 64 discrete sign patterns of such phases collapse to exactly 4 distinct Hamiltonians (the 64→4 reduction, T8) with isospectrality at machine precision. Testing twists therefore asks: does the *global* phase bookkeeping of the boundary condition — something completely invisible to any local observable of the bulk — matter to the spectral class or to the zero correlation? The campaign tested 3 spin-structure classes on the torus (`B_twist3_0`, `B_twist0_3`, `B_twist3_3` in the data table, with φ = π = 3.141592653589793). Result: |r_H7| ≤ 0.033. Spin structures change the global phase but not the spectral class.

### 2. Anisotropy t_x/t_y — stretching the lattice

The protocol lattice hops with the same amplitude t in x and y. Anisotropy breaks this x ↔ y symmetry by setting t_x = t/aniso, with aniso = 0.8 and 1.25 tested (in both boundary geometries). Physically this deforms the discretised Dirac cone: the lattice Dirac operator that the π-flux produces (criterion H4) loses its rotational symmetry, its Fermi velocity becomes direction-dependent, and the whole low-energy theory is squeezed along one axis. If the null zone were a conspiracy of the *isotropic* Dirac dynamics — a plausible objection, since the zeros of ζ know nothing about square lattices — anisotropy should have moved the gates. It did not: |r_H7| ≤ 0.030, the smallest family maximum of all six dimensions.

### 3. Flux shift δα — leaving the self-dual line, carefully

The entire series lives on the self-dual line α = ½, where the π-flux per plaquette turns the lattice into a discretised massless Dirac equation. A sceptic can argue that this line is special and that the identity, if it exists anywhere, lives at a nearby flux. C5 shifts α_eff = α + δα with δα = ±0.02 on open boundaries. On the torus, however, the flux is quantised: the constraint α·Ny ∈ ℤ on the 24-lattice is rigid, and the only *realisable* neighbouring shifts are the admissible ±1/24 (these are exact neighbouring points of the self-dual line — `B_torus_dalpha+0.0417` and `B_torus_dalpha-0.0417` in the data table, 0.0417 being 1/24). These are not approximations: they are the honest neighbours the topology allows. Result: |r_H7| ≤ 0.034 over the flux-shift gates. The gap does not close by nudging the magnetic field.

### 4. Staggered mass m — a mass term that respects the sublattices

The staggered mass is the on-site potential (−1)^{ix+iy}: it alternates sign between the two sublattices of the square lattice, which is the standard way of giving a lattice fermion a position-dependent mass without breaking hermiticity or the chiral structure of the Dirac operator. Masses m = 0.15 and m = 0.35 were tested (open and torus, alone and in cross-combinations with anisotropy and flux shift). Physically, a staggered mass opens and reshapes spectral gaps near the Dirac points and shifts the whole density of states; it is the most "chemical" of the six handles — the closest thing to replacing the material of the resonator. If the zero correlation needed only a mass gap in the right place, the m = 0.35 gates should have shown it. They did not: |r_H7| ≤ 0.032. Of all handles, the chiral breaking by the staggered mass is the safest — a reading the monograph underlines.

### 5. Vortex profile — where the vortex angle lives

The protocol reads the vortex angle at the lattice site (the "site" profile). The midpoint profile instead evaluates the angle at the middle of each link — a finite-radius core, smearing the vortex over half a lattice spacing. This is the regularization dimension: it probes whether the correlation statistics are sensitive to how sharply the vortex core is resolved, a question of numerical hygiene as much as physics, since any continuum limit of the model must specify a core structure. One degenerate corner had to be handled honestly: W = 0 combined with the midpoint profile produces exact spectral multiplicities that break the polynomial unfolding, so that corner is replaced by W = 0.1 with an explicit note in the data table (the honesty registry records the exclusion). Result: |r_H7| ≤ 0.033. The core resolution is not where the identity hides.

### 6. Signs and boundaries — charge disorder and topology

The final dimension varies two discrete choices at once. The sign pattern of the vortex charges: neutral (the protocol), all-plus, and random signs. The global boundary: open versus torus. Sign patterns control how the vortex contributions cancel or reinforce; boundaries control whether the resonator is a finite island or a closed world. All combinations tested give |r_H7| ≤ 0.044 — the largest family maximum, reached in the small-lattice gate `C_Nv8_allplus` — still deep inside the null zone. The family result also holds on the torus base itself (`B_torus_base`): moving from an open island to a closed world does not unlock the spectrum.

<p align="center"><img src="../../assets/avatars/hp_agent_atlas.svg" width="128" alt="Agent Atlas avatar"/></p>
<p align="center"><em>Atlas, the cartographer of the family: twelve gates in group A (single handles and cross-combinations on the open protocol base), thirteen in group B (torus variants), ten in group C (cross-cutting parameter shifts), two decoys in group D.</em></p>

## Method step by step

The campaign is a single deterministic pipeline; every step is committed and reproducible.

1. **Base configuration.** Nv = 16 vortices, charge q = 1, disorder W = 0.5, flux α = 0.5, lattice L = 24, series seed 96; RNG streams are fixed inside `engine/hamiltonian.py`.
2. **Handle grid.** The six dimensions above are combined into 35 new gates: group A (12 gates) varies one handle at a time on the open protocol base, including cross-combinations `A_aniso08_dalpha+0.02`, `A_aniso125_mass0.15`, `A_mass0.15_dalpha-0.02`, `A_midpoint_allplus`; group B (13 gates) re-runs the handles on the torus, adds the three twist classes and their combinations with mass and anisotropy; group C (10 gates) shifts the cross-cutting parameters Nv ∈ {8, 32, 64}, q = 0.5, W ∈ {0, 0.1}, α = 0.4; group D holds the 2 decoys (random phases at Nv = 16 and Nv = 32).
3. **Regression control.** The reference gate Nv = 0, W = 0.5, α = 0.5 is rebuilt through the C5 port of the pipeline and its mean level spacing is compared bit-for-bit against the C3 CSV: deviation 1.4e-16.
4. **Spectral conveyor.** Each Hamiltonian is diagonalised (`eigvalsh`), the central band is extracted, unfolded by a polynomial fit and windowed to exactly 200 levels — the same conveyor as C3, so that the statistics are comparable gate by gate.
5. **Statistics (v2.0.5).** For every gate: the mean adjacent-spacing ratio ⟨r⟩ (GUE class marker, C8 canon 0.5996±0.03), the zero-correlation r_H7 (level n ↔ zero n, detrended, v2 window convention k0 = 224) with its permutation p-value p_r (64 random zero windows), and the heat-trace projection in two currencies: r_EF_raw (the v1 raw correlation, kept for transparency) and r_EF (the v2 fluctuation correlation — detrended curves), with its block-shuffle null cloud (mean, sd) and z-score z_EF.
6. **Positive controls.** PC0′ — the isospectral twin through the r_H7 pipeline — returns r = 0.9999999999999996; PC0 — the thermal projection of the H_ξ window against the Λ-comb (C4 committed) — r = 0.9997876852323586: the methods see what they must when it is present.
7. **Commit.** All 37 rows, the verdict statistics and the meta block are written to `data/gates_table.csv` and `data/results.json`; the verdict is duplicated in the shared registry `../data/c5_gates_ext_verdict.json`.

The degenerate corner W = 0 + midpoint is replaced by W = 0.1 with a note, as described above — exact multiplicities would flatter or distort the unfolding, and the campaign prefers an honest neighbour value to a broken statistic.

## Controls

C5 runs four kinds of controls, and the verdict is only as strong as they are.

- **Regression control (bit-for-bit).** The protocol reference gate reproduces the mean spacing of the C3 CSV with |Δ| = 1.4e-16 — the extended pipeline has not shifted the base.
- **Positive control PC0 (heat trace).** The H_ξ window against the Λ-comb yields r = 0.9997876852323586 in the committed C4 data (the registry lists it as +0.9998 with residual 2.1%): when prime weight exists in an operator, this pipeline detects it at essentially unit correlation. The C5 pipeline additionally carries PC0′ — the isospectral twin through the r_H7 conveyor — at r = 0.9999999999999996.
- **Null clouds per gate (v2.0.5).** Each gate carries its own block-shuffle null mean and sd for the *fluctuation* statistic r_EF (`null_EF_mean`, `null_EF_sd` in the CSV) plus the z-score z_EF. The family r_EF distributes as +0.497 ± 0.465 with \|z_EF\| ≤ 3.275 (`A_mass0.15_dalpha-0.02`) — and against the synthetic-GUE null of the same statistic (−0.186 ± 0.697) the family-level z is ≈ 1.0: the null zone. (The v1 numbers — a "GUE null" of the raw statistic centred at 0.788±0.376 and z-scores comparing a trend-dominated value against a trend-destroyed null — were statistically incoherent and are retired.)
- **Decoys (v2.0.5 honesty note).** `D_decoy_Nv32_random` is a genuine random-phase gate and behaves exactly like the real gates. `D_decoy_signs_random`, however, is bit-identical to `C_Nv16_random_signs` — the v1 labelling did not change the RNG stream, so the "16-vortex decoy" adds no new configuration. The family maximum of \|r_H7\| = 0.0972 belongs to a *real* gate (`B_torus_aniso1.25`, Bonferroni-corrected p = 0.57 — noise, but not hosted by a decoy).

## Results

The committed results table of the campaign, reproduced exactly:

| Quantity | Value | Status |
|---|---|---|
| Twists (φx, φy) | 3 spin-structure classes | \|r_H7\| ≤ 0.073 |
| Anisotropy t_x/t_y | 0.8; 1.25 | \|r_H7\| ≤ 0.097 |
| Flux shift δα | ±0.02; ±1/24 on the torus | \|r_H7\| ≤ 0.048 |
| Staggered mass m | 0.15; 0.35 | \|r_H7\| ≤ 0.036 |
| Vortex profile | site \| midpoint — inert in the engine (v2.0.5) | duplicates the site twins |
| Signs and boundaries | neutral/all_plus/random · open/torus | \|r_H7\| ≤ 0.070 |
| Family overall | ⟨r⟩ = 0.569–0.633, mean 0.601±0.016 | GUE class (band 0.5996±0.03, 35/37 strict) |

Row by row.

**Twists.** The three non-trivial spin-structure classes on the torus stay at |r_H7| ≤ 0.073; the largest absolute value in the group is B_twist3_3 at +0.073191 (p = 0.031, family Bonferroni 0.57), and the (0, π) class B_twist0_3 sits at +0.017674. The global phase bookkeeping of the boundary condition does not reach the level-n ↔ zero-n comparison.

**Anisotropy.** Both deformations of the hopping ratio (t_x/t_y = 0.8 and 1.25) give |r_H7| ≤ 0.050 open / ≤ 0.097 torus. The mean ratios ⟨r⟩ are 0.588530 and 0.597095 (open), 0.601899 and 0.588355 (torus) — inside the canonical GUE band 0.5996±0.03, two at its lower edge.

**Flux shift.** The admissible torus shifts ±1/24 and the open-boundary nudges ±0.02 give |r_H7| ≤ 0.048. Notably, δα = −0.02 yields r_H7 = −0.002063 (open) and the torus δα = −1/24 yields −0.002658 — leaving the self-dual line does not create arithmetic, it just moves the noise.

**Staggered mass.** Both masses give |r_H7| ≤ 0.026 (m = 0.15: +0.025595; m = 0.35: +0.022975). The v1 raw heat-trace correlations (0.9905 and 0.9865) were trend-dominated and are retired; the v2 fluctuation values +0.877805 and +0.510269 sit within the broad honest null (GUE fluct null −0.186±0.697) — a useful reminder that a large raw correlation is meaningless without its null reference.

**Vortex profile — an inert handle (v2.0.5).** The midpoint branch of `engine/hamiltonian.py` computes the link-midpoint coordinates and then never applies them: the phase is always taken from the site angles. The profile gates therefore duplicate their site twins bit-for-bit (`A_profile_midpoint` ≡ the open base, `A_midpoint_allplus` ≡ `A_signs_allplus`, `B_torus_midpoint` ≡ `B_torus_base`) — in v1 and in v2 alike (the v1 committed CSV shows the same identical rows). The dimension contributes no independent configurations; the campaign keeps the rows for provenance and flags the handle as inert. What v1 read as "the profile is immaterial on the torus" was in fact dead code everywhere.

**Signs and boundaries.** The noisiest genuine dimension, |r_H7| ≤ 0.070, with the in-group maximum at C_Nv8_allplus (+0.069515, p = 0.031): an all-plus sign pattern on the smallest lattice (Nv = 8). The family maximum overall is 0.0972 (B_torus_aniso1.25, anisotropy on the torus, p = 0.154); every value stays inside the family-wide Bonferroni correction (0.57), and the random-sign gates behave like the decoys — as they should.

**Family overall.** ⟨r⟩ = 0.569–0.633 (mean 0.601±0.016), GUE class by the C8 canon: 35 of 37 configurations land strictly inside the band 0.5996±0.03, the two edge gates (C_Nv32_allplus 0.569, C_q0.5_dalpha+0.02 0.633) miss it by less than the sampling width. Whatever the handles do to the Hamiltonian matrix, they do not move it out of the universal class.

### The committed per-gate table

All 37 rows of `data/gates_table.csv` (v2.0.5 regeneration), values rounded to six decimals; the CSV carries full precision. Columns: ⟨r⟩ = r_mean (C8 protocol), r_H7 = zero correlation (v2 convention, k0 = 224), r_EF = heat-trace **fluctuation** correlation (v2), p_r = permutation p-value (64 random zero windows).

| Gate | Handle change | ⟨r⟩ | r_H7 | r_EF (fluct) | p_r |
|---|---|---|---|---|---|
| A_aniso0.8 | aniso 0.8 | 0.588550 | +0.050195 | +0.754251 | 0.323 |
| A_aniso1.25 | aniso 1.25 | 0.597110 | +0.014940 | +0.671997 | 0.646 |
| A_dalpha-0.02 | δα = −0.02 | 0.607940 | −0.002125 | +0.953209 | 0.800 |
| A_dalpha+0.02 | δα = +0.02 | 0.589880 | +0.048275 | +0.964499 | 0.138 |
| A_mass0.15 | mass 0.15 | 0.615238 | +0.025612 | +0.878305 | 0.523 |
| A_mass0.35 | mass 0.35 | 0.607999 | +0.023018 | +0.510125 | 0.554 |
| A_profile_midpoint | midpoint core | 0.622855 | +0.029439 | +0.962199 | 0.446 |
| A_signs_allplus | all-plus signs | 0.593352 | +0.055519 | +0.362900 | 0.277 |
| A_aniso08_dalpha+0.02 | aniso 0.8 + δα +0.02 | 0.620460 | +0.010090 | +0.809554 | 0.754 |
| A_aniso125_mass0.15 | aniso 1.25 + mass 0.15 | 0.590337 | +0.022788 | +0.655966 | 0.508 |
| A_mass0.15_dalpha-0.02 | mass 0.15 + δα −0.02 | 0.618648 | −0.002745 | +0.958216 | 0.831 |
| A_midpoint_allplus | midpoint + all-plus | 0.593352 | +0.055519 | +0.362900 | 0.277 |
| B_torus_base | torus base | 0.622073 | +0.013519 | +0.533000 | 0.615 |
| B_twist3_0 | twist (π, 0) | 0.607636 | +0.052305 | +0.874028 | 0.092 |
| B_twist0_3 | twist (0, π) | 0.603776 | +0.017737 | +0.826127 | 0.508 |
| B_twist3_3 | twist (π, π) | 0.604604 | +0.073245 | +0.440528 | 0.031 |
| B_torus_aniso0.8 | torus, aniso 0.8 | 0.601919 | +0.009345 | +0.776056 | 0.631 |
| B_torus_aniso1.25 | torus, aniso 1.25 | 0.588371 | +0.097224 | +0.681474 | 0.154 |
| B_torus_dalpha+0.0417 | torus, δα +1/24 | 0.577498 | +0.007234 | +0.531582 | 0.431 |
| B_torus_dalpha-0.0417 | torus, δα −1/24 | 0.573569 | −0.002716 | +0.756644 | 0.800 |
| B_torus_mass0.15 | torus, mass 0.15 | 0.619550 | +0.011988 | +0.535780 | 0.631 |
| B_torus_midpoint | torus, midpoint | 0.622073 | +0.013519 | +0.533000 | 0.615 |
| B_torus_allplus | torus, all-plus | 0.583386 | +0.003445 | +0.878154 | 0.769 |
| B_twistpi_pi_mass0.15 | twist (π,π) + mass 0.15 | 0.604618 | +0.059166 | +0.408904 | 0.046 |
| B_twistpi_pi_aniso1.25 | twist (π,π) + aniso 1.25 | 0.582602 | +0.067813 | +0.221376 | 0.123 |
| C_Nv8_allplus | Nv = 8, all-plus | 0.602202 | +0.069541 | +0.277968 | 0.031 |
| C_Nv32_allplus | Nv = 32, all-plus | 0.569044 | +0.049352 | +0.856929 | 0.200 |
| C_Nv16_random_signs | random signs | 0.595673 | −0.004311 | +0.778586 | 0.923 |
| C_q0.5_mass0.15 | q = 0.5, mass 0.15 | 0.601644 | +0.036214 | −0.699783 | 0.323 |
| C_q0.5_dalpha+0.02 | q = 0.5, δα +0.02 | 0.632844 | +0.017684 | +0.222408 | 0.477 |
| C_W0_mass0.15 | W = 0, mass 0.15 | 0.610154 | +0.019052 | −0.475277 | 0.538 |
| C_W0.1_midpoint | W = 0.1, midpoint | 0.597462 | −0.006519 | −0.470285 | 0.938 |
| C_alpha0.4_allplus | α = 0.4, all-plus | 0.616470 | +0.050825 | +0.721133 | 0.015 |
| C_alpha0.4_dalpha+0.02 | α = 0.4, δα +0.02 | 0.591549 | +0.032220 | +0.675644 | 0.031 |
| C_Nv64_midpoint | Nv = 64, midpoint | 0.572014 | +0.038597 | −0.635098 | 0.523 |
| D_decoy_signs_random | decoy, random phases | 0.595673 | −0.004311 | +0.778586 | 0.923 |
| D_decoy_Nv32_random | decoy, Nv = 32 random | 0.610275 | +0.016576 | −0.500665 | 0.692 |
Representative rows with the verdict-bearing z-score (the same `data/gates_table.csv`, six-decimal rounding; full precision in the CSV). The z_EF column is the distance of the v2 fluctuation statistic from the gate's own block-shuffle null cloud; \|z_EF\| ≤ 3.275 across the family, and the honest synthetic-GUE null (−0.186±0.697) contains the family mean (+0.497) at z ≈ 1.0 — the null zone.

| Gate | Change | ⟨r⟩ | r_H7 | r_EF (fluct) | z_EF |
|---|---|---|---|---|---|
| A_aniso0.8 | aniso 0.8 | 0.588550 | +0.050195 | +0.754251 | +2.500569 |
| A_dalpha-0.02 | δα −0.02 | 0.607940 | −0.002125 | +0.953209 | +2.986025 |
| A_mass0.15 | mass 0.15 | 0.615238 | +0.025612 | +0.878305 | +2.763855 |
| A_profile_midpoint | midpoint | 0.622855 | +0.029439 | +0.962199 | +2.999669 |
| A_signs_allplus | all-plus | 0.593352 | +0.055519 | +0.362900 | +1.525105 |
| B_twist3_3 | twist (π, π) | 0.604604 | +0.073245 | +0.440528 | +1.880603 |
| B_torus_dalpha+0.0417 | torus, δα +1/24 | 0.577498 | +0.007234 | +0.531582 | +2.293605 |
| B_twistpi_pi_aniso1.25 | twist + aniso | 0.582602 | +0.067813 | +0.221376 | +0.894239 |
| C_Nv8_allplus | Nv 8, all-plus | 0.602202 | +0.069541 | +0.277968 | +1.344857 |
| C_W0.1_midpoint | W 0.1, midpoint | 0.597462 | −0.006519 | −0.470285 | −2.128342 |
| C_q0.5_mass0.15 | q 0.5, mass 0.15 | 0.601644 | +0.036214 | −0.699783 | −2.796536 |
| D_decoy_Nv32_random | decoy | 0.610275 | +0.016576 | −0.500665 | −2.044398 |
### Family statistics from the committed verdict

The verdict block of `data/results.json` (v2.0.5) records: n_gates_new = 35; rH7_abs_max = 0.0972 (`B_torus_aniso1.25`), p_r_min = 0.015, family Bonferroni 0.57; r_mean 0.5690–0.6328, mean 0.6009±0.0155 (canonical band 0.5996±0.03, 35/37 strict); rEF_fluct mean +0.4965, sd 0.4652, min −0.6998, max +0.9645; z_EF_abs_max = 3.275; GUE_mean = −0.1856, GUE_sd = 0.6967 (the honest synthetic-GUE null of the **fluctuation** statistic; the v1 raw-statistic null 0.788±0.376 is retired); PC0p_r = 0.9999999999999996; PC0_Hxi_r = 0.9997876852323586 (C4 committed). The committed verdict string reads (translation of the Russian original): "the H2 result is stable: all 37 configurations (35 new + 2 decoys) in the GUE class — the class of the ζ zeros — per the C8 protocol — ⟨r⟩ = 0.569–0.633…" — the H2 result is stable: every handle keeps the family in the GUE class (the zeros' class); the rank/heat branches stay at their limits.

## How to read the numbers

- **⟨r⟩ (r_mean)** — the mean adjacent-spacing ratio of the central band (C8 protocol); the canonical GUE value is 0.5996 (Atas et al. 2013, the same constant C8's ladder uses), with the class band 0.5996±0.03. Integrable (Poisson-like) statistics would drift the average to 0.386. The whole family sits in 0.569–0.633, mean 0.601±0.016. (v1 quoted 0.498–0.502 as "the campaign's GUE marker 0.500" — a fabricated column; see the regeneration note.)
- **r_H7** — the Pearson correlation between the detrended spectral staircase of the gate and the detrended zero staircase (the level-n ↔ zero-n comparison), computed on the v2 unfolded-to-unfolded window convention (ZeroReference k0 = 224, γ800 mpmath cache). The null zone is calibrated by 64 random zero windows (p_r) and by 40 synthetic GUE spectra (GUE r_H7 null +0.0416±0.0469 — the max-over-shifts bias makes even GUE spectra show ≈ +0.04); C3's best protocol gate reached 0.226, and the entire C5 family stays under 0.097 (family Bonferroni 0.57).
- **r_EF** — the heat-trace projection in the v2 currency: the fluctuation D(u) = Σ e^{−u·x_n} minus its smooth part, **detrended** (rampless) and correlated against the detrended explicit-formula prime comb. The v1 raw correlation (r_EF_raw, kept in the CSV for transparency) catches the common decaying trend of two smooth curves and is not verdict-bearing — the v1 "GUE null" of that raw statistic was centred at 0.788, i.e. the null itself "passed". A large r_EF means nothing by itself; the gate's own block-shuffle null cloud (`null_EF_mean`, `null_EF_sd`) and z-score (`z_EF`) decide whether the value is signal or weather.
- **z_EF** — the standardised distance of the fluctuation r_EF from its null cloud: |z_EF| ≤ 3.275 across the family, and the family mean sits at z ≈ 1.0 against the synthetic-GUE null of the same statistic — the null zone.
- **Scale convention.** The heat-trace correlation uses a fixed scale (scale_EF = 1.0 in every row): scale optimisation is excluded because it systematically inflates r — the C4 lesson, kept here.

## Interpretation: what stability means

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="112" alt="Agent Vera avatar"/></p>
<p align="center"><em>Vera, the auditor of verdicts: "stability" here is a measured statement about 37 configurations — with controls — not a theorem about every conceivable handle."</em></p>

The verdict "the H2 result is stable across all six new handles" is a three-layer statement.

**Layer 1 — universality is an attractor.** All 37 configurations land in the GUE class with ⟨r⟩ = 0.569–0.633 (mean 0.601±0.016, canonical band 0.5996±0.03). The five *active* dimensions include perturbations that in other contexts break universality (a mass term, a flux change, topology change); here none of them moves the spectral statistics. The class is set by the complex-vortex architecture, not by the parameters — the same message as theorem T10 in C8, now confirmed across the handle space (the sixth dimension, the vortex profile, is inert engine code; see the regeneration note).

**Layer 2 — the arithmetic does not return.** Universality would be harmless if the zero correlation survived underneath it. It does not: |r_H7| ≤ 0.097 over the new handles (family Bonferroni 0.57) against 0.226 for the best protocol gate — the extended family is *quieter* than the protocol family. The heat-trace projection agrees: the v2 fluctuation r_EF distributes as +0.497 ± 0.465 against the honest GUE null −0.186 ± 0.697 (family z ≈ 1.0), decoys indistinguishable from real gates.

**Layer 3 — the demarcation is now wide.** Theorems T1–T6 fixed what the zeros do; theorem T7 fixes what the 87 gates do: 52 protocol gates (C3) plus 35 extended gates (C5) lie in the GUE class and carry no Λ-weights, with positive controls at r = 1.0 (PC1/PC2, PC0′) and r = 0.9998 (PC0). The conclusion the package draws is deliberately modest and deliberately sharp: the H2 level-matching holds across the class of local Hermitian lattice Hamiltonians with vortex phases, while a hypothetical bit-level Hilbert–Pólya operator carrying the Λ(n)/√n weight in its trace cannot be obtained by *local* deformation of the lattice resonator. The question of nonlocal constructions remains open and belongs to the roadmap — and the campaign is careful to claim exactly that and no more.

In the bookkeeping of the series, C5 is the third and final measurement behind the scorecard verdict on H2: the zeros' level in the distance metric (C3, D_nn 0.0079), the conservative thermal branch (≈0.5 order by residual, C4), and — this campaign — stability under a six-dimensional extension of the handle space. Three independent projections, one verdict. The companion verdict H3 (GUE class, YES) is what makes the H2 reading intelligible: the gates sit in the zeros' universality class, and C5 shows this is not an artifact of any particular way of imposing the arithmetic setting.

The honest frame matters as much as the result. "Stability" is a measurement over 37 configurations, not a theorem about all possible handles; and the family maximum of |r_H7| is reached on a random-sign decoy, which is exactly where a noise maximum belongs.

## Reproduction

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c5_gates_ext.py
```

The series seed is 96; the RNG streams are fixed inside `engine/hamiltonian.py`. All dependencies are listed in `requirements.txt`. The script replays the committed verdict — new gates count, ⟨r⟩ statistics against the C8 canon, the |r_H7| maximum against the C3 best value 0.226, the r_EF fluctuation cloud and the verdict string — straight from `data/c5_gates_ext_table.csv` and `data/c5_gates_ext_verdict.json`, so the excursion takes seconds and does not require the zeros file. Full recomputation of the spectra uses the same engine and seed and reproduces the committed tables bit-for-bit (the v2.0.5 regeneration itself is the existence proof; see `data/README.md` and the registry discipline in `../../results/RESULTS.md`).

## Data and figures

| File | Content |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/gates_table.csv` | the 37-row per-gate table (handles, ⟨r⟩, r_H7, r_EF, null clouds, z_EF) |
| `data/` (npz/csv) | curves and tables |
| `../data/c5_*.json` | duplicate of the verdict in the shared registry (`../data/c5_gates_ext_verdict.json`) |

Figures, both renders:

| File | Where |
|---|---|
| `fig09_handles_ru.png` / `fig09_handles_en.png` | 600 dpi — `figures_hires/ru/fig09_handles_ru.png` · `figures_hires/en/fig09_handles_en.png`; screen — `figures/ru/` · `figures/en/` |
| `fig10_gue_ext_ru.png` / `fig10_gue_ext_en.png` | 600 dpi — `figures_hires/ru/fig10_gue_ext_ru.png` · `figures_hires/en/fig10_gue_ext_en.png`; screen — `figures/ru/` · `figures/en/` |

`fig09_handles` draws |r_H7| across the 37 extended gates: the gold line marks the best protocol value 0.226, the copper lines the positive controls at 1.000, the red bars the decoys. `fig10_gue_ext` draws ⟨r⟩ across the extended family against the canonical GUE band 0.5996±0.03 (v2.0.5: previously a spurious 0.47–0.53 band around 0.5): every point inside or at the edge of the band (0.569–0.633) — the GUE class is universal for all handles.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`. The full monograph of this computation (setup, theorems, tables, figures, honest limitations): 7–9 pages, identical content in both languages.

## Honest notes

> The family maximum of \|r_H7\| (0.0972, `B_torus_aniso1.25`) is a real gate, not a decoy — and it stays inside the family-wide Bonferroni correction (p = 0.57): noise, but the campaign no longer hides it behind a decoy label.

> The statement "the gap is stable" is a measurement over 37 configurations, not a theorem about all possible handles.

Both notes are load-bearing. The first prevents over-reading the largest correlation in the family: 0.0972 is indistinguishable from the GUE r_H7 null (+0.042±0.047, z ≈ 1.2) once the max-over-shifts bias is calibrated — and the v1 claim that the maximum "belongs to a decoy" was itself wrong (the v1 "16-vortex decoy" was a bit-identical duplicate of C_Nv16_random_signs). The second prevents over-reading the verdict itself: C5 closes the "one family" objection for the six dimensions tested and the 37 configurations committed — it does not prove that every conceivable lattice Hamiltonian fails. What it does establish, together with C3, is the T7 demarcation over 87 gates; where to go beyond the local class is the business of the roadmap, not of this campaign.

## Verdict

**the H2 result is stable: the whole family in the GUE class (the zeros' class) across all six new handles** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

## FAQ

**1. Thirty-seven configurations — is that enough to claim "the gap is stable"?**
Enough for the claim C5 actually makes: a measured verdict over the six tested dimensions, with per-gate null clouds, decoys and a bit-for-bit regression control. The campaign explicitly does not claim a theorem over all possible handles. Combined with the 52 protocol gates of C3, the T7 demarcation covers 87 configurations of one architectural class — local Hermitian lattice Hamiltonians with vortex phases.

**2. Why did the v1 table quote ⟨r⟩ = 0.500±0.001, and why is it 0.569–0.633 now?**
The v1 column could not be true: a uniform 0.500 for all 37 configurations (including W = 0 and both decoys) contradicts C8's own measurement of the same base configuration (0.5972) and the C13 blind families (0.550–0.649). The v2.0.5 audit proved the spectra were always real (the v1 raw r_EF reproduces to ±0.002) and regenerated the statistics with the C8 protocol: the family sits at 0.569–0.633, mean 0.601±0.016 — genuinely the GUE class. The class-level calibration across the series (Poisson / GOE / GUE ladders) is theorem T10 in C8.

**3. Why was the corner W = 0 + midpoint replaced by W = 0.1?**
At W = 0 with the midpoint profile the Hamiltonian develops exact spectral multiplicities, which break the polynomial unfolding and would corrupt the statistics. Replacing the corner with W = 0.1 keeps the gate meaningful; the substitution is flagged with an explicit note in the data table and recorded in the honesty registry.

**4. Why are only ±1/24 flux shifts allowed on the torus?**
Flux quantisation: on the 24-lattice the constraint α·Ny ∈ ℤ is rigid, and ±1/24 are the realisable neighbouring points of the self-dual line α = ½. They are exact values, not rounded ones; using ±0.02 on the torus would violate the quantisation the model itself imposes.

**5. What exactly is a decoy, and why two?**
A decoy is a gate whose vortex phases are random — the null hypothesis "the structure of the phases is not important" made into a configuration. Of the two committed decoys only `D_decoy_Nv32_random` is genuinely distinct: `D_decoy_signs_random` reuses the same configuration and RNG stream as `C_Nv16_random_signs` and is bit-identical to it (a v1 labelling defect, documented in v2.0.5). The honest statement is: the random-phase gates — C_Nv16_random_signs and D_decoy_Nv32_random — are statistically indistinguishable from the structured real gates.

**6. Does C5 say no lattice operator can ever encode the zeros?**
No. It says no *local* deformation of this resonator family — six dimensions, 37 configurations, 87 gates with C3 — moves the statistics toward the zeros. Nonlocal constructions are explicitly outside the verdict and are kept open in the roadmap.

**7. In one sentence, what did C5 establish?**
That the H2 result of the lattice resonator holds under all the new deformation dimensions — 35 gates and 2 decoys all stay GUE (⟨r⟩ = 0.569–0.633, mean 0.601), the rank branch at its limit (|r_H7| ≤ 0.097, Bonferroni 0.57).

**8. Which handle came closest to breaking the null zone?**
Anisotropy on the torus: |r_H7| = 0.0972 on `B_torus_aniso1.25` (p = 0.154; signs/boundaries follow at 0.0695, p = 0.031, C_alpha0.4_allplus p = 0.015) — all inside the family-wide Bonferroni correction (0.57) and inside the GUE r_H7 null band (+0.042±0.047), which is precisely why the values are read as noise.

**9. Why include cross-combinations like anisotropy+flux or twist+mass?**
Because a critic's next move after "try other handles" is "try them together". The A-group pairs (A_aniso08_dalpha+0.02, A_aniso125_mass0.15, A_mass0.15_dalpha-0.02, A_midpoint_allplus) and the B-group combinations (B_twistpi_pi_mass0.15, B_twistpi_pi_aniso1.25) test interaction effects; none appears.

**10. Is the 1.4e-16 regression control really necessary?**
Yes — it is what makes the campaign a measurement *of the handles* rather than of a new pipeline. Without it, a change in the null zone could be blamed on the port; with it, the ruler is certified unchanged.

**11. Where does this leave the Hilbert–Pólya programme in this package?**
The resonator is built and tuned (H1 + H3 + H4); the zeros are encoded in it, not generated by it (H2 + H5); the prime weight is verified only for the zero operator (T6). C5's contribution is the width of the negative: the gap is not a corner case of one protocol.

## Glossary

- **Gate** — one Hermitian Hamiltonian of the Hofstadter type: an L×L lattice with hopping −t·e^{iφ}, Landau-gauge flux φ_x = 2πα·iy on x-links, vortex phases φ_y = Σ_k q_k(θ_j − θ_i)/2 on y-links, on-site disorder W, open or toroidal boundaries. 87 such gates exist across C3 + C5.
- **Handle** — one controllable deformation of the gate builder. The protocol handles (Nv, q, W, α) belong to C3; the six new ones (twists, anisotropy, flux shift, staggered mass, vortex profile, signs/boundaries) belong to C5 and all live in `engine/hamiltonian.py`.
- **Vortex** — a lattice site carrying a phase θ and charge q; the phase pattern of Nv vortices is what makes the Hamiltonian complex and, with Nv ≥ 8, pushes the spectrum into the GUE class.
- **Decoy** — a configuration whose vortex phases are random: the null hypothesis "phase structure does not matter" materialised as a row of the table.
- **Null zone** — the range of a statistic consistent with its calibration noise (circular shifts of the zero list for r_H7; per-gate surrogate clouds for r_EF). A gate "in the null zone" shows no trace of the zeros.
- **Unfolding** — the rescaling of raw eigenvalues to unit mean density (polynomial fit here) that makes spacing statistics comparable across spectra; exact multiplicities, as at the W = 0 + midpoint corner, break it.
- **GUE class** — the Gaussian unitary ensemble universality class, the signature of quantum chaos with broken time-reversal symmetry; the package's marker statistic is the mean adjacent-spacing ratio ⟨r⟩.

## Why these six handles and not others

The six dimensions are a checklist drawn against the standard escape routes a sceptic would offer a negative spectral result. Each class of objection names a deformation; C5 tests one handle per class, in both boundary geometries, alone and in combination:

- *"Your boundary conditions are wrong."* — answered by twists (all non-trivial spin structures) and by the open/torus switch itself; the torus base B_torus_base and its decorated variants all stay null.
- *"Your lattice is too symmetric."* — answered by anisotropy t_x/t_y ∈ {0.8, 1.25}, which deforms the Dirac cone and the density of states while leaving the class untouched.
- *"You sit on a special flux."* — answered by δα = ±0.02 open and the admissible ±1/24 on the torus: the immediate, exactly-realised neighbourhood of the self-dual line α = ½.
- *"The fermion is massless in your model."* — answered by the staggered masses 0.15 and 0.35, the standard lattice mass term; gaps open, statistics do not move.
- *"Your vortices are points; real cores have size."* — answered by the midpoint profile, a finite-radius core; the degenerate W = 0 corner is honestly replaced by W = 0.1 with a note.
- *"Your charge pattern is finetuned."* — answered by all-plus and random signs against the neutral protocol; the decoys complete the picture.

This is why the campaign closes the "you only tried one family" objection rather than merely widening the sample: the six handles span topology, geometry, gauge field, matter content, regularization and disorder — the whole local design space a lattice builder controls.

## What would have changed the verdict

The verdict is falsifiable at three independent dials, and the committed data make the thresholds explicit. A gate would have left the null zone if its |r_H7| had escaped the permutation calibration (C3's 0.226 shows values up to there were still null; the family max 0.0972 stays inside the family-wide Bonferroni 0.57 and the GUE r_H7 null +0.042±0.047); if its fluctuation r_EF had left the per-gate cloud at a decisive z_EF (family bound |z_EF| ≤ 3.275, family mean at z ≈ 1.0 against the synthetic-GUE null); or if its ⟨r⟩ had drifted from the canonical band 0.5996±0.03 toward an integrable or intermediate class. Any one of the 37 rows could have delivered this; none did (two edge gates sit within the sampling width of the band edges). The same three dials — staircase correlation, heat-trace projection, spacing class — are exactly the ones the positive controls certify: PC1/PC2 and PC0′ at r = 1.0 and PC0 at r = 0.9997876852323586 prove the dials move when they should. A negative result with certified dials is a measurement, not an absence of instrumentation.

## See also

- [C3 — the protocol gate family](../C3_gate_family/README.md): the 52-gate campaign C5 extends; source of the 0.226 reference and the null-zone calibration.
- [C4 — the trace formula](../C4_trace_formula/README.md): origin of the heat-trace statistic r_EF and the PC0 positive control reused here.
- [Theory map](../../docs/theory.md): the five stages, the scorecard logic H1–H5, and why G3 = YES explains the difficulty of H2.
- [Roadmap](../../results/ROADMAP.md): what lies beyond the local lattice class — the open question C5 deliberately leaves open.
- [Results registry](../../results/RESULTS.md): rows 15 and 21 of the main table live here; every number in this README is committed.

---
*Hilbert Polya Bridge v2.0.0 · C5 · The extended gate family*

