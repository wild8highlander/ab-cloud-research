# C15 · Dirichlet L-functions pipeline (T17)

> The C1–C4 + C6 pipeline for χ5 (even) and χ7 (odd): Z_χ reality, zero bisection + strip checks, twisted ψ_χ ladder, twisted trace formula.

[← Back to the main README](../../README.md)

## Question
The C1–C4 + C6 pipeline for χ5 (even) and χ7 (odd): Z_χ reality, zero bisection + strip checks, twisted ψ_χ ladder, twisted trace formula.

## Result
|ΔK| ≤ 9.6e-6 (χ5) / 6.1e-6 (χ7) with weight χ(n)Λ(n)/√n; gates vs L-zeros: null zone. The H2 gap is UNIVERSAL across L-functions.

## Figures
| File | Where |
|---|---|
| `fig23_dirichlet.png` | 600 dpi — `figures_hires/ru|en/fig23_dirichlet_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c15_dirichlet.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C15*
