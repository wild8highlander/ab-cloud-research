# Fortran 2018 Verification

Modern Fortran implementation — coarrays-free, plain `gfortran` territory,
standard library only.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.f90` | bilingual module (loader, unfolding, KS/CvM, regression) |
| `ab_cloud_verify_en.f90` | English-only variant |
| `ab_cloud_verify_ru.f90` | Russian-only variant |
| `run_verify.sh` | convenience wrapper: compiles with gfortran and runs |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **gfortran ≥ 9** (GCC) or `ifort`/`ifx` — Fortran 2018 subset, no external
  libraries beyond the intrinsic modules.

## Run

```bash
cd verification/fortran
chmod +x run_verify.sh
./run_verify.sh --zeros 10000 --source 50k --objection all

# or manually:
gfortran -O2 -std=f2018 -o ab_cloud_verify ab_cloud_verify.f90
./ab_cloud_verify --zeros 50000 --source 50k --objection 1 --lang en
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH` (argument parsing is hand-rolled, C-style, so it behaves
identically everywhere).

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS/CvM p-values against the GUE Wigner surmise, ⟨r⟩ with
bootstrap error, decay slope with 95% CI, timestamped report. Fortran's
default `double precision` matches the other languages bit-for-bit on the
same input zeros.

## spinor38/ — Test 38 port

`spinor38/spinor38.f90` reads the frozen classes from `../spinor64/data/`
(plain CSV parsing) and rebuilds the 28 odd-orbit spectra with a hand-written
cyclic-Jacobi eigensolver:

```bash
cd verification/fortran/spinor38
gfortran -O2 -std=f2018 -o spinor38 spinor38.f90 && ./spinor38
```

Details: `spinor38/README.md`.

## Troubleshooting

- **`gfortran: command not found`** — Debian/Ubuntu `apt install gfortran`;
  Fedora `dnf install gcc-gfortran`; macOS `brew install gfortran`;
  Termux `pkg install gfortran` (available in the main repo).
- If your compiler rejects `-std=f2018`, drop the flag — the code is also
  valid Fortran 2008.

## Кратко (по-русски)

- Реализация на Fortran 2018 (подмножество F2008), собирается gfortran
  одной командой, внешних библиотек нет.
- `./run_verify.sh --zeros 10000 --source 50k --objection all` — CLI и
  вердикты идентичны эталону на Python.
- `spinor38/` — Порт Test 38: алгоритм Якоби написан с нуля, данные из
  `../spinor64/data/`.
