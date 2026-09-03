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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `README.md` | 3.4 KB | file |
| `ab_cloud_verify.py` | 26.8 KB | file |
| `ab_cloud_verify_en.py` | 20.5 KB | file |
| `ab_cloud_verify_ru.py` | 22.5 KB | file |
| `run_verify.py` | 19.5 KB | file |
| **Total (recursive)** | **5 files, 92.7 KB** | |

## 🔬 Deep dive — the Python port in the parity matrix

The Python folder is the **self-contained reference port**:
`run_verify.py` deliberately packs everything into one file — the
Lambert W approximation, the GUE PDF/CDF, the KS and Cramér–von Mises
statistics, the zero loader and all three objection tests — so a
referee can audit the entire numeric chain without following imports.
The three verifiers (`ab_cloud_verify.py` plus the `_en`/`_ru`
reporting variants) are the original shared logic from which the other
nine languages were ported; when a reference output is disputed, this
folder's output is the tiebreaker. Being stdlib-only, it also serves as
the smoke test in CI: the full default run finishes in seconds on any
machine with Python installed.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** CPython ≥ 3.9 — standard library only, no pip packages
- **Entry point:** `python3 run_verify.py [flags]`

| Flag | Values | Meaning |
|---|---|---|
| `--zeros N` | integer, `0` = all | how many ordinates to use (default 10 000) |
| `--source NAME` | `auto`, `zeta_zeros_50000`, `zeta_zeros_500k`, `zeta_zeros_2M`, `zeta_zeros_highT`, `zeros6`, `zeta_zeros_50000_csv` | which frozen dataset from `../data/` to load (`auto` picks sensibly for the requested N) |
| `--objection X` | `all`, `1`, `2`, `3` | run the full suite or a single objection test |
| `--lang X` | `en`, `ru` | report language on stdout |

All inputs resolve against `../data/` — the frozen Odlyzko tables
described in `../data/README.md`. Nothing is downloaded or generated at
runtime; a run either reads the committed bytes or aborts. Reference
statistics every implementation must reproduce: pair-correlation KS =
0.047 with p = 0.27, Byers–Yang flux defect 3.5e-15, ⟨r⟩ = 0.5848 ±
0.0260 against the GUE value 0.5992, Connes self-duality via four zero
modes, Dirac slope v_F ≈ 0.125 with R² = 0.9997, b(50000) = 1.2126.

## 🧭 Cross-language parity

This port exists to prove the suite is language-independent: same frozen
inputs, same 37 tests, same numbers out. If this implementation ever
disagrees with the Julia reference (`../../code/ab_cloud_v19.jl`) or
with the other nine ports, the discrepancy is a bug in the port — the
data and the definitions are shared. CI exercises the interpreted
subset; the compiled ports are expected to be replayed locally with the
same one-line command shown above. The Test-38 companion lives in
`spinor38/` where present, and the spinor64 correction experiment — the
one that established 64/64 GUE-consistency for the Klein-quartic
structures — lives in `../spinor64/`.

## Кратко (по-русски)

- Порт существует для доказательства паритета: одинаковые замороженные
  данные, тот же набор тестов, те же эталонные числа (KS = 0.047,
  p = 0.27; дефект 3.5e-15; ⟨r⟩ = 0.5848 ± 0.0260).
- Флаги одинаковы во всех десяти реализациях — одна и та же командная
  строка проигрывается в каждой папке.
- Расхождение с эталоном трактуется как баг порта, а не как открытие.

- Эталонный самодостаточный порт: весь числовой конвейер в одном
  файле (Lambert W, GUE PDF/CDF, KS и Крамер–фон Мизес, загрузчик,
  три возражения) — аудит без переходов по импортам.
- Вердикт этой папки — тай-брейкеры для споров об эталонных числах.
- Только stdlib: прогон по умолчанию занимает секунды, CI-дым.
