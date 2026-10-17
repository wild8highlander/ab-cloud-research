# System card — the unified academic package

- **What the system is**: a research artefact packaging system — numbered
  structure (00–10), one registry funnel, six-language CLI, offline web lab,
  integrity test suite, honesty layer.
- **Outputs**: monographs (RU/EN), reports, figures, interactive displays,
  JSON contracts. No user data is collected; nothing phones home.
- **Failure modes**: checksum drift (detected by `09_tests`), i18n key
  drift (detected), funnel bypass (prevented by review protocol),
  overclaiming (prevented by the V13 obligation machine + licence §3).
- **Security**: static files only; see `SECURITY.md`.
- **Provenance**: `00_meta/provenance.jsonl` records every consolidation
  decision (source → destination → transform).
