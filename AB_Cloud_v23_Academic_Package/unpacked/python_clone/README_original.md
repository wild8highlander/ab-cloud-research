# AB-Cloud v23 SUPERCOMBO — Python Clone

A faithful, dependency-light **Python reimplementation** of the Julia
verification suite `ab_cloud_v23.jl` (AB-Cloud v23 SUPERCOMBO): all **38
tests**, the two-pass verdict algebra, report generation and plotting.

Author of the original suite and of this reimplementation:
**Isaev Iskhak Khamzatovich** (ORCID [0009-0003-7299-0701](https://orcid.org/0009-0003-7299-0701))

Part of the monograph submission package
*"An Aharonov–Bohm Lattice Operator Framework for the Riemann ζ Zeros: A
38-Test Computational Verification Suite"*.

---

## Quick start

```bash
pip install -r requirements.txt

python -m abcloud.cli --list                     # list the 38 tests
python -m abcloud.cli --test 1 --no-two-pass     # single test, single pass
python -m abcloud.cli --test 1-14                # statistics family (fast)
python -m abcloud.cli --test all                 # full suite (fast profile)
python -m abcloud.cli --test 1-14 --zeros 50000  # reference-scale statistics
python -m abcloud.cli --test all --full          # reference-scale everything
```

Outputs land in `results_py/` (configurable via `--out`): per-test folders
`test_XX_<slug>/report.md` + `plots/plot_01.png`, `plots/plot_02.png`, and a
master `final_report.md` + `results.json`.

## What is implemented

| Family | Tests | Status |
|--------|-------|--------|
| Gram-point approximation `b(N)` | 1–3 | full equivalence (same statistic, same H0–H7 sub-checks; peak \|Δγ̃\| = 9.0356 and b(50000) = 1.2128 vs the Julia run's 1.2126 reproduced) |
| GUE distributional tests | 4–6, 11, 12 | full equivalence (strict + effect-size dual criteria; large-n rejection documented) |
| Decay-law robustness | 7–10 | full equivalence |
| RMT global statistics | 13, 14 | full equivalence (disjoint-window Σ²(L), Δ₃(L)) |
| AB construction & gauge | 15, 22, 24, 25, 26 | structural equivalence (loop-product flux audit, string-gauge audit, Byers–Yang) |
| Topological probes | 17–20 | structural equivalence (projector-FHS Chern numbers, Dirac touching at α = 1/2 reproduced to 1e-15) |
| Phase / fractal constants | 21, 23 | exact analytic equivalence (arg γ* = 89.874°, \|CF\| = 1, β_imag = 2.854) |
| Scaling & disorder | 16, 28–36 | structural equivalence; see "Known deviations" |
| Cross-domain comparison | 34, 35 | structural equivalence; see "Known deviations" |
| Auxiliary constants | 37 | exact analytic equivalence ((1/2)! = √π/2, 32/π², ∫p₂ = 1) |
| Vortex-flux magnet | 38 | structural equivalence (2-D Ising universality class, T_c from the susceptibility peak) |

## Data

The clone ships the **same embedded 50,000-zero dataset** as the Julia
original (`abcloud/data/zeta_zeros_50000.txt`, extracted verbatim from
`EMBEDDED_ZEROS_50K_STR`, `ab_cloud_v23_v3.jl` line 4679). The reference
run's statistics are therefore recomputed on the identical data. Zeros above
50,000 (only needed with `--zeros >50000`) are computed via mpmath and cached.

## Two-pass verdict algebra

Exactly as in the Julia suite:

* **pass 1** — primary/standard implementation and acceptance windows;
* **pass 2** — HARDCORE deep validation (secondary lattice size / RNG stream,
  effect-size windows where documented);
* overall verdict = pass1 AND pass2; every pass writes its own verdict line,
  so the master report counts **entries** the same way the reference run
  counts its 79 entries.

A runtime exception in either pass produces a FAIL entry with the exception
text (Julia parity — cf. the v3 `UndefVarError: R_POISSON` incident of the
unpatched original, fixed in `ab_cloud_v23_v3.1.jl` (reference build: `ab_cloud_v23_v3.2.jl`) and structurally
impossible in the clone, which uses `R_MEAN_POISSON`).

## Known deviations (documented, by design)

The clone reproduces *semantics*, not bit-exact numbers. Three sources of
deviation, all documented in the monograph (Appendix D):

1. **PRNG streams and BLAS backends differ** — bootstrap/Monte-Carlo
   sub-checks use `numpy.random.default_rng`, so individual MC numbers differ
   from the Julia run while distributions match.
2. **Simplified AB Hamiltonian** — the clone's lattice is the
   nearest-neighbour π-flux (Harper) construction with on-site disorder.
   The original suite's five-diagonal AB-cloud Hamiltonian generates a full
   GUE regime (⟨r⟩ = 0.5996); the clone lands in the GOE-intermediate regime
   (⟨r⟩ ≈ 0.50–0.56 at clone sizes), so Tests 32, 33, 34 report FAIL against
   the same GUE windows the original passes. The statistic, the acceptance
   logic and the report format are identical; the measured values are
   printed as-is.
3. **Averaging protocols** — single-sequence block averaging (Test 35 K(t))
   instead of ensemble averaging; rescaled byte-robustness tolerance
   (Test 36) for the smaller accumulated bulk; both documented inline with
   `CLONE-CONVENTION` markers in the code.

## Package layout

```
abcloud/
  __init__.py          package doc + version
  core.py              zeta zeros, Gram points, RMT laws, statistics, AB lattice
  tests_01_14.py       statistics family
  tests_15_26.py       AB construction / topology / gauge family
  tests_27_38.py       chiral, scaling, cross-domain, auxiliary family
  runner.py            two-pass orchestration + progress bar
  report.py            report.md writer + matplotlib plot engine
  cli.py               argparse CLI
  data/zeta_zeros_50000.txt   embedded ζ-zero dataset (verbatim from Julia)
pyproject.toml         installable (pip install .  →  `abcloud` command)
requirements.txt       numpy, scipy, matplotlib, mpmath
```

## Verification summary of this clone

Executed during packaging (2026-09-16, Python 3.12, numpy 2.1 / scipy 1.14):

* Tests 1–14 at reference scale (`--zeros 50000`): **13/14 tests PASS** both
  passes; Test 6 pass-1 strict χ² rejects exactly as documented for the
  reference run (p = 8.7e-71 at n = 50k), pass-2 shape correlation clears it;
* Tests 15–38 (fast profile): **21/27 entries PASS**; the 6 FAIL entries are
  the documented clone-regime deviations of Tests 32/33/34 (simplified
  Hamiltonian) — every measured value is printed against its window;
* analytic identities (Tests 21–23, 37) match the Julia reference values to
  all printed digits.
