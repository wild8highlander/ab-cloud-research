# Frozen Verification Data — Riemann Zeta Zeros

The single source of truth for every numeric experiment in this repository:
all ten language implementations of `../`, the Julia suite `../../code/`, the
spinor64 experiment `../spinor64/` and the React dashboard
`../../apps/ab-cloud-dashboard/` read these files. Nothing here is generated
at runtime — the files are frozen so every rerun of every program sees
byte-identical input.

## Files

| File | Zeros | Format | Notes |
|---|---|---|---|
| `zeta_zeros_50000.txt` | 13 661 | plain text, one ordinate per line | default dataset; `#` comments allowed |
| `zeta_zeros_50000.csv` | 13 661 | CSV: `index, t, s_real, s_imag, zero_number` | column-documented variant |
| `zeta_zeros_50000_embedded.txt` | 50 000 | plain text | extracted from the embedded table inside `code/julia/ab_cloud_v19_v1.jl` (added in v1.1.0); the dashboard's Web Worker dataset |
| `zeta_zeros_500k_odlyzko.txt` | 500 000 | plain text | extended Odlyzko set |
| `zeta_zeros_2M_odlyzko.txt` | 2 000 000 | plain text | full Odlyzko set |
| `zeta_zeros_2M_odlyzko.txt.gz` | 2 000 000 | gzip of the above | compressed copy for slow links |
| `zeta_zeros_highT_blocks.txt` | 30 000+ | blocks with headers | zeros at large heights T ~ 10¹² |
| `zeros6.txt` | 2 001 051 | space-separated | original Odlyzko `zeros6` table |
| `Zeta_Zeros_50000.jl` | 13 661 | Julia source (`zeta_zeros_table = [...]`) | for `include()` in Julia notebooks |

## What a "zero" is here

Every file lists the **imaginary parts** `t` of zeros on the critical line,
i.e. values with `ζ(1/2 + it) = 0`, sorted increasingly. The first entries of
the 50k set: `14.134725142`, `21.022039639`, `25.010857580`, … Lines starting
with `#` are comments; empty lines are ignored; whitespace-separated extra
columns are tolerated by the loaders (they take column 1).

## Provenance

- **Odlyzko tables** — <https://www-users.cse.umn.edu/~odlyzko/zeta_tables/>
  (the 500k / 2M / zeros6 sets).
- 13 661-zero and high-T subsets — author's cuts of the certified tables
  (Isaev Iskhak Khamzatovich, ORCID 0009-0003-7299-0701).
- 50 000 embedded set — extracted verbatim from the Julia suite source, where
  it was embedded as a literal array; re-extraction is documented in the
  v1.1.0 CHANGELOG entry.

## How the code consumes the data

All implementations share the contract `load_zeros(data_dir, count, source)`:

| Requested count | File chosen with `source="auto"` |
|---|---|
| ≤ 13 661 | `zeta_zeros_50000.txt` |
| ≤ 500 000 | `zeta_zeros_500k_odlyzko.txt` |
| ≤ 2 000 000 | `zeta_zeros_2M_odlyzko.txt` |
| > 2 000 000 | `zeros6.txt` |

Explicit `source` overrides: `50k`, `500k`, `2M`, `2M_gz`, `highT`, `zeros6`,
`csv`.

```bash
# examples from the repo root
python3 verification/python/run_verify.py --zeros 200000 --source 500k --objection all
./verification/cpp/run_verify.sh --zeros 50000 --source 50k --objection 1
julia verification/julia/run_verify.jl --zeros 500000 --source 500k --objection all
```

## Integrity

Datasets are treated as immutable: never edit in place. If you need a new
cut, add a new file and register it in the loader of each language (one line
per language). The reference statistics in `../spinor64/data/reference_stats.json`
and the frozen spectra are likewise immutable contracts.

## Кратко (по-русски)

- Каталог — единственный источник нулей дзета-функции для всех программ
  репозитория; файлы заморожены, менять их нельзя.
- Основные наборы: 13 661 / 50 000 / 500 000 / 2 000 000 нулей + highT-блоки
  и оригинальная таблица Odlyzko `zeros6`.
- Формат: по одному `t` на строку (`ζ(1/2+it)=0`), комментарии через `#`;
  есть варианты CSV и Julia-массива.
- Все коды используют контракт `load_zeros(data_dir, count, source)` с
  автоматическим выбором файла по запрошенному количеству.
- Источник больших таблиц — официальные таблицы Одлыжко; набор 50 000
  извлечён из встроенного массива кода v19_v1.
