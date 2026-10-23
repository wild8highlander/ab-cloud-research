<!-- AB-ENRICHED:v1 · sub -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venice&height=48&color=0:00e5ff,100:05060f&section=header" alt="" width="100%"/>

**🧭 [⬆ verification/](../README.md) · [🏠 Root README](../../README.md)**

</div>
> **CANON_SPEC v3.0.** This implementation follows `../CANON_SPEC.md` — the unified kernel
> (θ-Newton Gram points, 32768-point GUE CDF table, λ-corrected KS p-value, CvM/AD/⟨r⟩),
> 28 frozen golden anchors self-checked before any verdict, honest branch-selected conclusions,
> thin `_en`/`_ru` language pins. Measured self-check: 28/28 PASS (machine-verified for
> python/C++/Go/Rust/Julia/JS; fortran/R/MATLAB/Haskell — same spec, runtime self-check).

> **🧭 Navigation:** [verification/](../README.md) · [Root README](../../README.md) · [CANON_SPEC](../CANON_SPEC.md)

# C++17 Verification

Native-speed implementation of the three-objection program. The spinor38
port in `spinor38/` was compiled and executed during the v1.1.0 preparation
with the exact commands below and reproduced the frozen reference numbers.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.cpp` | bilingual single-translation-unit library (loader, unfolding, KS/CvM, regression, report) |
| `ab_cloud_verify_en.cpp` | English-only build source |
| `ab_cloud_verify_ru.cpp` | Russian-only build source |
| `run_verify.sh` | compiles on the fly (g++ or clang++) and runs the CLI |
| `spinor38/` | Test 38 port — source + README |

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
- **A locally built binary refuses to run on FAT/exFAT drives** — rebuild it
  from source in place (exec bits do not survive on FAT).
- Windows: build with MSYS2/MinGW-w64 (`pacman -S mingw-w64-ucrt-x86_64-gcc`)
  or WSL; the sources are standard C++17.

## Summary

- C++17 with no external libraries; a single `g++` command builds the suite.
- `./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en`
  compiles and runs; the CLI and results are identical to the Python reference.
- `spinor38/` — the Test 38 port, compiled and executed during v1.1.0
  preparation: isospectrality 3.4e-14, ⟨r⟩ = 0.4515710793 — VERDICT PASS;
  the folder contains the source and its README.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 10.7 KB | directory |
| `README.md` | 6.5 KB | file |
| `ab_cloud_verify.cpp` | 40.8 KB | file |
| `ab_cloud_verify_en.cpp` | 197 B | file |
| `ab_cloud_verify_ru.cpp` | 197 B | file |
| `run_verify.sh` | 956 B | file |
| **Total (recursive)** | **7 files, 60.2 KB** | |

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
disagrees with the Julia reference (`../../code/ab_cloud_full.jl`) or
with the other nine ports, the discrepancy is a bug in the port — the
data and the definitions are shared. CI exercises the interpreted
subset; the compiled ports are expected to be replayed locally with the
same one-line command shown above. The Test-38 companion lives in
`spinor38/` where present, and the spinor64 correction experiment — the
one that established 64/64 GUE-consistency for the Klein-quartic
structures — lives in `../spinor64/`.

<div align="center">

<img src="../../assets/svg/divider-cyan.svg" alt="—" width="100%" height="12"/>
<sub>⚡ Part of <a href="../../README.md">AB-Cloud Research</a> — numbers are verbatim from the unified registry; no result on this page is a claim about the Riemann hypothesis · <a href="../README.md">⬆ parent section</a></sub>

</div>
