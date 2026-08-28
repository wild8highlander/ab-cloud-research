---
title: Quick start
---

# Quick start

## 1. Get the repository

```bash
git clone https://github.com/wild8highlander/ab-cloud-research.git
cd ab-cloud-research
```

## 2. Julia suite — the canonical numerics

Julia **≥ 1.10** is required; the suite is **dependency-free** (no `Pkg.add` needed).

```bash
julia code/ab_cloud_v19.jl --quick     # 16×16 → 32×32, ζ ≤ 5000, both passes (~3–5 min)
julia code/ab_cloud_v19.jl --test all  # full two-pass 37-test suite (30–60 min)
julia code/ab_cloud_v19.jl             # interactive menu (37 tests + Physics Lab + 3D lab)
```

In the interactive menu:

- keys `1..37` — individual tests; `a` — run all;
- `f` — quick check (the same `--quick` protocol);
- `l` — Physics Lab (22 experiments: vortex layouts, e⁻/e⁺ interferometry,
  hydrodynamics, Hadamard walk, AB-cloud 2D/3D maps);
- `3` — 3D laboratory (30 tests).

## 3. Ten-language verification

```bash
cd verification/python
python3 ab_cloud_verify.py --zeros ../data/zeta_zeros_50000.txt
```

Choose your language in `verification/` (cpp, fortran, go, haskell,
javascript, julia, matlab, python, r, rust) — each implements the same
protocol with the same output format.

## 4. 3D laboratory

```bash
cd lab-3d
pip install -r requirements.txt
make run
```

## What to expect

The `--quick` protocol prints verdicts for the reduced configuration and
writes full logs and reports (`md/html/pdf/docx/png`) next to the suite —
every number can be re-verified independently.
