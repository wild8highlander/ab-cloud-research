# C7 · Wave-packet dynamics

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Coherent propagation, reflection and scattering on L=96; energy conserved to 1e-15; the ζ-cloud is 16× more transparent than random in the far wing — the dynamical face of the Montgomery pair correlations.**

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

If the lattice resonator is an electron on a flux lattice, the packet must move: propagate coherently, reflect from boundaries, scatter on vortices. And if the ζ-phase structure is physical, the ζ-cloud must behave differently from a random cloud of the same density. It does — in three measured effects.

## Results

| Quantity | Value | Status |
|---|---|---|
| Energy conservation | 1e-15 on every trajectory | honest dynamics |
| Coherence (clean lattice) | ⟨x⟩: 24 → 4.3 (reflection, t≈14.5) → 44 | billiard trajectory |
| Vortex scattering | Nv=16: nearly transparent; Nv=64: R=0.39; Nv=256: R=0.47 | a monotone braking effect |
| Transverse drift (ζ Nv=256) | ⟨y⟩: 48 → 38; random: none | the phases steer |
| Transport P(x ≥ 90) | ζ-cloud 0.0032 vs random 0.0002 (×16) | the D10 effect reproduced |

## Method

A sparse 96×96 Hamiltonian (open bc), step dt = 0.1, horizon T = 40, the packet by the D10 convention. All the dynamics lives on the self-dual line α = ½, where the π flux turns the lattice into a discretised massless Dirac equation — criterion H4.

## Figures

| File | Where |
|---|---|
| `fig13_dynamics_en.png` | 600 dpi — `figures_hires/en/fig13_dynamics_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c7_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c7_dynamics.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> The identification of the self-dual line α = ½ with Re(s) = ½ is a conjectural bridge: statistical support exists (D7/D10), identity does not.
> The electron motion is confirmed in the dynamical sense; it is not a statement about the spectrum (see C3–C5).

## Verdict

**{'ru': 'Г4 — ДА (динамика честная); мост к Re(s)=½ — конъектура', 'en': 'H4 — YES (honest dynamics); the bridge to Re(s)=½ is a conjecture'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C7 · Wave-packet dynamics*
