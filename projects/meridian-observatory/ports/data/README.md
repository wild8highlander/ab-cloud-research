<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:a78bfa,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ ports/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
<div align="center">

# 📊 Shared Zero Table

**The 1,000 Riemann zeta zeros embedded in `AB_Cloud_Monumental_v6_3.jl`,
extracted once at full printed precision so that every port — and every
fresh clone without Julia — reads the identical table from disk.**

*1 000 zeros · γ₁ = 14.134725… · extracted by a provenance script, not retyped*

<img src="../assets/divider.svg" width="1152" alt="Animated neon divider"/>

</div>

> **🧭 Navigation:** [ports/](../README.md) · [meridian-spectral-observatory/](../../README.md) · [Root README](../../../README.md)



## What this is

[`monumental_zeta_zeros_1000.txt`](monumental_zeta_zeros_1000.txt) holds the
first 1 000 zeros of the Riemann zeta function on the critical line, one per
line, at the full precision printed in the Julia source. It is the default
`--data` input for the ports' `zeros`, `hp` and `sweep` modes when the full
50 000-zero file (`zeros50k.txt`, meridian root) is not at hand, and the
fixture of the monumental demo battery.

## Provenance

The table is **extracted, not recomputed**: the one-off script
[`../python/extract_monumental_zeros.py`](../python/extract_monumental_zeros.py)
parses the `const _ZETA_ZEROS_1000 = Float64[...]` literal straight out of
[`../../AB_Cloud_Monumental_v6_3.jl`](../../AB_Cloud_Monumental_v6_3.jl)
(source lines 491–1492) and writes the tokens verbatim — no float re-formatting,
no re-derivation. Re-running the extractor must reproduce this file byte for
byte; any diff means the Julia source changed and the ports' embedded tables
need the same update.

| Property | Value |
|---|---|
| Count | 1 000 |
| First zero | 14.134725141735… |
| Ordering | strictly increasing |
| Sibling tables | [`../python/abcloud/data/`](../python/abcloud/data/README.md) — the SP (13 661) and v5 (500) embedded RH tables |

> [!NOTE]
> The golden selftest does **not** depend on this file — it reads
> `zeros50k.txt` from the meridian root. This table exists so the demo/CLI
> path works on machines that never cloned the zero archive.

<div align="center">

**[↑ Ports overview](../README.md)** · [python package data](../python/abcloud/data/README.md)

</div>

---

<!-- enriched-r3 -->

This folder is part of the **port matrix of the Meridian Spectral Observatory**: one kernel re-expressed across languages, sharing the frozen zero table and checked against the same golden anchors. The [`golden/`](../golden/README.md) shelf defines the reference values; the [`data/`](../data/README.md) shelf holds the shared input. A port that reproduces the anchors bit-for-bit demonstrates that the observatory's arithmetic is a property of the specification, not of one runtime. The matrix overview is in [`ports/`](../README.md).

The shared zero table: the one input every port reads, kept byte-identical across languages.

```mermaid
flowchart LR
    D["data/<br/>shared zero table"] --> P["this port<br/>data"] --> G["golden/<br/>reference anchors"]
    style P fill:#1f6feb,color:#fff
```

*Every port reads the same table and must reproduce the same anchors.*

## Folder contents

| File | Size | What it is |
|---|---|---|
| `monumental_zeta_zeros_1000.txt` | 20 KB | plain-text dataset / log |


**Where next:** [golden anchors](../golden/README.md) · [data/](../data/README.md)

<div align="center">

<img src="../../../assets/svg/divider-violet.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
