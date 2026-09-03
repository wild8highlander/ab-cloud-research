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
