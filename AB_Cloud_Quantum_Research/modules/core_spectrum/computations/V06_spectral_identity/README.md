# Функция V6 · Спектральное тождество

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Совпадает ли характеристическая функция оператора с ξ? Прямой тест и позитивный контроль H_ξ.**

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

Совпадает ли характеристическая функция оператора с ξ? Прямой тест и позитивный контроль H_ξ.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V06 (plan Solution 6) | committed verdict |
| Key numbers | Затворы: rank 0.036 — тождества нет; H_ξ: log-остаток 5.8e-10 — тождество есть (тривиально по построению). | measured/proved |
| Verdict note | тождество спектра (n ↔ нуль n) для решёточных затворов — НЕТ (ранговое соответствие в нулевой зоне); для H_ξ — ДА по построению; цель V6 — аналитическое тождество, а не подбор полинома | honest |

## Method

rpbridge/spectral_identity.py: ранги vs нули; контроль Адамара ln Π|z²−γ²| − ln|ξ| = const (регрессия a + b·z²); зазоры/кратности.

## Figures

| File | Where |
|---|---|
| `fig06_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v06_verdict.json` | committed verdict of the campaign |
| `computations/V06_spectral_identity/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v06_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v06     # fresh recomputation
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

**{'ru': 'Тождество: ДА для H_ξ, НЕТ для затворов (измерено)', 'en': 'Identity: YES for H_ξ, NO for gates (measured)'}**

---

*AB Research Program v1.1.0 · V06 · Спектральное тождество*
