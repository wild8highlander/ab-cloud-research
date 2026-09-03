# lab-3d/outputs — Committed Verification Runs (2026-07-31)

Four complete, timestamped output folders produced by the 3D laboratory on
2026-07-31 and committed verbatim so the figures and numbers can be inspected
without re-running the simulations. Every folder follows the same report
convention: `<mode>.json` (machine dump) + `<mode>.md` / `.txt` / `.html`
(human reports) + `<mode>_summary.csv` (flat table) + all figures in both
PDF (vector) and PNG (600 dpi).

## Run inventory

| Folder | Mode | What it contains |
|---|---|---|
| `full_verification_2026-07-31_15-33-39/` | G — full verification | reviewer-point checks: ⟨r⟩ = 0.6159 vs GUE 0.5996, KS tests, FSS to N = 5000, Arf invariant 0 across N ∈ {16…4096}, Dirac cone β = 1.0, decay slope −0.967; figures 01–11 |
| `deep_zeros_2026-07-31_15-36-34/` | H — deep ζ analysis | 5000 embedded zeros: all on Re s = 1/2, NN spacing PDF, R₂(x), K(τ), S(T) statistics, decay times τₙ = ħ/γₙ |
| `3d_bridge_2026-07-31_15-36-37/` | I — AB↔Riemann bridge | 9 visualizations: spectral staircase, (α,σ) phase diagram, Dirac-cone family, form-factor surfaces, wavefunction density, decay-time manifold, pair-correlation landscape |
| `3d_advanced_2026-07-31_15-51-47/` | J — advanced 3D | Chern marker surface+heatmap, probability current, winding number W = 1 (11 points), Hofstadter butterfly, 121 exceptional-point candidates, edge-state localization |

## Headline numbers (recap)

| Metric | Value |
|---|---|
| ⟨r⟩ (ζ zeros / AB-Cloud) | 0.6159 / same within error (GUE 0.5996) |
| KS p (AB-Cloud vs ζ) | 0.27–0.88 — indistinguishable |
| Permutation test | Z = 14.10σ, p < 10⁻⁴⁴ |
| Arf invariant | 0 at every resolution |
| Winding number at RH | 1 (11 checkpoints) |

## How to regenerate

The folders are reproducible from `../code/` with fixed seeds (folder names
will carry the new timestamp):

```bash
cd ../code
python3 ab_cloud_3d_en.py    # choose mode G / H / I / J in the menu
```

## Reading the reports

Start with `<mode>.md` — it has the verdict table with raw numbers; the
`.json` holds the same data machine-readably; `_summary.csv` is convenient
for spreadsheets. Figure files are numbered to match the section order of
the `.md` report.

## Кратко (по-русски)

- Четыре зафиксированных прогона 3D-лаборатории от 2026-07-31: полная
  верификация (G), глубокий анализ нулей (H), мост AB↔Риман (I), продвинутая
  3D-визуализация (J).
- В каждой папке: json/md/txt/html-отчёты, summary.csv и все рисунки в
  PDF+PNG.
- Ключевые числа: ⟨r⟩ = 0.6159 (GUE 0.5996), KS p = 0.27–0.88, Z = 14.10σ,
  Arf = 0 на всех масштабах, W = 1.
- Воспроизводится из `../code/` меню-режимами G/H/I/J с фиксированными
  seed'ами.
