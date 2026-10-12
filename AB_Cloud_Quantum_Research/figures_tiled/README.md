# 🖼️ figures_tiled/ — плиточные фигуры «4 измерения» (600 dpi)

Плиточные фигуры пакета AB Cloud Quantum Research: **каждая фигура — сетка 2×2, четыре
разных измерения измерений одной теоремы** (метрика · поведение по
инстансам · контроль · порог). Построены из закоммиченных вердиктов кампаний
(`modules/core_spectrum/data/v*_verdict.json`) — никаких рукотворных
чисел. Разрешение 600 dpi (6600×4560 px), стиль «Critical Line & Copper»,
полностью автономны (без внешних шрифтов).

## Файлы

| Файл | Теорема | Кампания-источник |
|------|---------|-------------------|
| `ru/th1_4dim_ru.png`, `en/th1_4dim_en.png` | Th1 эрмитовость | V4 |
| `ru/th2_4dim_ru.png`, `en/th2_4dim_en.png` | Th2 самосопряжённость | V8 |
| `ru/th3_4dim_ru.png`, `en/th3_4dim_en.png` | Th3 сертификаты | V12 |
| `ru/th4_4dim_ru.png`, `en/th4_4dim_en.png` | Th4 формула Ли | V15 |
| `ru/th5_4dim_ru.png`, `en/th5_4dim_en.png` | Th5 блочная редукция | V9 |
| `ru/th6_4dim_ru.png`, `en/th6_4dim_en.png` | Th6 следовая формула | V7 |

Те же фигуры продублированы в `theorems_lemmas/T0K_*/figures/` и ВНЕДРЕНЫ в
12 документов теорем (RU/EN × PDF/DOCX).

## Как перегенерировать

```bash
python3 scripts/make_tiled_figures.py   # 12 фигур × 600 dpi
```

Скрипт читает только вердикты; при обновлении кампаний фигуры
пересобираются теми же данными — бит-в-бит при неизменных вердиктах
(детерминированные seeds).

## Оригинальные основные графики

Все оригинальные фигуры трёх программ **сохранены без изменений**:
`modules/core_spectrum/figures_hires/` (fig01–fig20 × RU/EN),
`modules/core_spectrum/computations/*/figures/`,
`modules/processor_ab/figures_hires/` (fig01–fig06),
`modules/verifier_multilang/figures_hires/` (fig01–fig14).
Плиточные фигуры — ДОПОЛНЕНИЕ к оригиналам, а не замена.

## English summary

`figures_tiled/` holds the merged package's tiled figures: every figure is a
2×2 grid of four independent measurement dimensions of one theorem (metric ·
per-instance behaviour · control · threshold), built strictly from committed
campaign verdicts at 600 dpi in the «Critical Line & Copper» style, RU/EN.
The original main figures of all three programs remain untouched inside
`modules/*/figures_hires/` — the tiles complement, never replace them.
