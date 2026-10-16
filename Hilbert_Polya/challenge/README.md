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
| `submissions/` | folder | 1 item | worked example submission + report (protocol-generated) |

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>
