# Performance — Dirac Laboratory

*Measured: 2026-10-06 16:56 · Python 3.12.14 · numpy 2.1.3 · scipy 1.14.1 · 2 logical cores · Linux 5.10.134-013.15.kangaroo.al8.x86_64*

## Measured wall times (no figures)

Mode independence (v1.4): D10b transport runs at L = 48, D10a pair
statistics at the canonical 2000 zeros and the D9d composite vortex
on the canonical 200^2 domain in BOTH modes — quick verdicts are now
identical to FULL. D9-D10 are still measured in FULL here: it is the
canonical mode and, for this module, also the faster one (the reduced
quick domain converges the sparse eigensolvers more slowly). All other
modules run their quick mode.

| Module | Module file | Mode | Wall time | Verdict |
|---|---|---|---|---|
| Core suite D1-D8 | `code/dirac_lab.py` | QUICK | **18.1 s** | 8/8 PASS |
| Extensions I: D9-D10 | `code/dirac_lab_extensions.py` | FULL | **59.1 s** | 2/2 PASS |
| Extensions II: D11 | `code/dirac_lab_extensions2.py` | QUICK | **8.5 s** | 1/1 PASS |
| Extensions III: D12-D14 | `code/dirac_lab_extensions3.py` | QUICK | **32.5 s** | 3/3 PASS |
| **Total** |  |  | **118.2 s** | **14/14 PASS** |

## Full mode (canonical run `results/run_20261006_full_v13`)

| Module | Scope | Wall time (recorded) |
|---|---|---|
| Core suite D1-D8 | 8 tests / 33 checks | ~2.0 min |
| Extensions I: D9-D10 | 2 tests / 19 checks | ~1.0 min |
| Extensions II: D11 | 1 test / 15 checks | ~0.3 min |
| Extensions III: D12-D14 | 3 tests / 29 checks | ~4.4 min |
| **Total** | **14 tests / 96 checks** | **~7.7 min** |

## Where the time goes and what is already optimized

- **Dense Hermitian eigendecompositions** dominate the core suite:
  the largest Hamiltonian is the 2L^2 = 8192-dimensional L = 64 torus
  (D1 finite-size track); `numpy.linalg.eigvalsh` (LAPACK `dsyevd`,
  multi-threaded BLAS) is used everywhere the full spectrum is needed.
- **Wall physics (D9, D13)**: the open-grid spectra are dense but the
  multiplet isolation needs only the sorted eigenvalue list — no
  eigenvector diagonalization on the largest grids.
- **D11/D12** avoid naive O(N_u^2) Fourier sums: the Dirichlet comb has
  a closed-form kernel (O(N_u) per evaluation, no diagonalization at all),
  and the dilation operator is diagonal by construction (F† diag F with
  the unitary DFT) — its spectrum is exact arithmetic, not iterative.
- **D11c/D14** form factors use the vectorized sliding-window estimator
  (per-window local re-unfolding, L_w = 200, stride L_w/2; the phase
  matrix is one `np.outer` per window) instead of quadratic pair loops.
- **Reproducibility first**: every module is seeded (seed 96) and the
  suite is deterministic; threading affects only BLAS internals, never
  the published numbers.

## How to reproduce

```bash
python3 scripts_gen/benchmark.py        # this table, quick mode
make quick                              # core sanity pass only
make all                                # canonical FULL run (~8-12 min)
```

To pin BLAS threading: `OMP_NUM_THREADS=4 make all` (results are
thread-count independent; only wall time changes).
