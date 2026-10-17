# raw/ — original, read-only

Byte copies of the source laboratories' curated datasets. **Read-only by
contract**: any transformation happens in `processed/` and is recorded in
`lineage.json`.

| Folder | Origin | Contents |
|---|---|---|
| `spectral_core/` | AB_Cloud_Quantum_Research/datasets | flagship numbers, ζ-zero reference table, campaign timeline |
| `dirac/` | dirac-lab/data | ζ-zero tables used by the Dirac laboratory (2000 / high / low) |
| `hilbert_polya/` | Hilbert_Polya/data | campaign verdict JSONs + gate tables (C1–C8 core set) |

Provenance: see `provenance.txt` and the package-level `00_meta/provenance.jsonl`.
