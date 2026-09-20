# `run_20260919_085734_m2/` — Test 34 on the Klein Quartic PSL(2,7): The 100,000-Zero Pass
> The addendum's closing record — the first Test 34 confrontation on a closed Hurwitz surface: 5 realizations, 100,000 zeros, pooled D = 0.0808, d_GUE = 0.0044, composite GUE-CONSISTENT.

_Location: [unpacked/](../../README.md) › [run_data/](../README.md) › [run_20260919_085734_m2/](README.md)_

This is the run that closes the September 2026 addendum (chapter Add.8 of the monograph) — and, with it, the arc that the package's v34 freeze documents. The standalone laboratory (`../../lab_standalone/finite-size_lab.jl` v1.3, MODE 2 HARDCORE) executed the Test 34 confrontation on the **Klein quartic** — the genus-3 Hurwitz surface built as the magnetic Cayley graph of PSL(2,7) (|G| = 168) with a ×56 voltage lift to 9,408 sites — against **100,000 ζ zeros**, five realizations, 26 minutes 15 seconds wall time.

## Headline statistics

| metric | value |
|---|---|
| pooled two-sample KS D vs ζ | **0.0808** (p = 1.187e-107) |
| d_GUE / d_Pois | **0.0044** / 0.2817 |
| R₂ plateau (1.0–2.0) | 0.9734 |
| mean |R₂ − GUE| | 0.0299 |
| ensemble median D / IQR | 0.0817 / 0.0017 |
| MAD outliers | none (zero) — ensemble STABLE |
| composite verdict | **GUE-CONSISTENT** — criterion satisfied on all three counts |

Read against the 17 September torus ensemble (pooled D = 0.0970 at 50,000 zeros), the Klein quartic pass demonstrates that the confrontation's residual distance is **geometry-independent**: on a completely different closed surface — no torus periodicity, a genuinely hyperbolic Hurwitz geometry — the lattice side lands statistically indistinguishable from pure GUE (d_GUE = 0.0044) while remaining far from Poisson (d_Pois = 0.2817).

## Why "reconstructed protocol"

The run executed on the operator's device; the console capture travelled (via IM paste), but the device-side result directory — plots, CSV arrays, machine config — did not survive. What ships here is therefore the **reconstructed protocol**: the console's own numbers, complete final blocks, with every derived field in `config.json` explicitly flagged and its derivation shown (the geometry identification 9408 = 168 × 56, the seed ladder 20260976802863…20260976803267 derived from the laboratory's deterministic arithmetic and matched against the console's truncated values). **Nothing is re-simulated.** The provenance policy is documented in the run's own README (`README_original.md`), in the monograph's Add.8, and in the config's `_provenance` field.

## Contents

`FINAL_REPORT_D.md` (reconstructed final report; renamed from `FINAL_REPORT.md`), `config_D.json` (provenance-flagged), `data_realizations_D.csv` (per-realization statistics verbatim + pooled row), and [`logs/`](logs/README.md) with the cleaned console protocol (`console_output.txt`) and the raw capture as received (`console_capture_raw.txt`).

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `FINAL_REPORT_D.md` | 3.5 KB · 78 lines | The consolidated final report (Markdown) — all statistics, per-realization table, forensics and verdict blocks. |
| `README_original.md` | 1.7 KB · 25 lines | The original package README (preserved from the ZIP; superseded for reading by the generated README.md of this folder). |
| `config_D.json` | 1.6 KB · 36 lines | The run configuration (JSON). |
| `data_realizations_D.csv` | 481 B · 7 lines | Per-realization statistics table. |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`logs/`](logs/README.md) | 2 files | Console protocol captures of the Klein quartic pass |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../README.md](../../README.md)._