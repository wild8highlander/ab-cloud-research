# -*- coding: utf-8 -*-
"""content/en_part1.py — monographs C1–C4 (English series)."""

AUTHOR = "Ishak Khamzatovich Isaev"
AFFIL = "Independent researcher, Nalchik, Kabardino-Balkarian Republic"
SERIES = "Hilbert Polya Bridge · monograph series C1–C8"


def _meta(title, subtitle, vol):
    return {"title": title, "subtitle": subtitle, "author": AUTHOR,
            "affil": AFFIL, "series": SERIES, "volume": vol,
            "version": "1.0.0", "date": "October 10, 2026"}


C1 = {
"meta": _meta("The Identity Function and the Γ-Ladder",
              "Assembling Z_id(t) = e^{iθ(t)}ζ(½+it) from algebraic closures; "
              "criteria K1–K4, K7", "C1"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "This monograph opens the series of eight computational works of the "
 "Hilbert Polya Bridge project. Its subject is a function that stitches "
 "together two branches of arithmetic: the smooth Γ-frame that supplies "
 "the phase, and the zeta factor that carries the zeros. We define the "
 "identity function Z_id(t) = e^{iθ(t)}ζ(½+it), where θ(t) = Im ln Γ(¼+it/2) "
 "− (t/2)lnπ is the continuous Riemann–Siegel phase. The construction is "
 "not postulated: every element is derived from the elementary identities "
 "of the next section, and no free parameter enters anywhere.",
 "The guiding question of campaign C1 is stated honestly: can an "
 "algebraic envelope — the product of a Γ-factor and ζ on the critical "
 "line — generate zeros in any other way than ζ itself does? The measured "
 "answer is negative, and precisely this negative result fixes the "
 "boundary between the graph and the operator for the entire series. "
 "Everything true of Z_id is true by identity; whatever Z_id cannot do, "
 "no rearrangement of the phase can do either.",
 "The methodological frame of the series is explicit: each criterion "
 "receives a code name (K1–K7), an exact threshold and a verdict — "
 "proven, measured or refuted. All derivations, thresholds and numbers "
 "needed for reproduction appear below; the campaign code is under two "
 "hundred lines and has no dependencies beyond mpmath and numpy."]},
{"h1": "T1. The Γ-ladder: three elementary closures",
 "theorem": {"label": "Theorem T1 (Γ-ladder closures).",
  "text": "For all u ∈ ℝ: |Γ(½+iu)|² = π/cosh(πu); |Γ(iu)|² = "
  "π/(u·sinh(πu)); |Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh(2πu).",
  "proof": "The first is Euler's reflection formula Γ(z)Γ(1−z) = "
  "π/sin(πz) at z = ½+iu. The second follows from the same identity in "
  "the limit with the Legendre duplication Γ(z)Γ(z+½) = 2^{1−2z}√π Γ(2z) "
  "at z = iu. The third is the duplication formula at z = ¼+iu: the "
  "modulus of Γ(¼+iu)Γ(¾+iu) reduces to cosh(2πu) up to normalization. "
  "All three closures are verified at dps = 40 with maximal relative "
  "residuals 1.3e-39 – 2.6e-39."},
 "paras": [
 "It matters that the ladder closes elementarily only at the three listed "
 "points of the frame. Our first conjecture — that the single modulus "
 "|Γ(¼+iu)| on the critical line admits a closed hyperbolic form — was "
 "refuted by direct computation: at u = 1 the ratio to the nearest "
 "hyperbolic candidate is 0.765, not 1. This negative result (criterion "
 "K1, refuted) is essential: the phase frame on the line holds only "
 "through the Legendre pair product, and it is the product that enters "
 "Z_id through θ(t). The residuals of all closures are collected in "
 "Table 1."],
 "table": {"caption": "Table 1. Γ-ladder closures (dps = 40, grid u ∈ [0, 4], 401 points)",
  "header": ["Closure", "Max relative residual", "Threshold", "Verdict"],
  "rows": [
   ["|Γ(½+iu)|² = π/cosh πu", "2.59e-39", "1e-30", "proven"],
   ["|Γ(iu)|² = π/(u·sinh πu)", "2.57e-39", "1e-30", "proven"],
   ["|Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu", "1.27e-39", "1e-30", "proven"],
   ["|Γ(¼+iu)| alone (candidate form)", "0.765 (structural mismatch)", "—", "refuted"]],
  "ratios": [0.44, 0.28, 0.12, 0.16]}},
{"h1": "T2. Reality of Z_id and the assembly",
 "theorem": {"label": "Theorem T2 (reality).",
  "text": "On the critical line Im Z_id(t) = 0 for all t; the parity "
  "Z_id(−t) = Z_id(t) holds to the same accuracy.",
  "proof": "ξ(½+it) is real on the line by the symmetry ξ(s) = ξ(1−s) "
  "and the reality of Dirichlet coefficients; θ(t) is odd, so e^{iθ(t)} "
  "rotates ζ(½+it) onto the real axis. Numerically: max|Im Z_id| = "
  "4.9e-29 at dps = 30, maximal parity violation 9.9e-29 — the floor of "
  "multi-precision arithmetic."},
 "paras": [
 "The assembly combines three sources: the Γ-frame gives the phase "
 "(shape), the zeta factor gives the zeros (arithmetic), and the "
 "normalization Ξ_id ≡ ξ(½+it) fixes the scale. One terminological "
 "warning is in order: the expression Riemann relations used in "
 "neighbouring projects refers to bilinear relations for period matrices, "
 "not to the Riemann Hypothesis; we keep the two strictly apart.",
 "The function is computed in two arithmetics: double precision (plots "
 "and statistics) and dps = 25–40 in mpmath (verdicts). The agreement of "
 "the branches serves as an independent control: on t ∈ [0, 200] the "
 "discrepancy never exceeds 1e-14 relative to the magnitude."]},
{"h1": "Results: zeros, Gram points, criteria summary",
 "paras": [
 "The zeros of Z_id on [0, 200] are found by sign-change bisection with "
 "80 refinement steps: 79 zeros, maximal deviation from the mpmath "
 "zetazero table 2.8e-14 (criterion K3). This confirms that the phase "
 "θ(t) moved no zero: the identity graph coincides with the ξ graph on "
 "the line. Gram points g_n (θ(g_n) = nπ) are built by findroot; among "
 "220 points, 4 sign violations occur — the classical Rosenberger–Spira "
 "picture first observed near n = 126 (criterion K7).",
 "Campaign verdicts: K1 — the ladder closes (with one refutation), "
 "K2 — reality proven, K3 — zeros coincide, K4 — argument principle "
 "consistent (details in monograph C2), K7 — Gram points reproduced. "
 "Composite verdict: PASS. The single refuted element is exactly the "
 "one we warned about: the algebraic envelope generates no zeros beyond "
 "those of ζ."],
 "figure": {"path": "figures_hires/{lang}/fig01_zid_{lang}.png",
  "caption": "Fig. 1. The identity function Z(t) on [0, 200]: bisection zeros (copper) and Gram points (rings); the vertical line is the t = 0 axis."},
 "figure2": {"path": "figures_hires/{lang}/fig02_gamma_ladder_{lang}.png",
  "caption": "Fig. 2. Relative residuals of the three Γ-ladder closures: the 1e-39 plateau confirms elementarity of all three forms."},
 "conclusion": [
 "The identity function is built and matches the Riemann Hypothesis in "
 "the block T ≤ 200 without any appeal to zero tables. The main lesson "
 "of C1 for the whole series: the Γ-frame fixes the shape but not the "
 "arithmetic; the road to the operator runs through counting (C2), the "
 "spectrum (C3–C5) and the trace (C4), not through new phase plots."]},
]}

C2 = {
"meta": _meta("The Argument Principle up to T = 1000",
              "Adaptive Turing step, pole calibration, RH verified in the strip",
              "C2"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C2 answers the counting question: how many zeta zeros lie in "
 "the critical strip below a given height T, and do all of them lie on "
 "the critical line? The answer comes from the argument principle with "
 "no appeal to zero tables: the contour (2,0) → (2,T) → (0,T) → (0,0) "
 "bypasses the pole s = 1 from above, and the count N(T) = Δarg ξ / 2π "
 "is compared with the number of on-line zeros found independently.",
 "This setup turns the Riemann Hypothesis into a checkable numerical "
 "equality N_strip = N_line at every height. For T ≤ 1000 the equality "
 "holds at thirteen heights — the main result of C2."]},
{"h1": "T3. The pole calibration lemma",
 "theorem": {"label": "Lemma T3 (pole calibration).",
  "text": "When the pole s = 1 is bypassed from above by a small "
  "semicircle, its argument contribution is −π; hence N(T) = Δarg ξ / 2π "
  "WITHOUT the additive +1.",
  "proof": "ξ'/ξ has a simple pole at s = 1 with residue +1; a clockwise "
  "half-passage contributes −π to Δarg ξ, which exactly compensates the "
  "standard +1 of the Riemann–von Mangoldt formula derived for contours "
  "enclosing the pole. Our first calibration with +1 produced a "
  "systematic unit shift at every height; it was caught by a cross-check "
  "of S(T) against the file and corrected."},
 "paras": [
 "The second trap of the campaign is step aliasing. The adaptive Turing "
 "step with a single leaf condition lost turns on steep segments: at "
 "T = 51.4 the first version returned N = 5 instead of 10. The trap was "
 "caught by cross-checking the residual S(T) against the file count; "
 "the cure is a double leaf condition — |Δarg| ≤ 0.3 AND arc length "
 "≤ h_safe, where h_safe is estimated from bounds on |ζ'/ζ| at the "
 "given height."]},
{"h1": "Method and the arithmetic bridge",
 "paras": [
 "The implementation is two-tier. A fast branch (numpy, double precision) "
 "runs the contour with the adaptive step; a reference branch (mpmath, "
 "dps = 26) recomputes the same contours at selected heights. The "
 "arithmetic bridge at T = 100.07 gives |ΔN| = 2.6e-26 — the count is "
 "not approximately but exactly determined within machine arithmetic. "
 "The anchors agree with the file: at all thirteen heights "
 "N_strip = n_line, maximal residual to the nearest integer 8.3e-25.",
 "The gap distribution is of independent interest: below T = 1000 the "
 "minimal gap is 0.3104, the maximal 6.887, the mean 1.521 — the opening "
 "members of the famous Lehman–Odlyzko sequence. Criterion K5 (the von "
 "Mangoldt counting identity) keeps S(T) within ±1.8 across the interval; "
 "the control points +0.38/+0.34/+0.79/+0.50 reproduce the classical "
 "oscillations."],
 "table": {"caption": "Table 1. Argument-principle anchors (excerpt; full list in data/c2_argument_verdict.json)",
  "header": ["T", "N (strip)", "n on line", "Residual"],
  "rows": [["10.00", "0", "0", "5.1e-28"], ["27.72", "3", "3", "3.2e-27"],
           ["51.37", "10", "10", "0.0"], ["100.07", "29", "29", "0.0"],
           ["199.64", "79", "79", "0.0"], ["500.45", "269", "269", "4.1e-25"],
           ["1000.57", "649", "649", "8.3e-25"]],
  "ratios": [0.25, 0.25, 0.25, 0.25]},
 "figure": {"path": "figures_hires/{lang}/fig03_argument_{lang}.png",
  "caption": "Fig. 1. N(T) (copper) against the smooth count N̄(T) (teal) and the residual S(T) (dashed, right axis): the anchors sit on the curve."},
 "figure2": {"path": "figures_hires/{lang}/fig04_gaps_{lang}.png",
  "caption": "Fig. 2. Nearest-neighbour zero gaps below T = 1000: mean 1.521, minimum 0.3104, maximum 6.887."}},
{"h1": "The second moment Σγ² and conclusions",
 "paras": [
 "Criterion K6 closes the second moment: Σ γ_n² up to T = 1 132 490.66 "
 "matches the formula (T³/6π)(ln(T/2π) − 1/3) with relative deviation "
 "8.8e-7 — without a single fitted constant. The history of the "
 "criterion is instructive: the first version carried a factor error "
 "of 4π³ ≈ 124, found precisely through the mismatch with the data; the "
 "final agreement is a property of the formula, not of the fit.",
 "The verdict of C2: the Riemann Hypothesis is verified in the strip up "
 "to T = 1000 — 649 zeros in the strip, 649 on the line, all residuals "
 "to the nearest integer below 8.3e-25. This is not a proof for all "
 "heights, but an honest boundary below which every component of the "
 "series (phase, counting, zeros) is consistent piece by piece. The next "
 "step is the operator: does a matrix exist whose spectrum reproduces "
 "these heights (campaigns C3–C5)?"]},
]}

C3 = {
"meta": _meta("The H7 Gate Family",
              "52 gates, permutation control, positive controls PC1/PC2", "C3"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C3 is the first spectral projection of the Hilbert–Pólya "
 "programme in our series. The question of criterion H2: does a gate "
 "exist — a vortex-cloud configuration on a 24×24 lattice with π flux "
 "(the self-dual line α = ½) — whose spectrum is identical to the zeta "
 "zero spectrum under the correspondence level n ↔ zero n? The family "
 "spans four protocol handles: vortex number Nv ∈ {0, 2, 8, 16, 32}, "
 "charge q ∈ {0.5, 1.0}, disorder W ∈ {0, 0.5, 1.0} and offset "
 "α ∈ {0.4, 0.5}; 52 unique configurations in total at master seed 96.",
 "The honest geometry of the question matters. Spectral identity is far "
 "stronger than a coincidence of spacing statistics: it requires "
 "correlation +1 between the sequences of levels and heights after "
 "unfolding. Hence, besides point statistics, we build permutation "
 "nulls (cyclic shifts of the zero list) and two positive controls on "
 "which the method must see identity when it exists."]},
{"h1": "Method: unfolding and three statistics",
 "paras": [
 "Both sides are brought to a common unfolding. Levels: polynomial "
 "counting of degree 6 over the central band 0.6 (344 eigenvalues, "
 "window of 200 levels). Zeros: the smooth Riemann–von Mangoldt count. "
 "Three identity statistics: r_H7 — Pearson correlation of the "
 "fluctuations level n ↔ zero n with the ramp removed from both sides; "
 "D_nn — mean nearest-neighbour distance after a global-shift optimum; "
 "KS_sp — the two-sample KS statistic between unfolded consecutive "
 "spacings.",
 "Null distributions: (i) 64 cyclic shifts of the zero list — the pure "
 "null no identity, all one-point statistics agree; (ii) 40 GUE "
 "matrices through the same pipeline — universality without identity. "
 "Positive controls: PC1 — the spinor64 twins, two representatives of "
 "one isospectral orbit (the method must return r = 1.000000000, "
 "D_nn = 2.7e-14; merging multiple levels and a shared piecewise-linear "
 "unfolding were required); PC2 — the graph: the 79 Z_id zeros of C2 "
 "against the file (r = 1.000000000000, D_nn = 1.2e-10). The gap between "
 "the graph and the operator is 9–10 orders of magnitude in D_nn."]},
{"h1": "Results and verdict",
 "paras": [
 "The best gate of the family (Nv = 0, W = 0.5, α = 0.5) yields "
 "r_H7 = 0.226 at p = 0.169; the Bonferroni correction over 52 "
 "comparisons is 0.80. All gates lie inside the null zones: decoys "
 "(random phases) 0.026±0.140, GUE −0.014±0.127. Identity is not found; "
 "the verdict on H2 is NO — but now as a measured result with positive "
 "controls: the method sees identity at the 1e-14 level when it exists "
 "and sees it in none of the 52 configurations.",
 "The only statistically noticeable signal — clustering ⟨r⟩ = 0.32 of "
 "the clean lattice without vortices (below Poisson) — is a "
 "localization effect, not kinship with ζ. It disappears at Nv ≥ 8, "
 "where the GUE plateau begins (⟨r⟩ = 0.60). The campaign summary and "
 "the full 52-gate table ship in data/c3_gates_table.csv; the verdict "
 "in c3_gates_verdict.json."],
 "table": {"caption": "Table 1. Campaign C3 summary",
  "header": ["Quantity", "Value", "Meaning"],
  "rows": [
   ["Best r_H7", "0.226 (p = 0.169, Bonferroni 0.80)", "no identity"],
   ["Decoys / GUE null", "0.026±0.140 / −0.014±0.127", "null zones"],
   ["PC1 spinor64 twins", "r = 1.000000000, D_nn = 2.7e-14", "method sees identity"],
   ["PC2 graph Z_id ↔ file", "r = 1.000000000000, D_nn = 1.2e-10", "method sees identity"],
   ["Graph↔operator gap", "9–10 orders (in D_nn)", "the master scale of the series"]],
  "ratios": [0.28, 0.44, 0.28]},
 "figure": {"path": "figures_hires/{lang}/fig05_gates_{lang}.png",
  "caption": "Fig. 1. r_H7 across the 52 gates: grey band — null zone, gold line — best gate 0.226, copper lines — positive controls ±1."}},
{"h1": "Conclusions",
 "paras": [
 "C3 fixes the scale of the problem: a desert of nine to ten orders lies "
 "between the graph and the operator, crossed by no protocol handle. "
 "This is not the end of the programme but its calibration: every new "
 "handle (C5) and every new metric (C4 — the trace projection) must now "
 "be compared against this scale. The working hypothesis of the series: "
 "if identity is possible at all, it will require not a rearrangement "
 "of phases but a new constructive principle — as campaign C6 also "
 "suggests, where prime arithmetic lives exactly in the flow but not "
 "in the spectrum."]},
]}

C4 = {
"meta": _meta("The Trace Formula: Tr e^{−uH} versus the Explicit Formula",
              "Hadamard identity, the prime weight Λ(n)/√n, the trace projection of the H2 gap",
              "C4"),
"sections": [
{"h1": "Introduction and setting",
 "paras": [
 "Campaign C4 is the next step of the map after the statistical (C3) and "
 "arithmetic (C6) projections: the comparison of the heat trace of an "
 "operator with the Guinand–Weil explicit formula. For a hypothetical "
 "Hilbert–Pólya operator H with spectrum {γ_n}, the trace formula should "
 "read Tr e^{−xH} = Σ e^{−xγ_n} = [smooth Γ-terms] − Σ Λ(n)/√n·x/(x²+ln²n) "
 "— the heat trace must carry the weight of primes. We derive the "
 "formula rigorously, verify it for the operator H_ξ = diag(±γ_n), and "
 "then measure what survives for the lattice gates.",
 "All constants are derived; none is fitted. The only calibration step "
 "is the verification of the identity itself against the data, with the "
 "threshold set by machine precision rather than convenience."]},
{"h1": "T6. The Q(a) identity and the trace formula",
 "theorem": {"label": "Theorem T6 (trace formula for H_ξ).",
  "text": "Let Q(a) := Σ_{γ>0} 2a/(a²+γ²). Then (i) Q(a) = ζ'/ζ(½+a) + "
  "1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀, where B = ξ'(0)/ξ(0) = "
  "½ln(4π) − 1 − γ/2 and C₀ = Σ_{γ>0} 1/(¼+γ²) = −B; (ii) for x > 0, "
  "K(x) := Tr e^{−xH_ξ} = (1/π)∫₀^∞ Q(a) sin(ax) da, and for a > ½ the "
  "series ζ'/ζ(½+a) = −ΣΛ(n)/n^{½+a} contributes the weight Λ(n)/√n.",
  "proof": "(i) is the Hadamard product for ξ: ξ'/ξ(s) = B + "
  "Σ_ρ[1/(s−ρ)+1/ρ] with B = ξ'(0)/ξ(0); pairing ρ with ρ̄ turns the sum "
  "into Q(a) + C₀, and the rest is the decomposition ξ'/ξ = 1/s + "
  "1/(s−1) − ½lnπ + ½ψ(s/2) + ζ'/ζ. (ii) uses 2a/(a²+γ²) = 2∫₀^∞ "
  "e^{−γt}sin(at)dt and sine-transform inversion; absolute convergence "
 "on both sides justifies the interchange of summation and integration."},
 "paras": [
 "As a by-product, the classical identity C₀ = 1 + γ/2 − ½ln(4π) is "
 "confirmed: the file sum yields 0.023095708966 — twelve digits coincide "
 "with −B. This is a beautiful built-in control: a constant computed "
 "from a two-million-entry zero list equals a constant made of four "
 "elementary numbers.",
 "The right-hand side of the trace formula splits into three parts: "
 "T1 — the Γ-geometry (integral of the closed form on [0, 1.5]); T2 — "
 "the prime part (the exact transform −ΣΛ(n)/√n·Im[e^{−A(ln n−ix)}/"
  "(ln n−ix)]); T3 — the smooth terms with exact Si/Ci forms. T2 is the "
 "weight of primes: on the grid x ∈ [0.08, 3] its share of K(x) reaches "
 "−3…−12%, and the entire fluctuation about the smooth part belongs to "
 "it alone."]},
{"h1": "M0/M1: calibration and the positive control",
 "paras": [
 "M0. Identity (i) is verified on the grid a ∈ {0.10 … 3.00}: the direct "
 "file sum over 2 001 052 zeros (with an analytic tail from the smooth "
 "density) against the closed form via mpmath gives max|ΔQ| = 1.7e-12. "
 "The formula is calibrated — all signs, constants and branches fixed.",
 "M1. The trace formula for H_ξ: the direct sum Σ e^{−xγ} against "
 "(1/π)∫Q sin on x ∈ [0.08, 3] agrees to a maximal absolute difference "
 "of 1.2e-5 — the numerical floor of the quadrature (for x ≥ 1 the "
 "value of K(x) itself is already ~1e-6). In the informative range "
 "x ≤ 0.35 the relative agreement is 1e-6 … 1e-4. Theorem T6 is "
 "verified: the heat trace of the zero operator carries the prime "
 "weight explicitly."],
 "figure": {"path": "figures_hires/{lang}/fig06_trace_{lang}.png",
  "caption": "Fig. 1. K(x): the direct sum (copper) against the explicit formula (teal) — agreement down to the quadrature floor across the range."},
 "figure2": {"path": "figures_hires/{lang}/fig07_parts_{lang}.png",
  "caption": "Fig. 2. Anatomy of K(x): the full curve, the prime part T2 (weight Λ/√n), the Γ-part T1 and the smooth part T3."}},
{"h1": "M2: the trace projection of the gates and the verdict",
 "paras": [
 "For the gates the same machinery applies: a 200-level unfolded window, "
 "the heat-trace fluctuation D(u) = Σe^{−u x_n} minus the smooth part, "
 "and the correlation r_EF with the prime comb P(u) = "
 "ΣΛ(n)/√n·u/(u²+ln²n) at fixed scale (the rank correspondence of the "
 "windows fixes the dual axis; scale optimisation is excluded as a "
 "source of inflation). Positive control PC0: the same window taken "
 "from the zeros themselves gives r = +0.9998 with a relative residual "
 "of 2.1% — the pipeline sees the comb when the spectrum is the zeros. "
 "The gates: r_EF from −0.93 to +1.00 against null clouds of surrogate "
 "0.00±0.39, Poisson 0.08±0.80, GUE 0.43±0.71 — no gate leaves the null "
 "zone; the best relative residual is 6.7% against 2.1% for PC0 — a "
 "gap of ≈0.5 orders in the trace metric (the metric is conservative: "
 "the surrogate null is wide).",
 "The verdict of C4 is double. Positive: the explicit formula and the "
 "trace theorem T6 are verified with full control — the weight of "
 "primes is now part of the package, not a literature reference. "
 "Negative: in the trace projection the H2 gap is confirmed a third "
 "independent way; lattice gates carry no Λ-weights, and GUE "
 "universality erases the arithmetic from the trace just as it erases "
 "it from the spacing statistics."],
 "table": {"caption": "Table 1. Campaign C4 summary",
  "header": ["Block", "Quantity", "Verdict"],
  "rows": [
   ["M0", "|ΔQ| ≤ 1.7e-12", "identity calibrated"],
   ["M1", "|ΔK| ≤ 1.2e-5 (absolute)", "T6 verified"],
   ["PC0 (zeros window)", "r = +0.9998, residual 2.1%", "method sees the prime weight"],
   ["52 gates", "r_EF −0.9…+0.98, null zone", "no prime weight"],
   ["Gap (trace metric)", "≈ 0.5 orders by residual", "H2 — NO, measured"],
   ["C3 reproduction", "|Δmean_spacing| = 1.4e-16", "bit-for-bit"]],
  "ratios": [0.26, 0.42, 0.32]},
 "figure3": {"path": "figures_hires/{lang}/fig08_rEF_{lang}.png",
  "caption": "Fig. 3. r_EF across the 52 gates: grey band — surrogate null ±0.39, copper line — PC0 +0.9998."}},
{"h1": "Conclusions",
 "paras": [
 "The trace formula completes the triad of projections of the H2 gap: "
 "rank correlation (C3, 9–10 orders), the ψ-ladder (C6, null zone) and "
 "now the heat trace (C4, ≈1 order in the window metric). All three "
 "converge on one statement: the arithmetic of primes lives in the "
 "zeros and does not transfer to the spectrum of a local resonator by "
 "any rearrangement of phases. For the future this means that a "
 "hypothetical Hilbert–Pólya operator must be nonlocal by nature — a "
 "question beyond the lattice family, left honestly open."]},
]}

DOCS = {"C1": C1, "C2": C2, "C3": C3, "C4": C4}
