# Функция V5 · Контролируемый предел L → ∞

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Сходится ли спектральный объект при росте решётки? Три вида сходимости и закон ошибки.**

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

Сходится ли спектральный объект при росте решётки? Три вида сходимости и закон ошибки.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V05 (plan Solution 5) | committed verdict |
| Key numbers | e(L) ≈ a·L^(−0.86), R² = 0.80; перекрытие проекторов при BC-возмущении 0.043; предел — открытое обязательство. | measured/proved |
| Verdict note | устойчивый степенной закон конечномерной ошибки обнаружен; экстраполяция за пределы прогона — оценка, а не доказательство сходимости | honest |

## Method

rpbridge/limits.py: вложимые вихри (масштабирование от L=12); C1 уровни, C2 проекторы (BC-возмущение), C3 след; МНК законов.

## Figures

| File | Where |
|---|---|
| `fig05_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v05_verdict.json` | committed verdict of the campaign |
| `computations/V05_limit_lattice/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v05_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v05     # fresh recomputation
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

**{'ru': 'Степенной закон ошибки измерен; сходимость L→∞ — оценка, не доказательство', 'en': 'Power error law measured; L→∞ convergence is an estimate'}**

---

*AB Research Program v1.1.0 · V05 · Контролируемый предел L → ∞*
