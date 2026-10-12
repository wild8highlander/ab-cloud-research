# Функция V9 · Симметрийная редукция (Th5)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Разлагается ли спектр по симметрии? Магнитные трансляции тора и блоки.**

[← Back to the main README](../../README.ru.md)

## Contents

1. [Campaign question](#campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest remarks](#honest-remarks)
9. [Verdict](#verdict)

---

## Campaign question

Разлагается ли спектр по симметрии? Магнитные трансляции тора и блоки.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V09 (plan Solution 9) | committed verdict |
| Key numbers | ε_Ux = 0, ε_Uy = 9.4e-15; объединение 6 блоков = спектр (7.1e-15); вихри ломают симметрию (ε_g = 5.1). | measured/proved |
| Verdict note | Th5 доказана и верифицирована (тор без вихрей: спектр = объединение блоков характеров, внеблочные элементы нулевые); вихревое размещение ломает симметрию (ε_g = O(1)) — редукция объясняет скелет спектра, не арифметику нулей | honest |

## Method

rpbridge/symmetry.py: A = U(2,0), B = U(0,2) — абелева G = ℤ_L×ℤ_L; совместный собственный базис; блоки и их спектры.

## Figures

| File | Where |
|---|---|
| `fig09_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v09_verdict.json` | committed verdict of the campaign |
| `computations/V09_symmetry_reduction/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v09_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v09     # fresh recomputation
python3 -m pytest tests/ -q                     # theorem machinery
```

## Honest remarks

- Metrics are pre-registered; verdicts are committed and independent of
  fresh recomputation.
- The zero file is the only external data; no third-party research code
  is imported.
- Every claim of this campaign has a claim file (V14 audit) with the
  list of what it does NOT prove.

## Verdict

**{'ru': 'Th5 доказана и верифицирована; вихри разрушают симметрию', 'en': 'Th5 proved and verified; vortices break the symmetry'}**

---

*AB Research Program v1.1.0 · V09 · Симметрийная редукция (Th5)*
