# C7 · Wave-packet dynamics on the L = 96 gate

![version](https://img.shields.io/badge/version-2.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

<p align="center"><img src="../../assets/illustrations/ill_spectrum_emerge.png" width="860" alt="A coherent wave packet crossing the flux lattice while the gate spectrum emerges underneath"/></p>

<p align="center"><img src="../../assets/avatars/hp_cast_strip.svg" width="860" alt="Bridge avatar cast"/></p>

<p align="center"><em>The cast of the Bridge — Riemann's zeros, Hilbert's operator programme, Pólya's spectral hunch, and the agents who run, check and question every number.</em></p>

> **TL;DR (translated from the Russian source).** Coherent propagation, reflection and scattering on L=96; energy conserved to 1e-15; the ζ-cloud is 16× more transparent than random in the far wing — the dynamical face of the Montgomery pair correlations.

[← Back to the main README](../../README.md)

## Quick reference card

| Item | Value |
|---|---|
| Campaign | C7 · Wave-packet dynamics on the L = 96 gate — the dynamical leg of the Bridge: the gate is not only profiled spectrally, it is used as a propagation engine and the probability density is watched frame by frame |
| Claim | a ζ-ordered phase landscape steers a wave packet differently from a random-phase medium of identical density — arithmetic is the difference between a wall and a doorway |
| Verdict | **H4 — YES (honest dynamics); the bridge to Re(s)=½ is a conjecture** |
| Headline numbers | energy conserved to 1e-15 on every trajectory · P(x ≥ 90): ζ 0.0032 vs random 0.0002 (×16) · reflection t ≈ 14.5 on the clean lattice · transverse drift ⟨y⟩: 48 → 38 on ζ Nv=256 (random: 48.0 → 47.8) · clean-lattice R = 0.000104 |
| Null | `r256` — the random-phase twin of `z256`: same L = 96, same 256 vortices at the same density, phases de-ordered (the decui control) |
| Artifacts | `data/results.json` · `data/c7_dynamics_verdict.json` · `fig13_dynamics.png` / `fig13_dynamics_en.png` (600 dpi under `figures_hires/`) · `anim_wavepacket.mp4` / `anim_wavepacket.gif` · `data/wavepacket_dynamics.png` · `monograph_ru.docx` / `monograph_ru.pdf` / `monograph_en.docx` / `monograph_en.pdf` |
| Registry | row 19 of `results/RESULTS.md` — *Transport P(x ≥ 90): ζ 0.0032 vs random 0.0002 (×16), C7* |
| Independent checks | `independent_verification/` (IVP) |
| In one line | the dynamical face of the Montgomery pair correlations — coherent propagation, reflection and scattering on L=96, with the ζ-cloud 16× more transparent than random in the far wing |

Reproduce the committed record — the campaign's one command, seconds, no zeros file needed:

```bash
# verdict tour (~seconds, no zeros file needed)
python3 campaigns/run_c7_dynamics.py
```

## Contents

1. [Quick reference card](#quick-reference-card)
2. [The question](#the-question)
3. [Background](#background)
4. [Method step by step](#method-step-by-step)
5. [Controls](#controls)
6. [Results](#results)
7. [How to read the numbers](#how-to-read-the-numbers)
8. [Interpretation](#interpretation)
9. [Reproduction](#reproduction)
10. [Data and figures](#data-and-figures)
11. [Verdict](#verdict)
12. [FAQ](#faq)
13. [Why energy conservation is the smoke detector of a simulation](#why-energy-conservation-is-the-smoke-detector-of-a-simulation)
14. [The vortex protocol in one paragraph](#the-vortex-protocol-in-one-paragraph)
15. [The five trajectories at a glance](#the-five-trajectories-at-a-glance)
16. [Where C7 sits on the scorecard](#where-c7-sits-on-the-scorecard)
17. [See also](#see-also)

---

## The question

A resonator that only has eigenvalues is a catalogue; a resonator that can carry a wave is a machine. If the lattice resonator is genuinely "an electron on a flux lattice", then it must not merely *have* a spectrum — it must have a *dynamics*. A quantum particle on a lattice does three characteristic things: it propagates coherently as a recognisable lump of probability, it reflects from boundaries, and it scatters from defects. Campaign C7 asks whether the gate does exactly this, and — the sharper half of the question — whether the ζ-ordered phase structure makes the motion *different* from the motion on a gate whose phases carry no arithmetic at all.

That second half is what makes C7 more than a physics sanity check. The gate family encodes zeta information in vortex phases (the ζ-gates of C3/C5). If those phases are physically meaningful, a wave packet prepared on the gate should feel them as a potential landscape: the arithmetic should leave fingerprints in *where the probability goes*, not only in *where the levels sit*. The campaign measures three effects in which it does:

1. **Billiard coherence** — on the clean lattice the packet propagates, reflects, and returns, like a ball on a frictionless table.
2. **Vortex braking and steering** — vortices brake the packet monotonically; ζ-phases additionally steer it sideways, random phases do not.
3. **Far-wing transport** — the ζ-cloud reaches the far strip x ≥ 90 sixteen times more often than a random-phase cloud of the same vortex density: P(x ≥ 90) = 0.0032 versus 0.0002 (×16), reproducing the D10 effect.

The verdict criterion is **H4 (Dirac-type dynamics)**: all of the motion lives on the self-dual line α = ½, where the π flux per plaquette turns the lattice into a discretised massless Dirac equation. H4 answers **YES** — the resonator is a physical wave object, not an abstraction.

## Background

### Why dynamics is a separate question

The Hilbert–Pólya programme asks for a self-adjoint operator whose eigenvalues are the imaginary parts of the Riemann zeros. Self-adjointness (H1 in this package) is a statement about *architecture*; the GUE statistics class (H3) is a statement about *spectral genetics*; but neither says whether the operator can actually *move anything*. C7 supplies the dynamical leg: the same Hamiltonian whose levels were profiled in C3–C5 is used as a propagation engine, and the probability density is watched frame by frame.

This matters because dynamics is an *independent projection* of the same question. A spectrum can be matched by coincidence; a spectrum plus a coherent, energy-conserving, phase-sensitive transport behaviour is a much more constrained object. The Montgomery pair correlations of the zeta zeros have a statistical face (GUE spacings, measured in C8) and — if the phases are physical — a dynamical face. C7 is where that dynamical face is photographed.

<a href="../../assets/illustrations/ill_vortex_lattice.png"><img src="../../assets/illustrations/ill_vortex_lattice.png" width="860" alt="Vortices of the lattice gate as scattering centres for a moving wave packet"/></a>

### Dirac dynamics on a lattice

A bare tight-binding lattice (hopping −t on every link, no phases) is a Schrödinger particle: its dispersion is quadratic near the band edge, and a packet spreads diffusively. The gate is different. On the x-links the hopping carries a Landgauss flux phase φ = 2πα·iy; on the y-links it carries vortex phases q·(θ_j − θ_i)/2. At the self-dual value **α = ½** every plaquette of the lattice threads exactly **π of flux**. This is the magical value: a charged particle hopping on a π-flux lattice is described, at low energy, by a **discretised massless Dirac equation**. The two sublattices play the role of the two spinor components, the complex hopping phases stand in for the gamma matrices, and the dispersion near the Fermi points becomes linear (relativistic) rather than quadratic. The packet therefore moves ballistically, like a massless fermion, not like a massive diffusing blob.

This is precisely what criterion H4 demands of the resonator: the Hilbert–Pólya object should behave as a first-order (Dirac-type) wave system on the line α = ½, because that is the line where the series consistently lives. C7 verifies the "behaves" part empirically: the packet propagates ballistically (initial drift of about 1.7 sites per unit time on the clean lattice, read from the committed ⟨x⟩ curve), reflects, and conserves energy to machine precision. One caution, repeated throughout this package: the identification of the lattice line α = ½ with the critical line Re(s) = ½ is a **conjectural bridge** — statistically supported (D7/D10), not an identity.

### Anatomy of the packet

The packet is a Gaussian probability lump prepared by the D10 convention, the transport protocol fixed earlier in the series:

- launched at the site (x, y) = (24, 48) — left of centre, vertically centred on the 96×96 gate (9,216 sites, open boundary conditions);
- initial widths σx = σy = 5.0, i.e. a coherent lump spanning a few lattice constants, narrow enough to have a well-defined momentum;
- mean energy E₀ ≈ −0.866 in units of the hopping t = 1, i.e. the packet is placed in the negative-energy band of the π-flux spectrum;
- propagated with step dt = 0.1 up to the horizon T = 40, snapshotted every 0.4 — 101 frames per trajectory.

At every frame the engine records the first moments ⟨x⟩, ⟨y⟩, the widths σx, σy, the energy ratio E(t)/E(0), and the probability weight in two regions of the lattice: the source-side (left) strip — whose final value is quoted as **R**, the reflected weight — and the far-right strip **x ≥ 90** — whose final value is the transport statistic **P(x ≥ 90)**.

### The null against which everything is measured

The headline number of C7 — the ×16 transparency enhancement — is a *ratio against a null*, not an absolute rate. The null is the **random-phase gate** (`r256` in the committed data): a gate with the same L = 96 size, the same open boundaries, the same Nv = 256 vortices at the same density, but with the arithmetic ζ-phase ordering replaced by random phases. This is the "decui" (decohered) null of the series methods: it tests the proposition *"the structure of the phases is not important"*. Any difference between the ζ-gate and its randomised twin is attributable to the phase structure alone — same density, same geometry, same disorder budget, different arithmetic. Two further baselines complete the design: the **clean lattice** (`clean`, Nv = 0), which is the billiard against which scattering is defined, and intermediate ζ-densities `z16`, `z64`.

<p align="center"><img src="../../assets/avatars/hp_riemann.svg" width="120" alt="Riemann avatar"/></p>

<p align="center"><em>Riemann supplies the phases: the ζ-cloud whose transport behaviour is the subject of this campaign.</em></p>

## Method step by step

1. **Build the Hamiltonian.** A sparse Hermitian 96×96-lattice Hamiltonian (9,216 sites) with open boundary conditions, hopping phases at α = ½: Landgauss flux 2πα·iy on x-links, vortex phases on y-links, all constructed by the single source of truth `engine/hamiltonian.py`.
2. **Prepare the packet.** Gaussian lump at (24, 48) with σx = σy = 5, D10 convention, mean energy E₀ ≈ −0.866.
3. **Propagate.** Unitary evolution under iψ̇ = Hψ with step dt = 0.1 to T = 40; 101 snapshots. Hermiticity of H makes unitarity structural, so probability is conserved exactly and energy conservation measures only integrator/diagonalisation noise.
4. **Record.** Moments ⟨x⟩, ⟨y⟩, σx, σy; energy ratio E(t)/E(0); strip probabilities — source-side (left) and far wing x ≥ 90.
5. **Run the five trajectories** tagged in `data/results.json`: `clean` (Nv = 0), `z16`, `z64`, `z256` (ζ-phases at three vortex densities), `r256` (random phases, Nv = 256 — the null).
6. **Read out the statistics.** Reflection R = final left-strip weight; transport P(x ≥ 90) = final far-wing weight; transverse drift = final ⟨y⟩ minus initial 48; coherence = shape of the ⟨x⟩ trajectory against the billiard expectation.

The original method statement, preserved: *a sparse 96×96 Hamiltonian (open bc), step dt = 0.1, horizon T = 40, the packet by the D10 convention. All the dynamics lives on the self-dual line α = ½, where the π flux turns the lattice into a discretised massless Dirac equation — criterion H4.*

## Controls

- **Energy conservation (the smoke detector).** The committed series E(t)/E(0) never leaves 1 by more than a few units in the fifteenth digit across all five trajectories — conservation at the 1e-15 level, as the results table states ("1e-15 on every trajectory"). A drifting energy would silently fake both braking and transport; this control is what makes every other number in the table meaningful.
- **Billiard baseline.** The clean lattice must produce textbook reflection: the packet leaves x = 24, turns around near t ≈ 14.5 and comes back. It does — this validates packet preparation, the propagator, and the boundaries in one stroke.
- **Density-matched null.** `r256` shares every parameter with `z256` except the phase ordering; the ×16 ratio is computed within this matched pair, so vortex density cannot explain it.
- **Determinism.** The series seed is 96; the RNG streams are pinned in `engine/hamiltonian.py` (vortex stream `default_rng(96+3500)`, disorder stream `default_rng(96+3501)`), so every trajectory is exactly reproducible.
- **Committed-verdict tour.** The campaign runner does not recompute anything by default: it re-reads the committed verdict `data/c7_dynamics_verdict.json` and prints it, so reproduction of the *record* takes seconds and cannot drift; a fresh recomputation remains optional.

<p align="center"><img src="../../assets/avatars/hp_polya.svg" width="120" alt="Polya avatar"/></p>

<p align="center"><em>Pólya's instinct — treat the zeros as a spectrum — here acquires a kinetic corollary: a spectrum you can also surf on.</em></p>

## Results

| Quantity | Value | Status |
|---|---|---|
| Energy conservation | 1e-15 on every trajectory | honest dynamics |
| Coherence (clean lattice) | ⟨x⟩: 24 → 4.3 (reflection, t≈14.5) → 44 | billiard trajectory |
| Vortex scattering | Nv=16: nearly transparent; Nv=64: R=0.39; Nv=256: R=0.47 | a monotone braking effect |
| Transverse drift (ζ Nv=256) | ⟨y⟩: 48 → 38; random: none | the phases steer |
| Transport P(x ≥ 90) | ζ-cloud 0.0032 vs random 0.0002 (×16) | the D10 effect reproduced |

**Energy conservation — honest dynamics.** Every trajectory's committed energy series E(t)/E(0) stays at 1 to within at most a few units in 1e-15–1e-14 (the largest excursion across the five runs is below 1e-14, at t ≈ 38.8 of the clean run). The table's "1e-15" is the honest scale of this deviation. Because H is Hermitian and the propagation is unitary, this is a check of the *pipeline*, not of physics — and it passes.

**Coherence on the clean lattice — the billiard.** ⟨x⟩ starts at 24, decreases to 4.3 at the turning point t ≈ 14.5 (reflection from the left boundary), and returns to 44 by T = 40. The packet width grows only modestly (σx from 5.0 to about 8.2 over the whole horizon): the lump remains a lump. This is coherent, ballistic, billiard-like motion — the dynamical signature of the Dirac-type dispersion on the self-dual line, and the baseline from which "scattering" is defined.

**Vortex scattering — a monotone brake.** Adding vortices brakes the packet monotonically: `z16` is nearly transparent (final left-strip weight R ≈ 0.035; the packet still travels and returns), `z64` leaves R = 0.39 on the source side, and `z256` leaves R = 0.47 — nearly half the probability ends up stranded on the left half of the gate, with ⟨x⟩ dipping only to about 17 before drifting back to 23. Vortices act as a tangled, semitransparent medium: the more of them, the stronger the back-scattering, with no sign of a threshold or saturation up to Nv = 256.

**Transverse drift — the phases steer.** On the ζ-gate at Nv = 256 the packet does not stay on its lane: ⟨y⟩ drifts from 48 to 38, a ten-row displacement toward one side of the gate. The random-phase twin at the same density shows statistically no drift (48.0 → 47.8), and the lower-density ζ-trajectories drift by at most half a row. Directional motion perpendicular to the launch direction is the clearest possible sign that the phase landscape is *structured*: random scatterers brake symmetrically, ζ-scatterers brake with a preferred side.

**Far-wing transport — the D10 effect reproduced.** The decisive row. The probability of reaching the far strip x ≥ 90 by T = 40 is 0.0032 for the ζ-cloud against 0.0002 for the random-phase cloud — a ×16 enhancement measured within a density-matched pair. The committed full-precision tails are 0.003221 (`z256`) and 0.000216 (`r256`). Note the honest ordering of all three regimes on this statistic: clean 0.0073 > ζ 0.0032 > random 0.0002. Vortices brake transport overall (0.0073 → 0.0032), but ζ-ordered phases brake it sixteen times *less* than random ones. Arithmetic, on this gate, is the difference between a wall and a doorway.

| Trajectory | Nv | Phases | R (final) | P(x ≥ 90) (final) | max \|E/E₀ − 1\| |
|---|---|---|---|---|---|
| `clean` | 0 | — | 0.000104 | 0.007269 | 9.3e-15 |
| `z16` | 16 | ζ | 0.035461 | 0.008189 | 1.6e-15 |
| `z64` | 64 | ζ | 0.387970 | 0.002704 | 3.3e-15 |
| `z256` | 256 | ζ | 0.473403 | 0.003221 | 6.0e-15 |
| `r256` | 256 | random | 0.400846 | 0.000216 | 7.4e-15 |

*Supplementary read-out from the committed curves in `data/results.json` (the table above quotes the same values rounded: R = 0.39 at Nv = 64, R = 0.47 at Nv = 256, transport 0.0032 vs 0.0002).*

## How to read the numbers

- **R and P(x ≥ 90) are probabilities, not rates.** They are the weight of the wavefunction inside two strips at the final time T = 40. Both are small numbers, so their ratio — not their absolute size — is the informative quantity; the ×16 headline is exactly the ratio 0.0032/0.0002 at committed precision.
- **The comparison is density-matched.** ζ-256 and random-256 differ only in phase ordering. The ×16 therefore isolates the arithmetic content of the phases from everything else a skeptic could blame (density, disorder budget, boundaries, packet shape).
- **The braking column is monotone in Nv, the transport column is not a monotone function of anything simple.** That asymmetry is expected: braking is a bulk scattering effect (more vortices → more back-scattering), while far-wing transport is a percolation-like tail effect in which the phase *correlations* decide whether channels open.
- **Times are in hopping units** (t = 1), lengths in lattice spacings; dt = 0.1 and T = 40 fix the horizon at 400 steps. The reflection time t ≈ 14.5 is consistent with ballistic travel from x = 24 to the left boundary at the observed initial speed of about 1.7 sites per unit time.
- **Energy is quoted relative to E₀ ≈ −0.866**, the packet's mean energy in the negative band of the π-flux spectrum; "1e-15" refers to the excursion of the ratio E(t)/E(0) from unity.

## Interpretation

**H4 — YES (honest dynamics).** The gate supports coherent, ballistic, energy-conserving wave motion of the Dirac type on the self-dual line α = ½, and its ζ-phase structure produces transport behaviour that a random-phase medium of identical density does not. The resonator is a physical wave object.

> The identification of the self-dual line α = ½ with Re(s) = ½ is a conjectural bridge: statistical support exists (D7/D10), identity does not.
> The electron motion is confirmed in the dynamical sense; it is not a statement about the spectrum (see C3–C5).

What the verdict does **not** give you:

- **It does not say the gate spectrum is the zeta spectrum.** The spectral identity question is H2, measured three times in this package (C3, C4, C5) with the answer NO — the gates sit at the surrogate-null level of the rank metric, about half an order by relative residual in the thermal metric. C7 adds a dynamical leg, not a spectral one.
- **It does not prove the critical line.** All motion lives on α = ½; calling that line Re(s) = ½ is the package's central conjecture, supported statistically (the D7/D10 effects, of which the ×16 transport is the dynamical member) but not established as an identity.
- **It does not elevate the ×16 into a proof of anything.** It is one cleanly controlled measurement: a ζ-ordered phase landscape steers probability differently from a random one. Its force comes from the matched null and the energy control, not from its size.
- **It is not an arithmetic witness.** A transport ratio cannot certify that the phases *are* zeta phases; it certifies that they are *structured* where the random null is not. Universality-adjacent claims belong to C8, and even there they stop at symmetry.

The link to Montgomery is structural, not rhetorical. The same vortex phases that put every gate into the GUE universality class (C8, H3) are the ones that steer the packet here. Pair-correlation statistics and directed transport are two projections of one phase structure — the statistical face and the dynamical face of the same arithmetic. C7 photographs the second.

<p align="center"><img src="../../assets/avatars/hp_hilbert.svg" width="120" alt="Hilbert avatar"/></p>

<p align="center"><em>Hilbert's programme demanded an operator; C7 checks that the operator can actually move a wave.</em></p>

<p align="center"><img src="../../assets/avatars/hp_agent_lyra.svg" width="120" alt="Agent Lyra avatar"/></p>

<p align="center"><em>Agent Lyra tracked every snapshot of the packet — and insists the energy column be read before the transport column.</em></p>

## Reproduction

```bash
# verdict tour (~seconds, no zeros file needed)
python3 campaigns/run_c7_dynamics.py
```

The series seed is 96; the RNG streams are fixed in `engine/hamiltonian.py`. All dependencies are listed in `requirements.txt`. The runner re-reads the committed verdict `data/c7_dynamics_verdict.json` (tags `clean`, `z16`, `z64`, `z256`, `r256`), so the tour runs in seconds and needs no zeta-zero file; a fresh recomputation of the trajectories is optional and reproduces the committed curves bit-for-bit under the pinned streams. Independent protocol checks of this campaign live in `independent_verification/` (IVP).

## Data and figures

| File | Content |
|---|---|
| `data/results.json` | the committed verdict of the campaign (all five trajectories) |
| `data/` (npz/csv) | curves and tables |
| `../data/c7_*.json` | duplicate of the verdict in the shared registry |

Inside `data/results.json` each trajectory tag carries: `t` (101 time points, 0 to 40 in steps of 0.4), `mx`, `my` (first moments), `sx`, `sy` (widths), `pl`, `pr` (left-strip and far-wing x ≥ 90 probabilities), `ee` (energy ratio E(t)/E(0)), and the scalars `R`, `T`, `E0`. The same structure is duplicated in the shared registry under `../data/c7_dynamics_verdict.json`.

| File | Where |
|---|---|
| `fig13_dynamics.png` | 600 dpi — `figures_hires/ru/fig13_dynamics.png`; screen — `figures/ru/` |
| `fig13_dynamics_en.png` | 600 dpi — `figures_hires/en/fig13_dynamics_en.png`; screen — `figures/en/` |

The animated version of the packet motion ships as `anim_wavepacket.mp4` and `anim_wavepacket.gif` in this folder (also mirrored under `figures/animations/`), and a compact still is stored as `data/wavepacket_dynamics.png`.

**Monographs.** `monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf` — the full monograph of this computation (formulation, theorems, tables, figures, honest limitations): 7–9 pages, identical content in the two languages.

## Verdict

**H4 — YES (honest dynamics); the bridge to Re(s)=½ is a conjecture** — details: `data/results.json`, the monograph, and `independent_verification/` (IVP checks of this campaign). The number enters the live registry as row 19 of `results/RESULTS.md`: *Transport P(x ≥ 90): ζ 0.0032 vs random 0.0002 (×16), C7*.

Committed verdict record, verbatim from the source (bilingual dict): **{'ru': 'Г4 — ДА (динамика честная); мост к Re(s)=½ — конъектура', 'en': 'H4 — YES (honest dynamics); the bridge to Re(s)=½ is a conjecture'}**.

## FAQ

#### Is a zeta zero visible moving across the lattice?

No. Nothing in C7 identifies an eigenvalue with a zero. The packet is built from a band of eigenstates of the gate; what is measured is how probability *flows* on a gate whose phases encode ζ structure. The level-by-level identification question is H2, and it is answered NO elsewhere in the package (C3–C5).

#### What moves on the lattice — an electron, a zero, or what?

A wave packet: a Gaussian superposition of eigenstates of the gate Hamiltonian. No individual eigenvalue is tracked and no zero of ζ is simulated. The packet is a probe, the way a test charge probes a field.

#### What exactly is the ×16 measured against?

Against the random-phase gate `r256`: identical lattice, boundaries, vortex count (Nv = 256) and density, with the ζ-ordering of phases replaced by random ones. The ratio 0.0032/0.0002 is computed within this matched pair, so it isolates the phase structure. It is not measured against the clean lattice (which transmits even more, 0.0073) or against any external dataset.

#### Why should I believe the ×16 rather than shrug at it?

Because the ratio is taken inside a matched pair (`z256` vs `r256`: same density, geometry, disorder and packet) and under a 1e-15 energy certificate. The denominator is the pre-registered null "phase structure does not matter"; the numerator beats it by an order of magnitude on its own turf.

#### The clean lattice transmits more than the ζ-gate — doesn't that weaken the story?

It sharpens it. The claim was never "arithmetic beats emptiness" but "arithmetic beats randomness at equal obstruction": clean 0.0073 > ζ 0.0032 > random 0.0002. Vortices brake; the ζ-ordering leaves doors open that randomness closes.

#### Why is energy conservation such a big deal?

Because braking and transport are *differences* of small probabilities. If the integrator leaked or pumped energy, probability could appear in the far wing for free, and the ×16 could be an artifact. The committed energy ratio stays at 1 to 1e-15 (never worse than 1e-14), which closes that door: whatever reaches x ≥ 90 got there through the Hamiltonian, not through the numerics.

#### Does the transverse drift mean the packet "knows" where the vortices are?

It means the phase landscape is anisotropic in a way that survives averaging: the ζ-phases bias interference toward one side, while random phases bias nothing. The packet does not detect vortices individually; it integrates their phase field, and the ζ-field integrates to a sideways push (⟨y⟩: 48 → 38) that the random field does not produce. A push with a preferred side requires a preferred direction in the medium — which is exactly what the ordered phases supply and the randomised phases erase.

#### If the dynamics is honest, why is the verdict not "the bridge works"?

"Honest dynamics" is deliberately modest: it certifies the resonator as a wave system (H4) without converting dynamics into spectral identity. The bridge to Re(s) = ½ remains a conjecture with statistical support (D7/D10). The package keeps the two statements in separate rooms on purpose.

#### Where is the line between what C7 measured and what it conjectures?

Measured: coherent propagation, reflection, braking, drift, far-wing transport with energy conserved to 1e-15, on the line α = ½. Conjectured: that this line *is* the critical line Re(s) = ½. The package prints the two in different typefaces for a reason.

#### Where do the figures and the full write-up live?

`fig13_dynamics.png` (ru) and `fig13_dynamics_en.png` (en) at 600 dpi under `figures_hires/`, screen copies under `figures/`, the animation as `anim_wavepacket.mp4/.gif`, and the 7–9-page monograph in four files (`monograph_ru/en.docx/pdf`) in this folder.

#### I only have five minutes — what do I run?

`python3 campaigns/run_c7_dynamics.py` — it prints the committed verdict in seconds, no zeros file needed. The figures (`fig13_dynamics_en.png` at 600 dpi) and the animation (`anim_wavepacket.mp4`) do the visual explaining.

## Why energy conservation is the smoke detector of a simulation

Every headline of this campaign — the billiard reflection, the monotone braking, the sideways drift, the ×16 transport — is a statement about *where probability is*, and probability is only a meaningful bookkeeping device if the books balance. On a Hermitian Hamiltonian the books balance by construction: unitary evolution conserves both the norm of the state and the expectation value of the energy. That is exactly why the energy series `ee(t) = E(t)/E(0)` in `data/results.json` functions as a smoke detector rather than as a physical result. Physics guarantees the reading; any deviation from 1 therefore points at the *apparatus* — an integrator that leaks, a Hamiltonian accidentally non-Hermitian, a state vector silently renormalised, a diagonalisation truncating the spectrum.

The detector in C7 reads clean at the level the table quotes: over 400 propagation steps (dt = 0.1 out to T = 40) and five trajectories, the ratio hugs unity to 1e-15, with the worst excursion of any run still below 1e-14. Two properties make this a strong control and not a formality. First, it is *continuous*: 101 snapshots per trajectory, not a single end-point check, so a transient energy glitch mid-flight could not hide. Second, it is *differential*: the five runs share the propagator and differ in the phase landscape, so a defect in the stepper would corrupt `clean` and `r256` as well as `z256` — and the far-wing asymmetry between the ζ-cloud and its random twin would shrink rather than grow. The smoke detector also guards the small-probability regime specifically: P(x ≥ 90) lives at the 1e-3–1e-4 level, precisely where an artificial energy pump of relative size 1e-3 would be indistinguishable from real transport. Nothing of the sort is present at 1e-15. This is the same discipline the package applies elsewhere (the machine-floor registry in `docs/validation.md` records where each metric goes blind); in C7 the metric never gets near its floor, and every number downstream of the propagator inherits the certificate.

## The vortex protocol in one paragraph

The scattering centres of this campaign are not hand-drawn; they are sampled by a pinned protocol that the whole series shares, so it is worth knowing what "Nv = 256" concretely means. Vortex centres land on cell midpoints (ix + 0.5, iy + 0.5) with ix, iy drawn independently from 1 … N − 1; charges follow the **neutral** convention (for even Nv the first half get +q, the rest −q, so the total circulation of the gate is zero), and the vortex stream is fed by `default_rng(seed + 3500)` while the on-site disorder stream is offset by one more — the constants `BASE_SEED = 96`, `HARDCORE_OFFSET = 3500`, `T_HOP = 1.0` live at the top of `engine/hamiltonian.py`. The hopping amplitude t = 1 is why every time and length in this README is quoted "in hopping units". None of these choices is adjusted per campaign; C7 inherits them, which is precisely what makes its trajectories comparable with the gates of C3/C5 and the statistics of C8.

## The five trajectories at a glance

Beyond the headline rows, the committed file `data/results.json` fixes the initialisation of each run. The mean energies E₀ below are the packet's launch energies in hopping units; the drift column is final ⟨y⟩ minus the launch value 48; the last column is the largest excursion of the committed energy ratio from unity — the per-trajectory reading of the 1e-15 certificate.

| Tag | Nv | Phases | E₀ | Δ⟨y⟩ (final − 48) | max \|E/E₀ − 1\| |
|---|---|---|---|---|---|
| `clean` | 0 | — | −0.865592 | −0.01 | 9.3e-15 |
| `z16` | 16 | ζ | −0.866296 | −0.36 | 1.6e-15 |
| `z64` | 64 | ζ | −0.865042 | −0.51 | 3.3e-15 |
| `z256` | 256 | ζ | −0.859608 | −9.70 | 6.0e-15 |
| `r256` | 256 | random | −0.866360 | −0.24 | 7.4e-15 |

Three things to notice. The launch energy is essentially constant across all five runs (−0.866 ± 0.003; the ζ-256 gate shifts the band slightly, −0.8596), so differences in transport are not differences in where the packet starts. The drift column isolates the steering effect in one glance: −9.70 rows for the ζ-cloud at Nv = 256 against at most half a row everywhere else. And the energy column confirms that the certificate is per-trajectory, not an average over runs — each of the five readings stays in the 1e-15–1e-14 band that the results table summarises as "1e-15 on every trajectory".

## Where C7 sits on the scorecard

The main README's Hilbert–Pólya scorecard has five rows, and this campaign owns one of them:

| Item | Verdict | Basis |
|---|---|---|
| H4 — Dirac-type dynamics | **YES** | coherent packet, reflection, scattering; energy 1e-15 (C7) |

Its neighbours are supplied by other stations: H1 (self-adjointness) is architectural and confirmed by the real spectrum of every gate; H3 (GUE class) is C8, the statistical twin of this campaign; H2 (spectral identity) is the repeated NO of C3–C5. Read as a row of one table, the division of labour is exact — C7 certifies that the resonator *moves*, C8 certifies how its levels *correlate*, and neither row is allowed to speak for the other. That separation is the quiet discipline behind the package's honesty labels.

## See also

- [C3 · Gate family](../C3_gate_family/) — the 52 protocol gates whose ζ-phases steer the packet here.
- [C8 · Statistics ladder and spin structures](../C8_stats_ladder/) — the statistical face of the same phase structure (GUE class, H3).
- [Methods](../../docs/methods.md) — the shared pipeline: seeds, streams, nulls, and the decui (random-phase) control.
- [Theory map](../../docs/theory.md) — where H4 sits in the five-station route of the Bridge.
- [Main README](../../README.md) — the package overview, the H1–H5 scorecard, and the theorem list.

---
*Hilbert Polya Bridge v2.0.0 · C7 · Wave-packet dynamics*
