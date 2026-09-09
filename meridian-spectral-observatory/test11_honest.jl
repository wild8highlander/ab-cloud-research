#!/usr/bin/env julia
# ═══════════════════════════════════════════════════════════════════════════
# test11_honest.jl — честная перекалибровка Test 11 из ab_cloud_v18.jl
#   (Anderson–Darling GOF: спейсинги нулей ζ(s) vs surmise Вигнера GUE β=2)
#
# ЧТО БЫЛО НЕ ТАК В ОРИГИНАЛЕ
# ----------------------------
# Оригинальный Test 11 строил MC null-распределение бутстрэпом (с возвращением)
# 49999 спейсингов из пула ~8000 реальных спейсингов ОДНОЙ матрицы GUE 10000×10000.
# 49999 отсчётов из 8000 различных значений с возвращением (~6.25× oversampling)
# порождают массу точных повторов (tied values) — то, чего в принципе не бывает
# у непрерывных данных. Формула A² (веса (2i−1) по возрастающим F(x_(i))) на
# повторах систематически завышается. Проверено отдельной симуляцией
# (тот же алгоритм на реальной матрице 4000×4000 и 10000×10000): один этот
# артефакт поднимает типичное значение null A² с учебных O(1) (медиана ~0.5–1,
# критическое значение 5% ≈ 2.492, НЕ зависит от n для корректно заданного
# непрерывного закона) до значений в разы и на порядок выше — сильно зависит
# от конкретной реализации матрицы. Это правдоподобно полностью объясняет,
# почему исходный прогон получил медиану референса 12.54 вместо ожидаемой ~1.
#
# ИСПРАВЛЕНИЕ
# -----------
# Для one-sample GOF-теста с ПОЛНОСТЬЮ заданным непрерывным H0 (спейсинги ~ i.i.d.
# ~ gue2_surmise_cdf) корректный MC null — это n_mc независимых повторов размера n,
# каждый — i.i.d. выборка НАПРЯМУЮ из gue2_surmise_cdf (inverse-transform sampling),
# а не бутстрэп конечного эмпирического пула. Именно так сделано здесь.
# p-value считается с add-one (Laplace) сглаживанием — "p = 0.0000" на паре тысяч
# повторов вводит в заблуждение, это артефакт отображения, а не настоящий ноль.
#
# Все остальные части (загрузка данных, unfolding, сама формула A²) НЕ менялись —
# они уже были независимо перепроверены (см. PASS 3 в исходном логе: точная
# формула и интерполяционная таблица дают A² с разницей 1.9e-05).
#
# Бонус: t_dependence_scan — проверка "сходимости на малых T" напрямую по данным
# (Objection 2 из комментариев кода), а не как утверждение в комментарии.
#
# ПОБОЧНО ИСПРАВЛЕНО: в оригинальном get_gue_ref лог печатал "poly_deg=9"
# захардкоженной константой, а реально вызывалась unfold_gue_eigenvalues(eigs)
# без poly_deg → использовался ДЕФОЛТ poly_deg=5 (см. сигнатуру функции,
# строка ~1407 ab_cloud_v18.jl). Численно эффект пренебрежимо мал (проверено:
# native A² пула 0.393 при deg=5 vs 0.393 при deg=9 на матрице 4000×4000) —
# то есть это баг честности лога, а не источник WARN. Не является предметом
# этого файла (этот файл вообще не строит референс из матрицы GUE), но
# стоит поправить в основном коде отдельно.
# ═══════════════════════════════════════════════════════════════════════════

using Random
using Printf

# ─────────────────────────────────────────────────────────────────────────
# 1. Статистические хелперы — Lanczos lgamma + regularized incomplete gamma
#    (СКОПИРОВАНО ДОСЛОВНО из ab_cloud_v18.jl, строки ~913-974, для полной
#    численной совместимости с исходным тестом)
# ─────────────────────────────────────────────────────────────────────────
const _LANCZOS_G = 7
const _LANCZOS_COEF = (
    0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7,
)

"""Lanczos approximation of ln(Γ(x)) for x > 0 (reflection formula for x < 0.5)."""
function lgamma_lanczos(x::Float64)::Float64
    if x < 0.5
        return log(π / sin(π * x)) - lgamma_lanczos(1.0 - x)
    end
    x -= 1.0
    a = _LANCZOS_COEF[1]
    t = x + _LANCZOS_G + 0.5
    for i in 1:(_LANCZOS_G + 1)
        a += _LANCZOS_COEF[i+1] / (x + i)
    end
    return 0.5 * log(2π) + (x + 0.5) * log(t) - t + log(a)
end

function _gammp_series(a::Float64, x::Float64)::Float64
    ap = a
    total = 1.0 / a
    δ = total
    for _ in 1:200
        ap += 1.0
        δ *= x / ap
        total += δ
        abs(δ) < abs(total) * 1e-15 && break
    end
    return total * exp(-x + a * log(x) - lgamma_lanczos(a))
end

function _gammq_cf(a::Float64, x::Float64)::Float64
    FPMIN = 1e-300
    b = x + 1.0 - a
    c = 1.0 / FPMIN
    d = 1.0 / b
    h = d
    for i in 1:200
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        abs(d) < FPMIN && (d = FPMIN)
        c = b + an / c
        abs(c) < FPMIN && (c = FPMIN)
        d = 1.0 / d
        δ = d * c
        h *= δ
        abs(δ - 1.0) < 1e-15 && break
    end
    return exp(-x + a * log(x) - lgamma_lanczos(a)) * h
end

"""Regularized lower incomplete gamma P(a,x) = γ(a,x)/Γ(a), any a>0, x>=0."""
function regularized_gamma_p(a::Float64, x::Float64)::Float64
    x <= 0.0 && return 0.0
    return x < a + 1.0 ? _gammp_series(a, x) : 1.0 - _gammq_cf(a, x)
end

# ─────────────────────────────────────────────────────────────────────────
# 2. GUE β=2 Wigner surmise CDF/PDF — идентично gue2_surmise_cdf в оригинале
# ─────────────────────────────────────────────────────────────────────────
"""F₂(s) = erf(2s/√π) − (4s/π)·exp(−4s²/π) = P(1/2, 4s²/π) − (4s/π)·exp(−4s²/π)."""
function gue2_surmise_cdf(s::Float64)::Float64
    s < 0 && return 0.0
    x2 = 4.0 * s^2 / π
    regularized_gamma_p(0.5, x2) - (4.0 * s / π) * exp(-x2)
end

gue2_surmise_pdf(s::Float64) = (32.0 / π^2) * s^2 * exp(-4.0 * s^2 / π)

# ─────────────────────────────────────────────────────────────────────────
# 3. Anderson–Darling statistic — идентична anderson_darling_stat в оригинале
# ─────────────────────────────────────────────────────────────────────────
function anderson_darling_stat(spacings::Vector{Float64}; cdf_func=gue2_surmise_cdf)::Float64
    # Формула — дословно как в оригинале (строки ~1096-1109 ab_cloud_v18.jl):
    # A² = −n − (1/n)·Σ (2i−1)·[ln F(x_(i)) + ln(1−F(x_(n+1-i)))]
    n = length(spacings)
    sorted_sp = sort(spacings)              # копия, не мутирует вход
    s = 0.0
    @inbounds for i in 1:n
        Fi  = clamp(cdf_func(sorted_sp[i]),         1e-300, 1.0 - 1e-16)
        Fni = clamp(cdf_func(sorted_sp[n + 1 - i]), 1e-300, 1.0 - 1e-16)
        s += (2i - 1) * (log(Fi) + log(1.0 - Fni))
    end
    return -Float64(n) - s / n
end

# ─────────────────────────────────────────────────────────────────────────
# 4. Unfolding — БЕЗ ИЗМЕНЕНИЙ, идентично normalized_spacings в оригинале
# ─────────────────────────────────────────────────────────────────────────
"""s_k = (γ_{k+1} − γ_k) · log(γ_k/2π) / 2π — ведущий порядок ρ(t) ≈ log(t/2π)/2π."""
function normalized_spacings(zeta_zeros::Vector{Float64})::Vector{Float64}
    n = length(zeta_zeros) - 1
    out = Vector{Float64}(undef, n)
    @inbounds for k in 1:n
        density = log(zeta_zeros[k] / (2π)) / (2π)
        out[k] = (zeta_zeros[k+1] - zeta_zeros[k]) * density
    end
    return out
end

"""Читает нули дзета из текстового файла (числа через пробел/перенос строки,
как EMBEDDED_ZEROS_50K_STR в оригинале, но из внешнего файла)."""
function load_zeta_zeros(path::AbstractString)::Vector{Float64}
    zeros_ = Float64[]
    for token in split(read(path, String))
        isempty(token) && continue
        startswith(token, '#') && continue
        push!(zeros_, parse(Float64, token))
    end
    sort!(zeros_)
    return zeros_
end

# ─────────────────────────────────────────────────────────────────────────
# 5. ЧЕСТНЫЙ MC null: n_mc независимых i.i.d.-выборок размера n НАПРЯМУЮ из
#    gue2_surmise_cdf — вместо бутстрэпа конечного эмпирического пула.
#
#    Реализовано через inverse-transform sampling с одноразовой таблицей
#    (монотонная сетка + линейная интерполяция) — это влияет только на
#    СКОРОСТЬ генерации null-выборок, не на то, чем они являются: каждая
#    точка по-прежнему i.i.d. ~ gue2_surmise_cdf с точностью интерполяции
#    (~1e-9, как и в собственной RMT_TABLE оригинала). Сама статистика A²
#    всегда считается через ТОЧНУЮ формулу gue2_surmise_cdf, не через таблицу.
# ─────────────────────────────────────────────────────────────────────────
struct InverseCdfTable
    grid_s::Vector{Float64}
    grid_F::Vector{Float64}
end

function build_inverse_table(; smax::Float64=8.0, npts::Int=400_001)::InverseCdfTable
    grid_s = collect(range(0.0, smax; length=npts))
    grid_F = [gue2_surmise_cdf(s) for s in grid_s]
    grid_F[end] = 1.0
    return InverseCdfTable(grid_s, grid_F)
end

"""Линейная интерполяция обратной CDF по таблице (searchsorted + lerp)."""
function sample_gue2!(out::Vector{Float64}, tab::InverseCdfTable, rng::AbstractRNG)
    grid_F, grid_s = tab.grid_F, tab.grid_s
    m = length(grid_F)
    @inbounds for i in eachindex(out)
        u = rand(rng)
        j = searchsortedfirst(grid_F, u)
        if j <= 1
            out[i] = grid_s[1]
        elseif j > m
            out[i] = grid_s[end]
        else
            F0, F1 = grid_F[j-1], grid_F[j]
            t = F1 > F0 ? (u - F0) / (F1 - F0) : 0.0
            out[i] = grid_s[j-1] + t * (grid_s[j] - grid_s[j-1])
        end
    end
    return out
end

"""n_mc реплик A², каждая — честная i.i.d.-выборка размера n из gue2_surmise_cdf."""
function honest_mc_null(n::Int, n_mc::Int, rng::AbstractRNG; tab::InverseCdfTable=build_inverse_table())::Vector{Float64}
    buf = Vector{Float64}(undef, n)
    out = Vector{Float64}(undef, n_mc)
    for k in 1:n_mc
        sample_gue2!(buf, tab, rng)
        out[k] = anderson_darling_stat(buf)
    end
    return out
end

"""MC p-value с add-one (Laplace) сглаживанием: (r+1)/(n_mc+1), r = #{null ≥ data}."""
function mc_pvalue(a2_data::Float64, null::Vector{Float64})
    r = count(x -> x >= a2_data, null)
    n_mc = length(null)
    return (r + 1) / (n_mc + 1), r
end

# ─────────────────────────────────────────────────────────────────────────
# 6. T-скан: падает ли A² по мере отбрасывания низких T? (Objection 2,
#    "low-T convergence" — проверяется напрямую, а не постулируется)
# ─────────────────────────────────────────────────────────────────────────
function t_dependence_scan(zeros_::Vector{Float64}, n_mc::Int, rng::AbstractRNG;
                            fracs=(0.0, 0.2, 0.4, 0.6, 0.8))
    tab = build_inverse_table()
    n_total = length(zeros_)
    rows = NamedTuple[]
    for frac in fracs
        start = floor(Int, frac * n_total) + 1
        sub = zeros_[start:end]
        length(sub) < 200 && continue
        sp = normalized_spacings(sub)
        a2 = anderson_darling_stat(sp)
        null = honest_mc_null(length(sp), n_mc, rng; tab=tab)
        p, r = mc_pvalue(a2, null)
        push!(rows, (frac_dropped=frac, t_min=sub[1], n=length(sp), A2=a2,
                      null_median=median_(null), null_q95=quantile_(null, 0.95),
                      p=p, r=r))
    end
    return rows
end

# минимальные median/quantile без зависимости от Statistics.jl
function median_(v::Vector{Float64})
    s = sort(v); n = length(s)
    return isodd(n) ? s[(n+1)÷2] : (s[n÷2] + s[n÷2+1]) / 2
end
function quantile_(v::Vector{Float64}, q::Float64)
    s = sort(v); n = length(s)
    idx = clamp(round(Int, q * (n - 1)) + 1, 1, n)
    return s[idx]
end

# ─────────────────────────────────────────────────────────────────────────
# 7. main
# ─────────────────────────────────────────────────────────────────────────
function run_test11_honest(zeros_path::AbstractString; n_mc::Int=2000, seed::Int=112,
                            t_scan::Bool=false, t_scan_mc::Int=400)
    zeros_ = load_zeta_zeros(zeros_path)
    @printf("Loaded %d zeta zeros, T in [%.3f, %.3f]\n", length(zeros_), zeros_[1], zeros_[end])

    sp = normalized_spacings(zeros_)
    n = length(sp)
    a2_data = anderson_darling_stat(sp)
    @printf("n spacings = %d\n", n)
    @printf("Data: A² = %.6f (vs exact GUE β=2 CDF)\n", a2_data)

    rng = MersenneTwister(seed)
    tab = build_inverse_table()
    null = honest_mc_null(n, n_mc, rng; tab=tab)
    p, r = mc_pvalue(a2_data, null)

    println()
    println("Честный MC null (n_mc=$n_mc, i.i.d. НАПРЯМУЮ из gue2_surmise_cdf, ",
            "БЕЗ бутстрэпа конечного пула):")
    @printf("  медиана A² = %.6f   (учебное ожидание для корректно заданного\n", median_(null))
    println("                             непрерывного H0: O(1), ~0.5–1)")
    @printf("  95%% квантиль = %.6f  (классическое асимптотическое критическое\n", quantile_(null, 0.95))
    println("                             значение 5% ≈ 2.492)")
    @printf("  MC p-value (add-one) = %.6f  (%d/%d null-реплик ≥ данных)\n", p, r, n_mc)
    verdict = p < 0.05 ? "ОТВЕРГНУТА" : "не отвергнута"
    println("  H0 (GUE β=2 surmise): $verdict при α=0.05")

    if t_scan
        println()
        println("="^70)
        println("T-скан: падает ли A² по мере отбрасывания низких T?")
        println("="^70)
        rows = t_dependence_scan(zeros_, t_scan_mc, rng)
        @printf("%12s %12s %8s %10s %10s %10s %10s\n",
                "frac_dropped", "T_min", "n", "A2", "null_med", "null_q95", "p")
        for row in rows
            @printf("%12.2f %12.2f %8d %10.4f %10.4f %10.4f %10.6f\n",
                    row.frac_dropped, row.t_min, row.n, row.A2,
                    row.null_median, row.null_q95, row.p)
        end
    end

    return (; a2_data, null, p, r, n)
end

# Запуск как скрипта: julia test11_honest.jl [zeros_file] [n_mc] [--t-scan]
if abspath(PROGRAM_FILE) == @__FILE__
    zeros_path = length(ARGS) >= 1 && !startswith(ARGS[1], "--") ? ARGS[1] : "zeta_zeros_50k.txt"
    n_mc = length(ARGS) >= 2 && !startswith(ARGS[2], "--") ? parse(Int, ARGS[2]) : 2000
    t_scan = "--t-scan" in ARGS
    run_test11_honest(zeros_path; n_mc=n_mc, seed=112, t_scan=t_scan)
end
