# lib_abqp.jl — общая библиотека серии ABQP Julia Research Program
# Версия 0.2.0 (исполнение протоколов E01–E15).
# Только стандартные библиотеки Julia.

using LinearAlgebra, Random, Statistics, SHA, Printf, Dates, DelimitedFiles

const OUTDIR = joinpath(@__DIR__, "..", "results")
mkpath(OUTDIR)

# ────────────────────────── базовые метрики ──────────────────────────

# Fidelity по модулю глобальной фазы (как в исходном пакете V20):
#   F(U,V) = |Tr(U'V)|^2 / d^2
fidelity(U, V) = abs(tr(U' * V))^2 / size(U, 1)^2

unitarity_residual(U) = norm(U' * U - I, Inf)

"Круговая дистанция между фазами α, β ∈ ℝ: |arg(e^{i(α−β)})| ∈ [0, π]."
circular_distance(α::Real, β::Real) = abs(angle(cis(α - β)))

# ────────────────────────── Haar-унитарии ──────────────────────────

function haar_unitary(rng::AbstractRNG, d::Integer)
    A = (randn(rng, d, d) + im * randn(rng, d, d)) ./ sqrt(2)
    Q, R = qr(A)
    Qm = Matrix(Q)
    diagR = diag(Matrix(R))
    phases = [iszero(x) ? 1.0 + 0im : x / abs(x) for x in diagR]
    return Qm * Diagonal(phases)
end

# ────────────────── Givens-компиляция (двухуровневая) ──────────────────

"""
Разложение унитарной матрицы U на последовательность двухуровневых
вращений (Givens) + диагональную фазу. Математически тождественно
компилятору V20 (Givens-QR → фазовая диагональ); вращение применяется
к строкам c и r напрямую — O(d) на вращение, O(d^3) суммарно.

Возвращает (rotations, diagphases, offdiag_residual), где
  rotations::Vector{Tuple{Int,Int,ComplexF64,ComplexF64,ComplexF64,ComplexF64}}
      — (c, r, w11, w12, w21, w22): блок W, действующий на строки (c, r):
        W·[a,b]ᵀ = [nr,0]ᵀ;  хранение блока, а не полной матрицы (O(1)/вращение);
  diagphases::Vector{ComplexF64} — фазовые примитивы (PHASE-эквивалент), длина d;
  offdiag_residual — ‖R − diag(R)‖_∞ после элиминации (должно быть ~ eps).
Программа исполнения: V = G₁' G₂' … G_k' D (в порядке применения).
"""
function givens_factors(U::AbstractMatrix{ComplexF64}; skip_eps = 1e-14)
    R = copy(U)
    d = size(U, 1)
    rotations = Tuple{Int,Int,ComplexF64,ComplexF64,ComplexF64,ComplexF64}[]
    for c in 1:d-1
        for r in d:-1:c+1
            a, b = R[c, c], R[r, c]
            abs(b) < skip_eps && continue
            nr = hypot(abs(a), abs(b))
            w11 = conj(a) / nr
            w12 = conj(b) / nr
            w21 = -b / nr
            w22 = a / nr
            rc = Vector{ComplexF64}(@view R[c, :])
            rr = Vector{ComplexF64}(@view R[r, :])
            @inbounds for j in 1:d
                R[c, j] = w11 * rc[j] + w12 * rr[j]
                R[r, j] = w21 * rc[j] + w22 * rr[j]
            end
            push!(rotations, (c, r, w11, w12, w21, w22))
        end
    end
    diagphases = [iszero(R[i, i]) ? 1.0 + 0im : R[i, i] / abs(R[i, i]) for i in 1:d]
    off = norm(R - Diagonal(diag(R)), Inf)
    return rotations, diagphases, off
end

"Сборка исполняемой матрицы V = G₁' G₂' … G_k' D из факторов.
Каждое вращение применяется к двум столбцам V — O(d) на шаг, O(k·d) всего."
function assemble_program(rotations, diagphases, d::Integer)
    V = Matrix{ComplexF64}(I, d, d)
    for (c, r, w11, w12, w21, w22) in rotations
        colc = Vector{ComplexF64}(@view V[:, c])
        colr = Vector{ComplexF64}(@view V[:, r])
        @inbounds for i in 1:d
            V[i, c] = colc[i] * conj(w11) + colr[i] * conj(w12)
            V[i, r] = colc[i] * conj(w21) + colr[i] * conj(w22)
        end
    end
    V = V * Diagonal(diagphases)
    return V
end

"Компиляция одной цели: возвращает (V, n_AB2, n_PHASE, offdiag, 1−F)."
function givens_compile(U::AbstractMatrix{ComplexF64})
    d = size(U, 1)
    rotations, diagphases, off = givens_factors(U)
    V = assemble_program(rotations, diagphases, d)
    err = max(0.0, 1 - fidelity(U, V))
    return V, length(rotations), length(diagphases), off, err
end

"Быстрая компиляция для масштабирования: только 1−F и счётчики (V не собирается).
Тождество: F(U, P·D) = |Tr(D'·P'·U)|²/d², где P'·U = D (точная арифметика)."
function givens_compile_fast(U::AbstractMatrix{ComplexF64})
    d = size(U, 1)
    rotations, diagphases, off = givens_factors(U)
    W = copy(U)
    for (c, r, w11, w12, w21, w22) in reverse(rotations)  # снимаем вращения
        rc = Vector{ComplexF64}(@view W[c, :])
        rr = Vector{ComplexF64}(@view W[r, :])
        @inbounds for j in 1:d
            W[c, j] = conj(w11) * rc[j] + conj(w12) * rr[j]
            W[r, j] = conj(w21) * rc[j] + conj(w22) * rr[j]
        end
    end
    resid = norm(W - Diagonal(diag(W)), Inf)
    f = abs(sum(conj.(diagphases) .* diag(W)))^2 / d^2
    return length(rotations), length(diagphases), off, resid, max(0.0, 1 - f)
end

# ────────────────────────── сохранение CSV ──────────────────────────

function save_rows(name, rows)
    path = joinpath(OUTDIR, name * ".csv")
    if isempty(rows)
        write(path, "status\nno_rows\n")
        return path
    end
    # объединение ключей всех строк (гетерогенные наборы строк)
    keys0 = Any[]
    for row in rows, k in keys(row)
        k in keys0 || push!(keys0, k)
    end
    open(path, "w") do io
        println(io, join(string.(keys0), ","))
        for row in rows
            println(io, join((replace(_csvstr(get(row, k, "")), "," => ";")
                              for k in keys0), ","))
        end
    end
    return path
end

_csvstr(x) = string(x)
_csvstr(x::Missing) = "NA"

# ────────────────────────── JSON-подобный журнал ──────────────────────────

"""
Минимальный детерминированный JSON-подобный журнал результатов.
Поддерживает Float64, Int, Bool, String, Nothing/Missing и плоские массивы.
"""
function json_dump(path::AbstractString, dict::AbstractDict)
    open(path, "w") do io
        println(io, "{")
        ks = collect(keys(dict))
        for (i, k) in enumerate(ks)
            v = dict[k]
            print(io, "  \"", k, "\": ", _jsonval(v), i < length(ks) ? "," : "")
            println(io)
        end
        println(io, "}")
    end
    return path
end

function _jsonval(v)
    if v isa Float64 || v isa Float32 || v isa BigFloat
        return @sprintf("%.17g", Float64(v))
    elseif v isa Integer
        return string(v)
    elseif v isa Bool
        return v ? "true" : "false"
    elseif v isa AbstractString
        return "\"" * replace(v, "\"" => "\\\"") * "\""
    elseif isnothing(v) || v isa Missing
        return "null"
    elseif v isa AbstractDict
        return "{" * join(("\"" * replace(string(k), "\"" => "\\\"") *
                           "\": " * _jsonval(x) for (k, x) in v), ", ") * "}"
    elseif v isa Tuple || v isa AbstractArray
        return "[" * join(_jsonval.(collect(v)), ", ") * "]"
    else
        return "\"" * replace(string(v), "\"" => "\\\"") * "\""
    end
end

# ────────────────────────── окружение ──────────────────────────

function env_info()
    Dict(
        "julia_version" => string(VERSION),
        "hostname_len" => 0,                 # не зависит от машины
        "date_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
        "word_size" => sizeof(Int),
        "blas_vendor_note" => "julia-stdlib linearalgebra",
    )
end
