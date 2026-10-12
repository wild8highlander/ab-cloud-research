# C13 · Blind families (R5, T15)

> Five families absent from the v1 handle space: imaginary x-hoppings, golden quasiperiodic vortices, dimers, power-law hoppings, flux dithering. 20 gates, one pipeline, PC0' = 1.000.

[← Back to the main README](../../README.md)

## Question
Five families absent from the v1 handle space: imaginary x-hoppings, golden quasiperiodic vortices, dimers, power-law hoppings, flux dithering. 20 gates, one pipeline, PC0' = 1.000.

## Result
All in the null zone: |r_H7| ≤ 0.040, min p = 0.29, GUE class intact. The H2 gap is robust to designs outside the v1 space.

## Figures
| File | Where |
|---|---|
| `fig21_blind.png` | 600 dpi — `figures_hires/ru|en/fig21_blind_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c13_blind_families.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C13*
