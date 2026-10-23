<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:ffd60a,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ 02_data/](../README.md) · [🏠 Root README](../../../../README.md)**

</div>
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

<div align="center">

<img src="../../../../assets/svg/divider-gold.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
