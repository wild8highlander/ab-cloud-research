<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ AB_Cloud_Academic_Package/](../README.md) · [🏠 Root README](../../../README.md)**

</div>
# 02_data — datasets, schemas, dictionaries, cards

> **🧭 Navigation:** [Package root](../README.md) · [AB_Cloud_Academic_Package/](../../README.md) · [Repo root](../../../README.md)

```mermaid
flowchart LR
    A["01_monographs<br/>the unified monograph"] --> B["02_data<br/>datasets · schemas · dictionaries"] --> C["03_figures<br/>consolidated figure set"]
    style B fill:#1f6feb,color:#fff
```

*Layer map of the unified package — the highlighted node is this layer.*

| Path | What it is |
|---|---|
| [`raw/`](raw/README.md) | byte copies of the sources' curated datasets (read-only) |
| [`processed/`](processed/) | the unified research registry — the single source of numbers |
| [`frozen/`](frozen/README.md) | the frozen ζ-zero datasets the verification suite reads (byte-identical to the repo's `verification/` canon) |
| [`synthetic/`](synthetic/README.md) | SYNTHETIC-marked demo data |
| [`external/`](external/README.md) | external sources (Odlyzko tables) — links + notes |
| [`schemas/`](schemas/) | JSON Schema, SQL DDL, Avro, Protobuf for the registry |
| [`data_dictionary.md`](data_dictionary.md) / `.csv` | dataset descriptions |
| [`codebook.md`](codebook.md) / `.yaml` | verdicts, series, precision conventions |
| [`datacard.md`](datacard.md) | Datasheets for Datasets |
| [`modelcard.md`](modelcard.md) | model cards (protocols, not ML models) |
| [`checksums.sha256`](checksums.sha256) | integrity over `02_data/**` |
| [`lineage.json`](lineage.json) | the transformation lineage |
| [`differential_privacy.json`](differential_privacy.json) | differential-privacy statement (`applicable: false` — no personal or human-subject data) |
| [`sampling_protocol.md`](sampling_protocol.md) | how the sources' numbers were sampled |

## The golden rule

Numbers are **verbatim from verdict files** (see `lineage.json` invariants).
The registry (`processed/research_registry.json`) is the funnel through which
every display artefact in this package is fed.

<div align="center">

<img src="../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
