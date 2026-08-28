#!/usr/bin/env julia
# =============================================================================
# AB-CLOUD VERIFICATION SUITE — BILINGUAL (EN/RU)
# Idiomatic Julia · Type Annotations · Efficient
# =============================================================================
# Проверочный пакет AB-Cloud — билингвальный (английский/русский)
# Три возражения против гипотезы Римана:
#   Возражение 1: b(N) → 0?  (сходимость отклонений Грама)
#   Возражение 2: GUE间距 KS-тест (уровневые промежутки)
#   Возражение 3: Large-T decay slope ≈ -0.5
# =============================================================================

using Printf

# =============================================================================
# Constants
# =============================================================================
const PI::Float64     = 3.14159265358979323846
const TWO_PI::Float64 = 6.28318530717958647693

# =============================================================================
# Data structures
# =============================================================================
struct VerifyResult
    label::String
    value::Float64
    pass::Bool
    detail::String
end

# =============================================================================
# Load zeta zeros with auto-selection
# =============================================================================
function load_zeros(n_request::Int; source::String="auto")::Vector{Float64}
    filepath::String = if source != "auto"
        "../data/$source"
    elseif n_request ≤ 13661
        "../data/zeta_zeros_50000.txt"
    elseif n_request ≤ 500_000
        "../data/zeta_zeros_500k_odlyzko.txt"
    elseif n_request ≤ 2_000_000
        "../data/zeta_zeros_2M_odlyzko.txt"
    else
        "../data/zeros6.txt"
    end

    println("  Data file: $filepath")
    zeros::Vector{Float64} = Float64[]

    open(filepath, "r") do io
        for line in eachline(io)
            line = strip(line)
            isempty(line) && continue
            startswith(line, '#') && continue
            try
                v = parse(Float64, line)
                v > 0.0 && push!(zeros, v)
            catch
                continue
            end
        end
    end

    if length(zeros) > n_request
        resize!(zeros, n_request)
    end

    return zeros
end

# =============================================================================
# Lambert W (principal branch) via Halley's method
# =============================================================================
function lambert_w0(x::Float64)::Float64
    x == 0.0 && return 0.0
    w::Float64 = log(max(x, 1e-30))
    w > 0.0 && (w = log(w))

    for _ in 1:50
        ew::Float64  = exp(w)
        f::Float64   = w * ew - x
        fp::Float64  = ew * (w + 1.0)
        fpp::Float64 = ew * (w + 2.0)
        delta::Float64 = f / (fp - 0.5 * f * fpp / fp)
        w -= delta
        abs(delta) < 1e-15 * abs(w) && break
    end
    return w
end

# =============================================================================
# Gram point: γ̃_n = 2π · W₀(n/e)
# =============================================================================
gram_point(n::Int)::Float64 = TWO_PI * lambert_w0(n / exp(1.0))

# =============================================================================
# Objection 1: b(N) = (1/N) * Σ|γ_k - γ̃_k|
# =============================================================================
function objection1(gammas::Vector{Float64}; lang::Int=0)::VerifyResult
    N::Int = length(gammas)
    s::Float64 = 0.0
    @inbounds for k in 1:N
        s += abs(gammas[k] - gram_point(k))
    end
    b_n::Float64 = s / N
    pass::Bool = b_n < 1.0

    if lang == 2
        println("\n═══════════════════════════════════════════════════")
        println("  ВОЗРАЖЕНИЕ 1: Сходимость b(N)")
        println("  b(N) = (1/N) · Σ|γ_k − γ̃_k|, точки Грама через W Ламберта")
        println("═══════════════════════════════════════════════════")
        @printf("    N       = %d\n", N)
        @printf("    b(N)    = %.8e\n", b_n)
        println("    Пройдено: $pass")
    else
        println("\n═══════════════════════════════════════════════════")
        println("  OBJECTION 1: b(N) Convergence")
        println("  b(N) = (1/N) · Σ|γ_k − γ̃_k|, Gram pts via Lambert W")
        println("═══════════════════════════════════════════════════")
        @printf("    N       = %d\n", N)
        @printf("    b(N)    = %.8e\n", b_n)
        println("    Pass:   $pass")
    end

    return VerifyResult("b(N)", b_n, pass, @sprintf("%.8e", b_n))
end

# =============================================================================
# GUE PDF: p(s) = (πs/2) · exp(-πs²/4)
# =============================================================================
gue_pdf(s::Float64)::Float64 = (PI * s / 2.0) * exp(-PI * s^2 / 4.0)

# =============================================================================
# GUE CDF via Simpson's rule
# =============================================================================
function gue_cdf(s::Float64)::Float64
    s ≤ 0.0 && return 0.0
    nsteps::Int = 200
    h::Float64 = s / nsteps
    sum_val::Float64 = 0.0
    @inbounds for i in 0:nsteps
        x = i * h
        if i == 0 || i == nsteps
            sum_val += gue_pdf(x)
        elseif isodd(i)
            sum_val += 4.0 * gue_pdf(x)
        else
            sum_val += 2.0 * gue_pdf(x)
        end
    end
    return min(h / 3.0 * sum_val, 1.0)
end

# =============================================================================
# Approximate Kolmogorov p-value
# =============================================================================
function kolmogorov_pvalue(d::Float64, n::Float64)::Float64
    z::Float64 = d * sqrt(n)
    pval::Float64 = 0.0
    for k in -10:10
        term::Float64 = exp(-2.0 * (2k * z + z)^2)
        pval += (-1)^k * term
    end
    return clamp(pval, 0.0, 1.0)
end

# =============================================================================
# Objection 2: GUE spacing KS test
# s_k = (γ_{k+1} - γ_k) · log(γ_k/(2π)) / (2π)
# =============================================================================
function objection2(gammas::Vector{Float64}; lang::Int=0)::VerifyResult
    N::Int = length(gammas)
    m::Int = N - 1
    s::Vector{Float64} = Vector{Float64}(undef, m)

    @inbounds for k in 1:m
        log_factor::Float64 = log(gammas[k] / TWO_PI)
        s[k] = (gammas[k+1] - gammas[k]) * log_factor / TWO_PI
    end

    # Sort for empirical CDF
    sort!(s)

    # KS statistic
    ks_stat::Float64 = 0.0
    @inbounds for k in 1:m
        cdf_emp::Float64  = k / m
        cdf_theo::Float64 = gue_cdf(s[k])
        d_plus::Float64   = abs(cdf_emp - cdf_theo)
        d_plus > ks_stat && (ks_stat = d_plus)
    end

    ks_pval::Float64 = kolmogorov_pvalue(ks_stat, Float64(m))
    pass::Bool = ks_pval > 0.05

    if lang == 2
        println("\n═══════════════════════════════════════════════════")
        println("  ВОЗРАЖЕНИЕ 2: GUE-интервалы, KS-критерий")
        println("  s_k = Δγ_k · log(γ_k/2π) / 2π,  p(s) = (πs/2)·e^{-πs²/4}")
        println("═══════════════════════════════════════════════════")
        @printf("    Кол-во интервалов = %d\n", m)
        @printf("    KS-статистика     = %.8e\n", ks_stat)
        @printf("    p-значение        = %.8e\n", ks_pval)
        println("    Пройдено (p>0.05): $pass")
    else
        println("\n═══════════════════════════════════════════════════")
        println("  OBJECTION 2: GUE Spacing KS Test")
        println("  s_k = Δγ_k · log(γ_k/2π) / 2π,  p(s) = (πs/2)·e^{-πs²/4}")
        println("═══════════════════════════════════════════════════")
        @printf("    Spacing count    = %d\n", m)
        @printf("    KS statistic     = %.8e\n", ks_stat)
        @printf("    p-value          = %.8e\n", ks_pval)
        println("    Pass (p>0.05):   $pass")
    end

    return VerifyResult("KS", ks_stat, pass, @sprintf("p=%.4e", ks_pval))
end

# =============================================================================
# Objection 3: Large-T decay slope ≈ -0.5
# Fit log|Δγ_k| vs log(γ_k)
# =============================================================================
function objection3(gammas::Vector{Float64}; lang::Int=0)::VerifyResult
    N::Int = length(gammas)
    i_start::Int = div(N, 2) + 1
    m::Int = N - i_start

    if m < 10
        return VerifyResult("slope", 0.0, false, "insufficient data")
    end

    # Compute means
    x_mean::Float64 = 0.0
    y_mean::Float64 = 0.0
    @inbounds for k in i_start:(N-1)
        x_mean += log(gammas[k])
        y_mean += log(abs(gammas[k+1] - gammas[k]))
    end
    x_mean /= m
    y_mean /= m

    # Linear regression
    sxx::Float64 = 0.0
    sxy::Float64 = 0.0
    @inbounds for k in i_start:(N-1)
        xv::Float64 = log(gammas[k])
        yv::Float64 = log(abs(gammas[k+1] - gammas[k]))
        sxx += (xv - x_mean)^2
        sxy += (xv - x_mean) * (yv - y_mean)
    end
    slope::Float64 = sxy / sxx
    deviation::Float64 = abs(slope + 0.5)
    pass::Bool = deviation < 0.15

    if lang == 2
        println("\n═══════════════════════════════════════════════════")
        println("  ВОЗРАЖЕНИЕ 3: Наклон убывания при больших T")
        println("  log|Δγ_k| ~ slope · log(γ_k),  ожидается slope ≈ -0.5")
        println("═══════════════════════════════════════════════════")
        @printf("    Точек регрессии = %d\n", m)
        @printf("    Наклон (slope)  = %.4f\n", slope)
        @printf("    Отклонение      = %.4f\n", deviation)
        println("    Пройдено:       $pass")
    else
        println("\n═══════════════════════════════════════════════════")
        println("  OBJECTION 3: Large-T Decay Slope")
        println("  log|Δγ_k| ~ slope · log(γ_k),  expected slope ≈ -0.5")
        println("═══════════════════════════════════════════════════")
        @printf("    Regression pts  = %d\n", m)
        @printf("    Slope           = %.4f\n", slope)
        @printf("    Deviation       = %.4f\n", deviation)
        println("    Pass:           $pass")
    end

    return VerifyResult("slope", slope, pass, @sprintf("dev=%.4f", deviation))
end

# =============================================================================
# Summary table
# =============================================================================
function print_summary(results::Vector{VerifyResult}; lang::Int=0)
    if lang == 2
        println("\n  ┌──────────┬────────────────────┬────────┐")
        println("  │ Возраж.  │    Значение        │ Стат.  │")
        println("  ├──────────┼────────────────────┼────────┤")
    else
        println("\n  ┌──────────┬────────────────────┬────────┐")
        println("  │ Obj.     │    Value           │ Status │")
        println("  ├──────────┼────────────────────┼────────┤")
    end

    labels = lang == 2 ? ["1:b(N)", "2:KS", "3:slope"] : ["1:b(N)", "2:KS", "3:slope"]
    for (i, r) in enumerate(results)
        status = r.pass ? "PASS" : "FAIL"
        @printf("  │ %-8s │ %16.6e │ %-6s │\n", labels[i], r.value, status)
    end

    println("  └──────────┴────────────────────┴────────┘")
end

# =============================================================================
# Banner
# =============================================================================
function print_banner(; lang::Int=0)
    println()
    if lang == 2
        println("  ╔═══════════════════════════════════════════════╗")
        println("  ║   AB-CLOUD ПРОВЕРКА — ГИПОТЕЗА РИМАНА        ║")
        println("  ║   Три возражения: b(N), GUE KS, Large-T      ║")
        println("  ╚═══════════════════════════════════════════════╝")
    else
        println("  ╔═══════════════════════════════════════════════╗")
        println("  ║   AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS  ║")
        println("  ║   Three objections: b(N), GUE KS, Large-T     ║")
        println("  ╚═══════════════════════════════════════════════╝")
    end
    println()
end

# =============================================================================
# Main entry point
# =============================================================================
function main()
    # Defaults
    n_zeros::Int    = 10000
    source::String  = "auto"
    objection::Int  = 0   # 0 = all
    lang::Int       = 0   # 0 = bilingual

    # Parse args
    args = ARGS
    i = 1
    while i ≤ length(args)
        arg = args[i]
        if arg == "--zeros" && i+1 ≤ length(args)
            i += 1; n_zeros = parse(Int, args[i])
        elseif arg == "--source" && i+1 ≤ length(args)
            i += 1; source = args[i]
        elseif arg == "--objection" && i+1 ≤ length(args)
            i += 1
            objection = args[i] == "all" ? 0 : parse(Int, args[i])
        elseif arg == "--lang" && i+1 ≤ length(args)
            i += 1
            lang = args[i] == "en" ? 1 : (args[i] == "ru" ? 2 : 0)
        end
        i += 1
    end

    print_banner(lang=lang)

    gammas::Vector{Float64} = load_zeros(n_zeros; source=source)
    N::Int = length(gammas)

    if lang == 2
        println("  Загружено нулей: $N (γ-ординаты)")
    else
        println("  Zeros loaded: $N (gamma ordinates)")
    end

    results::Vector{VerifyResult} = VerifyResult[]

    t_start = time()

    if objection == 0 || objection == 1
        push!(results, objection1(gammas; lang=lang))
    end
    if objection == 0 || objection == 2
        push!(results, objection2(gammas; lang=lang))
    end
    if objection == 0 || objection == 3
        push!(results, objection3(gammas; lang=lang))
    end

    print_summary(results; lang=lang)

    t_end = time()
    if lang == 2
        @printf("  Общее время: %.3f с\n", t_end - t_start)
    else
        @printf("  Total time: %.3f s\n", t_end - t_start)
    end
end

main()
