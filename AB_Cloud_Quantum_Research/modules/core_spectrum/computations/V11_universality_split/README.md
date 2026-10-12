# Функция V11 · Универсальность после разрушения

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Что выживает при разрушении арифметики? Режимы D1/D2/D3 против универсальных и арифметических метрик.**

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

Что выживает при разрушении арифметики? Режимы D1/D2/D3 против универсальных и арифметических метрик.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V11 (plan Solution 11) | committed verdict |
| Key numbers | ⟨r⟩ = 0.61 → 0.59 (выживает); сдвиг r_EF 0.17 < 2σ(A0) = 0.57 — шум-доминировано; разделение несёт V7. | measured/proved |
| Verdict note | GUE-универсальность выживает при всех режимах разрушения арифметики (⟨r⟩ в классе); арифметически-чувствительная метрика r_EF на окнах 200 уровней доминируется шумом (сдвиг режимов < 2σ собственного разброса A0) — на этом разрешении разделение признаков не достигается; разделение несёт следовой уровень V7 (PC0) | honest |

## Method

rpbridge/universality.py: 3 seeds × 4 режима; ⟨r⟩ и r_EF; нулевой разбор — собственный scatter A0.

## Figures

| File | Where |
|---|---|
| `fig11_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v11_verdict.json` | committed verdict of the campaign |
| `computations/V11_universality_split/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v11_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v11     # fresh recomputation
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

**{'ru': 'Универсальность — аттрактор; арифметика на окнах не видна', 'en': 'Universality is an attractor; arithmetic invisible on windows'}**

---

*AB Research Program v1.1.0 · V11 · Универсальность после разрушения*
