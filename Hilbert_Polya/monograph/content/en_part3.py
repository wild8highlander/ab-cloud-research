# -*- coding: utf-8 -*-
"""content/en_part3.py — consolidated volumes: theorems T1–T10 and appendix (EN)."""
from content.en_part1 import _meta

THEOREMS = {
"meta": _meta("Theorems of the Project",
              "T1–T10: statements, lemmas, proofs and honest labels",
              "Theorems"),
"sections": [
{"h1": "About this volume",
 "paras": [
 "This volume collects the ten statements on which the whole series "
 "rests. Each carries a status label: proven — a complete proof plus a "
 "machine verification exists; measured — a statement about a finite "
 "computational experiment with controls; conjecture — a working "
 "hypothesis of the series. We deliberately do not inflate the status: "
 "the difference between a proof and a measurement is part of the "
 "method.",
 "The numbering T1–T10 is shared by the READMEs, the monographs C1–C8, "
 "the Hilbert–Pólya scorecard and the Independent Verification "
 "Protocol. The proofs are given in a volume sufficient for checking "
 "without external sources; every constant is derived inside the "
 "series."]},
{"h1": "T1–T3: the frame and the counting",
 "theorem": {"label": "T1 (Γ-closures) — proven.",
  "text": "|Γ(½+iu)|² = π/cosh πu; |Γ(iu)|² = π/(u·sinh πu); "
  "|Γ(¼+iu)|·|Γ(¾+iu)| = π√2/√cosh 2πu; the single modulus on the line "
  "admits no elementary closure (K1, refuted).",
  "proof": "Euler reflection, Legendre duplication; the counterexample "
  "to the candidate form is 0.765 at u = 1. Verification at dps = 40: "
  "1.3–2.6e-39."},
 "theorem2": {"label": "T2 (reality of Z_id) — proven.",
  "text": "Im Z_id(t) = 0 on the critical line; parity holds to "
  "9.9e-29.",
  "proof": "ξ(½+it) ∈ ℝ (the symmetry ξ(s) = ξ(1−s)), θ(t) odd. "
  "Verification at dps = 30."},
 "theorem3": {"label": "T3 (pole calibration) — proven.",
  "text": "N(T) = Δarg ξ/2π with no additive +1 when the pole s = 1 is "
  "bypassed from above; a single leaf condition loses turns (2π "
  "aliasing).",
  "proof": "The residue of ξ'/ξ at s = 1 is +1; a clockwise half-passage "
  "contributes −π to Δarg. Practical verification: anchors "
  "0/3/10/29/79/649 and the arithmetic bridge 2.6e-26."}},
{"h1": "T4–T6: arithmetic and the trace",
 "theorem": {"label": "T4 (co-location) — proven.",
  "text": "(Φ_p, Φ_q) ≡ Φ_pq with Φ_p = ½ln p; max|ΔE| = 1.35e-14.",
  "proof": "Additivity of the logarithm; the lattice realisation "
  "preserves the identity at machine level."},
 "theorem2": {"label": "T5 (resolution kernel) — measured.",
  "text": "The composite-node response δ(d): 0 → 3.2e-3 (d = 0.5) → "
  "1.5e-2 (d = 2) → saturation ~2e-2 at d ≈ 4–6; multiplicativity is "
  "localised in 2–3 cells; first-order additivity fails (~1e-2).",
  "proof": "Direct measurement on the grid d ∈ [0, 6]; honesty label: "
  "depends on the flow conventions of C6."},
 "theorem3": {"label": "T6 (trace formula for H_ξ) — proven and verified.",
  "text": "Q(a) = ζ'/ζ(½+a) + 1/(½+a) + 1/(a−½) − ½lnπ + ½ψ(¼+a/2) − B − C₀ "
  "with B = ½ln(4π)−1−γ/2 = −C₀; K(x) = Tr e^{−xH_ξ} = (1/π)∫₀^∞ "
  "Q(a)sin(ax)da; for a > ½ the ζ-series contributes the weight Λ(n)/√n.",
  "proof": "Hadamard product plus 2a/(a²+γ²) = 2∫e^{−γt}sin(at)dt. "
  "Verification: |ΔQ| ≤ 1.7e-12 (M0), |ΔK| ≤ 1.2e-5 (M1)."}},
{"h1": "T7–T10: spectrum and symmetry",
 "theorem": {"label": "T7 (universality demarcation) — measured.",
  "text": "87 gates (52 protocol + 35 extended) lie in the GUE class "
  "(⟨r⟩ = 0.498–0.612) and carry no Λ-weights: r_H7 ≤ 0.226, "
  "|r_H7| ≤ 0.043 over the new handles, r_EF inside the null clouds.",
  "proof": "Campaigns C3–C5 with positive controls PC1/PC2 (r = 1.0) "
  "and PC0 (r = 0.9998)."},
 "theorem2": {"label": "T8 (64→4 reduction) — proven.",
  "text": "The E2 spin structures collapse to 4 Hamiltonians by the "
  "pairs (φx, φy) mod 2π; isospectrality within classes 1.1e-14.",
  "proof": "The phases enter through two sums of three 1-forms mod 2π "
  "→ 2×2 = 4 classes; verified against the E1/E2 tables."},
 "theorem3": {"label": "T9 (zero modes at α = 1/3) — measured.",
  "text": "On frustrated tori L ≡ 0 (mod 4) the clean lattice at "
  "α = 1/3 has exact zero modes: 18 at L = 12, 42 at L = 24.",
  "proof": "Direct diagonalisation with fixed multiplicities; a "
  "number-theoretic explanation (the Dirac index) is an open question "
  "of the series."},
 "theorem4": {"label": "T10 (statistics ladder) — measured.",
  "text": "Poisson/GOE/GUE are governed by symmetry (frustration / real "
  "disorder / complex vortices); GSE is structurally unreachable "
  "(T² = +1).",
  "proof": "An 11-channel ladder, classification by ⟨r⟩ + KS; the GSE "
  "limit is architectural."}},
{"h1": "Summary table and consequences",
 "paras": [
 "Of the ten statements, four are fully proven (T1, T2, T4, T6), one is "
 "proven and verified to a numerical floor (T6), four are measured with "
 "controls (T5, T7, T9, T10), and one is proven at the level of phase "
 "structure (T8). None carries a status higher than its content — and "
 "it is exactly this discipline that lets the series speak of the H2 "
 "gap of 9–10 orders as a measured fact rather than an estimate.",
 "The main consequences for the Hilbert–Pólya programme are collected "
 "in the scorecard: the resonator is built and tuned (H1+H3+H4), the "
 "zeros are encoded rather than generated (H2+H5), and the prime weight "
 "is verified only for the zero operator (T6). A hypothetical "
 "HP-operator, if it exists, is not a local deformation of the lattice "
 "family — the single bridge between all ten theorems and the three "
 "projections of the gap."],
 "table": {"caption": "Table 1. Statuses of the theorems",
  "header": ["T", "Content (brief)", "Status"],
  "rows": [["T1", "Γ-closures: 3 forms + a refutation", "proven"],
           ["T2", "Im Z_id = 0", "proven"],
           ["T3", "pole calibration of the argument principle", "proven"],
           ["T4", "co-location (Φ_p,Φ_q) ≡ Φ_pq", "proven"],
           ["T5", "resolution kernel δ(d), ξ_mult ≈ 2–3", "measured"],
           ["T6", "trace formula Tr e^{−xH_ξ}", "proven+verified"],
           ["T7", "universality demarcation (87 gates)", "measured"],
           ["T8", "64→4 reduction", "proven"],
           ["T9", "zero modes at α = 1/3", "measured"],
           ["T10", "Poisson/GOE/GUE ladder", "measured"]],
  "ratios": [0.1, 0.62, 0.28]}},
]}

APPENDIX = {
"meta": _meta("Appendix: Reproduction Protocols",
              "Environment, seeds, data dictionary, control register, scorecard",
              "Appendix"),
"sections": [
{"h1": "Environment and determinism",
 "paras": [
 "All campaigns ran in one environment: Python 3.12, numpy 2.1, "
 "scipy 1.14 (eigvalsh, driver evr), mpmath 1.3 (dps 25–40 per "
 "criterion), matplotlib 3.9 (600 dpi figures). The master seed of the "
 "series is 96; the RNG streams are fixed: vortices — default_rng(96 + "
 "3500), disorder — default_rng(96 + 3501), GUE nulls — default_rng(9000 "
 "+ k), Poisson nulls — default_rng(7000 + k). Runtimes: C1 ~2 s, "
 "C2 ~30 min (two arithmetics), C3 ~3 min, C4 ~12 s, C5 ~5 s, C6 ~8 min "
 "(the 10⁶ sieve), C7 ~20 min (L=96 dynamics), C8 ~1 min.",
 "The bit-for-bit base control: the protocol reference gate reproduces "
 "the mean level spacing of the C3 CSV with deviation 1.45e-16 — the "
 "kernel port (engine/hamiltonian.py) is equivalent to the original "
 "protocol up to summation order. All verdicts are committed in data/; "
 "the campaigns re-read them and recompute cheap invariants in seconds."]},
{"h1": "Data dictionary",
 "table": {"caption": "Table 1. Verdict files",
  "header": ["File", "Content", "Campaign"],
  "rows": [
   ["c1_identity_verdict.json", "K1–K7: ladder, reality, zeros, Gram", "C1"],
   ["c2_argument_verdict.json", "anchors 0/3/10/29/79/649, S(T), gaps, bridge", "C2"],
   ["c3_gates_verdict.json + c3_gates_table.csv", "52 gates, nulls, PC1/PC2", "C3"],
   ["c4_trace_verdict.json", "M0/M1/M2, PC0, trace-metric gap", "C4"],
   ["c5_gates_ext_verdict.json + c5_gates_ext_table.csv", "35+2 extended gates", "C5"],
   ["c6_primes_verdict.json", "co-location, kernel, ψ-ladder, codings", "C6"],
   ["c7_dynamics_verdict.json", "trajectories ⟨x⟩(t), transport P(x≥90)", "C7"],
   ["C8 ladder + spinor64", "11-channel ladder, 64→4 reduction", "C8"]],
  "ratios": [0.38, 0.44, 0.18]},
 "paras": [
 "The ζ zero file (2 001 052 heights, Odlyzko format) is not shipped "
 "for licensing reasons; its path is set by ZFILE in campaigns/ and "
 "defaults to verification/data/zeros6.txt of the neighbouring "
 "repository. Every verdict of the series is committed, so no test "
 "requires the zero file; fresh campaigns with recomputation are "
 "optional."]},
{"h1": "Register of positive and negative controls",
 "table": {"caption": "Table 2. Controls of the series",
  "header": ["Control", "Must show", "Value", "Where"],
  "rows": [
   ["PC1 spinor64 twins", "r = 1 on an isospectral orbit", "r = 1.000000000, D_nn = 2.7e-14", "C3"],
   ["PC2 graph ↔ file", "r = 1 between Z_id zeros and the file", "r = 1.000000000000", "C3"],
   ["PC0 zeros window (trace)", "the method sees the Λ-comb", "r_EF = +0.9998, residual 2.1%", "C4"],
   ["Decoys (random phases)", "the null zone of correlations", "0.026±0.140 / +0.050±0.153", "C3, C6"],
   ["GUE null", "universality without identity", "⟨r⟩-plateau; r_EF 0.43±0.71", "C3–C5"],
   ["Surrogate null (blocks)", "the width of the trace metric", "0.00±0.39", "C4"],
   ["Poisson null", "clustered spectra", "0.08±0.80", "C4"]],
  "ratios": [0.26, 0.3, 0.26, 0.18]},
 "paras": [
 "The discipline of controls: a method is allowed a negative verdict "
 "only after demonstrating a positive result on an object where "
 "identity is known to hold. Every negative result of the series (H2, "
 "H5, M3) passed this procedure; every positive one (T1–T4, T6, T8) "
 "passed an independent recount in IVP01–IVP10."]},
{"h1": "The Hilbert–Pólya scorecard",
 "table": {"caption": "Table 3. The five questions of the programme",
  "header": ["Item", "Question", "Verdict", "Basis"],
  "rows": [
   ["H1", "self-adjointness of the operator", "YES", "Hermitian by construction; real spectrum"],
   ["H2", "spectral identity level↔zero", "NO", "9–10 orders (C3); ≈0.5 order (C4); |r_H7| ≤ 0.043 (C5)"],
   ["H3", "the GUE class", "YES", "⟨r⟩ = 0.60 at Nv ≥ 8; all of C5 in class"],
   ["H4", "Dirac dynamics", "YES", "coherent packet, energy 1e-15 (C7)"],
   ["H5", "primes in the operator", "NO", "ψ-ladder 0.972 for zeros, null zone for gates (C6)"]],
  "ratios": [0.08, 0.3, 0.12, 0.5]},
 "conclusion": [
 "The cycle formula after eight campaigns: the resonator is built and "
 "tuned (H1+H3+H4); the zeros are encoded, not generated (H2+H5); the "
 "prime weight is verified only for the zero operator (T6). The "
 "roadmap — in results/ROADMAP.md: stitching the statistical and "
 "coding branches, nonlocal trace constructions, a number-theoretic "
 "explanation of T9."]},
]}

DOCS = {"theorems": THEOREMS, "appendix": APPENDIX}
