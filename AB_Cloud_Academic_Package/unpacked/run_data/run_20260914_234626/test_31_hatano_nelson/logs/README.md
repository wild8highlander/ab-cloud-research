# `logs/` — Computation Log and Console Capture of Test 31

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 31 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A31L.txt` | 2.8 KB · 28 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A31L.txt` | 3.1 KB · 36 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 31: Hatano-Nelson non-Hermitian skin
every log_comp() entry emitted while this test ran:

[05:25:20.846] [+20311.875s]  build_ab_cloud_hamiltonian: 48x48 (N=2304), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[05:25:24.130] [+20315.159s]  calc: ⟨r⟩_NN = 0.894102 (n=2304, Poisson-box ref NaN, 10 clouds)
[05:25:39.893] [+20330.922s]  calc: ⟨r⟩_NN = 0.907204 (n=2304, Poisson-box ref 0.851687, 10 clouds)
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_31_hatano_nelson/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_31.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
