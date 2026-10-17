# Datacard — Datasheets for Datasets

## Motivation
- **Purpose**: consolidate the numbers of the AB-Cloud research programme
  (spectral core, Dirac skeleton, Hilbert–Pólya bridge, blind verification)
  into one citable, checksummed, machine-readable dataset that serves the
  monograph, the reports, the web laboratory and the six-language CLI.
- **Creators**: Isaev Iskhak Khamzatovich (ORCID 0009-0003-7299-0701).
- **Funding**: none.

## Composition
- `processed/research_registry.json` — 35 flagship results, 11 verdicts,
  50 registry rows, 10 level descriptions (the unified record: levels I–VIII + IV+ heritage).
- `raw/spectral_core/` — 3 CSVs from AB_Cloud_Quantum_Research.
- `raw/dirac/` — 3 ζ-zero tables from dirac-lab.
- `raw/hilbert_polya/` — verdict JSONs and gate tables (C1–C8 core set).
- `raw/results_run/` — the v19 two-pass reference run (final report + 37 per-test reports and computation logs; heritage verdict layer).
- `raw/meridian/` — the 50,000-zero reference table (two formats) + the eight RU docs of the observatory.
- `raw/vortex_optimization/` — the T34-ext sweep CSVs (stages A/B/C), the L=96 GUE control JSON, and the curves.
- `raw/wave_attractors/` — the W1 experiment summaries (E1–E7), CSVs and the AB-water metrics.
- Instances: 663 reference zeros (spectral_core), 2000+2000+600 (dirac),
  50,000 zeros (meridian), v19 verdict payloads (80 files), T34-ext sweeps
  (242 configurations), W1 experiment payloads (28 files).

## Collection process
- All numbers were extracted **verbatim** from the source laboratories'
  verdict files (see `00_meta/provenance.jsonl` for the source→destination
  map). No number was re-computed or re-typed during consolidation.
- Pre-registration: verdict windows were fixed in the sources' configs
  before runs; the unified `config.yaml` mirrors them.

## Preprocessing/cleaning
- None beyond byte-copying for `raw/`; the `processed/` registry is a
  structured consolidation, not a transformation of values.

## Uses
- Reproduction of the monograph's tables; the web lab's displays; the CLI's
  `analyze` output; integrity tests.

## Distribution and license
- Data: ODbL 1.0 (`LICENSE-DATA`); umbrella research licence `LICENSE`.
- Honesty clause (LICENSE §3) applies to all derivatives.

## Maintenance
- Living dataset; updates must follow `00_meta/governance/review_protocol.md`
  (numbers pass, boundaries pass, registry is the funnel).
