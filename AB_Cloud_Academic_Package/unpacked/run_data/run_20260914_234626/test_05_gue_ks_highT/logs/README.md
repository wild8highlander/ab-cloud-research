# `logs/` — Computation Log and Console Capture of Test 5

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 5 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A05L.txt` | 812 B · 10 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A05L.txt` | 1.4 KB · 17 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 5: GUE KS test (high-T only)
every log_comp() entry emitted while this test ran:

[23:53:09.330] [+380.358s]  calc: KS D = 0.021622, p_asymptotic = 9.563953e-21 (n=49989, λ=4.8368)
[23:53:09.526] [+380.554s]  calc: KS D = 0.021625, p_asymptotic = 9.718636e-21 (n=49958, λ=4.8360)
[23:53:09.533] [+380.561s]  calc: KS D = 0.021588, p_asymptotic = 1.254559e-20 (n=49853, λ=4.8228)
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_05_gue_ks_highT/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_05.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
