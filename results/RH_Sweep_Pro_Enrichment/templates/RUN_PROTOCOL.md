# Протокол прогона RH-Sweep PRO (Run Protocol)

> Заполняется перед каждым прогоном, результаты которого пойдут в
> репозиторий. Основа — сид-дисциплина теста 34 (побайтовая
> детерминированность на фиксированной платформе).
> Редакция 1.0 · 2026-10-16

## 1. Окружение (фиксируется в config.json автоматически)

| Поле | Значение | Где взять |
|:--|:--|:--|
| Julia | {{JULIA_VERSION}} | `VERSION` |
| BLAS/LAPACK | {{BLAS_CONFIG}} | `LinearAlgebra.BLAS.get_config()` |
| Потоки | {{THREADS}} | `Threads.nthreads()`, `Sys.CPU_THREADS` |
| ОС / ядро | {{OS}} | `Sys.KERNEL`, `Sys.iswindows()` |
| Код | {{CODE_HASH}} | хеш коммита RH_Sweep_Pro_D.jl + Enricher |

Побайтовое совпадение спектров между разными платформами НЕ
гарантируется ( Floating-point BLAS ); сопоставимость — в пределах
платформы и версии BLAS.

## 2. Сид-конвенция (перенята из теста 34)

| RNG | Сид | Область |
|:--|:--|:--|
| размещение вихрей | `base + 3500` | общий для всех реализаций конфигурации |
| он-сайт разладка / джиттер | `base + 3500 + k` | по реализации k |
| GUE-контроль (пол метода) | `963500` | gue_floor_control |
| базовый сид | `96` | конвенция сьюты |

В текущем RH_Sweep_Pro_D.jl один `MersenneTwister(seed)` обслуживает все
потоки; для побайтовой воспроизводимости рекомендуется развести потоки
по таблице выше (см. отчёт, гл. 7.3) и зафиксировать фактические сиды
здесь:

| Поток | Фактический сид |
|:--|:--|
| вихри | {{SEED_VORTEX}} |
| беспорядок | {{SEED_DISORDER}} |
| джиттер α/W/σ | {{SEED_JITTER}} |

## 3. Параметры прогона

| Блок | Поля | Значение |
|:--|:--|:--|
| Решётка | L, n_seeds, n_zeta_zeros | {{L}} / {{N_SEEDS}} / {{N_ZETA}} |
| Физика | alpha, W, sigma, t_hop | {{ALPHA}} / {{W}} / {{SIGMA}} / {{T_HOP}} |
| Вихри | min/max_vortices, layout | {{NV_RANGE}} / {{LAYOUT}} |
| Jitter | alpha/W/sigma/pos/flip | {{JITTER_ALL}} |
| Sweep | use_alpha_sweep, границы | {{SWEEP}} |
| Режим | optimize, fine_grid | {{OPTIMIZE}} |

Проверка объёма выборки: `eigs_per_seed = ⌊0.3·L²⌋ = {{EPS}}`,
`N_AB = n_seeds·eigs_per_seed = {{N_AB}}`, кратность 250:
`⌊N_AB/250⌋ = {{NBLOCKS}}` полных блоков (цель ≥ 20 для
K corr(ζ) ≥ 0.9).

## 4. Порядок запуска

```bash
# 0) окружение зафиксировано, сиды внесены выше
julia -e 'include("RH_Sweep_Pro_D.jl"); include("RH_Results_Enricher.jl");
          cfg = preset_auto({{N_ZETA}});
          # ... правки cfg по таблице п.3 ...
          run(cfg);
          gue_floor_multi_report(cfg; n_floor_ens = 20, n_seeds_sig = 5)'
```

1. После прогона проверить наличие: `README.md`, `SUMMARY.md`,
   `DATA_DICTIONARY.md`, `config.json`, `manifest.sha256`.
2. Прогнать P1, если не сделан внутри: `export_curves`,
   `gue_floor_control`, `multi_seed_block`.
3. Обновить манифест последним: `make_manifest(out_dir)`.

## 5. Чек-лист перед пушем

- [ ] README.md заполнен (TL;DR, вердикты, ограничения)
- [ ] config.json соответствует фактическим полям прогона
- [ ] manifest.sha256 пересчитан ПОСЛЕ всех правок
- [ ] кривые/значимость/пол присутствуют или помечены «P1 — в работе»
- [ ] в текстах нет абсолютных путей рабочей машины
- [ ] утверждения сформулированы относительно GUE-пола
- [ ] ограничения прогона перечислены явно
