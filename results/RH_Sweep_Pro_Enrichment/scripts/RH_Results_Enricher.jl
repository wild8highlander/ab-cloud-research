# =====================================================================
# RH_Results_Enricher.jl — МОДУЛЬ ОБОГАЩЕНИЯ ПАПОК РЕЗУЛЬТАТОВ
# =====================================================================
# Компаньон к RH_Sweep_Pro_D.jl (RH·SWEEP PRO v1.0).
#
# ЧТО ДЕЛАЕТ:
#   1. ДОСТАВЛЯЕТ НЕДОСТАЮЩИЕ ФУНКЦИИ SWEEP-ДВИЖКА:
#        sweep_parameter, save_sweep_results, sweep_all_parameters
#      (в RH_Sweep_Pro_D.jl они вызываются, но не определены —
#       sweep_top10_pro() / sweep_combined_quick() падали с UndefVarError).
#   2. ПИШЕТ НАУЧНЫЙ СЛОЙ ПАПКИ ПРОГОНА (уровень P0):
#        README.md · SUMMARY.md · DATA_DICTIONARY.md · config.json ·
#        manifest.sha256
#   3. УРОВЕНЬ P1: кривые метрик (curves/*.csv), GUE-пол метода
#      (gue_floor.json), значимость по реализациям (multi_seed.csv).
#
# ЗАВИСИМОСТИ: только Base + DelimitedFiles (уже подключён в основном
#   файле). JSON.jl опционален. SHA-256 реализован чисто на Julia.
# ВСЁ fail-safe: отсутствие пакетов деградирует вывод, но не ломает прогон.
#
# ИНТЕГРАЦИЯ (3 строки) — см. INTEGRATION.md:
#   include("RH_Results_Enricher.jl")                        # после using-блока
#   enrich_run(cfg, final_result, all_results, eigs, zeta;
#              out_dir = cfg.output_dir)                     # в конце _final_run
#   gue_floor_multi_report(cfg; n_floor_ens = 20, n_seeds_sig = 5)  # опционально
#
# ТРЕБУЕТ, чтобы include выполнялся ПОСЛЕ загрузки RH_Sweep_Pro_D.jl
# (используются RHConfig, MetricsResult, build_hamiltonian_with_config,
#  central_eigs_sorted, compute_all_metrics, compute_R2, compute_K_empirical,
#  compute_Sigma2, compute_Delta3, compute_p_histogram, R_GUE, ZETA_ZEROS).
# =====================================================================

# ---------------------------------------------------------------------
# СЛУЖЕБНОЕ: JSON, форматирование, окружение
# ---------------------------------------------------------------------

const _ENR_JSON = Ref(false)
try
    @eval using JSON
    _ENR_JSON[] = true
catch
end

_enr_f(x::AbstractFloat; d::Int = 6) = string(round(Float64(x), digits = d))
_enr_f(x::Any; d::Int = 6) = string(x)

"""Простой JSON-писатель для плоских Dict{String,Any} и одного уровня вложенности."""
function _enr_json(data::Dict; indent::Int = 0)
    if _ENR_JSON[]
        return JSON.json(data)
    end
    function esc(s::String)
        return "\"" * replace(replace(s, "\\" => "\\\\"), "\"" => "\\\"") * "\""
    end
    function val(v)
        if v isa Dict
            inner = join(["$(esc(string(k))) : $(val(v[k]))" for k in keys(v)], ", ")
            return "{" * inner * "}"
        elseif v isa AbstractFloat || v isa Real
            return string(v)
        elseif v isa Bool
            return v ? "true" : "false"
        else
            return esc(string(v))
        end
    end
    inner = join(["$(esc(string(k))) : $(val(data[k]))" for k in keys(data)], ",\n")
    return "{\n" * inner * "\n}"
end

"""Строка окружения: Julia, BLAS, потоки, ОС."""
function _enr_env_info()
    try
        blas = LinearAlgebra.BLAS.get_config()
        return "julia $(VERSION) · $(blas) · threads=$(Threads.nthreads()) · " *
               "$(Sys.CPU_THREADS) CPU · $(Sys.KERNEL)"
    catch
        return "julia $(VERSION) · $(Sys.KERNEL)"
    end
end

# ---------------------------------------------------------------------
# ЧИСТАЯ РЕАЛИЗАЦИЯ SHA-256 (без зависимостей)
# ---------------------------------------------------------------------

const _SHA_K = UInt32[
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1,
    0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786,
    0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
    0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85, 0xa2bfe8a1, 0xa81a664b,
    0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a,
    0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

function _sha256(data::Vector{UInt8})
    bitlen = UInt64(length(data)) * 8
    msg = copy(data)
    push!(msg, 0x80)
    while length(msg) % 64 != 56
        push!(msg, 0x00)
    end
    for sh in (56, 48, 40, 32, 24, 16, 8, 0)   # big-endian length
        push!(msg, UInt8((bitlen >> sh) & 0xff))
    end
    h = UInt32[0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
               0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
    n = length(msg) ÷ 64
    for block in 1:n
        w = Vector{UInt32}(undef, 64)
        base = (block - 1) * 64
        for t in 1:16
            o = base + 4 * (t - 1)
            w[t] = UInt32(msg[o+1]) << 24 | UInt32(msg[o+2]) << 16 |
                   UInt32(msg[o+3]) << 8 | UInt32(msg[o+4])
        end
        for t in 17:64
            s0 = _enr_rotr(w[t-15], 7) ⊻ _enr_rotr(w[t-15], 18) ⊻ (w[t-15] >> 3)
            s1 = _enr_rotr(w[t-2], 17) ⊻ _enr_rotr(w[t-2], 19) ⊻ (w[t-2] >> 10)
            w[t] = w[t-16] + s0 + w[t-7] + s1
        end
        a, b, c, d, e, f, g, hh = h
        for t in 1:64
            S1 = _enr_rotr(e, 6) ⊻ _enr_rotr(e, 11) ⊻ _enr_rotr(e, 25)
            ch = (e & f) ⊻ (~e & g)
            t1 = hh + S1 + ch + _SHA_K[t] + w[t]
            S0 = _enr_rotr(a, 2) ⊻ _enr_rotr(a, 13) ⊻ _enr_rotr(a, 22)
            maj = (a & b) ⊻ (a & c) ⊻ (b & c)
            t2 = S0 + maj
            hh = g; g = f; f = e; e = d + t1
            d = c; c = b; b = a; a = t1 + t2
        end
        h[1] += a; h[2] += b; h[3] += c; h[4] += d
        h[5] += e; h[6] += f; h[7] += g; h[8] += hh
    end
    io = IOBuffer()
    for x in h
        print(io, lpad(string(x, base = 16), 8, "0"))
    end
    return String(take!(io))
end

@inline _enr_rotr(x::UInt32, k::Integer) = (x >> k) | (x << (32 - k))

"""SHA-256 содержимого файла."""
function _enr_sha256_file(path::AbstractString)
    return _sha256(read(path))
end

# ---------------------------------------------------------------------
# РЕМОНТ SWEEP-ДВИЖКА (патчи D-1 / D-2 из отчёта)
# ---------------------------------------------------------------------

"""
    sweep_parameter(param; range, base_cfg, verbose=false)
    -> (results, best_val, best_score, best_result)

Перебор одного поля RHConfig по списку `range`. Для каждого значения
собирается спектр (n_seeds реализаций, центральное окно 30 %), считаются
все метрики и результат инкрементально дописывается в
`<output_dir>/sensitivity/sweep_history.csv`.

Сигнатура совместима с вызовами внутри sweep_top10_pro() и
sweep_combined_quick() файла RH_Sweep_Pro_D.jl (патч D-1).
"""
function sweep_parameter(param::Symbol; range = collect(0.0:0.5:2.0),
                         base_cfg::RHConfig = default_config(),
                         verbose::Bool = false)
    results = MetricsResult[]
    best_val = NaN
    best_score = -Inf
    best_result = nothing

    hist_dir = joinpath(base_cfg.output_dir, "sensitivity")
    isdir(hist_dir) || mkpath(hist_dir)
    hist_path = joinpath(hist_dir, "sweep_history.csv")
    if !isfile(hist_path)
        open(hist_path, "w") do f
            println(f, "# RH-Sweep PRO · sweep_parameter(:$(param)) · $(_enr_env_info())")
            println(f, "param,value,score,tests_passed,tests_total,r_mean,r_std,r_class," *
                    "d_GUE,K_corr_GUE,K_corr_zeta,R2_rms_GUE,R2_rms_zeta,Delta3_rms_GUE," *
                    "brody_beta,gap_prob_E1,r_tilde_mean,n_eigs,timestamp")
        end
    end

    n_total = length(range)
    t0 = time()
    zeta = get_zeta_zeros_safe(base_cfg.n_zeta_zeros)
    for (idx, v) in enumerate(range)
        cfg = deepcopy(base_cfg)
        setfield!(cfg, param, v)
        cfg.verbose = verbose

        eigs_all = Float64[]
        eigs_per_seed = 0
        for seed in 0:(cfg.n_seeds - 1)
            H = build_hamiltonian_with_config(cfg.L, cfg.alpha, cfg.W, cfg.sigma,
                                              seed, cfg)
            eigs_seed = central_eigs_sorted(H, window = 0.3)
            if seed == 0
                eigs_per_seed = length(eigs_seed)
            end
            append!(eigs_all, eigs_seed)
        end

        res = compute_all_metrics(eigs_all, zeta;
                                  label = "$(param)=$(round(Float64(v), digits = 4))",
                                  L = cfg.L, alpha = cfg.alpha, W = cfg.W,
                                  sigma = cfg.sigma, seed = -1,
                                  eigs_per_seed = eigs_per_seed)
        push!(results, res)

        open(hist_path, "a") do f
            row = [string(param), _enr_f(Float64(v); d = 4),
                   _enr_f(res.composite_score; d = 4),
                   string(res.tests_passed), string(res.tests_total),
                   _enr_f(res.r_mean), _enr_f(res.r_std), res.r_class,
                   _enr_f(res.d_GUE), _enr_f(res.K_corr_GUE),
                   _enr_f(res.K_corr_zeta), _enr_f(res.R2_rms_GUE),
                   _enr_f(res.R2_rms_zeta), _enr_f(res.Delta3_rms_GUE),
                   _enr_f(res.brody_beta), _enr_f(res.gap_prob_E1),
                   _enr_f(res.r_tilde_mean), string(res.n_eigs),
                   Dates.format(now(), "yyyy-mm-dd HH:MM:SS")]
            println(f, join(row, ","))
        end

        if res.composite_score > best_score
            best_score = res.composite_score
            best_val = Float64(v)
            best_result = res
        end

        if verbose
            @printf("  [%d/%d] %s=%g → score %.2f · K corr(ζ) %.4f · %s\n",
                    idx, n_total, param, Float64(v), res.composite_score,
                    res.K_corr_zeta, res.r_class)
        end
    end

    if verbose
        @printf("sweep_parameter(:%s): best=%.4g, score=%.2f · %.1f c\n",
                param, best_val, best_score, time() - t0)
    end
    return results, best_val, best_score, best_result
end

"""
    save_sweep_results(all_results, best_params, output_dir)

Сохраняет результаты sweep по параметрам: `sensitivity/<param>.csv`
(значение → ключевые метрики) и `sweep_best.csv` со сводкой лучших точек.
Сигнатура совместима с вызовами в RH_Sweep_Pro_D.jl (патч D-1).
"""
function save_sweep_results(all_results::Dict, best_params::Dict,
                            output_dir::AbstractString)
    sens_dir = joinpath(output_dir, "sensitivity")
    isdir(sens_dir) || mkpath(sens_dir)

    for (param, results) in all_results
        path = joinpath(sens_dir, "sweep_$(param).csv")
        open(path, "w") do f
            println(f, "value,score,tests_passed,r_mean,r_class,K_corr_GUE," *
                    "K_corr_zeta,R2_rms_GUE,brody_beta,gap_prob_E1")
            for r in results
                row = [_enr_f(Float64(r.alpha); d = 4),
                       _enr_f(r.composite_score; d = 4),
                       string(r.tests_passed), _enr_f(r.r_mean), r.r_class,
                       _enr_f(r.K_corr_GUE), _enr_f(r.K_corr_zeta),
                       _enr_f(r.R2_rms_GUE), _enr_f(r.brody_beta),
                       _enr_f(r.gap_prob_E1)]
                println(f, join(row, ","))
            end
        end
    end

    best_path = joinpath(sens_dir, "sweep_best.csv")
    open(best_path, "w") do f
        println(f, "param,best_value,best_score,tests_passed,K_corr_zeta")
        for (param, bp) in best_params
            row = [string(param), _enr_f(Float64(bp["value"]); d = 4),
                   _enr_f(bp["score"]; d = 2),
                   string(bp["result"].tests_passed),
                   _enr_f(bp["result"].K_corr_zeta)]
            println(f, join(row, ","))
        end
    end

    println("  [enricher] sensitivity/: $(length(all_results)) параметров → $sens_dir")
    return sens_dir
end

"""
    sweep_all_parameters(; base_cfg, n_points=17)

Полный sweep: 8 параметров × n_points значений (по умолчанию 17 →
136 прогонов). Патч D-2: функция заявлена в консольном меню
RH_Sweep_Pro_D.jl, но в файле отсутствовала.
"""
function sweep_all_parameters(; base_cfg::RHConfig = preset_auto(5000, verbose = false),
                              n_points::Int = 17,
                              output_dir::AbstractString =
                                  "RH_Sweep_All_$(Dates.format(now(), "yyyymmdd_HHMMSS"))")
    isdir(output_dir) || mkpath(output_dir)
    params = [:alpha, :W, :sigma, :alpha_jitter, :W_jitter,
              :sigma_jitter, :vortex_pos_jitter, :vortex_charge_flip]

    coarse = collect(range(0.0, 8.0, length = n_points))
    all_results = Dict{String, Vector{MetricsResult}}()
    best_params = Dict{String, Any}()

    for (p_idx, param) in enumerate(params)
        vals = param === :vortex_charge_flip ?
               collect(range(0.0, 1.0, length = n_points)) : coarse
        println("[enricher] sweep $p_idx/8: :$param ($(length(vals)) точек)")
        results, best_val, best_score, best_result =
            sweep_parameter(param; range = vals, base_cfg = base_cfg,
                            verbose = false)
        all_results[string(param)] = results
        best_params[string(param)] = Dict("value" => best_val,
                                          "score" => best_score,
                                          "result" => best_result)
        save_sweep_results(all_results, best_params, output_dir)
    end

    # сводка в консоль
    println("\n[enricher] сводка полного sweep:")
    for (param, bp) in best_params
        @printf("  %-20s best=%-8.4g score=%.2f · K corr(ζ)=%.4f\n",
                param, bp["value"], bp["score"], bp["result"].K_corr_zeta)
    end
    return Dict("all_results" => all_results, "best_params" => best_params,
                "output_dir" => output_dir)
end

# ---------------------------------------------------------------------
# КРИВЫЕ МЕТРИК (уровень P1)
# ---------------------------------------------------------------------

"""
    export_curves(eigs, zeta; out_dir, method=:polynomial)

Выгружает кривые всех метрик для AB-облака и ζ-нулей в CSV —
сторонний проверяющий может пересчитать RMS-метрики без Julia:
`curves/R2_ab_vs_theory.csv, R2_zeta.csv, K_ab_vs_zeta.csv,
Sigma2.csv, Delta3.csv, p_hist.csv`.
"""
function export_curves(eigs::AbstractVector{<:Real},
                       zeta::AbstractVector{<:Real};
                       out_dir::AbstractString = "curves",
                       method::Symbol = :polynomial)
    isdir(out_dir) || mkpath(out_dir)

    s_values = collect(0.0:0.05:5.0)
    t_values = collect(0.0:0.02:2.0)
    L_values = collect(0.5:0.5:10.0)

    R2_ab = compute_R2(eigs, s_values; method = method)
    R2_gue = [R2_GUE_theory(s) for s in s_values]
    R2_zeta = compute_R2(zeta, s_values; method = method)
    writedlm(joinpath(out_dir, "R2_ab_vs_theory.csv"),
             [s_values R2_ab R2_gue], ',')
    writedlm(joinpath(out_dir, "R2_zeta.csv"), [s_values R2_zeta], ',')

    K_ab = compute_K_empirical(eigs, t_values; method = method, smooth = true)
    K_zeta = compute_K_empirical(zeta, t_values; method = method, smooth = true)
    K_gue = [K_GUE_theory(t) for t in t_values]
    writedlm(joinpath(out_dir, "K_ab_vs_zeta.csv"),
             [t_values K_ab K_zeta K_gue], ',')

    S2_ab = compute_Sigma2(eigs, L_values; method = method)
    S2_gue = [Sigma2_GUE_theory(L) for L in L_values]
    S2_poi = [Sigma2_Poisson_theory(L) for L in L_values]
    writedlm(joinpath(out_dir, "Sigma2.csv"), [L_values S2_ab S2_gue S2_poi], ',')

    D3_ab = compute_Delta3(eigs, L_values; method = method)
    D3_gue = [Delta3_GUE_theory(L) for L in L_values]
    writedlm(joinpath(out_dir, "Delta3.csv"), [L_values D3_ab D3_gue], ',')

    centers, hist = compute_p_histogram(eigs; nbins = 30, method = method)
    wig = [p_GUE_wigner(s) for s in centers]
    writedlm(joinpath(out_dir, "p_hist.csv"), [centers hist wig], ',')

    println("  [enricher] curves/: 6 файлов → $out_dir")
    return out_dir
end

# ---------------------------------------------------------------------
# GUE-ПОЛ МЕТОДА И ЗНАЧИМОСТЬ (уровень P1)
# ---------------------------------------------------------------------

function _gue_ensemble_eigs(N::Int; n_ens::Int = 20, window::Float64 = 0.3)
    """Спектры n_ens матриц GUE размера N×N; возвращает конкатенацию
    центральных окон (как у AB-облака) и eigs_per_ens."""
    rng = MersenneTwister(96_3500)
    eigs_per = floor(Int, window * N)
    out = Float64[]
    for k in 1:n_ens
        A = (randn(rng, N, N) .+ im .* randn(rng, N, N)) ./ sqrt(2.0)
        H = Hermitian((A .+ A') ./ 2)
        vals = eigvals(H)
        e0 = quantile(vals, 0.5 - window / 2)
        e1 = quantile(vals, 0.5 + window / 2)
        append!(out, sort(vals[(vals .>= e0) .& (vals .<= e1)]))
    end
    return out, eigs_per
end

"""
    gue_floor_control(L, n_seeds; n_ens=20, n_zeta=5000, out_dir=".")

Пол метода: те же RMS-метрики на ансамбле GUE той же структуры выборки.
Матрицы строятся размера eigs_per_seed = ⌊0.3·L²⌋, чтобы блок статистики
совпадал с блоком AB-облака. Пишет `gue_floor.json` и возвращает Dict.
"""
function gue_floor_control(L::Int, n_seeds::Int; n_ens::Int = 20,
                           n_zeta::Int = 5000, out_dir::AbstractString = ".")
    eigs_per_seed = floor(Int, 0.3 * L * L)
    eigs, _ = _gue_ensemble_eigs(eigs_per_seed; n_ens = n_ens)
    zeta = get_zeta_zeros_safe(min(n_zeta, N_ZETA_ZEROS_AVAILABLE))
    res = compute_all_metrics(eigs, zeta; label = "GUE_floor", L = L,
                              alpha = 0.0, W = 0.0, sigma = 0.0, seed = -1,
                              eigs_per_seed = eigs_per_seed)
    floor_data = Dict(
        "what" => "GUE floor: статистический нуль метода на данной выборке",
        "L" => L, "n_seeds" => n_seeds, "n_ensembles" => n_ens,
        "eigs_per_ensemble" => eigs_per_seed, "n_eigs_total" => length(eigs),
        "timestamp" => Dates.format(now(), "yyyy-mm-dd HH:MM:SS"),
        "metrics" => Dict(
            "r_mean" => res.r_mean, "d_GUE" => res.d_GUE,
            "R2_rms_GUE" => res.R2_rms_GUE, "R2_rms_zeta" => res.R2_rms_zeta,
            "K_corr_GUE" => res.K_corr_GUE, "K_corr_zeta" => res.K_corr_zeta,
            "Sigma2_rms_GUE" => res.Sigma2_rms_GUE,
            "Delta3_rms_GUE" => res.Delta3_rms_GUE,
            "p_rms_GUE" => res.p_rms_GUE,
            "composite_score" => res.composite_score,
            "tests_passed" => res.tests_passed))
    path = joinpath(out_dir, "gue_floor.json")
    open(path, "w") do f
        print(f, _enr_json(floor_data))
    end
    println("  [enricher] gue_floor.json: Score(пол) = ",
            round(res.composite_score, digits = 2), "/100")
    return floor_data
end

"""
    multi_seed_block(cfg; n_seeds=5)

Значимость: mean±std ключевых метрик по независимым реализациям.
Пишет `sensitivity/multi_seed.csv`. Jitter учитывается как в cfg —
для чистой значимости обнуляйте jitter в конфигурации.
"""
function multi_seed_block(cfg::RHConfig; n_seeds::Int = 5)
    zeta = get_zeta_zeros_safe(cfg.n_zeta_zeros)
    rows = Vector{Vector{String}}()
    hdr = ["seed", "n_eigs", "r_mean", "r_class", "K_corr_GUE", "K_corr_zeta",
           "R2_rms_GUE", "Delta3_rms_GUE", "p_rms_GUE", "composite_score"]
    for seed in 0:(n_seeds - 1)
        H = build_hamiltonian_with_config(cfg.L, cfg.alpha, cfg.W, cfg.sigma,
                                          seed, cfg)
        eigs = central_eigs_sorted(H, window = 0.3)
        res = compute_all_metrics(eigs, zeta; label = "seed=$(seed)", L = cfg.L,
                                  alpha = cfg.alpha, W = cfg.W, sigma = cfg.sigma,
                                  seed = seed, eigs_per_seed = length(eigs))
        push!(rows, [string(seed), string(length(eigs)), _enr_f(res.r_mean),
                     res.r_class, _enr_f(res.K_corr_GUE), _enr_f(res.K_corr_zeta),
                     _enr_f(res.R2_rms_GUE), _enr_f(res.Delta3_rms_GUE),
                     _enr_f(res.p_rms_GUE), _enr_f(res.composite_score; d = 2)])
    end
    sens_dir = joinpath(cfg.output_dir, "sensitivity")
    isdir(sens_dir) || mkpath(sens_dir)
    path = joinpath(sens_dir, "multi_seed.csv")
    open(path, "w") do f
        println(f, join(hdr, ","))
        for r in rows
            println(f, join(r, ","))
        end
    end
    println("  [enricher] multi_seed.csv: $n_seeds реализаций → $path")
    return path
end

"""Комфортная обёртка: GUE-пол + значимость одним вызовом."""
function gue_floor_multi_report(cfg::RHConfig; n_floor_ens::Int = 20,
                                n_seeds_sig::Int = 5)
    floor_data = gue_floor_control(cfg.L, cfg.n_seeds; n_ens = n_floor_ens,
                                   n_zeta = cfg.n_zeta_zeros,
                                   out_dir = cfg.output_dir)
    multi_seed_block(cfg; n_seeds = n_seeds_sig)
    return floor_data
end

# ---------------------------------------------------------------------
# МАНИФЕСТ ЦЕЛОСТНОСТИ
# ---------------------------------------------------------------------

"""
    make_manifest(out_dir; exclude=Set(["manifest.sha256"]))

Рекурсивно считает SHA-256 всех файлов `out_dir` и пишет
`manifest.sha256` (формат: `хеш  относительный_путь  # размер байт`).
"""
function make_manifest(out_dir::AbstractString;
                       exclude::Set{String} = Set(["manifest.sha256"]))
    lines = String[]
    push!(lines, "# RH-Sweep PRO · integrity manifest")
    push!(lines, "# generated: $(Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))")
    push!(lines, "# tool: RH_Results_Enricher.jl · $(Base.VERSION)")
    for (root, dirs, files) in walkdir(out_dir)
        for fname in sort(files)
            full = joinpath(root, fname)
            rel = relpath(full, out_dir)
            rel in exclude && continue
            h = _enr_sha256_file(full)
            sz = filesize(full)
            push!(lines, "$(h)  $(replace(rel, '\\' => '/'))  # $(sz) B")
        end
    end
    path = joinpath(out_dir, "manifest.sha256")
    open(path, "w") do f
        println(f, join(lines, "\n"))
    end
    println("  [enricher] manifest.sha256: $(length(lines) - 3) файлов → $path")
    return path
end

# ---------------------------------------------------------------------
# ОРКЕСТРАТОР P0: enrich_run
# ---------------------------------------------------------------------

function _enr_config_dict(cfg::RHConfig)
    d = Dict{String, Any}()
    for name in fieldnames(RHConfig)
        v = getfield(cfg, name)
        d[string(name)] = v isa Symbol ? String(v) : v
    end
    d["environment"] = _enr_env_info()
    return d
end

function _enr_verdicts(final_result, chi2_pass, brody_pass, comp_pass,
                       gap_pass, rtilde_pass)
    r = final_result
    return [
        ("1. ⟨r⟩ ≈ R_GUE (|d_GUE| < 0.05)", r.d_GUE < 0.05),
        ("2. R2(s) ближе к GUE, чем к Пуассону", r.R2_match_GUE),
        ("3. K(t) коррелирует с K(ζ)", r.K_match_GUE),
        ("4. Σ2(L) ближе к GUE, чем к Пуассону", r.Sigma2_match_GUE),
        ("5. Δ3(L) RMS < 0.5", !isnan(r.Delta3_rms_GUE) && r.Delta3_rms_GUE < 0.5),
        ("6. p(s) RMS < 0.2", r.p_rms_GUE < 0.2),
        ("7. χ2 Wigner < 0.5", chi2_pass),
        ("8. Brody β ≈ 2.0 ± 0.5", brody_pass),
        ("9. Compressibility < 0.3", comp_pass),
        ("10. E(s=1) ≈ 0.171 ± 0.15", gap_pass),
        ("11. ⟨r̃⟩ ≈ 0.3602 ± 0.05", rtilde_pass)]
end

"""
    enrich_run(cfg, final_result, all_results, eigs, zeta; out_dir)

Пишет научный слой P0 в папку прогона:
  README.md · SUMMARY.md · DATA_DICTIONARY.md · config.json · manifest.sha256
Вызывается один раз в конце _final_run(). Возвращает Dict с путями файлов.
"""
function enrich_run(cfg::RHConfig, final_result, all_results,
                    eigs::AbstractVector{<:Real},
                    zeta::AbstractVector{<:Real};
                    out_dir::AbstractString = cfg.output_dir)
    isdir(out_dir) || mkpath(out_dir)
    r = final_result

    chi2_pass = r.chi2_wigner < 0.5
    brody_pass = abs(r.brody_beta - 2.0) < 0.5
    comp_pass = r.spectral_compressibility < 0.3
    gap_pass = abs(r.gap_prob_E1 - 0.171) < 0.1
    rtilde_pass = !isnan(r.r_tilde_mean) && abs(r.r_tilde_mean - 0.3602) < 0.05
    verdicts = _enr_verdicts(r, chi2_pass, brody_pass, comp_pass, gap_pass,
                             rtilde_pass)
    n_pass = sum(v[2] for v in verdicts)

    # ---------- config.json ----------
    cfg_path = joinpath(out_dir, "config.json")
    open(cfg_path, "w") do f
        print(f, _enr_json(_enr_config_dict(cfg)))
    end

    # ---------- README.md ----------
    n_sweep_points = max(length(all_results) - 1, 0)
    readme = IOBuffer()
    println(readme, "# Прогон $(basename(out_dir))")
    println(readme)
    println(readme, "> RH-Sweep PRO · AB-облако ↔ ζ-нули · отчёт сгенерирован ",
            "RH_Results_Enricher.jl $(Dates.format(now(), "yyyy-mm-dd HH:MM"))")
    println(readme)
    println(readme, "## TL;DR")
    println(readme)
    println(readme, "| Величина | Значение |")
    println(readme, "|:---|:---|")
    println(readme, "| Лучшая конфигурация | α = $(r.alpha), W = $(r.W), σ = $(r.sigma) |")
    println(readme, "| Composite Score | $(round(r.composite_score, digits = 2)) / 100 |")
    println(readme, "| Тесты RMT | $(r.tests_passed)/$(r.tests_total) · $(n_pass)/11 с новыми |")
    println(readme, "| ⟨r⟩ | $(round(r.r_mean, digits = 5)) (R_GUE = $(R_GUE), класс $(r.r_class)) |")
    println(readme, "| K corr(GUE) / K corr(ζ) | $(round(r.K_corr_GUE, digits = 4)) / $(round(r.K_corr_zeta, digits = 4)) |")
    println(readme, "| Решётка | L = $(r.L) · $(r.n_eigs) соб. значений · $(length(zeta)) ζ-нулей |")
    println(readme)
    println(readme, "## Вердикты (11 тестов)")
    println(readme)
    for (name, ok) in verdicts
        println(readme, " - [", ok ? "x" : " ", "] ", name)
    end
    println(readme)
    println(readme, "## Состав папки")
    println(readme)
    println(readme, " - `plots/ csv/ txt/ json/` — артефакты конвейера (см. `DATA_DICTIONARY.md`)")
    println(readme, " - `config.json` — снапшот всех ", length(fieldnames(RHConfig)),
            " полей RHConfig + окружение")
    println(readme, " - `manifest.sha256` — контрольные суммы всех файлов папки")
    println(readme, " - `curves/ sensitivity/ gue_floor.json` — уровень P1 (если создан)")
    println(readme)
    println(readme, "## Воспроизведение")
    println(readme)
    println(readme, "```julia")
    println(readme, "include(\"RH_Sweep_Pro_D.jl\")")
    println(readme, "cfg = preset_auto($(cfg.n_zeta_zeros))   # L=$(cfg.L), n_seeds=$(cfg.n_seeds)")
    println(readme, "cfg.alpha = $(cfg.alpha); cfg.W = $(cfg.W); cfg.sigma = $(cfg.sigma)")
    println(readme, "cfg.output_dir = \"$(basename(out_dir))\"")
    println(readme, "run(cfg)")
    println(readme, "```")
    println(readme)
    println(readme, "Окружение: $(_enr_env_info()).  ")
    println(readme, "Побайтовое совпадение гарантируется только на той же платформе.")
    open(joinpath(out_dir, "README.md"), "w") do f
        print(f, String(take!(readme)))
    end

    # ---------- SUMMARY.md ----------
    summ = IOBuffer()
    println(summ, "# SUMMARY · $(basename(out_dir))")
    println(summ)
    println(summ, "```json")
    println(summ, _enr_json(Dict(
        "alpha" => r.alpha, "W" => r.W, "sigma" => r.sigma, "L" => r.L,
        "n_eigs" => r.n_eigs, "n_zeta_zeros" => length(zeta),
        "r_mean" => round(r.r_mean, digits = 5),
        "r_class" => r.r_class,
        "composite_score" => round(r.composite_score, digits = 2),
        "tests_passed" => r.tests_passed, "tests_total" => r.tests_total,
        "tests_with_new_metrics" => n_pass,
        "K_corr_GUE" => round(r.K_corr_GUE, digits = 4),
        "K_corr_zeta" => round(r.K_corr_zeta, digits = 4),
        "R2_rms_GUE" => round(r.R2_rms_GUE, digits = 6),
        "gap_prob_E1" => round(r.gap_prob_E1, digits = 4),
        "brody_beta" => round(r.brody_beta, digits = 4),
        "environment" => _enr_env_info())))
    println(summ, "```")
    open(joinpath(out_dir, "SUMMARY.md"), "w") do f
        print(f, String(take!(summ)))
    end

    # ---------- DATA_DICTIONARY.md ----------
    write_enricher_dictionary(out_dir)

    # ---------- manifest ----------
    make_manifest(out_dir)

    println("  [enricher] enrich_run: README/SUMMARY/DICTIONARY/config/manifest → $out_dir")
    return Dict("readme" => joinpath(out_dir, "README.md"),
                "summary" => joinpath(out_dir, "SUMMARY.md"),
                "dictionary" => joinpath(out_dir, "DATA_DICTIONARY.md"),
                "config" => cfg_path,
                "manifest" => joinpath(out_dir, "manifest.sha256"))
end

"""
    write_enricher_dictionary(out_dir)

Пишет DATA_DICTIONARY.md: словарь колонок metrics.csv, sensitivity/ и
curves/. Содержимое статично и синхронизировано с RH_Sweep_Pro_D.jl v1.0.
"""
function write_enricher_dictionary(out_dir::AbstractString)
    path = joinpath(out_dir, "DATA_DICTIONARY.md")
    open(path, "w") do f
        print(f, _DICTIONARY_MD)
    end
    return path
end

const _DICTIONARY_MD = """# Словарь данных прогона

Строка `metrics.csv` = одна конфигурация AB-облака. Все величины считаются
на центральных 30 % спектра с блочным усреднением B = 250.

## Идентификация

| Колонка | Смысл |
|:--|:--|
| `label` | человеко-читаемая метка точки (`α=…`, `final_α=…`) |
| `L` | сторона решётки; гамильтониан L²×L² |
| `alpha, W, sigma` | поток AB, сила беспорядка, радиус вихря |
| `n_eigs` | число центральных собственных значений (все seed) |

## Сигнальные метрики

| Колонка | Смысл | Цель GUE |
|:--|:--|:--|
| `r_mean`, `r_std` | среднее отношение интервалов ± std | 0.5996 |
| `r_class` | ближайший класс RMT (GUE/GOE/GSE/Poisson) | GUE |
| `d_GUE, d_GOE, d_GSE, d_Poisson` | |⟨r⟩ − эталон| | 0 |

## Парная корреляция и форм-фактор

| Колонка | Смысл | Цель |
|:--|:--|:--|
| `R2_rms_GUE` | RMS(R2_AB − R2_GUE) | → 0 |
| `R2_rms_Poisson` | RMS(R2_AB − 1) | → ∞ |
| `R2_rms_zeta` | RMS(R2_AB − R2_ζ) | → 0 |
| `R2_match_GUE` | ближе к GUE, чем к Пуассону | TRUE |
| `K_corr_GUE` | корреляция K(t) с GUE-ramp+plateau | → +1 |
| `K_corr_zeta` | корреляция K(t) с K(ζ) | → +1 |
| `K_match_GUE / K_match_zeta` | пороги 0.8/0.7 по corr(ζ) | TRUE |

## Статистики уровней

| Колонка | Смысл | Цель GUE |
|:--|:--|:--|
| `Sigma2_rms_GUE / _Poisson` | RMS Σ²(L) против теории | → 0 / → ∞ |
| `Delta3_rms_GUE` | RMS Δ₃(L) против GUE | < 0.5 |
| `p_rms_GUE` | RMS p(s) против Вигнера-GUE | < 0.2 |
| `p_mean` | среднее гистограммы p(s) | ~0.25 |

## Новые метрики (внутренние сравнительные)

| Колонка | Смысл | Цель GUE |
|:--|:--|:--|
| `chi2_wigner` | χ²-статистика против Вигнера (30 бинов) | < 0.5 |
| `chi2_pvalue` | exp(−χ²/2) — монотонная мера, НЕ p-value | → 1 |
| `brody_beta` | параметр Броуди (отталкивание уровней) | ≈ 2.0 |
| `spectral_compressibility` | mean Σ²(L)/L при L = 9–10 (прокси) | < 0.3 |
| `gap_prob_E1` | доля интервалов s ≥ 1 | ≈ 0.171 |
| `r_tilde_mean` | ⟨r̃⟩ = ⟨sᵢ/(sᵢ+sᵢ₊₁)⟩ | ≈ 0.3602 |
| `level_number_dev` | ⟨δ²ₙ⟩ отклонение номера уровня | → 0 |
| `symmetry_parameter` | S = ⟨r⟩/(1−⟨r⟩) (информационная) | ≈ 1.496 |

## Итог

| Колонка | Смысл |
|:--|:--|
| `composite_score` | агрегат 0–100 из 12 компонент (веса 15/10/5) |
| `tests_passed / tests_total` | пройдено тестов из 11 (6 классических + 5 новых) |

## Файлы уровня обогащения

| Файл | Колонки | Смысл |
|:--|:--|:--|
| `sensitivity/sweep_history.csv` | `param, value, score, …` | полная история sweep-точек (инкрементально) |
| `sensitivity/sweep_<param>.csv` | `value, score, …` | разрез по одному параметру |
| `sensitivity/sweep_best.csv` | `param, best_value, best_score, …` | лучшие точки |
| `sensitivity/multi_seed.csv` | `seed, r_mean, K_corr_…, score` | значимость по реализациям |
| `curves/R2_ab_vs_theory.csv` | `s, R2_ab, R2_gue` | пересчёт RMS(R2) без Julia |
| `curves/K_ab_vs_zeta.csv` | `t, K_ab, K_zeta, K_gue` | пересчёт корреляций K(t) |
| `curves/Sigma2.csv` | `L, S2_ab, S2_gue, S2_poi` | дисперсия числа уровней |
| `curves/Delta3.csv` | `L, D3_ab, D3_gue` | спектральная жёсткость |
| `curves/p_hist.csv` | `s_center, p_hist, p_wigner` | распределение интервалов |
| `gue_floor.json` | метрики GUE-ансамбля | статистический нуль метода |
| `config.json` | все поля RHConfig + окружение | снапшот прогона |
| `manifest.sha256` | `hash  path  # size` | целостность папки |
"""
