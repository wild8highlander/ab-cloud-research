# C14 · Anomaly hunt outside the GUE attractor (T16)

> Systematic scan of 121 configurations (protocol family × Nv,q,W,α + blind representatives). Honest taxonomy, ⟨r⟩-criterion.

[← Back to the main README](../../README.md)

## Question
Systematic scan of 121 configurations (protocol family × Nv,q,W,α + blind representatives). Honest taxonomy, ⟨r⟩-criterion.

## Result
97 GUE / 18 integrable (Nv=0, expected per C8) / 6 intermediate (weak vortex). No rank outliers (|r_H7| ≤ 0.153). The attractor is global; its basin is structured.

## Figures
| File | Where |
|---|---|
| `fig22_anomaly.png` | 600 dpi — `figures_hires/ru|en/fig22_anomaly_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c14_anomaly_hunt.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C14*
