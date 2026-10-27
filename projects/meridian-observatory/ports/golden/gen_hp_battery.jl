# gen_hp_battery.jl — HP gates H1–H8 (smoke) under the MT19937 swap.
# Writes the checkpoint JSON consumed by gen_golden_stack.jl (section A),
# so the long battery never has to live inside one big generation run.
#
# Run: julia gen_hp_battery.jl <meridian_dir> <out_json>

if length(ARGS) < 2
    println("usage: julia gen_hp_battery.jl <meridian_dir> <out_json>")
    exit(1)
end
mdir = abspath(ARGS[1])
outfile = abspath(ARGS[2])
ENV["HP_SA_NO_MENU"] = "1"

import Random
using Printf, Statistics, LinearAlgebra

# ── classic MT19937 + global swap — verbatim with gen_golden_stack.jl ────────
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
function Random.randperm(r::MT19937RNG, n::Integer)
    a = collect(1:Int(n))
    for i in Int(n):-1:2
        j = 1 + floor(Int, _mtdouble(r) * i)
        a[i], a[j] = a[j], a[i]
    end
    return a
end
Random.Sampler(r::MT19937RNG, ::Type{UInt8}, ::Random.Repetition) = Random.SamplerTrivial(UInt8)
Random.Sampler(r::MT19937RNG, ::Type{Float64}, ::Random.Repetition) = Random.SamplerTrivial(Float64)
Random.rand(r::MT19937RNG, sp::Random.SamplerTrivial{Type{UInt8}}) = Random.rand(r, UInt8)
Random.rand(r::MT19937RNG, sp::Random.SamplerTrivial{Type{Float64}}) = _mtdouble(r)
Random.Sampler(::Type{MT19937RNG}, sp::Random.Sampler, ::Union{Val{1},Val{Inf}}) = sp
Random.rand!(r::MT19937RNG, A::Array{UInt8,1}) = (for i in eachindex(A)
    A[i] = UInt8(_mt_next!(r.mt) >> 24)
end; A)
Random.rand!(r::MT19937RNG, A::Array{Float64}) = (for i in eachindex(A)
    A[i] = _mtdouble(r)
end; A)

for m in collect(methods(Random.MersenneTwister))
    Base.delete_method(m)
end
function Random.MersenneTwister(seed::Union{Nothing,Integer}=nothing; kwargs...)
    s = seed === nothing ? UInt32(0) : UInt32(mod(Int(seed), 2^32))
    return MT19937RNG(s)
end

# ── battery ──────────────────────────────────────────────────────────────────
include(joinpath(mdir, "hp_audit_standalone.jl"))
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

J = Dict{String,Any}()
J["meta"] = Dict("provenance" => "gen_hp_battery.jl checkpoint (HP smoke battery, MT19937 swap)")
hprundir = mkpath(joinpath(tempdir(), "hp_gold_stack_run"))
n_prev = length(HPMeridian.ALL_STATES)
cd(hprundir) do
    cfg = HPMeridian.make_hp_config()
    HPMeridian.apply_preset!(cfg, :smoke)
    HPMeridian.register_audits!()
    zeros_path = joinpath(mdir, "zeros50k.txt")
    HPMeridian.run_battery_core(cfg, collect(1:8), "smoke"; zeros_path = zeros_path)
end
fresh = HPMeridian.ALL_STATES[n_prev+1:end]
println("gates captured: ", [st.id for st in fresh])
for st in fresh
    k = st.id - 300
    (1 <= k <= 8) || continue
    sec = Dict{String,Any}()
    sec["verdict"] = st.status
    sec["headline"] = st.headline
    src_lines = String[]
    for (nm, ok, val) in st.rows
        push!(src_lines, string(nm) * " = " * string(val))
    end
    append!(src_lines, st.notes)
    for ln in split(st.console, '\n'; keepempty = false)
        push!(src_lines, String(ln))
    end
    floats = vcat(_extract_floats.(src_lines; cap = 60)..., _extract_floats(st.headline))
    sec["n_floats"] = length(floats)
    for (i, v) in enumerate(floats[1:min(end, 40)])
        sec[@sprintf("f%02d", i)] = v
    end
    J["hp_gate_H$k"] = sec
    println("H$k: ", st.status, " | ", st.headline[1:min(end, 90)])
end
for k in 1:8
    haskey(J, "hp_gate_H$k") || (J["hp_gate_H$k"] = Dict{String,Any}("verdict" => "ABSENT"))
end

# ── JSON writer (same conventions as gen_golden*.jl) ─────────────────────────
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
println("hp battery checkpoint written: ", outfile)
