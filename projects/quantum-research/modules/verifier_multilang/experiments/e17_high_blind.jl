# e17_high_blind.jl — ЭКСПЕРИМЕНТ 17: слепое обнаружение нулей ζ на высоте
# T = 1000 ДВУМЯ НЕЗАВИСИМЫМИ ДВИЖКАМИ (обязательство O-J1).
#
# Дисциплина слепоты (наследует Э-11):
#   A. ДВА ДЕТЕКТОРА (этот файл):
#      движок A — Эйлер–Маклорен с масштабируемым расписанием em_schedule
#                 (N = 64·2^k ≥ 0.512·t, K = 14), окно [0.3, 1000];
#      движок B — Риман–Зигель (Ариас де Рейна, e16_rs_engine.jl),
#                 окно [50, 1000].
#      Ни один не содержит эталонных нулей. Выходы фиксируются + хешируются
#      SHA256 ДО всякой валидации.
#   B. ВАЛИДАТОР (e17_validator.jl): запускается отдельно ПОСЛЕ фиксации хешей;
#      эталон — таблица mpmath.zetazero (results/e17_zetazero_reference.csv,
#      SHA256 проверяется при загрузке) + независимое расписание ЭМ (320,12)
#      + контроль полноты N(1000) по стандартному пути (принцип аргумента).

module HighBlind

using ..ZetaDetector
using ..RiemannSiegel
using SHA
using Printf

export zeta_line_em, zeta_line_rs, unwrapped_arg_generic, refine_zero_generic,
       detect_zeros_generic, run_detector_A, run_detector_B, standard_path_N

const OUTDIR = joinpath(@__DIR__, "..", "results")

zeta_line_em(t::Float64) = reference_em(t)
zeta_line_rs(t::Float64) = zeta_rs(t)

"""
Сетка t на [t0, t1] с шагом h; значения ζ(½+it) заданным движком; непрерывно
продолженный (развёрнутый) аргумент. Возвращает (ts, args, mags).
"""
function unwrapped_arg_generic(engine::Function, t0::Float64, t1::Float64, h::Float64)
    n = Int(ceil((t1 - t0) / h)) + 1
    ts = [t0 + h * i for i in 0:n-1]
    args = Vector{Float64}(undef, n)
    mags = Vector{Float64}(undef, n)
    prev_angle = 0.0
    for (i, t) in enumerate(ts)
        v = engine(t)
        mags[i] = Float64(abs(v))
        a = Float64(angle(v))
        if i == 1
            args[i] = a
        else
            d = a - prev_angle
            d = mod(d + Float64(π), Float64(2π)) - Float64(π)
            args[i] = args[i-1] + d
        end
        prev_angle = a
    end
    return ts, args, mags
end

"Уточнение нуля на скобке [ta, tb] золотым сечением по |ζ(½+it)| заданного движка."
function refine_zero_generic(engine::Function, ta::Float64, tb::Float64;
                             tol::Float64 = 1e-14)
    φ = (sqrt(5.0) - 1) / 2
    a, b = ta, tb
    c = b - φ * (b - a)
    d = a + φ * (b - a)
    fc = Float64(abs(engine(c)))
    fd = Float64(abs(engine(d)))
    for _ in 1:160
        if fc < fd
            b = d; d = c; fd = fc
            c = b - φ * (b - a)
            fc = Float64(abs(engine(c)))
        else
            a = c; c = d; fc = fd
            d = a + φ * (b - a)
            fd = Float64(abs(engine(d)))
        end
        (b - a) < tol && break
    end
    tm = (a + b) / 2
    return tm, Float64(abs(engine(tm)))
end

"""
Слепое обнаружение нулей заданным движком: сетка h; интервал с |Δarg| > π/2
→ кандидат; уточнение золотым сечением. НИКАКИХ эталонных значений.
"""
function detect_zeros_generic(engine::Function, t0::Float64, t1::Float64, h::Float64)
    ts, args, mags = unwrapped_arg_generic(engine, t0, t1, h)
    w = abs(args[end] - args[1]) / Float64(π)
    positions = Float64[]
    zmin = Float64[]
    for i in 2:length(ts)
        darg = abs(args[i] - args[i-1])
        if darg > π / 2
            ta = max(ts[i-1] - 2h, t0)
            tb = min(ts[i] + 2h, t1)
            pos, zm = refine_zero_generic(engine, ta, tb)
            push!(positions, pos)
            push!(zmin, zm)
        end
    end
    return Dict("grid_h" => h, "t0" => t0, "t1" => t1,
                "n_grid_points" => length(ts),
                "winding_count" => w,
                "positions" => positions,
                "abs_zeta_at_positions" => zmin)
end

function _write_positions(io, det)
    for (i, (p, z)) in enumerate(zip(det["positions"], det["abs_zeta_at_positions"]))
        println(io, "position,", i, ",", @sprintf("%.15f", p), ",",
                @sprintf("%.3e", z))
    end
end

"Детектор A: Эйлер–Маклорен (масштабируемое расписание), [0.3, 1000], h=0.01."
function run_detector_A()
    det = detect_zeros_generic(zeta_line_em, 0.3, 1000.0, 0.01)
    out_path = joinpath(OUTDIR, "e17_detector_em.csv")
    open(out_path, "w") do io
        println(io, "kind,key1,key2,value")
        println(io, "meta,engine,euler-maclaurin_scaled(N=64*2^k>=0.512t,K=14)")
        println(io, "meta,grid_h,", det["grid_h"])
        println(io, "meta,t0,", det["t0"])
        println(io, "meta,t1,", det["t1"])
        println(io, "meta,winding_count,", det["winding_count"])
        println(io, "meta,n_grid_points,", det["n_grid_points"])
        println(io, "meta,n_positions,", length(det["positions"]))
        _write_positions(io, det)
    end
    sha = open(out_path) do io
        bytes2hex(sha256(read(io)))
    end
    open(joinpath(OUTDIR, "e17_detector_em_sha256.txt"), "w") do io
        println(io, sha, "  e17_detector_em.csv")
    end
    return det, sha
end

"Детектор B: Риман–Зигель, [50, 1000], h=0.01."
function run_detector_B()
    det = detect_zeros_generic(zeta_line_rs, 50.0, 1000.0, 0.01)
    out_path = joinpath(OUTDIR, "e17_detector_rs.csv")
    open(out_path, "w") do io
        println(io, "kind,key1,key2,value")
        println(io, "meta,engine,riemann-siegel_arias-de-reyna")
        println(io, "meta,grid_h,", det["grid_h"])
        println(io, "meta,t0,", det["t0"])
        println(io, "meta,t1,", det["t1"])
        println(io, "meta,winding_count,", det["winding_count"])
        println(io, "meta,n_grid_points,", det["n_grid_points"])
        println(io, "meta,n_positions,", length(det["positions"]))
        _write_positions(io, det)
    end
    sha = open(out_path) do io
        bytes2hex(sha256(read(io)))
    end
    open(joinpath(OUTDIR, "e17_detector_rs_sha256.txt"), "w") do io
        println(io, sha, "  e17_detector_rs.csv")
    end
    return det, sha
end

"""
Контроль полноты: N(T) по стандартному пути 2 → 2+iT → ½+iT (свободному от
нулей), движок — масштабируемый Эйлер–Маклорен:
  S(T) = arg ζ(½+iT) (непрерывное продолжение по пути),
  N(T) = θ(T)/π + 1 + S(T)/π   (Риман–фон Мангольдт).
"""
function standard_path_N(T::Float64; h::Float64 = 0.1, hx::Float64 = 0.01)
    half = BigFloat("0.5")
    arg = 0.0
    n1 = Int(ceil(T / h))
    prev = Float64(angle(zeta_em_scaled(complex(BigFloat(2), BigFloat(0));
                                        N = 64, K = 14)))
    for i in 1:n1
        t = min(T, i * h)
        Nsch, Ksch = em_schedule(t)
        a = Float64(angle(zeta_em_scaled(complex(BigFloat(2), BigFloat(t));
                                         N = Nsch, K = Ksch)))
        d = a - prev
        d = mod(d + Float64(π), Float64(2π)) - Float64(π)
        arg += d
        prev = a
        t >= T && break
    end
    prev = Float64(angle(zeta_em_scaled(complex(BigFloat(2), BigFloat(T));
                                        N = em_schedule(T)[1], K = 14)))
    n2 = Int(ceil(1.5 / hx))
    for i in 1:n2
        x = max(half, 2 - i * hx)
        Nsch = em_schedule(T)[1]
        a = Float64(angle(zeta_em_scaled(complex(BigFloat(x), BigFloat(T));
                                         N = Nsch, K = 14)))
        d = a - prev
        d = mod(d + Float64(π), Float64(2π)) - Float64(π)
        arg += d
        prev = a
        x <= half && break
    end
    S_T = arg
    theta_T = Float64(theta_big(T))
    N_rvm = theta_T / π + 1 + S_T / π
    return S_T, theta_T, N_rvm
end

end # module
