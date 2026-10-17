# DATA_DICTIONARY — RH_Auto_5000_L64_s5

Словарь всех файлов данных этой папки: исходные артефакты прогона, после-прогонные кривые и контрольные файлы. Все CSV содержат строку-заголовок с `#`-комментарием (методология) и первую строку имён колонок.

---

## 1. Исходные данные прогона (`data/`)

### `data/metrics.csv` — сводка конфигураций прогона
Формат из кода (`save_csv_report`). Заголовок из трёх `#`-строк (инструмент, дата).
В этом прогоне сохранены 2 строки (лучшие конфигурации); колонки соответствуют
полям `MetricsResult` (см. §4). Ограничение: новые метрики v1.0 (χ², β, κ, E(s=1), ⟨r̃⟩)
в момент прогона в CSV не писались — они в логе `report/report.txt` и восстановлены
частично в `figures/fig05_score_composition.png`.

### `data/ab_eigs.txt` — 6140 собственных значений AB-облака
- 5 сидов × 1228 уровней (окно 0.3, L=64).
- ⚠ **КЛЮЧЕВОЕ СВОЙСТВО ВЁРСТКИ:** файл сохранён **глобально отсортированным**.
  Это НЕ «5 блоков подряд»: это объединение (суперпозиция) пяти независимых
  сид-спектров. Последствия:
  - per-seed статистики (⟨r⟩ = 0.59999, K_corr(ζ) = 0.9417 и т.д.) считались в
    памяти прогона ДО сортировки — они в `results.json` и `report/report.txt`;
  - пост-хок статистики по файлу показывают суперпозицию m=5: ⟨r⟩ = 0.3913,
    ⟨r̃⟩ = 0.2527 — это ожидаемое смещение к Пуассону при наложении спектров,
    а НЕ ошибка данных. Проверка: симуляция union m=5 GUE-спектров даёт
    ⟨r⟩ = 0.393 ± 0.004 (см. `curves/curve_superposition_m.csv`,
    `figures/fig02_superposition.png`, `animations/anim01_superposition_m.gif`);
  - все кривые в `curves/`, посчитанные по файлу, помечены `_union` и
    документированы с этой оговоркой;
  - исправление на будущее: `scripts/RH_Sweep_Pro_D_FIXED.jl` (патч P10) пишет
    `csv/seeds/ab_eigs_seed{k}.txt` для каждого сида.

### `data/zeta_zeros.txt` — 5000 нулей дзета-функции
Первые 5000 верифицированных нулей ζ(s) (mpmath.zetazero, 25 знаков), t ∈ [14.134725, 4843.7]. Одна последовательность (не суперпозиция).

### `data/results.json` — машинный итог прогона
Ключи `best_result` (18 полей): `alpha`, `W`, `sigma`, `L`, `n_eigs`, `r_mean`,
`r_class`, `composite_score`, `tests_passed/total`, `R2_rms_GUE`, `R2_rms_zeta`,
`K_corr_GUE`, `K_corr_zeta`, `Sigma2_rms_GUE`, `Delta3_rms_GUE`, `p_rms_GUE`,
`label`; `best_params` (α/W/σ); `metadata` (инструмент, метка времени, размер
пула ζ-нулей 13661).

### `data/config.json` — полная реконструкция конфигурации
Все параметры прогона, включая восстановленные из дефолтов кода (помечены
`reconstructed: true`): вихри (гекс, 6), jitter (выкл), окно 0.3, сетки биннинга.

### `data/gue_control.json` — GUE-контроль (метод Т34)
Пол статистической погрешности: RMS отклонения двух половин GUE-симуляции
(24 матрицы 300×300, расщепление 12+12) друг от друга, обработанных той же
методологией, что и данные (poly-unfold deg5, блоки 250, KDE bw=0.15).
- `floor_R2_rms_GUE_vs_GUE` = 0.025557 — пол;
- `run_R2_rms_AB_vs_GUE_perseed` = 0.020975 — значение прогона **ниже пола**;
- вердикт + все пересчитанные по файлу-union величины (с оговоркой m=5);
- блок `superposition_check` — численная верификация находки о вёрстке.

### `data/assets.npz` — сжатый бандл массивов
numpy-архив всех кривых и выборок (использовался генератором фигур/анимаций;
пригоден для самостоятельных построений без пересчёта).

---

## 2. Кривые (`curves/`, пересчёт post-run по методологии кода)

Общая методология: развёртка `polynomial_unfold(deg=5)` (идентична коду), блочное
усреднение по 250 уровней (`K_BLOCK_SIZE`), сравнение с аналитическими эталонами
кода: `R2_GUE_theory(s) = 1−(sin πs/πs)²`, `K_GUE_theory(t) = min(t,1)`,
`Σ²_GUE = (1/π²)·ln L + 1/(8π²)`, Пуассон: R₂=1, K=1, Σ²=L, Δ₃=L/15.
Колонки `*_AB_union` — по файлу-union (оговорка m=5, см. §1), `*_zeta` — по ζ-нулям.

| Файл | Колонки | Сетка |
|---|---|---|
| `curve_R2_s.csv` | `s, R2_AB_union, R2_zeta, R2_GUE_theory, R2_Poisson_theory` | s = 0…5, шаг 0.05, KDE bw=0.15 |
| `curve_K_t.csv` | `t, K_AB_union, K_zeta, K_GUE_theory, K_Poisson` | t = 0…2, шаг 0.02, сглаж. 5, ramp<0.5 защищён |
| `curve_Sigma2_L.csv` | `L, Sigma2_AB_union, Sigma2_zeta, Sigma2_GUE_theory_kak_v_kode, Sigma2_Poisson` | L = 1…100 |
| `curve_Delta3_L.csv` | `L, Delta3_AB_union, Delta3_zeta` | L = 1…100, МНК-оценка как в коде |
| `curve_p_s.csv` | `s, p_AB_union, p_GUE_wigner_surmise, p_Poisson, E_s_AB_union` | 30 бинов, s ∈ [0,4] |
| `curve_ratio_hist.csv` | `r_center, density_AB_union, density_zeta` | 50 бинов r ∈ [0,1] |
| `curve_superposition_m.csv` | `m, r_mean, r_lo95, r_hi95, rtilde_mean, rtilde_lo95, rtilde_hi95, file_AB_m5_r, file_AB_m5_rtilde` | m = 1…10, 8 реализаций, GUE 600×600 |

---

## 3. Фигуры и анимации

### `figures/` (новые, dpi 150)
| Файл | Что показывает |
|---|---|
| `banner.png` | баннер папки с ключевыми числами прогона |
| `fig01_ratio_histogram.png` | гистограмма r: файл-union vs ζ-нули vs эталоны; аннотации per-seed 0.5999 и union 0.3913 |
| `fig02_superposition.png` | **научная находка**: ⟨r⟩(m) и ⟨r̃⟩(m) при суперпозиции m спектров; точка файла ложится на m=5 |
| `fig03_R2_K.png` | R₂(s) и K(t): данные vs теории |
| `fig04_gue_floor.png` | Σ²(L) и Δ₃(L) в log-log с эталонами |
| `fig05_score_composition.png` | вклад 12 компонент в Composite Score 84.85 (7 точных из results.json + 3 из лога + 1 остаток) |
| `fig06_tests_summary.png` | сводка 11 тестов: 10 ✓ / 1 ✗ |
| `original_run/` | 5 оригинальных PNG прогона (01–05) без изменений |

### `animations/` (GIF, 990×594)
| Файл | Содержание |
|---|---|
| `anim01_superposition_m.gif` | гистограмма r при наращивании union m=1→5: смещение 0.60 → 0.39 |
| `anim02_ratio_buildup.gif` | накопление гистограммы r по файлу, счётчик ⟨r⟩(N) |
| `anim03_spectrum_alignment.gif` | ECDF AB ↔ ζ-нули с счётчиком колмогоровской дистанции |
| `anim04_R2_convergence.gif` | R₂(s) накапливается по 25 блокам, счётчик RMS vs GUE |
| `anim05_score_buildup.gif` | сборка Composite Score по компонентам до 84.85 |

---

## 4. Поля MetricsResult (соответствие CSV ↔ JSON ↔ код)

| Поле | Смысл | Эталон |
|---|---|---|
| `r_mean` / `r_std_ab` | ⟨r⟩ = ⟨min/max⟩ отношений соседних спейсингов (per-seed) | R_GUE = 0.5996 |
| `r_class` | ближайший ансамбль (GUE/GOE/GSE/Poisson) | — |
| `d_GUE…d_Poisson` | |⟨r⟩ − R_*| | → 0 |
| `R2_rms_GUE/Poisson/zeta` | RMS R₂(s) против теории/ζ | GUE → 0 |
| `K_corr_GUE/zeta` | корреляция K(t) с эталоном | → +1 |
| `Sigma2_rms_GUE/Poisson` | RMS Σ²(L) | GUE → 0 |
| `Delta3_rms_GUE` | RMS Δ₃(L) | → 0 |
| `p_rms_GUE` | RMS p(s) vs сюрмиз Вигнера | → 0 |
| `chi2_wigner` | χ² p(s) vs Вигнер (нормированное) | < 0.5 |
| `chi2_pvalue` | **v1.1:** настоящее выживание Q(dof/2, x/2); v1.0: exp(−χ²/2) | → 1 |
| `brody_beta` | параметр Броуди (log-log регрессия) | 2.0 (GUE) |
| `spectral_compressibility` | **v1.1:** МНК-наклон dΣ²/dL; v1.0: Σ²(L)/L | → 0 (GUE) |
| `gap_prob_E1` | E(s=1) — доля щелей ≥ 1 | 0.171 |
| `r_tilde_mean` | ⟨r̃⟩ = ⟨min/(a+b)⟩ | R_RTILDE_GUE = 0.3602 |
| `level_number_dev` | ⟨δ²ₙ⟩ отклонение номеров уровней | → 0 |
| `symmetry_parameter` | S = ⟨r⟩/(1−⟨r⟩) | 1.496 (GUE) |
| `composite_score` | 12 компонент, 0–100 (веса в коде) | → 100 |
| `tests_passed/total` | 11 тестов | 11/11 |

## 5. Названия, которые не стоит менять

`ab_eigs.txt`, `zeta_zeros.txt`, `metrics.csv`, `results.json` — читаются
`RH_Results_Enricher.jl` и пост-процессингом; при переименовании обновите
`example_post_run.jl`.
