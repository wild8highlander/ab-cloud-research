# tables/ — the summary workbook of the series

> **🧭 Navigation:** [Hilbert_Polya/](../README.md) · [Root README](../../README.md)

<p align="center"><img src="../assets/illustrations/ill_trace_formula.png" width="600" alt="Trace formula terms laid out as spreadsheet columns"/></p>

<p align="center"><img src="../assets/avatars/hp_cast_strip.svg" width="720" alt="Bridge avatar cast"/></p>
<p align="center"><em>The whole series on one desk pad: five sheets that a referee can read without opening a single script.</em></p>

[← Back to the main README](../README.md)

## What this folder is

The spreadsheet face of the series. One workbook, `hp_workbook.xlsx`,
condenses the released numbers — the headline results, the protocol gate
lattices, the theorem list and the final Hilbert–Pólya scorecard — into five
sheets that mirror the committed verdicts in `data/`. It is a derived
artifact: the scripts rebuild it, the ledger quotes it, and referees read it.

## Contents

| File | Contents |
|------|----------|
| `hp_workbook.xlsx` | the five-sheet summary workbook of the series |

The five sheets:

| Sheet | What it holds |
|-------|---------------|
| Headline | the headline numbers of the series |
| Gates C3 | the 52 protocol gates |
| Gates C5 ext | the extended family, 35+2 |
| Theorems | T1–T10 |
| HP scorecard | the Hilbert–Pólya scorecard |

## How to use it

Rebuild from the committed sources:

```bash
make workbook
```

or directly:

```bash
python3 scripts/build_workbook.py
```

The sources are `data/`: the gate tables (`c3_gates_table.csv`,
`c5_gates_ext_table.csv`) and the committed campaign verdicts
(`c1_identity_verdict.json`, `c3_gates_verdict.json`, `c4_trace_verdict.json`,
`c5_gates_ext_verdict.json`, `c6_primes_verdict.json`, and their companions)
are what the sheets are rendered from. After a rebuild, the workbook should
match `results/RESULTS.md` line for line; any mismatch means one of the two
is stale.

## Conventions

- The workbook is generated, never hand-edited: a manual change survives
  exactly until the next `make workbook`.
- Sheet names and their order are fixed; consumers (and the monographs'
  appendix volume) rely on them.
- Every numeric cell is traceable to a committed verdict in `data/` — the
  workbook adds presentation, not new numbers.

## See also

- [../data/README.md](../data/README.md) — the committed sources of every sheet
- [../scripts/README.md](../scripts/README.md) — `build_workbook.py` and the rest of the pipeline
- [../results/RESULTS.md](../results/RESULTS.md) — the living ledger the sheets must match
- [../monograph/README.md](../monograph/README.md) — the bound volumes that quote the same tables

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The summary workbook of the series (Excel): the one-spreadsheet view of the campaign verdicts.
