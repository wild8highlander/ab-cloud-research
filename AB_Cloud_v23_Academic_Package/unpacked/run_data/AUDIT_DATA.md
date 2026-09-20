# Audit-Tier Run Data — `run_data/run_20260914_234626/`

This folder is the **complete reference-run archive** of the AB-Cloud v23 SUPERCOMBO
suite (reference run `run_20260914_234626`, executed 2026-09-14 → 2026-09-16 in a single
interactive session of 93,748 s / 26.04 h on Julia 1.12.0). It is the evidence base for
every number quoted in the monograph and its Academic Essence companion, and it ships
inside the submission package so that the record and its data travel together.

## Contents

| Path | What it is |
|---|---|
| `FINAL_REPORT/final_report.{md,html,pdf,docx}` | The consolidated final report in four formats — all 38 test reports embedded inline with their verdicts, result lines, plot inventories, computation logs, and console captures. |
| `FINAL_REPORT/logs/full_run_log.txt` | The consolidated execution log (9,921 lines): every test's computation log and console capture in execution order, with timestamps and cumulative wall-clock offsets. |
| `FINAL_REPORT/logs/computation_log_full.txt` | Every `log_comp()` entry emitted during the run. |
| `FINAL_REPORT/logs/results_verdicts.txt` | The one-line verdict register: all 79 verdict entries (66 PASS / 13 FAIL), each with its verbatim statistic line. |
| `FINAL_REPORT/logs/test_*/`, `FINAL_REPORT/reports/test_*/` | Per-test logs and reports. |
| `test_01_bN_convergence/ … test_38_curie_point/` | The 38 test folders: `report.{md,html,pdf,docx}`, `logs/` (computation log + stdout capture), `plots/` (60 PNG figures, 36 animations). |
| `index.html` | The run's index page. |

## The audit tier (menu key `h` family — HARDCORE / SERIES / AUDIT passes)

On top of the 38 primary (pass-1) verdicts, every test in the run carries a
**HARDCORE pass-2 deep audit** — the suite's deep-audit apparatus (menu key `h`
family): re-derived verdicts through harder, often lattice-independent checks on the
secondary 96×96 lattice or the full 50,000-zero dataset. Tests 19/29/31 add SERIES
pass-3 sweeps; Test 19 adds an AUDIT pass-4 twist audit.

**The audit tier's census: 35 batteries, 127 individually logged sub-checks, 121 passed
in-run.** The full census is tabulated in Appendix A.3 of the monograph; the summary:

| Battery | Sub-checks | Failed | In-run outcome |
|---|---|---|---|
| Tests 1–11, 13–26, 27b, 30b–33b, 37b, 19c/19d, 29c, 31c | 114 | 0 | PASS |
| Test 12b (two-sample KS audit) | 3 | 2 | WARN |
| Test 28b (f_GUE audit) | 2 | 1 | WARN |
| Test 34b (confrontation audit) | 4 | 1 | WARN |
| Test 35b (form-factor audit) | 3 | 2 | WARN |

The four batteries that carried failed sub-checks are analysed in the monograph
(Part II and Appendix C). In particular, the Test 34b R₂ signature
(⟨|ΔR₂|⟩ = 0.0002, d_GUE = 0.876, d_Poisson = 0.9998) is traced by the v3.2 estimator
audit to two documented code defects (cartesian-loop break-exit; position-stride
subsampling), and the pooled two-sample distance D = 0.1096 to the ζ-side
sliding-window reference unfolding — corrected in the v3.2 reference build
(`julia_patched/ab_cloud_v23_v3.2.jl`), with the falsifiable post-fix window
D = 0.03–0.06.

## How to verify any number in the monograph

1. Locate the test folder for the chapter you are reading (the chapter number is the
   test number; e.g. Chapter 34 → `test_34_direct_vs_zeta/`).
2. Open `report.md` — it embeds the what-the-test-verifies statement, the result line,
   the plot inventory, the full computation log, and the console capture.
3. The lettered lines of the console capture (H0 … H7, K1–K3, S1–S4, R1–R4, Z1–Z5, …)
   print each sub-check's statistic, its pre-registered limit, and its outcome verbatim.
4. Cross-check the verdict line against `FINAL_REPORT/logs/results_verdicts.txt` and the
   master table in Appendix A.2 of the monograph.

## Reproduction paths

- Single test (Julia, from the package root):
  `julia julia_patched/ab_cloud_v23_v3.2.jl --test 34 --no-two-pass`
- Full suite (reference scale, ≈ 26 h): `--test all`
- Cross-language fast profile (Python, minutes):
  `pip install -r python_clone/requirements.txt && python -m abcloud.cli --test all`
- The 20-minute Test 34 re-run that verifies the v3.2 prediction (pooled
  D = 0.03–0.06) executes against this same archive and appends its captures in the
  identical format.


## September 2026 addendum runs (Test 34 verification chain)

Besides the reference-run archive above, `run_data/` carries the three standalone-laboratory
runs of the September 2026 addendum — the Test 34 independent verification chain:

| Run | Protocol | Headline |
|---|---|---|
| `run_20260917_080329_m2/` | MODE 2 HARDCORE, torus 96×96, 20 realizations, 50,000 zeros (91,360 spacings) | pooled D = 0.0970, d_GUE = 0.0768; ensemble STABLE (one MAD outlier) |
| `run_20260917_084900_m3/` | MODE 3 DEEP DIAG: differential CDF, short-range zone, seed forensics, finite-size probe, bootstrap | the effect is real, seeded, size-independent |
| `run_20260919_085734_m2/` | MODE 2 HARDCORE, **Klein quartic PSL(2,7)** (Cayley ×56 lift, 9,408 sites), 5 realizations, **100,000 zeros** (23,320 spacings) | pooled **D = 0.0808**, d_GUE = **0.0044**, plateau = 0.9734; composite criterion satisfied (GUE-CONSISTENT); ensemble STABLE, zero MAD outliers |

The 19 September run is documented in Addendum Add.8 of the monograph, the Academic
Essence, and both preprints. Its shipped folder is a faithful reconstruction from the
operator console capture (see its README.md): every statistic is verbatim; the geometry
identification and the full 14-digit seeds are derived deterministically from the
laboratory source arithmetic and are flagged as such in config.json.
