#!/usr/bin/env julia
# spinor38.jl — Test 38: 64 spinor structures of the Klein quartic (Julia port)
# Verifies, using ONLY the frozen data files and the stdlib LinearAlgebra:
#   1. the 28 odd (Arf=1) structures are exactly isospectral (max pairwise
#      spectral distance ~ 1e-14) — no spinor structure is unique;
#   2. <r> of the representative spectrum matches the reference
#      0.4515710792825435.
#
# Run: julia spinor38.jl [repo-root]

using LinearAlgebra
using Printf

function find_data_dir(root)
    bases = String[]
    !isempty(root) && push!(bases, root)
    push!(bases, pwd())
    for b in bases
        for _ in 1:6
            cand = joinpath(b, "verification", "spinor64", "data",
                            "spinor_classes.csv")
            isfile(cand) && return joinpath(b, "verification", "spinor64", "data")
            b = joinpath(b, "..")
        end
    end
    error("data dir not found; pass repo root as argument")
end

function jacobi_eigen(A::Matrix{Float64})
    n = size(A, 1)
    M = copy(A)
    for sweep in 1:200
        off = 0.0
        for p in 1:n, q in (p+1):n
            off += M[p, q]^2
        end
        off < 1e-24 && break
        for p in 1:n, q in (p+1):n
            abs(M[p, q]) < 1e-15 && continue
            tau = (M[q, q] - M[p, p]) / (2 * M[p, q])
            t = sign(tau) / (abs(tau) + sqrt(1 + tau^2))
            c = 1 / sqrt(1 + t^2)
            s = t * c
            for k in 1:n
                akp, akq = M[k, p], M[k, q]
                M[k, p] = c * akp - s * akq
                M[k, q] = s * akp + c * akq
            end
            for k in 1:n
                apk, aqk = M[p, k], M[q, k]
                M[p, k] = c * apk - s * aqk
                M[q, k] = s * apk + c * aqk
            end
        end
    end
    sort!(diag(M))
end

function main()
    root = length(ARGS) >= 1 ? ARGS[1] : ""
    dd = find_data_dir(root)

    classes = Tuple{Int,Int,Int,Vector{Float64}}[]
    lines = readlines(joinpath(dd, "spinor_classes.csv"))
    for ln in lines[2:end]
        isempty(ln) && continue
        parts = split(ln, ','; limit=4)
        cls = parse(Int, parts[1]); orb = parse(Int, parts[2])
        arf = parse(Int, parts[3])
        sgn = [parse(Float64, tok) for tok in split(parts[4])]
        push!(classes, (cls, orb, arf, sgn))
    end
    edges = Tuple{Int,Int}[]
    elines = readlines(joinpath(dd, "klein_graph_edges.csv"))
    for ln in elines[2:end]
        isempty(ln) && continue
        parts = split(ln, ',')
        push!(edges, (parse(Int, parts[2]), parse(Int, parts[3])))
    end
    js = read(joinpath(dd, "reference_stats.json"), String)
    function jsonnum(key::String)
        m = match(Regex("\"$(key)\":\s*([-0-9.eE+]+)"), js)
        isnothing(m) ? 0.0 : parse(Float64, m.captures[1])
    end
    r_ref = jsonnum("r_mean_reference")
    n_zero_ref = round(Int, jsonnum("n_zero_modes"))
    representative = round(Int, jsonnum("representative_class"))

    const_N = 56
    n_odd = count(c -> c[2] == 0, classes)

    spectra = Vector{Vector{Float64}}()
    rep_spectrum = Vector{Float64}()
    for (cls, orb, _arf, sgn) in classes
        orb == 0 || continue
        A = zeros(const_N, const_N)
        for (k, (u, v)) in enumerate(edges)
            A[u+1, v+1] = sgn[k]
            A[v+1, u+1] = sgn[k]
        end
        w = jacobi_eigen(A)
        cls == representative && (rep_spectrum = w)
        push!(spectra, w)
    end

    isomax = 0.0
    for a in 1:length(spectra), b in (a+1):length(spectra), i in 1:const_N
        isomax = max(isomax, abs(spectra[a][i] - spectra[b][i]))
    end

    lam = sort(abs.(rep_spectrum))
    n_zero = count(v -> v < 1e-8, lam)
    dsp = Float64[]
    for i in 1:length(lam)-1
        d = lam[i+1] - lam[i]
        d > 1e-8 && push!(dsp, d)
    end
    r_mean = sum(min(dsp[i], dsp[i+1]) / max(dsp[i], dsp[i+1])
                 for i in 1:length(dsp)-1) / (length(dsp) - 1)

    println("Test 38 - 64 spinor structures of the Klein quartic (Julia port)")
    @printf("classes loaded: %d | odd-orbit members: %d\n", length(classes), n_odd)
    println("isospectrality within the odd orbit: max|dlambda| = ",
            @sprintf("%.3e", isomax), " -> ", isomax < 1e-9 ? "PASS" : "FAIL")
    println("zero modes (representative): ", n_zero, " (expected ", n_zero_ref, ")")
    rok = abs(r_mean - r_ref) < 1e-6
    println("<r> (representative): ", @sprintf("%.10f", r_mean),
            " (reference 0.4515710793) -> ", rok ? "PASS" : "FAIL")
    ok = isomax < 1e-9 && n_zero == n_zero_ref && rok
    println("VERDICT: ", ok ? "PASS" : "FAIL")
    ok || exit(1)
end

main()
