# Python Verification — the Reference Implementation

This folder is the **reference implementation** of the three-objection
verification program. Every other language folder in `../` is expected to
reproduce this one's numbers; when in doubt, this code is the arbiter.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.py` | bilingual library: zero loader, unfolding, b(N) convergence, KS/CvM GUE tests, log-log regression, report writer (auto-selects RU/EN text) |
| `ab_cloud_verify_en.py` | same, English-only output |
| `ab_cloud_verify_ru.py` | same, Russian-only output |
| `run_verify.py` | self-contained CLI runner — the only file you normally touch |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- Python **3.10+**
- Standard library only for the core path (`math`, `json`, `argparse`,
  `random`, `statistics`). `matplotlib` is optional: without it the runner
  still prints all verdict tables and skips PNG export.

## Run

```bash
cd verification/python

# all three objections, 5 000 zeros, Russian output
python3 run_verify.py --zeros 5000 --objection all --lang ru

# GUE test on 200 000 zeros from the 500k Odlyzko file
python3 run_verify.py --zeros 200000 --source 500k --objection 2 --lang en

# explicit data directory (any folder with the zero files)
python3 run_verify.py --zeros 50000 --data-dir ../data --objection 1
```

## What you get

- the b(N) convergence table (N = 100 … dataset size) with power-law fit,
  R² and the verdict against `bN_pass_threshold = 2.0`;
- KS + Cramér–von Mises p-values of the unfolded spacings against the GUE
  Wigner surmise, ⟨r⟩ with bootstrap error (n = 1000);
- the log-log decay slope with a 95% CI;
- a timestamped text report next to the script;
- `*.png` plots when matplotlib is available.

Typical wall time: < 1 s for 5 000 zeros, ~3 s for 50 000, ~15 s for 500 000
(single core, pure Python).

## spinor38/ — Test 38 port

`spinor38/spinor38.py` reads the frozen 64 spinor classes from
`../spinor64/data/`, rebuilds the 28 odd-orbit spectra with a **hand-written
Jacobi eigensolver** (no NumPy, no LAPACK) and verifies:

1. exact isospectrality of operators inside the PSL(2,7) orbit;
2. the ⟨r⟩ statistic of the frozen AB-cloud reference run.

Run it with:

```bash
cd verification/python/spinor38 && python3 spinor38.py
```

Frozen-data contract, column formats and the physics context:
[`../spinor64/README.md`](../spinor64/README.md) and
[`../spinor38/README.md`](spinor38/README.md) (present in every language
folder of this suite).

## Notes

- The loader is the canonical `load_zeros(data_dir, count, source)` contract
  shared by all ten languages; `source="auto"` picks the smallest file that
  holds the requested count (see `../README.md`, §4).
- All randomness (bootstrap, shuffles) uses fixed seeds — reruns are
  byte-identical.

## Кратко (по-русски)

- Эталонная реализация верификации на Python 3.10+, без внешних
  зависимостей (matplotlib опционален — только для графиков).
- Запуск: `python3 run_verify.py --zeros 5000 --objection all --lang ru`.
- Печатает таблицу b(N), KS/CvM против GUE, наклон убывания; пишет отчёт.
- `spinor38/` — Порт Test 38: чистый Python, собственный алгоритм Якоби,
  чтение замороженных данных из `../spinor64/data/`.
