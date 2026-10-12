# Функция V4 · Паспорт оператора (Th1)

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Определён ли оператор строго и что доказано о нём? Паспорт P1–P4.**

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

Определён ли оператор строго и что доказано о нём? Паспорт P1–P4.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V04 (plan Solution 4) | committed verdict |
| Key numbers | ‖H−H†‖ = 0 (точно); ‖Hv−λv‖ = 8.8e-15; спаривание λ↔−λ (W=0) 8.2e-15. Th1 доказана. | measured/proved |
| Verdict note | Th1 доказана: эрмитовость по построению, спектр вещественен, киральность α=½/W=0 — бипартидность | honest |

## Method

rpbridge/operator.py: явные формулы элементов, батарея L ∈ {12,16,24,32} × ручки; эрмитовость/невязки/киральность.

## Figures

| File | Where |
|---|---|
| `fig04_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v04_verdict.json` | committed verdict of the campaign |
| `computations/V04_operator_passport/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v04_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v04     # fresh recomputation
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

**{'ru': 'Th1: эрмитовость и вещественность — доказано', 'en': 'Th1: hermiticity and reality — proved'}**

---

*AB Research Program v1.1.0 · V04 · Паспорт оператора (Th1)*
