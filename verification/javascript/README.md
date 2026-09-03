# JavaScript / Node.js Verification

Browser-free Node.js implementation — compiled **and executed** during the
v1.1.0 preparation together with the C++ build, cross-checking the frozen
Test-38 numbers in a second independent runtime.

## Files

| File | What it is |
|---|---|
| `ab_cloud_verify.js` | bilingual ES-module-style script (CommonJS-compatible) with loader, unfolding, KS/CvM, regression |
| `ab_cloud_verify_en.js` | English-only variant |
| `ab_cloud_verify_ru.js` | Russian-only variant |
| `run_verify.js` | standalone CLI runner |
| `spinor38/` | Test 38 port (see below) |

## Requirements

- **Node.js ≥ 18** — no `npm install`, zero dependencies.

## Run

```bash
cd verification/javascript

# all objections, 50 000 zeros
node run_verify.js --zeros 50000 --source 50k --objection all --lang en

# GUE-only quick check
node run_verify.js --zeros 5000 --objection 2 --lang ru
```

CLI: `--zeros N`, `--source NAME`, `--objection 1/2/3/all`, `--lang en/ru`,
`--data-dir PATH`.

## What you get

Same verdict set as the Python reference: b(N) table + power-law fit, KS/CvM
p-values vs the GUE surmise, ⟨r⟩ with bootstrap CI, decay slope; timestamped
text report. V8's double arithmetic agrees with C++/Python to ~1e-12 on the
b(N) tables.

## spinor38/ — Test 38 port (compiled & PASSed)

| Item | Value |
|---|---|
| Source | `spinor38/spinor38.js` |
| Verified result | isospectrality **3.4e-14**, ⟨r⟩ = **0.4515710793** — **VERDICT PASS** |

```bash
cd verification/javascript/spinor38
node spinor38.js       # reads ../../spinor64/data/ frozen files
```

The port uses a hand-written cyclic-Jacobi eigensolver on plain
`Float64Array`s — no math libraries — and reproduces the C++ result exactly.

## Notes

- If you want the *browser* experience instead of CLI, use the React
  dashboard app `../../apps/ab-cloud-dashboard/` — it computes the same ζ
  statistics live in a Web Worker.

## Кратко (по-русски)

- Реализация на Node.js ≥ 18 без единой зависимости (`npm install` не нужен).
- `node run_verify.js --zeros 50000 --source 50k --objection all` — те же три
  возражения, что и в эталоне; результаты совпадают с C++ до ~1e-12.
- `spinor38/` — Порт Test 38: прогнан при подготовке v1.1.0 вместе с C++,
  изоспектральность 3.4e-14, ⟨r⟩ = 0.4515710793 — PASS; алгоритм Якоби
  написан с нуля на Float64Array.
