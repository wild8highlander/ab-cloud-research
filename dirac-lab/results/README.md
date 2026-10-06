# results/ — Run artifacts and cross-verification

| Artifact | Content |
|---|---|
| `run_20261006_full_v13/REPORT.md` | **Master verdict ledger** of the canonical core run (8/8 PASS, 33 checks) |
| `run_20261006_full_v13/REPORT_EXTENSIONS.md` | **Extensions ledger** (v1.1): D9 10/10 + D10 9/9 PASS |
| `run_20261006_full_v13/REPORT_EXTENSIONS2.md` | **Extensions II ledger** (v1.2): D11 15/15 PASS (Berry–Keating / Connes) |
| `run_20261006_full_v13/REPORT_EXTENSIONS3.md` | **Extensions III ledger** (v1.3): D12 9/9 + D13 10/10 + D14 10/10 PASS (beyond §8: infinite BK ladder, JR wall under the conjugating drive, Odlyzko form factor) |
| `run_20261006_full_v13/results*.json` | Machine-readable verdicts, checks and metrics (core + extensions + extensions II + extensions III) |
| `run_20261006_full_v13/D*.csv` | Per-test data tables (finite-size ladder, tower, Berry phases, Landau fits, Klein transmissions, ZB frequencies, ζ-decoration metrics, chiral audit, D9 kernel/localization, D10 pair/transport statistics, D11 operator/coding/drive statistics, D12 comb/staircase/coverage, D13 wall-under-drive, D14 form factors) |
| `CROSS_VERIFICATION.md` | Python ↔ Julia comparison report with the full results table and methodology |
| `cross_verification_julia.json` | Machine-readable Julia cross-check output (core) |
| `cross_verification_ext.json` | Machine-readable Julia cross-check output (D9 extension) |
| `cross_verification_ext2.json` | Machine-readable Julia cross-check output (D11 extension) |
| `cross_verification_ext3.json` | Machine-readable Julia cross-check output (D12–D14 extensions) |
| `run_20261006_081031/` | Preserved **v1.0** canonical run (D1–D8) — kept for provenance |
| `PERFORMANCE.md` | **v1.4 performance sheet**: measured quick/FULL wall times of all four modules, where the time goes, reproducibility |
| `run_20261006_full_v11/`, `run_20261006_full_v12/` | Preserved **v1.1 / v1.2** canonical runs — kept for provenance |

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
