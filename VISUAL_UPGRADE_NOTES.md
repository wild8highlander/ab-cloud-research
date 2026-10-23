# AB-Cloud — Visual README Upgrade

Этот архив содержит визуальное обновление README-документации репозитория
и файлы исправления CI. Все пути внутри архива совпадают со структурой
репозитория — распаковка поверх клона применяет всё одной командой.

## Что внутри

**Новые визуальные ассеты (14 файлов), `assets/visuals/`:**

| Файл | Тип | Источник |
|---|---|---|
| `charts/zeros_pair_correlation.{light,dark}.svg` | график | реальные данные: frozen `zeros50k.txt` (50 000 ζ-нулей), ⟨r⟩ = 0.6119 |
| `charts/zeros_critical_strip.{light,dark}.svg` | график | реальные данные: первые 100 нулей из frozen-датасета |
| `charts/test_cost_ranking.{light,dark}.svg` | график | реальные тайминги флагманского прогона `run_20260902_134759` |
| `charts/spinor64_classes.{light,dark}.svg` | график | реальные данные E2: `spinor64/output/spinor64_table.csv` |
| `ai/hero_{dark,light}.png` | AI-обложка | концептуальная абстракция (критическая линия, GUE-облака) |
| `ai/ab_cloud_concept_{dark,light}.png` | AI-схема | концептуальная иллюстрация (решётка + вихри + ζ-нули) |
| `animated/ab_flux_vortex.svg` | анимация | SMIL/CSS, адаптивная тема (prefers-color-scheme) |
| `animated/gue_transition.svg` | анимация | SMIL/CSS, переход Пуассон → GUE |

**Обновлённые README (19 файлов):** главный README, AB_Cloud_Quantum_Research,
AB_Cloud_Academic_Package, Hilbert_Polya, dirac-lab, meridian-spectral-observatory,
code, verification (+ spinor64), formal (+ lean4), lab-3d, apps (+ lab3d,
dashboard), monographs, results, docs, modules/processor_ab, modules/core_spectrum.

В каждом: Mermaid-схемы (там, где их не было), графики через `<picture>`
с переключением светлая/тёмная тема, навигационные строки «🧭 Navigation».
Существующий текст сохранён 1:1 — только добавления.

**Фикс CI (2 файла):** `.github/workflows/ci.yml` (добавлен `typer` в pip install)
и `AB_Cloud_Academic_Package/AB_Cloud_Academic_Package/06_code/python/run.py`
(совместимость с typer ≥ 0.27, вендорящим click). Все 9 контрактных тестов
проверены локально на свежем клоне — зелёные.

## Как применить (Termux / Android)

```bash
cd /storage/emulated/0/Download/ab-cloud-research
unzip -o /storage/emulated/0/Download/ab-cloud-visual-upgrade.zip -d .
git add -A
git commit -m "docs: visual README upgrade (charts, AI covers, animated SVG, mermaid); fix(ci): typer"
git push
```

Если `unzip` не установлен: `pkg install unzip -y`.

## Как откатить (если что-то не понравится)

```bash
git restore .                                   # вернёт все изменённые файлы
git clean -fd assets/visuals/                   # удалит новые ассеты (только эта папка)
```

## Примечания о честности данных

- Все четыре графика построены программно (matplotlib) из коммитнутых
  артефактов репозитория — не декорация; источник указан в подписи каждого.
- AI-иллюстрации и анимации помечены в README как *conceptual, not raw data*.
- Значение ⟨r⟩ = 0.6119 на графике — собственная перепроверка frozen-датасета;
  оно совпадает с честным выводом v3.0 сьюта (⟨r⟩ = 0.6119 на 50 000 нулей)
  и лежит внутри GUE-диапазона [0.5772, 0.6212].
