# C9 · Nonlocal trace primitive (R1, T11)

> Does an operator exist whose heat trace carries Λ(n)/√n BY CONSTRUCTION (directly from Guinand–Weil, not through the lattice)? Family N1–N5: H_ξ control, DCT/QR isospectral twins, Berry–Keating xp, LCM kernel.

[← Back to the main README](../../README.md)

## Question
Does an operator exist whose heat trace carries Λ(n)/√n BY CONSTRUCTION (directly from Guinand–Weil, not through the lattice)? Family N1–N5: H_ξ control, DCT/QR isospectral twins, Berry–Keating xp, LCM kernel.

## Result
N2/N3 twins: r_H7 = 1.000, r_EF(fluct) = 0.999 — the primitive exists; xp and LCM kernel stay in null zones. T11: heat-trace uniqueness ⇒ the H2 gap is a wall of LOCALITY, not of the trace.

## Figures
| File | Where |
|---|---|
| `fig17_nonlocal.png` | 600 dpi — `figures_hires/ru|en/fig17_nonlocal_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c9_nonlocal_trace.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C9*
