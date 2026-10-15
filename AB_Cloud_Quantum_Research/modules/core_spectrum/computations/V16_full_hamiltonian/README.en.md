# V16 · Full Hamiltonian × Algebraic Function

![version](https://img.shields.io/badge/version-1.2.0-298bbc) ![](https://img.shields.io/badge/series-V01--V19-3b4f58) ![](https://img.shields.io/badge/status-honest-3a6b4f)

> **Does the full handle space couple the lattice to the ζ zeros via the θ-phase of Z_id — no GUE reduction? A map of 96 configurations × 3 seeds.**

[← Back to the main README](../../README.md)

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

Does the full handle space couple the lattice to the ζ zeros via the θ-phase of Z_id — no GUE reduction? A map of 96 configurations × 3 seeds.

## Results

| Quantity | Value | Status |
|---|---|---|
| Campaign | V16 (plan Solution 16) | committed verdict |
| Key numbers | max r_align = +0.160 (z = 2.49 < 6 — no identity); weights θ/log|ζ|/none: −0.108/+0.092/−0.085 — all inside the null zone; PC Z_id↔file r = 1.0 (38 zeros, 4.9e-10). | measured/proved |
| Verdict note | Level identity — YES (D_nn bridge); bit-level branch open | honest |

## Method

rpbridge/fullham.py: the weight q_k = θ(γ̃_k)/π (algebraic phase), the r_align metric (ΔU ↔ Δγ increments, bridge on the first 50 levels, out-of-sample on 150); the null — 200 permutations; PC — Z_id zeros against the file.

## Figures

| File | Where |
|---|---|
| `fig17_en.png` | 600 dpi — `figures_hires/en/`; infographics — `figures/en/` |

## Monographs

| File | Format |
|---|---|
| `monograph_en.pdf` | PDF |
| `monograph_en.docx` | DOCX |

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

**{'ru': 'Тождество уровней — ДА (мост D_nn)', 'en': 'Level identity — YES (the D_nn bridge: gates at the zeros\' level); the bit-level branch does not close (z = 2.49); the algebraic function is the r=1 object'}**

---

*AB Research Program v1.1.0 · V16 · Full Hamiltonian × Algebraic Function*
