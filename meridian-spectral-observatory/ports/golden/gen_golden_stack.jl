# gen_golden_stack.jl — golden anchors for the STACK layer (HP H1–H8 gates,
# RH stack metrics/presets, Monumental physics gallery) for the 4-language ports.
#
# Run: julia gen_golden_stack.jl <meridian_dir> <out_json>
#
# RNG POLICY (same as gen_golden.jl): Julia's MersenneTwister is dSFMT-based and
# NOT reproducible outside Julia. The canonical cross-language semantics are
# "the unmodified original kernels + classic MT19937 substituted everywhere".
# This generator globally replaces the MersenneTwister CONSTRUCTOR so every
# rand/randn inside the included original files consumes the classic MT19937
# stream. Every port (python/cpp/rust/go) implements the identical MT19937 and
# the identical call order, so anchors are bit-comparable across all languages.
# Semantics pinned here (documented in PORT_SPEC.md):
#   rand(RNG)          = classic genrand_res53 ((a>>5)*2^26 + (b>>6)) / 2^53
#   rand(RNG, lo:hi)   = lo + floor(Int, u * len)      (u = next res53 double)
#   rand(RNG, vec)     = vec[1 + floor(Int, u * len)]
#   randn(RNG)         = Box-Muller: 2 draws u1,u2; sqrt(-2 log u1) * cos(2π u2);
#                        u1 <= 0 is redrawn (u2 NOT consumed on redraw)
#   rand(RNG, UInt8)   = top 8 bits of the next UInt32

if length(ARGS) < 2
    println("usage: julia gen_golden_stack.jl <meridian_dir> <out_json>")
    exit(1)
end
mdir = abspath(ARGS[1])
outfile = abspath(ARGS[2])
ENV["HP_SA_NO_MENU"] = "1"          # never auto-open the HP console on include

import Random
using Printf, Statistics, LinearAlgebra

# ── Classic MT19937 (init_genrand) — verbatim from gen_golden.jl ─────────────
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

# ── MT19937RNG: drop-in replacement consumed by the included originals ───────
mutable struct MT19937RNG <: Random.AbstractRNG
    mt::MT19937Classic
end
MT19937RNG(seed::Integer) = MT19937RNG(MT19937Classic(seed))
Base.copy(r::MT19937RNG) = MT19937RNG(copy(r.mt))
_mtdouble(r::MT19937RNG) = Random.rand(r.mt, Float64)
Random.rand(r::MT19937RNG) = _mtdouble(r)
Random.rand(r::MT19937RNG, ::Type{Float64}) = _mtdouble(r)
function Random.randn(r::MT19937RNG)
    u1 = _mtdouble(r)
    while u1 <= 0.0
        u1 = _mtdouble(r)
    end
    u2 = _mtdouble(r)
    return sqrt(-2.0 * log(u1)) * cos(2.0 * π * u2)
end
function Random.rand(r::MT19937RNG, rge::UnitRange{Int})
    return first(rge) + floor(Int, _mtdouble(r) * length(rge))
end
function Random.rand(r::MT19937RNG, a::Vector{Float64})
    return a[1 + floor(Int, _mtdouble(r) * length(a))]
end
Random.rand(r::MT19937RNG, ::Type{UInt8}) = UInt8(_mt_next!(r.mt) >> 24)
function Random.rand(r::MT19937RNG, ::Type{UInt8}, n::Integer)
    return UInt8[_mt_next!(r.mt) >> 24 for _ in 1:n]
end
# randperm (H7 shuffled control / H8): canonical Fisher-Yates on the res53
# stream — j = 1 + floor(u*i) for i = n:-1:2, one double per step. Documented
# in PORT_SPEC.md; every port implements the identical routine.
function Random.randperm(r::MT19937RNG, n::Integer)
    a = collect(1:Int(n))
    for i in Int(n):-1:2
        j = 1 + floor(Int, _mtdouble(r) * i)
        a[i], a[j] = a[j], a[i]
    end
    return a
end
Random.Sampler(r::MT19937RNG, ::Type{UInt8}, ::Random.Repetition) = Random.SamplerTrivial(UInt8)
Random.Sampler(r::MT19937RNG, sp::Random.SamplerType{UInt8}, ::Val{1}) = Random.SamplerTrivial(UInt8)
Random.Sampler(r::MT19937RNG, ::Type{Float64}, ::Random.Repetition) = Random.SamplerTrivial(Float64)
Random.Sampler(r::MT19937RNG, sp::Random.SamplerType{Float64}, ::Val{1}) = Random.SamplerTrivial(Float64)
Random.rand(r::MT19937RNG, sp::Random.SamplerTrivial{Type{UInt8}}) = Random.rand(r, UInt8)
Random.rand(r::MT19937RNG, sp::Random.SamplerTrivial{Type{Float64}}) = _mtdouble(r)
Random.Sampler(::Type{MT19937RNG}, sp::Random.Sampler, ::Union{Val{1},Val{Inf}}) = sp
Random.rand(r::MT19937RNG, sp::Random.SamplerTrivial{DataType,Any}) = Random.rand(r, sp[])
function Random.rand!(r::MT19937RNG, A::Array{UInt8,1})
    for i in eachindex(A)
        A[i] = UInt8(_mt_next!(r.mt) >> 24)
    end
    return A
end

# ── GLOBAL SWAP: MersenneTwister(...) → MT19937RNG ───────────────────────────
println("methods(Random.MersenneTwister) before swap: ", length(methods(Random.MersenneTwister)))
for m in collect(methods(Random.MersenneTwister))
    Base.delete_method(m)
end
function Random.MersenneTwister(seed::Union{Nothing,Integer}=nothing; kwargs...)
    s = seed === nothing ? UInt32(0) : UInt32(mod(Int(seed), 2^32))
    return MT19937RNG(s)
end
# self-test: classic stream must match the ports (MT19937(5489))
_t = MT19937Classic(5489)
_u1 = Random.rand(_t, Float64)
_u2 = Random.rand(_t, Float64)
println("MT19937 self-test: d1=", _u1, " d2=", _u2)
@assert Random.MersenneTwister(42) isa MT19937RNG

J = Dict{String,Any}()
J["meta"] = Dict("julia" => string(VERSION), "rng" => "MT19937-classic global swap",
                 "randn" => "box-muller 2-draw cos",
                 "range" => "lo+floor(u*len)", "u8" => "top 8 bits of u32")
function put!(section::String, key::String, v::Float64)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
function puti!(section::String, key::String, v::Int)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
function puts!(section::String, key::String, v::String)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
function putb!(section::String, key::String, v::Bool)
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
function putv!(section::String, key::String, v::Vector{Float64})
    d = get!(() -> Dict{String,Any}(), J, section)
    d[key] = v
end
const FLOAT_RE = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
function _extract_floats(s::String; cap::Int = 60)
    out = Float64[]
    for m in eachmatch(FLOAT_RE, s)
        v = tryparse(Float64, m.match)
        v === nothing || push!(out, v)
        length(out) >= cap && break
    end
    return out
end
function _safe!(sec::String, key::String, thunk)
    try
        v = thunk()
        if v isa Float64; put!(sec, key, v)
        elseif v isa Int; puti!(sec, key, v)
        elseif v isa Bool; putb!(sec, key, v)
        else put!(sec, key, Float64(v))
        end
    catch err
        puts!(sec, key * "_ERR", sprint(showerror, err)[1:min(end, 140)])
    end
end
function _safev!(sec::String, key::String, thunk)
    try
        putv!(sec, key, Float64.(thunk()))
    catch err
        puts!(sec, key * "_ERR", sprint(showerror, err)[1:min(end, 140)])
    end
end

# generic structural dumper (NamedTuple/Dict/vectors -> flat key space)
function _dump_any!(sec::String, prefix::String, x, depth::Int = 0)
    depth > 3 && return
    if x isa NamedTuple
        for (k, v) in pairs(x)
            _dump_any!(sec, prefix * "_" * string(k), v, depth + 1)
        end
    elseif x isa Dict
        for (k, v) in sort!(collect(x); by = kv -> string(kv[1]))
            _dump_any!(sec, prefix * "_" * string(k), v, depth + 1)
        end
    elseif x isa AbstractFloat
        (isnan(x) || isinf(x)) || put!(sec, prefix, x)
    elseif x isa Bool
        putb!(sec, prefix, x)
    elseif x isa Integer
        puti!(sec, prefix, x)
    elseif x isa AbstractVector{Float64}
        length(x) <= 12 ? putv!(sec, prefix * "_v", x) :
            (puti!(sec, prefix * "_len", length(x)); putv!(sec, prefix * "_head", x[1:min(3, end)]))
    elseif x isa AbstractVector{Int}
        length(x) <= 12 ? putv!(sec, prefix * "_v", Float64.(x)) :
            (puti!(sec, prefix * "_len", length(x)); putv!(sec, prefix * "_head", Float64.(x[1:min(3, end)])))
    elseif x isa AbstractVector
        puti!(sec, prefix * "_len", length(x))
        isempty(x) || _dump_any!(sec, prefix * "_i1", x[1], depth + 1)
    end
end

# RNG semantics anchors (every port must reproduce these EXACTLY)
rr = MT19937RNG(9)
_safev!("rng_semantics", "doubles", () -> [Random.rand(rr) for _ in 1:5])
rr = MT19937RNG(11)
_safev!("rng_semantics", "randn", () -> [Random.randn(rr) for _ in 1:5])
rr = MT19937RNG(13)
_safev!("rng_semantics", "range", () -> Float64.(Random.rand.(Ref(rr), [1:7, 2:9, 1:40])))
rr = MT19937RNG(17)
_safev!("rng_semantics", "vecpick", () -> [Random.rand(rr, [1.0, -1.0]) for _ in 1:4])
rr = MT19937RNG(19)
_safev!("rng_semantics", "u8", () -> Float64.([Random.rand(rr, UInt8) for _ in 1:4]))
rr = MT19937RNG(23)
_safev!("rng_semantics", "u8array", () -> Float64.(Random.rand(rr, UInt8, 8)))

# ═════════════════════════════════════════════════════════════════════════════
# SECTION A — HP audit gates H1–H8 (hp_audit_standalone.jl, smoke battery)
# CAPTURE: run_battery_core records one MiniTestState per gate into
# ALL_STATES (status/headline/rows/notes/console) — no monkey-patching needed
# (a naive rep_begin!/rep_finish! redefinition recurses infinitely in Julia:
# the "captured original" and the new method share one generic function).
# ═════════════════════════════════════════════════════════════════════════════
println("=== A: HP battery ===")
const _HP_BATTERY_JL = get(ENV, "HP_BATTERY_JL", "")

if !isempty(_HP_BATTERY_JL)
    # Fast path: load the pre-computed battery checkpoint (a Julia literal
    # file produced from gen_hp_battery.jl's JSON output) and merge it in.
    include(abspath(_HP_BATTERY_JL))     # defines J_HP::Dict{String,Any}
    for k in keys(J_HP)
        J[string(k)] = J_HP[k]
    end
    println("battery loaded from checkpoint: ", sort(collect(keys(J_HP))))
else
    include(joinpath(mdir, "hp_audit_standalone.jl"))  # module HPMeridian in Main

    # The original _hp_std_vortices is typed `rng::MersenneTwister` (the dSFMT
    # type), so under the global MT19937 swap the dispatch fails. Rebind it with
    # an untyped rng — SAME body, only the type annotation removed. (No
    # rep_begin!/rep_finish! monkey-patching: in Julia the "captured original"
    # and the redefined method share one generic function object, so the naive
    # wrapper recurses into itself -> StackOverflowError. The verdict capture
    # reads HPMeridian.ALL_STATES instead — see below.)
    HPMeridian.eval(quote
        function _hp_std_vortices(cfg::HPConfig, L::Int, rng)
            Nv = resolve_vortex_count(cfg)
            q_mag = resolve_q_magnitude(cfg)
            return Nv == 0 ? Vortex[] :
                   random_vortex_configuration(Nv, L, L; q_magnitude = q_mag,
                                               enforce_neutrality = true, rng = rng,
                                               place_at_centers = true)
        end
    end)

    hprundir = mkpath(joinpath(tempdir(), "hp_gold_stack_run"))
    n_prev = length(HPMeridian.ALL_STATES)
    cd(hprundir) do
        cfg = HPMeridian.make_hp_config()
        HPMeridian.apply_preset!(cfg, :smoke)
        HPMeridian.register_audits!()          # main() does this before the battery
        zeros_path = joinpath(mdir, "zeros50k.txt")
        HPMeridian.run_battery_core(cfg, collect(1:8), "smoke"; zeros_path = zeros_path)
    end
    fresh = HPMeridian.ALL_STATES[n_prev+1:end]
    println("gates captured: ", [st.id for st in fresh])
    for st in fresh
        k = st.id - 300
        (1 <= k <= 8) || continue
        sec = "hp_gate_H$k"
        puts!(sec, "verdict", st.status)
        puts!(sec, "headline", st.headline)
        src_lines = String[]
        for (nm, ok, val) in st.rows
            push!(src_lines, string(nm) * " = " * string(val))
        end
        append!(src_lines, st.notes)
        for ln in split(st.console, '\n'; keepempty = false)
            push!(src_lines, String(ln))
        end
        floats = vcat(_extract_floats.(src_lines; cap = 60)..., _extract_floats(st.headline))
        puti!(sec, "n_floats", length(floats))
        for (i, v) in enumerate(floats[1:min(end, 40)])
            put!(sec, @sprintf("f%02d", i), v)
        end
    end
    for k in 1:8
        haskey(J, "hp_gate_H$k") || puts!("hp_gate_H$k", "verdict", "ABSENT")
    end
end

# ═════════════════════════════════════════════════════════════════════════════
# SECTION B — RH stack (RH_Sweep_Pro.jl canonical metrics + RH_Unified_v5 extras)
# ═════════════════════════════════════════════════════════════════════════════
println("=== B: RH stack ===")
module RHSP
include(joinpath(ARGS[1], "RH_Sweep_Pro.jl"))
end
module RHU5
include(joinpath(ARGS[1], "RH_Unified_v5.jl"))
end

_rhcfg = RHSP.default_config()
_H16 = RHSP.build_hamiltonian_with_config(16, 1.0 / π, 2.0, 0.5, 0, _rhcfg)
eigs16 = RHSP.central_eigs_sorted(_H16; window = 0.3)
puti!("rh", "n_eigs16", length(eigs16))
putv!("rh", "eigs16_head", eigs16[1:min(3, end)])
putv!("rh", "eigs16_tail", eigs16[max(1, end-2):end])

mres = RHSP.compute_all_metrics(eigs16, RHSP.get_zeta_zeros_safe(500);
                                label = "anchor16", L = 16, alpha = 1.0 / π,
                                W = 2.0, sigma = 0.5, seed = 0, eigs_per_seed = 0)
println("B-step: SP metrics done"); flush(stdout)
println("B-step: field extraction SP"); flush(stdout)
for f in fieldnames(typeof(mres))
    v = getfield(mres, f)
    if v isa Float64 && !isnan(v); put!("rh_metrics_sp", string(f), v); end
    if v isa Bool; putb!("rh_metrics_sp", string(f), v); end
    if v isa Int; puti!("rh_metrics_sp", string(f), v); end
end

mres5 = RHU5.compute_all_metrics(eigs16, RHU5.get_zeta_zeros_safe(500);
                                 label = "anchor16", L = 16, alpha = 1.0 / π,
                                 W = 2.0, sigma = 0.5, seed = 0, eigs_per_seed = 0)
println("B-step: v5 metrics done"); flush(stdout)
println("B-step: field extraction v5"); flush(stdout)
for f in fieldnames(typeof(mres5))
    v = getfield(mres5, f)
    if v isa Float64 && !isnan(v); put!("rh_metrics_v5", string(f), v); end
    if v isa Bool; putb!("rh_metrics_v5", string(f), v); end
    if v isa Int; puti!("rh_metrics_v5", string(f), v); end
end

println("B-step: byte diag"); flush(stdout)
r_mean16 = mean(RHSP.spacing_ratios(eigs16))
bd = RHU5.compute_byte_level_diagnostics(eigs16, r_mean16; n_bytes = 200_000, seed = 12345)
put!("rh_byte", "r_byte_quantized", bd.r_byte_quantized)
put!("rh_byte", "byte_quant_diff", bd.byte_quant_diff)
putb!("rh_byte", "byte_quant_robust", bd.byte_quant_robust)
put!("rh_byte", "rng_entropy_bits", bd.rng_entropy_bits)
put!("rh_byte", "rng_chi2_z", bd.rng_chi2_z)
putb!("rh_byte", "rng_uniform_ok", bd.rng_uniform_ok)
putb!("rh_byte", "byte_match", bd.byte_match)

println("B-step: presets"); flush(stdout)
pa = RHSP.preset_auto(100)
puti!("rh_presets", "auto_L", pa.L); puti!("rh_presets", "auto_seeds", pa.n_seeds)
puti!("rh_presets", "auto_nzz", pa.n_zeta_zeros)
pb = RHSP.preset_balanced(100; max_time_minutes = 2)
puti!("rh_presets", "balanced_L", pb.L); puti!("rh_presets", "balanced_seeds", pb.n_seeds)
pi_ = RHSP.preset_irrational(:phi)
put!("rh_presets", "irrational_phi_alpha", Float64(pi_.alpha))
ma, ml = RHSP.generate_extended_magic_alphas()
puti!("rh_alphas", "ext_n", length(ma))
putv!("rh_alphas", "ext_head", Float64.(ma[1:6]))
putv!("rh_alphas", "ext_tail", Float64.(ma[end-5:end]))
puti!("rh_alphas", "magic_n", length(RHSP.MAGIC_ALPHA_VALUES))

# ═════════════════════════════════════════════════════════════════════════════
# SECTION C — Monumental physics gallery (AB_Cloud_Monumental_v6_3.jl)
# ═════════════════════════════════════════════════════════════════════════════
println("=== C: Monumental ===")
include(joinpath(mdir, "AB_Cloud_Monumental_v6_3.jl"))
const M = AB_Cloud_Monumental

function _mono_eigs(L::Int, α::Float64; W = 2.0, σ = 0.0, seed = 0)
    H = M.build_ab_cloud_hamiltonian(L, α; W = W, sigma = σ, seed = seed)
    return sort(real.(eigvals(Hermitian(H))))
end
function _store_spec(sec, e)
    putv!(sec, "head", e[1:min(3, end)])
    putv!(sec, "tail", e[max(1, end-2):end])
    put!(sec, "mid", e[div(length(e), 2)])
    return e
end

e12 = _store_spec("mon_spec_L12a13", _mono_eigs(12, 1.0 / 3.0))
e12h = _store_spec("mon_spec_L12a12", _mono_eigs(12, 0.5))
e16 = _store_spec("mon_spec_L16a25", _mono_eigs(16, 0.4))
e16s = _store_spec("mon_spec_L16a13_s05_seed7", _mono_eigs(16, 1.0 / 3.0; W = 2.0, σ = 0.5, seed = 7))

sr12 = M.spacing_ratios(e12)
put!("mon_stats", "r_L12a13", mean(sr12))
put!("mon_stats", "fGUE_L12a13", M.f_GUE_score(e12))
ch = M.chirality_index(e12)
put!("mon_stats", "chirality_mean", ch[1]); put!("mon_stats", "chirality_spread", ch[2])
_safev!("mon_stats", "numvar", () -> M.number_variance(e12, [1.0, 2.0, 4.0]))
_safev!("mon_stats", "sff", () -> M.spectral_form_factor(e12, [0.5, 1.0, 2.0]))

H12 = M.build_ab_cloud_hamiltonian(12, 0.5; W = 2.0, sigma = 0.0, seed = 0)
E12 = eigen(Hermitian(H12))
psi = E12.vectors[:, div(144, 2)]
_dump_any!("mon_entropy", "mf", M.multifractal_spectrum(12, 0.5, 2.0, 0.0; seed = 0, n_states = 2, qs = -4.0:1.0:4.0))
_dump_any!("mon_entropy", "ipr", M.ipr_scaling([12, 16], 0.5, 2.0, 0.0))
_dump_any!("mon_entropy", "tee", M.topological_entanglement_entropy(12, 0.5, 2.0, 0.0;
        seed = 0, n_states = 3, subsystem_fractions = [0.25, 0.5, 0.75]))
_safe!("mon_entropy", "vne_mid", () -> M.von_neumann_entropy(psi, 12, 0.5))
_safe!("mon_entropy", "lyapunov", () -> M.lyapunov_exponent(12, 0.5, 2.0, 0.0).gamma_mean)

_dump_any!("mon_topology", "chern_13", M.first_chern_number(1.0 / 3.0; band_index = 0, n_k = 40))
_dump_any!("mon_topology", "chern_12", M.first_chern_number(0.5; band_index = 0, n_k = 40))
_dump_any!("mon_topology", "chern_23", M.first_chern_number(2.0 / 3.0; band_index = 0, n_k = 40))
_dump_any!("mon_topology", "bott", M.bott_index(12, 0.5, 2.0, 0.0; seed = 0))
_dump_any!("mon_topology", "z2", M.z2_invariant_kane_mele(12, 0.5, 2.0, 0.0))
_dump_any!("mon_topology", "chiral_winding", M.chiral_winding_number(0.5; n_k = 60))
_dump_any!("mon_topology", "index_theorem", M.index_theorem_chiral(12, 0.5, 2.0, 0.0))
_dump_any!("mon_topology", "eta", M.eta_invariant(12, 1.0 / 3.0, 2.0, 0.0))
_dump_any!("mon_topology", "second_chern", M.second_chern_class_4d(0.5; n_k = 12))
_dump_any!("mon_topology", "vw_sumrule", M.vortex_winding_sum_rule(8, 0.5; custom_n_vortices = [2, 6]))
_dump_any!("mon_topology", "ab_phase", M.ab_phase_winding_per_vortex(8, 1.0 / 3.0; R_loop = 2.0, n_theta = 64))

put!("mon_zeta", "rvN_50", M.riemann_von_mangoldt_N(50.0))
_safev!("mon_zeta", "unfold_head", () -> M.unfold_zeta_zeros(M.zeta_zeros(100))[1:3])
_safev!("mon_zeta", "paircorr", () -> M.pair_correlation_zeta(M.zeta_zeros(100), [1.0, 2.0, 3.0]))
put!("mon_zeta", "bk_sigma_1000", M.bogomolny_keating_sigma(1000))

_safev!("mon_sweep", "alpha_r_mean", () -> M.sweep_alpha(L = 12, W = 2.0, sigma = 0.0,
        alpha_grid = [1.0 / 3.0, 0.5], n_realizations = 2).r_mean)
_safev!("mon_sweep", "alpha_fGUE", () -> M.sweep_alpha(L = 12, W = 2.0, sigma = 0.0,
        alpha_grid = [1.0 / 3.0, 0.5], n_realizations = 2).f_GUE)

primes = M.sieve_of_eratosthenes(50)
puti!("mon_nt", "pi_50", length(primes))
pcarr = M.prime_counting(100)
puti!("mon_nt", "pi_100", pcarr[end])
mu = M.mobius_function(100)
puti!("mon_nt", "mobius_sum100", sum(mu))
ms = M.mobius_sum(100)
puti!("mon_nt", "mertens_100", ms[end])
gaps, pr = M.prime_gaps(100)
puti!("mon_nt", "gaps_n", length(gaps))
putv!("mon_nt", "gaps_head", Float64.(gaps[1:min(5, end)]))

_safe!("mon_tasks", "v01_herm_err", () -> M.v01(L = 12, W = 2.0, sigma = 0.0, seed = 0).hermitian_error)
_safe!("mon_tasks", "v01_passes", () -> M.v01(L = 12, W = 2.0, sigma = 0.0, seed = 0).passes)
_safe!("mon_tasks", "v05_all_pass", () -> M.v05(L = 12).all_pass)
_safe!("mon_tasks", "v50_nv", () -> M.v50().n_vortices)
_dump_any!("mon_tasks", "v100", M.v100())

# ═════════════════════════════════════════════════════════════════════════════
# write JSON
# ═════════════════════════════════════════════════════════════════════════════
function to_json(x::Any, ind::Int = 0)
    pad = " " ^ ind
    if x isa Dict{String,Any}
        parts = String[]
        for k in sort(collect(keys(x)))
            push!(parts, pad * "  " * "\"$k\": " * to_json(x[k], ind + 2))
        end
        return "{\n" * join(parts, ",\n") * "\n" * pad * "}"
    elseif x isa AbstractFloat
        (isnan(x) || isinf(x)) && return "null"
        return @sprintf("%.17g", x)
    elseif x isa Bool
        return x ? "true" : "false"
    elseif x isa Integer
        return string(x)
    elseif x isa AbstractVector{Float64}
        return "[" * join([(isnan(v) || isinf(v)) ? "null" : @sprintf("%.17g", v) for v in x], ", ") * "]"
    else
        s = string(x)
        s = replace(s, "\\" => "\\\\")
        s = replace(s, "\"" => "\\\"")
        s = replace(s, "\n" => "\\n")
        return "\"" * s * "\""
    end
end
open(outfile, "w") do io
    write(io, to_json(J))
end
println("golden stack written: ", outfile)
