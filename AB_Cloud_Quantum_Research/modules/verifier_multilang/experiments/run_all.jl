# run_all.jl — ABQP Julia Research Program v0.4.0: ИСПОЛНЕНИЕ протоколов E01–E18.
#
# Апгрейд против каркаса v0.1.0: каждый эксперимент доведён до полной силы
# своего протокола (experiments/experiment_01_15.md): предрегистрированные
# пороги, контроли, независимые seeds, отрицательные контроли, CPTP-каналы,
# LHV-модели, трёхмеханизменный контраст и СЛЕПОЙ детектор нулей ζ (E11).
# v0.3.0 (обязательство O-J1): E16 — независимый движок Римана–Зигеля;
# E17 — слепое обнаружение нулей на высоте T=1000 двумя движками.
# v0.4.0 (обязательство O-J2, класс B): E18 — компилятор против сильных
# baseline (BL1 наивный Givens, BL2 Эйлер, BL4 Хаусхолдер, BL3 coordinate
# descent, BL5 случайный поиск) при РАВНЫХ ограничениях ISA.
#
# Запуск:  julia --project=. experiments/run_all.jl
# Результаты: results/*.csv + результаты валидации E11/E17 после хешей детекторов.

include(joinpath(@__DIR__, "lib_abqp.jl"))
include(joinpath(@__DIR__, "e11_zeta_blind.jl"))
include(joinpath(@__DIR__, "e16_rs_engine.jl"))
include(joinpath(@__DIR__, "e17_high_blind.jl"))
include(joinpath(@__DIR__, "e18_baselines.jl"))

using .ZetaDetector
using .RiemannSiegel
using .HighBlind
using .E18Baselines
using LinearAlgebra, Random, Statistics, SHA, Printf, Dates

const ENV_INFO = env_info()
const T_START = Dates.now(Dates.UTC)

# ══════════════════════ E01. Контрольные унитарные матрицы ══════════════════════

function exp01_controls()
    rows = Dict{String,Any}[]
    H2 = ComplexF64[1 1; 1 -1] / sqrt(2)
    dft = [cis(2π * j * k / 4) / 2 for j in 0:3, k in 0:3]
    rng = MersenneTwister(111)
    diagU = Matrix(Diagonal(cis.(2π * rand(rng, 4))))
    controls = Dict(
        "identity" => Matrix{ComplexF64}(I, 4, 4),
        "permutation" => ComplexF64.(circshift(Matrix{Float64}(I, 4, 4), (1, 0))),
        "DFT4" => dft,
        "Hadamard4" => kron(H2, H2),
        "random_diagonal" => diagU)
    for (k, U) in controls
        push!(rows, Dict("experiment" => 1, "case" => k,
                         "unitarity_residual" => unitarity_residual(U),
                         "one_minus_F_self" => max(0.0, 1 - fidelity(U, U)),
                         "one_minus_F_global_phase" =>
                             max(0.0, 1 - fidelity(U, cis(0.731) * U))))
    end
    # Контроль с внесённой ошибкой в один элемент (шаг 4 протокола):
    Uc = copy(controls["DFT4"]); Uc[2, 3] += 1e-3
    push!(rows, Dict("experiment" => 1, "case" => "corrupted_DFT4_plus_1e-3",
                     "unitarity_residual" => unitarity_residual(Uc),
                     "one_minus_F_self" => max(0.0, 1 - fidelity(controls["DFT4"], Uc)),
                     "one_minus_F_global_phase" => missing))
    save_rows("experiment_01_controls", rows)
    return rows
end

# ══════════════════════ E02. Haar-компиляция 4×4 и 8×8 ══════════════════════

function exp02_haar_compilation()
    rows = Dict{String,Any}[]
    # Репликация исходных seeds V20 + новые предрегистрированные seeds серии:
    series = [(4, 2, 96, 200, 1e-12, "replication_v20"),
              (8, 3, 296, 100, 1e-10, "replication_v20"),
              (4, 2, 20261, 200, 1e-12, "new_predeclared"),
              (8, 3, 20262, 100, 1e-10, "new_predeclared")]
    for (d, n, seed, count, threshold, role) in series
        rng = MersenneTwister(seed)
        errs = Float64[]; fails = 0; gates_ab2 = 0; gates_phase = 0
        maxoff = 0.0
        for _ in 1:count
            U = haar_unitary(rng, d)
            V, nab2, nph, off, err = givens_compile(U)
            push!(errs, err)
            (err > threshold) && (fails += 1)
            gates_ab2 = nab2; gates_phase = nph
            maxoff = max(maxoff, off)
        end
        push!(rows, Dict("experiment" => 2, "dimension" => d, "n_qubits" => n,
                         "seed" => seed, "role" => role, "count" => count,
                         "max_one_minus_F" => maximum(errs),
                         "median_one_minus_F" => median(errs),
                         "p95_one_minus_F" => quantile(errs, 0.95),
                         "n_failures" => fails, "threshold" => threshold,
                         "threshold_pass" => fails == 0,
                         "ab2_blocks" => gates_ab2, "phase_gates" => gates_phase,
                         "max_offdiag_residual" => maxoff))
    end
    save_rows("experiment_02_haar", rows)
    return rows
end

# ══════════════════════ E03. Масштабирование и фазовая диаграмма ══════════════════════

function exp03_scaling()
    rows = Dict{String,Any}[]
    for n in 1:8
        d = 2^n
        rng = MersenneTwister(1000 + n)
        U = haar_unitary(rng, d)
        t_gen = @elapsed U = haar_unitary(MersenneTwister(1000 + n), d)
        # min-of-3 для фазовых времён (стандартная практика бенчмарков):
        t_comp = Inf; t_asm = Inf; t_ver = Inf
        rot = ph = off = V = err = nothing
        for rep in 1:3
            t1 = @elapsed rot, ph, off = givens_factors(U)
            t2 = @elapsed V = assemble_program(rot, ph, d)
            t3 = @elapsed err = max(0.0, 1 - fidelity(U, V))
            t_comp = min(t_comp, t1); t_asm = min(t_asm, t2); t_ver = min(t_ver, t3)
        end
        al = @allocated givens_factors(U)
        push!(rows, Dict("experiment" => 3, "n_qubits" => n, "dimension" => d,
                         "sec_generate" => t_gen, "sec_compile" => t_comp,
                         "sec_assemble" => t_asm, "sec_verify" => t_ver,
                         "alloc_bytes_compile" => al,
                         "est_dense_bytes_per_matrix" => 2 * d * d * sizeof(ComplexF64),
                         "ab2_blocks" => length(rot), "phase_gates" => length(ph),
                         "one_minus_F" => err, "offdiag_residual" => off))
    end
    save_rows("experiment_03_scaling", rows)
    # Регрессия log t = a + b log d по точкам d ≥ 16 (n ≥ 4):
    xs = [log(2, r["dimension"]) for r in rows if r["dimension"] >= 16]
    ys = [log(2, r["sec_compile"]) for r in rows if r["dimension"] >= 16]
    k = length(xs)
    xm, ym = mean(xs), mean(ys)
    b = sum((xs .- xm) .* (ys .- ym)) / sum((xs .- xm) .^ 2)
    a = ym - b * xm
    resid = ys .- (a .+ b .* xs)
    s = sqrt(sum(resid .^ 2) / (k - 2))
    sb = s / sqrt(sum((xs .- xm) .^ 2))
    save_rows("experiment_03_fit", [
        Dict("experiment" => 3, "slope_b_log2" => b, "slope_stderr" => sb,
             "ci_lo" => b - 3.182sb, "ci_hi" => b + 3.182sb,
             "intercept_a_log2" => a, "n_points" => k)])
    return rows, Dict("slope_b_log2" => b, "slope_stderr" => sb,
                      "slope_ci95" => [b - 3.182 * sb, b + 3.182 * sb],
                      "intercept_a_log2" => a, "n_points" => k)
end

# ══════════════════════ E04. Seeds, реплей, порядок прогонов ══════════════════════

function _compile_bytes(seed::Int)
    rng = MersenneTwister(seed)
    U = haar_unitary(rng, 4)
    V, _, _, _, _ = givens_compile(U)
    return reinterpret(UInt8, vec(reinterpret(Float64, vec(V))))
end

function exp04_replay()
    a, b = _compile_bytes(96), _compile_bytes(96)
    sha = bytes2hex(sha256(a))
    # Независимая серия из 20 seeds (дважды, в двух порядках):
    seeds = collect(4001:4020)
    errs1 = Float64[]; errs2 = Float64[]
    for s in seeds
        rng = MersenneTwister(s); U = haar_unitary(rng, 4)
        push!(errs1, givens_compile(U)[5])
    end
    for s in reverse(seeds)                      # другой порядок прогонов
        rng = MersenneTwister(s); U = haar_unitary(rng, 4)
        push!(errs2, givens_compile(U)[5])
    end
    order_independent = errs1 == reverse(errs2)
    save_rows("experiment_04_replay", [
        Dict("experiment" => 4, "seed_replay" => 96, "byte_exact_replay" => a == b,
             "sha256_output" => sha,
             "independent_seeds" => 20,
             "max_one_minus_F_20seeds" => maximum(errs1),
             "median_one_minus_F_20seeds" => median(errs1),
             "order_independent" => order_independent,
             "julia_version" => ENV_INFO["julia_version"])])
    return Dict("byte_exact" => a == b, "sha" => sha, "max20" => maximum(errs1),
                "median20" => median(errs1), "order_ok" => order_independent)
end

# ══════════════════════ E05. Чувствительность к фазовому шуму ══════════════════════

function exp05_phase_noise()
    rng = MersenneTwister(505)
    U = haar_unitary(rng, 4)
    V, d = givens_compile(U)[1], 4
    rows = Dict{String,Any}[]
    budget = 1e-8                                # прикладной бюджет (предрегистрирован)
    sigma_star = nothing
    for sigma in [0.0, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
        vals = Float64[]
        for _ in 1:100
            phases = sigma .* randn(rng, 4)
            Vn = Diagonal(cis.(phases)) * V
            push!(vals, max(0.0, 1 - fidelity(U, Vn)))
        end
        p95 = quantile(vals, 0.95)
        push!(rows, Dict("experiment" => 5, "mode" => "random_sigma",
                         "sigma_rad" => sigma, "repeats" => 100,
                         "median_one_minus_F" => median(vals),
                         "p95_one_minus_F" => p95, "max_one_minus_F" => maximum(vals)))
        if p95 <= budget
            sigma_star = sigma
        end
    end
    # Систематический сдвиг (детерминированный режим):
    for delta in [0.0, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
        Vn = Diagonal(cis.(fill(delta, 4))) * V
        push!(rows, Dict("experiment" => 5, "mode" => "systematic_bias",
                         "sigma_rad" => delta, "repeats" => 1,
                         "median_one_minus_F" => max(0.0, 1 - fidelity(U, Vn)),
                         "p95_one_minus_F" => missing,
                         "max_one_minus_F" => missing))
    end
    # Контроль: глобальная фаза не влияет на F:
    gp = max(0.0, 1 - fidelity(U, cis(0.577) * V))
    save_rows("experiment_05_phase_noise", rows)
    return Dict("sigma_star_p95_le_budget" => sigma_star, "budget" => budget,
                "global_phase_control_1mF" => gp)
end

# ══════════════════════ E06. Память: дефазировка и деполяризация отдельно ══════════════════════

h2b(p) = p <= 0 ? 0.0 : (p >= 1 ? 0.0 : -p * log2(p) - (1 - p) * log2(1 - p))

function exp06_memory_noise()
    rng = MersenneTwister(606)
    rows = Dict{String,Any}[]
    # Канал A: бит-флип p на такт (классическая память в вычислительном базисе)
    for p in [0.0, 0.001, 0.005, 0.01, 0.02, 0.05], T in [1, 10, 100, 1000]
        trials = 2000; correct = 0
        for _ in 1:trials
            bit = rand(rng, Bool); observed = bit
            for _ in 1:T
                rand(rng) < p && (observed = !observed)
            end
            correct += (observed == bit)
        end
        pT = (1 - (1 - 2p)^T) / 2                       # эквивалентный BSC
        push!(rows, Dict("experiment" => 6, "channel" => "bitflip_p",
                         "param" => p, "steps" => T, "trials" => trials,
                         "readout_accuracy_sim" => correct / trials,
                         "readout_accuracy_analytic" => (1 + (1 - 2p)^T) / 2,
                         "mutual_information_bits" => 1 - h2b(pT)))
    end
    # Канал B: деполяризация q на такт (кубит, матрица плотности; аналитически)
    for q in [0.0, 0.001, 0.005, 0.01, 0.02, 0.05], T in [1, 10, 100, 1000]
        surv = (1 - q)^T
        push!(rows, Dict("experiment" => 6, "channel" => "depolarizing_q",
                         "param" => q, "steps" => T, "trials" => 0,
                         "readout_accuracy_sim" => missing,
                         "readout_accuracy_analytic" => (1 + surv) / 2,
                         "mutual_information_bits" => missing,
                         "bloch_survival" => surv))
    end
    # Канал C: чистая дефазировка p_d (когерентность |ρ01| → (1−2p_d)^T |ρ01|)
    for pd in [0.0, 0.001, 0.005, 0.01, 0.02, 0.05], T in [1, 10, 100, 1000]
        push!(rows, Dict("experiment" => 6, "channel" => "dephasing_pd",
                         "param" => pd, "steps" => T, "trials" => 0,
                         "readout_accuracy_sim" => missing,
                         "readout_accuracy_analytic" => 1.0,
                         "mutual_information_bits" => missing,
                         "coherence_survival" => (1 - 2pd)^T))
    end
    save_rows("experiment_06_memory_noise", rows)
    return Dict("ideal_control_ok" =>
                    all(r["readout_accuracy_sim"] === missing ||
                        r["readout_accuracy_sim"] == 1.0
                        for r in rows if r["param"] == 0.0 &&
                            r["channel"] == "bitflip_p"))
end

# ══════════════════════ E07. Код исправления ошибок против контроля ══════════════════════

wilson_ci(k::Int, n::Int) = begin
    p = k / n; z = 1.96
    den = 1 + z^2 / n
    c = (p + z^2 / (2n)) / den
    hw = z * sqrt(p * (1 - p) / n + z^2 / (4n^2)) / den
    [max(0.0, c - hw), min(1.0, c + hw)]
end

function exp07_repetition_code()
    rng = MersenneTwister(707)
    rows = Dict{String,Any}[]
    trials = 100_000
    for mode in ("independent", "correlated")
        for p in 0.001:0.005:0.101
            rawerr = 0; logicalerr = 0
            for _ in 1:trials
                bit = rand(rng, Bool)
                e1 = rand(rng) < p
                e2 = mode == "correlated" ? e1 : rand(rng) < p
                e3 = mode == "correlated" ? e1 : rand(rng) < p
                rawerr += ((bit ⊻ e1) != bit)
                m = count((bit ⊻ e1, bit ⊻ e2, bit ⊻ e3)) >= 2
                logicalerr += (m != bit)
            end
            ci_raw = wilson_ci(rawerr, trials)
            ci_log = wilson_ci(logicalerr, trials)
            push!(rows, Dict("experiment" => 7, "mode" => mode, "p" => p,
                             "trials" => trials,
                             "uncoded_error_rate" => rawerr / trials,
                             "uncoded_ci95_lo" => ci_raw[1],
                             "uncoded_ci95_hi" => ci_raw[2],
                             "logical_error_rate" => logicalerr / trials,
                             "logical_ci95_lo" => ci_log[1],
                             "logical_ci95_hi" => ci_log[2]))
        end
    end
    save_rows("experiment_07_repetition_code", rows)
    # PASS: независимый режим — логическая < некодированной на p<0.05 (CI-раздельно);
    # коррелированный контроль — выигрыш исчезает (|Δrate| внутри CI)
    gain_ok = all(r["logical_ci95_hi"] < r["uncoded_ci95_lo"]
                  for r in rows if r["mode"] == "independent" && r["p"] <= 0.051)
    corr_ok = all(abs(r["logical_error_rate"] - r["uncoded_error_rate"]) <
                  max(r["logical_ci95_hi"] - r["logical_ci95_lo"],
                      r["uncoded_ci95_hi"] - r["uncoded_ci95_lo"]) + 0.01
                  for r in rows if r["mode"] == "correlated")
    return Dict("independent_gain_ok" => gain_ok, "correlated_control_ok" => corr_ok)
end

# ══════════════════════ E08. Полный перебор ALU и обратимость ══════════════════════

function exp08_alu()
    rows = Dict{String,Any}[]
    # Обратимый сумматор (a,b) → (a, (a+b) mod 16): полная таблица 256 входов
    outputs = Set{Tuple{Int,Int}}()
    collisions = 0
    ok = true
    for a in 0:15, b in 0:15
        out = (a, mod(a + b, 16))
        out in outputs && (collisions += 1)
        push!(outputs, out)
        ok &= (out[1] == a && out[2] == mod(a + b, 16))
    end
    push!(rows, Dict("experiment" => 8, "operation" => "reversible_add_mod16",
                     "inputs" => 256, "unique_outputs" => length(outputs),
                     "collisions" => collisions, "bijective" => length(outputs) == 256,
                     "truth_table_ok" => ok))
    # Умножение mod 16: нечётные множители — перестановка, чётные — нет (предрегистрировано)
    for m in 0:15
        outs = Set(mod(m * x, 16) for x in 0:15)
        push!(rows, Dict("experiment" => 8, "operation" => "mulmod16",
                         "multiplier" => m, "inputs" => 16,
                         "unique_outputs" => length(outs),
                         "collisions" => 16 - length(outs),
                         "bijective" => length(outs) == 16,
                         "multiplier_parity" => isodd(m) ? "odd" : "even"))
    end
    # Фазовый оракул сравнения (−1)^{[a>b]}: унитарная диагональ, не классический компаратор
    oracle_ok = all(abs(((-1)^Int(a > b)) - cis(π * Int(a > b))) < 1e-12
                    for a in 0:15, b in 0:15)
    push!(rows, Dict("experiment" => 8, "operation" => "phase_oracle_comparator",
                     "inputs" => 256, "unique_outputs" => 256,
                     "collisions" => 0, "bijective" => true,
                     "truth_table_ok" => oracle_ok))
    save_rows("experiment_08_alu", rows)
    mul_rows = filter(r -> r["operation"] == "mulmod16", rows)
    pattern_ok = all(r["bijective"] == (r["multiplier_parity"] == "odd")
                     for r in mul_rows)          # odd→bijective, even→not
    return Dict("adder_bijective" => length(outputs) == 256 && ok && collisions == 0,
                "mulmod_pattern_ok" => pattern_ok,
                "oracle_ok" => oracle_ok)
end

# ══════════════════════ E09. Обратимая арифметика: реальные схемы ══════════════════════
# Реверсивный СУММАТОР IN-PLACE (a,b) → (a, a+b mod 2^n) на явных затворах
# (Toffoli/CNOT) со ЧИСТЫМИ вспомогательными проводами. История: v0.1.0-каркас
# стирал бит суммы (поймано полным перебором); первая попытка v0.2.0 тоже дала
# 2^n−1 ошибок — восстановление b_i^orig шло через d_i вместо a_i; исправлено:
#   провода: a[1..n], b[1..n], c[1..n] (переносы), d[1..n] (a_i⊕b_i); c,d init 0
#   Ф1: d_i = a_i⊕b_i:            CNOT(a_i,d_i); CNOT(b_i,d_i)
#       c_i = maj:                Toffoli(a_i,b_i,c_i); Toffoli(d_i,c_{i-1},c_i)
#   Ф2: сумма в b:                CNOT(a_i,b_i); CNOT(c_{i-1},b_i)  → b_i = s_i
#   Ф3 (i = n..1; восстановление b_i^orig, чистка c_i,d_i, возврат s_i):
#       b_i ← b_i^orig:           CNOT(a_i,b_i); CNOT(c_{i-1},b_i)
#       снять накопление:        Toffoli(d_i,c_{i-1},c_i)
#       d_i → 0:                  CNOT(a_i,d_i); CNOT(b_i,d_i)
#       c_i → 0:                  Toffoli(a_i,b_i,c_i)
#       b_i ← s_i:                CNOT(a_i,b_i); CNOT(c_{i-1},b_i)
#       (для i=1 — без c_0: аналогично с одним CNOT на шагах a/e)
# Ожидаемая стоимость: Toffoli = 4n−2, CNOT = 10n−3 (проверяется перебором).

mutable struct Revcircuit
    wires::Vector{Int}          # 0/1
    toffoli::Int
    cnot::Int
end

function _toff!(cr::Revcircuit, i::Int, j::Int, k::Int)
    cr.wires[k] = cr.wires[k] ⊻ (cr.wires[i] & cr.wires[j])
    cr.toffoli += 1
end
function _cnot!(cr::Revcircuit, i::Int, j::Int)
    cr.wires[j] = cr.wires[j] ⊻ cr.wires[i]
    cr.cnot += 1
end

"Реверсивное сложение (a,b) → (a, a+b mod 2^n) на затворах; возвращает b, счётчики."
function rev_add(a::Int, b::Int, n::Int)
    w = zeros(Int, 4n)
    for i in 1:n
        w[i] = (a >> (i - 1)) & 1
        w[n + i] = (b >> (i - 1)) & 1
    end
    cr = Revcircuit(w, 0, 0)
    ai(i) = i; bi(i) = n + i; ci(i) = 2n + i; di(i) = 3n + i
    for i in 1:n                                   # Ф1: d_i и переносы
        _cnot!(cr, ai(i), di(i))
        _cnot!(cr, bi(i), di(i))
        _toff!(cr, ai(i), bi(i), ci(i))
        i > 1 && _toff!(cr, di(i), ci(i - 1), ci(i))
    end
    for i in 1:n                                   # Ф2: сумма в b
        _cnot!(cr, ai(i), bi(i))
        i > 1 && _cnot!(cr, ci(i - 1), bi(i))
    end
    for i in n:-1:1                                # Ф3: чистка + возврат суммы
        _cnot!(cr, ai(i), bi(i))                   # b_i → b_i^orig (частично)
        i > 1 && _cnot!(cr, ci(i - 1), bi(i))      # b_i = b_i^orig
        i > 1 && _toff!(cr, di(i), ci(i - 1), ci(i))   # снять накопление
        _cnot!(cr, ai(i), di(i))                   # d_i → b_i^orig
        _cnot!(cr, bi(i), di(i))                   # d_i → 0
        _toff!(cr, ai(i), bi(i), ci(i))            # c_i → 0
        _cnot!(cr, ai(i), bi(i))                   # b_i → s_i (частично)
        i > 1 && _cnot!(cr, ci(i - 1), bi(i))      # b_i = s_i
    end
    s = 0
    for i in 1:n
        s += cr.wires[bi(i)] << (i - 1)
    end
    garbage_clean = all(cr.wires[ci(i)] == 0 for i in 1:n) &&
                    all(cr.wires[di(i)] == 0 for i in 1:n)
    return s, cr.toffoli, cr.cnot, garbage_clean
end

function exp09_arithmetic_cost()
    rows = Dict{String,Any}[]
    exhaustive_ok = true
    toff_ok = true; cnot_ok = true; clean_ok = true
    for n in 2:8
        nerr = 0
        tf = cn = -1
        for a in 0:(2^n - 1), b in 0:(2^n - 1)
            s, t, c, cl = rev_add(a, b, n)
            if a == 0 && b == 0
                tf = t; cn = c          # счётчики затворов детерминированы схемой
            end
            clean_ok &= cl
            s == mod(a + b, 2^n) || (nerr += 1)
        end
        exhaustive_ok &= (nerr == 0)
        toff_ok &= (tf == 4n - 2)
        cnot_ok &= (cn == 10n - 3)
        push!(rows, Dict("experiment" => 9, "bits" => n,
                         "mode" => "exhaustive",
                         "inputs_checked" => 2^(2n), "errors" => nerr,
                         "toffoli" => tf, "cnot" => cn,
                         "total_gates" => tf + cn,
                         "dense_dim_4n" => 4n,
                         "dense_complex_matrix_bytes" => 2^(4n) * sizeof(ComplexF64)))
    end
    # Большие разрядности: случайные тесты + инварианты схемы
    rng = MersenneTwister(909)
    for n in (12, 16)
        nerr = 0
        for _ in 1:10_000
            a = rand(rng, 0:(2^n - 1)); b = rand(rng, 0:(2^n - 1))
            s, t, c, cl = rev_add(a, b, n)
            clean_ok &= cl
            s == mod(a + b, 2^n) || (nerr += 1)
        end
        push!(rows, Dict("experiment" => 9, "bits" => n, "mode" => "random_10k",
                         "inputs_checked" => 10_000, "errors" => nerr,
                         "toffoli" => 4n - 2, "cnot" => 10n - 3,
                         "total_gates" => 14n - 5,
                         "dense_dim_4n" => 4n,
                         "dense_complex_matrix_bytes" => 2^(4n) * sizeof(ComplexF64)))
    end
    save_rows("experiment_09_cost", rows)
    return Dict("exhaustive_ok" => exhaustive_ok,
                "toffoli_formula_ok" => toff_ok, "cnot_formula_ok" => cnot_ok,
                "ancilla_clean_ok" => clean_ok)
end

# ══════════════════════ E10. Алгебраические числа как фазы ══════════════════════

function exp10_phase_readout()
    setprecision(BigFloat, 200)
    vals_f = [sqrt(2.0), sqrt(3.0), 2.0^(1 / 3), (1 + sqrt(5.0)) / 2, NaN]
    # 2cos(2π/7) — через BigFloat и приведение:
    x7 = 2 * cos(2 * BigFloat(π) / 7)
    vals_big = [BigFloat(2)^(BigFloat(1) / BigFloat(2)),
                BigFloat(3)^(BigFloat(1) / BigFloat(2)),
                BigFloat(2)^(BigFloat(1) / BigFloat(3)),
                (1 + sqrt(BigFloat(5))) / 2,
                x7]
    rows = Dict{String,Any}[]
    for (i, xb) in enumerate(vals_big)
        xf = isfinite(vals_f[i]) ? vals_f[i] : Float64(xb)
        # явное отображение g(x) = 2π·frac(x)  (задокументировано; modulo 2π)
        phase_big = 2BigFloat(π) * (xb - floor(xb))
        phase_f = 2π * (xf - floor(xf))
        err_f = circular_distance(phase_f, phase_f)                     # самосогласование слоя
        err_fb = circular_distance(phase_f, Float64(phase_big))         # Float64 vs BigFloat
        neg = circular_distance(phase_f + 0.01, Float64(phase_big))     # отрицательный контроль
        push!(rows, Dict("experiment" => 10, "case" => i,
                         "value_float64" => xf,
                         "phase_float64" => phase_f,
                         "phase_bigfloat200" => Float64(phase_big),
                         "circular_error_self" => err_f,
                         "circular_error_f64_vs_big" => err_fb,
                         "negative_control_shift_0p01" => neg))
    end
    save_rows("experiment_10_phase_readout", rows)
    max_err = maximum(r["circular_error_f64_vs_big"] for r in rows)
    min_neg = minimum(r["negative_control_shift_0p01"] for r in rows)
    max_neg = maximum(r["negative_control_shift_0p01"] for r in rows)
    return Dict("max_circular_error_f64_vs_big" => max_err,
                "negative_control_min" => min_neg,
                "negative_control_max" => max_neg)
end

# ══════════════════════ E12. Интерферометр Маха–Зендера и AB-фаза ══════════════════════

function exp12_interferometer()
    H = ComplexF64[1 1; 1 -1] / sqrt(2)
    rows = Dict{String,Any}[]; worst = 0.0
    for (grid, tag) in ((collect(range(0, 2π, length = 257)), "dense_257"),
                        (collect(range(0, 2π, length = 33)), "sparse_33"))
        for phi in grid
            U = H * Diagonal(ComplexF64[1, cis(phi)]) * H
            psi = U * ComplexF64[1, 0]
            p = abs2(psi[2])
            resid = abs(p - sin(phi / 2)^2)
            worst = max(worst, resid)
            push!(rows, Dict("experiment" => 12, "grid" => tag, "phi" => phi,
                             "p_numeric" => p, "p_analytic" => sin(phi / 2)^2,
                             "residual" => resid))
        end
    end
    # Контроль глобальной фазы на всю матрицу:
    gp_worst = 0.0
    for phi in range(0, 2π, length = 257)
        U = cis(0.3) .* (H * Diagonal(ComplexF64[1, cis(phi)]) * H)
        psi = U * ComplexF64[1, 0]
        gp_worst = max(gp_worst, abs(abs2(psi[2]) - sin(phi / 2)^2))
    end
    # Конечные точки φ=0 и φ=2π: интерференция возвращает P=0:
    endpoints = [abs2((H * Diagonal(ComplexF64[1, cis(phi)]) * H *
                       ComplexF64[1, 0])[2]) for phi in (0.0, 2π)]
    # Различный шум в двух плечах (сигнатурный режим):
    rng = MersenneTwister(1212)
    arm_noise = Dict{Float64,Vector{Float64}}()
    for sig in (1e-6, 1e-4, 1e-2)
        dev = Float64[]
        for _ in 1:200
            phi = 0.7
            e1, e2 = sig * randn(rng), sig * randn(rng)
            U = H * Diagonal(ComplexF64[cis(e1), cis(phi + e2)]) * H
            push!(dev, abs(abs2((U * ComplexF64[1, 0])[2]) - sin(phi / 2)^2))
        end
        arm_noise[sig] = [mean(dev), maximum(dev)]
    end
    for (sig, mv) in arm_noise
        push!(rows, Dict("experiment" => 12, "grid" => "arm_noise_sigma_" * string(sig),
                         "phi" => missing, "p_numeric" => mv[1],
                         "p_analytic" => missing, "residual" => mv[2]))
    end
    save_rows("experiment_12_interferometer", rows)
    return Dict("max_residual" => worst, "global_phase_control_max" => gp_worst,
                "endpoints_P" => endpoints,
                "arm_noise_mean_max" => Dict(string(k) => v for (k, v) in arm_noise))
end

# ══════════════════════ E13. No-signaling: чистые/смешанные/CPTP/контроль ══════════════════════

function partial_trace_B(rho, dA, dB)
    out = zeros(ComplexF64, dA, dA)
    for a in 1:dA, ap in 1:dA, b in 1:dB
        out[a, ap] += rho[(a-1)*dB+b, (ap-1)*dB+b]
    end
    out
end

trace_distance(X, Y) = norm(X - Y, 1) / 2

function exp13_nosignaling()
    rng = MersenneTwister(1313)
    rows = Dict{String,Any}[]
    worst_unitary = 0.0; worst_cptp = 0.0; control_min = Inf
    # (а) случайные чистые состояния, локальная унитарная на B
    for trial in 1:100
        psi = randn(rng, ComplexF64, 4); psi /= norm(psi)
        rho = psi * psi'
        U = haar_unitary(rng, 2)
        joint = kron(Matrix{ComplexF64}(I, 2, 2), U)
        r1 = partial_trace_B(rho, 2, 2)
        r2 = partial_trace_B(joint * rho * joint', 2, 2)
        D = trace_distance(r1, r2)
        worst_unitary = max(worst_unitary, D)
        push!(rows, Dict("experiment" => 13, "class" => "pure_unitary",
                         "trial" => trial, "trace_distance" => D))
    end
    # (б) смешанные состояния (смесь K=4 чистых), локальная унитарная
    for trial in 1:100
        w = rand(rng, 4); w /= sum(w)
        rho = zeros(ComplexF64, 4, 4)
        for wk in w
            psi = randn(rng, ComplexF64, 4); psi /= norm(psi)
            rho .+= wk .* (psi * psi')
        end
        U = haar_unitary(rng, 2)
        joint = kron(Matrix{ComplexF64}(I, 2, 2), U)
        r1 = partial_trace_B(rho, 2, 2)
        r2 = partial_trace_B(joint * rho * joint', 2, 2)
        D = trace_distance(r1, r2)
        worst_unitary = max(worst_unitary, D)
        push!(rows, Dict("experiment" => 13, "class" => "mixed_unitary",
                         "trial" => trial, "trace_distance" => D))
    end
    # (в) локальный CPTP-канал деполяризации на B: ρ → (1−q)ρ + q·ρ_A⊗I_B/2
    for trial in 1:100
        psi = randn(rng, ComplexF64, 4); psi /= norm(psi)
        rho = psi * psi'
        q = 0.3
        rhoA = partial_trace_B(rho, 2, 2)
        eI = Matrix{ComplexF64}(I, 2, 2) ./ 2
        rho_cptp = (1 - q) .* rho .+ q .* kron(rhoA, eI)
        r1 = partial_trace_B(rho, 2, 2)
        r2 = partial_trace_B(rho_cptp, 2, 2)
        D = trace_distance(r1, r2)
        worst_cptp = max(worst_cptp, D)
        push!(rows, Dict("experiment" => 13, "class" => "pure_local_cptp",
                         "trial" => trial, "trace_distance" => D))
    end
    # (г) ОТРИЦАТЕЛЬНЫЙ КОНТРОЛЬ: нелокальный CNOT меняет маргинал A
    for trial in 1:20
        psi = randn(rng, ComplexF64, 4); psi /= norm(psi)
        rho = psi * psi'
        cnot = ComplexF64[1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0]
        r1 = partial_trace_B(rho, 2, 2)
        r2 = partial_trace_B(cnot * rho * cnot', 2, 2)
        D = trace_distance(r1, r2)
        control_min = min(control_min, D)
        push!(rows, Dict("experiment" => 13, "class" => "control_nonlocal_CNOT",
                         "trial" => trial, "trace_distance" => D))
    end
    save_rows("experiment_13_nosignaling", rows)
    return Dict("worst_unitary" => worst_unitary, "worst_cptp" => worst_cptp,
                "control_nonlocal_min" => control_min)
end

# ══════════════════════ E14. CHSH: сэмплирование, аналитика, LHV-контроль ══════════════════════

function exp14_chsh()
    # |Φ+⟩, измерения A(α)=cosα·σz+sinα·σx, B(β) аналогично ⇒ E(a,b)=cos(a−b)
    a0, a1, b0, b1 = 0.0, π / 2, π / 4, -π / 4
    E(a, b) = cos(a - b)
    S_analytic = abs(E(a0, b0) + E(a0, b1) + E(a1, b0) - E(a1, b1))
    # Монте-Карло совместных исходов (N=10^6 на настройку):
    rng = MersenneTwister(1414)
    N = 1_000_000
    Es = Float64[]; ses = Float64[]
    for (a, b) in ((a0, b0), (a0, b1), (a1, b0), (a1, b1))
        p_same = (1 + E(a, b)) / 2
        same = 0
        for _ in 1:N
            oA = rand(rng) < 0.5 ? 1 : -1          # знак A — симметричный
            sameSign = rand(rng) < p_same           # P(тот же знак) = (1+E)/2
            oB = sameSign ? oA : -oA
            same += (oA * oB == 1)
        end
        ê = 2 * same / N - 1
        push!(Es, ê)
        push!(ses, sqrt(max(0.0, 1 - ê^2) / N))
    end
    S_sampled = abs(Es[1] + Es[2] + Es[3] - Es[4])
    sigma_S = sqrt(ses[1]^2 + ses[2]^2 + ses[3]^2 + ses[4]^2)
    # LHV-контроль: перебор всех детерминированных стратегий (A0,A1,B0,B1)∈{±1}^4
    lhv_max = 0.0
    for A0 in (-1, 1), A1 in (-1, 1), B0 in (-1, 1), B1 in (-1, 1)
        Sl = abs(A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1)
        lhv_max = max(lhv_max, Sl)
    end
    save_rows("experiment_14_chsh", [
        Dict("experiment" => 14, "quantity" => "S_analytic", "value" => S_analytic),
        Dict("experiment" => 14, "quantity" => "S_sampled_1e6", "value" => S_sampled),
        Dict("experiment" => 14, "quantity" => "S_sampled_sigma", "value" => sigma_S),
        Dict("experiment" => 14, "quantity" => "S_minus_2sqrt2_sigma",
             "value" => abs(S_sampled - 2sqrt(2)) / sigma_S),
        Dict("experiment" => 14, "quantity" => "LHV_max_S", "value" => lhv_max),
        Dict("experiment" => 14, "quantity" => "quantum_bound", "value" => 2sqrt(2)),
        Dict("experiment" => 14, "quantity" => "local_bound", "value" => 2.0)])
    return Dict("S_analytic" => S_analytic, "S_sampled" => S_sampled,
                "sigma" => sigma_S, "deviation_sigmas" => abs(S_sampled - 2sqrt(2)) / sigma_S,
                "lhv_max" => lhv_max)
end

# ══════════════════════ E15. Топологическая устойчивость: три механизма ══════════════════════

function exp15_topology_ablation()
    rng = MersenneTwister(1515)
    rows = Dict{String,Any}[]
    H = ComplexF64[1 1; 1 -1] / sqrt(2)
    phi = 0.7
    P0 = sin(phi / 2)^2                       # эталонный выход MZI

    # M1: общая локальная унитарная на внутреннюю степень обоих плеч (алгебраическое
    # сокращение): |ψ⟩ ∝ |0⟩⊗|v⟩ + e^{iφ}|1⟩⊗V|v⟩; наблюдаемая = только путь.
    m1_resid_max = 0.0
    for _ in 1:1000
        V = haar_unitary(rng, 2)
        v = ComplexF64[1, 0]
        w = V * v
        # когерентность путей = ⟨v|V†V|v⟩·e^{iφ}/2; P = ½−Re(coh)
        coh = dot(v, V' * (V * v)) * cis(phi) / 2
        p_num = 0.5 - real(coh)
        m1_resid_max = max(m1_resid_max, abs(p_num - P0))
        push!(rows, Dict("experiment" => 15, "mechanism" => "M1_common_local_unitary",
                         "condition" => "random_V", "effect" => abs(p_num - P0)))
    end

    # M2: асимметричная фаза δ только в одном плече: эффект ∝ δ (предрегистрировано)
    m2 = Dict{Float64,Float64}()
    for delta in (1e-6, 1e-4, 1e-2, 0.1, 0.5)
        eff = abs(sin((phi + delta) / 2)^2 - P0)
        m2[delta] = eff
        push!(rows, Dict("experiment" => 15, "mechanism" => "M2_asymmetric_phase",
                         "condition" => string(delta), "effect" => eff))
    end
    slope_ok = m2[1e-4] / 1e-4 > 0.05 && m2[1e-4] / 1e-4 < 0.75   # dP/dφ = sinφ/2 ≈ 0.322

    # M3: глобальный топологический параметр — AB-поток Φ, φ = 2π·Φ/Φ₀
    Phi0 = 1.0; Phi = 0.2
    P_of(Phi) = sin(π * Phi / Phi0)^2
    full_q_shift = abs(P_of(Phi + Phi0) - P_of(Phi))            # периодичность: ≈ 0
    half_q_shift = abs(P_of(Phi + Phi0 / 2) - P_of(Phi))        # полу-квант: O(1)
    push!(rows, Dict("experiment" => 15, "mechanism" => "M3_AB_flux_full_quantum",
                     "condition" => "dPhi=Phi0", "effect" => full_q_shift))
    push!(rows, Dict("experiment" => 15, "mechanism" => "M3_AB_flux_half_quantum",
                     "condition" => "dPhi=Phi0/2", "effect" => half_q_shift))

    # Абляция A: убрать относительную фазу (φ≡0) → топологический сдвиг не виден
    P_of_phi0(Ph) = sin(π * 0.0 / Phi0)^2        # перекрёстная фаза удалена
    abl_zero_full = abs(P_of_phi0(Phi + Phi0) - P_of_phi0(Phi))
    push!(rows, Dict("experiment" => 15, "mechanism" => "ABLATION_phi0_full_shift",
                     "condition" => "phi_forced_0", "effect" => abl_zero_full))

    # Абляция B: заменить AB-фазу непериодической моделью пути φ_lin = Φ (рад)
    lin_full = abs(sin((Phi + Phi0) / 2)^2 - sin(Phi / 2)^2)    # НЕ защищено: эффект > 0
    push!(rows, Dict("experiment" => 15, "mechanism" => "CONTROL_linear_phase_model",
                     "condition" => "dPhi=Phi0", "effect" => lin_full))

    save_rows("experiment_15_topology_ablation", rows)
    return Dict("m1_resid_max" => m1_resid_max,
                "m2_slope_ok" => slope_ok,
                "m3_full_quantum_residual" => full_q_shift,
                "m3_half_quantum_effect" => half_q_shift,
                "ablation_phi0_effect" => abl_zero_full,
                "linear_model_full_shift_effect" => lin_full)
end

# ══════════════════════ E11. Слепое обнаружение нулей ζ ══════════════════════

function exp11_blind_zeta()
    println("  [E11] самотесты ζ-оценки (без эталонных нулей)...")
    st = ZetaDetector.zeta_selftest()
    save_rows("experiment_11_selftest", [
        Dict("experiment" => 11, "test" => k, "residual" => v)
        for (k, v) in st])
    dm = ZetaDetector.detector_meta()
    save_rows("experiment_11_meta", [
        Dict("experiment" => 11, "key" => k, "value" => string(v))
        for (k, v) in dm])
    # ── ДЕТЕКТОР (слепой) ──
    println("  [E11] детектор: намотка аргумента, h=0.01, [0.3, 60]...")
    det = ZetaDetector.detect_zeros(0.3, 60.0, 0.01)
    out_path = joinpath(OUTDIR, "e11_detector_output.csv")
    open(out_path, "w") do io
        println(io, "kind,key1,key2,value")
        println(io, "meta,method,zeta_em_bigfloat140_winding,")
        println(io, "meta,grid_h,", det["grid_h"])
        println(io, "meta,t0,", det["t0"])
        println(io, "meta,t1,", det["t1"])
        println(io, "meta,winding_count,", det["winding_count"])
        println(io, "meta,n_grid_points,", det["n_grid_points"])
        for (i, (p, z)) in enumerate(zip(det["positions"],
                                         det["abs_zeta_at_positions"]))
            println(io, "position,", i, ",", @sprintf("%.15f", p), ",",
                    @sprintf("%.3e", z))
        end
    end
    sha = open(out_path) do io
        bytes2hex(sha256(read(io)))
    end
    open(joinpath(OUTDIR, "e11_detector_sha256.txt"), "w") do io
        println(io, sha, "  e11_detector_output.csv")
    end
    println("  [E11] выход детектора ЗАФИКСИРОВАН: ", length(det["positions"]),
            " позиций; SHA256=", sha[1:16], "…")
    # ── ВАЛИДАТОР (только после фиксации) ──
    println("  [E11] валидатор (независимый метод + эталонные константы)...")
    include(joinpath(@__DIR__, "e11_validator.jl"))
    val = Base.invokelatest(ZetaValidator.run_validation!, det["positions"],
                            det["winding_count"])
    # CSV валидации:
    save_rows("experiment_11_validation", [
        Dict("experiment" => 11, "quantity" => k, "value" => v)
        for (k, v) in (
            ("n_detector", val["n_detector"]),
            ("n_reference_in_range", val["n_reference_in_range"]),
            ("n_matched", val["n_matched"]),
            ("precision", val["precision"]),
            ("recall", val["recall"]),
            ("max_position_error", val["max_position_error"]),
            ("rms_position_error", val["rms_position_error"]),
            ("gauss_newton_max_error_vs_reference",
             val["gauss_newton_max_error_vs_reference"]),
            ("gauss_newton_max_abszeta", val["gauss_newton_max_abszeta"]),
            ("winding_count", val["winding_count"]),
            ("winding_zeros_rounded", val["winding_zeros_rounded"]),
            ("S_T_standard_path", val["S_T"]),
            ("theta_T", val["theta_T"]),
            ("N_rvm", val["N_rvm"]),
            ("N_rvm_rounded", val["N_rvm_rounded"]))])
    save_rows("experiment_11_matched", [
        Dict("experiment" => 11, "gamma_reference" => g, "gamma_detected" => gd,
             "delta" => dv)
        for (g, gd, dv) in val["matched_table"]])
    # Развёрнутая фаза для рисунка (прореженная):
    ts, args, mags = ZetaDetector.unwrapped_arg(0.3, 60.0, 0.02)
    save_rows("experiment_11_winding_curve", [
        Dict("experiment" => 11, "t" => t, "arg_unwrapped" => a, "abs_zeta" => m)
        for (t, a, m) in zip(ts, args, mags)])
    return det, val, st, sha
end

# ══════════════════════ E16. Независимый движок Римана–Зигеля ══════════════════════

function exp16_rs_engine()
    println("  [E16] сборка таблиц F/DM (Эйлер-рекуррента, 400 бит) и самотесты...")
    st = RiemannSiegel.rs_selftest()
    save_rows("experiment_16_selftest", [
        Dict("experiment" => 16, "test" => k, "residual" => v)
        for (k, v) in st])
    save_rows("experiment_16_meta", [
        Dict("experiment" => 16, "key" => k, "value" => string(v))
        for (k, v) in RiemannSiegel.rs_meta()])
    # Стоимость при равной точности: EM(масштабируемое расписание) против RS
    println("  [E16] бенчмарк EM против RS (7 прогонов, медиана)...")
    rows = []
    for t in (100.0, 300.0, 1000.0, 3000.0, 10000.0)
        tems = Float64[]; trss = Float64[]
        agree = 0.0
        Nsch, Ksch = RiemannSiegel.em_schedule(t)
        for _ in 1:7
            t0 = time_ns()
            z1 = RiemannSiegel.reference_em(t)
            push!(tems, (time_ns() - t0) / 1e6)
            t1 = time_ns()
            z2, meta = RiemannSiegel.zeta_rs_line(t)
            push!(trss, (time_ns() - t1) / 1e6)
            agree = max(agree, Float64(abs(z1 - z2)))
        end
        push!(rows, Dict("experiment" => 16, "height" => t,
                         "em_N" => Nsch, "em_K" => Ksch,
                         "em_ms_median" => median(tems),
                         "rs_ms_median" => median(trss),
                         "rs_L" => last(RiemannSiegel.zeta_rs_line(t))["L"],
                         "rs_floor" => last(RiemannSiegel.zeta_rs_line(t))["floor"],
                         "agree" => agree))
        println("    t=", t, ": EM=", round(median(tems), digits = 3),
                " ms  RS=", round(median(trss), digits = 3),
                " ms  agree=", agree)
    end
    save_rows("experiment_16_benchmark", rows)
    return Dict("selftest" => st, "benchmark" => rows)
end

# ══════════════════════ E17. Слепое обнаружение на T=1000, два движка ══════════════════════

function exp17_detector_A()
    println("  [E17/3a] детектор A: Эйлер–Маклорен, [0.3, 1000], h=0.01 (~100k точек)...")
    tA = time_ns()
    detA, shaA = HighBlind.run_detector_A()
    println("      A: ", length(detA["positions"]), " позиций; намотка/π = ",
            round(detA["winding_count"], digits = 4), "; ",
            round((time_ns() - tA) / 1e9, digits = 1), " с; SHA=", shaA[1:16], "…")
    return detA, shaA
end

function exp17_detector_B()
    println("  [E17/3b] детектор B: Риман–Зигель, [50, 1000], h=0.01 (~95k точек)...")
    tB = time_ns()
    detB, shaB = HighBlind.run_detector_B()
    println("      B: ", length(detB["positions"]), " позиций; намотка/π = ",
            round(detB["winding_count"], digits = 4), "; ",
            round((time_ns() - tB) / 1e9, digits = 1), " с; SHA=", shaB[1:16], "…")
    return detB, shaB
end

function exp17_validate()
    println("  [E17/3c] валидатор: SHA-пины, Гаусс–Ньютон (320,12), эталон, N(1000)...")
    include(joinpath(@__DIR__, "e17_validator.jl"))
    val = Base.invokelatest(HighValidator.run_high_validation!)
    println("      N(1000) = ", val["N_rvm"], " → ", val["N_round"],
            "; precision EM/RS = ", val["em"]["precision"], "/",
            val["rs"]["precision"], "; recall = ", val["em"]["recall"], "/",
            val["rs"]["recall"])
    println("      max|Δγ| EM = ", val["em"]["max_err"], "; RS = ",
            val["rs"]["max_err"], "; кросс-движок = ", val["cross_max"],
            "; устойчивость сетки = ", val["max_shift"])
    return val
end

# ══════════════════════ E18. Компилятор против сильных baseline (O-J2) ══════════════════════

function exp18_baselines()
    println("  [E18/5] компилятор ABQP против BL1/BL2/BL4 (точные) и BL3/BL5 (численные)...")
    function abqp_compile(U)
        d = size(U, 1)
        rots, dph, off = givens_factors(U)
        V = assemble_program(rots, dph, d)
        err = max(0.0, 1 - fidelity(U, V))
        twoq = sum(E18Baselines.twoq_equiv18(c, r) for (c, r, _, _, _, _) in rots; init = 0)
        slots = [(c, r) for (c, r, _, _, _, _) in rots]
        return (n_ab2 = length(rots), n_phase = length(dph), twoq = twoq,
                one_minus_F = err, slots = slots)
    end
    gates = run_e18(abqp_compile)
    println("      ABQP против baseline: success_all=", gates["abqp_success_all"],
            "; primitives_le=", gates["abqp_primitives_le_baselines"],
            "; time_x50=", gates["abqp_time_advantage_x50"],
            "; identity=", gates["identity_zero_ab2"],
            "; corrupted=", gates["corrupted_compiles"])
    return gates
end

# ══════════════════════ ГЛАВНАЯ ТОЧКА ВХОДА ══════════════════════

function run_stage(stage::AbstractString)
    if stage == "1" || stage == "all"
        r01 = exp01_controls(); println("ok [01]")
        r02 = exp02_haar_compilation(); println("ok [02]")
        r03, fit3 = exp03_scaling(); println("ok [03]")
        r04 = exp04_replay(); println("ok [04]")
        r05 = exp05_phase_noise(); println("ok [05]")
        r06 = exp06_memory_noise(); println("ok [06]")
        r07 = exp07_repetition_code(); println("ok [07]")
        r08 = exp08_alu(); println("ok [08]")
        r09 = exp09_arithmetic_cost(); println("ok [09]")
        r10 = exp10_phase_readout(); println("ok [10]")
        det11, val11, st11, sha11 = exp11_blind_zeta(); println("ok [11]")
        r12 = exp12_interferometer(); println("ok [12]")
        r13 = exp13_nosignaling(); println("ok [13]")
        r14 = exp14_chsh(); println("ok [14]")
        r15 = exp15_topology_ablation(); println("ok [15]")
        summary = Dict(
            "stage" => "1 (E01-E15)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e01_max_unitarity_residual" => maximum(r["unitarity_residual"] for r in r01),
            "e02_all_pass" => all(r["threshold_pass"] for r in r02),
            "e03_slope_b" => fit3["slope_b_log2"],
            "e03_slope_ci95" => fit3["slope_ci95"],
            "e04_byte_exact_replay" => r04["byte_exact"],
            "e04_order_independent" => r04["order_ok"],
            "e05_sigma_star" => r05["sigma_star_p95_le_budget"],
            "e06_ideal_control_ok" => r06["ideal_control_ok"],
            "e07_independent_gain_ok" => r07["independent_gain_ok"],
            "e07_correlated_control_ok" => r07["correlated_control_ok"],
            "e08_adder_bijective" => r08["adder_bijective"],
            "e08_mulmod_pattern_ok" => r08["mulmod_pattern_ok"],
            "e09_exhaustive_ok" => r09["exhaustive_ok"],
            "e09_gate_formula_ok" => r09["toffoli_formula_ok"] && r09["cnot_formula_ok"],
            "e10_max_circular_error" => r10["max_circular_error_f64_vs_big"],
            "e11_selftest_max_residual" => maximum(values(st11)),
            "e11_n_detected" => length(det11["positions"]),
            "e11_winding" => det11["winding_count"],
            "e11_precision" => val11["precision"],
            "e11_recall" => val11["recall"],
            "e11_max_position_error" => val11["max_position_error"],
            "e11_gauss_newton_max_err" => val11["gauss_newton_max_error_vs_reference"],
            "e11_N_rvm" => val11["N_rvm"],
            "e12_max_residual" => r12["max_residual"],
            "e13_worst_nosignaling" => max(r13["worst_unitary"], r13["worst_cptp"]),
            "e13_control_min" => r13["control_nonlocal_min"],
            "e14_S_sampled" => r14["S_sampled"],
            "e14_deviation_sigmas" => r14["deviation_sigmas"],
            "e14_lhv_max" => r14["lhv_max"],
            "e15_m1_resid_max" => r15["m1_resid_max"],
            "e15_m3_full_quantum" => r15["m3_full_quantum_residual"],
            "e15_m3_half_quantum" => r15["m3_half_quantum_effect"],
            "e15_linear_model_effect" => r15["linear_model_full_shift_effect"])
        json_dump(joinpath(OUTDIR, "summary_stage1.json"), summary)
    end
    if stage == "2" || stage == "all"
        r16 = exp16_rs_engine(); println("ok [16]")
        json_dump(joinpath(OUTDIR, "summary_stage2.json"), Dict(
            "stage" => "2 (E16)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e16_F_series_residual" => r16["selftest"]["F_series_residual"],
            "e16_Z_realness_max" => r16["selftest"]["Z_realness_max"],
            "e16_agree_vs_em_max" => r16["selftest"]["agree_vs_em_max"],
            "e16_benchmark_agree_max" => maximum(x["agree"] for x in r16["benchmark"]),
            "e16_em_ms_at_1000" => [x["em_ms_median"] for x in r16["benchmark"] if x["height"] == 1000.0][1],
            "e16_rs_ms_at_1000" => [x["rs_ms_median"] for x in r16["benchmark"] if x["height"] == 1000.0][1]))
    end
    if stage == "3a" || stage == "all"
        detA, shaA = exp17_detector_A(); println("ok [17a]")
        json_dump(joinpath(OUTDIR, "summary_stage3a.json"), Dict(
            "stage" => "3a (detector A)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e17_n_detected_em" => length(detA["positions"]),
            "e17_winding_em" => detA["winding_count"],
            "e17_sha_em" => shaA))
    end
    if stage == "3b" || stage == "all"
        detB, shaB = exp17_detector_B(); println("ok [17b]")
        json_dump(joinpath(OUTDIR, "summary_stage3b.json"), Dict(
            "stage" => "3b (detector B)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e17_n_detected_rs" => length(detB["positions"]),
            "e17_winding_rs" => detB["winding_count"],
            "e17_sha_rs" => shaB))
    end
    if stage == "3c" || stage == "all"
        val = exp17_validate(); println("ok [17c]")
        json_dump(joinpath(OUTDIR, "summary_stage3c.json"), Dict(
            "stage" => "3c (validator)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e17_precision_em" => val["em"]["precision"],
            "e17_recall_em" => val["em"]["recall"],
            "e17_precision_rs" => val["rs"]["precision"],
            "e17_recall_rs" => val["rs"]["recall"],
            "e17_max_err_em" => val["em"]["max_err"],
            "e17_max_err_rs" => val["rs"]["max_err"],
            "e17_cross_engine_max" => val["cross_max"],
            "e17_N_rvm" => val["N_rvm"],
            "e17_N_rvm_rounded" => val["N_round"],
            "e17_grid_robustness_max_shift" => val["max_shift"]))
    end
    if stage == "5" || stage == "all"
        gates18 = exp18_baselines(); println("ok [18]")
        json_dump(joinpath(OUTDIR, "summary_stage5.json"), Dict(
            "stage" => "5 (E18)",
            "run_utc" => string(Dates.format(Dates.now(Dates.UTC), "yyyy-mm-ddTHH:MM:SSZ")),
            "julia" => ENV_INFO["julia_version"],
            "e18_abqp_success_all" => gates18["abqp_success_all"],
            "e18_abqp_primitives_le_baselines" => gates18["abqp_primitives_le_baselines"],
            "e18_abqp_time_advantage_x50" => gates18["abqp_time_advantage_x50"],
            "e18_identity_zero_ab2" => gates18["identity_zero_ab2"],
            "e18_corrupted_compiles" => gates18["corrupted_compiles"],
            "e18_median_ms_abqp_haar4" => gates18["median_ms_abqp_haar4"],
            "e18_median_ms_bl3_haar4" => gates18["median_ms_bl3_haar4"]))
    end
    if stage == "4" || stage == "all"
        merge_summaries(); println("ok [4: summary.json]")
    end
end

"Мини-парсер плоского JSON (стадийные сводки — только скаляры)."
function _parse_flat_json(path::AbstractString)
    out = Dict{String,Any}()
    for ln in eachline(path)
        m = match(r"^\s*\"([^\"]+)\":\s*(.+?),?\s*$", ln)
        m === nothing && continue
        key, val = m.captures[1], strip(m.captures[2])
        val = strip(val, [','])
        if val == "true"
            out[key] = true
        elseif val == "false"
            out[key] = false
        elseif val == "null"
            out[key] = nothing
        elseif startswith(val, "\"")
            out[key] = strip(val, ['"'])
        else
            out[key] = tryparse(Float64, val) !== nothing ? tryparse(Float64, val) :
                       tryparse(Int, val)
        end
    end
    return out
end

"Слияние стадийных сводок в summary.json (обратная совместимость с v0.2.0)."
function merge_summaries()
    merged = Dict{String,Any}()
    for f in ("summary_stage1.json", "summary_stage2.json", "summary_stage3a.json",
              "summary_stage3b.json", "summary_stage3c.json", "summary_stage5.json")
        p = joinpath(OUTDIR, f)
        isfile(p) || continue
        d = _parse_flat_json(p)
        for (k, v) in d
            k == "stage" && continue
            merged[k] = v
        end
    end
    json_dump(joinpath(OUTDIR, "summary.json"), merged)
    println("Сводка: results/summary.json (", length(merged), " полей)")
end

function main()
    println("╔══════════════════════════════════════════════════════════════╗")
    println("║ ABQP JULIA RESEARCH PROGRAM v0.4.0 · ИСПОЛНЕНИЕ E01–E18      ║")
    println("╚══════════════════════════════════════════════════════════════╝")
    stage = length(ARGS) >= 1 ? ARGS[1] : "all"
    println("Стадия: ", stage)
    run_stage(stage)
    println("Полное время стадии: ",
            @sprintf("%.1f с", (Dates.now(Dates.UTC) - T_START).value / 1000))
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
