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
