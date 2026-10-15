# Функция V16 · Полный гамильтониан × алгебраическая функция

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Связывает ли полное пространство ручек гамильтониана решётку с нулями ζ через θ-фазу Z_id — без редукции к GUE? Карта 96 конфигураций × 3 seeds.**

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

Связывает ли полное пространство ручек гамильтониана решётку с нулями ζ через θ-фазу Z_id — без редукции к GUE? Карта 96 конфигураций × 3 seeds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V16 (plan Solution 16) | committed verdict |
| Key numbers | max r_align = +0.160 (z = 2.49 < 6 — тождества нет); веса θ/log|ζ|/none: −0.108/+0.092/−0.085 — все в нулевой зоне; PC Z_id↔файл r = 1.0 (38 нулей, 4.9e-10). | measured/proved |
| Verdict note | Тождество уровней замыкается мостом D_nn (затворы на уровне нулей, v2.0.7); битовая ветвь не замыкается во всём пространстве ручек (z = 2.49 < 6); алгебраическая функция — объект с r=1 | honest |

## Method

rpbridge/fullham.py: вес q_k = θ(γ̃_k)/π (алгебраическая фаза), метрика r_align (корреляция приращений ΔU ↔ Δγ, мост по первым 50 уровням, out-of-sample на 150); нулевая модель — 200 пермутаций; PC — нули Z_id против файла.

## Figures

| File | Where |
|---|---|
| `fig17_ru.png` | 600 dpi — `figures_hires/ru/`; infographics — `figures/ru/` |

## Monographs

| File | Format |
|---|---|
| `monograph_ru.pdf` | PDF |
| `monograph_ru.docx` | DOCX |

## Data

| File | Content |
|---|---|
| `data/v16_verdict.json` | committed verdict of the campaign |
| `computations/V16_full_hamiltonian/data/` | campaign artifacts |

## Reproduction

```bash
python3 campaigns/run_v16_*.py        # verdict tour (seconds)
python3 scripts/compute_all.py v16     # fresh recomputation
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

**{'ru': 'Тождество уровней — ДА (мост D_nn: затворы на уровне нулей); битовая ветвь не замыкается во всём пространстве ручек (z = 2.49); алгебраическая функция — объект с r=1', 'en': 'Level identity — YES (the D_nn bridge: gates at the zeros\' level); the bit-level branch does not close over the full handle space (z = 2.49); the algebraic function is the r=1 object'}**

---

*AB Research Program v1.1.0 · V16 · Полный гамильтониан × алгебраическая функция*
