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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 8.6 KB | directory |
| `README.md` | 2.5 KB | file |
| `ab_cloud_verify.f90` | 23.5 KB | file |
| `ab_cloud_verify_en.f90` | 12.1 KB | file |
| `ab_cloud_verify_ru.f90` | 13.6 KB | file |
| `run_verify.sh` | 2.1 KB | file |
| **Total (recursive)** | **7 files, 62.4 KB** | |

## 🔬 Deep dive — the Fortran port in the parity matrix

The Fortran 2018 port keeps the house numerical style of
the discipline: explicit everything, array bounds checked at runtime
(`-fcheck=all` is on by default), and warnings that are meant to be
treated as errors. If a regression sneaks into the statistics code,
this port fails loudly and early — that is its role in the parity
matrix. The reporting variants mirror the shared flag language, so the
port slots into cross-language replays without special-casing.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** gfortran with -O2 -std=f2018 -fcheck=all -Wall -Wextra
- **Entry point:** `bash run_verify.sh   # compiles, then runs`

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

- Фортран-2018 порт: явный код, проверка границ массивов
  (`-fcheck=all` по умолчанию), предупреждения — как ошибки.
- Роль в матрице паритета: громко и рано падать на регрессиях.
- Те же флаги, что у всех портов — без исключений при повторных прогонах.
