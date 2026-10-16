# Data dictionary — 02_data

| Dataset | Format | Key columns | Origin | Notes |
|---|---|---|---|---|
| `processed/research_registry.json` | JSON | `flagship_results[]`, `verdicts[]`, `numbers_registry[]` | consolidated | the single source of numbers for the monograph, reports, web lab, CLI |
| `raw/spectral_core/flagship_numbers.csv` | CSV | `metric, value, source_verdict, module` | ABQR | RU metric names; verbatim |
| `raw/spectral_core/zeta_zeros_reference.csv` | CSV | index, ordinate | ABQR | reference zeros (internal mpmath cache dump) |
| `raw/spectral_core/campaign_timeline.csv` | CSV | campaign, date, status | ABQR | programme timeline |
| `raw/dirac/zeta_zeros_*.txt` | TXT | one ordinate per line | dirac-lab | 2000 zeros / high band / low band |
| `raw/hilbert_polya/*.json` | JSON | verdict payloads | HP | campaign verdicts C1–C8 |
| `raw/hilbert_polya/*gates*.csv` | CSV | gate parameters | HP | C3/C5 gate families |
| `checksums.sha256` | text | `sha256  path` | generated | covers everything under 02_data |

**Number-handling rule.** Values are stored as text, verbatim from the
sources' verdict files. Scientific notation, fractions and intervals keep
their original string form; never re-format a number without recording both
forms in `lineage.json`.
