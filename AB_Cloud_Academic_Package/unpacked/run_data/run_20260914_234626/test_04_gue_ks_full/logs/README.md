# `logs/` — Computation Log and Console Capture of Test 4

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 4 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A04L.txt` | 1.2 KB · 14 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A04L.txt` | 1.2 KB · 12 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 4: GUE KS test (full range)
every log_comp() entry emitted while this test ran:

[23:52:57.718] [+368.746s]  calc: KS D = 0.021619, p_asymptotic = 9.567870e-21 (n=49999, λ=4.8368)
[23:52:57.719] [+368.748s]  calc: KS D = 0.029562, p_asymptotic = 3.479907e-05 (n=6251, λ=2.3408)
[23:52:57.720] [+368.748s]  calc: KS D = 0.025418, p_asymptotic = 6.066737e-04 (n=6250, λ=2.0125)
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_04_gue_ks_full/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_04.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
