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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `spinor38/` | 2 files, 6.3 KB | directory |
| `README.md` | 2.5 KB | file |
| `ab_cloud_verify.js` | 15.5 KB | file |
| `ab_cloud_verify_en.js` | 9.6 KB | file |
| `ab_cloud_verify_ru.js` | 10.5 KB | file |
| `run_verify.js` | 3.9 KB | file |
| **Total (recursive)** | **7 files, 48.4 KB** | |

## 🔬 Deep dive — the JavaScript / Node.js port in the parity matrix

The JavaScript port is the bridge to the web layer of the
project: the same statistics definitions that the React dashboard and
the 3D lab render visually are exercised here against the same frozen
tables, in the language those apps are written in. It runs on bare
Node — no package installation, no build step — which makes it the
quickest interactive check on a machine without compilers. The
`spinor38/` port mirrors the validated C++ reference exactly, as in
every other language folder.

## ▶ Running — toolchain, entry point, flags

- **Toolchain:** Node.js ≥ 18 — no npm packages
- **Entry point:** `node run_verify.js [flags]`

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

- Мост к веб-слою проекта: те же определения статистик, что
  рендерят дашборд и 3D-лаборатория, против тех же таблиц.
- Голый Node: без npm, без сборки — самая быстрая интерактивная проверка.
- Порт spinor38 зеркалит валидированный C++-эталон.
