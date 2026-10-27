# e16_rs_engine.jl — ЭКСПЕРИМЕНТ 16: независимый движок Римана–Зигеля.
#
# Структура формулы — Ариас де Рейна I/II (High Precision Computation of
# Riemann's Zeta Function by the Riemann–Siegel Formula, I & II); сборка
# сверена с реализацией mpmath/functions/rszeta.py (J. Arias de Reyna, BSD).
# Коэффициенты F вычисляются САМИ (без рукописных таблиц) через целочисленную
# рекурренту чисел Эйлера (A000111) и две устойчивые свёртки — на повышенной
# точности (400 бит), т.к. промежуточные члены растут ~4^n при истинных c_n,
# убывающих суперэкспоненциально (F — целая функция порядка 2).
#
# Дисциплина: движок НЕ содержит эталонных нулей. Проверки:
#   (a) ряд F против прямой формулы (|z| ≤ 0.999) ≤ 1e−30;
#   (b) вещественность Z(t) = e^{iθ}ζ(½+it) ≤ 1e−12;
#   (c) согласие с Эйлером–Маклореном (ZetaDetector.zeta_em) на общих сетках
#       при равной точности ≤ 1e−9 (предрегистрированный порог O-J1);
#   (d) документирование пола ошибки и стоимостей (без порога).

module RiemannSiegel

using ..ZetaDetector

export zeta_rs_line, zeta_rs, Z_rs, rs_selftest, rs_meta,
       zeta_em_scaled, em_schedule, reference_em

const WORK_PRECISION = 140
const SETUP_PRECISION = 400
const JMAX = 200            # порядок ряда F
const MMAX = 60             # максимальный порядок производных F
setprecision(BigFloat, WORK_PRECISION)

# ── Числа Эйлера-зигзага E_n (A000111), точные BigInt ─────────────────────
# E_{n+1} = (Σ_k C(n,k)E_kE_{n−k} + δ_{n0})/2;  секанс-числа S_{2j} = E_{2j}.
function _zigzag(m::Int)
    E = BigInt[1]
    for n in 1:m
        s = sum(binomial(BigInt(n - 1), BigInt(k)) * E[k+1] * E[n-k] for k in 0:(n-1))
        if n == 1
            s += 1
        end
        push!(E, s ÷ 2)
    end
    return E
end

# ── Коэффициенты ряда F (на 400 бит, один раз) ────────────────────────────
# F(z) = (e^{πi(z²/2+3/8)} − i√2·cos(πz/2)) / (2cos(πz)) = Σ_n c_n z^n (чётные)
function _taylor_F(order::Int)
    return setprecision(BigFloat, SETUP_PRECISION) do
        E = _zigzag(order + 2)
        c = fill(complex(BigFloat(0), BigFloat(0)), order + 1)
        phase = exp(complex(BigFloat(0), 3 * BigFloat(π) / 8))
        sq2 = sqrt(BigFloat(2))
        pihalf = BigFloat(π) / 2
        for n in 0:(order ÷ 2)
            # Part2: −i√2 · Σ_k (−1)^k (π/2)^{2k}/(2k)! · ½S_{2(n−k)}π^{2(n−k)}/(2n−2k)!
            p2 = Complex{BigFloat}(0)
            for k in 0:n
                j = n - k
                p2 += (-1)^k * pihalf^(2k) / BigFloat(factorial(BigInt(2k))) *
                      E[2j+1] * BigFloat(π)^(2j) / BigFloat(factorial(BigInt(2j)))
            end
            p2 *= complex(BigFloat(0), -sq2 / 2)
            # Part1: e^{3πi/8} · Σ_j S_{2j}π^{2j}/(2j)! · (iπ/2)^{n−j}/(n−j)! · ½
            p1 = Complex{BigFloat}(0)
            for j in 0:n
                m = n - j
                p1 += E[2j+1] * BigFloat(π)^(2j) / BigFloat(factorial(BigInt(2j))) *
                      complex(BigFloat(0), pihalf)^m / BigFloat(factorial(BigInt(m)))
            end
            p1 *= phase / 2
            c[2n+1] = p1 + p2
        end
        return c
    end
end

const TAYLOR_HP = _taylor_F(JMAX)

# ── Таблица производных рядов Dm[m][j] = (j+m)!/j! · c_{j+m} ──────────────
# F^{(m)}(p) = Σ_j Dm[m][j]·p^j — поточечно, без сдвигов ряда.
# Строится на 400 бит, затем ЧЕСТНО округляется до рабочих 140 бит.
function _dm_table()
    rows_hp = setprecision(BigFloat, SETUP_PRECISION) do
        fact = [factorial(BigInt(i)) for i in 0:JMAX]
        rows = Vector{Vector{Complex{BigFloat}}}(undef, MMAX + 1)
        for m in 0:MMAX
            row = Vector{Complex{BigFloat}}(undef, JMAX - m + 1)
            for j in 0:(JMAX - m)
                ratio = fact[j+m+1] // fact[j+1]
                row[j+1] = TAYLOR_HP[j+m+1] * BigFloat(ratio)
            end
            rows[m+1] = row
        end
        return rows
    end
    # округление до рабочей точности (создание новых BigFloat при 140 битах)
    rows_w = Vector{Vector{Complex{BigFloat}}}(undef, MMAX + 1)
    for m in 0:MMAX
        row = rows_hp[m+1]
        rows_w[m+1] = [Complex{BigFloat}(BigFloat(real(v)), BigFloat(imag(v)))
                       for v in row]
    end
    return rows_w
end

const DM = _dm_table()

# ── Универсальные коэффициенты d[n,k] (σ=1/2, psigma=0) ───────────────────
function _d_table(L::Int)
    d = Vector{Dict{Int,BigFloat}}(undef, L)
    d[1] = Dict{Int,BigFloat}(0 => BigFloat(1))
    for n in 1:(L-1)
        dn = Dict{Int,BigFloat}()
        for k in 0:(3n ÷ 2)
            m = 3n - 2k
            if m != 0
                acc = BigFloat(0)
                if haskey(d[n], k - 2)
                    acc -= (m + 1) * d[n][k-2]
                end
                if haskey(d[n], k)
                    acc += d[n][k] / (4 * m)
                end
                dn[k] = acc
            else
                acc = BigFloat(0)
                for r in 0:(k-1)
                    fk = factorial(BigInt(2k - 2r)) // factorial(BigInt(k - r))
                    acc -= dn[r] * (-1)^(k - r) * BigFloat(fk)
                end
                dn[k] = acc
            end
        end
        d[n+1] = dn
    end
    return d
end

const D_FULL = _d_table(MMAX ÷ 3 + 2)

const PIPOW = let v = Vector{BigFloat}(undef, 2 * MMAX + 2)
    v[1] = BigFloat(1)
    for i in 1:(2 * MMAX + 1)
        v[i+1] = v[i] * BigFloat(π)
    end
    v
end

const POW2I = [complex(BigFloat(0), BigFloat(2))^ell for ell in 0:MMAX]

const LN_TABLE = [log(BigFloat(i)) for i in 1:16384]
const ISQRT_TABLE = [1 / sqrt(BigFloat(i)) for i in 1:16384]

"n^{-s} для n ≤ 4096: n^{-1/2}·(cos(t ln n) − i·sin(t ln n)) через sincos."
@inline function fast_npow(n::Int, σ::BigFloat, t::BigFloat)
    lnn = @inbounds LN_TABLE[n]
    # σ фиксирован ½ или 2 в наших вызовах: обобщённо через exp только при σ ≠ ½
    if σ == BigFloat("0.5")
        e = @inbounds ISQRT_TABLE[n]
    else
        e = exp(-σ * lnn)
    end
    ph = -t * lnn
    sn, cs = sincos(ph)
    return complex(e * cs, e * sn)
end

"""
ζ(½+it) движком Римана–Зигеля (Ариас де Рейна). Возвращает (ζ, meta).
Обрезка асимптотического ряда: U-turn с шагом 2 (члены затухают парами
нечёт/чёт) либо ранний выход при |term_k| < target/100.
"""
function zeta_rs_line(t::Float64; target::Float64 = 1e-14)
    tb = BigFloat(t)
    a = sqrt(tb / (2 * BigFloat(π)))
    N = Int(floor(a))
    p = 1 - 2 * (a - N)
    Lcap = length(D_FULL) - 1
    # степени p (реальные)
    pw = Vector{BigFloat}(undef, JMAX + 1)
    pw[1] = BigFloat(1)
    for j in 1:JMAX
        pw[j+1] = pw[j] * p
    end
    # ленивые F^{(m)}(p) — инкрементально, без замыканий
    fp = Vector{Complex{BigFloat}}(undef, MMAX + 1)
    have = -1
    ainv = 1 / a
    ak = BigFloat(1)
    rssum = Complex{BigFloat}(0)
    prev_mag = BigFloat(0)
    prev2_mag = BigFloat(0)
    L_used = 0
    floor_mag = BigFloat(0)
    for k in 0:Lcap
        mtop = min(3k, MMAX)
        while have < mtop
            have += 1
            row = DM[have+1]
            acc = Complex{BigFloat}(0)
            @inbounds for j in 0:(length(row) - 1)
                acc += row[j+1] * pw[j+1]
            end
            fp[have+1] = acc
        end
        term = Complex{BigFloat}(0)
        for ell in 0:(3k ÷ 2)
            dk = get(D_FULL[k+1], ell, BigFloat(0))
            dk == 0 && continue
            term += dk * fp[3k - 2ell + 1] / (PIPOW[2k - ell + 1] * POW2I[ell+1])
        end
        mag = abs(term * ak)
        if k >= 2 && mag > prev2_mag && mag > target
            break                          # U-turn асимптотики (шаг 2)
        end
        rssum += term * ak
        L_used = k + 1
        floor_mag = mag
        mag < target / 100 && break
        prev2_mag = prev_mag
        prev_mag = mag
        ak *= ainv
    end
    arg = (tb / 2) * log(tb / (2 * BigFloat(π))) - tb / 2 - BigFloat(π) / 8
    sign_flip = (N - 1) % 2 == 0 ? BigFloat(1) : BigFloat(-1)
    S3 = sign_flip * sqrt(ainv) * exp(complex(BigFloat(0), -arg))
    # S1 = Σ_{n=1}^{N} n^{-s}   (усечение ВКЛЮЧИТЕЛЬНО: _zetasum(s,1,N−1)=Σ_{j≤N})
    S1 = Complex{BigFloat}(0)
    half = BigFloat("0.5")
    for n in 1:N
        S1 += fast_npow(n, half, tb)
    end
    R = S1 + rssum * S3
    theta = theta_big(t)
    zeta = R + exp(complex(BigFloat(0), -2 * theta)) * conj(R)
    meta = Dict("N" => N, "p" => Float64(p), "L" => L_used,
                "floor" => Float64(floor_mag))
    return zeta, meta
end

"ζ(½+it) — обёртка."
zeta_rs(t::Float64) = zeta_rs_line(t)[1]

"Z(t) = e^{iθ}·ζ(½+it) — вещественная функция Римана–Зигеля."
function Z_rs(t::Float64)
    z, _ = zeta_rs_line(t)
    return exp(complex(BigFloat(0), theta_big(t))) * z
end

const RS_META = Dict{String,Any}(
    "module" => "RiemannSiegel (e16_rs_engine.jl)",
    "method" => "Riemann–Siegel expansion (Arias de Reyna I/II); coefficients from integer Euler recurrence, no hand tables",
    "setup_precision_bits" => SETUP_PRECISION,
    "work_precision_bits" => WORK_PRECISION,
    "taylor_order" => JMAX,
    "max_F_derivative" => MMAX,
    "truncation" => "stride-2 U-turn on |term_k|")

rs_meta() = RS_META

# ── Масштабируемый Эйлер–Маклорен (референсный движок для сравнения) ──────
# ζ(s) = Σ_{n<N} n^{-s} + N^{1-s}/(s−1) + ½N^{-s} + Σ_k [B_{2k}/(2k)!]·s^{↑(2k−1)}·N^{-s-2k+1}
# Ошибка хвоста ~ t^{2K+1}/((2K+2)!·N^{2K+1/2}) ⇒ расписание растёт с высотой.
"ζ(s) Эйлером–Маклореном с явным расписанием (N, K)."
function zeta_em_scaled(s::Complex{BigFloat}; N::Int = 64, K::Int = 14)
    acc = Complex{BigFloat}(0)
    σ = real(s); t = imag(s)
    for n in 1:(N-1)
        acc += fast_npow(n, σ, t)
    end
    Nb = BigFloat(N)
    acc += Nb^(1 - s) / (s - 1)
    acc += BigFloat("0.5") * Nb^(-s)
    sp = s                                        # s^{↑1}
    for k in 1:K
        bern = BigFloat(ZetaDetector.BERN[k])
        fact = BigFloat(factorial(BigInt(2k)))
        acc += bern * sp * Nb^(-s - BigFloat(2k - 1)) / fact
        sp *= (s + BigFloat(2k - 1)) * (s + BigFloat(2k))   # s^{↑(2k+1)}
    end
    return acc
end

"Расписание ЭМ по высоте: N = 64·2^k ≥ 0.512·t (хвост ~ (t/N)^{2K+1}/((2K+2)!·N^{1/2})), K=14."
function em_schedule(t::Float64)
    N = 64
    while N < 0.512 * t + 1.0
        N *= 2
    end
    return N, 14
end

"ζ(½+it) Эйлером–Маклореном с масштабируемым расписанием (референс E16/E17)."
function reference_em(t::Float64)
    N, K = em_schedule(t)
    return zeta_em_scaled(complex(BigFloat("0.5"), BigFloat(t)); N = N, K = K)
end

"""
Самотесты движка (без эталонных нулей):
  F-ряд против прямой формулы в 5 точках (≤1e−30);
  вещественность Im[e^{iθ}ζ_RS] на сетке высот (≤1e−12);
  согласие с Эйлером–Маклореном на общих сетках (порог 1e−9 — предрегистрирован).
"""
function rs_selftest(; grid_step::Float64 = 3.7, t0::Float64 = 250.0,
                     t1::Float64 = 1000.0)
    f_resid = 0.0
    for zt in (0.13, 0.31, 0.47, 0.93, 0.999)
        zb = BigFloat(zt)
        direct = (exp(complex(BigFloat(0), BigFloat(π) * (zb^2 / 2 + BigFloat(3) / 8))) -
                  complex(BigFloat(0), 1) * sqrt(BigFloat(2)) *
                  cos(BigFloat(π) * zb / 2)) / (2 * cos(BigFloat(π) * zb))
        series = Complex{BigFloat}(0)
        for n in 0:140
            series += TAYLOR_HP[n+1] * zb^n
        end
        f_resid = max(f_resid, Float64(abs(direct - series)))
    end
    realness = 0.0
    agree_max = 0.0
    ts = Float64[]
    t = t0
    while t <= t1
        push!(ts, t)
        t += grid_step
    end
    for t in ts
        zb = BigFloat(t)
        z, _ = zeta_rs_line(t)
        zref = reference_em(t)
        agree_max = max(agree_max, Float64(abs(z - zref)))
        Zv = exp(complex(BigFloat(0), theta_big(t))) * z
        realness = max(realness, Float64(abs(imag(Zv))))
    end
    return Dict("F_series_residual" => f_resid,
                "Z_realness_max" => realness,
                "agree_vs_em_max" => agree_max,
                "n_grid_points" => length(ts))
end

end # module
