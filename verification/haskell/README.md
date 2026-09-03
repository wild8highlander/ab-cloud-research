# Haskell Verification

Pure-GHC implementation of the three-objection program — `base` and
`containers` only, no heavy libraries.

## Files

| File | What it is |
|---|---|
| `Main.hs` | CLI runner + bilingual report writer |
| `ZerosLoader.hs` | the shared zero-loading contract (`loadZeros :: FilePath -> Int -> Source -> IO [Double]`) |
| `VerifyEN.hs` | English-only check set |
| `VerifyRU.hs` | Russian-only check set |
| `run_verify.sh` | convenience wrapper (`ghc --make` + exec) |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **GHC ≥ 9** / **cabal** or **stack** — packages outside `base`/`containers`
  are not used.

## Run

```bash
cd verification/haskell
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en

# or manually:
ghc -O2 -o verify_ru VerifyRU.hs ZerosLoader.hs && ./verify_ru --zeros 5000
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH`.

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS/CvM p-values against the GUE Wigner surmise, ⟨r⟩ with
bootstrap error, decay slope with 95% CI, timestamped report. All statistics
are written in explicit double arithmetic (`Double`), so cross-language
agreement stays at the 1e-12 level.

## spinor38/ — Test 38 port

`spinor38/Main.hs` reads the frozen classes from `../spinor64/data/` and
rebuilds the 28 odd-orbit spectra with a hand-written cyclic-Jacobi
eigensolver on strict unboxed doubles:

```bash
cd verification/haskell/spinor38
ghc -O2 -o spinor38 Main.hs && ./spinor38
```

Details and the frozen-data contract: `spinor38/README.md` and
[`../spinor64/README.md`](../spinor64/README.md).

## Troubleshooting

- **`ghc: command not found`** — install GHCup (`curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh`) or `apt install ghc`.
- Compilation is single-shot (`ghc --make`); no cabal project file is needed
  on purpose, to keep the folder copy-paste friendly.

## Кратко (по-русски)

- Реализация на GHC ≥ 9 — только `base` и `containers`, без внешних пакетов.
- `./run_verify.sh --zeros 50000 --source 50k --objection 1 --lang en` —
  компилирует одной командой `ghc --make` и запускает; CLI как у всех языков.
- `spinor38/` — Порт Test 38: алгоритм Якоби на строгих unboxed Double,
  замороженные данные из `../spinor64/data/`.
