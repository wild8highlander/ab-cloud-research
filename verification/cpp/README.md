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
