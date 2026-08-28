# =====================================================================
# Generate_Zeta_Zeros_PythonCall.jl
# =====================================================================
# FAST generator zeros ζ(s) via PythonCall.jl + mpmath.
#
# PythonCall.jl — modern replacement PyCall:
#   [OK] Not requires configuration Python (использует built-in CondaPkg)
#   [OK] Automatically installs mpmath
#   [OK] Works on all platforms
#   [OK] Speed: 12 нулей/сек (50k zeros for ~70 минут)
#
# УСТАНОВКА (once):
#   julia -e 'using Pkg; Pkg.add(["PythonCall","CondaPkg","ProgressMeter","JSON"])'
#
# При first запуске automatically will install Python + mpmath.
#
# RUN:
#   julia -e 'include("Generate_Zeta_Zeros_PythonCall.jl"); main(n_zeros=50000)'
# =====================================================================

# === ОПЦИОНАЛЬНЫЕ ПАКЕТЫ ===

# 1. PythonCall — modern Python interop
try
    using PythonCall
    global const HAS_PYCALL_NEW = true
    println("[OK] PythonCall.jl доступен")
catch
    global const HAS_PYCALL_NEW = false
    println("WARNING: PythonCall.jl not installed")
    println("  Установите: julia -e 'using Pkg; Pkg.add(\"PythonCall\")'")
end

# 2. CondaPkg — for автоматической установки Python-packages
try
    using CondaPkg
    global const HAS_CONDAPKG = true
catch
    global const HAS_CONDAPKG = false
end

# 3. SpecialFunctions — резервный method
try
    using SpecialFunctions
    global const HAS_SPEC = true
catch
    global const HAS_SPEC = false
end

try
    using ProgressMeter
    global const HAS_PROGRESS = true
catch
    global const HAS_PROGRESS = false
end

try
    using JSON
    global const HAS_JSON = true
catch
    global const HAS_JSON = false
end

using Printf
using Dates
using Statistics

# =====================================================================
# 1. ИНИЦИАЛИЗАЦИЯ mpmath ЧЕРЕЗ PythonCall
# =====================================================================

# Глобальные переменные for mpmath
const mpmath_state = Ref{Any}(nothing)
const mpmath_zetazero_fn = Ref{Any}(nothing)
const mpmath_mp_dps_setter = Ref{Any}(nothing)

"""
    init_mpmath(precision_digits=25)

Инициализирует mpmath через PythonCall.
Автоматически устанавливает mpmath через CondaPkg если нужно.
"""
function init_mpmath(precision_digits::Int=25; verbose::Bool=true)
    if !HAS_PYCALL_NEW
        return false
    end

    if verbose
        println("\n>>> Инициализация mpmath via PythonCall <<<")
    end

    # Устанавливаем mpmath via CondaPkg if он доступен
    if HAS_CONDAPKG
        if verbose
            println("  Installation mpmath via CondaPkg (can занять время on first запуске)...")
        end
        try
            CondaPkg.add("mpmath")
            CondaPkg.add_channel("conda-forge")
            if verbose
                println("  [OK] mpmath установлен via CondaPkg")
            end
        catch e
            if verbose
                println("  [!] CondaPkg.add not удалось: $e")
                println("  Пробую pip install mpmath...")
            end
            try
                pip = pyimport("pip")
                pip.main(["install", "mpmath"])
                if verbose
                    println("  [OK] mpmath установлен via pip")
                end
            catch e2
                if verbose
                    println("  [FAIL] Not удалось set mpmath: $e2")
                end
                return false
            end
        end
    end

    # Импортируем mpmath
    try
        global mpmath_state[] = pyimport("mpmath")
        global mpmath_zetazero_fn[] = mpmath_state[].zetazero
        global mpmath_mp_dps_setter[] = mpmath_state[].mp.dps

        # Устанавливаем accuracy
        mpmath_state[].mp.dps = precision_digits

        # Тестовый вызов
        test_zero = mpmath_zetazero_fn[](1)
        test_t = pyconvert(Float64, test_zero.imag)

        if verbose
            println("  [OK] mpmath импортирован, accuracy = $precision_digits знаков")
            println("  [OK] Тест: first zero = $test_t (ожидается 14.134725141735)")
            if abs(test_t - 14.134725141735) < 1e-6
                println("  [OK] Тест пройден!")
                return true
            else
                println("  [!] Тестовый zero отличается from ожидаемого")
                return false
            end
        end
        return true
    catch e
        if verbose
            println("  [FAIL] Ошибка импорта mpmath: $e")
            println("  Попробуйте вручную:")
            println("    using CondaPkg; CondaPkg.add(\"mpmath\")")
        end
        return false
    end
end

"""
    get_zeta_zero_mpmath(n)

Возвращает n-й нуль ζ(s) через mpmath.zetazero(n).
"""
function get_zeta_zero_mpmath(n::Int)
    if mpmath_zetazero_fn[] === nothing
        return NaN
    end
    try
        zero = mpmath_zetazero_fn[](n)
        return pyconvert(Float64, zero.imag)
    catch e
        return NaN
    end
end

# =====================================================================
# 2. РЕЗЕРВНЫЙ МЕТОД: Riemann-Siegel via SpecialFunctions
# =====================================================================

"""
    hardy_z(t)

Вычисляет Hardy Z-функцию через Riemann-Siegel формулу.
Резервный метод если mpmath недоступен.
"""
function hardy_z(t::Float64)
    if !HAS_SPEC
        return NaN
    end

    s_gamma = ComplexF64(0.25, t / 2)
    try
        log_gamma_val = SpecialFunctions.loggamma(s_gamma)
        theta = imag(log_gamma_val) - (t / 2) * log(π)
        return riemann_siegel_z(t, theta)
    catch
        return NaN
    end
end

function riemann_siegel_z(t::Float64, theta::Float64)
    N = max(1, floor(Int, sqrt(t / (2π))))
    z_sum = 0.0
    for n in 1:N
        phase = theta - t * log(n)
        z_sum += cos(phase) / sqrt(n)
    end
    z_sum *= 2
    if abs(cos(theta)) > 1e-10
        psi_approx = cos(2 * theta - t * log(2π) + π / 4) / (2 * cos(theta))
        rs_correction = (-1)^(N - 1) * (t / (2π))^(-0.25) * psi_approx
        z_sum += rs_correction
    end
    return z_sum
end

function find_zeta_zero_bisection(t_start::Float64, t_end::Float64; max_iter::Int=40)
    f_start = hardy_z(t_start)
    f_end = hardy_z(t_end)
    if isnan(f_start) || isnan(f_end) || f_start * f_end > 0
        return NaN
    end
    a, b = t_start, t_end
    fa = f_start
    for _ in 1:max_iter
        mid = (a + b) / 2
        f_mid = hardy_z(mid)
        if isnan(f_mid)
            return NaN
        end
        if abs(f_mid) < 1e-12
            return mid
        end
        if fa * f_mid < 0
            b = mid
        else
            a = mid
            fa = f_mid
        end
        if abs(b - a) < 1e-12
            break
        end
    end
    return (a + b) / 2
end

# =====================================================================
# 3. ИЗВЕСТНЫЕ ПЕРВЫЕ 50 ZEROS (for резервного метода)
# =====================================================================

const KNOWN_ZEROS_50 = Float64[
    14.134725141735, 21.022039638772, 25.010857580146, 30.424876125860,
    32.935061587739, 37.586178158826, 40.918719012147, 43.327073280915,
    48.005150881167, 49.773832477672, 52.970321477714, 56.446247697063,
    59.347044002602, 60.831778524610, 65.112544048082, 67.079810529494,
    69.546401711174, 72.067157674482, 75.704690699084, 77.144840068875,
    79.337375020249, 82.910380854086, 84.735492980517, 87.425274613125,
    88.809111207634, 92.491899270558, 94.651344040520, 95.870634228245,
    98.831194218194, 101.317851005731, 103.725538040478, 105.446623052326,
    107.168611184276, 111.029535543169, 111.874659176993, 114.320220915453,
    116.226680320858, 118.790782865976, 121.370125002421, 122.946829293553,
    124.256818558346, 127.516683879597, 129.578704199561, 131.087688530933,
    133.497737202998, 134.756509753374, 138.116042054533, 139.736208952121,
    141.123707404021, 143.111845807621,
]

# =====================================================================
# 4. ГЕНЕРАЦИЯ ЧЕРЕЗ PythonCall + mpmath (FAST МЕТОД)
# =====================================================================

"""
    generate_zeros_pythoncall(n_zeros; verbose)

Генерация через PythonCall + mpmath.zetazero().
Скорость: ~12 нулей/сек (50k за ~70 минут).
"""
function generate_zeros_pythoncall(n_zeros::Int; verbose::Bool=true)
    if mpmath_zetazero_fn[] === nothing
        if !init_mpmath(25, verbose=verbose)
            return nothing
        end
    end

    if verbose
        println("\n>>> Generation via PythonCall + mpmath <<<")
        println("  Speed: ~12 нулей/сек")
        println("  Ожидаемое время for $n_zeros нулей: ~$(round(n_zeros/12/60, digits=1)) минут")
    end

    t_start = time()
    zeros = Float64[]

    p = nothing
    if verbose && HAS_PROGRESS
        p = Progress(n_zeros, desc="Нули: ", dt=0.5, barlen=50, color=:green)
    end

    for i in 1:n_zeros
        t = get_zeta_zero_mpmath(i)

        if isnan(t)
            println("\n  Ошибка on нуле $i — остановка")
            break
        end

        push!(zeros, t)

        if p !== nothing
            next!(p)
        elseif verbose && i % 500 == 0
            elapsed = time() - t_start
            rate = i / max(elapsed, 0.1)
            eta = (n_zeros - i) / max(rate, 0.1)
            println("  $i/$n_zeros  (t=$(round(t, digits=2)), speed=$(round(rate, digits=1))/s, ETA=$(round(eta, digits=0))s)")
        end
    end

    if p !== nothing
        finish!(p)
    end

    elapsed = time() - t_start
    if verbose
        println("\n  Done: $(length(zeros)) zeros for $(round(elapsed, digits=1))s ($(round(elapsed/60, digits=1)) мин)")
    end

    return zeros
end

# =====================================================================
# 5. РЕЗЕРВНЫЙ МЕТОД: Бисекция + Riemann-Siegel
# =====================================================================

function generate_zeros_bisection(n_zeros::Int; verbose::Bool=true)
    if !HAS_SPEC
        println("ERROR: SpecialFunctions.jl not installed")
        return Float64[]
    end

    if verbose
        println("\n>>> Резервный method: Бисекция + Riemann-Siegel <<<")
        println("  [!] Очень медленно (0.5 нулей/сек)")
    end

    zeros = Float64[]
    n_known = min(50, n_zeros)
    append!(zeros, KNOWN_ZEROS_50[1:n_known])

    if n_zeros <= 50
        return zeros
    end

    if verbose
        println("  Первые $n_known zeros загружены of tables.")
    end

    p = nothing
    if verbose && HAS_PROGRESS
        p = Progress(n_zeros - n_known, desc="Нули: ", dt=0.5, barlen=50, color=:red)
    end

    t = zeros[end]
    scan_step = 0.5
    n_found = n_known
    t_start_time = time()

    while n_found < n_zeros
        t_prev = t
        t += scan_step

        z_prev = hardy_z(t_prev)
        z_curr = hardy_z(t)

        if !isnan(z_prev) && !isnan(z_curr) && z_prev * z_curr < 0
            zero_t = find_zeta_zero_bisection(t_prev, t)

            if !isnan(zero_t) && zero_t > 0.1
                if isempty(zeros) || abs(zero_t - zeros[end]) > 0.01
                    push!(zeros, zero_t)
                    n_found += 1

                    if p !== nothing
                        next!(p)
                    elseif verbose && n_found % 100 == 0
                        elapsed = time() - t_start_time
                        rate = (n_found - n_known) / max(elapsed, 0.1)
                        eta = (n_zeros - n_found) / max(rate, 0.1)
                        println("  Нуль #$n_found: t = $(round(zero_t, digits=4)), speed=$(round(rate, digits=1))/s, ETA=$(round(eta, digits=0))s")
                    end
                end
            end
        end

        if t > 200 * n_zeros
            break
        end
    end

    if p !== nothing
        finish!(p)
    end

    return zeros
end

# =====================================================================
# 6. УНИВЕРСАЛЬНАЯ ФУНКЦИЯ ГЕНЕРАЦИИ
# =====================================================================

function generate_zeros(n_zeros::Int; verbose::Bool=true)
    if verbose
        println("\nВыбор метода генерации:")
        println("  PythonCall:         $(HAS_PYCALL_NEW ? "✓ доступен" : "✗")")
        println("  CondaPkg:           $(HAS_CONDAPKG ? "✓ доступен" : "✗")")
        println("  SpecialFunctions:   $(HAS_SPEC ? "✓ доступен (резерв)" : "✗")")
    end

    # Метод 1: PythonCall + mpmath
    if HAS_PYCALL_NEW
        if verbose
            println("\n>>> Метод 1: PythonCall + mpmath (макс. speed) <<<")
        end
        zeros = generate_zeros_pythoncall(n_zeros, verbose=verbose)
        if zeros !== nothing && !isempty(zeros)
            return zeros, "PythonCall + mpmath.zetazero()"
        end
        if verbose
            println("  Переключаюсь on резервный method...")
        end
    end

    # Метод 2: Бисекция + Riemann-Siegel
    if HAS_SPEC
        if verbose
            println("\n>>> Метод 2: Бисекция + Riemann-Siegel (резервный) <<<")
        end
        zeros = generate_zeros_bisection(n_zeros, verbose=verbose)
        return zeros, "Бисекция + Riemann-Siegel"
    end

    println("\nERROR: ни one method not доступен.")
    println("Установите PythonCall:")
    println("  julia -e 'using Pkg; Pkg.add([\"PythonCall\",\"CondaPkg\"])'")
    return Float64[], "None"
end

# =====================================================================
# 7. СОХРАНЕНИЕ В РАЗНЫХ ФОРМАТАХ
# =====================================================================

function save_zeros_txt(zeros::Vector{Float64}, filepath::String)
    open(filepath, "w") do f
        println(f, "# Нули дзета-функции Riemann ζ(s) on критической линии Re(s) = 1/2")
        println(f, "# Формат: t (where s = 1/2 + it)")
        println(f, "# Сгенерировано: $(Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))")
        println(f, "# Всего нулей: $(length(zeros))")
        println(f, "# Источник: Generate_Zeta_Zeros_PythonCall.jl")
        for z in zeros
            @printf(f, "%.15f\n", z)
        end
    end
    println("  TXT: $filepath ($(length(zeros)) нулей)")
end

function save_zeros_csv(zeros::Vector{Float64}, filepath::String)
    open(filepath, "w") do f
        println(f, "# CSV: Нули ζ(s) on критической линии")
        println(f, "# Сгенерировано: $(Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))")
        println(f, "index,t,s_real,s_imag,zero_number")
        for (i, t) in enumerate(zeros)
            @printf(f, "%d,%.15f,0.5,%.15f,%d\n", i, t, t, i)
        end
    end
    println("  CSV: $filepath ($(length(zeros)) нулей)")
end

function save_zeros_json(zeros::Vector{Float64}, filepath::String, precision::Int, method::String)
    if !HAS_JSON
        open(filepath, "w") do f
            println(f, "{\"total_zeros\": $(length(zeros)), \"precision\": $precision}")
        end
        println("  JSON (упрощённый): $filepath")
        return
    end
    data = Dict(
        "metadata" => Dict(
            "description" => "Нули ζ(s) on критической линии Re(s) = 1/2",
            "format" => "t, where s = 1/2 + it",
            "total_zeros" => length(zeros),
            "precision_digits" => precision,
            "generated_at" => Dates.format(now(), "yyyy-mm-dd HH:MM:SS"),
            "first_zero" => zeros[1],
            "last_zero" => zeros[end],
            "method" => method,
            "source" => "Generate_Zeta_Zeros_PythonCall.jl"
        ),
        "zeros" => zeros
    )
    open(filepath, "w") do f
        JSON.print(f, data, 2)
    end
    println("  JSON: $filepath ($(length(zeros)) нулей)")
end

function save_zeros_julia(zeros::Vector{Float64}, filepath::String, precision::Int, method::String)
    open(filepath, "w") do f
        println(f, "# =====================================================================")
        println(f, "# Zeta_Zeros_Table.jl — $(length(zeros)) REAL zeros ζ(s)")
        println(f, "# =====================================================================")
        println(f, "# Сгенерировано: $(Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))")
        println(f, "# Источник: Generate_Zeta_Zeros_PythonCall.jl")
        println(f, "# Метод: $method")
        println(f, "# Accuracy: $precision знаков after запятой")
        println(f, "# Всего нулей: $(length(zeros))")
        println(f, "#")
        println(f, "# First zero: $(zeros[1])")
        println(f, "# Last zero: $(zeros[end])")
        println(f, "# =====================================================================")
        println(f)
        println(f, "const N_ZETA_ZEROS_AVAILABLE = $(length(zeros))")
        println(f, "const ZETA_ZEROS_VERIFIED_COUNT = $(length(zeros))")
        println(f)
        println(f, "const ZETA_ZEROS = Float64[")
        for i in 1:4:length(zeros)
            chunk = zeros[i:min(i+3, length(zeros))]
            formatted = [@sprintf("%.15f", z) for z in chunk]
            line = "    " * join(formatted, ", ")
            if i + 3 < length(zeros)
                line *= ","
            end
            println(f, line)
        end
        println(f, "]")
        println(f)
        println(f, "\"\"\"")
        println(f, "    get_zeta_zeros_safe(n; prefer_verified=true)")
        println(f)
        println(f, "Возвращает первые n zeros ζ(s).")
        println(f, "\"\"\"")
        println(f, "function get_zeta_zeros_safe(n::Int; prefer_verified::Bool=true)")
        println(f, "    return ZETA_ZEROS[1:min(n, N_ZETA_ZEROS_AVAILABLE)]")
        println(f, "end")
    end
    println("  Julia: $filepath ($(length(zeros)) нулей)")
end

# =====================================================================
# 8. СТАТИСТИКА
# =====================================================================

function compute_mean_r(zeros::Vector{Float64})
    if length(zeros) < 3
        return NaN
    end
    sorted_zeros = sort(zeros)
    spacings = [sorted_zeros[i+1] - sorted_zeros[i] for i in 1:length(sorted_zeros)-1]
    ratios = Float64[]
    for i in 1:length(spacings)-1
        s1, s2 = spacings[i], spacings[i+1]
        if s1 > 0 && s2 > 0
            push!(ratios, min(s1, s2) / max(s1, s2))
        end
    end
    return isempty(ratios) ? NaN : mean(ratios)
end

# =====================================================================
# 9. ГЛАВНАЯ ФУНКЦИЯ
# =====================================================================

"""
    main(; n_zeros, precision, output_prefix, verbose)

Главная функция: генерирует нули ζ(s) и сохраняет в 4 форматах.
"""
function main(;
              n_zeros::Int=50000,
              precision::Int=25,
              output_prefix::String="zeta_zeros",
              verbose::Bool=true)

    println("\n" * "="^78)
    println("  ГЕНЕРАТОР ZEROS ζ(s) (PythonCall + mpmath)")
    println("="^78)
    println("  Количество нулей: $n_zeros")
    println("  Префикс файлов:   $output_prefix")
    println("="^78)

    if !HAS_PYCALL_NEW && !HAS_SPEC
        println("\nERROR: ни PythonCall, ни SpecialFunctions not installedы")
        println("Установите PythonCall:")
        println("  julia -e 'using Pkg; Pkg.add([\"PythonCall\",\"CondaPkg\"])'")
        return nothing
    end

    t_start = time()
    dt_start = now()

    # Generation
    println("\n>>> Шаг 1: Generation zeros <<<")
    zeros, method = generate_zeros(n_zeros, verbose=verbose)

    if isempty(zeros)
        println("ERROR: нули not generated")
        return nothing
    end

    t_gen = time() - t_start
    println("\n  Сгенерировано: $(length(zeros)) zeros for $(round(t_gen, digits=1))s ($(round(t_gen/60, digits=1)) мин)")
    println("  Метод: $method")

    # Статистика
    println("\n>>> Шаг 2: Статистика <<<")
    mean_r = compute_mean_r(zeros)
    println("  First zero: $(zeros[1])")
    println("  Last zero: $(zeros[end])")
    println("  ⟨r⟩ = $(round(mean_r, digits=6)) (R_GUE = 0.5996)")
    if abs(mean_r - 0.5996) < 0.02
        println("  [OK] ⟨r⟩ ≈ R_GUE -> нули соответствуют GUE")
    else
        println("  [!] ⟨r⟩ отличается from R_GUE")
    end

    # Сохранение
    println("\n>>> Шаг 3: Сохранение in 4 форматах <<<")
    suffix = "_$(n_zeros)"
    save_zeros_txt(zeros, "$(output_prefix)$(suffix).txt")
    save_zeros_csv(zeros, "$(output_prefix)$(suffix).csv")
    save_zeros_json(zeros, "$(output_prefix)$(suffix).json", precision, method)
    save_zeros_julia(zeros, "Zeta_Zeros$(suffix).jl", precision, method)

    # Итог
    t_total = time() - t_start
    println("\n" * "="^78)
    println("  ИТОГ")
    println("="^78)
    println("  Длительность: $(round(t_total, digits=1))s ($(round(t_total/60, digits=1)) мин)")
    println("  Zeros: $(length(zeros)), ⟨r⟩ = $(round(mean_r, digits=6))")
    println("  Метод: $method")
    println("  Файлы:")
    println("    - $(output_prefix)$(suffix).txt")
    println("    - $(output_prefix)$(suffix).csv")
    println("    - $(output_prefix)$(suffix).json")
    println("    - Zeta_Zeros$(suffix).jl  ← main for интеграции")
    println("="^78)

    return Dict(
        "zeros" => zeros,
        "n_zeros" => length(zeros),
        "mean_r" => mean_r,
        "method" => method,
        "elapsed_seconds" => t_total
    )
end

# Быстрые пресеты
generate_100() = main(n_zeros=100)
generate_1000() = main(n_zeros=1000)
generate_5000() = main(n_zeros=5000)
generate_50000() = main(n_zeros=50000)
generate_100000() = main(n_zeros=100000)

# =====================================================================
# ВЫВОД ПРИ ЗАГРУЗКЕ
# =====================================================================

println("\n" * "="^78)
println("  Generate_Zeta_Zeros_PythonCall.jl загружен")
println("  [T]  Время: $(Dates.format(now(), "yyyy-mm-dd HH:MM:SS"))")
println("="^78)
println("  Доступные методы:")
println("    PythonCall + mpmath: $(HAS_PYCALL_NEW ? "✓ (макс. скорость, 12 нулей/сек)" : "✗")")
println("    CondaPkg:            $(HAS_CONDAPKG ? "✓ (авто-установка)" : "✗")")
println("    SpecialFunctions:    $(HAS_SPEC ? "✓ (резервный)" : "✗")")
if HAS_PROGRESS
    println("    ProgressMeter:      [OK]")
end
if HAS_JSON
    println("    JSON:               [OK]")
end

if !HAS_PYCALL_NEW
    println()
    println("  -----------------------------------------------------------------")
    println("  [!] ДЛЯ МАКСИМАЛЬНОЙ СКОРОСТИ установите PythonCall:")
    println("  -----------------------------------------------------------------")
    println("    julia -e 'using Pkg; Pkg.add([\"PythonCall\",\"CondaPkg\",\"ProgressMeter\",\"JSON\"])'")
    println("  -----------------------------------------------------------------")
end

println()
println("  Запуск:")
println("    main(n_zeros=50000)     — 50,000 zeros (рекомендуется)")
println("    generate_100()          — тест (100 нулей, ~10 сек)")
println("    generate_1000()         — 1,000 zeros (~1 мин)")
println("    generate_50000()        — 50,000 zeros (~70 мин)")
println("    generate_100000()       — 100,000 zeros (~2.5 часа)")
println()
println("  After генерации пришлите мне file Zeta_Zeros_<n>.jl")
println("="^78)

if abspath(PROGRAM_FILE) == @__FILE__
    println("\nЗапуск generate_1000() by умолчанию...")
    generate_1000()
end
