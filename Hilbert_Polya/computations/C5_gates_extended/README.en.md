# C5 · The extended gate family

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **35 new gates + 2 decoys across six new handles: twists, anisotropy, flux shift, staggered mass, vortex profile, signs and boundaries. Verdict: the H2 gap is stable — the GUE class and the null zone for everyone.**

[← Back to the main README](../../README.md)

## Contents

1. [The campaign question](#the-campaign-question)
2. [Results](#results)
3. [Method](#method)
4. [Figures](#figures)
5. [Monographs](#monographs)
6. [Data](#data)
7. [Reproduction](#reproduction)
8. [Honest notes](#honest notes)
9. [Verdict](#verdict)

---

## The campaign question

Perhaps identity is reached not on the C3 protocol handles but on some others? The campaign extends the handle space by six dimensions and checks whether any of them moves a gate out of the null zone. The regression control: the protocol reference gate reproduces the mean spacing of the C3 CSV bit-for-bit (1.4e-16).

## Results

| Quantity | Value | Status |
|---|---|---|
| Twists (φx, φy) | 3 spin-structure classes | |r_H7| ≤ 0.033 |
| Anisotropy t_x/t_y | 0.8; 1.25 | |r_H7| ≤ 0.030 |
| Flux shift δα | ±0.02; ±1/24 on the torus | |r_H7| ≤ 0.034 |
| Staggered mass m | 0.15; 0.35 | |r_H7| ≤ 0.032 |
| Vortex profile | site | midpoint | |r_H7| ≤ 0.033 |
| Signs and boundaries | neutral/all_plus/random · open/torus | |r_H7| ≤ 0.044 |
| Family overall | ⟨r⟩ = 0.498–0.502 (0.500±0.001) | GUE class for all |

## Method

All handles are implemented in engine/hamiltonian.py: twists — phases on the torus wrap links (the C8 spin structures); anisotropy — t_x = t/aniso; flux shift — α_eff = α + δα (on the torus only the admissible ±1/24); mass — the staggered potential (−1)^{ix+iy}; the midpoint profile — the vortex angle taken from the link midpoint (a finite-radius core); signs — neutral (protocol), all-plus, random; boundaries — open or torus. The degenerate corner W = 0 + midpoint is replaced by W = 0.1 with a note.

## Figures

| File | Where |
|---|---|
| `fig09_handles_en.png` | 600 dpi — `figures_hires/en/fig09_handles_en.png`; экран — `figures/en/` |
| `fig10_gue_ext_en.png` | 600 dpi — `figures_hires/en/fig10_gue_ext_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c5_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c5_gates_ext.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> The family maximum of |r_H7| is reached on a random-sign decoy — the expected noise maximum, not a signal.
> The statement the gap is stable is a measurement over 37 configurations, not a theorem about all possible handles.

## Verdict

**{'ru': 'разрыв Г2 устойчив ко всем шести новым ручкам', 'en': 'the H2 gap is stable across all six new handles'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C5 · The extended gate family*
