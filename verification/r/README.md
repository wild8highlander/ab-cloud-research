# R Verification

Base-R implementation — no CRAN packages required, runs anywhere R does.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.R` | bilingual module (loader, unfolding, KS/CvM, regression) |
| `ab_cloud_verify_en.R` | English-only variant |
| `ab_cloud_verify_ru.R` | Russian-only variant |
| `run_verify.R` | standalone CLI runner (`Rscript`) |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **R ≥ 4.3** — base only (`stats`, `utils`). No `install.packages()`.

## Run

```bash
cd verification/r
Rscript run_verify.R --zeros 50000 --source 50k --objection all --lang en
Rscript run_verify.R --zeros 5000 --objection 2 --lang ru
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH`.

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS and Cramér–von Mises p-values against the GUE Wigner
surmise (R's own `ks.test` cross-checks the hand-rolled statistic),
⟨r⟩ with bootstrap error, decay slope with 95% CI, timestamped report.

## spinor38/ — Test 38 port

`spinor38/spinor38.R` reads the frozen classes from `../spinor64/data/` and
rebuilds the 28 odd-orbit spectra with an R-native Jacobi eigensolver:

```bash
cd verification/r/spinor38
Rscript spinor38.R
```

## Notes

- R's `ks.test` is used only as a cross-check; the reported statistic is
  computed manually so that all ten languages agree definitionally.
- Base R plotting (`png()`) is used when available; on headless systems the
  runner detects it and skips PNG export gracefully.

## Кратко (по-русски)

- Реализация на base R ≥ 4.3 — пакеты CRAN не нужны вовсе.
- `Rscript run_verify.R --zeros 50000 --source 50k --objection all --lang en`
  — те же три возражения; CLI как во всех остальных языках.
- `spinor38/` — Порт Test 38 на R: замороженные данные из `../spinor64/data/`,
  собственный алгоритм Якоби.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 5.8 KB | directory |
| `README.md` | 2.0 KB | file |
| `ab_cloud_verify.R` | 11.9 KB | file |
| `ab_cloud_verify_en.R` | 8.1 KB | file |
| `ab_cloud_verify_ru.R` | 9.0 KB | file |
| `run_verify.R` | 3.9 KB | file |
| **Total (recursive)** | **7 files, 40.7 KB** | |

## 🔬 Deep dive — the R port in the parity matrix

The R port speaks to the statistics community in its
native idiom: base R vectorized operations, the same KS and
Cramér–von Mises statistics computed without any contributed package,
and the shared flag language parsed from the command line. Because R
is the lingua franca of applied statistics, this port doubles as an
independent re-derivation of the statistical machinery — if the GUE
comparison is implemented correctly, an R practitioner can confirm it
from a fresh clone in one command. The `spinor38/` port mirrors the
validated reference, as everywhere else.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** R ≥ 4.0 — base R only, no CRAN packages
- **Entry point:** `Rscript run_verify.R [flags]`

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

- Базовый R без CRAN-пакетов: те же KS и Крамер–фон Мизес,
  тот же набор флагов.
- Двойная роль: независимая перепроверка статистической механики
  силами R-сообщества одной командой из свежего клона.
- spinor38 зеркалит валидированный эталон.
