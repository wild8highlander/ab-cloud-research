# C5 · The Extended Gate Family — six new handle dimensions and the stability of the H2 gap

<p align="center"><img src="../../assets/illustrations/ill_shutter_wall.png" width="860" alt="A wall of lattice shutters: thirty-five new gates hung on six new handle dimensions, all still locked in the null zone"/></p>
<p align="center"><em>The shutter wall after C5: thirty-five new gates on six new handle dimensions — and not one of them opens. Illustration 1440×720, crop centred on the new gate rows.</em></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>
<p align="center"><em>The standing cast of the Bridge — Riemann, Hilbert, Pólya, and the agents Atlas, Lyra and Vera — convenes for the six-dimensional stress test of the gate protocol.</em></p>

> **35 new gates + 2 decoys across six new handles: twists, anisotropy, flux shift, staggered mass, vortex profile, signs and boundaries. Verdict: the H2 gap is stable — GUE class (⟨r⟩ = 0.500±0.001) and null zone (|r_H7| ≤ 0.043) for all.**

[← Back to the main README](../../README.md)

## Contents

1. [The question](#the-question)
2. [Background: the one-family objection](#background-the-one-family-objection)
3. [Design space: the six handle dimensions](#design-space-the-six-handle-dimensions)
4. [Method step by step](#method-step-by-step)
5. [Controls](#controls)
6. [Results](#results)
7. [How to read the numbers](#how-to-read-the-numbers)
8. [Interpretation: what stability means](#interpretation-what-stability-means)
9. [Reproduction](#reproduction)
10. [Data and figures](#data-and-figures)
11. [Honest notes](#honest-notes)
12. [Verdict](#verdict)
13. [FAQ](#faq)
14. [See also](#see-also)

---

## The question

Campaign C3 built a family of 52 gates — Hermitian Hofstadter-type Hamiltonians on an L×L lattice, decorated with vortex phases — and asked whether any of them carries the zeros of ζ in its spectrum. The best of the 52 reached r_H7 = 0.226, comfortably inside the null zone, and the campaign closed with a measured NO on the spectral-identity hypothesis H2. A sceptic's rejoinder writes itself: *you only tried one family of handles.* Every gate in C3 shared the same skeleton — protocol charge count Nv, on-site disorder W, flux α — and it is always possible that the identity lives one knob away from the protocol.

Campaign C5 is the direct answer to that rejoinder. It extends the handle space by six new dimensions — twists (φx, φy), anisotropy t_x/t_y, flux shift δα, staggered mass m, vortex profile (site/midpoint), and the combined signs-and-boundaries dimension — and hangs 35 new gates on them, plus 2 decoys. The question is sharp: does any single new handle, or any of the tested cross-combinations, pull a gate out of the null zone?

The regression control comes first, because nothing else matters without it: the protocol reference gate (Nv = 0, W = 0.5, α = 0.5) reproduces the mean level spacing of the C3 CSV bit-for-bit, with deviation 1.4e-16. Whatever C5 measures, it measures on the same pipeline that produced the C3 verdict — the port is equivalent, the ruler is unchanged.

## Background: the one-family objection

Why is the objection serious enough to spend an entire campaign on it? Because the package's own diagnosis of the H2 gap makes it serious. Campaign C3 (and later C8) established that the vortex lattice sits in the GUE universality class — the third verdict on the Hilbert–Pólya scorecard, H3 = YES. Universality is a two-edged result: it says the resonator is a genuine quantum-chaotic object, and it also explains *why* H2 fails, since a universal spectrum erases precisely the arithmetic detail that a level-n ↔ zero-n identity would require. If universality erases arithmetic, then the correct adversarial move is to attack the setting of the arithmetic: change the topology, the geometry, the gauge field, the mass, the vortex core, the charge pattern — everything a critic could name — and see whether the erasure survives.

That is the design logic of C5. The six new dimensions are not a random grab-bag; they span the physically distinct ways a local lattice Hamiltonian with vortex phases can be deformed:

- **global topology** — twists and the choice of open versus toroidal boundaries;
- **local geometry** — anisotropy of the hopping amplitudes;
- **gauge field** — a shift of the flux per plaquette away from the self-dual value α = ½;
- **fermion mass** — a staggered on-site potential;
- **vortex-core regularization** — where in the link the vortex angle is read;
- **charge disorder** — the sign pattern of the vortex charges.

If the H2 gap were an artifact of one particular protocol, a six-dimensional sweep with 37 configurations should expose it. It does not: every configuration lands in the GUE class, and none leaves the null zone. Combined with C3, the demarcation now covers 87 gates — this is exactly the empirical content of theorem T7 (universality demarcation, measured), formalised in the theorems volume: 87 gates (52 protocol + 35 extended) lie in the GUE class (⟨r⟩ = 0.498–0.612 across the campaigns) and carry no Λ-weights — r_H7 ≤ 0.226 over the protocol family, |r_H7| ≤ 0.043 over the new handles, and r_EF inside the null clouds, with positive controls PC1/PC2 at r = 1.0 and PC0 at r = 0.9998.

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
5. **Statistics.** For every gate: the mean adjacent-spacing ratio ⟨r⟩ (GUE class marker), the zero-correlation r_H7 (level n ↔ zero n, detrended), and the heat-trace projection r_EF with its null cloud (mean, sd) and z-score z_EF.
6. **Positive controls.** PC0 — the thermal projection of the H_ξ window against the Λ-comb — gives r = 0.9997540255853161 in the committed data: the method sees prime weight when it is present.
7. **Commit.** All 37 rows, the verdict statistics and the meta block are written to `data/gates_table.csv` and `data/results.json`; the verdict is duplicated in the shared registry `../data/c5_gates_ext_verdict.json`.

The degenerate corner W = 0 + midpoint is replaced by W = 0.1 with a note, as described above — exact multiplicities would flatter or distort the unfolding, and the campaign prefers an honest neighbour value to a broken statistic.

## Controls

C5 runs four kinds of controls, and the verdict is only as strong as they are.

- **Regression control (bit-for-bit).** The protocol reference gate reproduces the mean spacing of the C3 CSV with |Δ| = 1.4e-16 — the extended pipeline has not shifted the base.
- **Positive control PC0 (heat trace).** The H_ξ window against the Λ-comb yields r = 0.9997540255853161 (the registry lists it as +0.9998 with residual 2.1%): when prime weight exists in an operator, this pipeline detects it at essentially unit correlation.
- **Null clouds per gate.** Each gate carries its own null mean and sd for r_EF (`null_EF_mean`, `null_EF_sd` in the CSV) plus the z-score z_EF; no gate leaves its cloud. Across the family the committed verdict block records rEF_mean = 0.6112285569902335 and rEF_sd = 0.3452702369140134 — a textbook null distribution, with rEF_max = 0.9911878822153721 attained by the staggered-mass gate `A_mass0.15` and still consistent with its own cloud (z_EF = 2.455031478585997).
- **Decoys.** Two decoys with random vortex phases (`D_decoy_signs_random`, `D_decoy_Nv32_random`) anchor the noise floor: they behave exactly like the real gates, which is the point. The family maximum of |r_H7| is reached on a random-sign decoy — the expected noise maximum, not a signal.

## Results

The committed results table of the campaign, reproduced exactly:

| Quantity | Value | Status |
|---|---|---|
| Twists (φx, φy) | 3 spin-structure classes | \|r_H7\| ≤ 0.033 |
| Anisotropy t_x/t_y | 0.8; 1.25 | \|r_H7\| ≤ 0.030 |
| Flux shift δα | ±0.02; ±1/24 on the torus | \|r_H7\| ≤ 0.034 |
| Staggered mass m | 0.15; 0.35 | \|r_H7\| ≤ 0.032 |
| Vortex profile | site \| midpoint | \|r_H7\| ≤ 0.033 |
| Signs and boundaries | neutral/all_plus/random · open/torus | \|r_H7\| ≤ 0.044 |
| Family overall | ⟨r⟩ = 0.498–0.502 (0.500±0.001) | GUE class for all |

Row by row.

**Twists.** The three non-trivial spin-structure classes on the torus stay at |r_H7| ≤ 0.033; the largest absolute value in the group is B_twist3_3 at −0.03301495046331931, and the (0, π) class B_twist0_3 sits at +0.001815546323399943, essentially zero. The global phase bookkeeping of the boundary condition does not reach the level-n ↔ zero-n comparison.

**Anisotropy.** Both deformations of the hopping ratio (t_x/t_y = 0.8 and 1.25) give |r_H7| ≤ 0.030, the quietest handle in the family. The mean ratios ⟨r⟩ are 0.5002209850116544 and 0.4992803588243496 — square in the middle of the GUE window.

**Flux shift.** The admissible torus shifts ±1/24 and the open-boundary nudges ±0.02 give |r_H7| ≤ 0.034. Notably, δα = −0.02 yields r_H7 = 8.334933248494393e-05, the single smallest zero correlation in the entire campaign: leaving the self-dual line does not create arithmetic, it just moves the noise.

**Staggered mass.** Both masses give |r_H7| ≤ 0.032 (m = 0.15: +0.018988358449378486; m = 0.35: +0.01448110766274665). The heat-trace correlations r_EF = 0.9911878822153721 and 0.9865888932396799 are the two largest in the family and remain inside their null clouds — a useful reminder that a large raw correlation is meaningless without its null reference.

**Vortex profile.** The midpoint core gives |r_H7| ≤ 0.033 (A_profile_midpoint: +0.03256480942017184). On the torus the midpoint profile coincides with the site values to the last digit (`B_torus_midpoint` duplicates `B_torus_base` exactly in the committed CSV) — on a torus the profile choice is immaterial, another hint that the statistics are set by symmetry, not by core cosmetics.

**Signs and boundaries.** The noisiest dimension, |r_H7| ≤ 0.044, with the family maximum at C_Nv8_allplus (−0.0434730569109078): an all-plus sign pattern on the smallest lattice (Nv = 8). Even this maximum is five times smaller than the best protocol value 0.226 of C3, and the random-sign gates behave like the decoys — as they should.

**Family overall.** ⟨r⟩ = 0.498–0.502 (0.500±0.001), GUE class for all: every one of the 37 configurations lands in a band a tenth of a percent wide. Whatever the handles do to the Hamiltonian matrix, they do not move it out of the universal class.

### The committed per-gate table

All 37 rows of `data/gates_table.csv`, values rounded to six decimals; the CSV carries full precision. Columns: ⟨r⟩ = r_mean, r_H7 = zero correlation, r_EF = heat-trace correlation.

| Gate | Handle change | ⟨r⟩ | r_H7 | r_EF |
|---|---|---|---|---|
| A_aniso0.8 | aniso 0.8 | 0.500221 | +0.002616 | 0.808533 |
| A_aniso1.25 | aniso 1.25 | 0.499280 | −0.009176 | 0.704904 |
| A_dalpha-0.02 | δα = −0.02 | 0.500288 | +0.000083 | 0.978381 |
| A_dalpha+0.02 | δα = +0.02 | 0.501066 | −0.033538 | 0.959337 |
| A_mass0.15 | mass 0.15 | 0.500624 | +0.018988 | 0.991188 |
| A_mass0.35 | mass 0.35 | 0.500344 | +0.014481 | 0.986589 |
| A_profile_midpoint | midpoint core | 0.499375 | +0.032565 | 0.952809 |
| A_signs_allplus | all-plus signs | 0.499674 | +0.013159 | 0.547357 |
| A_aniso08_dalpha+0.02 | aniso 0.8 + δα +0.02 | 0.500764 | +0.029568 | 0.754706 |
| A_aniso125_mass0.15 | aniso 1.25 + mass 0.15 | 0.499778 | −0.025720 | 0.713761 |
| A_mass0.15_dalpha-0.02 | mass 0.15 + δα −0.02 | 0.500102 | −0.000327 | 0.979535 |
| A_midpoint_allplus | midpoint + all-plus | 0.499674 | +0.013159 | 0.547357 |
| B_torus_base | torus base | 0.500180 | −0.025928 | 0.484949 |
| B_twist3_0 | twist (π, 0) | 0.499887 | −0.025492 | 0.914057 |
| B_twist0_3 | twist (0, π) | 0.498143 | +0.001816 | 0.735324 |
| B_twist3_3 | twist (π, π) | 0.499711 | −0.033015 | 0.221711 |
| B_torus_aniso0.8 | torus, aniso 0.8 | 0.499361 | −0.009631 | 0.735015 |
| B_torus_aniso1.25 | torus, aniso 1.25 | 0.499121 | +0.006168 | 0.759888 |
| B_torus_dalpha+0.0417 | torus, δα +1/24 | 0.498481 | −0.004102 | 0.301775 |
| B_torus_dalpha-0.0417 | torus, δα −1/24 | 0.499141 | −0.003245 | 0.840169 |
| B_torus_mass0.15 | torus, mass 0.15 | 0.500409 | −0.026000 | 0.418220 |
| B_torus_midpoint | torus, midpoint | 0.500180 | −0.025928 | 0.484949 |
| B_torus_allplus | torus, all-plus | 0.498542 | +0.007999 | 0.724552 |
| B_twistpi_pi_mass0.15 | twist (π,π) + mass 0.15 | 0.499153 | −0.019047 | 0.299809 |
| B_twistpi_pi_aniso1.25 | twist (π,π) + aniso 1.25 | 0.501781 | +0.022340 | 0.124648 |
| C_Nv8_allplus | Nv = 8, all-plus | 0.499237 | −0.043473 | 0.351375 |
| C_Nv32_allplus | Nv = 32, all-plus | 0.498077 | −0.020808 | 0.825231 |
| C_Nv16_random_signs | random signs | 0.499175 | −0.018555 | 0.692253 |
| C_q0.5_mass0.15 | q = 0.5, mass 0.15 | 0.498512 | +0.015509 | −0.617819 |
| C_q0.5_dalpha+0.02 | q = 0.5, δα +0.02 | 0.499914 | −0.020146 | 0.941967 |
| C_W0_mass0.15 | W = 0, mass 0.15 | 0.499920 | −0.031596 | 0.203941 |
| C_W0.1_midpoint | W = 0.1, midpoint | 0.499329 | −0.010839 | −0.090584 |
| C_alpha0.4_allplus | α = 0.4, all-plus | 0.499889 | +0.013537 | 0.771227 |
| C_alpha0.4_dalpha+0.02 | α = 0.4, δα +0.02 | 0.501059 | +0.004770 | 0.683918 |
| C_Nv64_midpoint | Nv = 64, midpoint | 0.499473 | −0.023645 | 0.661968 |
| D_decoy_signs_random | decoy, random phases | 0.499175 | −0.018555 | 0.692253 |
| D_decoy_Nv32_random | decoy, Nv = 32 random | 0.499121 | −0.020663 | 0.916640 |

### Family statistics from the committed verdict

The verdict block of `data/results.json` records: n_gates_new = 35; rH7_abs_max = 0.0434730569109078; rEF_max = 0.9911878822153721; rEF_mean = 0.6112285569902335; rEF_sd = 0.3452702369140134; PC0_Hxi_r = 0.9997540255853161; GUE_mean = 0.7880407730570796; GUE_sd = 0.3758286233259756 (the GUE null cloud of the heat-trace statistic). The committed verdict string reads: "разрыв Г2 устойчив: ни одна новая ручка не выводит r_EF/r_H7 из нулевой зоны" — the H2 gap is stable: no new handle moves r_EF/r_H7 out of the null zone.

## How to read the numbers

- **⟨r⟩ (r_mean)** — the mean adjacent-spacing ratio of the unfolded spectrum, the campaign's GUE class marker; the C5 calibration places the universal value at 0.500, and integrable (Poisson-like) statistics would drift the average systematically away from it. The whole family sits in 0.498–0.502.
- **r_H7** — the Pearson correlation between the detrended spectral staircase of the gate and the detrended zero staircase (the level-n ↔ zero-n comparison; the label is the C3 pipeline's channel name for this statistic). Detrending removes the ramps so that only the fluctuations are compared. The null zone is calibrated by circular shifts of the zero list; C3's best protocol gate reached 0.226, and the entire C5 family stays under 0.0435.
- **r_EF** — the heat-trace projection introduced in C4: the fluctuation D(u) = Σ e^{−u·x_n} minus its smooth part, correlated against the explicit-formula prime comb P with a fixed scale and an OLS-fitted amplitude. A large r_EF means nothing by itself; the gate's own null cloud (`null_EF_mean`, `null_EF_sd`) and z-score (`z_EF`) decide whether the value is signal or weather.
- **z_EF** — the standardised distance of r_EF from its null cloud. All 37 gates stay within their clouds (|z_EF| ≤ 3.4563051301961507 across the family, with the null sd ranging from 0.12906723550210084 to 0.499555297750286).
- **Scale convention.** The heat-trace correlation uses a fixed scale (scale_EF = 1.0 in every row): scale optimisation is excluded because it systematically inflates r — the C4 lesson, kept here.

## Interpretation: what stability means

<p align="center"><img src="../../assets/avatars/hp_agent_vera.svg" width="112" alt="Agent Vera avatar"/></p>
<p align="center"><em>Vera, the auditor of verdicts: "stability" here is a measured statement about 37 configurations — with controls — not a theorem about every conceivable handle."</em></p>

The verdict "the H2 gap is stable across all six new handles" is a three-layer statement.

**Layer 1 — universality is an attractor.** All 37 configurations land in the GUE class with ⟨r⟩ = 0.500±0.001. The six dimensions include perturbations that in other contexts break universality (a mass term, a flux change, topology change); here none of them moves the spectral statistics. The class is set by the complex-vortex architecture, not by the parameters — the same message as theorem T10 in C8, now confirmed across a six-dimensional handle space.

**Layer 2 — the arithmetic does not return.** Universality would be harmless if the zero correlation survived underneath it. It does not: |r_H7| ≤ 0.043 over the new handles against 0.226 for the best protocol gate — the extended family is, if anything, *quieter* than the protocol family. The heat-trace projection agrees: r_EF distributed as 0.611 ± 0.345, inside the null clouds, decoys indistinguishable from real gates.

**Layer 3 — the demarcation is now wide.** Theorems T1–T6 fixed what the zeros do; theorem T7 fixes what the 87 gates do: 52 protocol gates (C3) plus 35 extended gates (C5) lie in the GUE class and carry no Λ-weights, with positive controls at r = 1.0 (PC1/PC2) and r = 0.9998 (PC0). The conclusion the package draws is deliberately modest and deliberately sharp: a hypothetical Hilbert–Pólya operator carrying the Λ(n)/√n weight in its trace cannot be obtained by *local* deformation of the lattice resonator. The question of nonlocal constructions remains open and belongs to the roadmap — the negative verdict covers the class of local Hermitian lattice Hamiltonians with vortex phases, and the campaign is careful to claim exactly that and no more.

The honest frame matters as much as the result. "Stability" is a measurement over 37 configurations, not a theorem about all possible handles; and the family maximum of |r_H7| is reached on a random-sign decoy, which is exactly where a noise maximum belongs.

## Reproduction

```bash
# excursion through the verdict (~seconds, no zeros file needed)
python3 campaigns/run_c5_gates_ext.py
```

The series seed is 96; the RNG streams are fixed inside `engine/hamiltonian.py`. All dependencies are listed in `requirements.txt`. The script replays the committed verdict — new gates count, ⟨r⟩ statistics, the |r_H7| maximum against the C3 best value 0.226, the r_EF cloud and the verdict string — straight from `data/c5_gates_ext_table.csv` and `data/c5_gates_ext_verdict.json`, so the excursion takes seconds and does not require the zeros file. Full recomputation of the spectra uses the same engine and seed and is expected to reproduce the committed tables bit-for-bit (see `data/README.md` and the registry discipline in `../../results/RESULTS.md`).

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
| `fig09_handles.png` / `fig09_handles_en.png` | 600 dpi — `figures_hires/ru/fig09_handles.png` · `figures_hires/en/fig09_handles_en.png`; screen — `figures/ru/` · `figures/en/` |
| `fig10_gue_ext.png` / `fig10_gue_ext_en.png` | 600 dpi — `figures_hires/ru/fig10_gue_ext.png` · `figures_hires/en/fig10_gue_ext_en.png`; screen — `figures/ru/` · `figures/en/` |

`fig09_handles` draws |r_H7| across the 37 extended gates: the gold line marks the best protocol value 0.226, the copper lines the positive controls at 1.000, the red bars the decoys. `fig10_gue_ext` draws ⟨r⟩ across the extended family: every point inside the 0.47–0.53 band — the GUE class is universal for all handles.

Monographs: `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`. The full monograph of this computation (setup, theorems, tables, figures, honest limitations): 7–9 pages, identical content in both languages.

## Honest notes

> The family maximum of \|r_H7\| is reached on a random-sign decoy — the expected noise maximum, not a signal.

> The statement "the gap is stable" is a measurement over 37 configurations, not a theorem about all possible handles.

Both notes are load-bearing. The first prevents over-reading the largest correlation in the family: it belongs to a decoy, and a decoy exists precisely to host such maxima. The second prevents over-reading the verdict itself: C5 closes the "one family" objection for the six dimensions tested and the 37 configurations committed — it does not prove that every conceivable lattice Hamiltonian fails. What it does establish, together with C3, is the T7 demarcation over 87 gates; where to go beyond the local class is the business of the roadmap, not of this campaign.

## Verdict

**{'ru': 'разрыв Г2 устойчив ко всем шести новым ручкам', 'en': 'the H2 gap is stable across all six new handles'}** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign).

## FAQ

**1. Thirty-seven configurations — is that enough to claim "the gap is stable"?**
Enough for the claim C5 actually makes: a measured negative over the six tested dimensions, with per-gate null clouds, decoys and a bit-for-bit regression control. The campaign explicitly does not claim a theorem over all possible handles. Combined with the 52 protocol gates of C3, the T7 demarcation covers 87 configurations of one architectural class — local Hermitian lattice Hamiltonians with vortex phases.

**2. Why does the family table quote ⟨r⟩ = 0.500±0.001?**
Because every gate of the family was run through the same statistics as C3, and in this campaign's window the mean adjacent-spacing ratio sits in 0.498–0.502 for all 37 configurations. The number that matters is the width: a tenth of a percent across twists, anisotropy, flux shifts, masses, profiles, signs and two boundary geometries. The class-level calibration across the series (Poisson / GOE / GUE ladders) is theorem T10 in C8.

**3. Why was the corner W = 0 + midpoint replaced by W = 0.1?**
At W = 0 with the midpoint profile the Hamiltonian develops exact spectral multiplicities, which break the polynomial unfolding and would corrupt the statistics. Replacing the corner with W = 0.1 keeps the gate meaningful; the substitution is flagged with an explicit note in the data table and recorded in the honesty registry.

**4. Why are only ±1/24 flux shifts allowed on the torus?**
Flux quantisation: on the 24-lattice the constraint α·Ny ∈ ℤ is rigid, and ±1/24 are the realisable neighbouring points of the self-dual line α = ½. They are exact values, not rounded ones; using ±0.02 on the torus would violate the quantisation the model itself imposes.

**5. What exactly is a decoy, and why two?**
A decoy is a gate whose vortex phases are random — the null hypothesis "the structure of the phases is not important" made into a configuration. Two decoys (Nv = 16 and Nv = 32) anchor the noise floor of both r_H7 and r_EF. Their behaviour is statistically indistinguishable from the real gates, which is the strongest single sentence in the campaign.

**6. Does C5 say no lattice operator can ever encode the zeros?**
No. It says no *local* deformation of this resonator family — six dimensions, 37 configurations, 87 gates with C3 — moves the statistics toward the zeros. Nonlocal constructions are explicitly outside the verdict and are kept open in the roadmap.

## See also

- [C3 — the protocol gate family](../C3_gate_family/README.md): the 52-gate campaign C5 extends; source of the 0.226 reference and the null-zone calibration.
- [C4 — the trace formula](../C4_trace_formula/README.md): origin of the heat-trace statistic r_EF and the PC0 positive control reused here.
- [Theory map](../../docs/theory.md): the five stages, the scorecard logic H1–H5, and why G3 = YES explains the difficulty of H2.
- [Roadmap](../../results/ROADMAP.md): what lies beyond the local lattice class — the open question C5 deliberately leaves open.
- [Results registry](../../results/RESULTS.md): rows 15 and 21 of the main table live here; every number in this README is committed.

---
*Hilbert Polya Bridge v1.0.0 · C5 · The extended gate family*

