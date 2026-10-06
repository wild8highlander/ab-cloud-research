# =============================================================================
# AB-Cloud Dirac Laboratory — Julia cross-verification, EXTENSIONS II (D11) — v1.2
# Independent re-implementation of the Berry–Keating / Connes conjugation-action
# test. LinearAlgebra only (dense; N_u = 256 log-grid + the 2000-zero data file).
#
# Conventions match code/dirac_lab_extensions2.py exactly:
#   u-grid u_j = j·Λ/N_u, j = 0..N_u−1 (periodic), Λ = ln(t_med/2πe)
#   unitary DFT F_{jm} = exp(−2πi·q_m·j/N_u)/√N_u, q = fftfreq integer modes
#   Ĥ = F† diag(2πq/Λ) F  → spectrum EXACTLY arithmetic E_m = 2πm/Λ
#   U(u₀) = e^{iu₀Ĥ} = F† diag(e^{iu₀E}) F — the conjugation (dilation) action
#   trace comb Tr U(u₀) = Σ_m e^{iu₀E_m} (Dirichlet kernel, Λ-periodic)
#   staircase N_BK(E) = #{E_m ≤ E} = floor(ΛE/2π) + N/2 + 1 (incl. the m = 0 mode)
#   density residual r_n = n − (t_n/2π)·ln(t_n/2πe)   (RvM: 7/8 + S(t))
#   recognition identity frac(t/δ) ≡ frac((t/2π)ln(t/2π)), δ = 2π/ln(t/2π)
# =============================================================================
using LinearAlgebra

const N_U = 256

# ---- exact spectral Berry–Keating operator ----
function bk_operator(N::Int, Λ::Float64)
    q = zeros(N)
    for m in 1:N
        k = m - 1
        q[m] = k < N / 2 ? k : k - N          # fftfreq integer modes
    end
    E = 2π .* q ./ Λ
    j = 0:(N-1)
    F = exp.(-2π * im .* (j .* permutedims(q)) ./ N) ./ sqrt(N)
    H = F' * (E .* F)
    H = (H + H') / 2
    U(u0::Float64) = F' * (exp.(1im .* u0 .* E) .* F)
    return H, U, E
end

function comb_closed(u0::Float64, Λ::Float64, N::Int)
    s = 0.0 + 0.0im
    for k in 0:(N-1)
        s += exp(1im * u0 * 2π * (k - N / 2) / Λ)
    end
    return s
end

# ---- ζ-zero data (same file as the Python suite) ----
function load_zeros(path::String, n::Int)
    zs = Float64[]
    for line in eachline(path)
        s = strip(line)
        if !isempty(s) && !startswith(s, "#")
            push!(zs, parse(Float64, s))
        end
    end
    return zs[1:min(n, length(zs))]
end

# ---- main ----
zs = load_zeros(joinpath(@__DIR__, "..", "data", "zeta_zeros_2000.txt"), 2000)
tmed = sort(zs)[length(zs) ÷ 2]
Λ = log(tmed / (2π * ℯ))
println("Julia cross-check (extensions II D11): N_u = $N_U, zeros = $(length(zs)), Λ = $(round(Λ, digits=6))")

H, U, E = bk_operator(N_U, Λ)
w = eigvals(Hermitian(H))
dev_spec = maximum(abs.(w .- sort(E)))

U1, U2 = U(0.31), U(0.17)
dev_sg  = maximum(abs.(U1 * U2 - U(0.48)))
dev_un  = maximum(abs.(U1' * U1 - I(N_U)))

u0 = 0.37 * Λ
dev_comb = abs(tr(U(u0)) - comb_closed(u0, Λ, N_U))
dev_per  = abs(tr(U(u0 + Λ)) - tr(U(u0))) / max(abs(tr(U(u0))), 1.0)

stair_ok = true
for Ep in range(0.13, 0.9 * maximum(abs.(E)); length=24)
    nbk = count(w .<= Ep)
    nfm = floor(Int, Λ * Ep / (2π)) + N_U ÷ 2 + 1
    global stair_ok &= (nbk == nfm)
end

# density residuals + recognition identity on the real zeros
nidx = 1:length(zs)
resid = nidx .- (zs ./ (2π)) .* log.(zs ./ (2π * ℯ))
r_mean, r_max = sum(resid) / length(resid), maximum(abs.(resid))
frac(x) = x - floor(x)
circ(x) = min(abs(x), abs(1 - abs(x)))
d_recog = maximum(circ.(frac.(zs ./ (2π ./ log.(zs ./ (2π)))) .-
                        frac.((zs ./ (2π)) .* log.(zs ./ (2π)))))

println()
println("[D11a] spectrum dev    = $(round(dev_spec, sigdigits=2))")
println("[D11a] semigroup dev   = $(round(dev_sg, sigdigits=2))   unitarity dev = $(round(dev_un, sigdigits=2))")
println("[D11a] trace comb dev  = $(round(dev_comb, sigdigits=2))   periodicity rel = $(round(dev_per, sigdigits=2))")
println("[D11a] staircase exact = $stair_ok")
println("[D11a] density: mean r = $(round(r_mean, sigdigits=5))   max|r| = $(round(r_max, sigdigits=3))")
println("[D11b] recognition max circle dist = $(round(d_recog, sigdigits=2))")

ok_spec  = dev_spec < 1e-11
ok_alg   = (dev_sg < 1e-11) && (dev_un < 1e-11)
ok_comb  = (dev_comb < 1e-11) && (dev_per < 1e-11)
ok_dens  = (1.10 <= r_mean <= 1.65) && (r_max <= 2.3)
ok_recog = d_recog < 1e-10

println()
println("CROSS-CHECK VERDICTS (Julia, extensions II D11)")
println("  exact arithmetic spectrum:            ", ok_spec  ? "PASS" : "FAIL")
println("  conjugation algebra (sg + unitary):   ", ok_alg   ? "PASS" : "FAIL")
println("  Dirichlet trace comb + Λ-periodicity: ", ok_comb  ? "PASS" : "FAIL")
println("  staircase integer identity:           ", stair_ok ? "PASS" : "FAIL")
println("  BK density on real zeros:             ", ok_dens  ? "PASS" : "FAIL")
println("  recognition identity (mod 1):         ", ok_recog ? "PASS" : "FAIL")
allok = ok_spec && ok_alg && ok_comb && stair_ok && ok_dens && ok_recog
println("  → ", allok ? "ALL PASS" : "MISMATCH — investigate")
exit(allok ? 0 : 1)
