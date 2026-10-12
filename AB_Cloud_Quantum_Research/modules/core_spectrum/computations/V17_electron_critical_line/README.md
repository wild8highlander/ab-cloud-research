# Функция V17 · Электрон на критической прямой

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Проходит ли электрон (волновой пакет) когерентно по каналу самодуальной линии α = ½ и направляет ли его ζ-облако? Волновод 96×24, T = 40, три облака.**

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

Проходит ли электрон (волновой пакет) когерентно по каналу самодуальной линии α = ½ и направляет ли его ζ-облако? Волновод 96×24, T = 40, три облака.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V17 (plan Solution 17) | committed verdict |
| Key numbers | Энергия 1.8e-15; транзит: чистая 0.160 / ζ 0.112 / случайное 0.069 (ζ/ran = ×1.62); D_y: ζ 2.81 против 0.54; r_phase: ζ −0.96 против random −0.52. | measured/proved |
| Verdict note | Динамика честная; ζ-облако направляет ×1.62; мост «линия ½ = Re(s)½» — конъектура (Г4 ДА) | honest |

## Method

rpbridge/electron.py: точная динамика в собственном базисе (2304×2304), пакет σ=3, k₀=π/2; транзит P(x≥88), отклонение D_y, когерентность C(t), фазовое сопровождение θ(траектория).

## Figures

| File | Where |
|---|---|
| `fig18_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v17_verdict.json` | committed verdict of the campaign |
| `computations/V17_electron_critical_line/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v17_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v17     # fresh recomputation
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

**{'ru': 'Динамика честная; ζ-облако направляет ×1.62; мост «линия ½ = Re(s)½» — конъектура (Г4 ДА)', 'en': 'Honest dynamics; the ζ-cloud guides ×1.62; the line½ = Re(s)½ bridge is a conjecture (H4 YES)'}**

---

*AB Research Program v1.1.0 · V17 · Электрон на критической прямой*
