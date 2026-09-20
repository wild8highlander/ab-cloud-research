# lab_standalone/ — standalone research codes (September 2026, v34 package)

| File | What it is | Lines |
|---|---|---|
| `finite-size_lab.jl` | **Test 34 standalone laboratory, v1.3** — interactive/CLI instrument for the direct AB-cloud vs ζ-zeros confrontation. Modes: 1 NORMAL, 2 HARDCORE (ensemble pass, MAD outliers, leave-one-out), 3 DEEP DIAG (differential CDF, short-range zone, seed forensics, finite-size probe, bootstrap), 4 CONFIGURATOR sweeps, **5 UNIVERSAL (geometry sweep: every geometry × tests 1–4)**. Geometries: torus, Klein bottle, pillow orbifold, cube sphere, and the Hurwitz surfaces PSL(2,7), PSL(2,8), PSL(2,13), **PSL(2,27)** — every scalable geometry auto-stretches to the L² site budget (v1.1–v1.3 big-matrix fixes: Z-k voltage lifts with the heptagon flux preserved bit-for-bit). Julia ≥ 1.9, stdlib only. Produced runs `run_20260917_080329_m2`, `run_20260917_084900_m3` and `run_20260919_085734_m2` (in `run_data/`). | 5,177 |
| `ab_cloud_v23.jl` | Full SUPERCOMBO suite, **v3.3 working copy** — v3.2 estimator-validity patch series (BF-02…BF-06, canonical ζ-side unfolding) plus the v3.3 **TEST 34G geometry sweep (Test 39)**: the finite-size laboratory ported into the suite, seven closed surfaces per run, big-matrix parity with the lab, pooled + UNIVERSAL verdicts. Same reference build that is reproduced in Appendix B of the monograph. | 32,095 |
| `hp_audit_standalone.jl` | **HP·MERIDIAN v24.1-SA** — compact standalone module for the Hilbert–Pólya deep audit (menu `h` tests only), carved out of the suite so the H-checks can evolve independently of the monolithic code. | 6,054 |

Usage:

```bash
julia finite-size_lab.jl --mode=2 --headless          # HARDCORE ensemble pass
julia finite-size_lab.jl --mode=5 --headless          # universal geometry sweep
julia ab_cloud_v23.jl --test 39 --no-two-pass         # suite TEST 34G geometry sweep
julia ab_cloud_v23.jl --test 34 --no-two-pass         # suite Test 34 re-run
julia hp_audit_standalone.jl                          # H-audit menu
```

Run provenance (September 2026 addendum series):

* `run_20260917_080329_m2` — torus 96×96, 20 realizations, 50,000 zeros; pooled D = 0.0970.
* `run_20260917_084900_m3` — MODE 3 deep diagnostics on the same protocol.
* `run_20260919_085734_m2` — **Klein quartic PSL(2,7)** (Cayley |G|=168 ×56 lift, 9,408
  sites), 5 realizations, **100,000 zeros**; pooled D = 0.0808, d_GUE = 0.0044,
  plateau = 0.9734; composite criterion satisfied (GUE-CONSISTENT), ensemble STABLE.
