# gen_golden.jl — generate golden reference numbers for the 4-language ports
# from the ORIGINAL Julia sources (ab_cloud_full.jl + hp_audit_standalone.jl).
# Run: julia gen_golden.jl <meridian_dir> <out_json>
# Every number here is produced by the unmodified original kernels.

if length(ARGS) < 2
    println("usage: julia gen_golden.jl <meridian_dir> <out_json>")
    exit(1)
end
mdir = abspath(ARGS[1])
outfile = abspath(ARGS[2])

include(joinpath(mdir, "ab_cloud_full.jl"))          # silent library mode
println("suite included")

import Random
using DelimitedFiles

# ── Classic MT19937 (init_genrand) ───────────────────────────────────────
# The SAME algorithm is embedded verbatim in every port (python/cpp/rust/go),
# so window sampling for Σ²/Δ₃ is bit-identical across all five languages.
# (Julia's built-in MersenneTwister is dSFMT — NOT compatible.)
mutable struct MT19937Classic <: Random.AbstractRNG
    mt::Vector{UInt32}
    idx::Int
end

function MT19937Classic(seed::Integer)
    mt = Vector{UInt32}(undef, 624)
    mt[1] = UInt32(mod(Int(seed), 2^32))
    for i in 2:624
        prev = UInt64(mt[i-1])
        mt[i] = UInt32(mod(1812433253 * (prev ⊻ (prev >> 30)) + (i - 1), 2^32))
    end
    # idx = 625 (empty): the first call must twist BEFORE drawing, and every
    # generated block must yield ALL 624 elements mt[1..624] — the reference
    # C (mt19937ar) semantics that python/cpp/rust/go ports implement.
    MT19937Classic(mt, 625)
end

function _mt_next!(r::MT19937Classic)::UInt32
    if r.idx > 624
        M_ = 397
        @inbounds for i in 1:624
            y = (r.mt[i] & 0x80000000) | (r.mt[mod1(i + 1, 624)] & 0x7fffffff)
            nxt = r.mt[mod1(i + M_, 624)] ⊻ (y >> 1)
            isodd(y) && (nxt = nxt ⊻ 0x9908b0df)
            r.mt[i] = nxt
        end
        r.idx = 1
    end
    y = r.mt[r.idx]
    r.idx += 1
    y = y ⊻ (y >> 11)
    y = y ⊻ ((y << 7) & 0x9d2c5680)
    y = y ⊻ ((y << 15) & 0xefc60000)
    y = y ⊻ (y >> 18)
    return y
end

Random.rand(r::MT19937Classic, ::Type{Float64}) =
    (Float64(_mt_next!(r) >> 5) * 67108864.0 + Float64(_mt_next!(r) >> 6)) / 9007199254740992.0
println("MT19937 classic ready")

# ── zeros ────────────────────────────────────────────────────────────────────
zeros_path = joinpath(mdir, "zeros50k.txt")
zeta = vec(readdlm(zeros_path, Float64))
sort!(zeta)
n_zeros = length(zeta)
println("zeros: ", n_zeros)

J = Dict{String,Any}()
J["meta"] = Dict("julia"=>string(VERSION), "zeros_file"=>"zeros50k.txt",
                 "n_zeros"=>n_zeros, "gamma1"=>zeta[1], "gammaN"=>zeta[end])

function put!(section::String, key::String, v::Float64)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
function puti!(section::String, key::String, v::Int)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end

# ── 1. Lambert W / Gram points ───────────────────────────────────────────────
for x in (0.5, 1.0, 3.7, 10.0, 271.8, 12345.6)
    put!("lambert_w", "x=$(x)", lambert_w(x))
end
for n in (1, 2, 3, 10, 100, 1000, 10000, 50000)
    put!("gram_point", "n=$(n)", gram_point(n))
end

# ── 2. b(N) ladder ───────────────────────────────────────────────────────────
for N in (100, 500, 1000, 5000, 10000, 50000)
    put!("bN", "N=$(N)", compute_bN(zeta, N))
end
put!("bN", "N=1000_off500", compute_bN(zeta, 1000; offset=500))

# ── 3. normalized spacings ───────────────────────────────────────────────────
sp = normalized_spacings(zeta)
puti!("spacings", "n", length(sp))
put!("spacings", "mean", mean(sp))
put!("spacings", "var", var(sp))

# ── 4. surmises / special functions ─────────────────────────────────────────
for s in (0.05, 0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 4.9)
    put!("gue2_cdf", "s=$(s)", gue2_surmise_cdf(s))
    put!("goe_cdf", "s=$(s)", goe_surmise_cdf(s))
    put!("gue2_pdf", "s=$(s)", gue2_surmise_pdf(s))
end
for (a, x) in ((0.5, 0.1), (0.5, 2.0), (1.0, 1.0), (2.0, 3.0), (0.5, 12.0))
    put!("gamma_p", "a=$(a)_x=$(x)", regularized_gamma_p(a, x))
end
for (x, df) in ((3.84, 1.0), (16.92, 29.0), (25.0, 10.0))
    put!("chi2_cdf", "x=$(x)_df=$(df)", chi2_cdf(x, df))
end
put!("ks_pvalue", "lam=0.5", ks_asymptotic_pvalue(0.5))
put!("ks_pvalue", "lam=1.3", ks_asymptotic_pvalue(1.3))
put!("ks_pvalue", "lam=0.02", ks_asymptotic_pvalue(0.02))

# ── 5. GOF of the zero spacings vs GUE ───────────────────────────────────────
D, pks = ks_test(sp)
put!("ks_zeros", "D", D); put!("ks_zeros", "p", pks)
W2 = cvm_test(sp)
put!("cvm_zeros", "W2", W2)
A2 = anderson_darling_stat(sp)
put!("ad_zeros", "A2", A2)
chi2v, dfv, pchi = chi2_gue_test(sp; nbins=30)
put!("chi2_zeros", "chi2", chi2v); put!("chi2_zeros", "df", Float64(dfv)); put!("chi2_zeros", "p", pchi)
r_mean, n_r = mean_adjacent_spacing_ratio(zeta)
put!("rmean_zeros", "r", r_mean); puti!("rmean_zeros", "n_r", n_r)

# ── 6. long-range statistics (statistical anchors; own MT in ports) ─────────
pos = unfolded_positions(zeta)
rngS = MT19937Classic(777)
for L in (5.0, 10.0, 20.0, 50.0, 100.0)
    put!("S2", "L=$(L)", number_variance(pos, L; n_windows=3000, rng=rngS))
end
for L in (5.0, 10.0, 20.0, 50.0)
    put!("D3", "L=$(L)", delta3_rigidity(pos, L; n_windows=300, n_grid=300, rng=rngS))
end

# ── 7. K(t) form factor on zeros + envelope RMS ─────────────────────────────
tvals = collect(0.1:0.1:3.0)
# Store the EXACT grids in the golden so every port loads identical values
# (no language-specific `colon`/`arange` semantics in the parity path).
J["grids"] = Dict{String,Any}("tvals"=>tvals)
Kz = compute_K_form_factor(zeta, tvals; smooth_window=3)
for (i, t) in enumerate(tvals)
    if t in (0.2, 0.5, 1.0, 2.0, 3.0)
        put!("K_zeros", "t=$(t)", Kz[i])
    end
end
mask = tvals .>= 0.3
rms_env = sqrt(mean((Kz[mask] .- [_hp_kgue_envelope(t) for t in tvals[mask]]).^2))
put!("K_zeros", "rms_env", rms_env)

# ── 8. H1 ζ positive control (deterministic on the zeros!) ──────────────────
zslice = zeta[1:min(end, 20000)]
primes = [2, 3, 5, 7, 11, 13]
ω_targets = [log(p) for p in primes]
ωgrid = collect(0.3:0.004:3.2)
J["grids"]["omega"] = ωgrid
Pz = _hp_raw_ft(zslice, ωgrid)
med_z = median(Pz)
snrs = [begin
            i = argmin(abs.(ωgrid .- ω))
            Pz[i] / med_z
        end for ω in ω_targets]
put!("h1_zeta", "median", med_z)
for (j, p) in enumerate(primes)
    put!("h1_zeta", "snr_log$(p)", snrs[j])
end

# ── 9. Hamiltonian goldens (explicit vortices, W=0 → fully deterministic) ───
function store_eigs2(section::String, ev::Vector{Float64})
    n = length(ev)
    for k in 1:3; put!(section, "eig$(k)", ev[k]); end
    put!(section, "eigmid", ev[div(n, 2)])
    for k in 0:2; put!(section, "eigend$(3-k)", ev[n - k]); end
end

# 9a. clean Hofstadter L=8, α=0.5, open, W=0, no vortices
c1 = ABCloudConfig(8, 8, Vortex[], 0.5, 1.0, :open, 0.0, 96, :monumental)
e1 = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(c1)))))
store_eigs2("ham_L8_open_a05_clean", e1)

# 9b. L=8, α=0.25, two explicit neutral vortices at plaquette centers
vorts = [Vortex(3.5, 3.5, 1.0), Vortex(6.5, 6.5, -1.0)]
c2 = ABCloudConfig(8, 8, vorts, 0.25, 1.0, :open, 0.0, 96, :monumental)
e2 = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(c2)))))
store_eigs2("ham_L8_open_a025_2vort", e2)

# 9c. L=10 torus, α=0.2 (α·Ny = 2 ∈ ℤ), clean
c3 = ABCloudConfig(10, 10, Vortex[], 0.2, 1.0, :torus, 0.0, 96, :monumental)
e3 = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(c3)))))
store_eigs2("ham_L10_torus_a02_clean", e3)

# 9d. Byers–Yang: q → q+1 on a NEUTRAL config (W=0) — spectra identical.
# Stated for the :dirac gauge model (Test 25): integer flux quanta are
# invisible → Δ ≈ 1e-15. (The :monumental smooth-gauge model rescales a
# genuinely q-dependent field and is NOT Byers–Yang invariant.)
vy1 = [Vortex(3.5, 3.5, 1.0), Vortex(6.5, 6.5, -1.0)]
vy2 = [Vortex(3.5, 3.5, 2.0), Vortex(6.5, 6.5, 0.0)]
cy1 = ABCloudConfig(8, 8, vy1, 0.3, 1.0, :open, 0.0, 96, :dirac)
cy2 = ABCloudConfig(8, 8, vy2, 0.3, 1.0, :open, 0.0, 96, :dirac)
e_y1 = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(cy1)))))
e_y2 = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(cy2)))))
dy = maximum(abs.(e_y1 - e_y2))
put!("byers_yang", "L8_max_diff", dy)

# 9e. Connes self-duality α ↔ 1/α — the SUITE's connes_self_duality_defect
# formula (relative L² distance of sorted spectra on an OPEN lattice),
# evaluated at W=0 for cross-language reproducibility (the suite helper
# hardcodes W=4, whose residual ε uses Julia dSFMT — not portable).
function connes_defect_W0(α::Float64, Nx::Int, Ny::Int)
    cfg_α = ABCloudConfig(Nx, Ny, Vortex[], α, 1.0, :open, 0.0)
    cfg_1α = ABCloudConfig(Nx, Ny, Vortex[], 1.0 / α, 1.0, :open, 0.0)
    ev_α = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(cfg_α)))))
    ev_1α = sort(real.(eigvals(Hermitian(build_ab_cloud_hamiltonian(cfg_1α)))))
    return norm(ev_α - ev_1α) / max(norm(ev_α), 1e-30)
end
put!("connes", "L12_a05_defect_W0", connes_defect_W0(0.5, 12, 12))

# 9f. chiral AIII defect at α=1/2, W=0: ||S·H·S + H||_F / ||H||_F, S = (ix+iy) parity
cch = ABCloudConfig(12, 12, Vortex[], 0.5, 1.0, :open, 0.0, 96, :monumental)
Hch = build_ab_cloud_hamiltonian(cch)
N = 12 * 12
S = Diagonal([(((mod(i - 1, 12) + 1) + div(i - 1, 12) + 1) % 2 == 0) ? 1.0 : -1.0 for i in 1:N])
defect = norm(S * Hch * S + Hch) / norm(Hch)
put!("chiral", "L12_a05_defect", defect)

# 9g. Dirac-string flux: plaquette curl of the BOND phases (monumental model).
function bond_phase_right(H, Nx, ix, iy)   # hop (ix,iy)→(ix+1,iy)
    i = (iy - 1) * Nx + ix; j = (iy - 1) * Nx + ix + 1
    return angle(H[i, j] / (-1.0 + 0im))
end
function bond_phase_up(H, Nx, ix, iy)      # hop (ix,iy)→(ix,iy+1)
    i = (iy - 1) * Nx + ix; j = iy * Nx + ix
    return angle(H[i, j] / (-1.0 + 0im))
end
cf = ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0)], 0.25, 1.0, :open, 0.0, 96, :dirac)
Hf = build_ab_cloud_hamiltonian(cf)
# 9g. Dirac-string flux — the SUITE's canonical plaquette_flux (Test 24):
# CCW sum of angle(−H[b,a]) over the 4 bonds. Target: 2πα on every
# plaquette + 2πq on the vortex plaquette (:dirac model). max circular
# deviation over all inner plaquettes — expected ≈ 1e-14.
function _dirac_flux_maxdev(Hf, Nx, α, qv::Float64)
    function plaquette_flux(ix, iy)
        i_bl = (iy - 1) * Nx + ix
        i_br = (iy - 1) * Nx + ix + 1
        i_tr = iy * Nx + ix + 1
        i_tl = iy * Nx + ix
        φ_bot = angle(-Hf[i_br, i_bl])
        φ_right = angle(-Hf[i_tr, i_br])
        φ_top = angle(-Hf[i_tl, i_tr])
        φ_left = angle(-Hf[i_bl, i_tl])
        return φ_bot + φ_right + φ_top + φ_left
    end
    maxdev = 0.0
    for iy in 1:(Nx - 1), ix in 1:(Nx - 1)
        flux = plaquette_flux(ix, iy)
        has_vortex = (ix == 3 && iy == 3)
        target = 2π * α + (has_vortex ? 2π * qv : 0.0)
        dev = abs(mod(flux - target + π, 2π) - π)
        maxdev = max(maxdev, dev)
    end
    return maxdev
end
put!("dirac_flux", "L8_max_dev", _dirac_flux_maxdev(Hf, 8, 0.25, 1.0))

# ── 10. unfold / spearman / aicc / wald anchors ─────────────────────────────
u = _hp_unfold_local(zeta[1:2000])
put!("unfold", "u2", u[2]); put!("unfold", "u1000", u[1000]); put!("unfold", "u2000", u[2000])
x = collect(1.0:20.0); y = 2.0 .+ 0.5 .* x .+ 0.1 .* sin.(x)
a, b, R2, seb, res = linreg(x, y)
put!("linreg", "a", a); put!("linreg", "b", b); put!("linreg", "R2", R2)
put!("aicc", "n40_rss10_k3", _hp_aicc(40, 10.0, 3))
pv, lo, hi = _hp_wald_ci(7, 20)
put!("wald", "p", pv); put!("wald", "lo", lo); put!("wald", "hi", hi)
xr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]; yr = [1.1, 2.3, 2.9, 4.2, 5.1, 5.8, 7.2, 7.9]
put!("spearman", "xy", cor(_hp_rankdata(xr), _hp_rankdata(yr)))

# ── 11. test11 honest: exact A² ─────────────────────────────────────────────
put!("test11", "A2_full", anderson_darling_stat(normalized_spacings(zeta)))

# ── write JSON ───────────────────────────────────────────────────────────────
function to_json(x::Any, ind::Int=0)
    pad = " " ^ ind
    if x isa Dict{String,Any}
        parts = String[]
        for k in sort(collect(keys(x)))
            push!(parts, pad * "  " * "\"$k\": " * to_json(x[k], ind + 2))
        end
        return "{\n" * join(parts, ",\n") * "\n" * pad * "}"
    elseif x isa AbstractFloat
        return @sprintf("%.17g", x)
    elseif x isa Integer
        return string(x)
    elseif x isa AbstractVector{Float64}
        return "[" * join([@sprintf("%.17g", v) for v in x], ", ") * "]"
    else
        return "\"" * string(x) * "\""
    end
end
open(outfile, "w") do io
    write(io, to_json(J))
end
println("golden written: ", outfile)
