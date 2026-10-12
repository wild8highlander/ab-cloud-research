# e11_validator.jl — ЭКСПЕРИМЕНТ 11, слой B: НЕЗАВИСИМЫЙ ВАЛИДАТОР.
#
# Запускается СТРОГО ПОСЛЕ фиксации и хеширования выхода детектора
# (run_all.jl контролирует порядок). Содержит:
#   1) опубликованные эталонные константы (первые 13 нулей, литература);
#   2) независимый метод локализации: Гаусс–Ньютон по |ζ|² (не намотка
#      и не золотое сечение) с другим численным расписанием ζ
#      (N=48, K=10 вместо N=64, K=14 у детектора);
#   3) расчёт precision / recall / max / RMS ошибки позиций;
#   4) контроль устойчивости к сетке (перезапуск детектора на h∈{0.02, 0.005});
#   5) контроль полноты по принципу аргумента (намотка ↔ число нулей).

module ZetaValidator

using ..ZetaDetector
using Printf, SHA

export run_validation!, REFERENCE_ZEROS

# Публикаторы: первые 13 нетривиальных нулей ζ (независимый источник:
# mpmath.zetazero(1..13), 40 значащих цифр, прогенерирован отдельно от детектора).
# ЭРРАТУМ v0.1.0-каркаса: γ12 была закодирована рукой как 56.446200059994141 —
# слепой детектор дал 56.446247697063399, mpmath подтвердил ДЕТЕКТОР
# (|ζ| там = 9.9e−15, а на «рукотворном» значении |ζ| = 1.1e−4).
const REFERENCE_ZEROS = [
    14.134725141734693790, 21.022039638771554993, 25.010857580145688763,
    30.424876125859513210, 32.935061587739189691, 37.586178158825671257,
    40.918719012147495187, 43.327073280914999519, 48.005150881167159728,
    49.773832477672302182, 52.970321477714460644, 56.446247697063394804,
    59.347044002602353080]

"Независимое расписание оценки ζ (отличается от детектора)."
function zeta_val(s::Complex{BigFloat})
    N = 48; K = 10
    acc = BigFloat(0)
    for n in 1:(N - 1)
        acc += BigFloat(n)^(-s)
    end
    Nb = BigFloat(N)
    acc += Nb^(1 - s) / (s - 1)
    acc += BigFloat("0.5") * Nb^(-s)
    sp = s                                            # s^{↑1}
    for k in 1:K
        acc += BigFloat(ZetaDetector.BERN[k]) * sp * Nb^(-s - BigFloat(2k - 1)) /
               BigFloat(factorial(BigInt(2k)))
        sp *= (s + BigFloat(2k - 1)) * (s + BigFloat(2k))   # s^{↑(2k+1)}
    end
    return acc
end

"Гаусс–Ньютон по |ζ|²: независимый способ локализации нуля."
function gauss_newton_zero(t_init::Float64)
    half = BigFloat("0.5")
    function F(t::Float64)
        v = zeta_val(Complex{BigFloat}(half, BigFloat(t)))
        return (Float64(real(v)), Float64(imag(v)))
    end
    t = t_init
    for _ in 1:60
        h = 1e-6
        f0 = F(t)
        fp = F(t + h)
        fm = F(t - h)
        # J ≈ [(fp−fm)/(2h)] — вектор производных (2-компоненты)
        d1 = (fp[1] - fm[1]) / (2h)
        d2 = (fp[2] - fm[2]) / (2h)
        g = f0[1] * d1 + f0[2] * d2                 # ½∇|ζ|²
        jj = d1^2 + d2^2
        jj < 1e-300 && break
        step = g / jj
        abs(step) > 1e-3 && (step = sign(step) * 1e-3)
        t -= step
        abs(step) < 1e-15 && break
    end
    v = zeta_val(Complex{BigFloat}(half, BigFloat(t)))
    return t, Float64(abs(v))
end

"""
Полная валидация: detector_positions (из зафиксированного CSV),
контроль сетки через перезапуск детектора, precision/recall, ошибки.
"""
function run_validation!(detector_positions::Vector{Float64},
                         detector_winding::Float64; t1::Float64 = 60.0)
    ref = REFERENCE_ZEROS
    n_ref_in_range = count(x -> x <= t1, ref)

    # 1) назначение детектор↔эталон (жадное по ближайшему)
    matches = Tuple{Int,Float64,Float64}[]   # (idx_ref, γ_ref, γ_det)
    used = falses(length(detector_positions))
    recalls = 0
    max_err = 0.0
    sq_sum = 0.0
    for (i, g) in enumerate(ref)
        g <= t1 || continue
        best, bj = Inf, 0
        for (j, gd) in enumerate(detector_positions)
            if !used[j] && abs(gd - g) < best
                best = abs(gd - g); bj = j
            end
        end
        if bj > 0 && best <= 0.5
            used[bj] = true
            push!(matches, (i, g, detector_positions[bj]))
            max_err = max(max_err, best)
            sq_sum += best^2
            recalls += 1
        end
    end
    n_det = length(detector_positions)
    precision = n_det == 0 ? 0.0 : recalls / n_det
    recall = n_ref_in_range == 0 ? 0.0 : recalls / n_ref_in_range

    # 2) независимая локализация (Гаусс–Ньютон) от позиций детектора
    gn_positions = Float64[]
    gn_zmin = Float64[]
    for gd in detector_positions
        t, zm = gauss_newton_zero(gd)
        push!(gn_positions, t)
        push!(gn_zmin, zm)
    end
    gn_max_err_vs_ref = 0.0
    for (i, g, gd) in matches
        gn_max_err_vs_ref = max(gn_max_err_vs_ref, abs(gn_positions[i] - g))
    end

    # 3) устойчивость к сетке: перезапуск детектора на h=0.02 и h=0.005
    robust = Dict{String,Any}()
    for h in (0.02, 0.005)
        d = ZetaDetector.detect_zeros(0.3, t1, h)
        robust[@sprintf("h_%.3f", h)] = Dict(
            "count" => length(d["positions"]),
            "winding" => d["winding_count"],
            "max_diff_vs_first" => length(d["positions"]) == n_det ?
                maximum(abs.(d["positions"] .- detector_positions)) : NaN)
    end

    # 4) полнота по Риману–фон Мангольдту (аргументный принцип, стандартный путь)
    S_T, theta_T, N_rvm = ZetaDetector.standard_path_arg(t1)
    winding_zeros = round(detector_winding)   # диагностическое (намотка по прямой)

    return Dict(
        "n_detector" => n_det,
        "n_reference_in_range" => n_ref_in_range,
        "n_matched" => recalls,
        "precision" => precision,
        "recall" => recall,
        "max_position_error" => max_err,
        "rms_position_error" => sqrt(sq_sum / max(1, recalls)),
        "gauss_newton_max_error_vs_reference" => gn_max_err_vs_ref,
        "gauss_newton_max_abszeta" => maximum(gn_zmin),
        "grid_robustness" => robust,
        "winding_count" => detector_winding,
        "winding_zeros_rounded" => winding_zeros,
        "S_T" => S_T, "theta_T" => theta_T, "N_rvm" => N_rvm,
        "N_rvm_rounded" => round(N_rvm),
        "matched_table" => [(Float64(g), Float64(gd), Float64(gd - g))
                            for (_, g, gd) in matches])
end

end # module
