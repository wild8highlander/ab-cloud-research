# =====================================================================
# example_post_run.jl — обогащение УЖЕ СУЩЕСТВУЮЩЕГО прогона
# =====================================================================
# Сценарий: прогон RH_Auto_5000_L64_s5_20261016_122739 уже сделан,
# пересчитывать диагонализации не хочется. Скрипт достраивает научный
# слой P1: кривые метрик, GUE-пол, значимость, манифест.
# Файлы P0 (README/SUMMARY/DICTIONARY/config/manifest) уже лежат готовыми
# в enriched_example/ поставки — скопируйте их в папку прогона.
#
# ЗАПУСК:
#   julia --project=. -e 'include("RH_Sweep_Pro_D.jl");
#                         include("RH_Results_Enricher.jl");
#                         include("example_post_run.jl")'
# =====================================================================

RUN_DIR = "RH_Auto_5000_L64_s5_20261016_122739"

# --- 1. Загрузка сохранённого спектра и ζ-нулей ----------------------
eigs_path = joinpath(RUN_DIR, "csv", "ab_eigs.txt")
zeta_path = joinpath(RUN_DIR, "csv", "zeta_zeros.txt")

eigs = vec(readdlm(eigs_path))::Vector{Float64}
zeta = vec(readdlm(zeta_path))::Vector{Float64}
println("[post-run] спектр: $(length(eigs)) соб. значений · ζ-нули: $(length(zeta))")

# --- 2. Кривые метрик (P1): пересчёт без Julia со стороны проверяющего
export_curves(eigs, zeta; out_dir = joinpath(RUN_DIR, "curves"))

# --- 3. GUE-пол метода (P1): статистический нуль на L=64, 5 seed -------
gue_floor_control(64, 5; n_ens = 20, n_zeta = length(zeta), out_dir = RUN_DIR)

# --- 4. Конфигурация прогона → multi-seed значимость -------------------
# Воссоздаём cfg прогона (значения — из results.json / config.json)
cfg = preset_auto(length(zeta), verbose = false)
cfg.L = 64
cfg.n_seeds = 5
cfg.alpha = 1 / π                    # 0.3183098861837907
cfg.W = 2.0
cfg.sigma = 0.5
cfg.min_vortices = 6
cfg.max_vortices = 6
cfg.vortex_layout = :hexagonal
cfg.output_dir = RUN_DIR             # multi_seed.csv ляжет в папку прогона

multi_seed_block(cfg; n_seeds = cfg.n_seeds)

# --- 5. Свежий манифест (после добавления curves/ и gue_floor.json) ----
make_manifest(RUN_DIR)

# --- 6. Итог -----------------------------------------------------------
println("""
[post-run] готово. Папка $RUN_DIR теперь содержит:
  · curves/            — 6 CSV с кривыми метрик (пересчёт без Julia)
  · gue_floor.json     — пол метода; сравнивайте Score минус пол
  · sensitivity/multi_seed.csv — mean±std значимость по реализациям
  · manifest.sha256    — обновлён после всех добавлений
Дополните README.md разделом «Пол метода», когда прогоните шаги 3–4.""")
