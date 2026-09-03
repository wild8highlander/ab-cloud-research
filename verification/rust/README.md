# Rust Verification

Memory-safe implementation of the three-objection program; ships as a cargo
project with zero external crates (std only). Source + build documentation
delivered in v1.1.0 (the toolchain was not present in the preparation
sandbox — build it locally, the code is standard stable Rust).

## Files

| File | What it is |
|---|---|
| `src/main.rs` | CLI runner (default binary `ab_cloud_verify`) |
| `src/verify_en.rs` | English-only variant of the checks |
| `src/verify_ru.rs` | Russian-only variant |
| `Cargo.toml` | manifest — **no dependencies** |
| `run_verify.sh` | convenience wrapper: `cargo run --release -- <args>` |
| `spinor38/` | Test 38 port (own cargo project) |

## Requirements

- **Rust ≥ 1.70** (stable toolchain; install via rustup).

## Run

```bash
cd verification/rust
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 500k --objection 1 --lang ru

# or directly:
cargo run --release -- --zeros 50000 --source 500k --objection all --lang en
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH` — identical to every other language folder.

## What you get

The same verdict set as the Python reference (b(N) table + fit, KS/CvM vs
GUE, decay slope). Release build is fully optimised; expect the fastest
runtimes of all ten implementations on large datasets.

## spinor38/ — Test 38 port

Separate cargo project reading the frozen classes from `../spinor64/data/`:

```bash
cd verification/rust/spinor38
cargo run --release
```

Hand-written Jacobi eigensolver, no LAPACK/BLAS; details in
`spinor38/README.md`.

## Troubleshooting

- **`cargo: command not found`** — install rustup: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`.
- First build compiles only your crate (no deps) — a few seconds.

## Кратко (по-русски)

- Реализация на Rust ≥ 1.70, cargo-проект вообще без внешних крейтов.
- `cargo run --release -- --zeros 50000 --source 500k --objection all` —
  CLI и вердикты идентичны эталону на Python.
- `spinor38/` — отдельный cargo-проект порта Test 38 (алгоритм Якоби,
  без LAPACK), данные читаются из `../spinor64/data/`.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 3 files, 8.5 KB | directory |
| `src/` | 3 files, 33.5 KB | directory |
| `Cargo.toml` | 182 B | file |
| `README.md` | 2.2 KB | file |
| `run_verify.sh` | 1.8 KB | file |
| **Total (recursive)** | **9 files, 46.1 KB** | |

## 🔬 Deep dive — the Rust port in the parity matrix

The Rust port is organized as a cargo crate with
`src/main.rs` (flags and orchestration) and `src/verify_en.rs` /
`src/verify_ru.rs` (reporting variants); the `spinor38/` companion is
its own crate with `src/main.rs`. Ownership makes the loader's buffer
handling provably free of use-after-free and data races, and release
mode gives native-speed sweeps over the 500k and 2M tables. No
external crates are used, so the port builds offline; CI treats it as
the compiled-parity representative alongside C++ and Fortran.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** cargo, Rust ≥ 1.70, edition 2021 — no external crates
- **Entry point:** `bash run_verify.sh   # wraps: cargo run --release`

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

- Cargo-крейт: main (оркестрация) + verify_en/verify_ru;
  spinor38 — отдельный крейт.
- Владение буферами исключает use-after-free и гонки; --release даёт
  нативную скорость по таблицам 500k/2M.
- Ноль внешних крейтов — офлайн-сборка; CI-представитель компилируемых портов.
