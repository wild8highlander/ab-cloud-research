#!/usr/bin/env julia
#=
wave_attractors.jl — Julia port of the ray-level core of study W1
(Hyperbolic wave attractors) for cross-verification against the Python
reference implementation (ray_billiard.py).

The script reads the launch states from data/rays_reference.csv (produced
by run_experiments.py / dump_reference_csv.py), propagates each ray in the
asymmetric hexagonal chamber with the exact hyperbolic reflection law, and
writes data/rays_julia.csv with the resulting attractor diagnostics.

Cross-verification is performed by scripts/verify_cross.py, which compares
  * the attractor period,
  * the chirality index of the closed loop,
  * the loop geometry (point-wise distance),
  * the final |k| on the dispersion contour,
between the two independent implementations.

Only Julia standard library is used (DelimitedFiles, Printf).

Usage:  julia wave_attractors.jl [path/to/wave_attractors/root]
=#

using DelimitedFiles
using Printf
using Statistics
using LinearAlgebra
using Random

# ---------------------------------------------------------------------------
# Medium: hyperbolic dispersion  ky^2 - kx^2/eta = K^2  (mu = diag(1, -eta))
# ---------------------------------------------------------------------------

struct Medium
    kind::String
    eta::Float64
end

function group_velocity(m::Medium, k::Vector{Float64})
    if m.kind == "isotropic"
        return copy(k)
    end
    return [-k[1] / m.eta, k[2]]
end

function unit(v::Vector{Float64})
    L = hypot(v[1], v[2])
    return v ./ L
end

# ---------------------------------------------------------------------------
# Chamber (simple polygon, CCW, closed)
# ---------------------------------------------------------------------------

struct Chamber
    v::Matrix{Float64}          # (n+1, 2), first row == last row
    name::String
end

function chamber_hexagon_asym(s_left::Float64, s_right::Float64, y_v::Float64;
                              w::Float64=1.0, h::Float64=1.0)
    pts = [0.0 h; w h; w y_v; w - s_right 0.0; s_left 0.0; 0.0 y_v; 0.0 h]
    return Chamber(pts, "hexagon_asym")
end

"""walls(ch) -> Vector{Tuple{Vector{Float64},Vector{Float64},Vector{Float64}}}
   (P0, t_hat, n_inward) per segment; index aligned with segment i."""
function walls(ch::Chamber)
    out = Vector{Tuple{Vector{Float64},Vector{Float64},Vector{Float64}}}()
    v = ch.v
    centroid = vec(mean(v[1:end-1, :]; dims=1))
    for i in 1:(size(v, 1) - 1)
        p0 = vec(v[i, :])
        e = vec(v[i+1, :]) - p0
        L = hypot(e[1], e[2])
        if L < 1e-14
            push!(out, (p0, [1.0, 0.0], [0.0, 1.0]))
            continue
        end
        t = e ./ L
        n_in = [-t[2], t[1]]
        if dot(n_in, centroid - p0) < 0
            n_in = -n_in
        end
        push!(out, (p0, t, n_in))
    end
    return out
end

function first_hit(ch::Chamber, p::Vector{Float64}, d::Vector{Float64})
    best_s = Inf
    best_i = -1
    v = ch.v
    for i in 1:(size(v, 1) - 1)
        a = vec(v[i, :])
        e = vec(v[i+1, :]) - a
        det = d[1] * (-e[2]) - (-e[1]) * d[2]
        abs(det) < 1e-15 && continue
        rhs = a - p
        s = (rhs[1] * (-e[2]) - rhs[2] * (-e[1])) / det
        u = (d[1] * rhs[2] - d[2] * rhs[1]) / det
        if s > 1e-11 && -1e-9 <= u <= 1.0 + 1e-9 && s < best_s
            best_s = s
            best_i = i
        end
    end
    if best_i < 0
        return nothing
    end
    return (best_s, best_i)
end

# ---------------------------------------------------------------------------
# Exact reflection law (k-vector form, Vieta root + Newton polish)
# ---------------------------------------------------------------------------

function dispersion_coeffs(m::Medium, kt::Float64, n::Vector{Float64},
                           t::Vector{Float64}, K::Float64)
    if m.kind == "isotropic"
        return 1.0, 0.0, kt * kt - K * K
    end
    A = n[2]^2 - n[1]^2 / m.eta
    B = 2.0 * kt * (t[2] * n[2] - t[1] * n[1] / m.eta)
    C = kt^2 * (t[2]^2 - t[1]^2 / m.eta) - K^2
    return A, B, C
end

function reflect(k::Vector{Float64}, t::Vector{Float64}, n::Vector{Float64},
                 m::Medium, K::Float64)
    kt = dot(k, t)
    kn_inc = dot(k, n)
    A, B, C = dispersion_coeffs(m, kt, n, t, K)
    kn_new = 0.0
    if abs(A) < 1e-12
        if abs(B) < 1e-12
            return copy(k)
        end
        kn_new = -C / B
    else
        disc = B^2 - 4.0 * A * C
        disc < 0.0 && (disc = 0.0)
        sq = sqrt(disc)
        r1 = (-B - sq) / (2.0 * A)
        r2 = (-B + sq) / (2.0 * A)
        kn_new = abs(r2 - kn_inc) >= abs(r1 - kn_inc) ? r2 : r1
    end
    # Newton polish back onto the contour
    F = A * kn_new^2 + B * kn_new + C
    dF = 2.0 * A * kn_new + B
    if abs(dF) > 1e-14
        kn_new -= F / dF
    end
    return [kt * t[1] + kn_new * n[1], kt * t[2] + kn_new * n[2]]
end

# ---------------------------------------------------------------------------
# Ray propagation with limit-cycle detection
# ---------------------------------------------------------------------------

function rotate(k::Vector{Float64}, ang::Float64)
    c, s = cos(ang), sin(ang)
    return [c * k[1] - s * k[2], s * k[1] + c * k[2]]
end

function propagate_ray(ch::Chamber, m::Medium, p0::Vector{Float64},
                       k0::Vector{Float64}, K::Float64;
                       max_bounces::Int=1600, loop_tol::Float64=1e-7,
                       loop_window::Int=100)
    W = walls(ch)
    pts = Vector{Vector{Float64}}([copy(p0)])
    ks = Vector{Vector{Float64}}([copy(k0)])
    segs = Float64[]
    edges = Int[]
    p = copy(p0)
    k = copy(k0)
    scale = maximum(maximum(ch.v, dims=1) .- minimum(ch.v, dims=1))
    corner_eps = 1e-7 * scale

    for bounce_i in 1:max_bounces
        d = unit(group_velocity(m, k))
        hit = first_hit(ch, p, d)
        if hit === nothing
            error("ray escaped chamber at p=($(round(p[1]; digits=6)),$(round(p[2]; digits=6)))")
        end
        s, edge = hit
        p_hit = p .+ s .* d

        # corner robustness: reflect vertex hits off the bisector of the two
        # adjacent wall normals (rounded-corner defect model; deterministic,
        # identical to the Python implementation)
        corner_hit = false
        dmin, j = findmin([hypot(ch.v[i, 1] - p_hit[1], ch.v[i, 2] - p_hit[2])
                           for i in 1:(size(ch.v, 1) - 1)])
        if dmin <= corner_eps
            n1 = W[j][3]
            j2 = (j - 2) % (size(ch.v, 1) - 1) + 1
            n2 = W[j2][3]
            n_eff = unit(n1 .+ n2)
            t_eff = [-n_eff[2], n_eff[1]]
            k = reflect(k, t_eff, n_eff, m, K)
            corner_hit = true
            edge = j
        end

        p = p_hit
        push!(pts, copy(p))
        push!(segs, s)
        push!(edges, edge)

        if corner_hit
            n_out = n_eff
        else
            _, t, n = W[edge]
            k = reflect(k, t, n, m, K)
            n_out = n
        end
        push!(ks, copy(k))
        vg = unit(group_velocity(m, k))
        # tiny step along the INWARD NORMAL (safe at corners / grazing)
        p = p .+ n_out .* (1e-9 * scale)
    end

    loop, period = detect_limit_cycle(pts, loop_tol, loop_window)
    return (pts=pts, ks=ks, segs=segs, edges=edges, loop=loop, period=period)
end

function detect_limit_cycle(pts::Vector{Vector{Float64}}, tol::Float64,
                            max_period::Int)
    M = length(pts)
    M < 8 && return nothing, 0
    tail_start = max(1, M - max_period - 10)
    for per in 2:min(max_period, (M - tail_start) ÷ 2)
        idx0 = M - per + 1
        ok = true
        for j in 0:(per - 1)
            i1 = idx0 - j
            i2 = idx0 - j - per
            i2 < tail_start && break
            if hypot(pts[i1][1] - pts[i2][1], pts[i1][2] - pts[i2][2]) > tol
                ok = false
                break
            end
        end
        if ok
            loop = pts[(M - per + 1):M]
            return loop, per
        end
    end
    return nothing, 0
end

function chirality_index(loop::Vector{Vector{Float64}})
    n = length(loop)
    n < 3 && return 0.0
    total = 0.0
    for i in 1:n
        a = loop[i]
        b = loop[i % n + 1]
        c = loop[(i + 1) % n + 1]
        a1 = atan(b[2] - a[2], b[1] - a[1])
        a2 = atan(c[2] - b[2], c[1] - b[1])
        dphi = a2 - a1
        while dphi > pi;  dphi -= 2pi; end
        while dphi < -pi; dphi += 2pi; end
        total += dphi
    end
    return total / (2pi)
end

_round(x) = round(x; digits=6)  # noqa (kept for interactive use)

# ---------------------------------------------------------------------------
# Main: read reference launch states, propagate, write results
# ---------------------------------------------------------------------------

function main()
    root = length(ARGS) >= 1 ? ARGS[1] : dirname(@__DIR__)
    data_dir = joinpath(root, "data")
    ref_csv = joinpath(data_dir, "rays_reference.csv")
    out_csv = joinpath(data_dir, "rays_julia.csv")

    ETA = 100.0
    med = Medium("hyperbolic", ETA)
    ch = chamber_hexagon_asym(0.03, 0.06, 0.35)

    ref = readdlm(ref_csv, ',', Float64; header=true)
    header = ref[2]
    data = ref[1]
    cols = Dict(name => i for (i, name) in enumerate(vec(header)))
    n_rays = size(data, 1)
    println("[W1-julia] reference rays: ", n_rays)

    out = Vector{Vector{String}}()
    push!(out, ["ray", "n_bounces", "period", "loop_found", "chirality",
                "final_kx", "final_ky"])
    short = Vector{Vector{String}}()
    push!(short, ["ray", "bounce", "x", "y"])
    SHORT_HORIZON = 100
    for ir in 1:n_rays
        p0 = [data[ir, cols["p0x"]], data[ir, cols["p0y"]]]
        k0 = [data[ir, cols["k0x"]], data[ir, cols["k0y"]]]
        res = propagate_ray(ch, med, p0, k0, 1.0)
        loop_found = res.loop !== nothing
        chi = loop_found ? chirality_index(res.loop) : 0.0
        per = loop_found ? res.period : 0
        kf = res.ks[end]
        push!(out, [@sprintf("%d", ir - 1), @sprintf("%d", length(res.edges)),
                     @sprintf("%d", per), loop_found ? "1" : "0",
                     @sprintf("%.12e", chi),
                     @sprintf("%.12e", kf[1]), @sprintf("%.12e", kf[2])])
        # short-horizon trajectory (deterministic comparison vs Python)
        nb = min(SHORT_HORIZON, length(res.pts) - 1)
        for b in 1:nb
            push!(short, [@sprintf("%d", ir - 1), @sprintf("%d", b - 1),
                           @sprintf("%.16e", res.pts[b+1][1]),
                           @sprintf("%.16e", res.pts[b+1][2])])
        end
    end

    writedlm(out_csv, out, ',')
    writedlm(joinpath(data_dir, "rays_short_julia.csv"), short, ',')
    println("[W1-julia] wrote ", out_csv)
end

main()
