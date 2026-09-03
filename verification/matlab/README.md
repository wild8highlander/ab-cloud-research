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
