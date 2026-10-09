# C2 · The argument principle up to T = 1000

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Counting zeros in the critical strip without tables: the adaptive Turing step, the pole calibration (lemma T3), the arithmetic bridge 2.6e-26; RH verified in the strip: 649 = 649.**

[← Back to the main README](../../README.md)

## Contents

1. [The campaign question](#the-campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest notes](#honest notes)
9. [Verdict](#verdict)

---

## The campaign question

How many zeta zeros lie in the critical strip below a height T, and are they all on the critical line? The campaign answers via the argument principle: the contour (2,0)→(2,T)→(0,T)→(0,0) bypassing the pole s = 1 from above gives N(T) = Δarg ξ / 2π, compared with the number of on-line zeros found independently. The equality N_strip = N_line at each height operationalises the Riemann Hypothesis; at thirteen heights up to T ≈ 1000 it holds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Anchors N(T) | 0 / 3 / 10 / 29 / 79 / 138 / 202 / 269 / … / 649 | = n_line |
| Arithmetic bridge fp ↔ mpmath (T = 100.07) | |ΔN| = 2.6e-26 | machine rigour |
| Residual S(T) on [0, 1.13e6] | maximum 1.7994 (within ±1.8) | classics reproduced |
| Second moment Σγ² (K6) | deviation from (T³/6π)(ln(T/2π)−1/3) = 8.8e-7 | formula exact |
| Gaps below T = 1000 | min 0.3104 · max 6.887 · mean 1.521 | Lehman–Odlyzko |
| The 2π aliasing trap | first version lost turns (N=5 instead of 10) | found and fixed |

## Method

A two-tier implementation: a numpy branch with a recursively adaptive step (the double leaf condition: |wrap| ≤ 0.3 AND length ≤ h_safe from the |ζ′/ζ| bounds) and an mpmath branch at dps = 26 for reference heights. The pole is bypassed from above by a small semicircle; by lemma T3 the additive +1 is NOT applied — its absence is verified by the S(T) cross-check and the anchors of the zero file.

## Figures

| File | Where |
|---|---|
| `fig03_argument_en.png` | 600 dpi — `figures_hires/en/fig03_argument_en.png`; экран — `figures/en/` |
| `fig04_gaps_en.png` | 600 dpi — `figures_hires/en/fig04_gaps_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c2_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c2_argument.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> Verification in the strip up to T = 1000 is not a proof of RH for all heights; it is the honest boundary below which the counting agrees component by component.
> The K6 story is instructive: the first version of the second-moment formula carried a factor error of 4π³ ≈ 124, found through the mismatch with the data; the final agreement is a property of the formula, not a fit.

## Verdict

**{'ru': 'RH верифицирована в полосе до T = 1000 (649 = 649)', 'en': 'RH verified in the strip up to T = 1000 (649 = 649)'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C2 · The argument principle up to T = 1000*
