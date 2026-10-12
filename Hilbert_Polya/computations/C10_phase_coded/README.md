# C10 · Phase coding with hard co-location (R2, T12)

> Gate configurations OBLIGED to satisfy (Φ_p,Φ_q) ≡ Φ_pq: site-linked phase overlay Φ_p = 2π{β ln p}. T12 classification: additive systems = β·ln p; {0,π}-valued systems (χ4) are gauge-trivial.

[← Back to the main README](../../README.md)

## Question
Gate configurations OBLIGED to satisfy (Φ_p,Φ_q) ≡ Φ_pq: site-linked phase overlay Φ_p = 2π{β ln p}. T12 classification: additive systems = β·ln p; {0,π}-valued systems (χ4) are gauge-trivial.

## Result
Co-location residual 4.4e-16 for ANY β (by construction); the spectrum does not see it: r_H7 ≤ 0.092 over 11 β-values, GUE class unchanged.

## Figures
| File | Where |
|---|---|
| `fig18_coloc.png` | 600 dpi — `figures_hires/ru|en/fig18_coloc_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c10_phase_coded.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C10*
