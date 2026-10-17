# raw/ — original, read-only

Byte copies of the source laboratories' curated datasets. **Read-only by
contract**: any transformation happens in `processed/` and is recorded in
`lineage.json`.

| Folder | Origin | Contents |
|---|---|---|
| `spectral_core/` | AB_Cloud_Quantum_Research/datasets | flagship numbers, ζ-zero reference table, campaign timeline |
| `dirac/` | dirac-lab/data | ζ-zero tables used by the Dirac laboratory (2000 / high / low) |
| `hilbert_polya/` | Hilbert_Polya/data | campaign verdict JSONs + gate tables (C1–C8 core set) |
| `meridian/` | meridian-spectral-observatory | the observatory's documentation set (`docs/`, RU), `CITATION.cff` and the zero tables (`zeros50k.txt`, `zeta_zeros_50k.txt`) |
| `results_run/` | repository `results/` | the v19 two-pass reference-run artifacts (37 tests): `FINAL_REPORT/`, per-test `test_reports/` + `computation_logs/`, two flat reference logs |
| `vortex_optimization/` | Test 34-ext study | the vortex-density scan measurements: stage CSVs, the L = 96 GUE control JSON, `curves/*.npz` |
| `wave_attractors/` | Wave_attractors study (W1) | the E1–E7 experiment summaries, ray dumps, cross-verification JSONs and `REPRODUCING.md` |

Provenance: see `provenance.txt` and the package-level `00_meta/provenance.jsonl`.
