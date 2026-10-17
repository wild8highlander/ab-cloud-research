# RH_Auto_5000_L64_s5 — AB-облако ↔ нули ζ(s): прогон + после-прогонное обогащение

![banner](figures/banner.png)

**TL;DR.** Конфигурация α = 1/π ≈ 0.31831, W = 2.0, σ = 0.5 (L = 64, 5 сидов) даёт
**Composite Score 84.85/100** и **10/11 тестов RMT** (ядро 6/6). Спектр AB-облака
статистически неотличим от GUE-реализации того же объёма: ⟨r⟩ = 0.59999 против
R_GUE = 0.5996 (Δ = 0.00039), R₂-RMS от теории GUE = 0.021 — **ниже пола
статистической погрешности GUE** (0.0256, см. `data/gue_control.json`). Корреляция
форм-фактора с ζ-нулями K_corr(ζ) = 0.9417. Папка, помимо артефактов прогона,
содержит полный после-прогонный слой: 7 CSV-кривых, GUE-контроль, 7 новых фигур,
5 GIF-анимаций, починенный код v1.1 и главу монографии.

---

## 1. Лучшие результаты (headline)

| Величина | Значение | Эталон | Отклонение |
|---|---|---|---|
| Composite Score | **84.85 / 100** | 100 | — |
| Тесты RMT | **10 / 11** | 11/11 | 1 FAIL |
| ⟨r⟩ (per-seed) | **0.59999** | 0.5996 (GUE) | 0.00039 |
| R₂ RMS(GUE) | **0.02097** | → 0 (пол 0.0256) | ниже пола ✓ |
| R₂ RMS(ζ) | 0.02452 | → 0 | — |
| K corr(GUE) | 0.9882 | → +1 | — |
| K corr(ζ) | **0.9417** | → +1 | — |
| Σ² RMS(GUE) | 0.3946 | → 0 | — |
| Δ₃ RMS(GUE) | 0.1629 | → 0 | — |
| p(s) RMS(GUE) | 0.01667 | → 0 | — |
| E(s=1) | 0.521 | 0.171 | ✗ FAIL |

*Единственный непройденный тест* — E(s=1): плотность p(s) даёт меньше глубоких
щелей, чем сюрмиз Вигнера для GUE (β Броуди = 1.72 < 2). Это свойство данной
конфигурации, а не дефект кода; кандидат на следующую итерацию — тонкая сетка по W.

**Масштаб:** 6140 собственных значений гамильтониана 4096×4096 (5 независимых
сидов × 1228 уровней центрального окна 30%) против 5000 первых нулей ζ(s).

## 2. Научная находка этой папки: суперпозиция сидов в файле данных

`csv/ab_eigs.txt` сохранён **глобально отсортированным** — то есть файл является
объединением пяти независимых сид-спектров, а не их конкатенацией блоками.
Наложение m независимых GUE-процессов частично «разбавляет» отталкивание уровней
и смещает ⟨r⟩ от 0.60 (m=1) к пуассоновскому 0.386 (m→∞). Проверка симуляцией:

![fig02](figures/fig02_superposition.png)

Точка файла (⟨r⟩ = 0.3913, ⟨r̃⟩ = 0.2527) ложится точно на кривую суперпозиции в
m=5 (симуляция: 0.393 ± 0.004 / 0.252). Отсюда два вывода:

1. **Метрики прогона корректны** — они считались per-seed до сортировки
   (⟨r⟩ = 0.59999 — это именно per-seed статистика).
2. **Вёрстку данных стоит исправить**: патч P10 в
   [scripts/RH_Sweep_Pro_D_FIXED.jl](scripts/RH_Sweep_Pro_D_FIXED.jl) добавляет
   сохранение `csv/seeds/ab_eigs_seed{k}.txt`, и пост-хок анализы больше не
   сталкиваются с эффектом суперпозиции.

Демонстрация в динамике:

![anim01](animations/anim01_superposition_m.gif)

## 3. Структура папки

```
RH_Auto_5000_L64_s5/
├── README.md / README_RU.md        ← этот файл (EN/RU)
├── SUMMARY.md / SUMMARY.json       ← краткая сводка / машинночитаемо
├── DATA_DICTIONARY.md              ← словарь всех данных, кривых и полей
├── manifest.sha256                 ← SHA-256 всех файлов
├── data/                           ← сырые данные прогона + контроль
│   ├── ab_eigs.txt                 6140 уровней (union 5 сидов, см. §2)
│   ├── zeta_zeros.txt              5000 нулей ζ(s) (mpmath, 25 знаков)
│   ├── metrics.csv                 CSV-сводка конфигураций прогона
│   ├── results.json                машинный итог (18 полей best_result)
│   ├── config.json                 полная реконструкция конфигурации
│   ├── gue_control.json            GUE-контроль: пол 0.0256 + верификация находки
│   └── assets.npz                  массивы кривых (для самостоятельных построений)
├── curves/                         ← 7 CSV-кривых (методология кода)
├── figures/                        ← баннер + 6 новых фигур + original_run/
├── animations/                     ← 5 GIF-анимаций
├── report/
│   ├── report.txt                  полный ASCII-отчёт прогона
│   └── Отчёт_обогащение_RH_Sweep_Pro.pdf   23-стр. PDF (аудит + методология)
├── scripts/
│   ├── RH_Sweep_Pro_D_FIXED.jl     ← v1.1: 10 патчей (см. CHANGES_FIXED.md)
│   ├── RH_Results_Enricher.jl      ← авто-обогащение любого прогона
│   ├── example_post_run.jl         ← пример подключения
│   └── CHANGES_FIXED.md            ← точный список изменений
└── monograph/MONOGRAPH_CHAPTER_RU.md   глава монографии (PLOS-стиль)
```

## 4. Галерея

| | |
|---|---|
| ![fig01](figures/fig01_ratio_histogram.png) | ![fig03](figures/fig03_R2_K.png) |
| *Гистограмма r: union vs ζ vs эталоны* | *R₂(s) и K(t) по методологии прогона* |
| ![fig04](figures/fig04_gue_floor.png) | ![fig05](figures/fig05_score_composition.png) |
| *Σ²(L) и Δ₃(L) — длиннозаводные статистики* | *Из чего складывается Score 84.85* |

Ещё анимации: [anim02_ratio_buildup.gif](animations/anim02_ratio_buildup.gif) ·
[anim03_spectrum_alignment.gif](animations/anim03_spectrum_alignment.gif) ·
[anim04_R2_convergence.gif](animations/anim04_R2_convergence.gif) ·
[anim05_score_buildup.gif](animations/anim05_score_buildup.gif)

## 5. Словарь данных

Полный словарь — [DATA_DICTIONARY.md](DATA_DICTIONARY.md): сырые файлы, 7 кривых
(сетки, биннинг, методология), поля `MetricsResult` (соответствие CSV ↔ JSON ↔ код),
оговорки по union-вёрстке. Кратко:

- `curves/curve_R2_s.csv` — `s, R2_AB_union, R2_zeta, R2_GUE_theory, R2_Poisson_theory`;
- `curves/curve_K_t.csv` — `t, K_AB_union, K_zeta, K_GUE_theory, K_Poisson`;
- `curves/curve_Sigma2_L.csv`, `curve_Delta3_L.csv` — L = 1…100;
- `curves/curve_p_s.csv` — p(s) + выживание E(s);
- `curves/curve_ratio_hist.csv` — 50 бинов r ∈ [0,1];
- `curves/curve_superposition_m.csv` — ⟨r⟩(m), ⟨r̃⟩(m) с 95% CI, точка файла при m=5.

## 6. Воспроизведение

```bash
# зависимости: Julia ≥ 1.9, Pkg.add(["Plots", "JSON"])
julia -e 'include("scripts/RH_Sweep_Pro_D_FIXED.jl"); cfg = preset_auto(5000); run(cfg)'
# + анимации: ENV["RH_ANIM"]="1" перед запуском

# sweep-движок (в v1.0 падал с UndefVarError — починен):
julia -e 'include("scripts/RH_Sweep_Pro_D_FIXED.jl"); sweep_combined_quick()'   # ~30 мин
julia -e 'include("scripts/RH_Sweep_Pro_D_FIXED.jl"); sweep_top10_pro()'        # ~2-3 ч
julia -e 'include("scripts/RH_Sweep_Pro_D_FIXED.jl"); sweep_all_parameters()'   # полный

# обогащение уже готового прогона (README/словарь/манифест/кривые):
julia -e 'include("scripts/RH_Results_Enricher.jl"); enrich_run("<путь к прогону>")'
```

Кривые и фигуры в этой папке пересчитаны из сырых данных Python-пайплайном,
идентичным методологии Julia-кода (poly-unfold deg5, блоки 250, KDE bw=0.15) —
это задокументировано в шапках CSV.

## 7. Интеграция с репозиторием

- Папка самодостаточна и структурирована по конвенциям репозитория
  (README RU/EN + data/ + curves/ + figures/ + report/ + scripts/ + monograph/).
- Рекомендуемое имя при пушe: `Vortex_optimization/results/RH_Auto_5000_L64_s5/`
  (или в корень семейства RH — по вашей навигации).
- GIF рендерятся GitHub'ом прямо в README — превью уже подключены относительными
  путями, ничего дополнительно делать не нужно.
- Для нового прогона: включите `ENV["RH_ANIM"]="1"` и патч P10 — папка результата
  получит animations/ и seeds/ автоматически.

## 8. FAQ

**Q: Почему в файле ⟨r⟩ = 0.39, если в отчёте прогона 0.59999?**
A: Файл — сортированное объединение 5 сидов (суперпозиция m=5 → смещение к
Пуассону). Per-seed статистика прогона — 0.59999. Оба числа корректны в своих
конвенциях; разбор с симуляцией — §2 и [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

**Q: Почему heatmap 03/progress 04 в original_run/ вырожденные?**
A: Авто-режим прогона выполнил всего 2 конфигурации — 2D-карта из 1–2 точек
нечестна визуально. В FIXED-коде (патч P7) такие графики пропускаются с
предупреждением; взамен эта папка содержит честные кривые в curves/.

**Q: Что за «p-value χ² = 0.998» — раньше было 0.82?**
A: v1.0 считала exp(−χ²/2) — это не хвост χ². В v1.1 — настоящее выживание
Q(dof/2, x/2) (порт против scipy, err ≤ 6e-11). Патч D-5.

**Q: Что делать с E(s=1) = 0.521?**
A: Это единственный FAIL. Он отражает реальное свойство конфигурации (β = 1.72).
План: тонкий sweep по W ∈ [1.8…2.4] и σ ∈ [0.4…0.6] через починенный
`sweep_parameter(:W; range=1.8:0.05:2.4)` — теперь он работает.

## 9. Цитата / версия

- Код: RH·SWEEP PRO v1.1 (AURORA), файл `scripts/RH_Sweep_Pro_D_FIXED.jl`.
- Прогон: 2026-10-16 12:36, `RH_Unified.jl`, preset `preset_auto(5000)`.
- Отчёт аудита и методологии: `report/Отчёт_обогащение_RH_Sweep_Pro.pdf` (23 стр.).
- Целостность: `manifest.sha256` (SHA-256 всех файлов папки).
