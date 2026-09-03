# AB-Cloud Dashboard — React application №1

Interactive real-time dashboard of the AB-Cloud verification suite
(React 18 + Vite, no chart dependencies — hand-rolled SVG).

Tabs:
1. **Run report (37 tests)** — verdicts of the two-pass run
   `run_20260902_134759` (Julia 1.12, 50,000 Odlyzko zeros, HARDCORE
   pass-2), with the WARN-calibration note.
2. **Real-time ζ statistics** — the same diagnostics as suite tests 1–5,
   13, 14 computed live in a Web Worker from the embedded 50,000-zero
   dataset: b(N) convergence, ⟨r⟩ + KS vs the exact GUE ratio law,
   Σ²(L), Δ₃(L).
3. **Test 38 — 64 spinors** — the frozen spinor classes of
   `verification/spinor64/` with the 28 odd-structure spectra computed
   live by a hand-written Jacobi eigensolver (isospectrality ≈ 1e-14;
   corrects the v21 "idx=38 uniqueness" claim).

## Run / build

```bash
npm install
npm run dev        # local dev server
npm run build      # static build to dist/
npm run preview
```

The committed `dist/` is a ready-to-serve static build (GitHub Pages
compatible, relative base `./`).
