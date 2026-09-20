# `python_clone/` — The Python Reimplementation of the Suite
> A faithful, dependency-light Python port of all 38 tests: same statistics, same verdict algebra, same embedded 50,000-zero dataset — cross-validating the Julia apparatus in a second language.

_Location: [unpacked/](../README.md) › [python_clone/](README.md)_

This package is a **complete Python reimplementation of the AB-Cloud v23 SUPERCOMBO suite**: all 38 tests, the two-pass verdict algebra, the report writer, the plot engine and the CLI, executing against the identical embedded 50,000-zero dataset that the Julia apparatus carries. Its purpose is the cross-language reproduction documented as Add.2 of the September 2026 addendum — the strongest practical answer to "is the result an artifact of one language, one library, one implementation?" The original package README for the clone is preserved as `README_original.md`, including its family-by-family equivalence and deviation table.

## Quick start

```bash
pip install -r requirements.txt
python -m abcloud.cli --list                     # list the 38 tests
python -m abcloud.cli --test 1 --no-two-pass     # single test, single pass
python -m abcloud.cli --test 1-14                # statistics family (fast)
python -m abcloud.cli --test all                 # full suite (fast profile)
python -m abcloud.cli --test 1-14 --zeros 50000  # reference-scale statistics
python -m abcloud.cli --test all --full          # reference-scale everything
```

Outputs land in `results_py/` (configurable via `--out`): per-test folders `test_XX_<slug>/report.md` + `plots/`, and a master `final_report.md` + `results.json` — mirroring the Julia suite's output layout exactly, so the two implementations' reports can be compared folder by folder.

## Equivalence status in brief

The statistics family (Tests 1–14) reproduces **full equivalence** — same statistic definitions, same lettered sub-checks, with the clone's peak |Δγ̃| = 9.0356 and b(50000) = 1.2128 against the Julia run's 1.2126 documented in the README_original. The long-range RMT statistics (13, 14), the phase/fractal constants (21, 23) and the auxiliary Γ-identities (37) are exact or fully equivalent; the structural families (15–26, 28–36, 38) are equivalent in structure with documented deviations. The full table is in `README_original.md`.

## Layout

- [`abcloud/`](abcloud/README.md) — the Python package: `core.py` (statistics engine), `tests_01_14.py`, `tests_15_26.py`, `tests_27_38.py` (the batteries), `runner.py` (two-pass orchestration), `report.py` (report writer), `plot.py` logic inside `report.py`'s plot engine, `cli.py` (command line), `data/` (the embedded zeros).
- `pyproject.toml`, `requirements.txt` — packaging and dependencies (NumPy/SciPy/matplotlib only).

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `README_original.md` | 6.2 KB · 122 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `pyproject.toml` | 516 B · 16 lines | Python packaging metadata for the abcloud clone. |
| `requirements.txt` | 52 B · 4 lines | Python dependencies of the clone (NumPy/SciPy/matplotlib). |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`abcloud/`](abcloud/README.md) | 8 files, 1 subfolders | The Python package of the clone (core, batteries, runner, CLI) |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._