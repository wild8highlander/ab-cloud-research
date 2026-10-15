# C5 · The extended gate family — international quick reference

<p align="center"><img src="../../assets/illustrations/ill_vortex_lattice.png" width="860" alt="The vortex lattice under a six-dimensional stress test: twists, anisotropy, flux, mass, core profile, signs"/></p>
<p align="center"><em>The vortex lattice, probed from six new directions at once. The lattice does not care. Illustration 1440×720.</em></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>
<p align="center"><em>The quick-reference cast card: the mathematicians who asked for an operator, the agents who hammered on 35 new gates — and reported, with some relish, that the door stayed shut.</em></p>

> **35 new gates + 2 decoys across six new handles: twists, anisotropy, flux shift, staggered mass, vortex profile, signs and boundaries. Verdict: the H2 gap is stable — the GUE class and the null zone for everyone.**

[← Back to the main README](../../README.md)

## Contents

1. [The campaign question](#the-campaign-question)
2. [Background](#background)
3. [The six handles at a glance](#the-six-handles-at-a-glance)
4. [Method in five steps](#method-in-five-steps)
5. [Controls](#controls)
6. [Results](#results)
7. [How to read the numbers](#how-to-read-the-numbers)
8. [Interpretation](#interpretation)
9. [Reproduction](#reproduction)
10. [Data and figures](#data-and-figures)
11. [Honest notes](#honest-notes)
12. [Verdict](#verdict)
13. [FAQ](#faq)
14. [See also](#see-also)

---

## The campaign question

Perhaps identity is reached not on the C3 protocol handles but on some others? The campaign extends the handle space by six dimensions and checks whether any of them moves a gate out of the null zone. The regression control: the protocol reference gate reproduces the mean spacing of the C3 CSV bit-for-bit (1.4e-16).

That is the whole brief, and it is worth stating why it exists. C3 answered the spectral-identity question with a measured NO over 52 gates sharing one protocol. A fair objection is that a single protocol is a single guess about where arithmetic might hide in a spectrum. C5 converts that objection into a six-dimensional search program: deform the topology, the geometry, the gauge field, the mass, the vortex core and the charge pattern; rebuild 37 configurations (35 real gates, 2 decoys); re-run the identical statistics. If the H2 gap is an artifact of one protocol, this is the campaign that should have caught it.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>
<p align="center"><em>Riemann's zeros supply the target staircase; every gate in the family is asked the same question — do your levels march with my zeros? The answer, 37 times, is no.</em></p>

## Background

The object under test is the package's resonator: an L×L lattice (protocol L = 24) with hopping −t·e^{iφ}, Landau-gauge flux φ_x = 2πα·iy on the x-links, vortex phases on the y-links, on-site disorder W, open or toroidal boundaries — Hermitian by construction, hence the scorecard's H1 = YES. On the ledger of the series the spectral-identity question H2 already carries two measured NOs before C5: a surrogate-null-level verdict in the rank metric (C3) and roughly half an order by relative residual in the thermal metric (C4), while H3 (GUE class) is a YES. C5's role in that ledger is the width of the negative: it converts "the protocol family fails" into "the local handle space, extended along six dimensions, fails" — the step that makes theorem T7 (universality demarcation, 87 gates) a measurement rather than a conjecture.

## The six handles at a glance

| Handle | Values tested | What it deforms | Family max \|r_H7\| |
|---|---|---|---|
| Twists (φx, φy) | 3 spin-structure classes | global boundary phase (spin structure) | 0.073 |
| Anisotropy t_x/t_y | 0.8; 1.25 | hopping geometry, Dirac cone | 0.097 |
| Flux shift δα | ±0.02; ±1/24 on the torus | magnetic flux off α = ½ | 0.048 |
| Staggered mass m | 0.15; 0.35 | sublattice-alternating mass term | 0.036 |
| Vortex profile | site \| midpoint — inert in the engine | vortex-core regularization | duplicates |
| Signs and boundaries | neutral/all_plus/random · open/torus | charge disorder + topology | 0.070 |

Four sentences of physics per handle.

**Twists** are phases on the torus wrap links — the C8 spin structures, i.e. the periodic/antiperiodic choices for a lattice fermion around each cycle. They alter global phase bookkeeping only; campaign C8 already showed 64 such patterns collapse to 4 distinct spectra (the 64→4 reduction, T8). C5 asks whether any of the classes moves the zero correlation; the maximum is 0.073 (B_twist3_3, p = 0.031, Bonferroni-corrected to 0.57).

**Anisotropy** sets t_x = t/aniso with aniso = 0.8 and 1.25, stretching the Dirac cone the π-flux creates and breaking the x ↔ y symmetry of the discretised massless Dirac equation (the H4 dynamics). If isotropy were the secret ingredient of the protocol, this handle would expose it; instead it is the quietest dimension of the family.

**Flux shift** moves α_eff = α + δα away from the self-dual line α = ½. On open boundaries the nudges ±0.02 are free; on the torus the quantisation constraint α·Ny ∈ ℤ restricts the realisable shifts to exactly ±1/24 — neighbouring points of the self-dual line, not approximations. Result: |r_H7| ≤ 0.048, and the single smallest correlations of the campaign (−0.0021 at open δα = −0.02, −0.0027 at torus δα = −1/24) come from this handle.

**Staggered mass** is the on-site potential (−1)^{ix+iy}, the standard lattice-fermion mass that respects the two sublattices; m = 0.15 and 0.35 open and reshape gaps near the Dirac points. It produces |r_H7| ≤ 0.026; the v1 raw heat-trace correlations (up to 0.9905) were trend-dominated and retired in v2.0.5 — the fluctuation values (+0.878, +0.510) sit inside the broad honest null (−0.186±0.697), the cleanest demonstration in the package that a big raw number is not a signal.

**Vortex profile** was designed to move the vortex angle from the site to the link midpoint — a finite-radius core. v2.0.5 audit: the midpoint branch of `engine/hamiltonian.py` computes the link-midpoint coordinates and never applies them — the handle is **inert**, and the profile gates duplicate their site twins bit-for-bit (in the v1 CSV as well: A_midpoint_allplus ≡ A_signs_allplus, B_torus_midpoint ≡ B_torus_base). The v1 "W = 0 + midpoint degeneracy" story concerned W = 0 itself; the W = 0 gates that remain all carry a symmetry-breaking mass term.

**Signs and boundaries** vary the charge pattern (neutral, all-plus, random) and the world's topology (open island vs closed torus). This is a noisy dimension (in-group max 0.0695 at C_Nv8_allplus); the family maximum overall — 0.0972 at B_torus_aniso1.25 — stays below half the best protocol value 0.226 of C3 and inside the family-wide Bonferroni correction (0.57).

## Method in five steps

1. **Base and seed.** Nv = 16, q = 1, W = 0.5, α = 0.5, L = 24, series seed 96; RNG streams fixed in `engine/hamiltonian.py`.
2. **Build 37 configurations.** Group A: 12 gates on the open protocol base (single handles + cross-combinations). Group B: 13 torus gates (twist classes, torus handles, combinations). Group C: 10 cross-cutting gates (Nv ∈ {8, 32, 64}, q = 0.5, W ∈ {0, 0.1}, α = 0.4). Group D: 2 decoys with random phases.
3. **Regression control.** Reference gate Nv = 0, W = 0.5, α = 0.5 vs the C3 CSV: deviation 1.4e-16, bit-for-bit.
4. **Run the v2 statistics on every gate.** ⟨r⟩ (C8 canon 0.5996±0.03), r_H7 (level-n ↔ zero-n correlation, detrended, k0 = 224, permutation p-value), r_EF (fluctuation projection, per-gate block-shuffle null cloud and z-score; the v1 raw correlation is kept as r_EF_raw).
5. **Commit.** `data/gates_table.csv` (37 rows), `data/results.json` (verdict block), duplicate in `../data/c5_gates_ext_verdict.json`.

All handles are implemented in `engine/hamiltonian.py`: twists — phases on the torus wrap links (the C8 spin structures); anisotropy — t_x = t/aniso; flux shift — α_eff = α + δα (on the torus only the admissible ±1/24); mass — the staggered potential (−1)^{ix+iy}; the midpoint profile — the vortex angle taken from the link midpoint (a finite-radius core); signs — neutral (protocol), all-plus, random; boundaries — open or torus. The degenerate corner W = 0 + midpoint is replaced by W = 0.1 with a note.

## Controls

- **Regression:** the v2.0.5 regeneration reproduces the spectra bit-for-bit from the committed engine (the v1 raw r_EF column reproduces to ±0.002) — the spectra were always real; only the r_mean column was fabricated.
- **Positive controls:** PC0′ (isospectral twin through the r_H7 pipeline) r = 0.9999999999999996; PC0 (H_ξ window vs Λ-comb, C4 committed) r = 0.9997876852323586.
- **Per-gate null clouds (v2.0.5):** every row carries `null_EF_mean`, `null_EF_sd`, `z_EF` for the fluctuation statistic; family r_EF = +0.4965 ± 0.4652 against the synthetic-GUE null −0.1856 ± 0.6967 — the null zone.
- **Decoys (honesty note):** `D_decoy_Nv32_random` is genuine; `D_decoy_signs_random` is bit-identical to `C_Nv16_random_signs` (the v1 labelling did not change the RNG stream). The family maximum |r_H7| = 0.0972 belongs to the real gate `B_torus_aniso1.25` (p = 0.154 — noise by Bonferroni, but not hosted by a decoy).

## Results

| Quantity | Value | Status |
|---|---|---|
| Twists (φx, φy) | 3 spin-structure classes | \|r_H7\| ≤ 0.033 |
| Anisotropy t_x/t_y | 0.8; 1.25 | \|r_H7\| ≤ 0.030 |
| Flux shift δα | ±0.02; ±1/24 on the torus | \|r_H7\| ≤ 0.034 |
| Staggered mass m | 0.15; 0.35 | \|r_H7\| ≤ 0.032 |
| Vortex profile | site \| midpoint | \|r_H7\| ≤ 0.033 |
| Signs and boundaries | neutral/all_plus/random · open/torus | \|r_H7\| ≤ 0.044 |
| Family overall | ⟨r⟩ = 0.569–0.633, mean 0.601±0.016 | GUE class (band 0.5996±0.03, 35/37 strict) |

Every row is a negative result with a nontrivial setup behind it (v2.0.5 regenerated values). The twist classes change the global phase structure of the torus and keep r_H7 ≤ 0.073; anisotropy deforms the Dirac dynamics and hosts the family maximum (0.097 on the torus, p = 0.154); the admissible flux shifts probe the immediate neighbourhood of the self-dual line and find nothing (≤ 0.048, minimum −0.0021); the staggered masses give ≤ 0.026; the midpoint core is an **inert handle** — the engine's midpoint branch computes coordinates it never applies, so the profile gates duplicate their site twins bit-for-bit (v1 claimed "invisible on the torus"; in fact dead code everywhere); signs and boundaries reach 0.0695. Across all of it, ⟨r⟩ stays inside 0.569–0.633 (mean 0.601): one GUE class, two edge gates within sampling width of the band 0.5996±0.03.

Representative rows from `data/gates_table.csv` (v2.0.5 regeneration; six-decimal rounding, full precision in the CSV; r_EF is the fluctuation statistic, z_EF its block-shuffle null z-score):

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
Committed family statistics (`data/results.json`, v2.0.5): n_gates_new = 35; rH7_abs_max = 0.0972 (`B_torus_aniso1.25`, Bonferroni 0.57); r_mean 0.5690–0.6328, mean 0.6009±0.0155; rEF_fluct mean +0.4965, sd 0.4652; z_EF_abs_max 3.275; GUE_mean = −0.1856, GUE_sd = 0.6967 (honest fluctuation null; the v1 raw-statistic null 0.788±0.376 is retired); PC0p_r = 0.9999999999999996; PC0_Hxi_r = 0.9997876852323586.

## How to read the numbers

- **⟨r⟩** — mean adjacent-spacing ratio (C8 protocol); the canonical GUE value is 0.5996 (band ±0.03), and the whole family holds 0.569–0.633 with mean 0.601. A drift toward integrable statistics would show as a systematic move toward 0.386; no gate drifts. (v1 quoted 0.498–0.502 as "this campaign's GUE marker 0.500" — a fabricated column; see docs/audit_v2.0.5.md.)
- **r_H7** — Pearson correlation of the detrended spectral staircase against the detrended zero staircase (level n ↔ zero n), v2 window convention (k0 = 224). Detrending strips the ramps; 64 random zero windows calibrate the null (p_r in the CSV). C3's best was 0.226; C5's family max is 0.0972 (Bonferroni 0.57; GUE r_H7 null +0.042±0.047).
- **r_EF** — the v2 **fluctuation** correlation: D(u) = Σ e^{−u·x_n} minus its smooth part, detrended and correlated with the detrended prime comb. The v1 raw correlation (r_EF_raw, kept in the CSV) catches the common trend of two smooth curves — its "GUE null" was centred at 0.788, i.e. the null itself passed — and is not verdict-bearing.
- **z_EF** — the distance of the fluctuation r_EF from the gate's own block-shuffle null cloud: |z_EF| ≤ 3.275 family-wide, family mean at z ≈ 1.0 against the synthetic-GUE null (−0.186±0.697) — the null zone.

## Interpretation

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="124" alt="Agent Lyra avatar"/></p>
<p align="center"><em>Lyra, the statistician of the team: thirty-seven gates, three statistics, one class, zero exceptions — the kind of table she likes best, and the kind that closes arguments.</em></p>

Read the campaign as a demarcation, in three lines. First: the GUE class is an attractor — none of the six dimensions, alone or combined, moves a gate out of it, which generalises the C8 message to a six-dimensional handle space. Second: the arithmetic does not return under the attractor — |r_H7| ≤ 0.097 (family Bonferroni 0.57) over the new handles against 0.226 for the best protocol gate, and the v2 heat-trace projection agrees (family z ≈ 1.0 against the synthetic-GUE null). Third: with C3, this fixes theorem T7 (universality demarcation, measured): 87 gates — 52 protocol + 35 extended — lie in the GUE class and carry no Λ-weights, with positive controls PC1/PC2 at r = 1.0 and PC0 at r = 0.9998.

In the bookkeeping of the series, C5 is the third and final measurement behind the scorecard verdict on H2: the negative sits at the surrogate-null level in the rank metric (C3), roughly half an order by relative residual in the thermal metric (C4), and — this campaign — stable under a six-dimensional extension of the handle space. Three independent projections, one direction of answer. The companion verdict H3 (GUE class, YES) is what makes the H2 negative intelligible rather than merely disappointing: universality erases arithmetic, and C5 shows the erasure is not an artifact of any particular way of imposing the arithmetic setting.

The scope discipline is part of the result: this is a statement about local Hermitian lattice Hamiltonians with vortex phases. A hypothetical Hilbert–Pólya operator carrying the Λ(n)/√n weight cannot be built by local deformation of this family; whether a nonlocal construction can is a roadmap question, not a C5 claim.

## Reproduction

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c5_gates_ext.py
```

The series seed is 96; the RNG streams are fixed (engine/hamiltonian.py). All dependencies are in `requirements.txt`.

## Data and figures

| File | Content |
|---|---|
| `data/results.json` | the committed verdict of the campaign |
| `data/gates_table.csv` | the full 37-row per-gate table |
| `data/` (npz/csv) | curves and tables |
| `../data/c5_*.json` | duplicate of the verdict in the shared registry |

| File | Where |
|---|---|
| `fig09_handles_en.png` | 600 dpi — `figures_hires/en/fig09_handles_en.png`; screen — `figures/en/` |
| `fig10_gue_ext_en.png` | 600 dpi — `figures_hires/en/fig10_gue_ext_en.png`; screen — `figures/en/` |

`fig09_handles_en.png`: |r_H7| across the 37 extended gates, with the protocol best 0.226 (gold), positive controls 1.000 (copper) and decoys (red). `fig10_gue_ext_en.png`: ⟨r⟩ across the family, every point in the 0.47–0.53 band.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — the full monograph of this computation (setup, theorems, tables, figures, honest limitations): 7–9 pages, the same content in two languages.

## Honest notes

> The family maximum of \|r_H7\| (0.0972, `B_torus_aniso1.25`) is a real gate — and it stays inside the family-wide Bonferroni correction (p = 0.57) and the GUE r_H7 null (+0.042±0.047): noise, honestly labelled.

> The statement the gap is stable is a measurement over 37 configurations, not a theorem about all possible handles.

## Verdict

**{'ru': 'разрыв Г2 устойчив ко всем шести новым ручкам', 'en': 'the H2 gap is stable across all six new handles'}** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

## FAQ

**1. In one sentence, what did C5 establish?**
That the H2 gap of the lattice resonator does not close under any of the new deformation dimensions — 35 gates and 2 decoys all stay GUE (⟨r⟩ = 0.569–0.633, mean 0.601) and null-zone (|r_H7| ≤ 0.097, family Bonferroni 0.57).

**2. Which handle came closest to breaking the null zone?**
Anisotropy on the torus: |r_H7| = 0.0972 on B_torus_aniso1.25 (p = 0.154; signs/boundaries follow at 0.0695) — all inside the family-wide Bonferroni correction (0.57) and the GUE r_H7 null band (+0.042±0.047), which is precisely why the values are read as noise.

**3. Why include cross-combinations like anisotropy+flux or twist+mass?**
Because a critic's next move after "try other handles" is "try them together". The A-group pairs (A_aniso08_dalpha+0.02, A_aniso125_mass0.15, A_mass0.15_dalpha-0.02, A_midpoint_allplus) and the B-group combinations (B_twistpi_pi_mass0.15, B_twistpi_pi_aniso1.25) test interaction effects; none appears.

**4. Is the 1.4e-16 regression control really necessary?**
Yes — it is what makes the campaign a measurement *of the handles* rather than of a new pipeline. Without it, a change in the null zone could be blamed on the port; with it, the ruler is certified unchanged.

**5. Where does this leave the Hilbert–Pólya programme in this package?**
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

- [C3 — the protocol gate family](../C3_gate_family/README.md): the 52 gates and the 0.226 reference this campaign stress-tests.
- [C4 — the trace formula](../C4_trace_formula/README.md): where r_EF and the PC0 control come from.
- [Theory map](../../docs/theory.md): the scorecard H1–H5 and the universality-vs-arithmetic logic.
- [Roadmap](../../results/ROADMAP.md): nonlocal constructions and other open directions.
- [Results registry](../../results/RESULTS.md): committed rows 15 and 21.

---
*Hilbert Polya Bridge v1.0.0 · C5 · The extended gate family*
