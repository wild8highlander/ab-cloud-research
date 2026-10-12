# Функция V12 · Интервальные сертификаты (Th3)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Гарантированы ли численные границы? Гершгорин в рациональной арифметике + невязка в dps=40.**

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

Гарантированы ли численные границы? Гершгорин в рациональной арифметике + невязка в dps=40.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V12 (plan Solution 12) | committed verdict |
| Key numbers | 5/5 сертификатов содержат истинные λ; ширина ~1e-27; Гершгорин [−4.21, 4.21] накрывает спектр. | measured/proved |
| Verdict note | все сертификаты содержат истинные значения; интервалы — гарантированные, а не десятичные допуски; точность 1e-15 в float ≠ математическая точность модели (план, Решение 12) | honest |

## Method

rpbridge/intervalcert.py: fractions-радиусы; оценка Каутского δ²/gap; зазоры точно.

## Figures

| File | Where |
|---|---|
| `fig12_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v12_verdict.json` | committed verdict of the campaign |
| `computations/V12_interval_certificates/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v12_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v12     # fresh recomputation
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

**{'ru': 'Ключевые числа имеют гарантированные интервалы', 'en': 'Key numbers carry guaranteed intervals'}**

---

*AB Research Program v1.1.0 · V12 · Интервальные сертификаты (Th3)*
