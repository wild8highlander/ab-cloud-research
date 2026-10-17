

# Changelog (release editorial history)

## 2026-10-16 — Sync with Hilbert_Polya v2.0.7–v2.0.10

The unified package is synchronized with the repository state of 2026-10-16
(commit 2b5d352). The Hilbert–Pólya laboratory's audit wave v2.0.7–v2.0.10
reached every layer of the package:

### Verdicts corrected (the headline of this sync)
- **G2 Spectral identity: NO -> YES** (audit v2.0.7). The gates measure
  D_nn = 0.0079 — the level of the shifted zero windows and the GUE zero
  class themselves (C3), with the trace bridge |ΔK| <= 1.2e-5 (C4). The
  bit-level branch (the direct gate-ladder escape at L = 96, T18) remains
  open and is recorded as the verdict's stated boundary.
- **G5 Primes in the operator: NO -> YES** (audit v2.0.8). The convergence
  ladder: the gate ψ-correlation is monotone in vortex coverage
  (−0.12 -> +0.09 -> +0.24) and converges with lattice size (the vortex
  scan: GUE floor 0.0324 -> 0.0220 at L = 24 -> 96, best pooled D = 0.0318);
  the zeros go 0.972 -> 1 by the explicit formula.
- **C5 honestly regenerated** (v2.0.5): the extended family measures
  ⟨r⟩ = 0.569–0.633 (mean 0.601), max |r_H7| = 0.097, Bonferroni 0.57 —
  replacing the stale r_mean column recognized as fake by the audit.

### Added
- **Campaign C17 (blind phase B, closed explicit-formula density)** —
  NEGATIVE by the letter of its pre-registered criterion (improvement over
  the primes-free null 1.04×, z_GUE = −3.3); the exploratory C17b blind
  valley-window stage reads the blind count exactly (19.0004 -> 19;
  25.00005 -> 25) with nodes reproducing the true comb quadrature to
  RMS 0.0021–0.0088. Verdict JSON: `02_data/raw/hilbert_polya/c17_blind_phaseB_verdict.json`;
  figures fig29–32 (ru/en).
- **algebraic_map** — the Jacobi map of the pixel encoding raised to an
  explicit algebraic function: exact closure in Q on the committed data
  (all 25 char-poly coefficients, D_25 = 0); two branches of Φ agree to
  1e-303; the Weyl bound explains the decoding error; the algebraic
  checksum amplifies a canvas quantum 2^15 times. Figures fig26–28 (ru/en).

### Data and figures
- Replaced (byte-copies of the regenerated verdicts): c3_gates_verdict.json,
  c3_gates_table.csv, c5_gates_ext_verdict.json, c5_gates_ext_table.csv,
  c6_primes_verdict.json.
- Updated figures: fig09_handles, fig10_gue_ext, fig14_ladder, fig25_map
  (ru + en, from figures_hires).
- figure_index.csv, captions (ru/en) and alt_texts.csv extended with the
  14 new figure files.

### Registries and surfaces
- research_registry.json: verdicts G2/G5 -> YES; sources and level III ->
  C1–C17; flagship results 36–37 (C17, algebraic_map); numbers registry
  rows 51–53; statistics 44+ campaigns.
- metrics.json: the same sync plus the enrichment record
  `hp_sync_2026_10_16`.
- Reports: report.md / report_ru.md (executive summary, programme table,
  verdict ledger, headline results 9–11, boundaries, outlook),
  executive_summary, lay_summary, one_pager, press_release, policy_brief,
  slides deck — all carried to the two-sided map (level identity + primes
  in; bit-level wall out).
- Monographs (ru/en, regular + MAX): verdict tables, the three-projections
  section, the v1 verdict (kept as a dated record with the audit
  correction), the C5 numbers, the conclusion; the embedded language
  abstracts (zh/de/es/fr/ar) refreshed; PDF + DOCX rebuilt
  (pandoc + tectonic; the Arabic abstract remains in DOCX/MD editions,
  omitted in the PDF as in the original build).
- Web lab: verdicts, level III essence, flagship results 23–24, displayed
  numbers 21–24, statistics.
- Dossier: claim table, one-sentence reading, honesty-layer index.
- README x7 (root, all languages): campaign count 43+ -> 44+, bridge rows
  C1–C17, the two-sided map wording; monograph language abstracts updated.
- checksums.sha256 regenerated for the changed data-funnel files.

### Unchanged (deliberately)
- The RH verdict: `blocked` (V13 obligation machine) — by construction.
- The heritage layers (v19 run, legacy package records).
- The raw data of the other sources (dirac, spectral_core, meridian,
  vortex_optimization, wave_attractors, results_run).


# Release editorial history (versionless)

The package carries no version numbers; this file records the editorial
milestones of the unified edition.

## 2026-10-14 — initial unified edition

- Structure `00_meta` … `10_notebooks` created per the unified specification.
- Research registry consolidated from the three sources (first pass).
- Monograph RU + EN written (full volumes); abstracts for zh/de/es/fr/ar.
- Report suite: unified report, executive summary, lay summary, press
  release, policy brief, one-pager, slide deck source.
- CLI implemented in Python, Julia, Rust, Go, JavaScript, Bash against
  `shared/contract.json`.
- Web laboratory built (offline, themable, bilingual).
- Integrity test suite written and green.
- Heritage: the legacy v23/v34 submission package structure retired; its
  38-test reference run recorded here and in CHANGELOG.md.
