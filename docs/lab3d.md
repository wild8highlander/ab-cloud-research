---
title: 3D lattice laboratory
---

# The 3D lattice laboratory

`lab-3d/` accompanies the preprint *"AB-Cloud: A Universal Lattice Operating
System for the Riemann Zeros"*.

## What it is

A **three-dimensional** non-Hermitian Hofstadter Hamiltonian with
topological **vortex lines** (instead of point vortices):

- 36³ lattices, Payerls phases e^(2πiαy), 5000 embedded ζ zeros;
- Python implementation (with Julia bridge), `requirements.txt` included;
- `data/` — embedded zeros; `outputs/` — complete generated reports
  (July 2026 runs: `3d_bridge`, `full_verification`, `3d_advanced`,
  `deep_zeros`); `preprint/` — the preprint source and PDF.

## Running

```bash
cd lab-3d
pip install -r requirements.txt
make run          # see lab-3d/Makefile for all targets
```

See `lab-3d/README.md` for the full description of the model and the
verification tasks.
