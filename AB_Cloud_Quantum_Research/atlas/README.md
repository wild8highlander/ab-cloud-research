# 🏛️ atlas/ — атлас флагманских результатов

Одна плитка 2×2 «четыре измерения программы» (600 dpi, RU/EN),
собранная **только из закоммиченных вердиктов**:

| Панель | Результат | Источник |
|--------|-----------|----------|
| a) слепое чтение нулей ζ, T ≤ 1000 | 649/649 (ЭМ) + 639/639 (РС), кросс-движок 0.0 | `e17_verdict.json` |
| b) точный компилятор AB-облаков | 1−F ≤ 4.4e-16 (4×4) · 6.7e-16 (8×8), пороги 1e-12/1e-10 | `v20_verdict.json` |
| c) след H_ξ ↔ простые | r = 0.9996 против решётки (контроль) 0.76 | `v07_verdict.json` |
| d) нелокальность без сигналинга | CHSH S = 2√2 − 4.4e-16, коммутаторы 0 | `v20_verdict.json` (V24-превью) |

| Файл | Описание |
|------|----------|
| `atlas_flagships_ru.png` | атлас, 600 dpi, русский |
| `atlas_flagships_en.png` | атлас, 600 dpi, английский |

Перестроить: `python3 scripts/make_atlas.py`.

Отдельные плитки «4 измерения» для теорем Th1–Th6 — в
[`figures_tiled/`](../figures_tiled/README.md); для теорем TS1–TS3 — в
[`research/realtime_spinor_memory/figures/`](../research/realtime_spinor_memory/README.md).

## English summary

`atlas/` is the one-tile 2×2 flagship atlas (600 dpi, RU/EN) built only
from committed verdicts: blind ζ-zero reading (649+639), the exact
compiler (1−F ≤ 4.4e-16), trace↔primes (r = 0.9996 vs 0.76 control),
and no-signaling nonlocality (S = 2√2 − 4.4e-16). Rebuild with
`scripts/make_atlas.py`.
