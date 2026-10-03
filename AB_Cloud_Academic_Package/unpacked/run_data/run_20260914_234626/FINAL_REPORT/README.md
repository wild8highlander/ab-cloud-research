# `FINAL_REPORT/` — The Consolidated Master Report of the Reference Run
> One folder, the whole run: the four-format master report with all 38 test reports embedded inline, the 9,921-line consolidated execution log, the verdict register, and the raw per-test copies.

_Location: [unpacked/](../../../README.md) › [run_data/](../../README.md) › [run_20260914_234626/](../README.md) › [FINAL_REPORT/](README.md)_

FINAL_REPORT is the last folder the reference run wrote and the one document a reader can open to see the entire 26-hour session from a single file: the master report `final_report.md` (with `.html`, `.pdf` and `.docx` editions) **embeds every test's full report inline** — verdicts, result lines, plot inventories, computation logs and console captures — so the whole run reads from one document. Since v23.5 this embedding is the run's canonical summary format, and the monograph's Appendix A tables are drawn from it.

## Contents

- **`final_report.md` / `.html` / `.pdf` / `.docx`** — the master report in four formats: the run header (session timing, Julia version, wall duration 93,748.1 s), the configuration snapshot with end-of-run values, the 79-entry verdict table (66 PASS / 0 WARN / 13 FAIL / 0 DONE at the primary tier), the full per-test reports embedded inline, and the reproduction commands.
- **[`logs/`](logs/README.md)** — the consolidated execution log `full_run_log.txt` (9,921 lines: every test's computation log + console capture in execution order, timestamped with cumulative wall-clock offsets), the full `log_comp()` register `computation_log_full.txt`, the one-line verdict register `results_verdicts.txt`, and the per-test raw log copies in `logs/test_XX_<slug>/`.
- **[`reports/`](reports/README.md)** — the raw per-test report copies (38 × 4 formats), kept as shipped for provenance; the reading copies live in each test's own folder.

## How to read it in practice

Start with the verdict table and the configuration snapshot (both near the top of the report). For any test of interest, jump to its embedded section (or open the test's own folder README in `../test_XX_<slug>/`, which re-presents the same content with navigation). Cross-check any verdict line against `logs/results_verdicts.txt` — the one-line register — and against Appendix A.2 of the monograph, which reproduces it verbatim. The audit-tier census (35 batteries, 127 sub-checks, 121 passed in-run) is tabulated in Appendix A.3 and in the reading guide `../../AUDIT_DATA.md` (shipped one level up as `run_data/AUDIT_DATA.md`).

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `final_report.docx` | 252.3 KB | Microsoft Word document. |
| `final_report.html` | 142.4 KB · 1725 lines | HTML document. |
| `final_report.pdf` | 195.5 KB | PDF document. |
| `final_report_AF.md` | 133.5 KB · 2055 lines | Markdown document. |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`logs/`](logs/README.md) | 3 files, 38 subfolders | Consolidated logs + verdict register + per-test raw logs |
| [`reports/`](reports/README.md) | 0 files, 38 subfolders | Raw per-test report copies (38 × 4 formats) |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../../README.md](../../../README.md)._