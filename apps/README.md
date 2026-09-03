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

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `ab-cloud-dashboard/` | directory, 21 files inside | folder |
| `ab-cloud-lab3d/` | directory, 13 files inside | folder |
| `README.md` | 2.1 KB | markdown guide |
| **Total (files)** | **2.1 KB** | 1 files + 2 subdirectories |

## 🔬 Deep dive — what the two applications are for

The repository ships **two independent React applications**, and a subtle
design decision matters here: **both apps are committed prebuilt**
(`ab-cloud-dashboard/dist/` and `ab-cloud-lab3d/dist/`). That means the
apps can be served as static files — GitHub Pages, any static host, or a
local `python3 -m http.server` — **without Node, without npm, without a
build step**. On a phone, in a review meeting, or ten years from now, the
bundles still open; the source next to them guarantees they can be
rebuilt, audited and modified.

The division of labour between the two apps mirrors the division between
*reading the evidence* and *playing with the physics*:

- **ab-cloud-dashboard** is the evidence reader: the verification results,
  the test ledger, the dataset charter and the monograph metadata in a
  point-and-click interface. If a number in a talk looks suspicious, the
  dashboard is the fastest way to trace it to the artifact that produced it.
- **ab-cloud-lab3d** is the physics playground: the 3D lattice laboratory
  in the browser — Hofstadter surfaces and vortex textures you can rotate,
  zoom and re-parameterise, matching the offline pipelines in `lab-3d/`.

Both apps read from the same committed evidence as everything else in the
repository; neither contains private copies of the numbers. A figure in
the dashboard and the corresponding PNG in the monograph directory trace
back to the same run artifact — that is the whole integrity model of the
project, extended to the browser.

### Serving locally

```bash
cd apps/ab-cloud-dashboard && python3 -m http.server 8080 -d dist
cd apps/ab-cloud-lab3d   && python3 -m http.server 8081 -d dist
```

Then open `http://localhost:8080` / `:8081`. Rebuilding from source
requires Node 18+: `npm ci && npm run build` inside the app folder.
