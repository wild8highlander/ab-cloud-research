#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""content/en_part4.py — Monograph 2.0 «The Operator That Almost Exists»
(English edition). Same DOCS contract as part1–3."""

AUTHOR = "Ishak Khamzatovich Isaev"
AFFIL = "Independent researcher, Nalchik, Kabardino-Balkarian Republic"
SERIES = "Hilbert Polya Bridge · monographs v2.0"
DATE = "October 12, 2026"
VERSION = "2.0.0"


def _meta(title, subtitle, vol):
    return {"title": title, "subtitle": subtitle, "author": AUTHOR,
            "affil": AFFIL, "series": SERIES, "volume": vol,
            "version": VERSION, "date": DATE}


V2 = {
"meta": _meta("The Operator That Almost Exists",
              "Eight new campaigns C9–C16, theorems T11–T18, and the "
              "boundary of the Hilbert–Pólya program after v1.0", "v2.0"),
"sections": [
{"h1": "Introduction: what changed since v1.0",
 "paras": [
 "Version 1.0 built a complete numerical laboratory for the Hilbert–Pólya "
 "program: eight campaigns C1–C8, ten theorems T1–T10, 87 gates and three "
 "independent projections of a single gap H2. The v1 answer was honest and "
 "measured: the resonator is built and tuned (self-adjointness, GUE class, "
 "Dirac dynamics — YES); the zeros are encoded, not generated (spectral "
 "identity and primes-in-operator — NO, each with positive controls); and "
 "the prime weight Λ(n)/√n provably lives in the heat trace of the zero "
 "operator (T6, |ΔK| ≤ 1.2e-5).",
 "The v1 roadmap named the directions able to move the main measured gap: "
 "nonlocal trace constructions (the T6 lesson), stitching the statistical "
 "and coding branches, a number-theoretic explanation of the α = 1/3 zero "
 "modes, and extending the verified band. Version 2.0 executes all five "
 "items and adds five new measurements: blind campaigns, an anomaly hunt "
 "outside the GUE attractor, transferring the pipeline to Dirichlet "
 "L-functions, a quantum-information layer, and an open challenge with a "
 "public metric.",
 "The honesty discipline is strengthened: in v2 the package uses NO "
 "external data file at all — the zeta zeros are computed by mpmath inside "
 "the package (the data/zeros/ cache of 800 zeros is bit-reproducible), "
 "and every metric convention is documented. Four errors and oversights "
 "were found-and-fixed in v2, including the Hadamard constant in the v1 "
 "shipped code; all are published in the honesty ledger (section 9).",
 "The v2 summary in one sentence: **the operator almost exists** — the "
 "primitive with the prime weight in its trace is built exactly and made "
 "arbitrarily nonlocal (C9/T11); arithmetic entered the lattice spectrum "
 "for the first time through the counting law of zero modes (C11/T13); "
 "the H2 gap turned out to be a universal property of the L-function "
 "class (C15/T17); and every time the wall passes through locality, not "
 "through the trace."]},
{"h1": "C9/T11. The nonlocal primitive: the trace knows the zeros exactly",
 "paras": [
 "The T6 lesson was that the heat trace of the operator stitched from the "
 "zeros carries the prime weight exactly: K(x) = Σ e^{−xγ} = "
 "(1/π)∫₀^∞ Q(a)sin(ax) da, where Q(a) unfolds into the prime comb "
 "Λ(n)/√n through ζ'/ζ for a > ½. Roadmap item R1 asked: can one build a "
 "family of operators whose trace carries this weight BY CONSTRUCTION, "
 "not through the lattice — and does that move r_EF out of the null "
 "cloud of gates?",
 "The first result of C9 is theorem T11, and it flips the question. "
 "**Theorem T11 (heat-trace uniqueness).** If Tr e^{−xH} = "
 "(1/π)∫Q(a)sin(ax) da for all x > 0, then spec H = {±γ_n}. The proof is "
 "three lines: both sides are Laplace–Stieltjes transforms of measures on "
 "(0,∞); by uniqueness the measure is determined by the trace; since "
 "(1/π)∫2a·sin(ax)/(a²+γ²)da = e^{−xγ}, the measure is the counting "
 "measure of the zero set. The architectural corollary: the prime weight "
 "in the trace is not decoration — it is the spectral measure itself; "
 "while nonlocality is achievable arbitrarily.",
 "The C9 family realizes this measurably: N1 — H_ξ = diag(±γ) (control); "
 "N2 — the DCT twin O·diag(γ)·Oᵀ with a deterministic dense orthogonal "
 "conjugation; N3 — the QR twin with a chaos seed independent of the "
 "zeros; N4 — truncated Berry–Keating xp (the outside-the-lattice "
 "candidate); N5 — the multiplicative kernel Λ(lcm(m,n))/√mn with the "
 "prime weight in the kernel itself. The v2 convention (unfolded-vs-"
 "unfolded, documented in docs/v2) makes the control honest: an "
 "isospectral twin must give r_H7 = 1.000 — and it does.",
 "Result: N2/N3 give r_H7 = 1.000000 and r_EF(fluct) = 0.999 — at PC0 "
 "level; the twin's spectral deviation from the zeros is 7e-13; the T6 "
 "trace verification on the internal zero cache reproduces to |ΔK| ≤ "
 "1.8e-6. In contrast, Berry–Keating (r_H7 = 0.047, z ≈ 0.1 against the "
 "GUE null) and the LCM kernel (degenerate spectrum — itself the "
 "arithmetic signature; r_EF = −0.96) stay in the null zones. Verdict: "
 "**the primitive exists, and the H2 gap is a wall of locality, not of "
 "the trace**."]},
{"h1": "C10/T12. Phase coding: hard co-location and its limit",
 "paras": [
 "Campaign C6 showed: the prime flow Φ_p = ½ln p composites exactly "
 "((Φ_p,Φ_q) ≡ Φ_pq, 1.35e-14), but the spectrum does not see the "
 "coding. Roadmap R2 demanded phase configurations OBLIGED to satisfy "
 "co-location. C10 solves this constructively and obtains a "
 "classification along the way.",
 "**Theorem T12 (classification).** Any phase system Φ: primes → ℝ/2πℤ "
 "with the identity Φ_pq ≡ Φ_p + Φ_q (mod 2π) is a homomorphism from the "
 "free abelian group ⟨p⟩; it is arbitrary on generators, and its "
 "ln-like normal form is Φ_p = 2π{β ln p}. For the characteristic case "
 "Φ_p = π·χ₄(p) the system takes values {0, π} and turns out "
 "**gauge-trivial** in the lattice overlay channel: e^{±iπ} = −1 flips "
 "every y-bond, and the transformation ψ → (−1)^y ψ removes the coding "
 "entirely (spectra coincide to 8.4e-15 — measured). The only non-gauge "
 "class is β·ln p.",
 "Measurement: gates with a site-linked overlay Φ_p (prime ↔ site index; "
 "a row-uniform overlay is pure gauge and does not change the spectrum — "
 "also measured during debugging). The hard co-location condition holds "
 "at machine zero (4.4e-16) for ANY β — by construction, before the "
 "spectrum runs. The spectral answer: r_H7 ≤ 0.092 across the whole "
 "β-grid of 11 values (best p = 0.015, Bonferroni 0.20), the GUE class "
 "unchanged (⟨r⟩ = 0.58–0.63). Verdict: **universality erases even hard "
 "codings** — consistent with M3 of v1, but now on the class of systems "
 "for which co-location is an identity, not an approximation."]},
{"h1": "C11/T13. The arithmetic bridge: zero modes at α = 1/3",
 "paras": [
 "The T9 observation (v1): at α = 1/3 there are zero modes on tori "
 "L ≡ 0 (mod 4) — 18 at L = 12, 42 at L = 24. The roadmap demanded the "
 "bridge «arithmetic L ≡ 0 (mod 3) → Dirac index». C11 builds a clean "
 "laboratory: the Kähler–Dirac (staggered) operator in the γ₅-Hermitian "
 "form H = ε·D + m with Landau flux α; the torus requires α·L ∈ ℤ — at "
 "α = 1/3 this is exactly L ≡ 0 (mod 3): flux quantization is the "
 "geometric cause of the first arch of the bridge.",
 "The full scan L = 6..48 (15 sizes, tolerance sweep 1e-6..1e-10) gives "
 "the law: **N₀ = 2L − 6·[L ≡ 0 (mod 12)] for L ≡ 0 (mod 6), else "
 "N₀ = 0**; the Dirac index Σ sign(ε) equals −2 exactly on the "
 "subfamily L ≡ 0 (mod 12) and 0 on L ≡ 6 (mod 12). The decisive checks "
 "on sizes absent in v1: L = 36 → 66, L = 48 → 90 — both exactly on the "
 "law. The T9 observation is refined: L = 18 (≡ 2 mod 4) also carries 36 "
 "modes — the modifier is mod 12, i.e. the conjunction of mod 3 (flux) "
 "and mod 4 (staggered structure).",
 "Additional measurements: the open boundary gives exactly one zero mode "
 "with index −1 for odd L ≡ 0 (mod 3) — an edge index; the α = 1/2 "
 "control — no zero modes at any L. This is the first genuine "
 "arithmetic-to-spectrum bridge inside the program: the number of zero "
 "modes of the lattice is read off the residues of L, and the index "
 "distinguishes two arithmetic subclasses. Proving the law through the "
 "Kähler–Dirac index is the main goal of v3 (N1 in the roadmap)."]},
{"h1": "C12/T14. The argument principle band to T = 5000",
 "paras": [
 "The C2 machine (adaptive argument principle with the Turing bridge of "
 "arithmetics) is extended to T = 5000. The core is the Riemann–Siegel "
 "function: Z(t) = mp.siegelz at dps = 20 with the bridge to e^{iθ}ζ at "
 "machine precision (max |Δ| = 0.0 at six control heights). The on-line "
 "count: a coarse grid of 0.15 with refinement of small-|Z| intervals "
 "(catching close pairs) and 36-iteration bisection; the run is done in "
 "segments (0–5000 in 13 runs, ~60 minutes).",
 "Result: **N_online(5000) = 4520** against the smooth count "
 "N̄(5000) = 4520.08; S_max = 0.91 ≤ 2 (the Turing validity threshold of "
 "the block scheme); strip checks by the argument principle over the "
 "full strip σ ∈ [0,1] in three windows — 11 = 11, 10 = 10, 5 = 5; the "
 "v1 anchors (0, 3, 10, 29, 79, 649) are reproduced bit-wise. Gaps: "
 "[0.0908, 6.887], mean 1.103. The verified-RH band grew from 649 zeros "
 "to 4520 — an order of magnitude in height and sevenfold in count."]},
{"h1": "C13/T15 + C14/T16. Blind families and the attractor taxonomy",
 "paras": [
 "Five gate families absent from the v1 handle space (Nv, q, W, α, aniso, "
 "dalpha, mass, profile, signs, bc, twist): BF1 — purely imaginary "
 "x-hoppings (phase +π/2, TRS broken differently); BF2 — quasiperiodic "
 "vortex positions by the golden ratio, no RNG; BF3 — staggered columns "
 "of vortex dimers; BF4 — long-range hoppings ~1/r²; BF5 — row-by-row "
 "flux dithering. Twenty gates, one pipeline, pipeline positive control "
 "PC0' = 1.000.",
 "Result of the blind protocol: all 20 gates are in the null zone — "
 "|r_H7| ≤ 0.040, minimal p = 0.29, GUE class intact. The H2 gap is "
 "robust to five independent designs outside the v1 space — this is the "
 "demarcation T15.",
 "The anomaly hunt (C14/T16) — a systematic scan of 121 configurations "
 "with an honest taxonomy: 97 configurations are the full GUE class; 18 "
 "are the integrable clean lattice (Nv = 0, Poisson/critical class — "
 "expected from C8); 6 are intermediate statistics of a weak vortex "
 "cloud (Nv ≤ 8 at q = 0.5, ⟨r⟩ = 0.47–0.53). No rank outliers "
 "(|r_H7| ≤ 0.153). Conclusion: **the GUE attractor is global for all "
 "vortex-carrying configurations**, but its basin has a measurable "
 "structure in (Nv, q, W) — a map of the approach to universality, not a "
 "sensation outside it."]},
{"h1": "C15/T17. Dirichlet L-functions: the gap is universal",
 "paras": [
 "The main question of plan item 12: is the measured H2 gap universal, "
 "or a defect of zeta specifically? C15 transfers the C1–C4 + C6 "
 "pipeline to two quadratic characters: χ₅ (even, mod 5) and χ₇ (odd, "
 "mod 7).",
 "The graph branch: Z_χ(t) = e^{iθ_χ(t)}L(½+it,χ) is real on the line to "
 "5e-35 (K2 analog); bisection gives 68 zeros ≤ 120 for χ₅ and 74 for "
 "χ₇ — matching the smooth counts 67.8 and 74.5; a sample strip check by "
 "the argument principle confirms the count (3 = 3 in two windows). The "
 "ψ_χ ladder: the twisted sieve Σχ(n)Λ(n) against the zero reference — "
 "correlations 0.902 and 0.949 (M2 analog with a positive control).",
 "The trace branch — theorem T17: **K_χ(x) = Σ e^{−xγ_χ} = "
 "(1/π)∫Q_χ(a)sin(ax)da, Q_χ(a) = Λ'/Λ(½+a,χ) − B_χ − C₀^χ carries the "
 "twisted weight χ(n)Λ(n)/√n**. The derivation repeats the Hadamard "
 "scheme for the entire function Λ_χ; along the way the exact identity "
 "C₀^χ = Λ'/Λ(½) − B_χ was found (an analog of B = −C₀ from v1). "
 "Verification: |ΔK| ≤ 9.6e-6 (χ₅) and 6.1e-6 (χ₇) — v1-level precision, "
 "with the prime part χ-twisted.",
 "The rank projection: the same gates against L-function zeros — "
 "r_H7 = 0.035–0.164, the null zone. Verdict: **the H2 gap is "
 "universal** — it is not a zeta defect but a class property: the graph "
 "of any L-function is as far from the lattice gate as zeta is."]},
{"h1": "C16/T18. The quantum-information layer",
 "paras": [
 "The third measurement of the resonator — through entanglement and "
 "complexity. The correct object for one-particle Hamiltonians is the "
 "fermionic entanglement of the Slater Fermi sea: fill the n lowest "
 "orbitals, the correlation matrix C_A = P_A(Σψψ†)P_A, and the spectrum "
 "λ ∈ [0,1] gives S_vN = −Σλ ln λ − Σ(1−λ)ln(1−λ) (the Peschel "
 "protocol).",
 "Q1: the gate's Fermi sea is weakly entangled — S_A ≈ 12–16 nats "
 "against the Haar baseline 160–220 (z > 100): **locality suppresses "
 "the volume-law entanglement** — the quantum-information echo of the "
 "wall of locality C9/T11. Q2: the mutual information of the halves "
 "carries no zero signature — the correlation of the MI profile with "
 "the zero window is −0.018 against −0.121 random (both in the null "
 "cone). Q3: the spectral form factor on unfolded windows — the gate "
 "and GUE slopes match within the spread, the zero window is more "
 "rigid. Verdict: **entanglement and complexity erase arithmetic along "
 "with spectral statistics** (T18)."]},
{"h1": "The v2 honesty ledger: found-and-fixed",
 "paras": [
 "The v1 discipline («statuses are not inflated, all constants are "
 "derived») is continued; v2 publishes four findings:",
 "1. **B_HADAMARD** in the v1 shipped code contained ln(2π) = 1.8379 "
 "instead of ln(4π) = 2.5310. The correct value B = −0.0230957 is "
 "confirmed by the committed v1 verdicts — the error was in the file "
 "constant only, not in the results. Fixed with a code comment.",
 "2. **The T9 observation of v1 is refined**: the full C11 law — "
 "N₀ = 2L − 6·[L ≡ 0 (mod 12)] — shows that modes exist on all "
 "L ≡ 0 (mod 6), including L = 18 (≡ 2 mod 4); the v1 formulation "
 "«tori L ≡ 0 (mod 4)» described only the index −2 subfamily.",
 "3. **The χ4 coding is gauge-trivial** — phase systems with values "
 "{0, π} are removed by the transformation ψ → (−1)^y ψ; the spectral "
 "coincidence 8.4e-15 is measured. This is a corollary of T12 and an "
 "honest constraint of the coding class.",
 "4. **The r_EF metric of v2** — on detrended fluctuations: the raw v1 "
 "correlation catches the common trend of two smooth curves (any smooth "
 "D(u) gives r ≈ 0.99). The GUE null is wide (±0.8) and stated "
 "explicitly; the isospectral control must give r_fluct = 0.999 — and "
 "does.",
 "Additionally: the T6 check passed n instead of ln n to K_formula; the "
 "pole a = 0.5 fell on the spline grid; the environment's background "
 "processes do not survive between calls — the C12 run was done in "
 "segments with a later assembly. All documented in code and verdicts."]},
{"h1": "Explorer, Challenge and reproducibility",
 "paras": [
 "**Bridge Explorer** (explorer/streamlit_app.py, `streamlit run`) — a "
 "live tool: turn the gate handles → the 576×576 spectrum is rebuilt in "
 "place → three projections of the gap + the C9–C16 verdicts + the "
 "bridge map. Every live number uses the same protocol as the campaigns.",
 "**The open challenge** (challenge/CHALLENGE.md + score_submission.py): "
 "the public metric — demonstrate r_H7 ≥ 0.7 under the v2 protocol with "
 "passing positive controls and an intact GUE class. The scorer is "
 "blind, rebuilds the gate from the spec itself, and saves the full "
 "report to challenge/submissions/ regardless of the outcome. The "
 "leaderboard is open.",
 "Reproducibility: IVP01–IVP18 — 18/18 PASS in one command; pytest "
 "21/21; the verdict-replay campaigns re-read the committed data in "
 "seconds; the fresh runs (C9–C16) are self-contained and need nothing "
 "beyond numpy/scipy/mpmath. The zeta zeros are an internal cache with "
 "the mpmath version fixed in the verdicts."]},
{"h1": "The v3 roadmap",
 "paras": [
 "N1. **Proving the T13 law**: explain N₀ = 2L − 6·[L ≡ 0 (mod 12)] "
 "through the Kähler–Dirac index and the spectral sequence of the torus "
 "with flux 1/3 — the first full «theorem from arithmetic» inside the "
 "lattice.",
 "N2. **Other characters and forms**: χ mod 3, 11, 13 and modular forms "
 "(level 11) — how far does the T17 universality reach.",
 "N3. **Stitching through the index**: the Kähler–Dirac operator itself "
 "as a candidate gate — does its heat trace carry the prime weight at "
 "α = 1/3?",
 "N4. **The band T = 50000** with the same segment machine (~40× the "
 "C12 time).",
 "N5. **Quantum response to the index**: does MI see the phase "
 "transition N₀ > 0 ⇔ L ≡ 0 (mod 6) in the C16 protocol.",
 "N6. **The challenge**: live submissions; the first accepted result — "
 "a joint paper."]},
{"h1": "The v2.0 verdict",
 "paras": [
 "The operator that almost exists exists exactly as far as the trace "
 "allows: with the prime weight in it — exactly (T11); with arbitrary "
 "nonlocality — exactly; with prime co-location in the phases — exactly "
 "(T12). It refuses to exist locally: none of the 227 measured "
 "configurations of five families and three classes left the null "
 "zones, and the approach to GUE itself turned out to be structured "
 "(T15, T16). Arithmetic manifested in the lattice spectrum for the "
 "first time — but where nobody looked: in the count of the Dirac-index "
 "zero modes (T13). And the gap measured on zeta turned out to be a "
 "property of the whole L-function class (T17). The continuation is in "
 "the v3 roadmap."]},
]}
DOCS = {"v2": V2}
