# `logs/` — Computation Log and Console Capture of Test 33

Each line of the computation log carries the time of day and the cumulative wall-clock offset (`[23:52:57.718] [+368.746s]`), the channel tag (`calc:` for computed statistics), and the values themselves. The stdout capture preserves the suite's console output verbatim: banner, progress lines, the lettered sub-check blocks (each statistic with its pre-registered limit and outcome), and the verdict line.

This `logs/` subfolder belongs to Test 33 of the reference run; its parent folder [`../README.md`](../README.md) carries the full test description, verdicts and explanation.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `computation_log_A33L.txt` | 12.3 KB · 103 lines | Timestamped computation log: every log_comp() entry emitted while the test ran, with wall-clock offsets. |
| `stdout_capture_A33L.txt` | 4.3 KB · 53 lines | Raw console capture: the suite's console output for this test, including lettered sub-check lines and the verdict block. |

## The first lines of the computation log (verbatim)

```text
FULL COMPUTATION LOG — test 33: L-scaling ⟨r⟩ (10→20→30→50→80→112)
every log_comp() entry emitted while this test ran:

[07:09:25.448] [+26556.476s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
[07:09:25.985] [+26557.014s]  calc: ⟨r⟩ = 0.629404 (n_r=59, n_eigs=61) [refs: GUE=0.5996 Poisson=0.3863]
[07:09:27.180] [+26558.208s]  build_ab_cloud_hamiltonian: 10x10 (N=100), α=0.5000, t=1.00, W=1.00, torus, 4 vortices, model=:monumental
```

## Where the full record lives

- The same log and capture ship as raw provenance copies in [`../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) — specifically its `test_33_l_scaling_rmean/` subfolder.
- Both are embedded verbatim inside the test's own report files (`../report_33.md` and its HTML/PDF/DOCX siblings) — see [`../README.md`](../README.md), section 7–8.
- The consolidated whole-session log is [`../../FINAL_REPORT/logs/`](../../FINAL_REPORT/logs/README.md) `full_run_log.txt` (9,921 lines).

---
_Package overview: [unpacked/](../../../README.md) · Run archive: [../../](../../README.md) · Test folder: [../](../README.md)_
