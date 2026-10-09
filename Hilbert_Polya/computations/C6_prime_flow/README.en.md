# C6 · The prime flow, the co-location kernel and the ψ-ladder

![version](https://img.shields.io/badge/version-1.0.0-298bbc) ![](https://img.shields.io/badge/series-C1--C8-3b4f58) ![](https://img.shields.io/badge/statuses-honest-3a6b4f)

> **Φ_p = ½ln p; exact co-location (Φ_p,Φ_q) ≡ Φ_pq (1.35e-14); the resolution kernel δ(d) with ξ_mult ≈ 2–3 cells; the ψ-ladder: corr = 0.972 for zeros, null zone for gates; universality washes the codings out.**

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

Does the arithmetic of primes live in the phase layer of the vortex cloud? Three questions: is the flow compositive (M1); does the ladder ψ(x) encode the zero structure of ζ (M2); does the spectrum see the codings, or does GUE universality wash them out (M3). The answers: the flow composites exactly, the ladder matches the zeros, the spectrum does not.

## Results

| Quantity | Value | Status |
|---|---|---|
| Co-location (Φ_p,Φ_q) ≡ Φ_pq (T4) | max|ΔE| = 1.35e-14 | proven+measured |
| Resolution kernel δ(d) (T5) | 0 → 3.2e-3 → 1.5e-2 → ~2e-2 (d≈4–6) | ξ_mult ≈ 2–3 cells |
| First-order additivity | fails (~1e-2) | the response is nonlinear |
| ψ-ladder: 200-zero reference | corr = +0.972, max err 4.2 | the prime weight of the zeros |
| ψ-ladder: gates | +0.24/+0.13/+0.09/−0.12 | null zone (H5 — NO) |
| M3: 4 flow codings | ⟨r⟩ = 0.585–0.611, spread 0.026 | one GUE class |

## Method

Flow: Φ_p = ½ln p on the lattice phases; co-location — the coincidence of the (p,q) node with the pq node in the phase layer. The kernel δ(d) — the response of a composite node to the distance d between factors. The ψ-ladder: the reference over the first 200 zeros ψ_ζ(x) = x − √x·Σe^{iγ ln x}/(½+iγ) − ln2π − ½ln(1−x⁻²) against the von Mangoldt sieve up to 10⁶; the methodological lesson — a window at γ~500 gives corr 0.48, the reference must live at the same heights. The M3 codings — random, 1/√p, ln p, D10 — at fixed positions.

## Figures

| File | Where |
|---|---|
| `fig11_coloc_en.png` | 600 dpi — `figures_hires/en/fig11_coloc_en.png`; экран — `figures/en/` |
| `fig12_psi_en.png` | 600 dpi — `figures_hires/en/fig12_psi_en.png`; экран — `figures/en/` |

## Monographs

`monograph_ru.docx` · `monograph_ru.pdf` · `monograph_en.docx` · `monograph_en.pdf`

Полная монография этого вычисления (постановка, теоремы, таблицы, рисунки,
честные ограничения): 7–9 страниц, один и тот же контент на двух языках.

## Data

| Файл | Содержание |
|---|---|
| `data/results.json` | закоммиченный вердикт кампании |
| `data/` (npz/csv) | кривые и таблицы |
| `../data/c6_*.json` | дубликат вердикта в общем реестре |

## Reproduction

```bash
# экскурсия по вердикту (~секунды, файл нулей не нужен)
python3 campaigns/run_c6_primes.py
```

Сид серии — 96; потоки RNG фиксированы (engine/hamiltonian.py). Все
зависимости — в `requirements.txt`.

## Honest notes

> H5 is a negative verdict with a positive control: the 0.972 correlation for the zeros shows the method sees the prime weight when it exists.
> Spectral codings (M3) are a universal mechanism without RH-proving force; an honest coding presents itself in the flow (T4) and the ladder (M2).

## Verdict

**{'ru': 'T4 доказана; Г5 — НЕТ, измерено; универсальность стирает кодировки', 'en': 'T4 proven; H5 — NO, measured; universality washes the codings out'}** — подробности: `data/results.json`, монография, и
`independent_verification/` (IVP-проверки этой кампании).

---
*Hilbert Polya Bridge v1.0.0 · C6 · The prime flow, the co-location kernel and the ψ-ladder*
