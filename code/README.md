# Canonical Julia Suite — `ab_cloud_v23.jl` (39 Tests, Two-Pass Protocol)

![Julia](https://img.shields.io/badge/Julia-1.10%2B-9558B2?style=flat-square&logo=julia&logoColor=white)
![Tests](https://img.shields.io/badge/tests-39%20%C3%97%202%20passes-2EA043?style=flat-square)
![Deps](https://img.shields.io/badge/dependencies-stdlib%20only-2EA043?style=flat-square)
![CI](https://img.shields.io/github/actions/workflow/status/wild8highlander/ab-cloud-research/julia.yml?branch=main&style=flat-square&label=Julia%20CI)

This folder holds the **canonical numerical program** of the project: a
single-file, dependency-free Julia suite that produces every number the
monographs quote. Language: Julia ≥ 1.10 (reference runs: Julia 1.12.0);
stdlib only — nothing to `Pkg.add()`.

## Files

| File | Size | What it is |
|---|---|---|
| `ab_cloud_v23.jl` | 32 095 lines | **canonical suite (v23)** — 39 registered tests, two-pass protocol, report engine (md/html/pdf/docx/png/gif), interactive menu, Physics Lab (H1–H7 gates), 3D lab, Test-34G geometry sweep |
| `RH_Unified_D.jl` · `RH_Sweep_Pro_D.jl` | ~8 800 lines | standalone RH sweep benches |
| `hp_audit_standalone.jl` | 6 054 lines | standalone Hilbert–Pólya audit battery |
| `julia/` | v23 provenance copy | suite provenance archive — see `julia/README.md` |

## The 39 tests, grouped

| Group | Tests | Verifies |
|---|---|---|
| Convergence | 1–3 | b(N) = (1/N)Σ\|γₖ−γ̃ₖ\| — table, monotonicity, rate; b(50000) = 1.2126, empirical law b(N) ≈ 7.0312·N^(−0.1685) (R² = 0.9895) |
| GUE statistics | 4–5, 9–17 | KS/CvM vs the GUE surmise, ⟨r⟩ = 0.5848 ± 0.0260 (GUE 0.5992), Σ²(L), Δ₃(L), K(τ), bootstrap CIs |
| Physics of the cloud | 6–8, 18–22 | Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality zero modes, AIII class, Dirac cone v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0) |
| Spinor / topology | 23–28 | Arf invariant, PSL(2,7) orbit structure, zero-mode counts 2/3/3/3/7 |
| Robustness | 29–38 | chaos/decay rate, half-factorial γ, byte-level robustness, form factor K(τ), residual diagnostics, Test 38 — 64-spinor isospectrality |
| Geometry sweep | 39 | **TEST 34G** — Test 34 laboratory ported onto 7 closed surfaces: torus, Klein bottle, pillow orbifold, cube sphere, Hurwitz PSL(2,7)/PSL(2,8)/PSL(2,13) magnetic Cayley graphs |

(Verdict semantics: PASS / WARN / FAIL against thresholds printed with each
test; the WARN band is calibration, documented in the run reports.)

## Running

```bash
# smoke run: one test on the embedded 50 000-zero dataset, ~1 min
julia code/ab_cloud_v23.jl --test 1

# the full two-pass 39-test suite (30–60 min, 50 000 zeros, 72×72 → 96×96)
julia code/ab_cloud_v23.jl --test all

# one test only, single pass
julia code/ab_cloud_v23.jl --test 33 --no-two-pass

# TEST 34G geometry sweep with knobs
julia code/ab_cloud_v23.jl --test 39 --t34g-l 96 --t34g-reps 2 --t34g-geoms all

# interactive menu: 39 tests + Physics Lab (H-gates) + 3D lab
julia code/ab_cloud_v23.jl
```

The embedded 50 000-zero dataset means the suite runs out of the box; to
point it at larger frozen datasets use `--data-dir verification/data`.

## CLI flags (selection)

| Flag | Effect |
|---|---|
| `--test N` / `--test all` | run one test / the whole suite |
| `--data-dir DIR` | where the frozen ζ datasets live |
| `--output-dir DIR` | where run reports are written |
| `--no-two-pass` | single pass (pass 1 only) |
| `--t34g-l / --t34g-reps / --t34g-geoms` | Test 34G geometry-sweep knobs |
| `--t38-quick` | Test 38 smoke mode (tiny lattices) |
| `--lang en / ru` | UI language |
| `--help` | full flag list |

## Two-pass protocol

Every test runs twice: a fast **pass 1**, then a **hardcore pass 2** with
tightened tolerances and sub-check decomposition; selected tests add a
**series pass 3**. A WARN in pass 1 is not a failure — it flags a
finite-size/calibration effect that pass 2 re-derives at sub-check level.
The stored flagship run (v19 era, 2026-09-02) is documented in
[`results/README.md`](../results/README.md) with 202 machine verdict lines.

## Historical note

The v19/v20/v21 historical sources were consolidated: the canonical suite is
now v23 (the change history lives in the file header — v3.1 → v3.7
changelogs), and the flagship-run artifacts of the v19 era remain committed
under `results/` exactly as produced. The v23 provenance copy lives in
[`code/julia/`](julia/).
