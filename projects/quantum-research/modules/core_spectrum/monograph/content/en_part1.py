# -*- coding: utf-8 -*-
"""content/en_part1.py — monographs V1–V5 (English series)."""
from content.common import _meta

AUTHOR = 'Ishak Khamzatovich Isaev'
AFFIL = 'Independent researcher, Nalchik, Kabardino-Balkarian Republic'
SERIES = 'AB Research Program · monograph series V1–V19'
DATE = 'October 10, 2026'


def M(title, subtitle, vol):
    return _meta(title, subtitle, vol, AUTHOR, AFFIL, SERIES, DATE)


V1 = {'meta': M('V1. Blind Spectral Experiment',
                'Separating calibration from test: what survives when the '
                'zeros are hidden', 'V01'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'The Hilbert–Pólya program demands that a spectral object not only '
  'reproduce the statistics of the zeta zeros but predict what it was '
  'never shown. In the AB-cloud construction the phases are tied to the '
  'ordinates γ_n, so the central validity question is data leakage: how '
  'much of the observed agreement is explained by geometry, and how much '
  'by feeding known zeros into the construction. Until this is answered, '
  'every “match” remains an internal consistency of the design.',
  'This campaign turns the blind protocol of the plan into a computation. '
  'The set of ordinates is split into disjoint parts G_cal and G_test; '
  'the gate parameters are chosen using the calibration part only; the '
  'test part is opened once, after the parameters are frozen. The split '
  'is deterministic and its hygiene is guaranteed by the fact that the '
  'test ordinates take part neither in the configuration choice nor in '
  'the spectrum-to-height mapping.']},
 {'h1': 'Method',
  'paras': [
  'Calibration sweeps eight protocol gate configurations (master seed '
  '96…103, lattice 24×24, Nv = 16, q = 1, W = 0.5, α = ½). For each '
  'configuration a window of 200 unfolded levels is built; the '
  'calibration score is the rank correlation between window increments '
  'and calibration ordinate increments taken through the smooth '
  'Riemann–von Mangoldt count N̄(γ) = γ/2π·ln(γ/2πe) + 5/8. The best '
  'configuration is frozen.',
  'On the blind test the window of the frozen gate is mapped to '
  'predicted ordinate increments through the local density dN̄/dγ; RMSE '
  'against the actual increments and the rank correlation r_test are '
  'measured. The honest null is the permutation distribution: 200 '
  'shuffles of the predicted increments define the null zone. The '
  'significance threshold is three null sigmas.'],
  'table': {'caption': 'Table 1. Protocol and results of V1',
   'header': ['Quantity', 'Value', 'Status'],
   'rows': [
    ['Calibration G_cal', '600 ordinates, 8 configurations', 'protocol'],
    ['Test G_test', '600 other ordinates, 1 run', 'blind'],
    ['r_cal (best)', '0.085', 'selection over 8'],
    ['r_test', '0.006', 'null zone'],
    ['Permutation null', '−0.002 ± 0.066', '200 permutations'],
    ['z-score', '0.09', 'no signal']]},
  'ratios': None},
 {'h1': 'Results and interpretation',
  'paras': [
  'The best calibration value r_cal = 0.085 is itself small: even on its '
  'own data the rank agreement of a gate window with the ordinates is '
  'random. The selection bias (maximum over eight configurations) '
  'explains this value entirely. On test, r_test = 0.006 against the '
  'permutation null −0.002 ± 0.066: z = 0.09 — no transfer at all.',
  'This measurement agrees with verdict H2 of the reference Hilbert '
  'Polya Bridge series (best r_H7 = 0.226 over 52 gates) and strengthens '
  'it protocol-wise: the absence of individual agreement is now '
  'established not on training data but on data the algorithm never '
  'saw. The negative result is not a failure but the hygiene norm of the '
  'whole program: it blocks self-deception at stages V6 and V15.'],
  'conclusion': [
  'The blind protocol is installed and passed in the strictest sense: '
  'the machinery works, the null zone is honest, there is no signal. '
  'All subsequent campaigns rely on this protocol as the foundation of '
  'validity.']},
]}

V2 = {'meta': M('V2. Arithmetic Null Models',
                'A pre-registered battery of statistics against five '
                'families of null models', 'V02'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'GUE statistics occur widely in systems unrelated to the zeta '
  'function: universality is an attractor, not evidence. Before '
  'attributing arithmetic specificity to AB-cloud, one must measure what '
  'the mere chaos of the lattice produces. Null models destroy the '
  'arithmetic while keeping the geometry and scales.',
  'The key discipline is pre-registration: the statistic vector '
  'S = (⟨r⟩, Σ²(L), Δ₃(L), K(t), D_KS) was fixed before the runs, no '
  'metric is chosen post hoc, and the multiple-testing correction is '
  'Bonferroni over five families. This is a direct implementation of '
  'Solution 2 of the plan.']},
 {'h1': 'Method',
  'paras': [
  'Families: M0 — protocol gates (Nv ∈ {0,2,8,16,32}, q = 1, W = 0.5, '
  'α = ½); N1 — all link phases replaced by uniform U(−π, π]; N3 — '
  'geometry without vortices (Hofstadter plus disorder); N4 — random '
  'vortex positions outside the protocol; plus reference ensembles GUE, '
  'GOE and Poisson of the same size 576. The full vector S is measured '
  'on a 200-level unfolded window for each model.',
  'The D_KS reference is ensemble-based: the pooled {r_n} sample of '
  'sixteen GUE matrices (3168 values) serves as the empirical GUE '
  'reference instead of a spacing surmise — this removes small-window '
  'systematics.'],
  'table': {'caption': 'Table 1. Model ladder (⟨r⟩ and D_KS to GUE)',
   'header': ['Model', '⟨r⟩', 'D_KS → GUE', 'Class'],
   'rows': [
    ['M0 AB-cloud', '0.6093', '0.0499', 'GUE'],
    ['N1 random phases', '0.5837', '0.0925', 'GUE'],
    ['N3 no vortices', '0.2733', '0.5518', 'intermediate'],
    ['N4 random positions', '0.6181', '0.0492', 'GUE'],
    ['reference GUE', '0.5984', '0.0622', 'GUE'],
    ['reference GOE', '0.5256', '0.1622', 'GOE'],
    ['reference Poisson', '0.4198', '0.3150', 'Poisson']]},
  'ratios': None},
 {'h1': 'Results and interpretation',
  'paras': [
  'AB-cloud falls into the GUE class together with N1 and N4: the vortex '
  'mechanics is sufficient for chaos but not specific — exactly what '
  'universality predicts. N3 (no vortices) stays intermediate: half '
  'flux alone does not fully chaotise a finite lattice. The reference '
  'ladder Poisson → GOE → GUE is reproduced, validating the battery '
  'itself.',
  'Hence the methodological constraint of the series: ⟨r⟩ and D_KS '
  'carry no arithmetic information — specificity must be sought only in '
  'arithmetic-sensitive trace-level metrics (V7) and in the inverse '
  'problem (V10). This feature split is the central methodological '
  'output of the plan, and V2 delivers it.'],
  'conclusion': [
  'The pre-registered battery is built; the class of AB-cloud is GUE, '
  'as for any sufficiently chaotic vortex lattice. Any further claim '
  'about arithmetic must pass through trace metrics.']},
]}

V3 = {'meta': M('V3. Critical Line Scan',
                'A parametric experiment σ ∈ [0,1] with a placebo control',
                'V03'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'The AB-cloud description claims that the critical line σ = ½ is '
  'optimal for the spectral statistics. The plan demands turning this '
  'claim into a strict reproducible parametric experiment: define how σ '
  'enters, scan D(σ) on a grid, and check the stability of any minimum '
  'across seeds. Special care is needed because ζ vanishes on the line '
  'itself — a weight built directly on the ordinates diverges to −∞ and '
  'would make a “minimum at ½” an artifact of the definition.',
  'The ambiguity is removed before the runs: vortex heights are assigned '
  'to midpoints between consecutive ordinates γ̃_k = (γ_k + γ_{k+1})/2, '
  'where |ζ| is finite on the whole strip 0 ≤ σ ≤ 1; the vortex weight '
  'is q_k(σ) = log|ζ(σ + iγ̃_k)|. The curve D(σ) = D_KS({r_n(σ)}, GUE) '
  'is measured on an 11-point grid with three seeds; the placebo uses '
  'the same weights from permuted ordinates.']},
 {'h1': 'Method and result',
  'paras': [
  'For each σ the 24×24 lattice is assembled with σ-dependent charges; '
  'a 200-level unfolded window is compared against the ensemble GUE '
  'reference of V2. The curvature at mid-strip is estimated by the '
  'second difference C_h = D(½−h) − 2D(½) + D(½+h) with h = 0.1.',
  'Result: the curve D(σ) is flat within the seed spread; the observed '
  'minimum sits near σ ≈ 0.8 and is not reproduced by the placebo; '
  'C_h < 0 — there is no local minimum at ½.'],
  'table': {'caption': 'Table 1. The curve D(σ) (mean over 3 seeds)',
   'header': ['σ', 'D_KS', 'σ', 'D_KS'],
   'rows': [
    ['0.0', '0.0732', '0.6', '0.0476'],
    ['0.1', '0.0767', '0.7', '0.0700'],
    ['0.2', '0.0663', '0.8', '0.0422'],
    ['0.3', '0.0852', '0.9', '0.0793'],
    ['0.4', '0.0984', '1.0', '0.0942'],
    ['0.5', '0.0916', '—', '—']]},
  'ratios': None},
 {'h1': 'Honest remarks and verdict',
  'paras': [
  'The negative verdict does not refute the Hilbert–Pólya program — it '
  'refutes the specific claim “σ = ½ is optimal in D_KS” for this weight '
  'design. Alternative entries (weights from |ζ|², from the logarithmic '
  'derivative, nonlinear σ in the phases) remain open options and need '
  'their own blind validation under protocol V1.',
  'The value of the campaign is the discipline: a minimum found without '
  'a placebo and without a fixed protocol would almost surely have '
  'become a false “confirmation” of the critical line. V3 records: in '
  'this construction the specificity of the line is absent — and this '
  'is measured.'],
  'conclusion': [
  'The scan follows the full protocol (grids, seeds, placebo); there is '
  'no minimum at σ = ½. The optimality claim for the critical line in '
  'AB-cloud is withdrawn to status “not confirmed”.']},
]}

V4 = {'meta': M('V4. Strict Operator Passport',
                'Hermiticity, reality of the spectrum and chirality of '
                'H_L (theorem Th1)', 'V04'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'Before spectral properties can be proved, the object must be defined '
  'without reference to an implementation. The passport fixes: state '
  'space ℂ^{L×L} (open boundaries — a bounded operator with full '
  'domain); explicit matrix elements: Landau phases φ_x = 2πα·iy on '
  'x-links, vortex differences φ_y = Σ_k (q_k/2)(θ_j − θ_i) on y-links, '
  'on-site potential V_i = Σ_k q_k·W/(r²/N + 1) + ε_i; open/torus '
  'boundaries.',
  'The passport checks (P1–P4) are consequences of the definition, not '
  'implementation tests: hermiticity H[i,j] = conj H[j,i] is built in, '
  'reality of the spectrum follows from the spectral theorem, and the '
  'chiral pairing λ ↔ −λ at α = ½, W = 0 follows from bipartiteness of '
  'the lattice (two-coloring by parity of ix + iy).']},
 {'h1': 'Theorem Th1',
  'theorem': {'label': 'Theorem Th1 (hermiticity and reality).',
   'text': 'For any choice of vortices, W, α and boundaries the operator '
   'H_L defined above satisfies H_L = H_L†; hence spec(H_L) ⊂ ℝ. If '
   'α = ½ and W = 0, the lattice is bipartite and spec(H_L) is '
   'symmetric: λ ∈ spec ⇒ −λ ∈ spec.',
   'proof': 'Every off-diagonal element comes as a pair H[i,j] = −t·e^{iφ}, '
   'H[j,i] = −t·e^{−iφ} = conj H[i,j] — hermiticity by construction; the '
   'spectral theorem gives reality. Bipartiteness: at W = 0 the diagonal '
   'is zero and every link joins opposite parity classes, so in the '
   '(even, odd) basis H = [[0, B], [B†, 0]] and the spectrum is '
   'symmetric. Numerically: max‖H−H†‖ = 0.0, max‖Hv−λv‖ = 8.8e-15, '
   'pairing 8.2e-15.'}},
 {'h1': 'Results',
  'paras': [
  'The passport battery covers L ∈ {12, 16, 24, 32} and four handle '
  'variants (vortices, disorder, α = 0.4). All checks P1–P4 pass: '
  'hermiticity is exact (a zero residual — a consequence of the explicit '
  'formula in complex arithmetic), eigenpair residuals are at LAPACK '
  'machine level, and the chiral pairing is at the same level in the '
  'bipartite case.',
  'Crucially, the passport separates the proved from the measured: Th1 '
  'is proved for all parameters at once; the numerical checks merely '
  'guard against implementation errors. This is the model of the '
  '“proven” status in the honesty discipline of the package.'],
  'table': {'caption': 'Table 1. Passport maxima',
   'header': ['Check', 'Battery maximum', 'Threshold', 'Verdict'],
   'rows': [
    ['P1 ‖H−H†‖_max', '0.0 (exact)', '1e-12', 'proven'],
    ['P2 reality', 'eigvalsh — real', '—', 'proven'],
    ['P3 pairing λ↔−λ (W=0)', '8.2e-15', '1e-12', 'proven'],
    ['P4 ‖Hv−λv‖', '8.8e-15', '1e-11', 'proven']]},
  'ratios': None},
 {'h1': 'Honest remarks',
  'paras': [
  'The passport also fixes the boundary: Th1 statements are '
  'finite-dimensional. Self-adjointness of the limiting operator as '
  'L → ∞ is a separate task (V8, obligation O03); numerical hermiticity '
  'of an infinite-dimensional object does not follow from it. Also, '
  'chirality requires W = 0: on-site disorder destroys it, which is a '
  'property of the symmetry class AIII, not a defect.'],
  'conclusion': [
  'The operator is defined unambiguously; Th1 is proved and verified to '
  'machine precision. The passport is the mandatory anchor of all '
  'subsequent campaigns.']},
]}

V5 = {'meta': M('V5. The Controlled Limit L → ∞',
                'Three kinds of convergence and the empirical error law '
                'e(L)', 'V05'), 'sections': [
 {'h1': 'Problem statement',
  'paras': [
  'The plan demands checking not only convergence of statistics but '
  'convergence of the spectral object itself. Three numerically feasible '
  'kinds are implemented: (C1) level convergence — agreement of '
  'individual eigenvalues in the common window |E| ≤ 1.5 as L grows; '
  '(C2) projector convergence — overlap of spectral projectors under a '
  'boundary-condition perturbation inside one space; (C3) trace '
  'convergence — the relative error of Tr e^{−tH²}. Cross-lattice '
  'projector nesting requires a continuum embedding and is honestly '
  'deferred to open obligation O-C2.',
  'The family is made vortex-nested: positions are defined on the '
  'reference lattice 12×12 and scaled with L, so the physical vortices '
  'are the same for every member. The error law e(L) is fitted against '
  'the candidates a·L^{−p}, b/log L, c·L^{−p}·log^q L by log-space '
  'least squares.']},
 {'h1': 'Method',
  'paras': [
  'Sizes L ∈ {12, 16, 20, 24, 32, 40, 48}; Gaussian window t = 0.1; '
  'reference — the largest lattice 48×48 (N = 2304). For C2 the '
  'projector overlap is measured between the open operator and the '
  'operator with a small torus twist ε = 0.02 at L = 24: both act on '
  'ℂ^{576}, so the comparison is correct without embeddings.',
  'Level matching C1 is done by order inside the window: the sorted '
  'level sequences of both lattices are compared elementwise — the '
  'standard finite-size protocol, not claiming a one-to-one level '
  'correspondence.']},
 {'h1': 'Results',
  'theorem': {'label': 'Statement (empirical error law).',
   'text': 'The relative trace error e(L) = |Tr e^{−tH_L²} − '
   'Tr e^{−tH_48²}|/Tr e^{−tH_48²} follows a power law e(L) ≈ a·L^{−p} '
   'with p ≈ 0.86 and R² ≈ 0.80 on L ∈ [12, 40].',
   'proof': 'Least squares in (log L, log e): slope −0.86 ± 0.03, '
   'R² = 0.80. The candidate b/log L fits systematically worse; the '
   'logarithmic correction c·L^{−p}·log^q L does not improve R². '
   'Values: e(12) = 0.94, e(24) = 0.75, e(40) = 0.30.'},
  'paras': [
  'The projector overlap under the BC perturbation ε = 0.02 gives a mean '
  'overlap of 0.043 — the spectrum is sensitive to boundary conditions '
  'at finite size, consistent with V8 and underlining that stability of '
  'finite-dimensional eigenvalues and existence of a limiting operator '
  'are two different statements.'],
  'table': {'caption': 'Table 1. Level and trace errors',
   'header': ['L', 'e_levels (C1)', 'e_trace (C3)'],
   'rows': [
    ['12', '9.4e-1', '9.4e-1'],
    ['16', '8.9e-1', '8.9e-1'],
    ['24', '7.5e-1', '7.5e-1'],
    ['32', '5.5e-1', '5.5e-1'],
    ['40', '3.0e-1', '3.0e-1']]},
  'ratios': None},
 {'h1': 'Honest remarks',
  'paras': [
  'A power law with p < 1 is slow convergence; extrapolation beyond '
  'L ≤ 48 remains an estimate, not a proof: “excellent approximation '
  'quality on computed sizes does not prove convergence as L → ∞” is a '
  'direct requirement of the plan. Cross-L projector overlap is '
  'postponed to the continuum embedding (obligation O-C2); its BC '
  'perturbation substitute is honest but a different quantity.'],
  'conclusion': [
  'The empirical error law is established and published together with '
  'the limits of its status. The limit L → ∞ remains an open '
  'mathematical obligation of the program.']},
]}

DOCS = {'V1': V1, 'V2': V2, 'V3': V3, 'V4': V4, 'V5': V5}
