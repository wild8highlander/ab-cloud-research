# `logs/` — Computation Log and Console Capture of Test 29

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 29 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A29L.txt` | 1.6 KB · 14 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A29L.txt` | 2.1 KB · 26 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 29: Dirac dip in DOS at α=1/2
every log_comp() entry emitted while this test ran:

[03:49:19.515] [+14550.543s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.3958, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:53:34.081] [+14805.109s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4271, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[03:58:04.195] [+15075.223s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.4583, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_29_dirac_dip/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_29.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
