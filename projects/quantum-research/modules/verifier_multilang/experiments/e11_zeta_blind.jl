# e11_zeta_blind.jl — ЭКСПЕРИМЕНТ 11: слепое обнаружение нулей дзета-функции.
#
# Дисциплина слепоты (протокол experiment_01_15.md, Э-11):
#   A. ДЕТЕКТОР (этот файл): получает ТОЛЬКО определение ζ(s), область поиска,
#      сетку и алгоритм намотки аргумента. Никаких эталонных нулей.
#      Выход фиксируется + хешируется SHA256 ДО всякой валидации.
#   B. ВАЛИДАТОР (e11_validator.jl): запускается отдельно, ПОСЛЕ фиксации хеша.
#
# Высокоценная оценка ζ(s) методом Эйлера–Маклорена (BigFloat, precision 140):
#   ζ(s) = Σ_{n=1}^{N-1} n^{-s} + N^{1-s}/(s-1) + ½N^{-s}
#          + Σ_{k=1}^{K} [B_{2k}/(2k)!] · s^{↑(2k-1)} · N^{-s-2k+1}
# Самотесты НЕ используют нули: ζ(2)=π²/6, ζ(4)=π⁴/90, ζ(-1)=-1/12,
# функциональное уравнение ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s).

module ZetaDetector

export zeta_em, zeta_selftest, unwrapped_arg, winding_count, refine_zero,
       detect_zeros, detector_meta, gamma_log, theta_big, standard_path_arg

const PRECISION = 140
setprecision(BigFloat, PRECISION)

# Числа Бернулли B_2..B_28 (точные рационалы), знаки B_{2k} = (−1)^{k+1}|B_{2k}|
const BERN = [1//6, -1//30, 1//42, -1//30, 5//66, -691//2730, 7//6,
              -3617//510, 43867//798, -174611//330, 854513//138,
              -236364091//2730, 855313//6160, -23749461029//870]

const N_TERMS = Ref(64)   # N (хвост Эйлера–Маклорена)
const K_TERMS = Ref(14)   # K (число поправок); ошибка ~ (|t|/N)^{2K}·N^{1/2}

"""
ζ(s) для Re(s) > −20, |Im s| ≤ 100, методом Эйлера–Маклорена.
"""
function zeta_em(s::Complex{BigFloat})
    N = BigFloat(N_TERMS[])
    K = K_TERMS[]
    acc = BigFloat(0)
    for n in 1:(N_TERMS[] - 1)
        acc += BigFloat(n)^(-s)
    end
    acc += N^(1 - s) / (s - 1)
    acc += BigFloat("0.5") * N^(-s)
    sp = s                                        # s^{↑1} (для k=1)
    for k in 1:K
        bern = BigFloat(BERN[k])
        fact = BigFloat(factorial(BigInt(2k)))           # 2k ≤ 28 → BigInt
        acc += bern * sp * N^(-s - BigFloat(2k - 1)) / fact
        # готовим s^{↑(2k+1)} = s^{↑(2k-1)}·(s+2k-1)·(s+2k)
        sp *= (s + BigFloat(2k - 1)) * (s + BigFloat(2k))
    end
    return acc
end

"log Γ(z) для произвольного z с |arg|<π: отражение + сдвиг вверх + Стирлинг."
function gamma_log(z::Complex{BigFloat})
    if real(z) < BigFloat("0.5")
        # Γ(z) = π / (sin(πz)·Γ(1−z))  ⇒  log Γ(z) = log π − log(sin πz) − log Γ(1−z)
        return log(BigFloat(π)) - log(sin(BigFloat(π) * z)) - gamma_log(one(z) - z)
    end
    zz = copy(z)
    P = one(z)
    while abs(zz) < 8
        P *= zz
        zz += one(zz)
    end
    # Стирлинг: log Γ(zz) = (zz−½)log zz − zz + ½log 2π + Σ B_{2k}/(2k(2k−1) zz^{2k−1})
    lg = (zz - BigFloat("0.5")) * log(zz) - zz + BigFloat("0.5") * log(BigFloat(2π))
    for k in 1:12
        lg += BigFloat(BERN[k]) / (BigFloat(2k * (2k - 1)) * zz^BigFloat(2k - 1))
    end
    return lg - log(P)
end

gamma_cf(z::Complex{BigFloat}) = exp(gamma_log(z))

"Риман–Зигель тета-функция θ(t) = Im log Γ(¼+it/2) − (t/2)·log π."
theta_big(t::Real) = imag(gamma_log(Complex{BigFloat}(BigFloat("0.25"),
                                                      BigFloat(t) / 2))) -
                      BigFloat(t) / 2 * log(BigFloat(π))

"""
Контроль полноты по классическому аргументному принципу (стандартный путь
2 → 2+iT → ½+iT, свободный от нулей):
  S(T) = arg ζ(½+iT) (непрерывное продолжение по стандартному пути),
  N(T) = θ(T)/π + 1 + S(T)/π   (Риман–фон Мангольдт).
N(T) считает ВСЕ нули в критической полосе до высоты T; согласие N(T) ≈
числу нулей, найденных на прямой, подтверждает отсутствие вне-прямых нулей
в диапазоне.
"""
function standard_path_arg(T::Float64; h::Float64 = 0.05, hx::Float64 = 0.01)
    half = BigFloat("0.5")
    # вертикальный участок: t = 0 → T при Re s = 2 (ζ(2) > 0 ⇒ arg = 0)
    arg = 0.0
    n1 = Int(ceil(T / h))
    prev = Float64(angle(zeta_em(Complex{BigFloat}(BigFloat(2), BigFloat(0)))))
    for i in 1:n1
        t = min(T, i * h)
        a = Float64(angle(zeta_em(Complex{BigFloat}(BigFloat(2), BigFloat(t)))))
        d = a - prev
        d = mod(d + Float64(π), Float64(2π)) - Float64(π)
        arg += d
        prev = a
        t >= T && break
    end
    # горизонтальный участок: x = 2 → ½ при t = T
    prev = Float64(angle(zeta_em(Complex{BigFloat}(BigFloat(2), BigFloat(T)))))
    n2 = Int(ceil(1.5 / hx))
    for i in 1:n2
        x = max(half, 2 - i * hx)
        a = Float64(angle(zeta_em(Complex{BigFloat}(BigFloat(x), BigFloat(T)))))
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

"Самотесты без эталонных нулей; возвращает Dict с невязками."
function zeta_selftest()
    z2 = zeta_em(Complex{BigFloat}(BigFloat(2), BigFloat(0)))
    z4 = zeta_em(Complex{BigFloat}(BigFloat(4), BigFloat(0)))
    zm1 = zeta_em(Complex{BigFloat}(BigFloat(-1), BigFloat(0)))
    r2 = Float64(abs(z2 - BigFloat(π)^2 / 6))
    r4 = Float64(abs(z4 - BigFloat(π)^4 / 90))
    rm1 = Float64(abs(zm1 + BigFloat(1) / BigFloat(12)))   # ζ(−1) = −1/12
    # Функциональное уравнение в двух фиксированных точках (без нулей):
    function fe_test(re::Float64, im::Float64)
        s = Complex{BigFloat}(BigFloat(re), BigFloat(im))
        lhs = zeta_em(s)
        w = one(s) - s                       # Γ(1−s) = Γ(w)
        gw = gamma_cf(w)
        rhs = BigFloat(2)^s * BigFloat(π)^(s - 1) * sin(BigFloat(π) * s / 2) *
              gw * zeta_em(one(s) - s)
        return Float64(abs(lhs - rhs) / max(1.0, abs(lhs)))
    end
    fe1 = fe_test(0.7, 29.3)
    fe2 = fe_test(1.3, 11.7)
    return Dict("resid_zeta2" => r2, "resid_zeta4" => r4,
                "resid_zeta_minus1" => rm1,
                "resid_functional_eq_1" => fe1,
                "resid_functional_eq_2" => fe2)
end

"""
Сетка t на [t0, t1] с шагом h; значения ζ(½+it); непрерывно продолженный
(развёрнутый) аргумент. Возвращает (ts, args, mags).
"""
function unwrapped_arg(t0::Float64, t1::Float64, h::Float64)
    n = Int(ceil((t1 - t0) / h)) + 1
    ts = [t0 + h * i for i in 0:n-1]
    vals = Vector{Complex{BigFloat}}(undef, n)
    half = BigFloat("0.5")
    for (i, t) in enumerate(ts)
        vals[i] = zeta_em(Complex{BigFloat}(half, BigFloat(t)))
    end
    args = Vector{Float64}(undef, n)
    args[1] = Float64(angle(vals[1]))
    for i in 2:n
        d = Float64(angle(vals[i])) - mod(args[i-1], Float64(2π))
        d = mod(d + Float64(π), Float64(2π)) - Float64(π)   # wrap в (−π, π]
        args[i] = args[i-1] + d
    end
    mags = [Float64(abs(v)) for v in vals]
    return ts, args, mags
end

winding_count(args) = abs(args[end] - args[1]) / Float64(π)

"""
Уточнение нуля на скобке [ta, tb]: золотое сечение по |ζ| (V-образна возле
простого нуля) с ограничением шага; возвращает (t̂, min|ζ|).
"""
function refine_zero(ta::Float64, tb::Float64; tol = 1e-14)
    half = BigFloat("0.5")
    f = t -> Float64(abs(zeta_em(Complex{BigFloat}(half, BigFloat(t)))))
    φ = (sqrt(5.0) - 1) / 2
    a, b = ta, tb
    c = b - φ * (b - a)
    d = a + φ * (b - a)
    for _ in 1:160
        f(c) < f(d) ? (b = d) : (a = c)
        c = b - φ * (b - a)
        d = a + φ * (b - a)
        (b - a) < tol && break
    end
    return (a + b) / 2, f((a + b) / 2)
end

"""
Слепое обнаружение нулей ζ на критической прямой:
сетка h по [t0, t1]; интервал с |Δarg| > π/2 → кандидат (простой ноль);
уточнение золотым сечением. НИКАКИХ эталонных значений.
"""
function detect_zeros(t0::Float64, t1::Float64, h::Float64)
    ts, args, mags = unwrapped_arg(t0, t1, h)
    w = winding_count(args)
    positions = Float64[]
    zmin = Float64[]
    for i in 2:length(ts)
        darg = abs(args[i] - args[i-1])
        if darg > π / 2
            ta = max(ts[i-1] - 2h, t0)     # расширить скобку (устойчивость)
            tb = min(ts[i] + 2h, t1)
            pos, zm = refine_zero(ta, tb)
            push!(positions, pos)
            push!(zmin, zm)
        end
    end
    return Dict("grid_h" => h, "t0" => t0, "t1" => t1,
                "n_grid_points" => length(ts),
                "winding_count" => w,
                "positions" => positions,
                "abs_zeta_at_positions" => zmin,
                "ts" => ts, "args" => args, "mags" => mags)
end

detector_meta() = Dict(
    "module" => "ZetaDetector (e11_zeta_blind.jl)",
    "method" => "argument winding of ζ(½+it); Euler–Maclaurin tail, BigFloat(140)",
    "reference_zeros_used" => false,
    "precision_bits" => PRECISION,
    "N_tail" => N_TERMS[], "K_corrections" => K_TERMS[])

end # module
