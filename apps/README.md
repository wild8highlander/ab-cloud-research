# apps — Two Interactive React Applications

Two self-contained web apps (React 18 + Vite) that make the project's
results explorable in a browser — no server, no Python, no Julia required.
Both ship **prebuilt static bundles** in `dist/` (committed, GitHub Pages
ready, relative base `./`), so you can serve them with any static file
server or open the Pages deployment directly.

| App | What it shows | Source | Prebuilt |
|---|---|---|---|
| [`ab-cloud-dashboard/`](ab-cloud-dashboard) | 37-test verdict dashboard + real-time ζ statistics (Web Worker) + in-browser 64-spinor Jacobi verification | `src/` | `dist/` |
| [`ab-cloud-lab3d/`](ab-cloud-lab3d) | WebGL 3D laboratory: Hofstadter lattice with vortices, Dirac cone, ζ critical strip (Three.js) | `src/` | `dist/` |

## Run from source

```bash
# app 1 — dashboard
cd apps/ab-cloud-dashboard
npm install
npm run dev          # Vite dev server with HMR
npm run build        # production build → dist/
npm run preview      # serve the production build locally

# app 2 — 3D laboratory
cd ../ab-cloud-lab3d
npm install && npm run dev
```

No environment variables, no backend; the heavy data (50 000 zeros, run
summary, frozen spinor data) is bundled into each app's `public/data/` and
`dist/data/`.

## Deploying to GitHub Pages

Each `dist/` is built with a relative base, so the folders can be served
from any path — e.g. via Pages from the `/docs` root, from a `gh-pages`
branch, or by copying `dist/` to any static host. Serving locally:
`npm run preview` or `python3 -m http.server -d apps/ab-cloud-dashboard/dist`.

## Кратко (по-русски)

- Два React-приложения (React 18 + Vite): дашборд 37 тестов с реальным
  временем (Web Worker) и браузерная спинор-проверка; и 3D-лаборатория на
  Three.js.
- Собранные статики уже в `dist/` (GitHub Pages-совместимы); из исходников —
  `npm install && npm run dev`.
- Данные (50 000 нулей, сводка прогона, замороженные спинор-данные)
  включены в приложение.
