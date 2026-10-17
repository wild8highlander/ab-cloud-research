# 02_data — datasets, schemas, dictionaries, cards

| Path | What it is |
|---|---|
| [`raw/`](raw/README.md) | byte copies of the sources' curated datasets (read-only) |
| [`processed/`](processed/) | the unified research registry — the single source of numbers |
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
