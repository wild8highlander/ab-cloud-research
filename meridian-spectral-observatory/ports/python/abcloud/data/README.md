<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ abcloud/](../README.md) · [🏠 Root README](../../../../../README.md)**

</div>
<div align="center">

# 🧮 Embedded ζ-Zero Tables (`abcloud/data`)

**Two zero tables extracted verbatim from the Julia sources of the RH_Sweep_Pro
family, shipped inside the Python package so the RH stack selftest runs
without any external files.**

*SP: 13 661 zeros · v5: 500 zeros · one per line · full printed precision*

</div>

## The tables

| File | Count | Source literal | Used by |
|---|---|---|---|
| [`rh_embedded_zeros_sp.txt`](rh_embedded_zeros_sp.txt) | 13 661 | `const ZETA_ZEROS = Float64[…]`, `RH_Sweep_Pro.jl` (source lines 830–4245) | `rh_stack.py` — SP gallery metrics (`rh_metrics_sp`, `rh_*` sections of the stack golden) |
| [`rh_embedded_zeros_v5.txt`](rh_embedded_zeros_v5.txt) | 500 | `const ZETA_ZEROS_EMBEDDED = Float64[…]`, `RH_Unified_v5.jl` (source lines 795–1080) | `rh_stack.py` — v5 gallery metrics (`rh_metrics_v5`) |

Both files are written one value per line at the full precision of the Julia
literals, in strictly increasing order. They mirror the corresponding tables
in the Julia sources exactly; nothing is recomputed or reformatted.

## Provenance

Extracted by the one-off provenance script
[`../../extract_rh_zeros.py`](../../extract_rh_zeros.py), which parses the
`const` literals out of the unmodified Julia sources, asserts the expected
count and strict monotonicity, and writes the tokens verbatim. Re-running the
extractor must reproduce these files byte for byte.

> [!NOTE]
> The 13 661-zero SP table and the 500-zero v5 table are **different
> extractions at different suite revisions**, kept separate on purpose — the
> stack golden anchors (`rh_metrics_sp` vs `rh_metrics_v5`) are computed
> against each table exactly as the corresponding Julia suite does.

<div align="center">

**[↑ abcloud package](../../README.md)** · [shared zero table](../../../data/README.md) · [golden](../../../golden/README.md)

</div>

<div align="center">

<img src="../../../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
