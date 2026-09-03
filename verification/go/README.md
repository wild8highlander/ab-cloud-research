# Go Verification

Concurrency-friendly Go implementation — standard library only.

## Files

| File | What it is |
|---|---|
| `main.go` | CLI runner + bilingual output |
| `zeros.go` | the shared `load_zeros(dataDir, count, source)` loader |
| `verify_en.go` | English-only check set |
| `verify_ru.go` | Russian-only check set |
| `run_verify.sh` | convenience wrapper (`go run .`) |
| `spinor38/` | Test 38 port — own module (`go.mod`) + README |

## Requirements

- **Go ≥ 1.21** — stdlib only (`os`, `bufio`, `math`, `sort`, `fmt`);
  `go build` works fully offline.

## Run

```bash
cd verification/go
chmod +x run_verify.sh
./run_verify.sh --zeros 50000 --source 500k --objection all --lang ru

# or directly:
go run . --zeros 50000 --source 500k --objection 1 --lang en
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH`.

## What you get

The same verdict set as the Python reference: b(N) convergence table with the
power-law fit, KS/CvM p-values against the GUE Wigner surmise, ⟨r⟩ with
bootstrap error, decay slope with 95% CI, timestamped report. Go's deterministic
`math/rand` seeding keeps bootstrap reruns reproducible.

## spinor38/ — Test 38 port

Self-contained module (own `go.mod`, so it never fights the parent folder's
module scope):

```bash
cd verification/go/spinor38
go run .
```

Reads the frozen classes from `../spinor64/data/`, rebuilds the 28 odd-orbit
spectra with a hand-written cyclic-Jacobi eigensolver; details in
`spinor38/README.md`.

## Кратко (по-русски)

- Реализация на Go ≥ 1.21, только стандартная библиотека — `go run` работает
  офлайн.
- `go run . --zeros 50000 --source 500k --objection all --lang ru` — CLI и
  вердикты идентичны эталону на Python.
- `spinor38/` — отдельный Go-модуль порта Test 38 (свой `go.mod`, алгоритм
  Якоби без LAPACK).

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 3 files, 7.7 KB | directory |
| `README.md` | 2.0 KB | file |
| `main.go` | 2.1 KB | file |
| `run_verify.sh` | 78 B | file |
| `verify_en.go` | 7.1 KB | file |
| `verify_ru.go` | 8.0 KB | file |
| `zeros.go` | 3.5 KB | file |
| **Total (recursive)** | **9 files, 30.5 KB** | |

## 🔬 Deep dive — the Go port in the parity matrix

The Go port is split into small files by role — `main.go`
(flags and orchestration), `zeros.go` (the loader), `verify_en.go` and
`verify_ru.go` (reporting variants) — mirroring how the suite is
organized in the compiled ports while staying one `go run .` away from
execution. The module has no external dependencies, so the port builds
offline from a fresh clone; `spinor38/` carries its own `go.mod` for
the same reason. This is the port that demonstrates the suite runs
identically under a garbage-collected runtime with a stricter
compiler-enforced style.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** Go ≥ 1.20 — standard library only, zero module dependencies
- **Entry point:** `bash run_verify.sh   # wraps: go run .`

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

- Разбит по ролям: main (оркестрация), zeros (загрузчик),
  verify_en/verify_ru (варианты отчёта) — как в компилируемых портах.
- Ноль внешних зависимостей: собирается офлайн из свежего клона.
- Демонстрирует паритет под GC-рантаймом со строгим стилем компилятора.
