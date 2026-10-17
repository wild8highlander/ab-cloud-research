<div align="center">

[![Shelf](https://img.shields.io/badge/Shelf-results%20·%20H‑shelf-00E5FF?style=flat-square)](../README.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21825394-blue?style=flat-square)](https://doi.org/10.5281/zenodo.21825394)

</div>

# 🔬 Test H1–H8 — the `hp_audit_standalone.jl` audit shelf

> **Eight standalone Hilbert–Pólya audit campaigns (2026‑10‑15), each frozen exactly as produced — WARNs included.**

This shelf holds the eight one-shot runs of **`hp_audit_standalone.jl`** — the standalone Hilbert–Pólya audit menu that answers eight *different* experimental questions (H‑1 … H‑8) about the AB‑Cloud operator family. Every run lives in its own timestamped folder with the full console report, per-test artifacts and the machine-written one-line verdicts, and nothing here has been edited after the fact.

The menu is deliberately adversarial: it re-uses a control battery (ζ-zero controls, null ceilings, SNR thresholds) before it scores any effect, so a PASS means the control battery held *and* the effect cleared its threshold, while a WARN marks an honest negative or a parameter-dependent result. Three of the eight runs (H‑1, H‑5, H‑8) carry WARN verdicts — that is the audit working as designed, not a defect of the shelf.

## 🧾 The eight runs

| Run folder | Test | One-line verdict | Report |
|---|---|---|---|
| [`run_2026-10-15_125845 Test H-1 hp_audit_standalone.jl`](run_2026-10-15_125845%20Test%20H-1%20hp_audit_standalone.jl/) | **H-1 · prime oscillations** — do AB-phase fingerprints survive in prime-driven oscillations? | `Test H1 [HP audit]: 5 sub-checks, 2 failed → WARN` | [final report](run_2026-10-15_125845%20Test%20H-1%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_171944 Test H-2 hp_audit_standalone.jl`](run_2026-10-15_171944%20Test%20H-2%20hp_audit_standalone.jl/) | **H-2 · Weyl-law density** — lattice vs power-law density of states (Model B vs A) | `Test H2 [HP audit]: 4 sub-checks, 0 failed → PASS` | [final report](run_2026-10-15_171944%20Test%20H-2%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_172357 Test H-3 hp_audit_standalone.jl`](run_2026-10-15_172357%20Test%20H-3%20hp_audit_standalone.jl/) | **H-3 · power-law real spectrum** — level-spacing dictionary check — rejection expected, and observed | `Test H3 [HP audit]: 6 sub-checks, 0 failed → PASS` | [final report](run_2026-10-15_172357%20Test%20H-3%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_172445 Test H-4 hp_audit_standalone.jl`](run_2026-10-15_172445%20Test%20H-4%20hp_audit_standalone.jl/) | **H-4 · critical q-scan** — where exactly does the KS-distance minimum sit on the q-line? | `Test H4 [HP audit]: 5 sub-checks, 0 failed → PASS` | [final report](run_2026-10-15_172445%20Test%20H-4%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_203604 Test H-5 hp_audit_standalone.jl`](run_2026-10-15_203604%20Test%20H-5%20hp_audit_standalone.jl/) | **H-5 · large ensemble** — does GUE universality survive a multi-regime × N ensemble? (parameter-dependent → WARN) | `Test H5 [HP audit]: 9 sub-checks, 1 failed → WARN` | [final report](run_2026-10-15_203604%20Test%20H-5%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_221845 Test H-6 hp_audit_standalone.jl`](run_2026-10-15_221845%20Test%20H-6%20hp_audit_standalone.jl/) | **H-6 · stability stress** — boundary, jitter and hermiticity stress of the operator | `Test H6 [HP audit]: 4 sub-checks, 0 failed → PASS` | [final report](run_2026-10-15_221845%20Test%20H-6%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_223559 H-7 hp_audit_standalone.jl`](run_2026-10-15_223559%20H-7%20hp_audit_standalone.jl/) | **H-7 · sequence correlation** — are verdict lines independent of input sequence order? | `Test H7 [HP audit]: 4 sub-checks, 0 failed → PASS` | [final report](run_2026-10-15_223559%20H-7%20hp_audit_standalone.jl/final_report.md) |
| [`run_2026-10-15_225604 H-8 hp_audit_standalone.jl`](run_2026-10-15_225604%20H-8%20hp_audit_standalone.jl/) | **H-8 · all numbers trace** — audit-of-the-audit: does every reported number trace to raw logs? (1 sub-check failed → WARN) | `Test H8 [HP audit]: 6 sub-checks, 1 failed → WARN` | [final report](run_2026-10-15_225604%20H-8%20hp_audit_standalone.jl/final_report.md) |

Verdicts are quoted verbatim from each run's `results_verdicts.txt` (WARN is an honest negative or a parameter-dependent result — it is part of the scientific record and must not be edited away).

## 🧪 How to read a run folder

Each run folder contains `final_report.md` / `final_report.html` (the full human-readable report), `results_verdicts.txt` (the machine-written one-line verdicts, quoted verbatim in the table above), a `logs/` directory with the raw console stream, one `test_<id>_<name>/` directory per experiment with its committed plots, and the experiment's `test_<id>_<name>_REPORT.txt` verdict file beside it. To re-examine any single experiment, start from its `*_REPORT.txt`, then cross-check the numbers against `logs/` — the H‑8 campaign exists precisely to certify that this cross-check closes for every number printed anywhere on this shelf.

## 📁 Contents

The only items on this shelf are the eight run folders themselves — they are all described, with verbatim verdicts and report links, in the run table above. No loose files live here: everything else is inside a run folder, one level down.

## 🧭 Navigation

[⬅ Back to the parent shelf](../README.md) · [🏠 Repo root](../../README.md)

---

<div align="center">

*Part of the [AB-Cloud Research](../../README.md) repository · DOI [10.5281/zenodo.21825394](https://doi.org/10.5281/zenodo.21825394) · © 2026 Isaev Iskhak Khamzatovich — personal proprietary use, see the [license terms](../../LICENSE).*

</div>
