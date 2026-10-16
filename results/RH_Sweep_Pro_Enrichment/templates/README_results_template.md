# Прогон {{RUN_NAME}}

> RH-Sweep PRO · AB-облако ↔ ζ-нули · {{SHORT_DESCRIPTION}}
> Дата: {{DATE}} · Julia {{JULIA_VERSION}} · {{PLATFORM}}

## TL;DR

| Величина | Значение | Комментарий |
|:--|:--|:--|
| Лучший Score | {{SCORE}} / 100 | {{SCORE_MINUS_FLOOR}} выше GUE-пола метода |
| Тесты RMT | {{TESTS_PASSED}}/{{TESTS_TOTAL}} | {{FAILED_TESTS_LIST}} |
| Конфигурация | α = {{ALPHA}}, W = {{W}}, σ = {{SIGMA}} | вихри: {{N_VORTICES}} × {{LAYOUT}} |
| ⟨r⟩ | {{R_MEAN}} | R_GUE = 0.5996 · класс {{R_CLASS}} |
| K corr(GUE) / corr(ζ) | {{K_GUE}} / {{K_ZETA}} | {{N_ZETA}} ζ-нулей · {{N_EIGS}} соб. значений |
| Решётка | L = {{L}} ({{MATRIX_DIM}}) · {{N_SEEDS}} реализаций | N_AB/N_ζ = {{RATIO}} |

**Рекомендация одной строкой:** {{ONE_LINE_RECOMMENDATION}}

## Вердикты (11 тестов)

- [{{X1}}] 1. ⟨r⟩ ≈ R_GUE (|d_GUE| < 0.05)
- [{{X2}}] 2. R₂(s) ближе к GUE, чем к Пуассону
- [{{X3}}] 3. K(t) коррелирует с K(ζ)
- [{{X4}}] 4. Σ²(L) ближе к GUE, чем к Пуассону
- [{{X5}}] 5. Δ₃(L) RMS < 0.5
- [{{X6}}] 6. p(s) RMS < 0.2
- [{{X7}}] 7. χ² Wigner < 0.5
- [{{X8}}] 8. Brody β ≈ 2.0 ± 0.5
- [{{X9}}] 9. Compressibility < 0.3
- [{{X10}}] 10. E(s=1) ≈ 0.171 ± 0.15
- [{{X11}}] 11. ⟨r̃⟩ ≈ 0.3602 ± 0.05

## Что в этой папке

| Путь | Что это |
|:--|:--|
| `plots/` | 01 — 6-панельное сравнение с GUE/Poisson/ζ; 02 — ζ в AB-облаке; 05 — 7 панелей новых метрик |
| `csv/metrics.csv` | строка на конфигурацию: 37 колонок — см. `DATA_DICTIONARY.md` |
| `csv/ab_eigs.txt` | {{N_EIGS}} центральных собственных значений (сырой спектр) |
| `csv/zeta_zeros.txt` | использованные ζ-нули |
| `txt/report.txt` | консольный протокол прогона |
| `json/results.json` | лучшая точка в машинном виде |
| `config.json` | снапшот всех 35 полей RHConfig + окружение |
| `manifest.sha256` | контрольные суммы всех файлов (целостность) |
| `curves/` | кривые метрик CSV — независимый пересчёт без Julia |
| `sensitivity/` | история sweep, разрезы по параметрам, multi-seed значимость |
| `gue_floor.json` | GUE-пол метода на данной выборке |

## Воспроизведение

```bash
julia -e 'include("RH_Sweep_Pro_D.jl");
          cfg = preset_auto({{N_ZETA}});
          cfg.alpha = {{ALPHA}}; cfg.W = {{W}}; cfg.sigma = {{SIGMA}};
          cfg.output_dir = "{{RUN_NAME}}";
          run(cfg)'
```

Сид-конвенция и правила детерминированности — `RUN_PROTOCOL.md`.
Заявление о воспроизводимости: побайтовое совпадение — только на той же
платформе (Julia {{JULIA_VERSION}} + {{BLAS}}).

## Ограничения

{{LIMITATIONS}}
<!-- пример: одиночная точка (не скан) · одна платформа · N_ζ = 5000 из 13 661 ·
     N_v = 6 — нижняя граница рабочего окна · E(s=1) не пройден -->
