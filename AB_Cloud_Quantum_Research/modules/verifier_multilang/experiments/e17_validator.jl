# e17_validator.jl — ЭКСПЕРИМЕНТ 17, слой B: НЕЗАВИСИМЫЙ ВАЛИДАТОР.
#
# Запускается СТРОГО ПОСЛЕ фиксации и хеширования выходов ОБОИХ детекторов
# (run_all.jl контролирует порядок). Содержит:
#   1) проверку целостности эталонной таблицы mpmath.zetazero по SHA256
#      (таблица сгенерирована независимо, scripts/make_zetazero_reference.py);
#   2) независимый метод локализации: Гаусс–Ньютон по |ζ|² с ДРУГИМ
#      расписанием ЭМ (N=320, K=12 — не совпадает с расписанием детектора);
#   3) precision / recall / max / RMS ошибки позиций против эталона;
#   4) кросс-движковое согласие (ЭМ-детектор против RS-детектора);
#   5) устойчивость к сетке на подокне [900, 1000]: h ∈ {0.02, 0.005};
#   6) контроль полноты N(1000) по стандартному пути (принцип аргумента).

module HighValidator

using ..ZetaDetector
using ..RiemannSiegel
using ..HighBlind
using SHA
using Printf

export run_high_validation!

const OUTDIR = joinpath(@__DIR__, "..", "results")
const REF_CSV = joinpath(OUTDIR, "e17_zetazero_reference.csv")
const REF_SHA = joinpath(OUTDIR, "e17_zetazero_reference_sha256.txt")

"Независимое расписание валидатора: (N=320, K=12) — отличается от детекторных."
val_zeta(t::Float64) = zeta_em_scaled(complex(BigFloat("0.5"), BigFloat(t));
                                      N = 320, K = 12)

"Гаусс–Ньютон по |ζ|² (независимый способ локализации нуля)."
function gauss_newton_zero(t_init::Float64)
    function F(t::Float64)
        v = val_zeta(t)
        return (Float64(real(v)), Float64(imag(v)))
    end
    t = t_init
    for _ in 1:60
        h = 1e-6
        f0 = F(t)
        fp = F(t + h)
        fm = F(t - h)
        d1 = (fp[1] - fm[1]) / (2h)
        d2 = (fp[2] - fm[2]) / (2h)
        g = f0[1] * d1 + f0[2] * d2
        jj = d1^2 + d2^2
        jj < 1e-300 && break
        step = g / jj
        abs(step) > 1e-3 && (step = sign(step) * 1e-3)
        t -= step
        abs(step) < 1e-15 && break
    end
    v = val_zeta(t)
    return t, Float64(abs(v))
end

"Загрузка эталонной таблицы с проверкой SHA256."
function load_reference()
    expected = strip(split(read(REF_SHA, String), "\n")[1])
    h = bytes2hex(sha256(read(REF_CSV)))
    h == split(expected)[1] || error("SHA256 эталонной таблицы не совпал")
    gammas = Tuple{Int,Float64}[]
    for ln in eachline(REF_CSV)
        lnstartswith = startswith(ln, "n,") || startswith(ln, "n=")
        (isempty(ln) || lnstartswith) && continue
        parts = split(ln, ",")
        length(parts) == 2 || continue
        push!(gammas, (parse(Int, parts[1]), parse(Float64, parts[2])))
    end
    return gammas
end

"Чтение позиций из пинованного CSV детектора."
function read_detector_csv(path::String)
    pos = Float64[]
    meta = Dict{String,String}()
    for ln in eachline(path)
        parts = split(ln, ",")
        if parts[1] == "position" && length(parts) >= 4
            push!(pos, parse(Float64, parts[3]))
        elseif parts[1] == "meta" && length(parts) >= 3
            meta[parts[2]] = join(parts[3:end], ",")
        end
    end
    return pos, meta
end

"""
Полная валидация E17. Читает ПИНОВАННЫЕ выходы детекторов (с проверкой SHA256
против .sha256-файлов — слепая дисциплина), сопоставляет с эталоном, пишет CSV.
"""
function run_high_validation!()
    # ── целостность пинов детекторов (дисциплина слепоты) ──
    for (csv, shafile) in (("e17_detector_em.csv", "e17_detector_em_sha256.txt"),
                           ("e17_detector_rs.csv", "e17_detector_rs_sha256.txt"))
        expected = strip(split(read(joinpath(OUTDIR, shafile), String), "\n")[1])
        h = bytes2hex(sha256(read(joinpath(OUTDIR, csv))))
        h == split(expected)[1] || error("SHA256 детектора не совпал: $csv")
    end
    pos_em, meta_em = read_detector_csv(joinpath(OUTDIR, "e17_detector_em.csv"))
    pos_rs, meta_rs = read_detector_csv(joinpath(OUTDIR, "e17_detector_rs.csv"))
    winding_em = parse(Float64, meta_em["winding_count"])
    winding_rs = parse(Float64, meta_rs["winding_count"])

    ref = load_reference()
    ref_gamma = [g for (n, g) in ref]

    # ── Гаусс–Ньютон (независимое расписание) для обоих детекторов ──
    refined_em = Float64[]
    absz_em = Float64[]
    for p in pos_em
        t, z = gauss_newton_zero(p)
        push!(refined_em, t)
        push!(absz_em, z)
    end
    refined_rs = Float64[]
    absz_rs = Float64[]
    for p in pos_rs
        t, z = gauss_newton_zero(p)
        push!(refined_rs, t)
        push!(absz_rs, z)
    end

    # ── Сопоставление с эталоном (окно ±0.1, взаимно-однозначно) ──
    function match_to_reference(refined::Vector{Float64}, lo::Float64, hi::Float64)
        inrange = [g for g in ref_gamma if lo <= g < hi]
        matched = 0
        errs = Float64[]
        table = Tuple{Float64,Float64,Float64}[]
        used = falses(length(inrange))
        for t in refined
            best, bi = Inf, 0
            for (i, g) in enumerate(inrange)
                !used[i] || continue
                d = abs(t - g)
                if d < best
                    best = d
                    bi = i
                end
            end
            if bi > 0 && best <= 0.1
                used[bi] = true
                matched += 1
                push!(errs, best)
                push!(table, (inrange[bi], t, best))
            end
        end
        nfp = length(refined) - matched          # ложные положительные
        nfn = length(inrange) - matched          # ложные отрицательные
        precision = matched / max(length(refined), 1)
        recall = matched / max(length(inrange), 1)
        max_err = isempty(errs) ? NaN : maximum(errs)
        rms_err = isempty(errs) ? NaN : sqrt(sum(e^2 for e in errs) / length(errs))
        return Dict("n_detected" => length(refined), "n_reference" => length(inrange),
                    "n_matched" => matched, "n_false_pos" => nfp, "n_false_neg" => nfn,
                    "precision" => precision, "recall" => recall,
                    "max_err" => max_err, "rms_err" => rms_err, "table" => table)
    end

    m_em = match_to_reference(refined_em, 0.3, 1000.0)
    m_rs = match_to_reference(refined_rs, 50.0, 1000.0)

    # ── Кросс-движок: позиции RS против позиций ЭМ на общем окне ──
    cross_errs = Float64[]
    for (i, t) in enumerate(refined_rs)
        # ближайшая позиция ЭМ (списки упорядочены по возрастанию)
        best = Inf
        for u in refined_em
            d = abs(t - u)
            d < best && (best = d)
        end
        push!(cross_errs, best)
    end
    cross_max = isempty(cross_errs) ? NaN : maximum(cross_errs)

    # ── Контроль полноты N(1000) ──
    S_T, theta_T, N_rvm = standard_path_N(1000.0)
    N_round = round(Int, N_rvm)

    # ── Устойчивость к сетке на [900, 1000] ──
    main_in_window = [t for t in refined_em if 900.0 <= t <= 1000.0]
    robust_rows = []
    max_shift = 0.0
    for h in (0.02, 0.005)
        det_h = detect_zeros_generic(zeta_line_em, 900.0, 1000.0, h)
        refined_h = Float64[]
        for p in det_h["positions"]
            t, z = gauss_newton_zero(p)
            push!(refined_h, t)
        end
        shift_h = 0.0
        for t in refined_h
            best = Inf
            for u in main_in_window
                d = abs(t - u)
                d < best && (best = d)
            end
            shift_h = max(shift_h, best)
        end
        max_shift = max(max_shift, shift_h)
        push!(robust_rows, (h, length(refined_h), shift_h))
    end

    # ── CSV ──
    open(joinpath(OUTDIR, "experiment_17_validation.csv"), "w") do io
        println(io, "experiment,quantity,value")
        for (eng, m) in (("em", m_em), ("rs", m_rs))
            for k in ("n_detected", "n_reference", "n_matched", "n_false_pos",
                      "n_false_neg", "precision", "recall", "max_err", "rms_err")
                println(io, 17, ",$(eng)_$(k),", m[k])
            end
        end
        println(io, 17, ",cross_engine_max_err,", cross_max)
        println(io, 17, ",winding_em,", winding_em)
        println(io, 17, ",winding_rs,", winding_rs)
        println(io, 17, ",S_T_standard_path,", S_T)
        println(io, 17, ",theta_T,", theta_T)
        println(io, 17, ",N_rvm,", N_rvm)
        println(io, 17, ",N_rvm_rounded,", N_round)
        println(io, 17, ",grid_robustness_max_shift,", max_shift)
    end
    open(joinpath(OUTDIR, "experiment_17_matched_em.csv"), "w") do io
        println(io, "experiment,gamma_reference,gamma_detected,delta")
        for (g, t, d) in m_em["table"]
            println(io, 17, ",", @sprintf("%.15f", g), ",",
                    @sprintf("%.15f", t), ",", @sprintf("%.3e", d))
        end
    end
    open(joinpath(OUTDIR, "experiment_17_matched_rs.csv"), "w") do io
        println(io, "experiment,gamma_reference,gamma_detected,delta")
        for (g, t, d) in m_rs["table"]
            println(io, 17, ",", @sprintf("%.15f", g), ",",
                    @sprintf("%.15f", t), ",", @sprintf("%.3e", d))
        end
    end
    open(joinpath(OUTDIR, "experiment_17_robustness.csv"), "w") do io
        println(io, "experiment,h,n_zeros,max_shift")
        for (h, nz, sh) in robust_rows
            println(io, 17, ",", h, ",", nz, ",", @sprintf("%.3e", sh))
        end
    end
    # Кривая намотки для рисунка (прореженная, движок ЭМ)
    ts, args, mags = unwrapped_arg_generic(zeta_line_em, 0.3, 1000.0, 0.25)
    open(joinpath(OUTDIR, "experiment_17_winding_curve.csv"), "w") do io
        println(io, "experiment,t,arg_unwrapped,abs_zeta")
        for (t, a, m) in zip(ts, args, mags)
            println(io, 17, ",", @sprintf("%.4f", t), ",",
                    @sprintf("%.6f", a), ",", @sprintf("%.6e", m))
        end
    end

    return Dict("em" => m_em, "rs" => m_rs, "cross_max" => cross_max,
                "S_T" => S_T, "theta_T" => theta_T, "N_rvm" => N_rvm,
                "N_round" => N_round, "max_shift" => max_shift,
                "robust_rows" => robust_rows)
end

end # module
