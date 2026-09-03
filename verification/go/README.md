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
