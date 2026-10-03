# `python_clone/abcloud/` — The Clone's Python Package
> The importable package: statistics core, the three test-battery modules, two-pass runner, report writer, plot engine, CLI, and the embedded ζ-zero dataset.

_Location: [unpacked/](../../README.md) › [python_clone/](../README.md) › [abcloud/](README.md)_

This is the Python package itself — the directory that makes `python -m abcloud.cli` work. Five modules and a data folder, each mapping one-to-one onto a responsibility of the Julia suite:

| Module | Responsibility |
|---|---|
| `core.py` | The statistics engine: the b(N) Gram ladder, unfolding, KS/χ²/AD machinery, ⟨r⟩ ratios, Σ²(L), Δ₃(L), the R₂(s) pair correlation, the form factor, the bootstrap and Monte-Carlo machinery — the shared vocabulary of all 38 tests. |
| `tests_01_14.py` | Batteries 1–14: the convergence triad, the distributional family, the decay-law block, the long-range RMT statistics. |
| `tests_15_26.py` | Batteries 15–26: the AB construction certificates, the GUE classification, the exact duality/symmetry/flux/topology layer. |
| `tests_27_38.py` | Batteries 27–38: the binary-chiral dictionary rework, the merit aggregate, the scaling/robustness block, the direct confrontation, the form factor, byte robustness, the Γ identities and the Curie-point magnet. |
| `runner.py` | The two-pass orchestrator: primary verdicts, HARDCORE pass-2 audits, the composite verdict algebra, run-folder bookkeeping. |
| `report.py` | The report writer and plot engine: emits `report.md` (+ plots) per test and the master `final_report.md`, in the same folder layout as the Julia outputs. |
| `cli.py` | The command-line interface: `--list`, `--test N|a-b|all`, `--no-two-pass`, `--zeros N`, `--full`, `--out DIR`. |
| `data/zeta_zeros_50000.txt` | The embedded dataset: the 50,000 ζ zeros (Odlyzko-sourced) that every test consumes — the identical array the Julia suite embeds. |

The module split along test ranges (01–14, 15–26, 27–38) matches the statistical / construction / advanced families of the monograph's Part II, so a reader can open `tests_15_26.py` beside monograph chapters 15–26 and follow test by test. The statistics-level equivalence and the documented deviations are tabulated in the clone's root README (`../README_original.md`).

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `__init__.py` | 521 B · 15 lines | Package initialisation for the abcloud clone. |
| `cli.py` | 3.6 KB · 98 lines | The clone's command-line interface (--list, --test N|a-b|all, --no-two-pass, --zeros, --full, --out). |
| `core.py` | 25.1 KB · 698 lines | The clone's statistics engine: Gram ladder, unfolding, KS/χ²/AD, ⟨r⟩, Σ²(L), Δ₃(L), R₂(s), form factor, bootstrap/Monte-Carlo machinery. |
| `report.py` | 12.3 KB · 269 lines | The clone's report writer and plot engine — emits per-test reports and the master final_report in the Julia suite's layout. |
| `runner.py` | 7.5 KB · 190 lines | The clone's two-pass orchestrator: primary verdicts, HARDCORE pass-2 audits, composite verdict algebra. |
| `tests_01_14.py` | 26.4 KB · 556 lines | Batteries 1–14: the convergence triad, the distributional family, decay-law robustness, long-range RMT statistics. |
| `tests_15_26.py` | 30.1 KB · 599 lines | Batteries 15–26: AB construction certificates, GUE classification, the exact duality/symmetry/flux/topology layer. |
| `tests_27_38.py` | 25.9 KB · 534 lines | Batteries 27–38: binary-chiral dictionary, merit aggregate, scaling/robustness, the direct confrontation, form factor, byte robustness, Γ identities, Curie point. |

## Subfolders

| Subfolder | Contents | What it is |
|---|---|---|
| [`data/`](data/README.md) | 1 files | The embedded 50,000-zero dataset |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../../README.md](../../README.md)._