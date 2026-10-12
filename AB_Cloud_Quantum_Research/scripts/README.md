# 🔧 scripts/ — пайплайны пакета AB Cloud Quantum Research

| Скрипт | Что делает |
|--------|-----------|
| `make_tiled_figures.py` | 12 плиточных фигур 2×2 («4 измерения») @600 dpi для Th1–Th6 из закоммиченных вердиктов → `figures_tiled/{ru,en}/` + `theorems_lemmas/T0K_*/figures/` |
| `make_theorem_docs.py` | 12 документов теорем (RU/EN × PDF/DOCX) с внедрённой плиточной фигурой; рендеры и контент — из `modules/core_spectrum` без дублирования |
| `make_theorem_readmes.py` | 6 детальных README папок теорем (вывод, 4 измерения, границы, EN summary) |
| `make_banner.py` | анимированный баннер `assets/banner.gif` (критическая прямая + нули ζ) и логотип `assets/logo*.svg/png` |
| `make_release.py` | SHA256SUMS.txt + ZIP релиза в `/home/z/my-project/download/` |
| `validate_package.py` | чистая проверка (95+): структура, версии, вердикты, 36 документов, 20 фигур, веб-лаборатории, формальный слой, витрина |
| `make_datasets.py` | курируемые данные: flagship_numbers, campaign_timeline (43 кампании), эталон 660 нулей ζ → `datasets/` |
| `make_atlas.py` | атлас флагманов — плитка 2×2 (слепые нули · компилятор · след·простые · CHSH) @600 dpi → `atlas/` |
| `make_timeline.py` | хронологическая карта 43 кампаний @600 dpi → `timeline/` |
| `make_whitepaper.py` | белый отчёт исследования (RU/EN PDF, числа из вердиктов) → `whitepaper/` |

Скрипты вспомогательного исследования — в
`research/realtime_spinor_memory/` (`make_figures.py`,
`make_theorem_docs.py`, `experiments/run_all.py`).

## Быстрый старт

```bash
python3 scripts/make_tiled_figures.py     # фигуры
python3 scripts/make_theorem_docs.py      # 24 doc-файла (12 док-ов)
python3 scripts/make_theorem_readmes.py   # README теорем
python3 scripts/make_banner.py            # assets
python3 scripts/validate_package.py       # самопроверка
python3 scripts/make_release.py           # релиз
```

## Зависимости

Python ≥ 3.10: `matplotlib`, `numpy`, `Pillow`, `reportlab`, `python-docx`,
`openpyxl`, `pypdf` (см. `../requirements.txt`). Рендеры теорем используют
шрифты FreeSerif из системы. Julia-программа запускается своим стеком:
`julia modules/verifier_multilang/experiments/run_all.jl all`.

## English summary

`scripts/` builds everything derived in the merged package: tiled 4-dimension
figures (600 dpi), the 12 bilingual theorem documents with embedded tiles,
theorem READMEs, the animated banner/logo assets, package validation and the
release ZIP. Renderers and theorem content are reused from the mother
package — no source duplication.
