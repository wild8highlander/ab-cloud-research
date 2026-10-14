# -*- coding: utf-8 -*-
"""content/en_part5.py — campaigns V16–V18 (English series, v1.1.0)."""
from content.common import _meta
from content.en_part1 import AUTHOR, AFFIL, SERIES, DATE

# ═══════════════════════ V16 ══════════════════════════════════════════════
V16 = {'meta': _meta(
    'V16. Full Hamiltonian × Full Algebraic Function',
    'Coupling the lattice to the ζ zeros via the θ-phase of Z_id over '
    'the entire handle space — no reduction to the GUE class', 'V16',
    AUTHOR, AFFIL, SERIES, DATE), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
   'The whole previous series V1–V15 measured the lattice '
   'statistically: ⟨r⟩, D_KS against the GUE surmise, the form factor. '
   'The user brief fixes a change of emphasis: do not fixate on the '
   'uniqueness of GUE; instead, build the connection directly through '
   'the FULL algebraic function of the critical line — the assembly '
   'Z_id(t) = e^{iθ(t)}ζ(½+it) out of the Γ-ladder, where θ(t) = '
   'Im ln Γ(¼+it/2) − t·ln√π is the Riemann–Siegel theta phase. The '
   'argument of ζ jumps by π at every zero; the phase therefore '
   'carries the POSITIONS of the zeros, not only their density. The '
   'campaign question: if the vortex charges of the full Hamiltonian '
   'are modulated by the θ-phase, q_k = θ(γ̃_k)/π, does an alignment '
   'of the spectrum with the zero ordinates appear — and does any '
   'point of the FULL handle space (signs, profile, anisotropy, mass, '
   'twists, δα) exist at which the rank agreement measured by the '
   'reference (H2) leaves the null zone?',
   'This is a map campaign: 96 configurations of a 2·2·3·2·2·2 '
   'factorial design × 3 seeds = 288 spectra of the 24×24 lattice '
   'under one and the same ζ-weight vortex protocol. The alignment '
   'metric r_align is the Pearson correlation between the increments '
   'of the unwrapped levels ΔU_n and the increments of the zero '
   'ordinates Δγ_n over a 200-level window; the linear bridge is fit '
   'on the first 50 levels, the residual is measured on the remaining '
   '150 (honest out-of-sample). The null model is 200 permutations of '
   'the ordinate increments: marginal densities are preserved while '
   'the level-n ↔ zero-n correspondence is destroyed.']},
 {'h1': 'Method and result',
  'paras': [
   'The core is rpbridge/fullham.py. Algebraic side: the θ-phase is '
   'computed in mpmath (dps 30) at the midpoints γ̃_k = (γ_k+γ_{k+1})/2 '
   '— deliberately off the zero set; the weight q_k = θ(γ̃_k)/π ∈ '
   '(−1, 1) enters the vortex phases of the full Hamiltonian with all '
   'C5 handles (twists, anisotropy, δα, staggered mass, profile, '
   'signs). For the weight comparison three modes run on the baseline '
   'configuration: the θ-phase of Z_id, log|ζ| (the V3 protocol), and '
   'no weight. The positive control is the algebraic function itself: '
   'the zeros of Z_id(t) on [0, 120] by bisection against the zero '
   'file.',
   'Main result: the identity does NOT close anywhere in the full '
   'handle space. The maximum r_align = +0.160 (configuration 64: '
   'all_plus charges, site profile, anisotropy 1.2) against the null '
   'zone −0.009 ± 0.068 — z = 2.49, far below the identity threshold; '
   'the out-of-sample residual of the best configuration is 0.134 '
   '(13% of the window span). The map average is −0.008: the handle '
   'map is noise, there is no lucky point. Weight comparison: θ-phase '
   '−0.108, log|ζ| +0.092, no weight −0.085 — all within ±2σ of the '
   'null zone; neither the algebraic phase nor the modulus of ζ '
   'revives the lattice. The positive control fires perfectly: 38 '
   'zeros of Z_id against the file, r = 1.0, maximum residual 4.9e-10 '
   '(the bisection floor) — the method sees identity where it '
   'exists.'],
  'table': {'caption': 'Table 1. V16: key numbers',
   'header': ['Quantity', 'Value', 'Status'],
   'rows': [
    ['Max r_align (96 configs × 3 seeds)', '+0.1597', 'z = 2.49'],
    ['Null zone (200 permutations)', '−0.009 ± 0.068', '—'],
    ['Map-average r_align', '−0.0083', 'noise map'],
    ['θ-phase weight (baseline)', '−0.108', 'inside null zone'],
    ['log|ζ| weight (V3 protocol)', '+0.092', 'inside null zone'],
    ['Out-of-sample RMSE, best config', '0.134', '13% of span'],
    ['PC: Z_id zeros vs file', 'r = 1.0, max 4.9e-10',
     'identity visible']]},
  'ratios': None},
 {'h1': 'Honest remarks and verdict',
  'paras': [
   'The negative result here is a measured boundary, not a defeat: it '
   'confirms the reference verdict (H2 — NO) on a wider class of '
   'objects and closes the hypothesis that the GUE-window protocol is '
   'specially selected — in the full handle space no statistically '
   'selected point exists, and the best z = 2.49 over 288 spectra is '
   'explained by multiple comparisons (the expected maximum of 288 '
   'Gaussian noises is ≈ 2.9σ). Emphasized: the campaign couples the '
   'lattice to the algebraic function through the PHASE (zero '
   'positions), bypassing GUE — and the identity still does not '
   'emerge. This strengthens the series conclusion: the obstacle is '
   'not the level statistics but the absence of a mechanism that '
   'transfers individual ordinates into the spectrum of a local '
   'Hamiltonian.',
   'Boundaries: a 200-level window, one geometry (24×24, open '
   'boundaries), 96 factorial configurations — continuous '
   'optimizations over the handles were not performed; non-local '
   'constructions remain outside the negative verdict, as in the '
   'reference.'],
  'conclusion': [
   'Verdict V16: the identity is NOT closed over the entire full '
   'handle space (z_best = 2.49 < 6); the θ-phase of Z_id is no more '
   'effective than log|ζ|; the positive control Z_id ↔ file gives '
   'r = 1.0. The full algebraic function remains the only object with '
   'exact identity — the H2 gap is reproduced and extended to the '
   'full gate class.']},
]}

# ═══════════════════════ V17 ══════════════════════════════════════════════
V17 = {'meta': _meta(
    'V17. Electron on the Critical Line',
    'Coherent transport of a wave packet along the self-dual line '
    'channel α = ½ on the full 96×24 Hamiltonian', 'V17', AUTHOR, AFFIL,
    SERIES, DATE), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
   'The reference monograph (campaign C7) states: "the motion of the '
   'electron along the critical line is confirmed in the dynamical '
   'sense" — on a 96×96 lattice at half flux, where the π-flux turns '
   'the lattice into a discretized massless Dirac equation, while the '
   'identification of the self-dual line α = ½ with Re(s) = ½ remains '
   'a conjectural bridge. This campaign reproduces and extends the '
   'calculation on the FULL Hamiltonian with an elongated waveguide '
   'geometry 96×24: an electron (a Gaussian packet, σ = 3, longitudinal '
   'momentum k₀ = π/2) is launched along the x axis — the "critical '
   'channel" — and lives on the horizon T = 40 with step dt = 0.1. '
   'Three vortex clouds are compared at identical geometry and seed '
   '96: the ζ-cloud (weights log|ζ(½+iγ̃_k)|, the V3 protocol), a '
   'random cloud of the same density, and the clean lattice.',
   'Metrics: the centroid trajectory ⟨x(t)⟩, ⟨y(t)⟩; the maximal '
   'deviation from the channel axis D_y; the transit P(x ≥ 88); the '
   'reflection P(x ≤ 4); the transverse spread σ_y(t); the coherence '
   'C(t) = |⟨ψ(0)|ψ(t)⟩|; energy conservation; and a new measurement — '
   'phase accompaniment: the correlation r_phase between the '
   'accumulated dynamical phase of the overlap arg⟨ψ(0)|ψ(t)⟩ and the '
   'θ-phase of the algebraic function along the trajectory '
   'θ(k₀⟨x(t)⟩) — the first direct numerical bridge "packet dynamics '
   '↔ algebraic function of the critical line" in the series.']},
 {'h1': 'Method and result',
  'paras': [
   'The core is rpbridge/electron.py. The dynamics is exact: the '
   '2304×2304 Hamiltonian is diagonalized once, propagation runs in '
   'the eigenbasis on a grid of 201 time points; energy conservation '
   'is machine-grade — the maximal relative deviation is 1.8e-15 on '
   'all trajectories. The packet is normalized; all three clouds use '
   'one and the same vortex position protocol (seed 96) and differ '
   'only in the weights.',
   'The results reproduce and refine the reference. Transit: clean '
   'lattice 0.160, ζ-cloud 0.112, random 0.069 — the ζ-cloud passes '
   'the electron ×1.62 better than the random cloud of the same '
   'density: the "phases guide" effect is reproduced on the centroid '
   'transit. The transverse behavior matches the reference '
   'qualitatively: the ζ-cloud deflects the packet from the channel '
   'axis by D_y = 2.81, the random one by only 0.54 — only ζ-phases '
   'create a transverse force. Coherence: the ζ-cloud preserves the '
   'overlap longer than the random one on the long horizon. Phase '
   'accompaniment: r_phase(ζ) = −0.96 against r_phase(random) = '
   '−0.52 — the dynamical phase of the packet in the ζ-cloud is '
   'rigidly anti-correlated with the θ-phase of the algebraic '
   'function; the magnitude and the sign are a new measured fact, and '
   'its interpretation is deferred to the honest remarks.'],
  'table': {'caption': 'Table 1. V17: three clouds, one packet',
   'header': ['Quantity', 'Clean', 'Random', 'ζ-cloud'],
   'rows': [
    ['Transit P(x ≥ 88) at T = 40', '0.1604', '0.0687', '0.1115'],
    ['Max deviation D_y', '0.0', '0.5404', '2.8050'],
    ['Coherence C(T = 40)', '0.0588', '0.0217', '0.0295'],
    ['r_phase with θ(trajectory)', '—', '−0.518', '−0.957'],
    ['Energy conservation (all)', '1.8e-15', '1.8e-15', '1.8e-15']]},
  'ratios': None},
 {'h1': 'Honest remarks and verdict',
  'paras': [
   'What is measured and what is not. Measured: the coherent dynamics '
   'of the packet on the self-dual line α = ½; the ×1.62 excess of '
   'the ζ-cloud transit over the random one; the transverse deviation '
   'only in the ζ-cloud; the rigid anti-correlation of the dynamical '
   'phase with θ. NOT measured: the identity of the line α = ½ with '
   'the critical line Re(s) = ½ — that is a conjectural bridge '
   'inherited from the reference; "the motion of the electron along '
   'the critical line" in this series means motion along the channel '
   'of the self-dual line statistically coupled to ζ — nothing more. '
   'The sign of r_phase: the anti-correlation is partly explained by '
   'the monotonicity of both phases (the large-scale drift pushes '
   '|r| toward 1 in any cloud); the difference ζ vs random (−0.96 vs '
   '−0.52) is the substantive part, but the physical mechanism calls '
   'for a separate study.',
   'Boundaries: one geometry and one seed (the determinism of the '
   'series); Nv = 48 vortices in the 96×24 channel; the packet is '
   'Gaussian, spinless; the horizon T = 40 — before the return of '
   'the packet.'],
  'conclusion': [
   'Verdict V17: the dynamics is honest (energy 1.8e-15); the electron '
   'passes the critical channel, the ζ-cloud guides it ×1.62 better '
   'than the random one and deflects it along y as in the reference '
   'C7; the phase accompaniment by the θ-function is measured (r = '
   '−0.96 vs −0.52 for random). The bridge "line ½ = Re(s) = ½" '
   'remains a conjecture — the H4 verdict is confirmed, no identity '
   'is claimed.']},
]}

# ═══════════════════════ V18 ══════════════════════════════════════════════
V18 = {'meta': _meta(
    'V18. The AB Operator as a Processor',
    'Exact single-qubit gates on a Hamiltonian block, two-qubit '
    'entanglement, and a deterministic AB-Pong game on the operator',
    'V18', AUTHOR, AFFIL, SERIES, DATE), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
   'The user claim: "the AB-cloud operator is able to work as a '
   'processor and run games". In the parent repository this direction '
   'is not measured — "gates" there merely denote families of '
   'Hamiltonians for the spectral question. This campaign turns the '
   'claim into three measurable levels of computability on the same '
   'AB-cloud Hamiltonian, without leaving its building blocks: '
   'P1 — single-qubit gates on a two-level block of the lattice (a '
   'site plus a neighbor, staggered mass m — the C5 handle, bond '
   'phase φ from the flux); P2 — entanglement of two qubits through '
   'an exchange link; P3 — a deterministic AB-Pong game whose entire '
   'ball dynamics is the unitary evolution e^{−iHt} of the AB-cloud '
   'operator.',
   'Processor criteria are pre-registered: (i) six gates {X, Y, Z, H, '
   'S, T} with fidelity F = |Tr(U_t†U)|²/4 ≥ 1 − 1e-9; (ii) the '
   'Wootters concurrence C > 0.5 from the product |↑↓⟩; (iii) an '
   'AB-Pong game completes, the score is deterministic, the replay is '
   'bit-exact. The composite verdict "processor" = (i) ∧ (ii) ∧ '
   '(iii).']},
 {'h1': 'Method and result',
  'paras': [
   'P1. The block H₂ = m·σz − t·cos φ·σx − t·sin φ·σy (the Pauli '
   'algebra verified). All six gates are implemented ANALYTICALLY by '
   'calibrated pulses: X, Y — π-rotations on the purely tunneling '
   'block (m = 0, φ = 0 and π/2); Z, S, T — rotations in the purely '
   'massive channel (m·t* = π/2, π/4, π/8); H — the block '
   '[[1,1],[1,−1]] = √2·H at m = t = 1, φ = π, pulse t* = π/(2√2). '
   'Measured fidelities: F = 1.0 − 2e-16 for all six — the machine '
   'floor.',
   'P2. Two blocks in kron order with an exchange link −J: the states '
   '|a↑b↓⟩ and |a↓b↑⟩ are degenerate (E = 0), the detuning to |↑↑⟩, '
   '|↓↓⟩ is 2m = 4 ≫ J — the link is isolated, the leakage through '
   'the σx-mixing is ~ (t/2m)² ≈ 0.6%. The maximal concurrence C = '
   '0.984 at t = 2.373 — near-Bell with the predicted leakage. The '
   'full CNOT synthesis is registered as the open obligation O18 — '
   'here the fact of entanglement is measured.',
   'P3. The AB-Pong board is a 1D chain of 64 sites with a uniform '
   'Peierls phase φ_ab = π/3 (in 1D the gauge reduces to a phase: it '
   'sets the drift E(k) = −2t·cos(k+φ)). The ball is a narrow packet '
   '(σ = 1, k₀ = π/6, group velocity v = 2t·sin(π/2) — the inflection '
   'point, minimal dispersion). The paddles are mirror reflectors '
   'with GAUGE compensation: (Uψ)(x) = e^{−2iφx}ψ(2p−x); without it '
   'the inversion k → −k does not reverse the velocity (v(−k) = '
   '2t·sin(φ−k) ≠ −v(k)) and the ball flies into its own wall — the '
   'discovered effect is documented. The Pong geometry: paddle homes '
   '17 and 47, reach radius 8, lead 2.5, cooldown 0.25 s, goals at '
   'x ≤ 5 and x ≥ 58. A game over T = 20: the score 0:1, 10 mirror '
   'intercepts, 411 log events, the replay is bit-exact.'],
  'table': {'caption': 'Table 1. V18: processor passport',
   'header': ['Level', 'Quantity', 'Value', 'Criterion'],
   'rows': [
    ['P1', 'Fidelity X, Y, Z, S, T', '1.0 − 2e-16', '≥ 1 − 1e-9 — YES'],
    ['P1', 'Fidelity H (m = t = 1, φ = π)', '1.0 − 2e-16',
     '≥ 1 − 1e-9 — YES'],
    ['P2', 'Maximal concurrence', '0.984 at t = 2.373', '> 0.5 — YES'],
    ['P2', 'Leakage (t/2m)² estimate', '≈ 0.006', 'consistent'],
    ['P3', 'AB-Pong score', '0:1 (goal at the right wall)',
     'game completed — YES'],
    ['P3', 'Mirror intercepts / events', '10 / 411', '—'],
    ['P3', 'Game replay', 'bit-exact', 'determinism — YES'],
    ['Total', 'Processor (i)∧(ii)∧(iii)', 'YES', 'composite verdict']]},
  'ratios': None},
 {'h1': 'Honest remarks and verdict',
  'paras': [
   'What exactly is claimed. P1 works on the EFFECTIVE two-level '
   'block — the same building block the full Hamiltonian is assembled '
   'from; embedding the pulses into the full lattice with '
   'inter-qubit crosstalk is obligation O19. The Z/S/T channel is a '
   'limiting point of the handle space (pure mass, bond off). P2 — '
   'entanglement is measured, but CNOT synthesis and a universal '
   'two-qubit set are not performed (O18). P3 — the game is '
   'deterministic and runs on the operator, but it is a game with '
   'unitary mirror paddles and a lead-following AI; "running arbitrary '
   'games" does NOT follow from this — what follows is that the '
   'unitary dynamics of the AB operator plus permutation proxies form '
   'an executable environment for deterministic discrete games. The '
   'gauge-covariant mirror is a side theoretical result of the '
   'campaign: in a magnetic gauge a reflector must include the phase '
   'e^{−2iφx}, otherwise the inversion does not return the ball.',
   'Boundaries: a 1D board, 64 sites, no measurements (all logic via '
   'the centroid); the minimal-dispersion channel (inflection point); '
   'a single game (determinism verified by replay, not by an '
   'ensemble).'],
  'conclusion': [
   'Verdict V18: processor — YES on three levels: the gates {X, Y, Z, '
   'H, S, T} are exact (F = 1 − 2e-16), the entanglement is '
   'near-Bell (C = 0.984), the AB-Pong game executes on the AB '
   'operator deterministically (0:1, bit-exact replay). The user '
   'claim is translated from a declaration into a measured, '
   'reproducible result with honest boundaries (O18, O19).']},
]}

DOCS = {'V16': V16, 'V17': V17, 'V18': V18}
