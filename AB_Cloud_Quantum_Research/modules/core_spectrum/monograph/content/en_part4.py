# -*- coding: utf-8 -*-
"""content/en_part4.py — theorems volume and appendix (English series, v1.1.0)."""
from content.common import _meta
from content.en_part1 import AUTHOR, AFFIL, SERIES, DATE

THEOREMS = {'meta': _meta('Theorems of the AB Research Program',
 'Th1–Th6: hermiticity, self-adjointness, certificates, the spectral Li '
 'formula, block reduction, the Guinand–Weil trace formula',
 'Theorems', AUTHOR, AFFIL, SERIES, DATE), 'sections': [
 {'h1': 'Th1. Hermiticity and reality of the spectrum',
  'theorem': {'label': 'Theorem Th1 (V4).',
   'text': 'For any choice of vortices, W, α and boundaries the operator '
   'H_L satisfies H_L = H_L†; hence spec(H_L) ⊂ ℝ. At α = ½ and W = 0 '
   'the spectrum is symmetric: λ ∈ spec ⇒ −λ ∈ spec.',
   'proof': 'Every bond is inserted as the pair H[i,j] = −t·e^{iφ}, '
   'H[j,i] = −t·e^{−iφ} = conj(H[i,j]) — hermiticity by construction; '
   'the diagonal is real (vortex potential, disorder, staggered mass). '
   'By the spectral theorem for Hermitian matrices the whole spectrum '
   'is real. Symmetry at W = 0: the lattice is bipartite in the '
   'parity ix+iy; in that basis H = [[0, B], [B†, 0]]; if H(λ, 0) = '
   'λ·(u, v) then H(−v, u)·(−1) = −λ·(u, v) — the spectrum is '
   'symmetric about zero. Numerical certificate: ‖H − H†‖ = 0.0 '
   'exactly; the pairing λ ↔ −λ reproduced to 8.2e-15; reality '
   'residuals 8.8e-15 (the eigvalsh machine floor).'}},
 {'h1': 'Th1.1 Certificate and boundaries',
  'paras': [
   'The certificate is reproducible: test_th1_passport.py checks '
   'hermiticity on three protocol gates (Nv = 16/64/256, seed 96) and '
   'demands ‖H − H†‖ ≤ 1e-12; the fact is exactly 0.0, since the '
   'construction uses no approximations — conjugate pairs are written '
   'simultaneously. Importantly, hermiticity survives ALL the C5 '
   'handles — twists, anisotropy, δα, staggered mass, profile, signs: '
   'each handle either modifies the bond magnitude (preserving the '
   'phase pair) or the diagonal (staying real). This makes Th1 an '
   'architectural property, not a property of a single configuration.',
   'Boundaries: Th1 says nothing about the correspondence of the '
   'spectrum to the ζ zeros — that is the H2/H5 question, where the '
   "series' verdicts are: the level identity holds at the zeros' level "
   '(V6/V16 — YES via the D_nn bridge, v2.0.7) with the bit-level branch '
   'open (V16, z = 2.49 < 6), and the specific design claims refuted '
   '(V1: the blind coding is invisible; V3: σ = ½ is not optimal in '
   'D_KS). The '
   'pairing λ ↔ −λ breaks already at W > 0 (the vortex potential is '
   'asymmetric) and is not restored by vortices.']},
 {'h1': 'Th2. Finite-dimensional self-adjointness',
  'theorem': {'label': 'Theorem Th2 (V8).',
   'text': 'A symmetric operator on ℂ^N is essentially self-adjoint: '
   'defect indices (0, 0); e^{−iHt} is unitary; Im⟨ψ, Hψ⟩ = 0.',
   'proof': 'On ℂ^N every bounded symmetric operator is self-adjoint: '
   'D(H) = ℂ^N and the defect spaces ker(H* − iI), ker(H* + iI) are '
   'empty, since ‖(H ∓ iI)ψ‖² = ‖Hψ‖² + ‖ψ‖² ≥ ‖ψ‖² > 0 (the '
   'cross-term vanishes by symmetry). Consequences: real spectrum, '
   'e^{−iHt} a unitary group, ⟨ψ, Hψ⟩ real. Numerically: the minimal '
   'singular value of H − iI is 3.9 (theory: √(1 + min‖Hψ‖²) ≥ 1), '
   'the unitarity drift of e^{−iHt} is 2.2e-16 over 1000 steps. The '
   'limit part (L → ∞, essential self-adjointness of an unbounded '
   'operator) is the open obligation O03.'}},
 {'h1': 'Th2.1 Certificate and boundaries',
  'paras': [
   'Certificate: test_th2_selfadjoint.py checks three equivalent '
   'manifestations of self-adjointness — empty defects, unitary '
   'dynamics, real form — on the protocol gate; all three hold at '
   'machine floors. Practical value: the unitarity of e^{−iHt} '
   'underpins the dynamics campaigns (V17): the energy conservation '
   '1.8e-15 in V17 is a direct corollary of Th2. The gap '
   '"finite-dim proved / limit open" is recorded honestly: in the '
   'infinite-dimensional problem symmetry is not enough, boundary '
   'conditions are needed (open boundaries are natural, but the '
   'strict convergence of resonances is an open problem of the '
   'program).',
   'Boundaries: the theorem is finite-dimensional; the transfer to '
   'L → ∞ requires estimates of the essential spectrum and resonance '
   'geometry — see O03 in the obligation DAG.']},
 {'h1': 'Th3. Eigenvalue certificates',
  'theorem': {'label': 'Theorem Th3 (V12).',
   'text': 'For Hermitian H, a computed λ̃, a unit v with residual '
   'r = Hv − λ̃v, δ = ‖r‖ and gap g to the nearest other level, some '
   'λ̂ ∈ spec H satisfies |λ̂ − λ̃| ≤ δ²/g; the whole spectrum lies in '
   'the union of rational Gershgorin intervals.',
   'proof': 'Decompose v = c·u + w with u the normalized eigenvector '
   'of λ̂ and w ⊥ u. The residual weight on foreign levels yields the '
   'Kato-type estimate ‖w‖ ≤ δ/gap, hence |λ̂ − λ̃| ≤ δ²/gap — '
   'quadratic superconvergence: at δ ~ 1e-8 and gap ~ 0.5 the '
   'interval shrinks to ~2e-16. Gershgorin: for H = D + E the radii '
   'R_i = Σ_{j≠i}|H_ij| in exact rational arithmetic (fractions, '
   'limit_denominator 1e12) give rounding-free intervals; their union '
   'covers the spectrum deterministically. Verified 5/5 certificates '
   'with width ~1e-27 in mpmath (dps 40).'}},
 {'h1': 'Th3.1 Certificate and boundaries',
  'paras': [
   'Certificate: test_th3_certificates.py checks (a) the claimed level '
   'falls into its Kato interval, (b) the spectrum is covered by '
   'Gershgorin intervals, (c) the width reproduces. The series '
   'threshold 1e-27 is achieved on the first five levels of the '
   'protocol gate. Value for the program: the interval layer is a '
   '"trust passport" for all spectral comparisons (V1–V3, V6, V16) — '
   'any coincidence of levels with zero ordinates can be certified by '
   'intervals, not only by floating-point numbers.',
   'Boundaries: the estimate is quadratic in δ and therefore requires '
   'an already well-converged λ̃; for degenerate or close levels the '
   'gap is small and the interval widens — cluster versions of the '
   'estimate are not included in the package. Rational arithmetic is '
   'slow: the layer is applied pointwise, not to the whole spectrum.']},
 {'h1': 'Th4. The spectral Li formula',
  'theorem': {'label': 'Theorem Th4 (V15).',
   'text': 'The Li coefficients admit the spectral representation λ_n '
   '= Tr g_n(H_ξ), g_n(E) = 1 − (1 − 1/ρ(E))^n, ρ(E) = ½ − iE/2; the '
   'series converges absolutely; two computational paths agree with '
   '|Δ| ≤ 4.4e-11 for n ≤ 3000.',
   'proof': 'By definition λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] over the '
   'nontrivial zeros with conjugation accounted (λ_n is real). The '
   'bijection spec H_ξ ↔ zero pairs {γ, −γ} converts the trace into a '
   'pair sum: the pair contribution 2 − 2Re(1 − 1/ρ(γ))^n = O(n/γ²) '
   'as γ → ∞ — absolute convergence against Σ 1/γ². The poles of g_n '
   'sit at ρ = 1, i.e. E = −i — off the real spectrum of H_ξ: the '
   'trace is well defined. Numerics: two independent paths — (a) a '
   'direct sum over the zero file with a tail, (b) a spline trace over '
   'the thermal metric; agreement |Δ| ≤ 4.4e-11. Positivity λ_n ≥ 0 — '
   'the Li criterion — is measured for n ≤ 3000 (tails ≤ 0.115); for '
   'all n the question is open and equivalent to RH.'}},
 {'h1': 'Th4.1 Certificate and boundaries',
  'paras': [
   'Certificate: test_th4_li.py checks the agreement of the two paths '
   'on the grid n ≤ 3000 and positivity; threshold 1e-9, fact 4.4e-11. '
   'Value: Th4 is the bridge from the ζ zeros to the operator H_ξ — '
   'the "working operator" of the reference (H5 — YES for H_ξ while '
   'NO for the gates): the prime weight Λ(n)/√n lives in the trace of '
   'H_ξ, directly measured in V7.',
   'Boundaries: absolute convergence is proved, but positivity is '
   'empirical only up to n = 3000; extending the grid is linear in '
   'time and bounded by the zero file (external data). The '
   'path-agreement depends on the tail model (an exponential tail '
   'with the constant from the smooth part).']},
 {'h1': 'Th5. Block reduction by symmetry',
  'theorem': {'label': 'Theorem Th5 (V9).',
   'text': 'If [H, A] = [H, B] = 0 for the generators of the abelian '
   'group G of magnetic translations, then H is block-diagonal in the '
   'character decomposition of G and spec H = ⊔_χ spec(H|Π_χ ℂ^N).',
   'proof': 'Commuting unitaries A, B are simultaneously '
   'diagonalizable; their joint eigenvalues are the characters χ: G → '
   'U(1); the spectral projectors Π_χ (polynomials in A, B) commute '
   'with H: [H, Π_χ] = 0, hence each Π_χ ℂ^N is invariant and H '
   'decomposes into the direct sum of restrictions. Corollary: '
   'eigenvalues are found in smaller blocks with guaranteed coverage. '
   'Numerically: the union of 6 blocks reproduces the full spectrum '
   'to 7.1e-15; vortices break the symmetry (commutators ε_g = O(1)) '
   '— the reduction applies only to the clean lattice and to '
   'symmetric vortex configurations.'}},
 {'h1': 'Th5.1 Certificate and boundaries',
  'paras': [
   'Certificate: test_th5_block_reduction.py compares the union of '
   'the block spectra with the full spectrum; threshold 1e-9, fact '
   '7.1e-15. The value is twofold: (a) computational — the reduction '
   'speeds up scans (each block ~L²/6 instead of L²); (b) '
   'diagnostic — the magnitude ‖[H, A]‖ measures how far a vortex '
   'configuration is from symmetric and serves as a passport feature '
   'of a gate in V4.',
   'Boundaries: for protocol (asymmetric) vortices the reduction does '
   'not apply — this is not a defect but the boundary of its domain; '
   'partially symmetric configurations give approximate invariant '
   'subspaces, and the quantification of this idea is not included in '
   'the package.']},
 {'h1': 'Th6. The Guinand–Weil trace formula',
  'theorem': {'label': 'Theorem Th6 (V7).',
   'text': 'Q(a) = Σ_{γ>0} 2a/(a²+γ²) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) '
   '− ½lnπ + ½ψ(¼+a/2) − B − C₀, with B = ½ln(4π) − 1 − γ/2, C₀ = −B; '
   'and K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a)·sin(ax) da.',
   'proof': 'Step 1: the logarithmic derivative of the Hadamard '
   'product ξ(s) = ½·∏_ρ(1 − s/ρ) gives ξ′/ξ(½+a) proportional to '
   'Σ_γ 2a/(a² + γ²) — the sum Q(a) up to the normalization of the '
   'poles. Step 2: the explicit pole terms (the ζ pole at s = 1, the '
   'functional equation at s = ½, the Γ-factor through ψ) assemble '
   'into the constants; the comparison at a → 0+ fixes B = ½ln(4π) − '
   '1 − γ/2 (ERRATUM: the parent repository encodes ½ln(2π); here the '
   'value is re-derived and checked by the asymptotics). Step 3: the '
   'representation 2a/(a²+γ²) = 2∫₀^∞ e^{−γt}·sin(at) dt and the '
   'exchange of integration (absolute convergence at x > 0) give '
   'K(x) = (1/π)∫ Q(a) sin(ax) da. Step 4: at a > ½ the series ζ′/ζ '
   '= −Σ Λ(n)/n^{½+a} transfers the prime weight into the trace: the '
   'prime part of K is the comb over Λ(n)/√n. Numerically: |ΔQ| ≤ '
   '4.6e-8 (mpmath, 601-node spline), |ΔK| ≤ 6.9e-6 (Λ-sieve to '
   '2·10⁶, tail ≤ 1e-6).'}},
 {'h1': 'Th6.1 Certificate and boundaries',
  'paras': [
   'Certificate: test_th6_trace_formula.py checks Q(a) against the '
   'direct summation over the zero file and K(x) against the prime '
   'part; thresholds 1e-6/1e-5, facts 4.6e-8/6.9e-6; the PC0 recipe '
   'u·Σe^{−uN̄(γ)} − (1 − e^{−uX}) reproduced with the correlation r = '
   '+0.9996. Value: Th6 is the most precise bridge of the series '
   '"zeros ↔ operator": it not only records THAT primes live in the '
   'trace of H_ξ but also delivers the numerical pipeline (V7) on '
   'which the null operator of the program is assembled.',
   'Boundaries: the constant B depends on the normalization of ξ; the '
   'formula for K(x) requires x > 0 and the smooth part with exact '
   'Si/Ci forms; the Λ-sieve to 2·10⁶ limits the comb resolution — '
   'the tail beyond n > 2·10⁶ is estimated by an exponential, its '
   'contribution ≤ 1e-6.']},
 {'h1': 'The status table',
  'table': {'caption': 'Table 1. Theorem statuses',
   'header': ['Theorem', 'Campaign', 'Status', 'Key number'],
   'rows': [
    ['Th1', 'V4', 'proved', '‖H−H†‖ = 0'],
    ['Th2', 'V8', 'proved (finite-dim)', 'drift 2.2e-16'],
    ['Th3', 'V12', 'proved + verified', '5/5 certificates'],
    ['Th4', 'V15', 'proved + verified', '|Δ| = 4.4e-11'],
    ['Th5', 'V9', 'proved + verified', '7.1e-15'],
    ['Th6', 'V7', 'proved + verified', '|ΔK| = 6.9e-6']]},
  'ratios': None},
 {'h1': 'The boundary of the proved',
  'paras': [
   'None of the theorems proves RH or establishes the spectral '
   'identity for the lattice gates — the latter question is measured '
   'negatively three times (V1, V6, V16 — over the entire full handle '
   'space). The exact status of the program is fixed by the '
   'obligation DAG (V13): the path to RH contains 4 conjectures; the '
   'open obligations O03 (the L → ∞ limit), O18 (CNOT synthesis on '
   'the blocks), O19 (embedding the pulses into the full lattice) '
   'are added in v1.1.0. The theorems of the package are the '
   'foundation and the measurement infrastructure, not a final '
   'result.'],
  'conclusion': [
   'Six theorems, each with a full derivation, a numerical '
   'certificate, a reproducible test and honest boundaries. This is '
   'the honesty discipline in action.']},
]}

APPENDIX = {'meta': _meta('Appendix: Methods, Data, Reproducibility',
 'Protocols of the series V1–V18: lattice, unfolding, statistics, the '
 'trace pipeline, certificates, thresholds and machine floors',
 'Appendix', AUTHOR, AFFIL, SERIES, DATE), 'sections': [
 {'h1': 'A.1 Lattice and gates',
  'paras': [
   'The AB-cloud Hamiltonian: a Hermitian Hofstadter-type L×L lattice '
   'at half flux (α = ½ — the self-dual line of the discretized '
   'massless Dirac equation), vortex phases θ_k = atan2, on-site '
   'disorder W. Vortex protocol: cell centers (ix+0.5, iy+0.5), '
   'independent sampling, neutral charges. Series master seed 96; '
   'vortex RNG — seed + 3500, disorder — seed + 3501. The full handle '
   'space (V16): charge signs, vortex profile (site/midpoint), '
   'anisotropy t_x/t_y, staggered mass, twists (φx, φy), flux shift '
   'δα — a 96-configuration factorial design.',
   'Spectral pipeline: eigvalsh (driver evr) → central band 60% '
   '(fld arithmetic) → polynomial unfolding (degrees 6→3, '
   'piecewise-linear fallback) → 200-level window. Bit-exact '
   'reproduction of the reference C3 protocol: 1.45e-16.']},
 {'h1': 'A.2 Statistics and references',
  'paras': [
   'The vector S = (⟨r⟩, Σ²(L), Δ₃(L), K(t), D_KS) is '
   'pre-registered. The GUE reference for D_KS is empirical (an '
   'ensemble of 16 matrices 576×576, a pooled sample of 3168 {r_n} '
   'values); reference ladders: Poisson 2ln2−1 ≈ 0.386, GOE ≈ 0.531, '
   'GUE ≈ 0.600. The ζ zeros — the Odlyzko file of 50,000 ordinates '
   '(SHA-256 in data/README.md); the smooth count N̄(γ) = γ/2π·'
   'ln(γ/2πe) + 5/8. The algebraic function of the critical line '
   '(V16): Z_id(t) = e^{iθ(t)}ζ(½+it), θ(t) = Im ln Γ(¼+it/2) − '
   't·ln√π; the Γ-closures |Γ(½+iu)|² = π/cosh πu, |Γ(iu)|² = '
   'π/(u·sinh πu), the Legendre product |Γ(¼+iu)|·|Γ(¾+iu)| — '
   'residuals ~1.3e-39 at dps 40.',
   'The trace pipeline: Q(a) — a spline of the mpmath grid [0, 1.5] '
   '(601 nodes, the pole a = ½ shifted); the prime part — the Λ(n) '
   'sieve to 2·10⁶ (cached), tail ≤ 1e-6; the smooth part — exact '
   'Si/Ci forms; PC0 — the recipe u·Σ e^{−u·N̄(γ)} − (1−e^{−uX}), U ∈ '
   '[0.05, 1.0], 40 points.']},
 {'h1': 'A.3 Certificates and thresholds',
  'paras': [
   'The interval layer: Gershgorin in fractions (limit_denominator '
   '1e12), residuals in mpmath dps = 40, the gap exact. The data '
   'license layer: the zero file is the only external data; all '
   'verdicts are committed and independent of fresh recomputations.',
   'The threshold table (threshold → fact): hermiticity 1e-12 → 0.0; '
   'residuals 1e-11 → 8.8e-15; M0 1e-6 → 4.6e-8; M1 5e-5 → 6.9e-6; '
   'PC0 0.99 → 0.9996; Th4 1e-9 → 4.4e-11; reduction 1e-9 → 7.1e-15; '
   'unitarity 1e-12 → 2.2e-16; blind z > 3 → 0.09; V18 gates 1e-9 → '
   '2e-16; V18 entanglement > 0.5 → 0.984; V17 energy 1e-12 → '
   '1.8e-15.']},
 {'h1': 'A.4 Reproducibility',
  'paras': [
   'Self-build: make tour (a tour over the committed verdicts), make '
   'test (pytest), make ivp (independent verification), make figures '
   '/ monographs / workbook (artifact regeneration), make all. A '
   'fresh full recomputation of V1–V18: python3 scripts/'
   'compute_all.py and python3 scripts/compute_v161718.py (~10 '
   'minutes total; the zero file is included in the package). The '
   'web lab — web_lab/index.html, a self-contained file without '
   'external dependencies, including a playable AB-Pong.',
   'Every campaign is deterministic: fixed seeds, cached sieves, '
   'fixed grids. A divergence of a fresh run from the committed '
   'verdicts is a release stopper (the test_repro test).'],
  'conclusion': [
   'The appendix records all protocol decisions needed for an '
   'independent reproduction of the series V1–V18.']},
]}

DOCS = {'theorems': THEOREMS, 'appendix': APPENDIX}
