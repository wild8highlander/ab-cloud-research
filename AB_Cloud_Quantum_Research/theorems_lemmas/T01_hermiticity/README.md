# Th1. Hermiticity and the reality of the spectrum — theorem derivation

**Campaign:** V4 · **Formal reduction:** A1 (spectral theorem) · **Documents:**
`theorem_th1_{ru,en}.{pdf,docx}` ·
**Figure:** `figures/th1_4dim_ru.png`, `figures/th1_4dim_en.png`
(2×2 tile, four dimensions, 600 dpi)

## Statement

For any set of vortices, W, α and boundaries the operator H_L satisfies H_L = H_L†; hence spec(H_L) ⊂ ℝ. At α = ½ and W = 0 the spectrum is symmetric: λ ∈ spec ⇒ −λ ∈ spec.

## Proof idea

Every bond is inserted as a pair H[i,j] = −t·e^{iφ}, H[j,i] = −t·e^{−iφ} = conj(H[i,j]) — hermiticity by construction; the diagonal is real (the vortex potential, disorder, the staggered mass). The W = 0 symmetry comes from the bipartiteness of the lattice in ix+iy parity: in that basis H = [[0, B], [B†, 0]], and the spectrum mirrors about zero.

## The four dimensions of the figure

a) ‖H−H†‖ across the gates L = 12/16/24/32 — exactly 0.0 (log scale); b) spectrum-realness residuals across the gates — ≤ 8.8e−15; c) the λ ↔ −λ pairing — up to 8.2e−15; d) eigenpair residuals — ≤ 8.8e−15. The ε = 1e−12 threshold is marked on every panel.

## Campaign certificate and artifacts

test_th1_passport.py (the certificate, Nv = 16/64/256, seed 96); computations/V04_operator_passport/ (the monographs, the figures); verification/claim_audit/claims/claim_v04.json

## Boundaries (honest)

Th1 says nothing about matching the spectrum to the ζ zeros: the series' verdicts there are the level identity — YES at the zeros' level (V6/V16, the D_nn bridge, v2.0.7) with the bit-level branch open (V16) and the blind-coding / σ-scan design claims refuted (V1, V3). The λ ↔ −λ symmetry breaks already at W > 0 and is not restored by vortices.
