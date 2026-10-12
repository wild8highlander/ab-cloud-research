# Функция V3 · Скан критической линии

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Оптимален ли σ = ½ по спектральной статистике? Скан D(σ) по 11 точкам с плацебо и тремя seeds.**

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

Оптимален ли σ = ½ по спектральной статистике? Скан D(σ) по 11 точкам с плацебо и тремя seeds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V03 (plan Solution 3) | committed verdict |
| Key numbers | Кривая плоская: argmin ≈ 0.8, C_h < 0, минимум в ½ отсутствует и не подтверждается плацебо. | measured/proved |
| Verdict note | минимум D(σ) в окрестности σ = 1/2 отсутствует или неустойчив — специфичность линии измерена, а не постулирована (см. честные замечания) | honest |

## Method

rpbridge/critical_line.py: веса q_k(σ) = log|ζ(σ+iγ̃_k)| по серединам γ̃ (вне нулей); кривизна C_h; плацебо на переставленных ординатах.

## Figures

| File | Where |
|---|---|
| `fig03_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v03_verdict.json` | committed verdict of the campaign |
| `computations/V03_critical_line_scan/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v03_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v03     # fresh recomputation
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

**{'ru': 'Заявление об оптимальности σ=½ снято (не подтверждено)', 'en': 'The σ=½ optimality claim is withdrawn (not confirmed)'}**

---

*AB Research Program v1.1.0 · V03 · Скан критической линии*
