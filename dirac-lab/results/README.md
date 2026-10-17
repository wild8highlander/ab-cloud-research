# results/ — Run artifacts and cross-verification

| Artifact | Content |
|---|---|
| `run_20261006_081031/REPORT.md` | **Master verdict ledger** of the canonical run (D1–D8, 8/8 PASS, 33 checks) |
| `run_20261006_081031/results.json` | Machine-readable verdicts, checks and metrics of the canonical run (core) |
| `run_20261006_081031/D1_finite_size.csv` … `D8_chiral_protection.csv` | Per-test data tables of the canonical run (finite-size ladder, zero tower, Berry phases, Landau fits, Klein transmissions, ZB frequencies, ζ-decoration metrics, chiral audit) |
| `CROSS_VERIFICATION.md` | Python ↔ Julia comparison report with the full results table and methodology |
| `cross_verification_julia.json` | Machine-readable Julia cross-check output (core) |
| `cross_verification_ext.json` | Machine-readable Julia cross-check output (D9 extension) |
| `cross_verification_ext2.json` | Machine-readable Julia cross-check output (D11 extension) |
| `cross_verification_ext3.json` | Machine-readable Julia cross-check output (D12–D14 extensions) |
| `PERFORMANCE.md` | **v1.4 performance sheet**: measured quick/FULL wall times of all four modules, where the time goes, reproducibility |

The extension ledgers (`REPORT_EXTENSIONS.md`, `REPORT_EXTENSIONS2.md`,
`REPORT_EXTENSIONS3.md`) and their per-test CSVs are written locally by the
commands below and are not part of the committed tree; the per-test folders in
[`../tests/`](../tests/) carry the committed v1.4 extension ledgers.

## Reproduce

```bash
python3 ../code/dirac_lab.py            # core: writes a fresh run_<timestamp>/
python3 ../code/dirac_lab_extensions.py # extensions: REPORT_EXTENSIONS.md + D9/D10 CSVs
python3 ../code/dirac_lab_extensions2.py # extensions II: REPORT_EXTENSIONS2.md + D11 CSV
python3 ../code/dirac_lab_extensions3.py # extensions III: REPORT_EXTENSIONS3.md + D12/D13/D14 CSVs
julia   ../code/dirac_lab_cross.jl
julia   ../code/dirac_lab_cross_ext.jl
julia   ../code/dirac_lab_cross_ext2.jl
```

Every number quoted in the READMEs and both monographs regenerates from these artifacts.
