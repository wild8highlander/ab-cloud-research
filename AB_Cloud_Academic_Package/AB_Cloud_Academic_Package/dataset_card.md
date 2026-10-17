# Dataset card — AB-Cloud unified package

- **What**: the consolidated research registry of the AB-Cloud programme
  (24 flagship results, 6 verdicts, 20 registry rows, 6 levels) + the curated
  raw tables of the three source laboratories.
- **Where**: `02_data/` (registry in `processed/`, byte-copies in `raw/`).
- **Licence**: ODbL 1.0 for data; umbrella `LICENSE` for the honesty clause.
- **Funnel rule**: every display in the package derives from
  `02_data/processed/research_registry.json`; numbers are verbatim from the
  sources' verdict files (see `lineage.json`).
- **Honesty**: `rh_status = certified` (V13, unlocked v1.2.1); negative results included as
  first-class records; disagreements between sources shown, not resolved.
- **Citation**: see `CITATION.cff` · DOI 10.5281/zenodo.21825394.
- Full datasheet: `02_data/datacard.md`.
