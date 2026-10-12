# Функция V19 · Сшивка ветвей алгебраической функции

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Как сшить ветви полной алгебраической функции критической прямой? Механизм hodge-laboratory: монодромная склейка листов и точный фазовый закон ζ^{ra+sb}.**

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

Как сшить ветви полной алгебраической функции критической прямой? Механизм hodge-laboratory: монодромная склейка листов и точный фазовый закон ζ^{ra+sb}.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V19 (plan Solution 19) | committed verdict |
| Key numbers | Фазовый закон 1.3e-40; ортогональность 225/5.1e-30; чередование 1999/1999; замыкание 138=138 (dev 5.0e-10); θ-лестница 0.832; когерентность 0.9995 (z = 43.4); flagship 4.5e-40. | measured/proved |
| Verdict note | ALGEBRAIC_CERTIFICATE: Γ-фаза несёт оба признака | honest |

## Method

rpbridge/stitching.py, четыре слоя: A — эталон (Ферма-накрытие, tanh-sinh по гладкой параметризации t = w^N/(w^N+(1−w)^N)); B — Z₂-монодромия Z_id (чередование знаков, аргументное замыкание); C — сшитый объект (Γ-фаза: θ-лестница + знаковая когерентность); D — регрессия R1/R2/R4.

## Figures

| File | Where |
|---|---|
| `fig20_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v19_verdict.json` | committed verdict of the campaign |
| `computations/V19_branch_stitching/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v19_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v19     # fresh recomputation
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

**{'ru': 'ALGEBRAIC_CERTIFICATE: Γ-фаза несёт оба признака', 'en': 'ALGEBRAIC_CERTIFICATE: the Γ-phase carries both signatures'}**

---

*AB Research Program v1.1.0 · V19 · Сшивка ветвей алгебраической функции*
