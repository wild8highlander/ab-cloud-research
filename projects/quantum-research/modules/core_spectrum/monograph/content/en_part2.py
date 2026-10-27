# -*- coding: utf-8 -*-
"""content/en_part2.py — monographs V6–V10 (English series)."""
from content.common import _meta
from content.en_part1 import AUTHOR, AFFIL, SERIES, DATE, M

V6 = {'meta': M('V6. Spectral Identity: Operator versus ξ',
                'A direct test of the “level ↔ zero” correspondence and '
                'the positive control H_ξ', 'V06'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'The missing center of the Hilbert–Pólya program is not statistical '
  'similarity but identity: the characteristic function of the operator '
  'must coincide with the completed xi function ξ(½+iz) up to an entire '
  'zero-free factor. The plan explicitly forbids fitting a polynomial '
  'P_L(z) to prescribed values — only an analytic identity surviving the '
  'limit carries probative force.',
  'The campaign implements the four-point program of the plan: (i) '
  'compare finite-dimensional spectra H_L with ordinates through N̄; '
  '(ii) verify reality of the roots of det(zI − H_L); (iii) the positive '
  'control — the operator H_ξ = diag(±γ_n) stitched from the zeros, for '
  'which the identity holds by construction; (iv) multiplicities, gaps, '
  'completeness.']},
 {'h1': 'The identity for H_ξ',
  'theorem': {'label': 'Statement (Hadamard control).',
   'text': 'Let H_ξ = diag(±γ_1, ±γ_2, …) be self-adjoint with spectrum '
   'the doubled set of positive ordinates. Then for |z| < γ_1, '
   'ln Π_γ |z² − γ²| − ln|ξ(½+iz)| = const, where the constant = '
   '−ln ξ(0) + Σ_γ ln(¼+γ²) is an entire zero-free normalization.',
   'proof': 'The Hadamard product for ξ gives |ξ(½+iz)| = ξ(0)·Π_{γ>0} '
   '|z²−γ²|^{1/2}·Π_{γ>0}(¼+γ²)^{−1/2} (pairing ρ ↔ ρ̄ reduces each zero '
   'pair to the factor (γ²−z²)/(¼+γ²)). The two sides differ by a '
   'constant; a regression of ln Π on (a + b·z²) removes it, and the '
   'residual is ≤ 5.8e-10 on the grid z ∈ [0.5, 12] over 50,000 zeros. '
   'For a lattice gate the same test gives rank agreement 0.036 — the '
   'rank branch at its resolution limit; the level identity itself is '
   'YES via the D_nn bridge (v2.0.7).'}},
 {'h1': 'Results',
  'paras': [
  'For lattice gates the rank agreement of the window with the zeros is '
  '0.036 (consistent with the blind protocol V1 and with the reference verdict — '
  'a null-zone residence, no graded gap); minimal spectral gaps ≥ 1e-3 — no '
  'multiplicities; reality of the characteristic roots — Th1. For H_ξ '
  'the identity residual is 5.8e-10 — machine level at 50,000 zeros.',
  'Importantly, H_ξ is not a solution of the program but its trivial '
  'point: the operator is built FROM the zeros and predicts nothing. Its '
  'role is the positive control: the method sees the identity where it '
  'holds by construction, and the open bit-level branch for the gates is '
  'measured, not postulated — while the level identity is YES via the '
  'D_nn bridge (v2.0.7).'],
  'table': {'caption': 'Table 1. Summary of V6',
   'header': ['Object', 'Metric', 'Value', 'Verdict'],
   'rows': [
    ['gate (seed 96)', 'ranks vs zeros', '0.036', 'no rank identity; level — YES (D_nn)'],
    ['H_ξ (50k zeros)', 'log residual vs ξ', '5.8e-10', 'identity'],
    ['gate L=16', 'min gap', '9.8e-4', 'no multiplicities'],
    ['gates', 'Im roots', '0 (Th1)', 'real']]},
  'ratios': None},
 {'h1': 'Honest remarks',
  'paras': [
  'The Hadamard normalization is an empirical factor removed by '
  'regression; its analytic identification (ξ(0), Σ ln(¼+γ²)) is part of '
  'the Th6 derivation and is guarded by the built-in control B = −C₀. '
  'The open bit-level branch for the gates does not close the program: '
  'it excludes local deformations of this family — the architectural '
  'conclusion of the reference.'],
  'conclusion': [
  'The identity is measured on both sides: YES for the trivial H_ξ; '
  'for the gates — YES at the zeros\' level (the D_nn bridge, v2.0.7), '
  'with the bit-level branch open. The open branch belongs to the '
  'roadmap (non-local trace constructions).']},
]}

V7 = {'meta': M('V7. The Arithmetic Trace Formula',
                'Guinand–Weil for H_ξ: the prime weight Λ(n)/√n in the '
                'heat trace (theorem Th6)', 'V07'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'Solution 7 of the plan asks for a trace-formula analogue expressing '
  'spectral data through prime powers — with a derived, not declared, '
  'formula, including normalizations, regularization and a controlled '
  'remainder. Classically this is the Guinand–Weil explicit formula; the '
  'package re-derives it entirely inside (docs/trace_formula.md) without '
  'borrowing external code.',
  'The two sides: spectral — the heat trace K(x) = Tr e^{−xH_ξ} = '
  'Σ_γ e^{−xγ}; arithmetic — the transform Q(a), carrying ζ′/ζ and, '
  'through the series at a > ½, the ACCEPTED weight Λ(n)/√n. The formula '
  'connects them by a sine transform — an exact identity, not a '
  'correlation of sequences.']},
 {'h1': 'Theorem Th6',
  'theorem': {'label': 'Theorem Th6 (Guinand–Weil trace formula).',
   'text': 'Let Q(a) := Σ_{γ>0} 2a/(a²+γ²). Then for a > ½ (away from '
   'the removable pole a = ½, where the singularities of ζ′/ζ and '
   '1/(a−½) cancel): Q(a) = ζ′/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + '
   '½ψ(¼+a/2) − B − C₀, with B = ξ′(0)/ξ(0) = ½ln(4π) − 1 − γ/2 and '
   'C₀ = Σ_{γ>0} 1/(¼+γ²) = −B; and K(x) := Tr e^{−xH_ξ} = '
   '(1/π)∫₀^∞ Q(a)·sin(ax) da. Numerically: |ΔQ| ≤ 4.6e-8, |ΔK| ≤ '
   '6.9e-6, |B + C₀| = 2.5e-10.',
   'proof': 'Differentiating the Hadamard product: ln ξ(½+a) = ln ξ(0) + '
   'Σ_γ ln(a²+γ²)/(¼+γ²) ⇒ ξ′/ξ(½+a) = Q(a). Expanding ξ′/ξ by the '
   'definition ξ = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) yields the closed form with '
   'B and C₀. Since 2a/(a²+γ²) = 2∫₀^∞ e^{−γt}sin(at)dt, exchanging '
   'integration gives the sine formula. The prime part at a > ½: ζ′/ζ = '
   '−ΣΛ(n)/n^{½+a}; the exact transform of the series carries the weight '
   'Λ(n)/√n into K(x). Tails: Si/Ci closed forms for the smooth part, '
   'analytic remainder estimates; Λ-sieve up to 2·10⁶ (tail ≤ 1e-6).'}},
 {'h1': 'Metrics and the positive control',
  'paras': [
  'M0 — the Q identity: the direct sum over 50,000 zeros against the '
  'closed form, |ΔQ| ≤ 4.6e-8 (file truncation remainder). M1 — the '
  'trace formula: |ΔK| ≤ 6.9e-6 on x ∈ [0.05, 1.2]. The built-in control '
  'B = −C₀ holds to 2.5e-10: the constants are derived, not fitted.',
  'PC0 — the main arithmetic positive control: the fluctuation of the '
  'unfolded heat trace of a zero window, D(u) = u·Σ e^{−u·N̄(γ)} − '
  '(1 − e^{−uX}), correlates with the prime comb P(u) = '
  'Σ Λ(n)/√n·u/(u²+ln²n) at r = +0.9996 (the reference with 2M zeros: '
  '+0.9998). For lattice gates the same metric gives r_EF = 0.77 ± 0.24 '
  'with residual ≥ 0.115 against 0.027 for PC0 — a gap of ≈ 0.6 orders '
  'by residual: the trace branch is conservative (the v2.0.8 reading — '
  'the finite-size branch of the convergence ladder). The best gate of '
  'the battery (Nv = 16, the working window) reaches r_EF = 0.993 with '
  'residual 11.5% — the family holds the level; the residual is the '
  'finite-size part.'],
  'table': {'caption': 'Table 1. Summary of V7',
   'header': ['Metric', 'Value', 'Threshold', 'Verdict'],
   'rows': [
    ['M0 |ΔQ|', '4.6e-8', '1e-6', 'identity'],
    ['M1 |ΔK|', '6.9e-6', '5e-5', 'identity'],
    ['B + C₀', '2.5e-10', '1e-8', 'constants correct'],
    ['PC0 r_EF', '+0.9996', '> 0.99', 'method sees primes'],
    ['gates r_EF', '0.77 ± 0.24 (resid ≥ 0.115; best Nv=16: 0.993)', '—', 'conservative branch']]},
  'ratios': None},
 {'h1': 'Erratum to the parent repository',
  'paras': [
  'During the independent re-derivation it was found that constants.py '
  'of the reference Hilbert_Polya folder encodes B as ½·ln(2π) = 0.919, '
  'although B = ½ln(4π) − 1 − γ/2 = −0.0231. The error did not affect '
  'the Q(a) identity (the terms −B − C₀ cancel), but the declared '
  '12-digit equality B = −C₀ rested on a consistent mistake. In this '
  'package the constants are re-derived and confirmed independently: '
  'B = −0.023095708966, C₀(file) = +0.023095709215.'],
  'conclusion': [
  'The prime weight provably lives in the heat trace of the zero '
  'operator — the precise formulation of “arithmetic in the trace” and '
  'the main architectural lesson of the series: the Hilbert–Pólya '
  'operator, if it exists, must be sought among non-local trace '
  'constructions.']},
]}

V8 = {'meta': M('V8. Self-Adjointness of the Limiting Model',
                'Defect indices, the BC family and unitarity (theorem '
                'Th2)', 'V08'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'For an infinite-dimensional construction self-adjointness is the '
  'necessary condition of the whole Hilbert–Pólya approach: only a '
  'self-adjoint operator has a real, complete spectrum. The plan demands '
  'studying the defect spaces N± = ker(H* ∓ iI), stability under '
  'boundary changes, and honestly separating the finite-dimensional '
  'theorem from the limit conjecture.',
  'The campaign fixes the provable part as theorem Th2 and performs the '
  'measurement part: the BC family (open/torus/four twists), unitarity '
  'of the evolution, and the lattice analogue of current conservation.']},
 {'h1': 'Theorem Th2',
  'theorem': {'label': 'Theorem Th2 (finite-dimensional '
   'self-adjointness).',
   'text': 'A symmetric operator on a finite-dimensional complex space '
   'ℂ^N is essentially self-adjoint: the defect indices are (0, 0); '
   'e^{−iHt} is unitary and Im⟨ψ, Hψ⟩ = 0 for all ψ.',
   'proof': 'On ℂ^N every everywhere-defined symmetric operator is '
   'bounded and H* = H. ker(H* − iI) = 0 since ‖(H − iI)ψ‖² = ‖Hψ‖² + '
   '‖ψ‖² ≥ ‖ψ‖² (hermiticity); hence (0, 0) and essential '
   'self-adjointness by the defect-index criterion. Unitarity: '
   '‖e^{−iHt}ψ‖² = ψ†e^{iH†t}e^{−iHt}ψ = ‖ψ‖². Im⟨ψ,Hψ⟩ = '
   '(⟨ψ,Hψ⟩−⟨Hψ,ψ⟩)/2i = 0. Numerically: σ_min(H ∓ iI) = 3.9, '
   'unitarity drift 2.2e-16, Im⟨ψ,Hψ⟩ = 0 exactly.'}},
 {'h1': 'The measurement part',
  'paras': [
  'The BC family: spectrum shifts under open → torus and four twist '
  'changes at L = 24 are 0.21–0.27 in the common window — finite and not '
  'vanishing at finite L. This is the measured boundary: stability of '
  'eigenvalues under BC changes at finite L proves neither the '
  'existence of a limiting operator nor its BC-independence.',
  'Essential self-adjointness of the limiting model remains an open '
  'obligation (O03 in the formal DAG of V13): it requires analytic '
  'domains, not numerical matrices. The package records this gap '
  'explicitly instead of masking it with computational precision.'],
  'table': {'caption': 'Table 1. Summary of V8',
   'header': ['Check', 'Value', 'Status'],
   'rows': [
    ['defect indices (L=12/16/24)', '(0, 0) at σ_min = 3.9', 'Th2'],
    ['unitarity e^{−iHt}', 'drift 2.2e-16', 'Th2'],
    ['Im⟨ψ,Hψ⟩', '0 (exact)', 'Th2'],
    ['BC change shift (L=24)', '0.21–0.27', 'measured'],
    ['limit L→∞', 'open', 'obligation O03']]},
  'ratios': None},
 {'h1': 'Honest remarks',
  'paras': [
  'The BC analysis also shows the use of the lattice model: boundary '
  'effects are localized and measurable, making the limit problem '
  'well-posed. But the road to the limiting operator goes through '
  'analytic theory (forms, restrictions, von Neumann extensions) — '
  'numerical stability does not replace it.'],
  'conclusion': [
  'Th2 is proved; the limit part is an open obligation with an explicit '
  'status. Finite-dimensional self-adjointness is the foundation of all '
  'spectral claims of the series.']},
]}

V9 = {'meta': M('V9. Symmetry Reduction',
                'Magnetic translations of the torus and the block '
                'decomposition of the spectrum (theorem Th5)', 'V09'),
 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'Solution 9 of the plan: develop the spinor64 observation (64 spin '
  'structures → 4 Hamiltonians of the reference) into an exact symmetry '
  'reduction — prove that commutation with a group decomposes the '
  'spectrum into blocks, and measure what happens to the symmetry when '
  'vortices are switched on. For the lattice at full flux the correct '
  'group is the magnetic translation group of the torus.',
  'At α = ½ the translations U(1,0) and U(0,1) anticommute (the magnetic '
  'algebra), but their squares A = U(2,0), B = U(0,2) commute with each '
  'other and with H — an abelian subgroup G = ℤ_L × ℤ_L. It yields the '
  'exact reduction.']},
 {'h1': 'Theorem Th5',
  'theorem': {'label': 'Theorem Th5 (block reduction).',
   'text': 'Let H be Hermitian on ℂ^{L²} (torus, α·L ∈ ℤ, no vortices) '
   'and U(m,n) the magnetic translations. If [H, U(m,n)] = 0 for the '
   'generators, then [H, Π_χ] = 0 for the character projectors of '
   'G = ℤ_L × ℤ_L (generated by A, B); H is block-diagonal in the '
   'decomposition of the regular representation, and spec(H) is the '
   'union of the block spectra.',
   'proof': 'Π_χ = (1/|G|)Σ_g χ̄(g)g — spectral projectors of commuting '
   'unitaries; [H, A] = [H, B] = 0 gives [H, Π_χ] = 0, so each '
   'Π_χℂ^{L²} is H-invariant and the direct sum of restrictions '
   'reconstructs H. Numerically (L = 12): ε_Ux = 0.0, ε_Uy = 9.4e-15, '
   '[A,B] = 9.6e-15; the union of six block spectra reproduces the full '
   'spectrum to max|Δλ| = 7.1e-15, off-block elements ≤ 2.0e-15.'}},
 {'h1': 'Measuring the symmetry breaking',
  'paras': [
  'The vortex protocol places vortices randomly: translations stop '
  'commuting with H, ε_g = O(1). The four holonomy classes of twists '
  '(φx, φy) ∈ {0, π}² remain independent Hamiltonians with ⟨r⟩ = '
  '0.588–0.631 — all in the GUE class. This is the lattice analogue of '
  'the reference spinor64 conclusion: the reduction explains the '
  'skeleton of the spectrum, but the arithmetic of the zeros does not '
  'live in the symmetry.',
  'The practical value of Th5 is computational: the block structure '
  'allows independent diagonalization and algebraically explains '
  'degeneracies. But the main value is methodological: “which part of '
  'the spectrum is symmetry and which is arithmetic” is now separated '
  'by measurement, not declaration.'],
  'table': {'caption': 'Table 1. Summary of V9',
   'header': ['Check', 'Value', 'Verdict'],
   'rows': [
    ['ε_Ux (torus, no vortices)', '0.0', 'exact symmetry'],
    ['ε_Uy', '9.4e-15', 'exact symmetry'],
    ['blocks ↔ full spectrum', 'max|Δλ| = 7.1e-15', 'Th5 verified'],
    ['off-block elements', '2.0e-15', 'block-diagonal exact'],
    ['ε_g with vortices', '5.1 (O(1))', 'symmetry broken'],
    ['⟨r⟩ of four twists', '0.588–0.631', 'GUE class']]},
  'ratios': None},
 {'h1': 'Honest remarks',
  'paras': [
  'The reduction group is the abelian core of the magnetic algebra; the '
  'full non-commutative structure (projectors onto irreducible '
  'representations) gives the same blocks at finite size and is not '
  'separately highlighted. For the Hilbert–Pólya program the conclusion '
  'is restrained: the right symmetry structure is necessary but not '
  'sufficient — vortices carrying the arithmetic destroy it.'],
  'conclusion': [
  'Th5 is proved and verified to 1e-15; the symmetry breaking by '
  'vortices is measured. Symmetry explains the skeleton, not the '
  'arithmetic.']},
]}

V10 = {'meta': M('V10. The Inverse Problem: Arithmetic from the Spectrum',
                 'Identifiability of vortex parameters from traces',
                 'V10'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'If arithmetic phases influence the spectrum, the inverse problem '
  'arises: how accurately can the arithmetic be recovered from spectral '
  'data? The plan fixes the protocol: invariants Φ(θ) = (Tr H, …, '
  'Tr H^k), the sensitivity matrix J_ij = ∂Φ_i/∂θ_j, its rank and '
  'conditioning, then an optimization recovery on configurations never '
  'used in tuning.',
  'The answer determines what the spectrum can “encode” at all: if the '
  'rank of J is below the number of parameters, part of the arithmetic '
  'is unidentifiable from the chosen data by definition — however many '
  'statistics we collect.']},
 {'h1': 'Method',
  'paras': [
  'Configurations Nv ∈ {4, 8} on a 12×12 lattice; invariants up to '
  'k = 6 (computed as power sums of eigenvalues); sensitivity by '
  'central differences with step 1e-4. Charge recovery with fixed '
  'positions — Nelder–Mead from three starts; success threshold — '
  'recovery error < 1e-3.',
  'Additionally the separation is measured: the distance between the '
  'invariants of an arithmetic configuration (protocol C3) and a random '
  'one (same positions, random charges) — relative, in the Φ norm.']},
 {'h1': 'Results',
  'theorem': {'label': 'Statement (rank-limited identifiability).',
   'text': 'With k = 6 invariants the rank of J equals 6 for any '
   'configuration; charges are recovered with error ≤ 0.08 at fixed '
   'positions; full identifiability (rank = n_params = 12/24) is '
   'unreachable within this invariant class.',
   'proof': 'The rank cannot exceed the number of invariants k = 6 '
   '(dimension of the image of J); the singular values of J decay over '
   '~5 orders (cond ≈ 8.7e4), so the practical rank is lower. Recovery: '
   'max|Δq| = 0.077 at loss = 0.0149. Arithmetic-vs-random separation: '
   '1.6–3.5 relative units — a signal, not a proof of uniqueness.'}},
 {'h1': 'Honest remarks',
  'paras': [
  'A successful recovery does not prove uniqueness: even at full rank, '
  'distinct configurations may share close invariants (conditioning!), '
  'and a strict result requires a proof of identifiability — a global '
  'injective map θ ↦ spec. The plan warns about exactly this '
  'limitation, and V10 respects it.',
  'The practical conclusion for the program: power traces are the right '
  'carrier of the inverse problem (they enter the Li criterion V15 '
  'through power sums), and extending the invariant class (resolvent '
  'traces, heat traces at several t) is the direct continuation.'],
  'table': {'caption': 'Table 1. Summary of V10',
   'header': ['Quantity', 'Nv=4', 'Nv=8'],
   'rows': [
    ['rank J (k=6)', '6', '6'],
    ['n_params', '12', '24'],
    ['cond(J)', '8.7e4', '8.7e4'],
    ['recovery |Δq|', '0.077', '—'],
    ['arithmetic separation', '1.6–3.5', '—']]},
  'ratios': None},
 {'h1': 'Verdict',
  'paras': [],
  'conclusion': [
  'Identifiability is measured and rank-limited: part of the arithmetic '
  'is invisible to the spectrum from this invariant class in '
  'principle. Charge recovery works; the full inverse problem remains '
  'open.']},
]}

DOCS = {'V6': V6, 'V7': V7, 'V8': V8, 'V9': V9, 'V10': V10}
