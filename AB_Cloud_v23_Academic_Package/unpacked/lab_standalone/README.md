# `lab_standalone/` — The Standalone Research Codes (Julia)
> Three self-contained Julia programs: the full v3.3 verification suite (32,095 lines), the finite-size Test 34 laboratory (v1.3), and the HP·MERIDIAN H-audit module.

_Location: [unpacked/](../README.md) › [lab_standalone/](README.md)_

This folder is the computational heart of the package: the Julia programs that produced every number in the run archives. All three are **standalone** — each is a single self-contained `.jl` file running on Julia ≥ 1.9 with standard-library dependencies only, so a reproduction attempt needs no package installation beyond Julia itself. The original package README for this folder is preserved as `README_original.md` (its provenance table remains accurate for v34).

## The three programs

**`ab_cloud_v23.jl` — the full SUPERCOMBO suite, v3.3 working copy (32,095 lines).** The complete verification apparatus of the reference run: all 38 tests with their HARDCORE pass-2 audits, the SERIES passes of Tests 19/29/31, the two-pass verdict algebra, the report writer (MD/HTML/PDF/DOCX), the ABPlotV23 plot engine, the physics and 3-D laboratories, and — new in v3.3 — the **TEST 34G geometry sweep (Test 39)** that ports the finite-size laboratory into the suite and runs seven closed surfaces per invocation with pooled + UNIVERSAL verdicts. This is the same build reproduced verbatim in Appendix B of the monograph, and the program that executed `run_20260914_234626`.

**`finite-size_lab.jl` — the Test 34 standalone laboratory, v1.3 (5,177 lines).** The interactive/CLI instrument dedicated to the direct AB-cloud versus ζ-zeros confrontation. Five modes: 1 NORMAL, 2 HARDCORE (ensemble pass with MAD-outlier census and leave-one-out stability), 3 DEEP DIAG (differential CDF, short-range zone, seed forensics, finite-size probe, bootstrap), 4 CONFIGURATOR sweeps, and 5 UNIVERSAL — the geometry sweep across torus, Klein bottle, pillow orbifold, cube sphere and the Hurwitz surfaces PSL(2,7), PSL(2,8), PSL(2,13) and PSL(2,27), every scalable geometry auto-stretched to the L² site budget. Version 1.3 adds the voltage-lift stretching of all Hurwitz geometries with the heptagon flux preserved bit-for-bit. This laboratory produced the three September 2026 runs published under `run_data/`.

**`hp_audit_standalone.jl` — HP·MERIDIAN v24.1-SA (6,054 lines).** The compact Hilbert–Pólya deep-audit module (menu `h` tests only), carved out of the monolithic suite so the H-check battery can evolve independently between package freezes.

## Reproduction quick reference

```bash
julia ab_cloud_v23.jl --test all            # full suite (reference protocol)
julia ab_cloud_v23.jl --test 34 --no-two-pass   # single test re-run
julia finite-size_lab.jl --mode=2 --headless    # HARDCORE ensemble pass
julia finite-size_lab.jl --mode=5 --headless    # universal geometry sweep
julia hp_audit_standalone.jl                    # H-audit menu
```

A typical full-suite session of the reference scale runs for tens of hours on a single machine (the reference run took 26.04 h); the laboratories' individual modes are minutes-to-hours scale. The Python reimplementation in [`../python_clone/`](../python_clone/README.md) offers a dependency-light cross-check of all 38 tests.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `README_original.md` | 2.5 KB · 25 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `ab_cloud_v23.jl` | 2.1 MB · 32095 lines | The full SUPERCOMBO verification suite, v3.3 working copy — all 38 tests, HARDCORE audits, TEST 34G geometry sweep (Test 39); the Appendix B source of the monograph. |
| `finite-size_lab.jl` | 233.2 KB · 5177 lines | The Test 34 standalone laboratory, v1.3 — modes 1–5, eight geometries incl. PSL(2,27); produced the three September 2026 runs. |
| `hp_audit_standalone.jl` | 310.8 KB · 6054 lines | HP·MERIDIAN v24.1-SA — the standalone Hilbert–Pólya deep-audit module (menu h tests). |

## Provenance of the September 2026 runs

| Run (in `run_data/`) | Produced by | Headline |
|---|---|---|
| `run_20260917_080329_m2` | `finite-size_lab.jl` MODE 2, torus 96×96, 20 realizations | pooled D = 0.0970 |
| `run_20260917_084900_m3` | `finite-size_lab.jl` MODE 3, same protocol | D(L) flat, mixture w* ≈ 0.25 |
| `run_20260919_085734_m2` | `finite-size_lab.jl` MODE 2, **Klein quartic PSL(2,7)**, 100,000 zeros | pooled D = 0.0808, d_GUE = 0.0044 — GUE-CONSISTENT |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._