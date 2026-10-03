# `logs/` — Computation Log and Console Capture of Test 28

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 28 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A28L.txt` | 1.4 KB · 14 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A28L.txt` | 1.2 KB · 17 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 28: f_GUE figure of merit
every log_comp() entry emitted while this test ran:

[03:10:53.854] [+12244.883s]  calc: Σ²(L=2.000) = 0.423997 (n_pos=8401, n_windows=3000, mean_count=2.01)
[03:10:54.866] [+12245.895s]  build_ab_cloud_hamiltonian: 96x96 (N=9216), α=0.5000, t=1.00, W=1.00, open, 4 vortices, model=:monumental
[03:15:31.980] [+12523.008s]  calc: Σ²(L=2.000) = 0.663437 (n_pos=5530, n_windows=3000, mean_count=2.03)
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_28_f_gue_merit/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_28.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
