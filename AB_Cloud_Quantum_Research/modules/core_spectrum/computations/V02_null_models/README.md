# Функция V2 · Арифметические контрольные модели

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Даёт ли хаотичность решётки ту же статистику без арифметики? Пять семейств моделей против предрегистрированного вектора S.**

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

Даёт ли хаотичность решётки ту же статистику без арифметики? Пять семейств моделей против предрегистрированного вектора S.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V02 (plan Solution 2) | committed verdict |
| Key numbers | M0: ⟨r⟩ = 0.6093, D_KS = 0.0499 — GUE-класс; N3 без вихрей: 0.273 — вне класса; лестница эталонов воспроизведена. | measured/proved |
| Verdict note | AB-cloud попадает в GUE-класс вместе с N1/N4; специфичность арифметики измеряется не ⟨r⟩, а арифметически-чувствительными метриками V7/V11 | honest |

## Method

rpbridge/nullmodels.py: M0/N1/N3/N4 + эталоны GUE/GOE/Пуассон; ансамблевый GUE-эталон для D_KS (16 матриц); Бонферрони 5 семейств.

## Figures

| File | Where |
|---|---|
| `fig02_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v02_verdict.json` | committed verdict of the campaign |
| `computations/V02_null_models/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v02_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v02     # fresh recomputation
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

**{'ru': 'Класс GUE не специфичен; арифметика ищется в следах (V7)', 'en': 'GUE class is not specific; arithmetic lives in traces (V7)'}**

---

*AB Research Program v1.1.0 · V02 · Арифметические контрольные модели*
