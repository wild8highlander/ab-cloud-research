# results_run — Run Artifacts and Reference Logs (83 files)

Everything the Julia suite produced on paper-worthy runs, committed so the
numbers in the monographs are checkable without running anything. Two kinds
of content live here:

1. **The two-pass v19 run of 2026-09-02** (37 tests, Julia 1.12.0, 50 000
   Odlyzko zeros, pass 2 "HARDCORE" at 96×96): the aggregated
   `FINAL_REPORT/` plus the flattened per-test folders `test_reports/`
   (one `report.md` per test) and `computation_logs/` (one raw log per
   test) — 80 files of reports, tables and logs. The run's PNG plots are
   not committed — the plots regenerate deterministically from the suite.
2. **Two flat reference logs** — the 2026-08-28 37-test run (v18) and the
   v19 verification-report header/config dump from 2026-09-02.

## Layout

```
results_run/
├── FINAL_REPORT/               # aggregated two-pass verdict
│   ├── final_report.md / .pdf / .docx
│   └── logs/                   # run-level logs (computation, execution, verdicts)
├── test_reports/               # one report per test (test_01 … test_37, 37 total)
├── computation_logs/           # one raw log per test (37 total)
│   ├── test_01_bN_convergence_log.txt   # the actual numbers: fits, statistics, thresholds
│   └── …
├── ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt
└── verification_run_v18_37tests_2026-08-28.txt
```

Every report in `test_reports/` opens with the verdict line
(`Verdict: PASS | Generated: … | Suite: AB-Cloud v19 (Julia 1.12.0)`),
explains what the test verifies, states the raw result (e.g.
`8 sub-checks, 0 failed, b(50000)=1.2126 → PASS`) and lists the plots that
the suite regenerates.

## The 37 tests (folder names are self-describing)

| # | Test | # | Test |
|---|---|---|---|
| 01 | bN_convergence | 20 | … |
| 02 | bN_monotonicity | … | full list: `ls test_reports/` |
| 03 | bN_rate | … | the suite's own docs: the `ab_cloud_v19.jl` header (suite source not bundled in this package) |
| 04 | gue_ks_full | … | |
| … | | 36 | byte_robust |
| … | | 37 | half_factorial_gamma |

Highlights: GUE statistics of the 50 000-zero sample (⟨r⟩, KS, Σ², Δ₃),
Byers–Yang flux defect 3.5·10⁻¹⁵, Connes self-duality, Dirac cone
v_F ≈ 0.125 (R² = 0.9997), Berry R₂(0), Arf/orbit checks, robustness battery.

## Regenerating the plots

The plots were stripped from the committed run to keep the repository light
(the run writes ~600 dpi PNG + SVG + PDF + GIF per figure). Reproduce the
whole run including plots by running the v19 suite from the upstream
repository checkout (the suite source is not bundled in this package):

```bash
julia ab_cloud_v19.jl --test all           # 30–60 min; writes a NEW timestamped run folder
```

The committed numbers are reproducible because the suite is seeded and reads
the frozen data in `verification/data/` (repository root).

## Flat reference logs

| File | What it is |
|---|---|
| `verification_run_v18_37tests_2026-08-28.txt` | full console log of the 2026-08-28 v18 37-test run — the historical basis of monograph v22; includes the b(N) fit (b(N) ≈ 7.0312·N^(−0.1685), R² = 0.9895; alternative 1/log N fit R² = 0.9994) and the v23-notation caveat that α = 1/2 refers to the AB-phase, not the convergence rate |
| `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` | header/config dump of the v19 verification report: zeros = 50000, n_bootstrap = 1000, chi2_bins = 300, gue_matrix_size = 12000 (seed 112), rmt CDF table 32 768-pt (max\|ΔF\| = 4.9e-9), embedded-dataset note |

## How to read the run artifacts

1. Open `FINAL_REPORT/final_report.md` — it aggregates all 37 verdicts of
   both passes.
2. For a single test, read `computation_logs/test_XX_*_log.txt` first (raw
   numbers), then the matching `test_reports/test_XX_*_report.md`
   (verdict + interpretation).

## In short

- Artifacts of the v19 run of 2026-09-02: 37 tests, two passes (the second —
  HARDCORE 96×96), Julia 1.12.0, 50 000 Odlyzko zeros.
- Layout: `FINAL_REPORT/`, one flattened report per test under
  `test_reports/` and one raw log per test under `computation_logs/`;
  the run's plots are excluded and regenerate deterministically via
  `julia ab_cloud_v19.jl --test all`.
- Plus two flat journals: the v18 run of 2026-08-28 (the basis of monograph
  v22) and the v19 verification-report config dump.
- Reading order: `FINAL_REPORT/final_report.md` → a test's
  `computation_logs/test_XX_*_log.txt` → its `test_reports/test_XX_*_report.md`.

## 📁 Complete file inventory

| Entry | Size | Kind |
|---|---|---|
| `test_reports/` | 37 files | directory |
| `computation_logs/` | 37 files | directory |
| `FINAL_REPORT/` | 6 files | directory |
| `README_source.md` | 7.5 KB | file |
| `ab_cloud_v19_verify_report_2026-09-02_23-33-45.txt` | 986.5 KB | file |
| `verification_run_v18_37tests_2026-08-28.txt` | 58.3 KB | file |
| **Total (recursive)** | **83 files, 2.7 MB** | |

## 🔬 Deep dive — anatomy of the flagship run

The `FINAL_REPORT/` + `test_reports/` + `computation_logs/` set is the
complete artifact record of the two-pass v19 run: 37 tests, Julia 1.12.0,
50 000 Odlyzko zeros, pass 2 in "HARDCORE" mode on a 96×96 lattice
(pass 1 runs 72×72). `FINAL_REPORT/` carries the consolidated verdicts
(with the run-level logs), while each test's report and raw log sit
flattened under `test_reports/` and `computation_logs/` respectively. The
run's PNG plots are intentionally **not** committed: every plot regenerates
deterministically from the suite, and excluding them keeps the repository
clone-able — the numbers, which are what the monographs cite, are all here
as text.

How to check a printed number. Take any figure quoted in the monographs
— say the pair-correlation KS distance 0.047 with p = 0.27, the
Byers–Yang flux defect 3.5e-15, the Dirac slope v_F ≈ 0.125 with
R² = 0.9997, or b(50000) = 1.2126. Open `FINAL_REPORT/final_report.md`,
find the test row, then read the test's report
(`test_reports/test_XX_*_report.md`) and log
(`computation_logs/test_XX_*_log.txt`): inputs, parameters, statistic,
p-value. Nothing is hidden behind a rerun; the chain
printed-page → test → log is complete and committed.

The two flat logs beside the run serve as the historical baseline: the
2026-08-28 v18 37-test run (the first full-suite pass, referenced by the
earlier monograph builds) and the v19 verification report header/config
dump from 2026-09-02 (the exact configuration of the flagship run). To
reproduce rather than just read: install Julia 1.12, point the suite at
`verification/data/` and run `ab_cloud_v19.jl` from the upstream
repository checkout — the frozen inputs guarantee byte-identical
statistics.
