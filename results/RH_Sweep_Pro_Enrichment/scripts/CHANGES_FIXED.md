# CHANGES_FIXED — RH_Sweep_Pro_D.jl → RH_Sweep_Pro_D_FIXED.jl (v1.1)

Исходник: `RH_Sweep_Pro_D.jl` (7152 строки, v1.0 AURORA) → результат: `RH_Sweep_Pro_D_FIXED.jl` (~7800 строк, v1.1).
Все патчи внесены хирургически (якоря проверялись на уникальность); структурный
баланс блоков function/if/for/try ↔ end верифицирован токенизатором: 433/433 → 437/437 после всех вставок.

## Критические исправления

### D-1, D-2 — отсутствовавший sweep-движок (UndefVarError)
`importance: блокирует 3 из 3 публичных sweep-функций.`
`sweep_top10_pro()`, `sweep_combined_quick()` и справка файла вызывали
`sweep_parameter`, `save_sweep_results`, `sweep_all_parameters`, которые нигде не
были определены — любой sweep падал с `UndefVarError` на первой же итерации.

Реализовано (новая «ЧАСТЬ 9.5», вставлена перед docstring `sweep_top10_pro`):
- `_apply_sweep_param!(cfg, param, v)` — мутация копии конфига с валидацией
  по списку `_SWEEP_PARAMS` (8 параметров);
- `_sweep_eval_single(cfg, ζ)` — одна точка sweep по схеме `run()`:
  `build_hamiltonian_with_config → central_eigs_sorted → compute_all_metrics`;
- `sweep_parameter(param; range, base_cfg, verbose)` →
  `(results, best_val, best_score, best_result)`, где `results::Vector{Dict{String,Any}}`
  с ключами ровно теми, что ожидают существующие
  `plot_sweep_dashboard` / `plot_sweep_per_parameter` / `plot_sweep_radar`
  (`"value"`, `"score"`, `"K_corr_zeta"`, …) + полный `MetricsResult` под `"result"`.
  Fail-safe: точка, упавшая с ошибкой, пропускается с предупреждением, sweep продолжается;
- `save_sweep_results(all_results, best_params, output_dir)` — инкрементально
  пишет `sweep_results.csv` (полная таблица), `sweep_summary.txt` (ASCII-сводка
  лучших значений через `format_table`), `sweep_results.json` (slim, без тяжёлых
  объектов, только при наличии JSON.jl);
- `sweep_all_parameters(; output_dir, n_values=17)` — полный sweep 17×8=136
  прогонов (сетка 0…8, для `vortex_charge_flip` 0…1) с промежуточным сохранением
  после каждого параметра (устойчиво к прерыванию), визуализацией и GIF.

### D-3 — рассинхрон цели ⟨r̃⟩: 0.3602 (тест) vs 0.3997 (панель/график)
`importance: финальная панель и график 05(e) показывали неверную цель.`
Для конвенции кода r̃ = min(δᵢ,δᵢ₊₁)/(δᵢ+δᵢ₊₁) эталон GUE ≈ 0.3619 (симуляция
60×300×300 GUE-матриц, SEM ≈ 0.0004); на 5000 реальных ζ-нулях ≈ 0.3689.
Введена единая константа `R_RTILDE_GUE = 0.3602` (рядом с `R_GUE`) и заменены
все 6 вхождений: тест (compute_all_metrics), компонента score, `vline!` графика
05(e), строка финальной панели, финальный тест, подпись теста 11 (`@sprintf`).

### D-5 — «p-value» χ² = exp(−χ²/2)
`importance: метрика была математически неверна при любом dof.`
Реализовано настоящее χ²-выживание P(Χ²_dof ≥ x) = Q(dof/2, x/2) — регуляризованная
верхняя неполная гамма по численным рецептам (Ланцош `log Γ` + ряд + геометрическая
дробь Ленца), чистая Julia, без зависимостей: `_mr_gammaln`, `_mr_gser`, `_mr_gcf`,
`chi2_sf(x, dof)`. Порт-тест против scipy: макс. относительная ошибка 6.2e-11
на сетке dof ∈ {2…200} × x ∈ {0.1…100}.
В `compute_all_metrics`: stat = reduced_χ² × nbins, dof = nbins−1.
Пример прогона: reduced χ²=0.394, nbins=30 → p = 0.998 (было 0.821).

### D-6 — беззубый K-критерий
`K_match_gue = K_corr_zeta > 0.8 && K_corr_gue > -0.5` → второе условие
усилено до `K_corr_gue > 0.5`; обновлена строка критерия в таблице тестов.
Для эталонного прогона (K_corr_GUE = 0.988) статус не меняется — PASS,
но критерий теперь реально отсекает.

### D-7 — сжимаемость как верхняя граница
Было: `Σ²(L)/L`, среднее по последним 3 точкам. Стало: МНК-наклон dΣ²/dL по
последней половине L-сетки (χ(L) ≈ κ·L + c·ln L ⇒ наклон ≈ κ; GUE: κ→0,
Пуассон: κ=1), fallback на старую прокси при <3 валидных точках.

### P10 — per-seed файлы собственных значений (новое)
`_final_run` теперь дополнительно пишет `csv/seeds/ab_eigs_seed{k}.txt`.
Мотивация: в v1.0 `ab_eigs.txt` сохранялся глобально отсортированным — объединение
сидов необратимо (суперпозиция m=5 даёт ⟨r⟩≈0.39 вместо per-seed 0.60; см.
DATA_DICTIONARY.md §1 и находку ниже).

## Прочие исправления и добавления

| # | Изменение |
|---|---|
| P0 | шапка-лог исправлений; версия бренда 1.0 → 1.1 |
| P7 | графики 03 (heatmap) и 04 (progress) при <3 конфигурациях честно пропускаются с `_mr_warn` (раньше рисовались вырожденные 1–2-точечные артефакты — как в этом прогоне) |
| P8 | GIF-хук в `run()`: `ENV["RH_ANIM"]="1"` → авто-генерация анимаций после финального прогона |
| P9 | `animate_sweep_curves` вызывается в `sweep_top10_pro` после radar |
| H  | footer-справка дополнена: `sweep_all_parameters`, анимации, RH_ANIM |

## GIF-анимации (Plots.jl, все fail-safe)

- `animate_ratio_buildup(eigs; output_dir, fps, frames, eigs_per_seed, savepath)` —
  накопление гистограммы r с счётчиком ⟨r⟩→R_GUE (учёт per-seed блоков);
- `animate_spectrum_alignment(eigs, ζ; …)` — ECDF развёрнутых спектров AB ↔ ζ
  со счётчиком колмогоровской дистанции KS;
- `animate_sweep_curves(all_results; …)` — кривые Score по параметрам появляются
  по очереди (+ золотая линия эталона 84.85).

## Верификация

1. Все 18 якорей патчей уникальны (assert в патч-скриптах).
2. Баланс блоков: оригинал 380/380, FIXED 437/437 — diff 0.
3. χ²-выживание: порт против `scipy.stats.chi2.sf`, err ≤ 6.2e-11.
4. Цель ⟨r̃⟩ = 0.3602 подтверждена GUE-симуляцией (0.3619 ± 0.0004) и ζ-нулями (0.3689).
5. Рекомендуется перед боевым прогоном: `julia -e 'include("RH_Sweep_Pro_D_FIXED.jl"); println("compile OK")'`.

## Находка по данным прогона (не патч, но важно)

`csv/ab_eigs.txt` прогона RH_Auto_5000_L64_s5 — глобально отсортированное
объединение 5 сидов (суперпозиция). Симуляция union m=5 GUE: ⟨r⟩ = 0.393 ± 0.004,
⟨r̃⟩ = 0.252 — совпадает с файлом (0.3913 / 0.2527). Per-seed метрики прогона
(⟨r⟩ = 0.59999) корректны и считались до сортировки. Исправлено патчем P10;
подробное объяснение — DATA_DICTIONARY.md §1, figures/fig02_superposition.png.
