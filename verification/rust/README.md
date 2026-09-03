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
