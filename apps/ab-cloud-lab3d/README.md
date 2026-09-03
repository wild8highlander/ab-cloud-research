# AB-Cloud Lab 3D — React application №2

Interactive WebGL laboratory (React 18 + Vite + Three.js) visualizing the
3D-1…3D-34 experiments of the Julia suite:

1. **Hofstadter lattice** — L×L lattice with Landau-gauge phases (site bars
   colored by 2πα·j) and q=+1 vortices (red flux cones); the suite's GUE
   mechanism (:monumental phase field).
2. **Dirac cone** — E(k) = v_F·|k| linear dispersion at α = 1/2 (tests
   19/30, v_F(2π) = 1.9).
3. **ζ critical strip** — |ζ(σ+it)| surface with the critical line and the
   embedded zeros γ₁…γ₁₅; the ζ evaluator is a self-anchored
   Euler–Maclaurin port of experiment 3D-34 (JS self-check anchors:
   ζ(2), ζ(4), ζ(1/2)).

## Run / build

```bash
npm install
npm run dev        # local dev server
npm run build      # static build to dist/
npm run preview
```

The committed `dist/` is a ready-to-serve static build (GitHub Pages
compatible, relative base `./`).
