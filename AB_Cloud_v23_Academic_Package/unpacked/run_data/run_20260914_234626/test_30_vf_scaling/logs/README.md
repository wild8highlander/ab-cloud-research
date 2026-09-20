# `logs/` — Computation Log and Console Capture of Test 30

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 30 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A30L.txt` | 1.6 KB · 14 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A30L.txt` | 1.8 KB · 24 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 30: Dirac cone vF scaling vs L
every log_comp() entry emitted while this test ran:

[04:30:03.322] [+16994.351s]  build_ab_cloud_hamiltonian: 16x16 (N=256), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:04.976] [+16996.005s]  build_ab_cloud_hamiltonian: 24x24 (N=576), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
[04:30:06.368] [+16997.396s]  build_ab_cloud_hamiltonian: 32x32 (N=1024), α=0.5000, t=1.00, W=0.00, torus, 0 vortices, model=:monumental
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_30_vf_scaling/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_30.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
