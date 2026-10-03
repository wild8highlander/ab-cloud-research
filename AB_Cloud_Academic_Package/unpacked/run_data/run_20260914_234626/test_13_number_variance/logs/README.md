# `logs/` — Computation Log and Console Capture of Test 13

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 13 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A13L.txt` | 2.3 KB · 24 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A13L.txt` | 1.6 KB · 22 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 13: Number variance Σ²(L)
every log_comp() entry emitted while this test ran:

[23:57:04.365] [+615.394s]  calc: Σ²(L=2.000) = 0.381460 (n_pos=50000, n_windows=3000, mean_count=2.00)
[23:57:04.366] [+615.394s]  calc: Σ²(L=4.536) = 0.402894 (n_pos=50000, n_windows=3000, mean_count=4.54)
[23:57:04.367] [+615.395s]  calc: Σ²(L=10.287) = 0.354897 (n_pos=50000, n_windows=3000, mean_count=10.30)
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_13_number_variance/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_13.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
