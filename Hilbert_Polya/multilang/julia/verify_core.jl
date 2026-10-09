# verify_core.jl — Julia-двойник ядра. Запуск: julia verify_core.jl [out]
const G = 7.0
const C = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
           771.32342877765313, -176.61502916214059, 12.507343278686905,
           -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7]

function mod_gamma(re::Float64, u::Float64)::Float64
    zr, zi = re - 1.0, u
    xr, xi = C[1], 0.0
    for i in 2:9
        dr, di = zr + (i-1), zi
        den = dr^2 + di^2
        xr += C[i] * dr / den
        xi -= C[i] * di / den
    end
    tr, ti = zr + G + 0.5, zi
    mt = 0.5 * log(tr^2 + ti^2)
    at = atan(ti, tr)
    pe = (zr + 0.5) * mt - ti * at
    ph = ti * mt + (zr + 0.5) * at
    ar, ai = exp(pe) * cos(ph), exp(pe) * sin(ph)
    e = exp(-tr)
    br, bi = e * cos(-ti), e * sin(-ti)
    c1r, c1i = ar * xr - ai * xi, ar * xi + ai * xr
    d1r, d1i = c1r * br - c1i * bi, c1r * bi + c1i * br
    gr, gi = sqrt(2π) * d1r, sqrt(2π) * d1i
    return sqrt(gr^2 + gi^2)
end

function main()
    out = length(ARGS) > 0 ? ARGS[1] : "verify_control.txt"
    max_res = 0.0
    for u in (0.5, 1.0, 2.0, 3.0)
        ref = sqrt(π / cosh(π * u))
        max_res = max(max_res, abs(mod_gamma(0.5, u) - ref) / ref)
    end
    N = 100000
    spf = zeros(Int, N)
    for i in 2:N
        if spf[i] == 0
            for j in i:i:N
                if spf[j] == 0; spf[j] = i; end
            end
        end
    end
    s = 0.0
    for p in 2:N
        if spf[p] == p
            pk = p
            while pk <= N
                s += log(p) / pk^1.5
                pk *= p
            end
        end
    end
    open(out, "w") do f
        println(f, "gamma_closure_max_res = $(@sprintf("%.3e", max_res))")
        println(f, "lambda_sum_check = $(@sprintf("%.10f", s))")
        println(f, "n_sieve = $N")
    end
    println("julia twin OK: ", max_res, " ", s)
end
main()
