# Changelog — AB Cloud Academic Package (unified edition)

This package is **versionless by design**: it is a living academic structure,
not a release train. This changelog therefore records the *editorial history*
of the unified edition — what was consolidated, restructured, or rewritten —
rather than semantic-version bumps.

## 2026-10-16 — Sync with Hilbert_Polya v2.0.7–v2.0.10

The unified edition is synchronized with the repository state of 2026-10-16
(commit 2b5d352). The audit wave of the Hilbert–Pólya laboratory reached
every layer of the package:

- **Verdicts corrected.** G2 (spectral identity): NO → **YES** — the gates
  measure D_nn = 0.0079, the level of the shifted zero windows and the GUE
  zero class themselves (C3; audit v2.0.7); the bit-level branch (T18)
  remains open and is recorded as the verdict's stated boundary. G5 (primes
  in the operator): NO → **YES** — the convergence ladder: the gate
  ψ-correlation climbs with vortex coverage and lattice size (audit v2.0.8).
  G3's basis now carries the honestly regenerated C5 family numbers
  (⟨r⟩ = 0.569–0.633, mean 0.601; v2.0.5).
- **New campaign C17** (blind phase B, closed explicit-formula density):
  NEGATIVE by the letter of its pre-registered criterion (1.04× over the
  primes-free null, z_GUE = −3.3); the C17b blind valley windows read the
  blind count exactly (19.0004 → 19; 25.00005 → 25). Verdict JSON committed
  to `02_data/raw/hilbert_polya/`; figures fig29–32 (ru/en).
- **New section algebraic_map**: the Jacobi map of the pixel encoding as an
  explicit algebraic function — exact closure in Q (all 25 char-poly
  coefficients, D_25 = 0), the two branches of Φ agreeing to 10⁻³⁰³, the
  Weyl bound explaining the decoding error, and a 2¹⁵-amplifying algebraic
  checksum. Figures fig26–28 (ru/en).
- **Data**: the regenerated v2.0.5 verdicts (c3, c5 + CSVs, c6) replace the
  stale ones byte-for-byte; checksums.sha256 regenerated.
- **Surfaces rebuilt**: registry and metrics (flagship 36–37, numbers
  51–53, statistics 44+), reports (EN/RU + summaries + deck), monographs
  (RU/EN, regular + MAX — verdict tables, the three-projections section,
  the dated v1 record with the audit correction, conclusions; PDF + DOCX),
  web lab, dossier, ontology, seven READMEs, five language abstracts.
  Integrity suite: 39/39.

## 2026-10-14 — The unified edition

### Consolidated
- **Three laboratories merged into one package.** The research content of
  `AB_Cloud_Quantum_Research` (spectral core V01–V20 + verification E01–E18 +
  spinor study ES1–ES5), `dirac-lab` (D1–D14, 96 checks) and `Hilbert_Polya`
  (C1–C17, T1–T18) is now organised under one numbered structure
  (`00_meta` … `10_notebooks`) with a single research registry.
- **The unified monograph.** A single consolidated volume (RU and EN, full;
  zh/de/es/fr/ar as abstracts) covers all four levels of the programme —
  replacing the three separate per-laboratory monographs as the *narrative
  centre* of the package. The originals remain in their source folders.
- **One verdict ledger.** Г1–Г5 + RH(blocked) now live in one place
  (`04_reports/report.md` and `05_logs/metrics.json`), with every number
  naming its campaign.
- **One CLI contract.** `run` implemented identically in Python, Julia, Rust,
  Go, JavaScript and Bash; all read the same `config.yaml` and emit the same
  JSON contract (`06_code/shared/contract.json`).

### Removed
- **Version numbers.** The "v23/v34" identity of the legacy submission package
  is retired. The unified edition has no version in its name, READMEs, or
  artefact names. The legacy run archive (38-test reference run of
  2026-09-14) is preserved as *heritage* in the provenance records of
  `00_meta/` rather than as bulk content.

### Added
- The interactive **web laboratory** (`07_web_lab/index.html`) consolidating
  all campaign ledgers, verdict tables and flagship figures — fully offline.
- The **honesty layer index** (`00_meta/dossier.md`): every `does_not_prove`
  field of the three sources, cross-referenced.
- Multilingual surface: 8 README languages, glossary in 3 languages,
  CLI i18n in 2 languages (RU/EN) with a 7-language UI map in the web lab.
- FAIR / reproducibility / ethics / open-science checklists (`00_meta/`).
- Integrity test suite (`09_tests/`) validating package structure, config
  schema, i18n key parity, checksums and monograph structure.

### Editorial decisions
- Numbers are quoted verbatim from the sources' own verdict files; when two
  sources disagree, both are shown (the sources themselves document such
  cases, e.g. the ⟨r⟩ bulk-window convention difference in the Dirac
  cross-verification note 2).
- The negative results (locality wall, null zones, failed correspondences)
  are promoted to the front page rather than buried in appendices — they are
  the *map* for any positive construction.

## Heritage (pre-unification)

- **2026-09-19** — legacy package frozen at v34 (superseded by this edition).
- **2026-09-14** — the 38-test reference run (26.04 h, Julia 1.12); September
  addenda: cross-language reproduction, disorder sweep, Klein quartic
  PSL(2,7) ensemble pass at 100,000 zeros (pooled D = 0.0808).
- **2026-10-06** — dirac-lab full run 8/8 PASS + four Julia cross-ports.
- **2026-10-12** — Hilbert_Polya v2: campaigns C9–C16, theorems T11–T18.
