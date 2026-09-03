# C++17 Verification

Native-speed implementation of the three-objection program. Compiled and
executed during the v1.1.0 preparation — the binary in `spinor38/` was built
with the exact commands below and reproduced the frozen reference numbers.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.cpp` | bilingual single-translation-unit library (loader, unfolding, KS/CvM, regression, report) |
| `ab_cloud_verify_en.cpp` | English-only build source |
| `ab_cloud_verify_ru.cpp` | Russian-only build source |
| `run_verify.sh` | compiles on the fly (g++ or clang++) and runs the CLI |
| `spinor38/` | Test 38 port — source + prebuilt Linux binary + README |

## Requirements

- **g++ ≥ 9** or **clang++ ≥ 10** (C++17).
- No external libraries — `<vector>`, `<cmath>`, `<fstream>`, `<random>` only.

## Run

```bash
cd verification/cpp
chmod +x run_verify.sh

# compile+run: all objections, 50 000 zeros, English
./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en

# manual build (what run_verify.sh does)
g++ -O2 -std=c++17 -o ab_cloud_verify ab_cloud_verify.cpp
./ab_cloud_verify --zeros 50000 --source 50k --objection all --lang ru
```

## What you get

Identical CLI contract to the Python reference (`--zeros`, `--source`,
`--objection`, `--lang`, `--data-dir`); identical b(N) tables to ~1e-12,
identical KS statistics to ~1e-9. Output: console verdicts + timestamped
report file.

## spinor38/ — Test 38 port (compiled & PASSed)

| Item | Value |
|---|---|
| Source | `spinor38/spinor38.cpp` |
| Prebuilt binary | `spinor38/spinor38` (x86-64 Linux, static-ish, g++ -O2) |
| Verified result | isospectrality **3.4e-14**, ⟨r⟩ = **0.4515710793** — **VERDICT PASS** |

```bash
cd verification/cpp/spinor38
g++ -O2 -std=c++17 -o spinor38 spinor38.cpp
./spinor38                     # reads ../spinor64/data/ frozen files
```

The port rebuilds the 28 odd-orbit spectra with its own cyclic-Jacobi
eigensolver written from scratch (no LAPACK/BLAS) and compares them against
the frozen reference spectrum — the numbers above are from the actual v1.1.0
run recorded in `../spinor64/output/run_log.txt`.

## Troubleshooting

- **`g++: command not found`** — install a compiler: Debian/Ubuntu
  `apt install g++`; Termux `pkg install clang`; macOS `xcode-select --install`.
- **Binary refuses to run after checkout on FAT/exFAT drives** — rebuild it
  from source (exec bits do not survive on FAT); the same applies to the
  committed `spinor38` binary on Android shared storage.
- Windows: build with MSYS2/MinGW-w64 (`pacman -S mingw-w64-ucrt-x86_64-gcc`)
  or WSL; the sources are standard C++17.

## Кратко (по-русски)

- Реализация на C++17 без внешних библиотек; собирается одной командой g++.
- `./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en` —
  компилирует и запускает; CLI и результаты идентичны эталону на Python.
- `spinor38/` — Порт Test 38: скомпилирован и прогнан при подготовке v1.1.0,
  изоспектральность 3.4e-14, ⟨r⟩ = 0.4515710793 — ВЕРДИКТ PASS; в папке лежит
  и готовый бинарник, и исходник.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 8.8 KB | directory |
| `README.md` | 3.2 KB | file |
| `ab_cloud_verify.cpp` | 25.2 KB | file |
| `ab_cloud_verify_en.cpp` | 15.1 KB | file |
| `ab_cloud_verify_ru.cpp` | 18.5 KB | file |
| `run_verify.sh` | 5.2 KB | file |
| **Total (recursive)** | **7 files, 76.0 KB** | |

## 🔬 Deep dive — the C++ port in the parity matrix

The C++ port hosts the **validated spinor38 reference**:
`spinor38/spinor38.cpp` is the implementation every other Test-38 port
was checked against, byte-for-byte, before being accepted. The suite
itself compiles to a single binary per reporting variant; the wrapper
handles compilation flags and error colors. This is the port to run
when you want native-speed sweeps over the 2M-zero table — the
largest dataset in `../data/` — without any runtime or VM in the way.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** g++ with -std=c++17 -O2 (GCC ≥ 9; Clang also works)
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

- Здесь живёт валидированный эталон spinor38: все прочие порты
  Теста 38 сверялись с `spinor38/spinor38.cpp` побайтно.
- Обёртка сама компилирует и запускает; цвета и флаги — на борту.
- Нативная скорость для прогонов по таблице 2M нулей.
