# `logs/` — Computation Log and Console Capture of Test 32

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 32 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A32L.txt` | 4.8 KB · 43 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A32L.txt` | 5.9 KB · 84 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 32: Multi-realization ⟨r⟩ bootstrap
every log_comp() entry emitted while this test ran:

[05:37:38.247] [+21049.276s]  realization 1/5 (q=1.000): building 96x96 Hamiltonian (large-lattice diag dominates, minutes)
[05:37:39.194] [+21050.222s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, torus, 2 vortices, model=:monumental
[05:43:04.004] [+21375.032s]  calc: ⟨r⟩ = 0.581975 (n_r=5527, n_eigs=5529) [refs: GUE=0.5996 Poisson=0.3863]
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_32_rmean_bootstrap/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_32.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
