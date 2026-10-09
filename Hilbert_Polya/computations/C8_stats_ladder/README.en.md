# C8 · The statistics ladder and spin structures

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Poisson/GOE/GUE governed by symmetry (T10); GSE is structurally unreachable (T²=+1); spinor64: 64 spin structures → 4 Hamiltonians (T8) with isospectrality 1.1e-14.**

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

Which random-matrix classes does the lattice realise, and what governs them? And what do discrete phase structures encode — is there a hidden variable of arithmetic among them? The answers: the class is set by symmetry (the Dyson triplet); discrete codings are exact, but their capacity is set by phase symmetry, not by the number of structures.

## Results

| Quantity | Value | Status |
|---|---|---|
| Clean lattice | ⟨r⟩ = 0.324–0.386 | Poisson/clustering |
| Real disorder w = 1–4 | ⟨r⟩ = 0.520–0.538 | GOE plateau |
| Strong disorder w = 16–32 | ⟨r⟩ = 0.387 | Poisson (localization) |
| Complex vortices Nv ≥ 8 | ⟨r⟩ = 0.597–0.612 | GUE |
| GSE | T² = +1 → unreachable | architectural constraint |
| spinor64 E1 | 64 classes/84 edges; orbits 28/21/7/7/1; Arf 28/36 | bit-for-bit vs reference |
| spinor64 E2 (T8) | exactly 4 unique ⟨r⟩: 0.59348/0.59682/0.60054/0.60271 | 64 → 4 by (φx,φy) pairs |
| Orbit isospectrality | max|Δλ| = 1.02e-14 | machine precision |

## Method

An 11-channel ladder (n_real up to 5, n_spacings up to 1715): Nv, extra disorder w, boundaries; classification by ⟨r⟩ and KS against three references. spinor64: the 64 spin-structure classes of the Klein quartic (φx = π(e1+e3+e5), φy = π(e2+e4+e6) mod 2π) — the reduction to 2×2 = 4 classes; isospectrality is checked within orbits.

## Figures

| File | Where |
|---|---|
| `fig14_ladder_en.png` | 600 dpi — `figures_hires/en/fig14_ladder_en.png`; экран — `figures/en/` |
| `fig15_spinor_en.png` | 600 dpi — `figures_hires/en/fig15_spinor_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c8_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c8_stats_ladder.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> Universality is an attractor: it cannot witness arithmetic, because it erases everything but symmetry.
> All statistics is confirmed within the Dyson triplet; GSE is closed architecturally, not numerically.

## Verdict

**{'ru': 'Г3 — ДА; T8, T10', 'en': 'H3 — YES; T8, T10'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C8 · The statistics ladder and spin structures*
