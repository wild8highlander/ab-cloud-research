# C12 · Argument principle band to T=5000 (R4, T14)

> mp.siegelz machine (bridge to e^{iθ}ζ: 0.0), adaptive sign counting, segmented run, Turing-monitored S(T), strip argument windows.

[← Back to the main README](../../README.md)

## Question
mp.siegelz machine (bridge to e^{iθ}ζ: 0.0), adaptive sign counting, segmented run, Turing-monitored S(T), strip argument windows.

## Result
N_online(5000) = 4520 = N_strip; S_max = 0.91 ≤ 2; v1 anchors (0,3,10,29,79,649) reproduced bit-wise. RH verified in the wider band.

## Figures
| File | Where |
|---|---|
| `fig20_band5000.png` | 600 dpi — `figures_hires/ru|en/fig20_band5000_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c12_band_5000.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C12*
