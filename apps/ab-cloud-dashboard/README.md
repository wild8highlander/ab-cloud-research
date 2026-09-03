# AB-Cloud Dashboard — React Application №1

Interactive real-time dashboard of the AB-Cloud verification suite.
React 18 + Vite, **no charting dependencies** — every plot is hand-rolled
SVG, so the whole app is a few source files with a tiny bundle.

## The three tabs

### 1. Run report (37 tests)

The verdict table of the two-pass run `run_20260902_134759` (Julia 1.12.0,
50 000 Odlyzko zeros, HARDCORE pass 2 at 96×96) loaded from
`public/data/run_summary.json`. Each row: test id, name, per-pass verdict
(PASS / WARN / FAIL), the WARN-band calibration note is displayed so nobody
mistakes calibrated warnings for failures.

### 2. Real-time ζ statistics

The same diagnostics as suite tests 1–5, 13, 14 — computed **live in a Web
Worker** from the embedded 50 000-zero dataset
(`public/data/zeta_zeros_50000_embedded.txt`):

- b(N) convergence table (N = 100 … 50 000) with the power-law fit;
- ⟨r⟩ with KS test against the **exact GUE ratio law** (not just the
  surmise);
- number variance Σ²(L) and spectral rigidity Δ₃(L).

The UI stays responsive while the worker crunches; sliders let you change
the sample size and unfolding parameters.

### 3. Test 38 — 64 spinors

The frozen spinor classes of `verification/spinor64/` with the **28
odd-structure spectra computed live in the browser** by a hand-written
cyclic-Jacobi eigensolver (port of Test 38, no LAPACK — plain JS on
`Float64Array`s). You can pick any structure and watch its spectrum match
the orbit representative to ≈ 1e-14 — a direct in-browser refutation of the
withdrawn v21 "idx=38 uniqueness" claim.

## Architecture

| Piece | Where | Notes |
|---|---|---|
| Pages | `src/pages/{RunReport,ZerosStats,Spinor64}.jsx` | one tab each |
| Worker | `src/worker/stats.worker.js` | all heavy numerics; posts progress messages |
| UI kit | `src/components/ui.jsx` | tables, badges, sliders (hand-rolled) |
| Data | `public/data/run_summary.json`, `public/data/zeta_zeros_50000_embedded.txt` | copied verbatim from `results/` and `verification/data/` at build time |
| Styles | `src/styles.css` | dark scientific theme |

## Run / build

```bash
cd apps/ab-cloud-dashboard
npm install
npm run dev        # Vite dev server
npm run build      # production build → dist/
npm run preview    # serve dist/ locally
```

The committed `dist/` is a ready-to-serve static build (GitHub Pages
compatible, relative base `./`). Data files are duplicated into
`dist/data/` at build time.

## Кратко (по-русски)

- Дашборд на React 18 + Vite без графических библиотек (весь рендер —
  рукописный SVG).
- Вкладка 1: вердикты 37 тестов прогона run_20260902_134759; вкладка 2:
  живые статистики ζ (b(N), ⟨r⟩ + KS против точного GUE-закона, Σ², Δ₃) в
  Web Worker на 50 000 нулей; вкладка 3: Test 38 — 64 спинора, спектры
  28 нечётных структур считаются в браузере алгоритмом Якоби (≈1e-14).
- `npm run dev` для разработки; `dist/` уже собран и готов к публикации.
