# =============================================================================
# AB-Cloud Verification Suite — canonical kernel v3.0 (Julia)
# =============================================================================
# Objections verified against the frozen golden anchors (CANON_SPEC.md;
# canon: meridian-spectral-observatory, selftest 199/199).
# ab_cloud_verify_en.jl / ab_cloud_verify_ru.jl are thin language pins.
# =============================================================================

# ---------------------------------------------------------------------------
# Data sources (CANON_SPEC §9)
# ---------------------------------------------------------------------------
using Printf
using Printf: @printf

const SOURCES = [
    ("50k",      "zeta_zeros_50000.txt",          13661),
    ("50k_full", "zeta_zeros_50000_embedded.txt", 50000),
    ("500k",     "zeta_zeros_500k_odlyzko.txt",   500000),
    ("2M",       "zeta_zeros_2M_odlyzko.txt",     2001052),
    ("highT",    "zeta_zeros_highT_blocks.txt",   30000),
    ("csv",      "zeta_zeros_50000.csv",          13661),
    ("zeros6",   "zeros6.txt",                    2001052),
]

function resolve_source(count::Int, source::String)::Tuple{String,String}
    source == "2M_gz" && error("source '2M_gz' is not supported in the Julia port; use '2M'")
    if source != "auto"
        for (n, f, _) in SOURCES
            n == source && return (n, f)
        end
        error("unknown source: $source")
    end
    best = nothing
    for s in SOURCES
        if s[3] >= count && (best === nothing || s[3] < best[3])
            best = s
        end
    end
    best === nothing && error("no data source available for $count zeros")
    return (best[1], best[2])
end

function load_zeros(data_dir::String, count::Int, source::String)::Vector{Float64}
    sname, fname = resolve_source(count, source)
    path = joinpath(data_dir, fname)
    println("  Data file: $path (source '$sname')")
    zeros = Float64[]
    block_offset = 0.0
    for line in eachline(path)
        t = strip(line)
        isempty(t) && continue
        if startswith(t, "#")
            if sname == "highT"
                p = findfirst("offset=", t)
                if p !== nothing
                    block_offset = tryparse(Float64, strip(t[(p[end]+1):end]))
                    block_offset === nothing && (block_offset = 0.0)
                end
            end
            continue
        end
        v = if sname == "csv"
            parts = split(t, ',')
            length(parts) >= 2 ? tryparse(Float64, strip(parts[2])) : nothing
        else
            tryparse(Float64, t)
        end
        v === nothing && continue
        val = v + block_offset
        val > 0.0 || continue
        push!(zeros, val)
        count > 0 && length(zeros) >= count && break
    end
    sort!(zeros)
    isempty(zeros) && error("No valid zeros loaded")
    return zeros
end

# ---------------------------------------------------------------------------
# Canonical math kernel (CANON_SPEC §1–§6)
# ---------------------------------------------------------------------------
function lambert_w(x::Float64)::Float64
    x <= 0.0 && return 0.0
    w = log(x)
    w < 0.0 && (w = x)   # W(x) ~ x for 0<x<1; avoids the w=-1 flat point
    for _ in 1:50
        ew = exp(w)
        fp = ew * (w + 1.0)
        abs(fp) < 1e-30 && break
        delta = (w * ew - x) / fp
        w -= delta
        abs(delta) < 1e-14 * (1.0 + abs(w)) && break
    end
    return w
end

"""gram_point: solution of θ(t) = πk (CANON_SPEC §2): seed + 8 Newton iterations."""
function gram_point(k::Int)::Float64
    k <= 0 && return 0.0
    kf = Float64(k)
    t = 2.0 * π * kf / lambert_w(kf / ℯ)
    for _ in 1:8
        arg = t / (2.0 * π)
        arg <= 0.0 && break
        theta  = 0.5 * t * log(arg) - 0.5 * t - π / 8.0 + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t^3)
        dtheta = 0.5 * log(arg) - 1.0 / (48.0 * t^2) - 21.0 / (5760.0 * t^4)
        abs(dtheta) < 1e-30 && break
        t -= (theta - kf * π) / dtheta
    end
    return t
end

# erf — Julia Base has none; series for |x| < 2.2, Lentz continued fraction
# for erfc beyond (DLMF 7.9.1). Accuracy ~1e-15 (validated by the anchors).
function my_erf(x::Float64)::Float64
    ax = abs(x)
    v = if ax < 2.2
        term = ax
        s = ax
        x2 = ax * ax
        for k in 1:200
            term *= -x2 / k
            add = term / (2.0 * k + 1.0)
            s += add
            abs(add) < 1e-18 * abs(s) && break
        end
        2.0 / sqrt(π) * s
    else
        1.0 - my_erfc(ax)
    end
    return x >= 0.0 ? v : -v
end

function my_erfc(z::Float64)::Float64
    # G = z + (1/2)/(z + 1/(z + (3/2)/(z + ...))) via modified Lentz
    f = z; c = z; d = 0.0
    for k in 1:200
        a = k / 2.0
        d = z + a * d
        d == 0.0 && (d = 1e-300)
        c = z + a / c
        c == 0.0 && (c = 1e-300)
        d = 1.0 / d
        delta = c * d
        f *= delta
        abs(delta - 1.0) < 1e-17 && break
    end
    return exp(-z * z) / (sqrt(π) * f)
end

const GUE_TN = 32768
const GUE_SMAX = 5.0
const GUE_TABLE = [begin
    s = i * GUE_SMAX / (GUE_TN - 1)
    my_erf(2.0 * s / sqrt(π)) - (4.0 * s / π) * exp(-4.0 * s^2 / π)
end for i in 0:(GUE_TN-1)]

gue_exact(s::Float64) = s <= 0.0 ? 0.0 : my_erf(2.0 * s / sqrt(π)) - (4.0 * s / π) * exp(-4.0 * s^2 / π)

"""GUE (β=2) Wigner surmise CDF via the canonical 32768-point table (§5)."""
function gue_cdf(s::Float64)::Float64
    s <= 0.0 && return 0.0
    s >= GUE_SMAX && return gue_exact(s)
    x = s * (GUE_TN - 1) / GUE_SMAX
    i = floor(Int, x)
    (i < 0 || i >= GUE_TN - 1) && return gue_exact(s)
    t = x - i
    return (1.0 - t) * GUE_TABLE[i+1] + t * GUE_TABLE[i+2]
end

function compute_bn(zeros::Vector{Float64}, N::Int)::Float64
    (N <= 0 || N > length(zeros)) && return NaN
    s = 0.0
    for k in 1:N
        s += abs(zeros[k] - gram_point(k))
    end
    return s / N
end

function compute_bn_offset(zeros::Vector{Float64}, N::Int, offset::Int)::Float64
    (N <= 0 || offset + N > length(zeros)) && return NaN
    s = 0.0
    for k in 1:N
        s += abs(zeros[k] - gram_point(offset + k))
    end
    return s / N
end

function compute_spacings(zeros::Vector{Float64})::Vector{Float64}
    sp = Float64[]
    for k in 1:(length(zeros)-1)
        zeros[k] <= 0.0 && continue
        push!(sp, (zeros[k+1] - zeros[k]) * log(zeros[k] / (2.0 * π)) / (2.0 * π))
    end
    return sp
end

function ks_asymptotic_pvalue(lam::Float64)::Float64
    lam <= 0.0 && return 1.0
    v = 0.0
    if lam < 0.6
        s2 = 0.0
        for k in 1:1000
            term2 = exp(-(((2.0 * k - 1.0)^2) * π^2) / (8.0 * lam^2))
            s2 += term2
            term2 < 1e-18 && break
        end
        v = 1.0 - sqrt(2.0 * π) / lam * s2
    else
        s = 0.0
        sign = 1.0
        for k in 1:100
            term = sign * exp(-2.0 * k^2 * lam^2)
            s += term
            sign = -sign
            abs(term) < 1e-18 && break
        end
        v = 2.0 * s
    end
    return clamp(v, 0.0, 1.0)
end

function ks_test_dp!(sp::Vector{Float64})::Tuple{Float64,Float64}
    sort!(sp)
    n = Float64(length(sp))
    D = 0.0
    for i in 1:length(sp)
        F = gue_cdf(sp[i])
        D = max(D, abs(i / n - F), abs((i - 1) / n - F))
    end
    lam = (sqrt(n) + 0.12 + 0.11 / sqrt(n)) * D
    return (D, ks_asymptotic_pvalue(lam))
end

function cvm_test(sp::Vector{Float64})::Float64
    s = sort(sp)
    n = Float64(length(s))
    isempty(s) && return 0.0
    W2 = 0.0
    for i in 1:length(s)
        d = gue_cdf(s[i]) - (2.0 * i - 1.0) / (2.0 * n)
        W2 += d * d
    end
    return W2 + 1.0 / (12.0 * n)
end

function ad_stat(sp::Vector{Float64})::Float64
    s = sort(sp)
    length(s) < 2 && return NaN
    n = Float64(length(s))
    acc = 0.0
    for i in 1:length(s)
        Fi  = clamp(gue_cdf(s[i]), 1e-300, 1.0 - 1e-16)
        Fni = clamp(gue_cdf(s[end - i + 1]), 1e-300, 1.0 - 1e-16)
        acc += (2.0 * i - 1.0) * (log(Fi) + log(1.0 - Fni))
    end
    return -n - acc / n
end

function mean_ratio(zeros::Vector{Float64})::Tuple{Float64,Int}
    length(zeros) < 3 && return (NaN, 0)
    acc = 0.0
    cnt = 0
    for i in 1:(length(zeros)-2)
        a = zeros[i+1] - zeros[i]
        b = zeros[i+2] - zeros[i+1]
        m = max(a, b)
        a == 0.0 && b == 0.0 && continue
        acc += min(a, b) / m
        cnt += 1
    end
    cnt == 0 && return (NaN, 0)
    return (acc / cnt, cnt)
end

struct Linreg
    slope::Float64
    intercept::Float64
    se::Float64
    r2::Float64
end

function linreg(x::Vector{Float64}, y::Vector{Float64})::Linreg
    n = Float64(length(x))
    sx = sum(x); sy = sum(y)
    sxx = sum(abs2, x); sxy = sum(x .* y); syy = sum(abs2, y)
    den = n * sxx - sx * sx
    abs(den) < 1e-30 && return Linreg(0.0, 0.0, 0.0, 0.0)
    slope = (n * sxy - sx * sy) / den
    intercept = (sy - slope * sx) / n
    ss_tot = syy - sy^2 / n
    ss_res = sum(abs2, y[i] - (slope * x[i] + intercept) for i in eachindex(x))
    r2 = ss_tot > 0.0 ? 1.0 - ss_res / ss_tot : 0.0
    se = length(x) > 2 && den > 0.0 ? sqrt((ss_res / (n - 2.0)) * n / den) : 0.0
    return Linreg(slope, intercept, se, r2)
end

# ---------------------------------------------------------------------------
# Objections (CANON_SPEC §7)
# ---------------------------------------------------------------------------
struct Obj1Res
    ns::Vector{Int}
    bn::Vector{Float64}
    converging::Bool
    has_fit::Bool
    fit_a::Float64
    fit_s::Float64
    fit_r2::Float64
end

function run_objection1(zeros::Vector{Float64})::Obj1Res
    ns = filter(n -> n <= length(zeros), [100, 500, 1000, 5000, 10000, 50000])
    isempty(ns) && (ns = [min(length(zeros), 100)])
    bn = [compute_bn(zeros, n) for n in ns]
    converging = all(bn[i] < bn[i-1] for i in 2:length(bn))
    has_fit = false; fit_a = 0.0; fit_s = 0.0; fit_r2 = 0.0
    if length(ns) >= 3
        lx = [log(Float64(n)) for (n, b) in zip(ns, bn) if n > 1 && b > 0.0]
        ly = [log(b) for (n, b) in zip(ns, bn) if n > 1 && b > 0.0]
        if length(lx) >= 3
            lr = linreg(lx, ly)
            has_fit = true; fit_a = exp(lr.intercept); fit_s = -lr.slope; fit_r2 = lr.r2
        end
    end
    return Obj1Res(ns, bn, converging, has_fit, fit_a, fit_s, fit_r2)
end

struct Obj2Res
    n::Int
    mean::Float64
    var::Float64
    D::Float64
    p::Float64
    W2::Float64
    A2::Float64
    r::Float64
    nr::Int
    rejected::Bool
end

function run_objection2(zeros::Vector{Float64})::Obj2Res
    sp = compute_spacings(zeros)
    length(sp) < 2 && return Obj2Res(length(sp), NaN, NaN, NaN, NaN, NaN, NaN, NaN, 0, false)
    m = sum(sp) / length(sp)
    v = sum(abs2, s - m for s in sp) / (length(sp) - 1)
    D, p = ks_test_dp!(sp)
    r, nr = mean_ratio(zeros)
    return Obj2Res(length(sp), m, v, D, p, cvm_test(sp), ad_stat(sp), r, nr, p < 0.05)
end

struct Obj3Res
    ns::Vector{Int}
    slope::Float64
    intercept::Float64
    r2::Float64
    cilo::Float64
    cihi::Float64
    ok::Bool
end

function run_objection3(zeros::Vector{Float64})::Obj3Res
    maxz = length(zeros)
    ns = Int[]
    n = 50
    while n <= maxz
        push!(ns, n)
        n *= 2
    end
    (isempty(ns) || ns[end] != maxz) && maxz > 100 && push!(ns, maxz)
    lx = Float64[]; ly = Float64[]
    for n in ns
        b = compute_bn(zeros, n)
        b > 0.0 || continue
        push!(lx, log(Float64(n)))
        push!(ly, log(b))
    end
    length(lx) < 3 && return Obj3Res(ns, NaN, NaN, NaN, NaN, NaN, false)
    lr = linreg(lx, ly)
    return Obj3Res(ns, lr.slope, lr.intercept, lr.r2,
                   lr.slope - 1.96 * lr.se, lr.slope + 1.96 * lr.se,
                   abs(lr.slope + 0.5) < 0.1)
end

# ---------------------------------------------------------------------------
# Self-check (CANON_SPEC §8)
# ---------------------------------------------------------------------------
struct SCRow
    name::String
    skip::Bool
    ok::Bool
    got::Float64
    exp::Float64
    delta::Float64
end

function selfcheck(zeros::Vector{Float64})::Tuple{Vector{SCRow},Int,Int}
    rows = SCRow[]
    npass = 0; nfail = 0
    function add(name, got, exp, tol, rel)
        d = abs(got - exp) / (rel ? abs(exp) : 1.0)
        ok = !isnan(got) && d <= tol
        push!(rows, SCRow(name, false, ok, got, exp, d))
        ok ? (npass += 1) : (nfail += 1)
    end
    skips(name, need) = push!(rows, SCRow(name, true, false, 0.0, 0.0, 0.0))

    for (x, e) in ((0.5, 0.35173371124919584), (1.0, 0.5671432904097838),
                   (3.7, 1.1599531786120223), (10.0, 1.7455280027406992),
                   (271.8, 4.17576816800275), (12345.6, 7.417247034540566))
        add("lambert_w($x)", lambert_w(x), e, 1e-12, true)
    end
    for (n, e) in ((1, 23.17028270133466), (2, 27.670182217848343),
                   (3, 31.71797995477886), (10, 54.67523744685398),
                   (100, 238.58259051450293), (1000, 1421.25638903275),
                   (10000, 9878.910118894457), (50000, 40434.6952780045))
        add("gram_point(n=$n)", gram_point(n), e, 1e-6, false)
    end
    for (n, e) in ((100, 3.3321638710140165), (500, 2.3912304957476382),
                   (1000, 2.1072522951855435), (5000, 1.6299485869022874),
                   (10000, 1.4794053414584762), (50000, 1.2125526772588608))
        if n <= length(zeros)
            add("bN(N=$n)", compute_bn(zeros, n), e, 1e-6, false)
        else
            skips("bN(N=$n)", n)
        end
    end
    if length(zeros) >= 1500
        add("bN(N=1000,off=500)", compute_bn_offset(zeros, 1000, 500), 624.6201618180231, 1e-6, false)
    else
        skips("bN(N=1000,off=500)", 1500)
    end
    if length(zeros) >= 50000
        z5 = zeros[1:50000]
        sp = compute_spacings(z5)
        m = sum(sp) / length(sp)
        v = sum(abs2, s - m for s in sp) / (length(sp) - 1)
        D, p = ks_test_dp!(sp)
        add("spacings.mean", m, 0.999976001221201, 1e-9, false)
        add("spacings.var", v, 0.1590654827835423, 1e-9, false)
        add("ks_zeros.D", D, 0.021619337032982328, 1e-9, false)
        add("ks_zeros.p", p, 9.567870399361496e-21, 1e-6, true)
        add("cvm_zeros.W2", cvm_test(sp), 8.177703317829403, 1e-9, true)
        add("ad_zeros.A2", ad_stat(sp), 61.49242624209728, 1e-9, true)
        r, _ = mean_ratio(z5)
        add("rmean_zeros.r", r, 0.6118798907208398, 1e-9, false)
    else
        for nm in ("spacings.mean/var", "ks_zeros.D/p", "cvm_zeros.W2", "ad_zeros.A2", "rmean_zeros.r")
            skips(nm, 50000)
        end
    end
    return (rows, npass, nfail)
end

# ---------------------------------------------------------------------------
# Rendering (bilingual; thin _en/_ru wrappers pin the language)
# ---------------------------------------------------------------------------
function render_obj1(r::Obj1Res, lang::Symbol)::String
    io = IOBuffer()
    if lang == :ru
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  ВОЗРАЖЕНИЕ 1: Сходимость b(N)")
        println(io, "  b(N) = (1/N) · Σ|γ_k − γ̃_k|, точки Грама: θ(t) = πk (Ньютон)")
        println(io, "═══════════════════════════════════════════════════")
    else
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  OBJECTION 1: b(N) Convergence")
        println(io, "  b(N) = (1/N) · Σ|γ_k − γ̃_k|, Gram points: θ(t) = πk (Newton)")
        println(io, "═══════════════════════════════════════════════════")
    end
    lg(r, i) = r.bn[i] > 0.0 ? log10(r.bn[i]) : -999.0
    for i in eachindex(r.ns)
        @printf(io, "  %10d %15.8f %15.4f\n", r.ns[i], r.bn[i], lg(r, i))
    end
    if r.has_fit
        if lang == :ru
            @printf(io, "\n  Эмпирический закон:  b(N) ~ %.4f * N^(-%.4f)   (R^2 = %.4f)\n", r.fit_a, r.fit_s, r.fit_r2)
        else
            @printf(io, "\n  Empirical law:  b(N) ~ %.4f * N^(-%.4f)   (R^2 = %.4f)\n", r.fit_a, r.fit_s, r.fit_r2)
        end
    end
    if r.converging
        if lang == :ru
            println(io, "\nРезультат: b(N) сходится с ростом N. OK")
            println(io, "  b(N) монотонно убывает по таблице — сходимость подтверждена на доступном диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N)).")
        else
            println(io, "\nResult: b(N) converging as N increases. OK")
            println(io, "  b(N) decreases monotonically over the table — convergence confirmed on the accessible range. The decay is EMPIRICAL, not O(1/sqrt(N)).")
        end
    else
        lang == :ru ? println(io, "\nРезультат: b(N) НЕ сходится с ростом N. WARN") :
                      println(io, "\nResult: b(N) NOT converging as N increases. WARN")
    end
    return String(take!(io))
end

function render_obj2(r::Obj2Res, lang::Symbol)::String
    io = IOBuffer()
    if lang == :ru
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  ВОЗРАЖЕНИЕ 2: Статистика интервалов GUE")
        println(io, "  GUE (β=2) сурьмида через каноническую CDF-таблицу (32768 точек)")
        println(io, "═══════════════════════════════════════════════════")
    else
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  OBJECTION 2: GUE Spacing Statistics")
        println(io, "  GUE (β=2) Wigner surmise via the canonical 32768-point CDF table")
        println(io, "═══════════════════════════════════════════════════")
    end
    r.n < 2 && return String(take!(io)) * (lang == :ru ? "ПРЕДУПРЕЖДЕНИЕ: недостаточно интервалов.\n" : "WARNING: not enough spacings.\n")
    @printf(io, "  Spacing mean: %.9f  var: %.9f  (n = %d)\n", r.mean, r.var, r.n)
    @printf(io, "  Kolmogorov-Smirnov:  D = %.6f,  p-value = %.3e\n", r.D, r.p)
    @printf(io, "  Cramér-von Mises:    W^2 = %.6f\n", r.W2)
    @printf(io, "  Anderson-Darling:   A^2 = %.6f\n", r.A2)
    @printf(io, "  <r> (adjacent-ratio): %.6f  (n = %d, GUE surmise ~ 0.5992)\n", r.r, r.nr)
    if r.rejected
        lang == :ru ? println(io, "\nРезультат: KS-тест ОТВЕРГНУТ при alpha=0.05.") :
                      println(io, "\nResult: KS test REJECTED at alpha=0.05.")
        lang == :ru ?
            println(io, "  Примечание: при больших n точная GUE-сурьмида формально отвергается — это известные поправки конечных T у нулей ζ, а не дефект данных (среднее ~ 1 подтверждает развёртку; якоря golden).") :
            println(io, "  Note: at large n the exact GUE surmise is formally rejected — the known finite-T corrections of the zeta zeros, not a data artifact (mean ~ 1 validates the unfolding; golden-anchored).")
    else
        lang == :ru ? println(io, "\nРезультат: KS-тест НЕ ОТВЕРГНУТ при alpha=0.05.") :
                      println(io, "\nResult: KS test NOT REJECTED at alpha=0.05.")
    end
    return String(take!(io))
end

function render_obj3(r::Obj3Res, lang::Symbol)::String
    io = IOBuffer()
    if lang == :ru
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  ВОЗРАЖЕНИЕ 3: Скорость убывания при больших T")
        println(io, "═══════════════════════════════════════════════════")
    else
        println(io, "\n═══════════════════════════════════════════════════")
        println(io, "  OBJECTION 3: Large-T Decay Rate")
        println(io, "═══════════════════════════════════════════════════")
    end
    isnan(r.slope) && return String(take!(io)) *
        (lang == :ru ? "ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии.\n" : "WARNING: Insufficient data points for regression.\n")
    @printf(io, "  Slope     = %+.6f  (expected: -0.5)\n", r.slope)
    @printf(io, "  Intercept = %+.6f\n", r.intercept)
    @printf(io, "  R^2       = %.6f\n", r.r2)
    @printf(io, "  95%% CI for slope: [%.4f, %.4f]\n", r.cilo, r.cihi)
    if r.ok
        @printf(io, "\nResult: Fitted slope = %+.4f, expected = -0.500. OK\n", r.slope)
    else
        @printf(io, "\nResult: Fitted slope = %+.4f, expected = -0.500. WARN: slope deviates from -0.5 (decay is empirical)\n", r.slope)
    end
    return String(take!(io))
end

function render_selfcheck(rows::Vector{SCRow}, npass::Int, nfail::Int, lang::Symbol)::String
    io = IOBuffer()
    lang == :ru ?
        println(io, "\n=== Само-проверка golden — замороженные якоря (канон: meridian-spectral-observatory, selftest 199/199) ===") :
        println(io, "\n=== Golden self-check — frozen anchors (canon: meridian-spectral-observatory, selftest 199/199) ===")
    for r in rows
        r.skip && (lang == :ru ? @printf(io, "  %-24s ПРОПУСК\n", r.name) :
                                  @printf(io, "  %-24s SKIP\n", r.name); continue)
        st = r.ok ? (lang == :ru ? "ПРОЙДЕНО" : "PASS") : (lang == :ru ? "СБОЙ" : "FAIL")
        @printf(io, "  %-24s %s  computed = %.12g, expected = %.12g, Δ = %.3e\n", r.name, st, r.got, r.exp, r.delta)
    end
    lang == :ru ? @printf(io, "  Само-проверка: %d пройдено, %d провалено\n", npass, nfail) :
                  @printf(io, "  Self-check: %d passed, %d failed\n", npass, nfail)
    return String(take!(io))
end

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
function run_suite(; zeros::Int=50000, source::String="auto", objection::String="all",
                    lang::Symbol=:en, data_dir::String="../data", selfcheck_on::Bool=true)
    println()
    lang == :ru ? println("  ║   AB-CLOUD ПРОВЕРКА — ГИПОТЕЗА РИМАНА        ║") :
                  println("  ║   AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS  ║")
    println()
    gammas = load_zeros(data_dir, zeros, source)
    println("  Zeros loaded: ", length(gammas))
    length(gammas) < 2 && error("need at least 2 zeros")

    sc_fail = -1
    if selfcheck_on
        rows, npass, nfail = selfcheck(gammas)
        print(render_selfcheck(rows, npass, nfail, lang))
        sc_fail = nfail
    end
    (objection == "all" || objection == "1") && print(render_obj1(run_objection1(gammas), lang))
    (objection == "all" || objection == "2") && print(render_obj2(run_objection2(gammas), lang))
    (objection == "all" || objection == "3") && print(render_obj3(run_objection3(gammas), lang))
    println("\n  AB-Cloud Verification Suite — complete.\n")
    return sc_fail
end

function main()
    args = ARGS
    zeros = 50000; source = "auto"; objection = "all"; lang = :en
    data_dir = "../data"; selfcheck_on = true
    i = 1
    while i <= length(args)
        a = args[i]
        if a == "--zeros" && i < length(args); i += 1; zeros = parse(Int, args[i])
        elseif a == "--source" && i < length(args); i += 1; source = args[i]
        elseif a == "--objection" && i < length(args); i += 1; objection = args[i]
        elseif a == "--lang" && i < length(args); i += 1; lang = args[i] == "ru" ? :ru : :en
        elseif a == "--data-dir" && i < length(args); i += 1; data_dir = args[i]
        elseif a == "--no-selfcheck"; selfcheck_on = false
        end
        i += 1
    end
    sc_fail = run_suite(zeros=zeros, source=source, objection=objection,
                        lang=lang, data_dir=data_dir, selfcheck_on=selfcheck_on)
    sc_fail > 0 && exit(1)
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
