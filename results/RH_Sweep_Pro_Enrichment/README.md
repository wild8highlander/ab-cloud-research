# RH_Sweep_Pro_Enrichment — комплект научного обогащения папок результатов

> Компаньон к `RH_Sweep_Pro_D.jl` (RH·SWEEP PRO v1.0) и к каталогу
> `Vortex_optimization` (тест 34). Редакция 1.0 · 16.10.2026.
> Русская версия — основная; английский глоссарий терминов — в отчёте
> (глава 13) и в `README_EN.md`.

## TL;DR

Папка типичного прогона RH-Sweep PRO содержит «сырые» артефакты
(plots/csv/txt/json), но не содержит научного слоя: README, словаря
данных, кривых метрик, GUE-пола, значимости по реализациям и манифеста
целостности. Кроме того, в RH_Sweep_Pro_D.jl v1.0 функции
`sweep_parameter`, `save_sweep_results` и `sweep_all_parameters`
**вызываются, но не определены** — PRO-режимы sweep падают с
`UndefVarError`. Этот комплект закрывает обе проблемы:

- **Julia-модуль** `julia/RH_Results_Enricher.jl` — repair-функции
  sweep-движка (патчи D-1/D-2) + автогенерация артефактов P0/P1
  (README, SUMMARY, словарь, config.json, манифест SHA-256, curves/,
  sensitivity/, GUE-пол, multi-seed);
- **шаблоны** `templates/` — README прогона, словарь данных, протокол
  прогона с сид-конвенцией теста 34, протокол верификации;
- **monograph/** — черновик главы монографии (PLOS-стиль) по итогам
  прогона;
- **enriched_example/** — готовые файлы для слияния в папку
  конкретного прогона `RH_Auto_5000_L64_s5_20261016_122739`
  (манифест посчитан по реальным файлам);
- **report/** — полный PDF-отчёт (23 стр.): аудит прогона, разрыв со
  стандартом теста 34, важность всех настроек, план обогащения,
  протоколы, двуязычный глоссарий.

## Результаты верифицированного прогона (контекст)

| Величина | Значение |
|:--|:--|
| Конфигурация | α = 1/π ≈ 0.31831 · W = 2.0 · σ = 0.5 · L = 64 · 5 реализаций |
| Composite Score | 84.85 / 100 · тесты 10/11 (RMT-ядро 6/6) |
| ⟨r⟩ | 0.59999 (R_GUE = 0.5996; отклонение 0.00039) |
| K corr(GUE) / corr(ζ) | 0.988 / 0.942 |
| N_AB / N_ζ | 6140 / 5000 (блоки B = 250) |
| Единственный FAIL | E(s=1) = 0.521 против 0.171 → ослабленное отталкивание (β = 1.72) |

## Быстрый старт

### Вариант А — у меня уже есть прогон, пересчитывать нельзя

1. Скопируйте содержимое
   `enriched_example/RH_Auto_5000_L64_s5_20261016_122739/` в свою папку
   прогона (README, SUMMARY, словарь, config.json, manifest.sha256).
2. Для P1 (кривые, GUE-пол, значимость, свежий манифест):

```bash
julia -e 'include("RH_Sweep_Pro_D.jl");
          include("RH_Results_Enricher.jl");
          include("julia/example_post_run.jl")'
```

### Вариант Б — буду запускать новые прогоны

Три строки интеграции (подробности — `julia/INTEGRATION.md`):

```julia
include("RH_Results_Enricher.jl")                       # после using-блока
# в конце _final_run(), перед return:
enrich_run(cfg, final_result, all_results, eigs_final, zeta_zeros;
           out_dir = cfg.output_dir)
# опционально после прогона:
gue_floor_multi_report(cfg; n_floor_ens = 20, n_seeds_sig = 5)
```

Каждый новый прогон автоматически получает README, SUMMARY, словарь,
config.json и манифест; sweep-режимы (`sweep_top10_pro`,
`sweep_combined_quick`, `sweep_all_parameters`) начинают работать и
пишут инкрементальную историю точек в `sensitivity/`.

## Состав

```
RH_Sweep_Pro_Enrichment/
├── README.md                        ← этот файл (RU)
├── README_EN.md                     ← English summary
├── julia/
│   ├── RH_Results_Enricher.jl       ← модуль обогащения (без зависимостей)
│   ├── INTEGRATION.md               ← интеграция 3 строки + патчи D-1/D-2
│   └── example_post_run.jl          ← обогащение готового прогона
├── templates/
│   ├── README_results_template.md   ← шаблон README прогона
│   ├── DATA_DICTIONARY.md           ← словарь 37 колонок + файлы P1
│   ├── RUN_PROTOCOL.md              ← сид-протокол (конвенция теста 34)
│   └── VERIFICATION_PROTOCOL.md     ← независимая проверка прогона
├── monograph/
│   └── MONOGRAPH_CHAPTER_RU.md      ← черновик главы (PLOS-стиль)
├── enriched_example/
│   └── RH_Auto_5000_L64_s5_20261016_122739/   ← готовые P0-файлы
└── report/
    └── Отчёт_обогащение_RH_Sweep_Pro.pdf      ← полный отчёт (23 стр.)
```

## Куда класть в репозитории

Рекомендуемая раскладка (по аналогии с `Vortex_optimization`):

| Каталог комплекта | Куда положить |
|:--|:--|
| `julia/` | рядом с `RH_Sweep_Pro_D.jl` (в каталог кода) |
| `templates/` | `docs/templates/` или рядом с кодом |
| `monograph/` | слить с `Vortex_optimization/monograph/` |
| `enriched_example/…` | прямо в папку прогона в `results/` |
| `report/` | `Vortex_optimization/report/` либо в папку прогона |

## Дефекты исходного кода, закрываемые комплектом

| ID | Дефект | Решение |
|:--|:--|:--|
| D-1 | `sweep_parameter`, `save_sweep_results` не определены → `UndefVarError` | реализации в модуле, сигнатуры совпадают с местами вызова |
| D-2 | `sweep_all_parameters` заявлена в меню, отсутствует | реализация 8×N sweep с инкрементальной записью |
| D-3 | цель ⟨r̃⟩ расходится: 0.3602 (тест) vs 0.3997 (панель/график) | унификация на 0.3602; в шаблонах и словаре уже исправлено |
| D-4 | справка описывает 500 нулей вместо 13 661 | отметить при следующей правке основного файла |
| D-5/D-6/D-7 | χ²-«p-value», мягкий критерий K, прокси-компрессибилити | задокументированы в словаре данных и протоколе верификации |

## Лицензия и цитирование

Комплект распространяется на условиях лицензии репозитория
ab-cloud-research. При использовании ссылайтесь на каталог
`Vortex_optimization` (тест 34) и настоящий комплект
`RH_Sweep_Pro_Enrichment` v1.0.
