# C11 · α=1/3 zero modes vs arithmetic (R3, T13)

> Kähler–Dirac operator at α=1/3: the torus exists iff L ≡ 0 (mod 3) (flux quantization). Full scan L = 6..48 with tolerance sweep.

[← Back to the main README](../../README.md)

## Question
Kähler–Dirac operator at α=1/3: the torus exists iff L ≡ 0 (mod 3) (flux quantization). Full scan L = 6..48 with tolerance sweep.

## Result
Counting law N₀ = 2L − 6·[L ≡ 0 (mod 12)], index −2 on L ≡ 0 (mod 12); decisive L=36→66, L=48→90. First arithmetic→spectrum bridge; refines the v1 T9 observation.

## Figures
| File | Where |
|---|---|
| `fig19_alphathird.png` | 600 dpi — `figures_hires/ru|en/fig19_alphathird_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c11_alpha_third.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C11*
