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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 6.9 KB | directory |
| `Main.hs` | 2.9 KB | file |
| `README.md` | 2.5 KB | file |
| `VerifyEN.hs` | 7.2 KB | file |
| `VerifyRU.hs` | 7.8 KB | file |
| `ZerosLoader.hs` | 3.5 KB | file |
| `run_verify.sh` | 421 B | file |
| **Total (recursive)** | **8 files, 31.2 KB** | |

## 🔬 Deep dive — the Haskell port in the parity matrix

The Haskell port expresses the suite in pure functions
over loaded ordinate lists: `Main.hs` orchestrates, `ZerosLoader.hs`
parses the frozen tables, `VerifyEN.hs` and `VerifyRU.hs` produce the
reports. The type system turns the suite's guard conditions (positive
definiteness, monotonicity, bounds) into checked values, and the run
wrapper tries the interpreted path first so a referee without a
compiled toolchain still gets full output. Purity makes accidental
state leakage — the classic source of silent numeric drift —
structurally impossible here.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** GHC ≥ 9 — runhaskell for interpreted mode, ghc -O2 for compiled
- **Entry point:** `bash run_verify.sh   # prefers runhaskell, falls back to ghc`

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

- Набор как чистые функции над списками ординат: Main,
  ZerosLoader, VerifyEN/VerifyRU.
- Обёртка сначала пробует runhaskell — полный отчёт без компиляции.
- Чистота кода делает невозможной класс ошибок «утёкшее состояние».
