# `logs/test_07_decay_slope/` — Raw Log Copies of Test 7 (Provenance Set)

This folder is part of FINAL_REPORT's provenance layer: it preserves the **raw computation log and console capture of Test 7** exactly as the reference run wrote them. The reading copies — with the full test description, verdicts and excerpts — live in the test's own folder: [`../../test_07_decay_slope/`](../../test_07_decay_slope/README.md).

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_XX.txt` | 141 B · 4 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_XX.txt` | 1.2 KB · 13 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

These files are byte-identical to the copies in the test's own `logs/` folder; they are duplicated here (as shipped by the suite) so that the FINAL_REPORT's inline embeddings can always be audited against untouched originals. For the consolidated whole-session record, see [`../full_run_log.txt`](../full_run_log.txt) and the verdict register [`../results_verdicts.txt`](../results_verdicts.txt) (described in [`../README.md`](../README.md)).

---
_Package overview: [unpacked/](../../../../README.md) · FINAL_REPORT: [../](../README.md) · Test folder: [../../test_07_decay_slope/](../../test_07_decay_slope/README.md)_
