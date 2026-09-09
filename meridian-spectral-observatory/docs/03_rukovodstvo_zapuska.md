# 03 · Руководство по запуску: от нуля до первого прогона

> Здесь всё о практической стороне: установка Julia (включая Android/Termux), зависимости, запуск каждого стенда, меню и пресеты, профили конфигурации, типичное время и память.

---

## 1. Установка Julia

### 1.1 Android (Termux) — как у автора

```bash
pkg update && pkg upgrade -y
pkg install -y julia          # если есть в репозитории Termux
# если пакета нет — официальная сборка aarch64:
curl -LO https://julialang-s3.julialang.org/bin/linux/aarch64/1.10/julia-1.10.9-linux-aarch64.tar.gz
tar -xzf julia-1.10.9-linux-aarch64.tar.gz -C $HOME
echo 'export PATH="$HOME/julia-1.10.9/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
julia --version
```

Проверено на Julia 1.12 (в v24.1-SA есть специальный hotfix под fd-модель 1.12). Любая версия ≥ 1.10 подойдёт.

### 1.2 Linux / macOS

```bash
curl -fsSL https://install.julialang.org | sh    # juliaup — официальный установщик
julia --version
```

### 1.3 Windows

Скачайте установщик с [julialang.org/downloads](https://julialang.org/downloads/). Для полноцветной консоли рекомендуется Windows Terminal (MERIDIAN-консоль определяет Windows Terminal по `WT_SESSION` и не глушит цвета).

---

## 2. Зависимости по стендам

| Стенд | Зависимости | Комментарий |
|---|---|---|
| `ab_cloud_v*.jl` (все) | **только stdlib** | LinearAlgebra, Random, SparseArrays, Statistics, Printf, Dates — ничего ставить не нужно |
| `hp_audit_standalone.jl` | **только stdlib** | то же |
| `RH_Unified.jl`, `RH_Unified_v5.jl`, `RH_Sweep_Pro*.jl` | `Plots`, `JSON` | `julia -e 'using Pkg; Pkg.add(["Plots","JSON"])'` |
| `AB_Cloud_Monumental_v6_3*.jl` | stdlib; **опционально** `Arpack`, `Plots` | без Arpack — плотный fallback; без Plots — данные графиков в CSV |
| `test11_honest.py` | Python 3, `numpy`, `mpmath` | `pip install numpy mpmath` |
| `Magic_Alpha_Points_v1.jl` | только stdlib | библиотека |

---

## 3. Запуск стендов — точные команды

### 3.1 SUPERCOMBO `ab_cloud_v23_v2.jl`

```bash
julia -e 'include("ab_cloud_v23_v2.jl")'
```
Появится меню. Полезные пункты:
- `f` — **FAST battery**: пресет L=16, ensemble=100, прогон всех 7 HP-гейтов (~10–20 мин);
- `F` — **FULL battery**: пресет L=56, ensemble=40, α-scan n=30 (часы, «record-grade»);
- пункты меню параметров 16–18: `hp_deep_nulls` (по умолчанию 20), `hp_deep_configs` (10), `hp_alpha_scan`/`hp_alpha_scan_n` (включён, 40);
- меню `h` — HP-гейты H1–H7 по отдельности.

### 3.2 HP·MERIDIAN `hp_audit_standalone.jl`

```bash
julia -e 'include("hp_audit_standalone.jl")'
```
Консоль `meridian>`. Ключевые команды:
- `f` — пресет **FAST: L=72** (72×72 = 5184 узлов → каждый солв — плотная задача 5184×5184), ensemble=100/режим, α-scan n=40; H5-план автоматически ужимается в бюджет ≤ 40 солвов;
- `F` — пресет **FULL: L=56** (3136 узлов), ensemble=40, α-scan n=30;
- `s` (smoke) — пресет **SMOKE: L=20**, ensemble=8, deep 4/4, α-scan n=6, лестница [16,20,24], ζ cap 2000 — валидационный прогон;
- `5` — гейт H5 (REGIME-2×2 шоудаун + α-профиль);
- **`5d` — FOCUS-D (v24.2)**: переключает `hp_regime_mode = :regime_d` и запускает H5 с **всем бюджетом 40 солвов в режиме D** (Nv = L²/36, α = 25/900). Первые 7 сидов — бит-в-бит сиды [D]-блока showdown (offset 30 000);
- `z` — указать путь к файлу ζ-нулей (если `zeros50k.txt` не рядом со скриптом);
- doctor среды, `help`, about — по подсказке в консоли.

**Ctrl-C** прерывает вежливо: завершает текущий солв и выходит; каждые 60 секунд во время длинного LAPACK-вызова печатается строка «alive» — это не зависание, это heartbeat.

### 3.3 RH-линейка

```bash
# единый файл, быстрый тест
julia -e 'include("RH_Unified.jl"); run_quick_test()'
# полный прогон по пресету
julia -e 'include("RH_Unified.jl"); cfg = preset_full(); run(cfg)'
# список пресетов
julia -e 'include("RH_Unified.jl"); list_presets()'

# профессиональный свип (13 661 ζ-нулей)
julia -e 'include("RH_Sweep_Pro.jl"); run_quick_test()'
julia -e 'include("RH_Sweep_Pro.jl"); run_magic_test()'     # все 61 магические α
julia -e 'include("RH_Sweep_Pro.jl"); run_full_analysis()'
julia -e 'include("RH_Sweep_Pro.jl"); cfg = preset_balanced(13661; max_time_minutes=30); run(cfg)'
```

### 3.4 Монументальная батарея

```bash
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all(quick=true)'
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_all()'
julia -e 'include("AB_Cloud_Monumental_v6_3.jl"); AB_Cloud_Monumental.run_only(["V11","V35","V87"])'
```
Результаты: `CSV` (строка на задачу), `JSON` (полные массивы), per-task `PNG` и dashboard `PNG` (при наличии Plots.jl; иначе CSV-данные графиков).

### 3.5 Python-тест

```bash
python3 test11_honest.py --zeros-file zeta_zeros_50k.txt
```

---

## 4. Профиль конфигурации `p_myset.cfg`

Профиль — это «снимок» полей HPConfig, сохранённый из консоли HP·MERIDIAN (одна строка = одно поле `имя = значение`). Основные поля профиля «myset»:

| Группа | Поля |
|---|---|
| Решётка | `hp_L=20`, лестница `hp_L_ladder=[16,20,24]`, `hp_L_weyl=20`, `hp_weyl_grid=60` |
| Ансамбль/динамика | `hp_n_ensemble=8`, `hp_t_max=20`, `hp_dt=0.025`, `hp_h1_configs=2` |
| Сетка потока q | `hp_q_min=0.05`, `hp_q_max=1`, `hp_n_q_grid=21` |
| Арифметика | `hp_primes=[2,3,5,7,11,13]`, `hp_zeta_cap=2000` |
| Null/jitter | `hp_jitter_trials=2`, `hp_pos_jitter=0.35`, `hp_alpha_jitter=0.02` |
| GUE-калибровка | `hp_n_gue_calib=3`, `gue_matrix_size=12000`, `hp_gue_band=0.022` |
| Вердикты | `hp_pass_fraction=0.9`, `hp_regime_mode=showdown` |
| Deepen | `hp_deep_nulls=4`, `hp_deep_configs=4`, `hp_alpha_scan=false`, `hp_alpha_scan_n=6` |
| Воспроизводимость | **`hp_seed=2026`** |
| AB-блок | `ab_t=1`, `ab_center_fraction=0.6`, `ab_alpha_test16=0.5`, `ab_K_smooth_window=3`, `ab_n_realizations=5`, `ab_W=4`, `ab_W_max=1`, `ab_nv_list=[4]`, `ab_q_list=[1,2]` |

Профиль удобен для точного повторения прогона: загрузите его в консоли HP·MERIDIAN (или перенесите значения руками) — и сид 2026 воспроизведёт поток случайных чисел.

---

## 5. Время, память, ожидания

**Арифметика стоимости.** Гамильтониан — L²×L². Плотная диагонализация: время ≈ O((L²)³) = O(L⁶), память ≈ O((L²)²) = O(L⁴) (пик ≈ 2.5·(L²)²·16 байт — с запасом на рабочие массивы LAPACK).

| L | Матрица | Пик памяти (оценка) | Время 1 солва (смартфон) |
|---:|---|---:|---:|
| 16 | 256×256 | ~0.01 ГБ | < 1 с |
| 20 | 400×400 | ~0.015 ГБ | ~ 1 с |
| 56 | 3136×3136 | ~0.37 ГБ | ~ 25 с |
| 64 | 4096×4096 | ~0.6 ГБ | ~ 49 с (замер реального прогона) |
| 72 | 5184×5184 | ~1.0 ГБ | ~ 1.5–2 мин |

Реальные примеры: H5 64×64 (бюджет 40 солвов, 4 режима × 7 конфигов + α-профиль) занял **32 мин 47 с** на смартфоне; 72×72 FAST по оценке ≈ 1 час. Если прогресс-бар «стоит», а строки heartbeat каждые 60 с приходят — идёт обычный длинный LAPACK-вызов.

**Телефон перегревается / рвёт батарейку** — это нормально для O(L⁶); ставьте телефон на вентиляцию, держите зарядку, и берите `:smoke`/`f`-FAST для быстрых итераций.

---

## 6. Цвета и консоль (MERIDIAN DESIGN)

- Цвета включаются только на настоящем TTY; форс-включение: `MERIDIAN_COLOR_FORCE=1 julia -e '...'`; выключение: `MERIDIAN_COLOR=0`.
- Ширина рамок — 62 символа: рассчитана на экран телефона.
- Любая ошибка принтера деградирует в обычный текст — дизайн никогда не ломает прогон.
- На «тупых» терминалах (TERM=dumb), в Windows без Windows Terminal и при пайпинге в файл цвета автоматически отключаются.

---

## 7. Типичные проблемы

| Симптом | Причина | Решение |
|---|---|---|
| «ζ zeros not found — H1/H7 will run WITHOUT the ζ side» | `zeros50k.txt` не найден | положите файл рядом со скриптом, или `z` в консоли, или CLI `zeros=path`, или `export HP_ZEROS=/путь/zeros50k.txt` |
| Julia «package not found: Plots» | RH-линейка требует пакеты | `julia -e 'using Pkg; Pkg.add(["Plots","JSON"])'` |
| «Прогресс-бар не двигается, но alive печатается» | длинный LAPACK-вызов (1 поток, ccall) | ждать; это честный heartbeat, не зависание |
| Ctrl-C убил прогон | вежливое прерывание после текущего солва | просто запустите снова; сиды воспроизводимы |
| Память кончилась на L=72 | пик ~1 ГБ + система | закройте приложения; возьмите L=64/56 |
| В v19 «зависает на тесте 10» в старой консоли | известный дедлок live-tee, исправлен в v19.1 | используйте файл из этого репозитория (v19.1+) |
