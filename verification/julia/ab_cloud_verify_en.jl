#!/usr/bin/env julia
# =============================================================================
# AB-CLOUD VERIFICATION SUITE — ENGLISH
# Idiomatic Julia · Type Annotations · Efficient
# =============================================================================
# Three objections against the Riemann Hypothesis:
#   Objection 1: b(N) → 0?  (Gram point deviation convergence)
#   Objection 2: GUE spacing KS test (level spacing distribution)
#   Objection 3: Large-T decay slope ≈ -0.5
# =============================================================================

using Printf

const PI::Float64     = 3.14159265358979323846
const TWO_PI::Float64 = 6.28318530717958647693

# --- Load zeros ---
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
            line = strip(line); isempty(line) && continue; startswith(line, '#') && continue
            try; v = parse(Float64, line); v > 0.0 && push!(zeros, v); catch; continue; end
        end
    end
    length(zeros) > n_request && resize!(zeros, n_request)
    return zeros
end

# --- Lambert W ---
function lambert_w0(x::Float64)::Float64
    x == 0.0 && return 0.0
    w::Float64 = log(max(x, 1e-30)); w > 0.0 && (w = log(w))
    for _ in 1:50
        ew = exp(w); f = w*ew - x; fp = ew*(w+1.0); fpp = ew*(w+2.0)
        delta = f / (fp - 0.5*f*fpp/fp); w -= delta
        abs(delta) < 1e-15*abs(w) && break
    end
    return w
end

gram_point(n::Int)::Float64 = TWO_PI * lambert_w0(n / exp(1.0))

# --- Objection 1 ---
function objection1(gammas::Vector{Float64})
    N = length(gammas); s = 0.0
    @inbounds for k in 1:N; s += abs(gammas[k] - gram_point(k)); end
    b_n = s / N; pass = b_n < 1.0
    println("\n=====================================================")
    println("  OBJECTION 1: b(N) Convergence")
    println("  b(N) = (1/N) * Sum|gamma_k - gamma~_k|, Gram pts via Lambert W")
    println("=====================================================")
    @printf("    N       = %d\n", N); @printf("    b(N)    = %.8e\n", b_n)
    println("    Pass:   $pass")
    return b_n, pass
end

# --- GUE helpers ---
gue_pdf(s::Float64)::Float64 = (PI*s/2.0) * exp(-PI*s^2/4.0)

function gue_cdf(s::Float64)::Float64
    s ≤ 0.0 && return 0.0
    nsteps = 200; h = s / nsteps; sum_val = 0.0
    for i in 0:nsteps
        x = i * h
        if i == 0 || i == nsteps; sum_val += gue_pdf(x)
        elseif isodd(i); sum_val += 4.0*gue_pdf(x)
        else; sum_val += 2.0*gue_pdf(x); end
    end
    return min(h/3.0*sum_val, 1.0)
end

function kolmogorov_pvalue(d::Float64, n::Float64)::Float64
    z = d*sqrt(n); pval = 0.0
    for k in -10:10; pval += (-1)^k * exp(-2.0*(2k*z+z)^2); end
    return clamp(pval, 0.0, 1.0)
end

# --- Objection 2 ---
function objection2(gammas::Vector{Float64})
    N = length(gammas); m = N - 1
    s = Vector{Float64}(undef, m)
    @inbounds for k in 1:m
        s[k] = (gammas[k+1] - gammas[k]) * log(gammas[k]/TWO_PI) / TWO_PI
    end
    sort!(s)
    ks_stat = 0.0
    @inbounds for k in 1:m
        d_plus = abs(k/m - gue_cdf(s[k])); d_plus > ks_stat && (ks_stat = d_plus)
    end
    ks_pval = kolmogorov_pvalue(ks_stat, Float64(m)); pass = ks_pval > 0.05
    println("\n=====================================================")
    println("  OBJECTION 2: GUE Spacing KS Test")
    println("  s_k = dg_k * log(g_k/2pi) / 2pi,  p(s) = (pi*s/2)*exp(-pi*s^2/4)")
    println("=====================================================")
    @printf("    Spacing count    = %d\n", m)
    @printf("    KS statistic     = %.8e\n", ks_stat)
    @printf("    p-value          = %.8e\n", ks_pval)
    println("    Pass (p>0.05):   $pass")
    return ks_stat, ks_pval, pass
end

# --- Objection 3 ---
function objection3(gammas::Vector{Float64})
    N = length(gammas); i_start = div(N,2)+1; m = N - i_start
    m < 10 && return 0.0, false
    x_mean = 0.0; y_mean = 0.0
    @inbounds for k in i_start:(N-1)
        x_mean += log(gammas[k]); y_mean += log(abs(gammas[k+1]-gammas[k]))
    end
    x_mean /= m; y_mean /= m
    sxx = 0.0; sxy = 0.0
    @inbounds for k in i_start:(N-1)
        xv = log(gammas[k]); yv = log(abs(gammas[k+1]-gammas[k]))
        sxx += (xv-x_mean)^2; sxy += (xv-x_mean)*(yv-y_mean)
    end
    slope = sxy/sxx; dev = abs(slope+0.5); pass = dev < 0.15
    println("\n=====================================================")
    println("  OBJECTION 3: Large-T Decay Slope")
    println("  log|dg_k| ~ slope * log(g_k),  expected slope = -0.5")
    println("=====================================================")
    @printf("    Regression pts  = %d\n", m)
    @printf("    Slope           = %.4f\n", slope)
    @printf("    Deviation       = %.4f\n", dev)
    println("    Pass:           $pass")
    return slope, pass
end

# --- Main ---
function main()
    n_zeros = 10000; source = "auto"; objection = 0
    args = ARGS; i = 1
    while i ≤ length(args)
        arg = args[i]
        if arg == "--zeros" && i+1 ≤ length(args); i += 1; n_zeros = parse(Int, args[i])
        elseif arg == "--source" && i+1 ≤ length(args); i += 1; source = args[i]
        elseif arg == "--objection" && i+1 ≤ length(args)
            i += 1; objection = args[i] == "all" ? 0 : parse(Int, args[i])
        end; i += 1
    end

    println(); println("  +=================================================+")
    println("  |  AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS     |")
    println("  |  Three objections: b(N), GUE KS, Large-T        |")
    println("  +=================================================+"); println()

    gammas = load_zeros(n_zeros; source=source)
    println("  Zeros loaded: $(length(gammas)) (gamma ordinates)")

    t = time()
    results = []
    if objection == 0 || objection == 1; push!(results, ("1:b(N)", objection1(gammas)...)); end
    if objection == 0 || objection == 2; push!(results, ("2:KS", objection2(gammas)[1], objection2(gammas)[3])); end
    if objection == 0 || objection == 3; push!(results, ("3:slope", objection3(gammas)...)); end

    println("\n  +----------+--------------------+--------+")
    println("  | Obj.     |    Value           | Status |")
    println("  +----------+--------------------+--------+")
    for (lbl, val, p) in results
        @printf("  | %-8s | %16.6e | %-6s |\n", lbl, val, p ? "PASS" : "FAIL")
    end
    println("  +----------+--------------------+--------+")
    @printf("  Total time: %.3f s\n", time() - t)
end

main()
