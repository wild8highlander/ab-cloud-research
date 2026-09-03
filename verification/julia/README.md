# Julia Verification

Thin wrapper around the canonical numerical ideas of the project in Julia —
the same language the main suite `code/ab_cloud_v19.jl` (37 tests) is written
in, but reduced to the three-objection CLI so results can be cross-checked
line-by-line against the other nine languages.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.jl` | bilingual module (zero loader, unfolding, KS/CvM, regression) |
| `ab_cloud_verify_en.jl` | English-only variant |
| `ab_cloud_verify_ru.jl` | Russian-only variant |
| `run_verify.jl` | standalone CLI runner |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **Julia ≥ 1.9** (1.12 used for the reference runs). Standard library only —
  `LinearAlgebra`, `Statistics`, `Random`. No `Pkg.add()` needed, the script
  starts instantly even offline.

## Run

```bash
cd verification/julia

# all objections on 500 000 Odlyzko zeros
julia run_verify.jl --zeros 500000 --source 500k --objection all --lang en

# quick GUE check
julia run_verify.jl --zeros 5000 --objection 2 --lang ru
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH` — identical to every other language folder.

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS/CvM p-values vs the GUE Wigner surmise, ⟨r⟩ with bootstrap
error, decay-slope CI, timestamped report. First invocation pays ~0.5 s of
JIT compilation; the rest is native speed.

## spinor38/ — Test 38 port

`spinor38/spinor38.jl` reads the frozen classes from `../spinor64/data/`,
rebuilds the 28 odd-orbit spectra with a hand-written cyclic-Jacobi
eigensolver and checks exact isospectrality + ⟨r⟩:

```bash
cd verification/julia/spinor38
julia spinor38.jl
```

## Relation to the main suite

For the **full 37-test two-pass protocol** (not just the three objections)
use the canonical suite: `julia code/ab_cloud_v19.jl --test all` from the
repository root — see [`../code/README.md`](../code/README.md). This folder
exists so that the objection-level numbers can be verified *independently*
of the big suite.

## Кратко (по-русски)

- Реализация на Julia ≥ 1.9 только со стандартной библиотекой — запускается
  мгновенно, без установки пакетов.
- `julia run_verify.jl --zeros 500000 --source 500k --objection all` — те же
  три возражения, что и в эталоне, CLI идентичен всем языкам.
- `spinor38/` — Порт Test 38: замороженные данные + собственный алгоритм
  Якоби.
- Полный 37-тестовый прогон — в `code/ab_cloud_v19.jl` (другой каталог
  репозитория).

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 5.1 KB | directory |
| `README.md` | 2.8 KB | file |
| `ab_cloud_verify.jl` | 16.1 KB | file |
| `ab_cloud_verify_en.jl` | 6.8 KB | file |
| `ab_cloud_verify_ru.jl` | 8.4 KB | file |
| `run_verify.jl` | 2.6 KB | file |
| **Total (recursive)** | **7 files, 41.8 KB** | |

## 🔬 Deep dive — the Julia port in the parity matrix

The Julia port is the closest sibling of the canonical
research suite `../../code/ab_cloud_v19.jl` — the code that produced
the two-pass flagship run `results/run_20260902_134759` (50 000
Odlyzko zeros, pass 2 "HARDCORE" at 96×96). Same array semantics, same
statistics definitions, same report wording; if you want to trace a
monograph number to executable code, this folder is the shortest path.
The folder also hosts `spinor38/`, the Julia port of Test 38, keeping
the whole research narrative inside one language when convenient.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** Julia ≥ 1.9 (the flagship run used 1.12.0) — LinearAlgebra from stdlib
- **Entry point:** `julia run_verify.jl [flags]`

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

- Наиболее близок к каноническому исследовательскому набору
  `code/ab_cloud_v19.jl`, породившему двухпроходный прогон v19.
- Кратчайший путь от числа в монографии к исполняемому коду.
- Рядом — порт Теста 38 (`spinor38/`).
