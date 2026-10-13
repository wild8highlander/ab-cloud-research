#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""content/canon_en.py — the canonical monograph (English edition).

One consolidated volume without the v1/v2 split: T1–T18, campaigns
C1–C16, protocols, the pixel protocol and the roadmap in a single
continuous text. Assembled programmatically from content/en_part1–4
(single source of content); the fresh chapters mirror canon_ru.py.
"""
from content.en_part1 import C1, C2, C3, C4
from content.en_part2 import C5, C6, C7, C8
from content.en_part3 import THEOREMS, APPENDIX
from content.en_part4 import V2

AUTHOR = "Ishak Khamzatovich Isaev"
AFFIL = "Independent researcher, Nalchik, Kabardino-Balkarian Republic"
SERIES = "Hilbert Polya Bridge · canonical series"
DATE = "October 13, 2026"
VERSION = "2.0.0"


def _sec(doctree, needle):
    for s in doctree["sections"]:
        if needle in s["h1"]:
            return s
    raise KeyError(f"section not found: {needle}")


def _thm(doctree, needle):
    out = {}
    s = _sec(doctree, needle)
    for k in ("theorem", "theorem2", "theorem3", "theorem4"):
        if k in s:
            out[k] = s[k]
    return out


def _table(doctree, needle):
    s = _sec(doctree, needle)
    return s["table"]


def _fig(doctree, needle, key="figure"):
    s = _sec(doctree, needle)
    return s[key]


T3 = _thm(THEOREMS, "T1–T3")
T46 = _thm(THEOREMS, "T4–T6")
T710 = _thm(THEOREMS, "T7–T10")

META = {"title": "The Hilbert–Pólya Bridge: the Canonical Exposition",
        "subtitle": "Sixteen campaigns C1–C16, eighteen theorems T1–T18, "
                    "the Guinand–Weil trace formula and the pixel protocol "
                    "— one version of the package",
        "author": AUTHOR, "affil": AFFIL, "series": SERIES,
        "volume": "Canon", "version": VERSION, "date": DATE}

SECTIONS = []

# ── 1. Introduction ──────────────────────────────────────────────────────
SECTIONS.append({
"h1": "Introduction: one version of the programme",
"paras": [
 "The Hilbert–Pólya programme asks whether a self-adjoint operator H "
 "exists whose spectrum coincides with the ordinates of the nontrivial "
 "zeros of the Riemann zeta function. The Hilbert Polya Bridge package "
 "answers this question numerically and with an honesty discipline: "
 "sixteen campaigns C1–C16, eighteen theorems T1–T18, an 87-gate "
 "lattice family, the argument principle to T = 5000, the "
 "Guinand–Weil trace formula, and the pixel protocol of the second "
 "film. This volume is the canonical exposition of the whole package "
 "in a single version.",
 "Until now the series lived in four summary volumes: the theorem "
 "volume T1–T10, the reproduction-protocol appendix, the consolidated "
 "second-generation monograph, and the theorem volume T11–T18. The "
 "canonical edition retires the generational split: T1–T18 form one "
 "continuous framework, the chapters follow the campaigns, and every "
 "chapter cites the same committed verdicts from data/. No number in "
 "this volume is computed in place — everything is reproduced by the "
 "campaigns in seconds or documented in the honesty ledger.",
 "The method of the series is unchanged since the first campaign. "
 "Every result carries a status label — proven, measured, conjecture, "
 "refuted — and the status is never inflated. Every negative verdict "
 "is admissible only after a positive control: the method must see the "
 "identity where it is known to hold (the spinor64 twins, the graph "
 "against the file, the zero window in the trace). Everything is "
 "self-contained: the zeta zeros are computed by mpmath inside the "
 "package, the master seed is 96, and no external data files are used.",
 "How to read this volume. Chapters 2–6 are the first generation: the "
 "identity framework, counting, gates, the trace formula, dynamics and "
 "statistics. Chapters 7–13 are the eight campaigns C9–C16 with "
 "theorems T11–T18. Then follow the scorecard, the pixel protocol, the "
 "reproduction protocols, the honesty ledger, and the roadmap titled "
 "'the operator that encodes the zeros' — that is the goal of the "
 "programme, and the whole volume calibrates the path toward it."],
"figure": {"path": "figures/{lang}/light/info_map_{lang}.png",
 "caption": "Fig. 1. The map of the bridge: three projections of one gap "
            "Г2 and the wall of locality — the plan of the volume."}})

# ── 2. Framework (C1 + C2) ──────────────────────────────────────────────
SECTIONS.append({
"h1": "Framework: the identity function and the argument principle (C1–C2)",
"paras": [
 "The first two campaigns build and calibrate the graphical branch of "
 "the programme. C1 assembles the identity function "
 "Z_id(t) = e^{iθ(t)}ζ(½+it) from algebraic closures of the Γ-frame "
 "and proves that this envelope generates no zeros beyond ζ itself: "
 "the zeros of Z_id on [0, 200] — 79 of 79 with a maximum deviation of "
 "2.8e-14 from the mpmath reference; on 220 Gram points — the "
 "classical 4 sign violations. The negative answer to 'can the phase "
 "generate zeros' (K1; the candidate form refuted by direct "
 "computation: 0.765 instead of 1 at u = 1) fixes the boundary between "
 "the graph and the operator for the entire series.",
 "C2 answers the counting question: the number of zeros in the "
 "critical strip is compared with the number on the critical line by "
 "the argument principle, without any zero tables. The pole "
 "calibration (T3) and the double sheet condition of Turing's adaptive "
 "step give N_strip = N_line at thirteen heights up to T = 1000: "
 "649 = 649 with distance-to-integer at most 8.3e-25; the arithmetic "
 "bridge numpy/mpmath gives |ΔN| = 2.6e-26. The gaps below 1000 are "
 "[0.3104, 6.887] with mean 1.521; the second moment Σγ² agrees with "
 "the formula to 8.8e-7 after a factor error was found and fixed "
 "(honesty ledger).",
 "Together C1–C2 establish that the phase and counting machinery of "
 "the series is consistent component-by-component below the honest "
 "boundary T = 1000 — and that no element of the graph carries new "
 "arithmetic. The series then moves to the spectrum (C3–C5), the "
 "trace (C4) and the dynamics (C7)."],
 **T3,
"table": _table(C2, "Method and"),
"figure": _fig(C1, "Results"),
})

# ── 3. Gates (C3 + C5) ──────────────────────────────────────────────────
SECTIONS.append({
"h1": "Gates: universality without identity (C3, C5)",
"paras": [
 "Campaigns C3 and C5 are the spectral projection. Question Г2: does a "
 "gate exist — a vortex-cloud configuration on the 24×24 lattice with "
 "π flux — whose spectrum is identical to the spectrum of the zeros "
 "under the correspondence 'level n ↔ zero n'? The protocol handle "
 "space (Nv, q, W, α) plus six new dimensions of C5 (twists, "
 "anisotropy, flux shift, mass, profile, signs and boundaries) — 87 "
 "configurations in total, on one master seed and one unfolding "
 "pipeline.",
 "The answer is measured and negative: the best gate gives "
 "r_H7 = 0.226 (Bonferroni 0.80); the whole extended family stays at "
 "|r_H7| ≤ 0.043 with ⟨r⟩ = 0.500 ± 0.002 (GUE class). The positive "
 "controls show the method sees identity when it exists: the spinor64 "
 "twins (r = 1.000000000, D_nn = 2.7e-14) and the graph against the "
 "file (r = 1.000000000000, D_nn = 1.2e-10). The graph ↔ operator gap "
 "is 9–10 orders of magnitude in D_nn: a desert no handle crosses. "
 "GUE universality is an attractor erasing the arithmetic setting no "
 "matter how it is imposed."],
 "theorem": T710["theorem"],
"table": _table(C3, "Results and"),
"figure": _fig(C5, "Results", "figure"),
})

# ── 4. Trace formula (C4) ───────────────────────────────────────────────
SECTIONS.append({
"h1": "The Guinand–Weil trace formula (C4)",
"paras": [
 "C4 is the third projection of the gap and the main positive result "
 "of the first generation. For a hypothetical Hilbert–Pólya operator "
 "the heat trace must carry the prime weight. Theorem T6 makes this "
 "exact: Q(a) = ζ'/ζ(½+a) + ... − B − C₀ with B = ½ln(4π) − 1 − γ/2 "
 "= −C₀, and K(x) = Tr e^{−xH_ξ} = (1/π)∫Q(a)sin(ax)da with the weight "
 "Λ(n)/√n for a > ½. The identity is calibrated (M0: |ΔQ| ≤ 1.7e-12 on "
 "the file of 2 001 052 zeros with the analytic tail) and the trace "
 "formula verified (M1: |ΔK| ≤ 1.2e-5).",
 "For the gates the same machinery yields null zones: the positive "
 "control PC0 (a window taken from the zeros themselves) gives "
 "r_EF = +0.9998 with 2.1% residual, while the gates stay below the "
 "surrogate null ±0.39 with the best relative residual 6.7%. The gap "
 "is ≈ 0.5 of an order in the heat metric — a conservative metric. "
 "Conclusion: the prime weight provably lives in the trace of the "
 "zero operator and provably absent from the traces of all gates; a "
 "hypothetical HP operator, if it exists, must be nonlocal."],
 "theorem": T46["theorem3"],
"table": _table(C4, "M2"),
"figure": _fig(C4, "M0/M1"),
"figure2": _fig(C4, "M2", "figure3"),
})

# ── 5. Primes in the operator (C6) ──────────────────────────────────────
SECTIONS.append({
"h1": "Primes in the operator: flow, kernel, staircase (C6)",
"paras": [
 "C6 searches for the arithmetic of primes in the phase layer. The "
 "flow Φ_p = ½ln p composites exactly — theorem T4: (Φ_p, Φ_q) ≡ Φ_pq "
 "with max|ΔE| = 1.35e-14. The resolution kernel is short-range (T5): "
 "saturation ~2e-2 at d ≈ 4–6, multiplicativity localized in 2–3 "
 "cells; a linear approximation destroys the kernel. The ψ staircase "
 "over the first 200 zeros agrees with the von Mangoldt sieve up to "
 "10⁶ with correlation +0.972 — while the gates give "
 "+0.24/+0.13/+0.09/−0.12, the null zone (Г5 — NO, measured).",
 "Four encodings of the flow into vortex positions yield one GUE "
 "class (⟨r⟩ = 0.585–0.611): universality erases the arithmetic "
 "content of the phase more reliably than any measurement. The "
 "campaign's conclusion: primes are encoded in the structure of the "
 "zeros; an honest encoding must present itself in the flow (T4) and "
 "in the staircase (M2), not in level statistics; the path to the "
 "operator runs through generating the arithmetic, not copying it."],
 "theorem": T46["theorem"],
 "theorem2": T46["theorem2"],
"table": _table(C6, "M2."),
"figure": _fig(C6, "M2", "figure2"),
})

# ── 6. Dynamics and statistics (C7 + C8) ────────────────────────────────
SECTIONS.append({
"h1": "Dynamics and statistics (C7, C8)",
"paras": [
 "C7 is the dynamical measurement: on the self-dual line α = ½ the "
 "lattice indeed behaves as a discretized massless Dirac equation "
 "(Г4 — YES): a coherent packet, reflection from the boundaries, "
 "energy conserved to 1e-15. The ζ cloud is nearly transparent (Nv = 16 "
 "does not slow the packet) and steers the transport: P(x ≥ 90) for "
 "the ζ cloud is 16 times higher than for a random one (0.0032 vs "
 "0.0002) — the dynamical face of Montgomery's pair correlations. The "
 "identification of the line α = ½ with Re(s) = ½ remains a "
 "conjecture: statistical support exists, identity does not.",
 "C8 fixes the statistical frame (T10): the class is set by symmetry "
 "— the clean lattice is Poisson, real disorder GOE, complex vortices "
 "GUE (⟨r⟩ = 0.597–0.612), strong disorder Anderson–Poisson; GSE is "
 "architecturally unreachable (T² = +1). The reduction T8: 64 spin "
 "structures collapse into 4 Hamiltonians by the pairs (φx, φy) with "
 "isospectrality 1.1e-14 — discrete phases carry the universal class, "
 "not the arithmetic. Anything claiming arithmetic must present it "
 "outside statistics — in flow identities, in counting, or in the "
 "trace."],
 "theorem": T710["theorem2"],
 "theorem2": T710["theorem3"],
 "theorem3": T710["theorem4"],
"figure": _fig(C7, "Results"),
"figure2": _fig(C8, "T10."),
})

# ── 7–13. Second generation: C9–C16 from the single source ─────────────
for _needle in ("C9/T11", "C10/T12", "C11/T13", "C12/T14",
                "C13/T15", "C15/T17", "C16/T18"):
    SECTIONS.append(_sec(V2, _needle))

# ── 14. Scorecard ───────────────────────────────────────────────────────
SECTIONS.append({
"h1": "The Hilbert–Pólya scorecard",
"paras": [
 "The five-question scorecard condenses the whole measurement: the "
 "resonator is built and tuned (Г1 + Г3 + Г4); the zeros are encoded, "
 "not generated (Г2 + Г5); the prime weight is verified only for the "
 "zero operator (T6, T11). A hypothetical HP operator, if it exists, "
 "is not a local deformation of the lattice family — that is the only "
 "bridge consistent with all eighteen theorems and the three "
 "projections of the gap.",
 "Every verdict in the scorecard has a dated chain of evidence: "
 "campaigns C1–C16, positive controls, and the independent protocol "
 "IVP01–IVP18. That is why the 'NO' of Г2 and Г5 carries the same "
 "weight as the 'YES' of Г1, Г3, Г4: it was bought with the same "
 "discipline of controls."],
"table": {"caption": "Table 1. The five questions of the programme (scorecard)",
 "header": ["Item", "Question", "Verdict", "Evidence"],
 "rows": [
  ["Г1", "self-adjointness of the operator", "YES",
   "Hermiticity by construction; real spectrum"],
  ["Г2", "spectral identity level↔zero", "NO",
   "9–10 orders (C3); ≈0.5 order (C4); |r_H7| ≤ 0.043 (C5)"],
  ["Г3", "GUE class", "YES", "⟨r⟩ = 0.60 at Nv ≥ 8; all of C5 in class"],
  ["Г4", "Dirac dynamics", "YES", "coherent packet, energy 1e-15 (C7)"],
  ["Г5", "primes in the operator", "NO",
   "ψ-staircase 0.972 at zeros, null zone at gates (C6)"]],
 "ratios": [0.08, 0.3, 0.12, 0.5]}})

SECTIONS.append({
"h1": "The theorems T1–T18 at a glance",
"paras": [
 "The eighteen theorems form one framework: ten from the first "
 "generation (frame, counting, gates, trace, statistics) and eight "
 "from the second (trace uniqueness, phase classification, the index "
 "bridge, the band, blind demarcation, taxonomy, L-functions, quantum "
 "information). Statuses are never inflated: the difference between "
 "'proven' and 'measured' is part of the method, and it is what "
 "allows the series to speak of the Г2 gap as a measured fact.",
 "Six statements are fully proven and four more proven with numerical "
 "verification (T1–T4, T6, T8, T11, T12, T17); the rest are measured "
 "with controls. Full statements with proofs are spread across the "
 "chapters of this volume and the campaign monographs in "
 "computations/C*; the table below is the consolidated status "
 "registry."],
"table": {"caption": "Table 2. Statuses of theorems T1–T18",
 "header": ["T", "Content (brief)", "Status"],
 "rows": [
  ["T1", "Γ-closures: 3 forms + refutation of the candidate form", "proven"],
  ["T2", "Im Z_id = 0 on the line", "proven"],
  ["T3", "pole calibration of the argument principle", "proven"],
  ["T4", "co-location (Φ_p,Φ_q) ≡ Φ_pq", "proven"],
  ["T5", "resolution kernel δ(d), ξ_mult ≈ 2–3", "measured"],
  ["T6", "trace formula Tr e^{−xH_ξ}", "proven+verified"],
  ["T7", "universality demarcation (87 gates)", "measured"],
  ["T8", "spin-structure reduction 64→4", "proven"],
  ["T9", "zero modes α = 1/3 (refined: mod 12)", "measured"],
  ["T10", "Poisson/GOE/GUE ladder", "measured"],
  ["T11", "heat-trace uniqueness", "proven"],
  ["T12", "co-location classification", "proven+measured"],
  ["T13", "counting law N₀ = 2L−6·[L≡0 (mod 12)]", "measured (law)"],
  ["T14", "RH band to T = 5000 (4520 zeros)", "measured"],
  ["T15", "blind-family demarcation (20 gates)", "measured"],
  ["T16", "attractor taxonomy (121 configurations)", "measured"],
  ["T17", "twisted trace formula of L-functions", "proven+verified"],
  ["T18", "quantum echo of locality", "measured"]],
 "ratios": [0.1, 0.62, 0.28]}})

# ── 15. Pixel protocol ──────────────────────────────────────────────────
SECTIONS.append({
"h1": "The pixel protocol: the video as a measurement",
"paras": [
 "The package's second film — 'Zeros & Gates: pixel decoding' "
 "(3:06, 1920×1080, 30 fps) — is the first film rebuilt as an "
 "instrument: not a retelling but a recording of a measurement. The "
 "pipeline: 87 gates → 25×25 RGBA canvas → lossless PNG → byte-exact "
 "decode → f(E) = det(E·I − H_pixels) → 24 zeros by bisection → "
 "comparison against mpmath. The screen contains no decorative frame "
 "and no typed digit: every image is emitted by pixel_decoding.py, "
 "and every number is either read back from pixels or derived from "
 "what was read back.",
 "The encoding is honestly described as an inverse spectral problem. "
 "The measure with nodes γ₁…γ₂₄ (mpmath, 25 dps) and weights "
 "wₙ ∝ 1/|ζ′(½+iγₙ)| is run through a 24-step Lanczos pass with full "
 "reorthogonalization; the output is a real symmetric tridiagonal "
 "matrix J with α ∈ [44.85, 62.24] and β ∈ [4.51, 23.16] whose "
 "spectrum is identical to the prescribed zeros. Each pixel carries a "
 "32-bit word: a 30-bit Q22 mantissa (v = X·2⁻²²) and a sign bit in "
 "the alpha channel; 24 diagonal gates (αₙ), 46 coupling gates (23 β's "
 "and mirrors) and 17 witness gates of the calibration column — 87 in "
 "total.",
 "The measurement: from the decoded pixels a function "
 "f(E) = det(E·I − H_pixels) is built by the three-term recurrence "
 "p₀ = 1, p₁ = E − α₁, p_{k+1} = (E − α_{k+1})p_k − β_k²p_{k−1}; a "
 "120 001-point grid catches 24 sign changes, and 90 bisection "
 "iterations refine each root. Against the typed reference: "
 "max|Δ| = 1.26×10⁻⁷, RMS = 4.98×10⁻⁸ — seven matching digits across "
 "the whole comb from 14.1347251 to 87.4252746; the round-trip error "
 "is bounded by Q22 quantization (≈1.2×10⁻⁷), the PNG round-trip is "
 "byte-identical, the witness strip is 17/17.",
 "The honest frame of the protocol. The pixels never contain a zero — "
 "they contain α's and β's; the zeros rise from the function the "
 "pixels define. But the information flow of the pipeline is "
 "zeros → operator → zeros: the nodes and weights of the measure are "
 "prescribed from zetazero, and Lanczos merely repacks them into a "
 "matrix that is invertible by construction (the pair (γ, w) ↔ (α, β) "
 "is the classical inverse Jacobi problem). What is demonstrated is "
 "lossless encoding and integrity control, not an arithmetic "
 "generation of the operator. A blind version of the protocol — "
 "pixels from arithmetic, zeros as the prediction — is step N7 of "
 "the roadmap; that is what would turn the film from an instrument "
 "of honesty into a test of the programme."],
"table": {"caption": "Table. The pixel protocol: the measured score",
 "header": ["Quantity", "Value"],
 "rows": [
  ["Gates total / structural / witness", "87 / 70 / 17"],
  ["Canvas", "25×25 RGBA = 24×24 lattice + calibration"],
  ["Pixel format", "30-bit mantissa (Q22) + sign"],
  ["PNG round-trip (byte-for-byte)", "identical"],
  ["Witness strip", "17/17"],
  ["max|measured − typed|", "1.26×10⁻⁷"],
  ["RMS |Δ|", "4.98×10⁻⁸"],
  ["Relative error", "2.4×10⁻⁹"],
  ["Range of α / β", "[44.85, 62.24] / [4.51, 23.16]"]],
 "ratios": [0.55, 0.45]},
"figure": {"path": "video/pixel_decoding_canvas.png",
 "caption": "Fig. 1. The 25×25 RGBA master canvas: the big pixel formula "
            "— a 24×24 lattice plus the calibration column."},
"figure2": {"path": "video/pixel_decoding_matrix.png",
 "caption": "Fig. 2. H_pixels read back from the PNG bytes: all 70 "
            "structural entries annotated."},
"figure3": {"path": "video/pixel_decoding_spectrum.png",
 "caption": "Fig. 3. The measured zero staircase against the "
            "Riemann–von Mangoldt smooth count."}})

# ── 16. Reproduction protocols ──────────────────────────────────────────
SECTIONS.append({
"h1": "Environment, determinism and the data dictionary",
"paras": [
 "All campaigns ran in one environment: Python 3.12, numpy 2.1, "
 "scipy 2.14 (eigvalsh, driver evr), mpmath 1.3 (dps 25–40 by "
 "criteria), matplotlib 3.9 (figures at 600 dpi). The master seed is "
 "96; the RNG streams are fixed: vortices default_rng(96 + 3500), "
 "disorder default_rng(96 + 3501), GUE zeros default_rng(9000 + k), "
 "Poisson zeros default_rng(7000 + k). Runtimes range from seconds "
 "(C1) to about an hour (C2, C6); C12 ran in segments with a final "
 "assembly.",
 "The bit-for-bit base control: the protocol reference gate "
 "reproduces the mean level spacing of the C3 CSV with a deviation of "
 "1.45e-16 — the engine/hamiltonian.py core is equivalent to the "
 "original protocol. Verdicts are committed in data/; the campaigns "
 "re-read them and recompute cheap invariants in seconds. The full "
 "independent verification protocol IVP01–IVP18 passes 18/18 with "
 "one command; the pytest suite is 21/21. The dictionary of verdict "
 "files is in the table below."],
"table": _table(APPENDIX, "Data dictionary")})

SECTIONS.append({
"h1": "The registry of controls and the cycle formula",
"paras": [
 "The discipline of controls: a method is admitted to a negative "
 "verdict only after demonstrating a positive result on an object "
 "where the identity is known to hold. Every negative result of the "
 "series (Г2, Г5, M3) went through this procedure; every positive one "
 "(T1–T4, T6, T8) through an independent recomputation in "
 "IVP01–IVP10.",
 "The open challenge (challenge/CHALLENGE.md) accepts submissions "
 "against a public metric: r_H7 ≥ 0.7 under the v2 protocol with "
 "passing positive controls and an intact GUE class; the scorer is "
 "blind and keeps the full report regardless of outcome. The "
 "leaderboard is open."],
"table": _table(APPENDIX, "Register of positive"),
"conclusion": [
 "The cycle formula after sixteen campaigns: the resonator is built "
 "and tuned (Г1 + Г3 + Г4); the zeros are encoded, not generated "
 "(Г2 + Г5); the prime weight is verified for the zero operator (T6) "
 "and for the nonlocal primitive (T11), and absent from the local "
 "gates."]})

# ── 17. Honesty ledger ──────────────────────────────────────────────────
SECTIONS.append({
"h1": "The honesty ledger: the first generation",
"paras": [
 "The discipline 'statuses are not inflated, all constants are "
 "derived' is accompanied by a registry of published errors. From the "
 "first generation: the refutation of the Γ-module candidate form "
 "(K1) is published in the C1 monograph; the Σγ² factor error (4π³) "
 "was caught by disagreement with the data and fixed (C2); the "
 "degenerate angle W = 0 + midpoint was excluded from C5 with a note; "
 "the surrogate null of the heat metric was recognized as wide "
 "(±0.39) — the trace projection is conservative; 'all statistics' "
 "were confirmed within the Dyson triple, GSE being architecturally "
 "unreachable."]})
SECTIONS.append(_sec(V2, "honesty ledger"))

# ── 18. Roadmap ─────────────────────────────────────────────────────────
SECTIONS.append({
"h1": "Roadmap: the operator that encodes the zeros",
"paras": [
 "The directions are ordered by their expected effect on the main "
 "measured gap Г2 (9–10 orders in the rank metric, ≈0.5–1 in the heat "
 "metric) and on the main goal — showing that a Hilbert–Pólya "
 "operator encodes the zeros by generation, not by repacking.",
 "The theoretical bridge (N1–N3). N1 — a proof of the counting law "
 "T13: N₀ = 2L − 6·[L ≡ 0 (mod 12)] via the Kähler–Dirac index and "
 "the spectral sequence of the flux-1/3 torus; candidates are "
 "Atiyah–Singer on the lattice and the modularity of the curve "
 "x³ ≡ ... mod L. N2 — half-integer characters: transferring C15 to "
 "χ mod 3, 11, 13 and modular forms of level 11 — how far does the "
 "universality of T17 reach. N3 — stitching through the index: the "
 "Kähler–Dirac operator as a candidate gate; does its heat trace "
 "carry the prime weight (r_EF) at α = 1/3 — the one class where "
 "arithmetic has already entered the spectrum.",
 "Independence of H from the zeros (N7). The key falsifiable step: "
 "build candidates from arithmetic only and predict zeros blindly. "
 "Three candidate sources are already measured by the series: the "
 "LCM kernel Λ(lcm(m,n))/√mn (C9/N5 — a degenerate spectrum, but the "
 "prime weight is in the kernel), Kähler–Dirac at flux 1/3 (T13), "
 "and the discretization of the trace formula (a window of the "
 "explicit formula as a Hamiltonian). Acceptance criteria: prediction "
 "of new zeros beyond the fitted range; r_H7 ≥ 0.7 under the "
 "challenge protocol with passing positive controls and an intact "
 "GUE class; the blind pixel version — pixels from arithmetic, zeros "
 "from the spectrum.",
 "New campaigns (N4–N6). N4 — the band T = 50000 with the same "
 "segmented machine (~40× the C12 runtime). N5 — the quantum "
 "response to the index: does the MI profile see the phase transition "
 "N₀ > 0 ⇔ L ≡ 0 (mod 6) in the C16 protocol. N6 — the live intake of "
 "challenge submissions; the first accepted result becomes a joint "
 "paper.",
 "Literary anchors (N8). The Berry–Keating xp programme (1999) and "
 "its PT-symmetric version of Bender–Brody–Müller (2017) define the "
 "canonical nonlocal candidate; Connes' trace formula (1999) is the "
 "direct ancestry of T6/T11 — the spectral side of the trace "
 "construction is already measured by the series, and the wall of "
 "locality is noncommutative geometry turned onto a lattice. The xp "
 "variations with interactions (Sierra–Townsend, 2008) refine the "
 "candidate class. The classical supports — Weil's explicit formula "
 "(1952), Montgomery's GUE conjecture (1973), Odlyzko's computations "
 "(1987), and the Dyson triple (1962). The position of the series on "
 "this map: the only package where the trace side (T6/T11/T17), the "
 "demarcation of the local class (T7/T15/T16), and arithmetic in the "
 "spectrum (T13) are measured on one pipeline with controls."],
"conclusion": [
 "The verdict of the canonical edition. The operator that almost "
 "exists exists exactly as far as the trace allows: with the prime "
 "weight — exactly (T6, T11); with arbitrary nonlocality — exactly; "
 "with co-location of primes in phases — exactly (T12). It refuses to "
 "exist locally: 227 measured configurations of five families and "
 "three classes never left the null zones (T7, T15, T16). Arithmetic "
 "appeared in the lattice spectrum for the first time — in the count "
 "of zero modes of the Dirac index (T13) — and the gap turned out to "
 "be a property of the whole L-function class (T17). The pixel "
 "protocol fixes the discipline of encoding: zeros are transported "
 "without loss but are not generated. The only honest way forward is "
 "the roadmap: build H from arithmetic and predict the zeros "
 "blindly."]})

DOCS = {"canon": {"meta": META, "sections": SECTIONS}}

