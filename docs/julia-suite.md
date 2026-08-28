---
title: Julia suite — 37 tests, two-pass
---

# The canonical 37-test two-pass suite

`code/ab_cloud_v19.jl` (~30 000 lines, **no external packages**) is the
single source of truth for the numerics of this repository.

## Two-pass protocol

Every test runs **twice** at different lattice sizes. A verdict is only
accepted if both passes agree; the report engine writes per-test documents
(md, html, pdf, docx) plus figures (png 600 dpi, svg, gif) and full
computation logs, so each verdict can be re-verified independently.

## Test groups

| Group | Tests | Focus |
|---|---|---|
| Topology & gauge | 1–12 | Gram points, flux quanta, Byers–Yang, Chern C₁ |
| Spectral statistics | 13–24 | ⟨r⟩, Σ²(L), Δ₃(L), R₂(s), zero modes |
| ζ-zeros interface | 25–30 | certified zeros, Montgomery test, Dirac cone |
| Finite-size & disorder | 31–37 | Berry corrections, IPR, Hatano–Nelson skin |

## Report engine

Written from scratch (CRC32, zlib STORED blocks, PNG writer with pHYs,
GIF89a with custom LZW, vector PDF, DOCX via stored-ZIP, SVG) — the suite
needs nothing beyond a Julia 1.10 installation.

## Quick mode (CI)

```bash
julia code/ab_cloud_v19.jl --quick
```

Runs the reduced protocol (16×16 → 32×32, ζ ≤ 5000) with **both passes**
enabled — this is exactly what the [Julia workflow](https://github.com/wild8highlander/ab-cloud-research/blob/main/.github/workflows/julia.yml)
executes on every push.
