# Интеграция RH_Results_Enricher.jl в RH_Sweep_Pro_D.jl

> Модуль обогащения папок результатов · RH·SWEEP PRO v1.0 · редакция 1.0 (2026-10-16)

## 1. Полная интеграция — три строки

**Шаг 1.** В шапке `RH_Sweep_Pro_D.jl`, сразу после блока `using`
и опциональных пакетов (после определения `HAS_PLOTS` / `HAS_JSON`):

```julia
include("RH_Results_Enricher.jl")
```

**Шаг 2.** В конце `_final_run(...)`, непосредственно перед `return Dict(...)`:

```julia
enrich_run(cfg, final_result, all_results, eigs_final, zeta_zeros;
           out_dir = cfg.output_dir)
```

**Шаг 3 (опционально, один раз после прогона)** — GUE-пол метода и
значимость по реализациям:

```julia
gue_floor_multi_report(cfg; n_floor_ens = 20, n_seeds_sig = 5)
```

После этого **каждый** прогон (`run(cfg)`, пресеты, `sweep_top10_pro()` и
`sweep_combined_quick()` — последние два начинают работать благодаря патчам
D-1/D-2) сам дописывает в папку результатов:

| Файл | Уровень | Содержание |
|:--|:--:|:--|
| `README.md` | P0 | TL;DR-таблица, вердикты 11 тестов, состав папки, воспроизведение |
| `SUMMARY.md` | P0 | машинно-читаемая JSON-сводка лучшей точки |
| `DATA_DICTIONARY.md` | P0 | словарь всех колонок metrics.csv и файлов обогащения |
| `config.json` | P0 | снапшот всех 35 полей RHConfig + окружение (Julia/BLAS/ОС) |
| `manifest.sha256` | P0 | SHA-256 всех файлов папки |
| `curves/*.csv` | P1 | R₂(s), K(t), Σ²(L), Δ₃(L), p(s) для AB и ζ |
| `sensitivity/*.csv` | P1 | история sweep, разрезы по параметрам, multi-seed |
| `gue_floor.json` | P1 | статистический нуль метода на данной выборке |

## 2. Ремонт sweep-движка (патчи D-1 / D-2)

В `RH_Sweep_Pro_D.jl` v1.0 функции `sweep_parameter`,
`save_sweep_results` и `sweep_all_parameters` **вызываются, но не
определены** — `sweep_top10_pro()` и `sweep_combined_quick()` падали с
`UndefVarError`. Модуль поставляет реализации с сигнатурами, точно
совпадающими с местами вызова:

```julia
results, best_val, best_score, best_result =
    sweep_parameter(:alpha; range = collect(-4.0:0.5:4.0),
                    base_cfg = preset_auto(5000, verbose = false),
                    verbose = true)

save_sweep_results(all_results, best_params, output_dir)   # как в исходнике

sweep_all_parameters(; n_points = 17)                      # полный 8×17 sweep
```

Каждая точка sweep **инкрементально** дописывается в
`sensitivity/sweep_history.csv` — прерванный прогон не теряет данные
(дисциплина теста 34).

## 3. Обогащение уже существующего прогона (без пересчёта)

Если прогон уже сделан и есть `results.json` / `metrics.csv`, полный
пересчёт не нужен: README, SUMMARY, словарь, config-снапшот и манифест
лежат готовыми в `enriched_example/RH_Auto_5000_L64_s5_20261016_122739/`
поставки — скопируйте их в папку прогона. Кривые и GUE-пол (P1)
считаются быстро из сохранённых спектров:

```julia
include("RH_Sweep_Pro_D.jl")
include("RH_Results_Enricher.jl")

zeta = get_zeta_zeros_safe(5000)
eigs = readdlm("csv/ab_eigs.txt")[:, 1]

export_curves(eigs, zeta; out_dir = "RH_Auto_5000_L64_s5_20261016_122739/curves")
gue_floor_control(64, 5; n_ens = 20, n_zeta = 5000,
                  out_dir = "RH_Auto_5000_L64_s5_20261016_122739")
make_manifest("RH_Auto_5000_L64_s5_20261016_122739")
```

См. также `example_post_run.jl`.

## 4. Требования и гарантии

- **Зависимости:** только Base + DelimitedFiles. JSON.jl опционален
  (без него включается встроенный плоский JSON-писатель).
- **Порядок include:** строго после загрузки `RH_Sweep_Pro_D.jl` —
  модуль использует `RHConfig`, `MetricsResult`,
  `build_hamiltonian_with_config`, `central_eigs_sorted`,
  `compute_all_metrics`, `compute_R2`, `compute_K_empirical`,
  `compute_Sigma2`, `compute_Delta3`, `compute_p_histogram`,
  `get_zeta_zeros_safe`, `N_ZETA_ZEROS_AVAILABLE`, `R_GUE`,
  `preset_auto`, `default_config`.
- **Fail-safe:** отсутствие Plots/JSON деградирует вывод, но не ломает
  прогон; SHA-256 реализован чисто на Julia (верифицирован против
  эталонных векторов FIPS 180-4).
- **Совместимость:** поля `MetricsResult` используются только те, что
  объявлены в RH_Sweep_Pro_D.jl v1.0 (см. struct, строки 4978–5020).

## 5. Известные ограничения

1. `gue_floor_control` строит ансамбль GUE размера ⌊0.3·L²⌋×⌊0.3·L²⌋ —
   при L=64 это 20 диагонализаций матриц 1228×1228 (≈ минуты).
2. `sweep_all_parameters(; n_points=17)` — это 136 диагонализационных
   прогонов; при L=64 планируйте ~1–2 часа, при больших L используйте
   `n_points=8–10` или `preset_quick`-подобные конфигурации.
3. Побайтовая воспроизводимость гарантируется только на той же
   платформе (версия Julia + BLAS) — фиксируйте `config.json`.
