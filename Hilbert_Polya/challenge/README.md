<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-Hilbert–Pólya%20·%20challenge-FFB74D?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🏁 `challenge` — the public protocol gate

> **Find a legitimate pass through the gate, or document why it cannot be passed — both outcomes advance the record.**

This folder runs the open **protocol-gate challenge**: a scored, falsifiable task built on the audit's control battery. The rules live in [`CHALLENGE.md`](CHALLENGE.md), the live scoreboard in [`LEADERBOARD.md`](LEADERBOARD.md), and [`score_submission.py`](score_submission.py) is the referee — the exact script that scores any submission, so scoring is reproducible on your machine, not only on ours.

A submission is a JSON protocol file (see [`examples/example_gate.json`](examples/example_gate.json) for the schema and [`submissions/`](submissions/) for a worked example report produced by the protocol itself). The gate is calibrated so that naive parameter search *should* fail the control battery — a passing submission either exhibits a genuine effect that clears the null ceiling, or demonstrates a flaw in the gate itself. Both are publishable outcomes; neither has happened yet, which is exactly what makes the board interesting.

## 📁 Contents

| Item | Kind | Size | What it is |
|---|---|---|---|
| [`CHALLENGE.md`](CHALLENGE.md) | Markdown | 3.4 KB | the full rules: task definition, thresholds, scoring, submission format |
| `examples/` | folder | 1 item | schema example `example_gate.json` to start a submission from |
| [`LEADERBOARD.md`](LEADERBOARD.md) | Markdown | 308 B | current standings — best scores, dates, verdicts |
| [`score_submission.py`](score_submission.py) | Python | 4.7 KB | the referee: deterministic, dependency-light scorer |
| `submissions/` | folder | 1 item | the protocol-generated report of the worked example submission (`report_example-protocol-gate_20261012_170721.json`) |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>

---

<!-- enriched-r3 -->

This folder is a small but functional **shelf of its module**: it keeps a focused set of artifacts that the parent README references. The listing below is generated from the folder itself, so it is exact; the parent README explains how these pieces fit into the study. Nothing here is a compiled binary or an external download — everything is committed source, data or documentation.

The public protocol gate: the challenge folder that lets an outsider submit their own run of the protocol and get it checked against the committed verdicts.

**Subfolders:** `examples/` · `submissions/`
