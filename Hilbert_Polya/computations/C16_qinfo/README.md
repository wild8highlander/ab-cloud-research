# C16 · Quantum-information layer (T18)

> Fermionic entanglement of the Slater Fermi sea (correlation-matrix protocol), mutual information of halves, SFF ramp slopes.

[← Back to the main README](../../README.md)

## Question
Fermionic entanglement of the Slater Fermi sea (correlation-matrix protocol), mutual information of halves, SFF ramp slopes.

## Result
Locality suppresses volume-law entanglement (S_A ≈ 12–16 nats vs 160–220 Haar, z > 100) — the quantum echo of C9; MI carries no zero signature (−0.018 vs −0.121 random).

## Figures
| File | Where |
|---|---|
| `fig24_qinfo.png` | 600 dpi — `figures_hires/ru|en/fig24_qinfo_ru|en.png`; copy in `figures/ru|en/` |

## Data
| File | Content |
|---|---|
| `data/results.json` | committed verdict |
| `data/*.npz` / `*.csv` | curves and tables |

## Reproduction
```bash
python3 campaigns/run_c16_qinfo.py
```
Fresh runs are self-contained: the zeta zeros come from the internal
mpmath cache (`data/zeros/`), no external files. Runtime: seconds to
minutes (C12 is segmented; see `campaigns/run_c12_band5000.py`).

## Verdict
See `data/results.json` (verdict, RU+EN), the v2 monograph
(`monograph/v2_volume/`) and `independent_verification/` (IVP11–18).

---
*Hilbert Polya Bridge v2.0.0 · C16*
