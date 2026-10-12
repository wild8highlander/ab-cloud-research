# e18_baselines.jl — ЭКСПЕРИМЕНТ 18: компилятор против СИЛЬНЫХ baseline
# при РАВНЫХ ограничениях (обязательство O-J2, класс B гипотез).
#
# Постановка. Все методы обязаны выдавать программу В ТОМ ЖЕ ISA
# (двухуровневые блоки AB2 + диагональные фазы PHASE) и сравниваются на
# ОДНОМ независимом наборе целей (новые seeds 41800+, НЕ совпадающие с
# V20/E02): структурированные матрицы + Haar 4×4 (40 шт.) + Haar 8×8
# (20 шт.) + испорченный контроль.
#
# Методы:
#   ABQP — компилятор пакета (Givens-QR, замкнутая форма, без оптимизации);
#          передаётся колбэком из run_all.jl (настоящий lib_abqp.jl);
#   BL1  — наивный Givens: прямой порядок строк, без пропуска пренебрежимых
#          элементов (верхняя оценка бюджета замкнутой формы);
#   BL2  — учебная Эйлер-декомпозиция каждого 2×2 блока W = D1·G(θ)·D2:
#          1 AB2 + 4 PHASE на блок; слияние соседних фаз НЕ выполняется
#          (как в учебных реализациях); программа численно та же, что у
#          BL1 — различие в честно подсчитанном бюджете примитивов;
#   BL4  — Хаусхолдер-QR (d−1 отражений), каждое разложено в двухуровневые
#          вращения H = S†·P·S: 2m блоков AB2 + 2 PHASE на отражение;
#   BL3  — численный coordinate descent по ТОЧНО тем же слотам программы,
#          что у ABQP (равный бюджет примитивов), случайная инициализация,
#          покоординатный золотой поиск: 3 рестарта × 200 свипов (4×4),
#          1 × 100 (8×8);
#   BL5  — случайный поиск по тем же слотам: 3000 (4×4) / 300 (8×8) проб.
#
# Предрегистрированные пороги (results/ROADMAP.md, O-J2; протокол E18):
#   (i)   ABQP: 1−F ≤ 1e-12 на 100% независимого набора;
#   (ii)  примитивов у ABQP ≤ каждой точной ISA-baseline (BL1/BL2/BL4)
#         на каждой цели;
#   (iii) медиана времени компиляции ABQP × 50 ≤ медианы BL3
#         (подмножество Haar 4×4);
#   (iv)  контроль identity: 0 блоков AB2; испорченная цель компилируется
#         (1−F ≤ 0.01).
# Честная фиксация вне порогов: 2q-эквивалент ABQP сравнивается с
# теоретическим KAK-оптимумом (3 CNOT для 4×4; Vidal–Dawson 2004) как
# КОНТЕКСТ вне ISA-класса сравнения — превосходство по этой метрике
# НЕ заявляется.
#
# Только стандартные библиотеки Julia.

module E18Baselines

using LinearAlgebra, Random, Statistics, Printf, Dates

export run_e18, time_ms_e18

const OUTDIR = joinpath(@__DIR__, "..", "results")
mkpath(OUTDIR)

fidelity18(U, V) = abs(tr(U' * V))^2 / size(U, 1)^2

"2q-эквивалент блока на уровнях (c, r): та же конвенция CNOT-маршрутизации,
что в rpbridge/compiler.py пакета AB Quantum Processor (h = popcount XOR)."
twoq_equiv18(c::Int, r::Int) = begin
    h = count_ones((c - 1) ⊻ (r - 1))
    h == 1 ? 1 : 2h - 1
end

function time_ms_e18(f::Function, reps::Int)
    ts = Vector{Float64}(undef, reps)
    for i in 1:reps
        ts[i] = @elapsed f()
    end
    return 1e3 * median(ts)
end

# ────────────────────────── цели протокола ──────────────────────────

function haar18(rng::AbstractRNG, d::Int)
    A = (randn(rng, d, d) + im * randn(rng, d, d)) ./ sqrt(2)
    Q, R = qr(A)
    Qm = Matrix(Q)
    ph = [iszero(x) ? 1.0 + 0im : x / abs(x) for x in diag(Matrix(R))]
    return Qm * Diagonal(ph)
end

"Независимый набор целей E18 (seeds 41800+, НЕ пересекаются с V20/E02)."
function build_targets()
    H2 = ComplexF64[1 1; 1 -1] ./ sqrt(2)
    P2 = ComplexF64[1 0; 0 im]
    tg = Vector{NamedTuple{(:id, :family, :d, :seed, :U)}}()
    push!(tg, (id = "identity4", family = "structured", d = 4, seed = 0,
               U = Matrix{ComplexF64}(I, 4, 4)))
    push!(tg, (id = "DFT4", family = "structured", d = 4, seed = 0,
               U = ComplexF64[cis(2π * j * k / 4) / 2 for j in 0:3, k in 0:3]))
    push!(tg, (id = "DFT8", family = "structured", d = 8, seed = 0,
               U = ComplexF64[cis(2π * j * k / 8) / sqrt(8) for j in 0:7, k in 0:7]))
    push!(tg, (id = "clifford4_kronHP", family = "structured", d = 4, seed = 0,
               U = kron(H2, P2)))
    push!(tg, (id = "clifford8_kronHHH", family = "structured", d = 8, seed = 0,
               U = kron(H2, H2, H2)))
    push!(tg, (id = "permutation4", family = "structured", d = 4, seed = 0,
               U = ComplexF64.(circshift(Matrix{Float64}(I, 4, 4), (1, 0)))))
    push!(tg, (id = "permutation8_shift3", family = "structured", d = 8, seed = 0,
               U = ComplexF64.(circshift(Matrix{Float64}(I, 8, 8), (3, 0)))))
    rngD4 = MersenneTwister(41800)
    push!(tg, (id = "diagonal4", family = "structured", d = 4, seed = 41800,
               U = Matrix{ComplexF64}(Diagonal(cis.(2π * rand(rngD4, 4))))))
    rngD8 = MersenneTwister(41801)
    push!(tg, (id = "diagonal8", family = "structured", d = 8, seed = 41801,
               U = Matrix{ComplexF64}(Diagonal(cis.(2π * rand(rngD8, 8))))))
    # испорченный контроль: компилятор обязан завершиться и выдать программу
    Uc = ComplexF64[cis(2π * j * k / 4) / 2 for j in 0:3, k in 0:3]
    Uc[2, 3] += 1e-3
    push!(tg, (id = "corrupted_DFT4_plus_1e-3", family = "control", d = 4,
               seed = 0, U = Uc))
    # Haar-наборы (новые seeds)
    for i in 1:40
        push!(tg, (id = @sprintf("haar4_%02d", i), family = "haar4", d = 4,
                   seed = 41810 + i, U = haar18(MersenneTwister(41810 + i), 4)))
    end
    for i in 1:20
        push!(tg, (id = @sprintf("haar8_%02d", i), family = "haar8", d = 8,
                   seed = 41910 + i, U = haar18(MersenneTwister(41910 + i), 8)))
    end
    return tg
end

# ────────────────────────── точные baseline ──────────────────────────

"BL1: наивный Givens-QR (прямой порядок строк, без пропусков)."
function naive_givens(U::AbstractMatrix{ComplexF64})
    d = size(U, 1)
    R = copy(U)
    vals = Vector{NTuple{4,ComplexF64}}()
    idx = Vector{Tuple{Int,Int}}()
    for c in 1:d-1, r in c+1:d
        a, b = R[c, c], R[r, c]
        iszero(b) && continue          # точный нуль: вращение тождественно
        nr = hypot(abs(a), abs(b))     # порогового пропуска НЕТ (skip_eps = 0)
        w11 = conj(a) / nr; w12 = conj(b) / nr
        w21 = -b / nr;      w22 = a / nr
        rc = Vector{ComplexF64}(@view R[c, :])
        rr = Vector{ComplexF64}(@view R[r, :])
        @inbounds for j in 1:d
            R[c, j] = w11 * rc[j] + w12 * rr[j]
            R[r, j] = w21 * rc[j] + w22 * rr[j]
        end
        push!(vals, (w11, w12, w21, w22))
        push!(idx, (c, r))
    end
    dph = [iszero(R[i, i]) ? 1.0 + 0im : R[i, i] / abs(R[i, i]) for i in 1:d]
    off = norm(R - Diagonal(diag(R)), Inf)
    return vals, idx, dph, off
end

"Сборка программы V = W₁'···W_k'·D (право-мультипликативное внедрение —
та же конвенция, что в lib_abqp.jl, независимая реализация)."
function assemble18(vals, idx, dph, d::Int)
    V = Matrix{ComplexF64}(I, d, d)
    for (bi, (c, r)) in enumerate(idx)
        w11, w12, w21, w22 = vals[bi]
        colc = Vector{ComplexF64}(@view V[:, c])
        colr = Vector{ComplexF64}(@view V[:, r])
        @inbounds for i in 1:d
            V[i, c] = colc[i] * conj(w11) + colr[i] * conj(w12)
            V[i, r] = colc[i] * conj(w21) + colr[i] * conj(w22)
        end
    end
    return V * Diagonal(dph)
end

"BL2: учебная Эйлер-декомпозиция W = D1·G(θ)·D2 каждого 2×2 блока.
Возвращает (n_ab2, n_phase, max_reconstruction_err)."
function euler_zyz_counts(vals, idx, dph, d::Int)
    n_ab2 = 0
    n_ph = d                       # финальная диагональ программы
    maxerr = 0.0
    for bi in eachindex(idx)
        w11, w12, w21, w22 = vals[bi]
        ct, st = abs(w11), abs(w21)
        nrm = hypot(ct, st)
        ct /= nrm; st /= nrm
        if st < 1e-13
            n_ph += 2              # блок диагонален: только фазы пары
        else
            n_ab2 += 1             # вещественное вращение G(θ)
            n_ph += 4              # D1 (2 фазы) до + D2 (2 фазы) после
            e1 = st > 1e-13 ? w21 / abs(w21) :
                 (ct > 1e-13 ? w11 / ct : 1.0 + 0.0im)
            if ct > 1e-13
                d1 = w11 / (ct * e1)
                d2 = w21 / (st * e1)
                e2 = -w12 / (d1 * st)
                G = [ct -st; st ct]
                Wrec = Diagonal([d1, d2]) * G * Diagonal([e1, e2])
                maxerr = max(maxerr, norm(Wrec - [w11 w12; w21 w22], Inf))
            else                    # θ = π/2: W ≈ [[0, w12], [w21, 0]]
                continue            # фазы + перестановка: реконструкция точна
            end
        end
    end
    return n_ab2, n_ph, maxerr
end

"BL4: Хаусхолдер-QR с разложением каждого отражения в двухуровневые
вращения. Возвращает (V, n_ab2, n_phase, offdiag, n_reflections)."
function householder_program(U::AbstractMatrix{ComplexF64})
    d = size(U, 1)
    R = copy(U)
    V = Matrix{ComplexF64}(I, d, d)
    n_ab2 = 0
    n_ph = 0
    n_refl = 0
    for k in 1:d-1
        a = Vector{ComplexF64}(R[k:end, k])
        m = length(a)
        nrm = norm(a)
        α = -(iszero(a[1]) ? 1.0 + 0.0im : a[1] / abs(a[1])) * nrm
        v = copy(a)                    # вектор отражения: v = a − α·e₁
        v[1] -= α
        norm(v) < 1e-13 * max(1.0, nrm) && continue   # столбец уже готов
        n_refl += 1
        # S: выравнивание v на e_1 вращениями (1, j) в подпространстве
        vv = copy(v)
        nrot = 0
        for j in m:-1:2
            abs(vv[j]) < 1e-14 && continue
            p, q = vv[1], vv[j]
            nr = hypot(abs(p), abs(q))
            t1 = conj(p) / nr * vv[1] + conj(q) / nr * vv[j]
            t2 = -q / nr * vv[1] + p / nr * vv[j]
            vv[1] = t1; vv[j] = t2
            nrot += 1
        end
        n_ab2 += 2 * nrot          # S и S†
        n_ph += 2                  # P (знак на уровне k)
        # H_k = I − 2vv'/(v'v); программа: V ← V·embed(H_k)†; R ← H_k·R
        H = Matrix{ComplexF64}(I, m, m)
        H .-= 2 .* (v * v') ./ dot(v, v)
        E = Matrix{ComplexF64}(I, d, d)
        E[k:end, k:end] .= H
        V = V * E'
        R[k:end, :] = H * R[k:end, :]
    end
    dph = [iszero(R[i, i]) ? 1.0 + 0im : R[i, i] / abs(R[i, i]) for i in 1:d]
    off = norm(R - Diagonal(diag(R)), Inf)
    V = V * Diagonal(dph)
    return V, n_ab2, n_ph + d, off, n_refl
end

# ─────────────────── численные baseline (BL3 / BL5) ───────────────────

"Сборка параметрической программы по слотам (без аллокаций, in-place)."
function assemble_params!(V::Matrix{ComplexF64}, slots, ψ, θ, λ, φ, χ)
    d = size(V, 1)
    fill!(V, 0.0 + 0.0im)
    @inbounds for i in 1:d
        V[i, i] = 1.0 + 0.0im
    end
    @inbounds for bi in eachindex(slots)
        c, r = slots[bi]
        ct = cos(θ[bi]); st = sin(θ[bi])
        w11 = ct * cis(λ[bi]); w12 = st * cis(φ[bi])
        w21 = -st * cis(-φ[bi]); w22 = ct * cis(-λ[bi])
        g = cis(χ[bi])
        w11 *= g; w12 *= g; w21 *= g; w22 *= g
        for i in 1:d
            a = V[i, c] * conj(w11) + V[i, r] * conj(w12)
            b = V[i, c] * conj(w21) + V[i, r] * conj(w22)
            V[i, c] = a; V[i, r] = b
        end
    end
    @inbounds for j in 1:d
        z = cis(ψ[j])
        for i in 1:d
            V[i, j] *= z
        end
    end
    return V
end

"1−F(U, V) без аллокаций: F = |tr(U'V)|²/d²."
function op_err18(U, V)
    s = 0.0 + 0.0im
    @inbounds for j in axes(U, 2), i in axes(U, 1)
        s += conj(U[i, j]) * V[i, j]
    end
    d = size(U, 1)
    return max(0.0, 1 - abs(s)^2 / d^2)
end

"Золотое сечение: минимизация f на [lo, hi]."
function golden_min(f::Function, lo0::Real, hi0::Real; iters::Int = 28)
    lo = Float64(lo0); hi = Float64(hi0)
    g = (sqrt(5) - 1) / 2
    x1 = hi - g * (hi - lo); x2 = lo + g * (hi - lo)
    f1 = f(x1); f2 = f(x2)
    for _ in 1:iters
        if f1 < f2
            hi = x2; x2 = x1; f2 = f1
            x1 = hi - g * (hi - lo); f1 = f(x1)
        else
            lo = x1; x1 = x2; f1 = f2
            x2 = lo + g * (hi - lo); f2 = f(x2)
        end
    end
    return (lo + hi) / 2
end

"BL3: coordinate descent по слотам ABQP (равный бюджет примитивов).
Возвращает (best_err, evaluations)."
function coord_optimize(U, slots; rng, restarts::Int, sweeps::Int)
    d = size(U, 1)
    k = length(slots)
    V = Matrix{ComplexF64}(undef, d, d)
    evals = 0
    best = Inf
    for _ in 1:restarts
        θ = [π * rand(rng) for _ in 1:k]
        λ = [2π * rand(rng) - π for _ in 1:k]
        φ = [2π * rand(rng) - π for _ in 1:k]
        χ = [2π * rand(rng) - π for _ in 1:k]
        ψ = [2π * rand(rng) - π for _ in 1:d]
        fcoord = function ()
            assemble_params!(V, slots, ψ, θ, λ, φ, χ)
            evals += 1
            op_err18(U, V)
        end
        cur = fcoord()
        best = min(best, cur)
        for _ in 1:sweeps
            for i in 1:d
                x = ψ[i]
                ψ[i] = golden_min(z -> begin
                    ψ[i] = z
                    e = fcoord()
                    ψ[i] = x
                    e
                end, -π, π)
                cur = fcoord()
            end
            for bi in 1:k
                for (arr, lo, hi) in ((θ, 0.0, π), (λ, -π, π), (φ, -π, π),
                                      (χ, -π, π))
                    x = arr[bi]
                    arr[bi] = golden_min(z -> begin
                        arr[bi] = z
                        e = fcoord()
                        arr[bi] = x
                        e
                    end, lo, hi)
                    cur = fcoord()
                end
            end
            best = min(best, cur)
        end
    end
    return best, evals
end

"BL5: случайный поиск по тем же слотам."
function random_search(U, slots; rng, samples::Int)
    d = size(U, 1)
    k = length(slots)
    V = Matrix{ComplexF64}(undef, d, d)
    best = Inf
    for _ in 1:samples
        θ = [π * rand(rng) for _ in 1:k]
        λ = [2π * rand(rng) - π for _ in 1:k]
        φ = [2π * rand(rng) - π for _ in 1:k]
        χ = [2π * rand(rng) - π for _ in 1:k]
        ψ = [2π * rand(rng) - π for _ in 1:d]
        assemble_params!(V, slots, ψ, θ, λ, φ, χ)
        best = min(best, op_err18(U, V))
    end
    return best, samples
end

# ────────────────────────── CSV ──────────────────────────

_csvstr(x) = string(x)
_csvstr(x::Missing) = "NA"
_csvstr(x::AbstractString) = replace(x, "," => ";")

function save18(name::AbstractString, rows::Vector{<:Dict})
    path = joinpath(OUTDIR, name * ".csv")
    ks = String[]
    for row in rows, k in keys(row)
        string(k) in ks || push!(ks, string(k))
    end
    open(path, "w") do io
        println(io, join(ks, ","))
        for row in rows
            println(io, join((_csvstr(get(row, k, "")) for k in ks), ","))
        end
    end
    return path
end

# ────────────────────────── главный прогон ──────────────────────────

"""
run_e18(abqp_compile) — полный протокол E18.

abqp_compile(U) -> NamedTuple(n_ab2, n_phase, twoq, one_minus_F, slots)
— колбэк НАСТОЯЩЕГО компилятора пакета (lib_abqp.givens_factors +
assemble_program); slots = (c, r) блоков для численных baseline.
"""
function run_e18(abqp_compile::Function)
    tg = build_targets()
    rows = Vector{Dict{String,Any}}()
    optrows = Vector{Dict{String,Any}}()
    println("  [E18] целей: ", length(tg),
            " (структурированные 9 + Haar 40×4×4 + Haar 20×8×8 + контроль)")

    for t in tg
        U = Matrix{ComplexF64}(t.U)
        d = t.d

        # ── ABQP (настоящий компилятор пакета) ──
        a = abqp_compile(U)
        ms_abqp = time_ms_e18(() -> abqp_compile(U), 25)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "ABQP",
                         "n_ab2" => a.n_ab2, "n_phase" => a.n_phase,
                         "n_total" => a.n_ab2 + a.n_phase,
                         "twoq_equiv" => a.twoq,
                         "one_minus_F" => @sprintf("%.17g", a.one_minus_F),
                         "compile_ms" => @sprintf("%.6f", ms_abqp),
                         "success_1e12" => a.one_minus_F <= 1e-12))

        # ── BL1: наивный Givens ──
        vals1, idx1, dph1, off1 = naive_givens(U)
        V1 = assemble18(vals1, idx1, dph1, d)
        e1 = max(0.0, 1 - fidelity18(U, V1))
        ms1 = time_ms_e18(() -> assemble18(naive_givens(U)[1],
                                           naive_givens(U)[2],
                                           naive_givens(U)[3], d), 15)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "BL1_naive_givens",
                         "n_ab2" => length(vals1), "n_phase" => d,
                         "n_total" => length(vals1) + d,
                         "twoq_equiv" => sum(twoq_equiv18(c, r)
                                             for (c, r) in idx1; init = 0),
                         "one_minus_F" => @sprintf("%.17g", e1),
                         "compile_ms" => @sprintf("%.6f", ms1),
                         "success_1e12" => e1 <= 1e-12))

        # ── BL2: Эйлер ZYZ (учебная декомпозиция, тот же оператор) ──
        nab2_2, nph_2, recerr = euler_zyz_counts(vals1, idx1, dph1, d)
        e2 = e1      # программа численно та же; бюджет примитивов другой
        ms2 = ms1    # сборка того же класса O(k·d)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "BL2_euler_zyz",
                         "n_ab2" => nab2_2, "n_phase" => nph_2,
                         "n_total" => nab2_2 + nph_2,
                         "twoq_equiv" => sum(twoq_equiv18(c, r)
                                             for (c, r) in idx1; init = 0),
                         "one_minus_F" => @sprintf("%.17g", e2),
                         "compile_ms" => @sprintf("%.6f", ms2),
                         "success_1e12" => e2 <= 1e-12))

        # ── BL4: Хаусхолдер ──
        V4, nab2_4, nph_4, off4, nrefl = householder_program(U)
        e4 = max(0.0, 1 - fidelity18(U, V4))
        ms4 = time_ms_e18(() -> householder_program(U), 15)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "BL4_householder",
                         "n_ab2" => nab2_4, "n_phase" => nph_4,
                         "n_total" => nab2_4 + nph_4,
                         "twoq_equiv" => "NA",
                         "one_minus_F" => @sprintf("%.17g", e4),
                         "compile_ms" => @sprintf("%.6f", ms4),
                         "success_1e12" => e4 <= 1e-12))

        # ── BL3: coordinate descent (равный бюджет слотов) ──
        restarts = d == 4 ? 3 : 1
        sweeps = d == 4 ? 200 : 100
        rng3 = MersenneTwister(t.seed + 777_018)
        (best3, evals3) = coord_optimize(U, a.slots; rng = rng3,
                                         restarts = restarts, sweeps = sweeps)
        ms3 = time_ms_e18(() -> coord_optimize(U, a.slots; rng = rng3,
                                               restarts = restarts,
                                               sweeps = sweeps), 2)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "BL3_coord_descent",
                         "n_ab2" => a.n_ab2, "n_phase" => a.n_phase,
                         "n_total" => a.n_ab2 + a.n_phase,
                         "twoq_equiv" => a.twoq,
                         "one_minus_F" => @sprintf("%.17g", best3),
                         "compile_ms" => @sprintf("%.6f", ms3),
                         "success_1e12" => best3 <= 1e-12))
        push!(optrows, Dict("instance" => t.id, "family" => t.family,
                            "d" => d, "method" => "BL3_coord_descent",
                            "restarts" => restarts, "sweeps" => sweeps,
                            "evaluations" => evals3,
                            "best_one_minus_F" => @sprintf("%.17g", best3),
                            "compile_ms" => @sprintf("%.6f", ms3),
                            "converged_1e12" => best3 <= 1e-12))

        # ── BL5: случайный поиск ──
        samples = d == 4 ? 3000 : 300
        rng5 = MersenneTwister(t.seed + 555_018)
        (best5, _) = random_search(U, a.slots; rng = rng5, samples = samples)
        ms5 = time_ms_e18(() -> random_search(U, a.slots; rng = rng5,
                                              samples = samples), 2)
        push!(rows, Dict("instance" => t.id, "family" => t.family, "d" => d,
                         "seed" => t.seed, "method" => "BL5_random_search",
                         "n_ab2" => a.n_ab2, "n_phase" => a.n_phase,
                         "n_total" => a.n_ab2 + a.n_phase,
                         "twoq_equiv" => a.twoq,
                         "one_minus_F" => @sprintf("%.17g", best5),
                         "compile_ms" => @sprintf("%.6f", ms5),
                         "success_1e12" => best5 <= 1e-12))
        push!(optrows, Dict("instance" => t.id, "family" => t.family,
                            "d" => d, "method" => "BL5_random_search",
                            "restarts" => 1, "sweeps" => samples,
                            "evaluations" => samples,
                            "best_one_minus_F" => @sprintf("%.17g", best5),
                            "compile_ms" => @sprintf("%.6f", ms5),
                            "converged_1e12" => best5 <= 1e-12))
    end

    save18("experiment_18_baselines", rows)
    save18("experiment_18_optimization", optrows)

    # ── медианы и предрегистрированные пороги ──
    _med_ms(method, subfamily = nothing) = begin
        ms = [parse(Float64, r["compile_ms"]) for r in rows
              if r["method"] == method &&
              (subfamily === nothing || r["family"] == subfamily)]
        isempty(ms) ? NaN : median(ms)
    end

    abqp_rows = [r for r in rows if r["method"] == "ABQP" &&
                 r["family"] != "control"]
    gate_i = all(parse(Float64, r["one_minus_F"]) <= 1e-12 for r in abqp_rows)

    gate_ii = true
    byinst = Dict{String,Vector{Dict{String,Any}}}()
    for r in rows
        r["family"] == "control" && continue
        push!(get!(byinst, r["instance"], Vector{Dict{String,Any}}()), r)
    end
    for (inst, rs) in byinst
        getm(m) = [r for r in rs if r["method"] == m]
        isempty(getm("ABQP")) && continue
        ta = getm("ABQP")[1]["n_total"]
        for m in ("BL1_naive_givens", "BL2_euler_zyz", "BL4_householder")
            isempty(getm(m)) && continue
            if ta > getm(m)[1]["n_total"]
                gate_ii = false
                println("    [E18] gate-ii FAIL: ", inst, " ", m,
                        " ABQP=", ta, " baseline=", getm(m)[1]["n_total"])
            end
        end
    end

    med_abqp4 = _med_ms("ABQP", "haar4")
    med_bl34 = _med_ms("BL3_coord_descent", "haar4")
    gate_iii = med_abqp4 * 50 <= med_bl34

    idrow = [r for r in rows if r["instance"] == "identity4" &&
             r["method"] == "ABQP"]
    gate_iv_identity = !isempty(idrow) && idrow[1]["n_ab2"] == 0
    ctrl = [r for r in rows if r["family"] == "control" &&
            r["method"] == "ABQP"]
    gate_iv_corrupted = !isempty(ctrl) &&
        parse(Float64, ctrl[1]["one_minus_F"]) <= 0.01

    # сводная таблица по методам
    sumrows = Vector{Dict{String,Any}}()
    for m in ("ABQP", "BL1_naive_givens", "BL2_euler_zyz", "BL4_householder",
              "BL3_coord_descent", "BL5_random_search")
        rs = [r for r in rows if r["method"] == m && r["family"] != "control"]
        isempty(rs) && continue
        errs = [parse(Float64, r["one_minus_F"]) for r in rs]
        push!(sumrows, Dict(
            "method" => m, "n_targets" => length(rs),
            "median_compile_ms" => @sprintf("%.6f",
                median([parse(Float64, r["compile_ms"]) for r in rs])),
            "max_one_minus_F" => @sprintf("%.17g", maximum(errs)),
            "success_rate_1e12" => @sprintf("%.4f",
                count(x -> x <= 1e-12, errs) / length(errs))))
    end
    for (mm, fam) in (("ABQP", "haar4"), ("BL3_coord_descent", "haar4"))
        rs = [r for r in rows if r["method"] == mm && r["family"] == fam]
        errs = [parse(Float64, r["one_minus_F"]) for r in rs]
        push!(sumrows, Dict(
            "method" => mm * "@" * fam, "n_targets" => length(rs),
            "median_compile_ms" => @sprintf("%.6f",
                median([parse(Float64, r["compile_ms"]) for r in rs])),
            "max_one_minus_F" => @sprintf("%.17g", maximum(errs)),
            "success_rate_1e12" => @sprintf("%.4f",
                count(x -> x <= 1e-12, errs) / max(1, length(errs)))))
    end
    save18("experiment_18_summary", sumrows)

    gates = Dict("abqp_success_all" => gate_i,
                 "abqp_primitives_le_baselines" => gate_ii,
                 "abqp_time_advantage_x50" => gate_iii,
                 "identity_zero_ab2" => gate_iv_identity,
                 "corrupted_compiles" => gate_iv_corrupted,
                 "median_ms_abqp_haar4" => med_abqp4,
                 "median_ms_bl3_haar4" => med_bl34)
    println("    [E18] пороги: ",
            join([k * "=" * string(v) for (k, v) in gates if isa(v, Bool)],
                 "; "))
    println("    [E18] медианы, мс: ABQP@haar4=",
            @sprintf("%.4f", med_abqp4), "  BL3@haar4=",
            @sprintf("%.4f", med_bl34))
    return gates
end

end # module
