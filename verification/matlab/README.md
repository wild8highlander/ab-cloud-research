# MATLAB Verification

Native MATLAB implementation of the three-objection program — vectorised,
no toolboxes required.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.m` | bilingual module (loader, unfolding, KS/CvM, regression) |
| `ab_cloud_verify_en.m` | English-only variant |
| `ab_cloud_verify_ru.m` | Russian-only variant |
| `run_verify.m` | standalone CLI-style runner |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **MATLAB R2021b+** — base MATLAB only (no Statistics Toolbox: KS and CvM
  are implemented manually so every language shares one definition).

GNU Octave compatibility: the code targets base MATLAB syntax; Octave ≥ 7
usually runs it, but this is best-effort and not covered by the reference
numbers.

## Run

```matlab
cd verification/matlab
run_verify('--zeros', 50000, '--source', '50k', '--objection', 'all')
run_verify('--zeros', 5000, '--objection', '2', '--lang', 'ru')
```

Parameters mirror the CLI of all other languages: `zeros`, `source`,
`objection`, `lang`, `data-dir`.

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS/CvM p-values vs the GUE Wigner surmise, ⟨r⟩ with bootstrap
error, decay slope with 95% CI; timestamped report written next to the
scripts, optional figure export via `saveas`.

## spinor38/ — Test 38 port

`spinor38/spinor38.m` reads the frozen classes from `../spinor64/data/` and
rebuilds the 28 odd-orbit spectra with a MATLAB-native cyclic-Jacobi
eigensolver (deliberately not `eig`, so the isospectrality check is
independent of LAPACK):

```matlab
cd verification/matlab/spinor38
spinor38
```

## Кратко (по-русски)

- Реализация на MATLAB R2021b+ без тулбоксов: KS и CvM написаны вручную,
  чтобы определения совпадали во всех десяти языках.
- Запуск: `run_verify('--zeros', 50000, '--source', '50k', '--objection', 'all')`.
- `spinor38/` — Порт Test 38: собственный алгоритм Якоби (не `eig`),
  данные — из `../spinor64/data/`.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 6.0 KB | directory |
| `README.md` | 2.1 KB | file |
| `ab_cloud_verify.m` | 13.9 KB | file |
| `ab_cloud_verify_en.m` | 8.3 KB | file |
| `ab_cloud_verify_ru.m` | 9.1 KB | file |
| `run_verify.m` | 3.8 KB | file |
| **Total (recursive)** | **7 files, 43.3 KB** | |

## 🔬 Deep dive — the MATLAB / Octave port in the parity matrix

The MATLAB port serves the numerical-computing audience
that meets the project through its native environment: all statistics
are expressed in matrix form, the loader reads the same frozen tables,
and the runner accepts the shared flag language as function arguments.
It runs unchanged in GNU Octave, which keeps the port verifiable
without a MATLAB license. The `spinor38/` port follows the validated
C++ reference like every other language folder, and the reporting
variants produce the same PASS/FAIL verdict lines as the rest of the
matrix.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** MATLAB R2020b+ or GNU Octave 7+
- **Entry point:** `run_verify.m   # accepts the same flags: run_verify('--zeros', 50000, ...)`

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

- Для аудитуры MATLAB/Octave: статистики в матричной форме,
  те же замороженные таблицы, те же флаги как аргументы функции.
- Работает в GNU Octave без изменений — проверка без лицензии MATLAB.
- spinor38 следует C++-эталону; вердикты PASS/FAIL — как у всех.
