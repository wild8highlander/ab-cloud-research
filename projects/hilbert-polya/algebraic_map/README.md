<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ Hilbert_Polya/](../README.md) · [🏠 Root README](../../README.md)**

</div>
# algebraic_map — the algebraic function of the Jacobi encoding

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

This directory lifts the pixel protocol (`video/pixel_decoding.py`,
Appendix H.8) from a "numerical algorithm" to an **explicit algebraic
function** and answers the question: *which formulas does the encoding
generate, and which of them are new*.

## In short: what Φ is

The encoding maps the zeros and the weights onto the gates of the canvas.
It turns out that this map is the classical Jacobi map (Stieltjes,
1894–95; Gram; modern treatments: Szegő 1939, Golub–Meurant 2010, Deift
1999), written in explicit determinants:

```
measure:    ν_n = w_n² / Σ w_j²,   w_n ∝ 1/|ζ'(ρ_n)|        (weights = squares of the 1/ζ residues)
moments:    μ_k = Σ_n ν_n γ_n^k
D_n  = det(μ_{i+j})_{i,j=0}^{n−1},  D_0 = 1              (Hankel)
S_n  = det(Hankel with last column μ_{i+n}),  S_0 = 0

Φ:  α_n = S_{n+1}/D_{n+1} − S_n/D_n                       (diagonal of J)
    β_n² = D_{n+1}·D_{n−1}/D_n²                           (off-diagonal of J²)
```

Φ is rational in (γ, ν); the only radical is β_n = √β_n². The Lanczos in
`pixel_decoding.py` is simply a numerical way to evaluate Φ; decoding
(the three-term recurrence + bisection) is the inverse branch Φ⁻¹: the
coefficients of p_N(λ) = det(λI − J) are the elementary symmetric
polynomials of the nodes γ (Newton's identities), and the roots of p_N
are the original zeros.

## Files

| File | Purpose |
|------|---------|
| `jacobi_map.py` | Library: moments, Hankel, Φ (two branches: exact Stieltjes + mpmath determinants), Φ⁻¹, identities, Q22 quantization, reference Lanczos |
| `run_verification.py` | Full verification on the committed data; writes `data/amap_results.json` and the figures `figures/{ru,en}/fig26..28` |
| `data/amap_results.json` | All the numbers: exact checks, log₁₀ D_n/S_n/h_n, profiles, bounds |
| `report/` | Report "The algebraic map of the Jacobi encoding" (RU, PDF/DOCX): `HPB_algebraic_map_2026-10-13_ru.pdf` / `.docx`, the `_cover.html` cover, and `src/` — the build sources (content blocks and assembly scripts) |

## Main results (see report/ for details)

1. **Exact closure over ℚ.** On the real data (24 zeros, weights
   1/|ζ′|²): the char-polynomial assembled from (α, β²) coincides with
   Π(λ − γ_n) **in all 25 coefficients exactly** (Fraction arithmetic);
   D₂₅ = 0 exactly; Σαₙ = Σγₙ exactly — in particular, the witness pair
   `mean_alpha`/`mean_gamma` on the canvas agrees to 0.0 (a hidden
   checksum of the protocol).
2. **Two independent branches of Φ** (the sequential Stieltjes
   procedure and the D/S determinants at dps = 350) agree to 10⁻³⁰³ —
   the D/S formulas are proven on the data, not "checked by eye".
3. **The Weyl bound explains the decoding error**: ‖ΔJ‖₂ = 2.04·10⁻⁷ ≥
   max|Δγ| = 1.26·10⁻⁷; each gate is accurate to half an ulp of 2⁻²³.
4. **An algebraic checksum**: the identity Σα² + 2Σβ² = Σγ²
   strengthens the single canvas quantum by a factor of 2¹⁵ ≈ 3.3·10⁴ —
   a cheap integrity test for any future regeneration of the data.
5. **A new instantiation**: the encoding's measure is the "measure of
   quadratic residues" ν_n ∝ |Res(1/ζ, ρ_n)|²; its Jacobi matrix, the
   profiles αₙ/βₙ and the determinants D_n, S_n are not tabulated in the
   literature (as far as we know). The classics are the formulas
   themselves; what is new is the object they close on, and the fact
   that the pixel canvas is the Q22 quantization of Φ.

## Running

```bash
cd algebraic_map
python3 run_verification.py     # ~30 s: numpy, mpmath, pillow, matplotlib
```

Sanction to run: the Lanczos reproduces the committed JSON bit-for-bit
(dAlpha = dBeta = 0), all exact checks are green — any deviation means
the data is corrupted.

## Honest scope

This is not a proof of RH and not "generating zeros from arithmetic":
Φ is an inverse problem (the zeros are already part of the input). The
value: (a) the pixel protocol has gained a closed formula instead of a
Lanczos "black box" — a ready instrument for the blind protocol N7 of
`results/ROADMAP.md`; (b) the data of the ζ-measure (αₙ, βₙ, Dₙ, Sₙ, hₙ)
are now exactly computable and verifiable over ℚ; (c) corollary
identities (K1–K8 in the report) have been found and proven, including
practical checksums.

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The algebraic map: the algebraic function of the Jacobi encoding, kept as a separate mini-module with its own data, figures and report.

**Subfolders:** `data/` · `figures/` · `report/`

<div align="center">

<img src="../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
