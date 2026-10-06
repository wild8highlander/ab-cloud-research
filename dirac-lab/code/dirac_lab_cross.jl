#!/usr/bin/env julia
# =============================================================================
# AB-Cloud Dirac Laboratory — Julia cross-verification — v1.0
# Independent re-implementation of the key Dirac-Lab checks (D1, D2, D7, D8)
# against the Python canonical suite (code/dirac_lab.py, seed 96).
#
# Conventions (verbatim parent repository):
#   • Landau gauge Peierls phase on y-hops: 2π·α·x_i (0-based x), x-hops flat.
#   • Monumental atan smooth vortex gauge on VERTICAL bonds, factor 0.5,
#     principal-value atan2, unwrapped coordinate for the torus wrap bond.
#   • ζ→vortex coding: x_k = L·frac(t_k/δ_k), y_k = L·frac(t_k/(2δ_k)),
#     δ_k = 2π/log(t_k/2π), charges (−1)^k, plaquette centers +0.5.
#
# Usage:  julia dirac_lab_cross.jl [path/to/zeta_zeros_2000.txt]
# Output: console verdicts + results/cross_verification_julia.json
# =============================================================================

using LinearAlgebra
using Statistics
using Printf

# minimal dependency-free JSON writer (repo spirit: no external packages)
function json_escape(s::String)
    return replace(s, "\\" => "\\\\", "\"" => "\\\"")
end

function to_json(x::Float64)
    isnan(x) && return "NaN"
    isinf(x) && return x > 0 ? "Infinity" : "-Infinity"
    return @sprintf("%.17g", x)
end
to_json(x::Int) = string(x)
to_json(x::Bool) = x ? "true" : "false"
to_json(x::String) = "\"" * json_escape(x) * "\""

to_json(x::Vector) = "[" * join(to_json.(x), ",") * "]"

function to_json(d::Dict)
    parts = String[]
    for (k, v) in d
        push!(parts, "\"" * json_escape(string(k)) * "\":" * to_json(v))
    end
    return "{" * join(parts, ",") * "}"
end

# ─── ζ-zero-coded vortices (must match Python zeta_coded_vortices) ───────────
function zeta_coded_vortices(zeros::Vector{Float64}, L::Int, nv::Int)
    vortices = Tuple{Float64,Float64,Float64}[]
    for k in 1:nv
        t = zeros[mod1(k, length(zeros))]
        delta = 2π / log(t / (2π))
        x = L * ((t / delta) % 1.0)
        y = L * ((t / (2delta)) % 1.0)
        q = isodd(k) ? 1.0 : -1.0          # k is 1-based here: (−1)^k → +,−,…
        # Python: q = +1 if k % 2 == 0 (0-based) → 1-based odd k ↔ python even
        push!(vortices, (x + 0.5, y + 0.5, q))
    end
    return vortices
end

# ─── Hamiltonian builder (parent conventions) ────────────────────────────────
function build_hamiltonian(L::Int, alpha::Float64; vortices=Tuple{Float64,Float64,Float64}[])
    N = L * L
    H = zeros(ComplexF64, N, N)
    for x in 0:L-1, y in 0:L-1
        i = x * L + y + 1                      # 1-based
        # x-hop (flat), torus wrap
        j = ((x + 1) % L) * L + y + 1
        H[i, j] += 1.0
        H[j, i] += 1.0
        # y-hop: Landau phase 2πα·x + monumental atan vortex gauge
        jy = x * L + ((y + 1) % L) + 1
        ph = 2π * alpha * x
        yj = y + 1.0                            # unwrapped for the wrap bond
        for (vx, vy, q) in vortices
            a1 = atan(y - vy, x - vx)
            a2 = atan(yj - vy, x - vx)
            ph += 0.5 * q * (a1 - a2)
        end
        H[i, jy] += exp(im * ph)
        H[jy, i] += exp(-im * ph)
    end
    return H
end

# ─── Chiral (sublattice) operator ────────────────────────────────────────────
function sublattice_gamma(L::Int)
    g = zeros(L * L)
    for x in 0:L-1, y in 0:L-1
        g[x * L + y + 1] = (x + y) % 2 == 0 ? 1.0 : -1.0
    end
    return g
end

# ─── ⟨r⟩ statistic (bulk 60%, parent definition) ─────────────────────────────
function mean_r(vals::Vector{Float64}; frac=0.6)
    v = sort(vals)
    n = length(v)
    lo = floor(Int, (1 - frac) / 2 * n) + 1
    hi = floor(Int, (1 + frac) / 2 * n)
    v = v[lo:hi]
    d = diff(v)
    d = d[d .> 1e-14]
    isempty(d) && return NaN
    r = [min(d[i], d[i+1]) / max(d[i], d[i+1]) for i in 1:length(d)-1]
    return mean(r)
end

const results = Dict{String,Any}()

# ═════════════════════════════════════════════════════════════════════════════
println("═"^64)
println("AB-CLOUD DIRAC LAB — Julia cross-verification (seed-independent)")
println("═"^64)

# ─── Cross-D1: clean torus E₁ (compare with Python D1b table) ────────────────
python_d1 = Dict(16 => 0.765367, 24 => 0.517638, 32 => 0.390181)
cross_d1 = Dict{String,Any}()
worst = 0.0
for L in (16, 24, 32)
    ev = eigvals(Hermitian(build_hamiltonian(L, 0.5)))
    above = ev[ev .> 1e-8]
    e1 = above[1]
    py = python_d1[L]
    dev = abs(e1 - py) / py
    global worst = max(worst, dev)
    cross_d1[string(L)] = Dict("E1_julia" => e1, "E1_python" => py,
                               "E1_x_L" => e1 * L, "rel_dev" => dev)
    @printf("  D1 L=%2d: E₁(jl) = %.6f  E₁(py) = %.6f  E₁·L = %.4f  dev = %.2e\n",
            L, e1, py, e1 * L, dev)
end
ok_d1 = worst < 2e-6
println("  D1 cross-check: ", ok_d1 ? "PASS" : "FAIL", "  (worst rel dev ",
        @sprintf("%.2e", worst), ")")
results["D1"] = Dict("verdict" => ok_d1 ? "PASS" : "FAIL", "data" => cross_d1)

# ─── Cross-D2: zero tower + chiral structure ─────────────────────────────────
cross_d2 = Dict{String,Any}()
ok_tower = true
for L in (16, 24, 32)
    H = build_hamiltonian(L, 0.5)
    G = Diagonal(sublattice_gamma(L))
    anticomm = maximum(abs.(H * G + G * H))
    F = eigen(Hermitian(H)); ev = F.values; vec = F.vectors
    n_zero = count(abs.(ev) .< 1e-8)
    tower = abs.(ev) .< 1e-9
    pol = [dot(vec[:, k], G * vec[:, k]) for k in findall(tower)]
    gpol = round(Int, sum(sign.(real.(pol))))
    ok = n_zero == 4 && anticomm < 1e-10 && gpol == 0
    global ok_tower &= ok
    cross_d2[string(L)] = Dict("n_zero" => n_zero, "anticomm" => anticomm,
                               "gamma_polarity" => gpol)
    @printf("  D2 L=%2d: n_zero = %d  ||{H,Γ}|| = %.1e  Γ-polarity = %+d  %s\n",
            L, n_zero, anticomm, gpol, ok ? "✓" : "✗")
end
println("  D2 cross-check: ", ok_tower ? "PASS" : "FAIL")
results["D2"] = Dict("verdict" => ok_tower ? "PASS" : "FAIL", "data" => cross_d2)

# ─── Cross-D7: ζ-decorated Dirac operator (L = 32) ───────────────────────────
L = 32
nv = max(2, round(Int, 25.0 * L^2 / 900))
nv += nv % 2
zeros_path = length(ARGS) >= 1 ? ARGS[1] :
    joinpath(dirname(dirname(@__FILE__)), "data", "zeta_zeros_2000.txt")
zt = Float64[]
for line in eachline(zeros_path)
    s = strip(line)
    (isempty(s) || startswith(s, "#")) && continue
    push!(zt, parse(Float64, s))
    length(zt) >= 200 && break
end
@printf("  D7: %d ζ zeros loaded from %s\n", length(zt), basename(zeros_path))

cross_d7 = Dict{String,Any}()
rows = Dict{String,Any}[]
ok_herm, ok_gue = true, true
for (name, vort) in [("clean", Tuple{Float64,Float64,Float64}[]),
                     ("zeta", zeta_coded_vortices(zt, L, nv))]
    H = build_hamiltonian(L, 0.5; vortices=vort)
    herm = maximum(abs.(H - H'))
    ev = eigvals(Hermitian(H))
    n_zero = count(abs.(ev) .< 1e-8)
    above = ev[ev .> 1e-8]
    e1 = above[1]
    r_mean = mean_r(ev)
    push!(rows, Dict("config" => name, "Nv" => name == "clean" ? 0 : nv,
                     "n_zero" => n_zero, "E1" => e1, "E1_x_L" => e1 * L,
                     "r_mean" => r_mean, "herm" => herm))
    @printf("  D7 L=%d %-5s Nv=%3d: tower = %d  E₁·L = %.4f  ⟨r⟩ = %.4f\n",
            L, name, name == "clean" ? 0 : nv, n_zero, e1 * L, r_mean)
    name == "clean" && (ok_herm = herm < 1e-13 && n_zero == 4)
    name == "zeta" && (ok_gue = r_mean ≥ 0.56)
end
r_clean = rows[1]["r_mean"]; r_zeta = rows[2]["r_mean"]
ok_shift = (r_zeta - r_clean) ≥ 0.04
println("  D7 ⟨r⟩ shift: ", @sprintf("%+.4f", r_zeta - r_clean), "  → ",
        ok_shift ? "PASS" : "FAIL")
println("  D7 cross-check: ", (ok_herm && ok_gue && ok_shift) ? "PASS" : "FAIL")
results["D7"] = Dict("verdict" => (ok_herm && ok_gue && ok_shift) ? "PASS" : "FAIL",
                     "r_shift" => r_zeta - r_clean, "rows" => rows)

# ─── Cross-D8: chiral protection under ζ decoration ──────────────────────────
H = build_hamiltonian(L, 0.5; vortices=zeta_coded_vortices(zt, L, nv))
G = Diagonal(sublattice_gamma(L))
anticomm = maximum(abs.(H * G + G * H))
ev = eigvals(Hermitian(H))
pos = ev[ev .> 1e-12]
neg = -ev[ev .< -1e-12][end:-1:1]
m = min(length(pos), length(neg))
sym_err = maximum(abs.(pos[1:m] - neg[1:m]))
ok_d8 = anticomm < 1e-12 && sym_err < 1e-10
@printf("  D8: ||{H,Γ}|| = %.2e  E↔−E pairing = %.2e (%d pairs)  → %s\n",
        anticomm, sym_err, m, ok_d8 ? "PASS" : "FAIL")
results["D8"] = Dict("verdict" => ok_d8 ? "PASS" : "FAIL",
                     "anticomm" => anticomm, "sym_err" => sym_err, "pairs" => m)

# ─── Verdict summary + JSON ──────────────────────────────────────────────────
println("─"^64)
all_ok = all(r["verdict"] == "PASS" for (k, r) in results)
println("JULIA CROSS-VERIFICATION: ", all_ok ? "ALL PASS" : "FAILURES PRESENT")
println("═"^64)
results["summary"] = Dict("all_pass" => all_ok,
                          "julia_version" => string(VERSION),
                          "zeros_used" => length(zt))

outpath = joinpath(dirname(dirname(@__FILE__)), "results",
                   "cross_verification_julia.json")
open(outpath, "w") do f
    write(f, to_json(results))
end
println("  json → ", outpath)
