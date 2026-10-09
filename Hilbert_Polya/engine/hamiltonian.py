"""engine.hamiltonian — конструкция резонатора (единственный источник).

Эрмитов гамильтониан AB-облака: ландгаузовский флакс 2πα·iy на x-связях,
вихревые фазы q/2·(θ_j−θ_i) на y-связях (RAW разность, разрыв непрерывности
не разворачивается — точный протокол C3), on-site беспорядок W; открытые и
торические границы; расширение C5 (твисты, анизотропия, δα, масса, профиль,
знаки). Самодостаточно: numpy/scipy.
"""
import numpy as np
from scipy.linalg import eigvalsh

# ── протокольные константы (единые для всей серии) ──────────────────────────
BASE_SEED = 96          # мастер-сид серии
HARDCORE_OFFSET = 3500  # поток RNG вихрей: seed + HARDCORE_OFFSET
T_HOP = 1.0             # амплитуда прыжка
CENTER_FRACTION = 0.6   # доля центральной полосы спектра
MIN_DIST = 3.0          # hardcore-минимальная дистанция вихрей


# ── конфигурация вихрей ─────────────────────────────────────────────────────
def random_vortex_configuration(Nv, Nx, Ny, q_mag, rng, mode="protocol",
                                signs="neutral"):
    """Nv вихрей, точный протокол C3: центры ячеек (ix+0.5, iy+0.5),
    ix,iy ~ целые из 1..N−1 — независимый сэмплинг (без hardcore-ограничений).

    Заряды (ручка C5 'signs'):
      'neutral'  — протокол: чётный Nv → первая половина +q, остальные −q
                   (нулевая суммарная циркуляция); нечётный → (Nv+1)/2 плюс;
      'all_plus' — все заряды +q;
      'random'   — знаки ±q случайно.
    Возвращает список (x, y, q).
    """
    if Nv == 0:
        return []
    pts = []
    for _ in range(Nv):  # интерливинг потоков x/y — точный порядок протокола
        pts.append((float(rng.integers(1, Nx)) + 0.5,
                    float(rng.integers(1, Ny)) + 0.5))
    if signs == "neutral":
        half = Nv // 2 if Nv % 2 == 0 else (Nv + 1) // 2
        q = np.full(Nv, float(q_mag))
        q[half:] = -float(q_mag)
    elif signs == "all_plus":
        q = np.full(Nv, float(q_mag))
    elif signs == "random":
        q = float(q_mag) * rng.choice([-1.0, 1.0], size=Nv)
    else:
        raise ValueError(signs)
    return [(x, y, float(qi)) for (x, y), qi in zip(pts, q)]


# ── гамильтониан ─────────────────────────────────────────────────────────────
def build_hamiltonian(Nx, Ny, vortices, alpha, t, W, bc, rng_dis,
                      twist=(0.0, 0.0), aniso=1.0, dalpha=0.0, mass=0.0,
                      profile="site"):
    """Эрмитов гамильтониан AB-облака (самодостаточная реализация).

    * x-связь (ix→ix+1, строка iy): φ = 2π·α_eff·iy, α_eff = α + dalpha;
    * y-связь (iy→iy+1): φ = Σ_k q_k·(θ_j−θ_i)/2, θ_k = atan2 по профилю:
        'site'     — угол из точки i (точечный вихрь, протокол C3);
        'midpoint' — угол из середины связи (ядро конечного радиуса);
    * твисты (C5): на wrap-связях торуса добавляются (φx, φy) —
      спин-структуры в смысле C8;
    * анизотропия (C5): x-прыжок = t/aniso, y-прыжок = t (t_x·t_y = t²);
    * стэггерд-масса (C5): H[i,i] += mass·(−1)^{ix+iy};
    * беспорядок W: on-site V_i = Σ_k q_k·W/(r²N⁻¹+1) + ε_i ~ U(−0.01,0.01);
    * границы: 'open' | 'torus' (торус требует α_eff·Ny ∈ ℤ);
    * эрмитовость по построению: H[i,j] = −t·e^{iφ}, H[j,i] = conj.
    """
    alpha_eff = alpha + dalpha
    if bc == "torus" and abs(alpha_eff * Ny - round(alpha_eff * Ny)) > 1e-10:
        raise AssertionError(f"torus needs α·Ny ∈ ℤ, got {alpha_eff * Ny}")
    N = Nx * Ny
    ix = np.arange(Nx, dtype=np.float64)
    iy1 = np.arange(1, Ny + 1, dtype=np.float64)
    XX, YY = np.meshgrid(ix + 1.0, iy1)
    XX, YY = XX.ravel(), YY.ravel()

    H = np.zeros((N, N), dtype=np.complex128)
    tx = t / aniso
    ty = t

    # ── x-связи ──
    rows = np.repeat(np.arange(Ny), Nx - 1)
    cols = np.tile(np.arange(Nx - 1), Ny)
    i_from = rows * Nx + cols
    i_to = i_from + 1
    phi_x = 2.0 * np.pi * alpha_eff * (rows + 1.0)
    if bc == "torus":
        rw = np.arange(Ny)
        i_from = np.concatenate((i_from, rw * Nx + (Nx - 1)))
        i_to = np.concatenate((i_to, rw * Nx + 0))
        phi_x = np.concatenate((phi_x, 2.0 * np.pi * alpha_eff * (rw + 1.0)
                                + twist[0]))
    H[i_from, i_to] = -tx * np.exp(1j * phi_x)
    H[i_to, i_from] = -tx * np.exp(-1j * phi_x)

    # ── y-связи ──
    iy_pairs = np.arange(Ny - 1)
    cols_v = np.tile(np.arange(Nx), iy_pairs.size)
    rows_v = np.repeat(iy_pairs, Nx)
    j_from = rows_v * Nx + cols_v
    j_to = j_from + Nx
    x1, y1 = XX[j_from], YY[j_from]
    x2, y2 = XX[j_to], YY[j_to]
    if profile == "midpoint":
        x1, y1 = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        x2, y2 = x1, y1  # один и тот же угол для всей связи
    # точный протокол: RAW разность углов (без wrap) по координатам сайтов
    phi_y = np.zeros(j_from.size)
    for (vx, vy, qk) in vortices:
        th = np.arctan2(YY - vy, XX - vx)
        phi_y += 0.5 * qk * (th[j_to] - th[j_from])
    if bc == "torus":
        cw = np.arange(Nx)
        j_from = np.concatenate((j_from, (Ny - 1) * Nx + cw))
        j_to = np.concatenate((j_to, cw))
        # wrap: фаза Ландау 2πα·Ny + вихри с РАЗВЁРНУТОЙ верхней координатой
        xs_c = np.arange(1, Nx + 1, dtype=float)
        phi_w = np.full(Nx, 2.0 * np.pi * alpha_eff * Ny + twist[1])
        for (vx, vy, qk) in vortices:
            th_bot = np.arctan2(Ny - vy, xs_c - vx)
            th_top = np.arctan2(Ny + 1.0 - vy, xs_c - vx)
            phi_w += 0.5 * qk * (th_top - th_bot)
        phi_y = np.concatenate((phi_y, phi_w))
    H[j_from, j_to] = -ty * np.exp(1j * phi_y)
    H[j_to, j_from] = -ty * np.exp(-1j * phi_y)

    # ── on-site: вихревой потенциал + беспорядок + стэггерд-масса ──
    diag = np.zeros(N)
    if W > 0:
        for (vx, vy, qk) in vortices:
            r2 = (XX - vx) ** 2 + (YY - vy) ** 2
            diag += qk * W / (r2 / N + 1.0)
        diag += rng_dis.uniform(-0.01, 0.01, N)
    if mass != 0.0:
        diag += mass * ((np.floor(XX).astype(int) + np.floor(YY).astype(int)) % 2
                        * 2.0 - 1.0)
    H[np.arange(N), np.arange(N)] = diag
    return H


# ── спектральные утилиты (протокол C3) ──────────────────────────────────────
def central_band(sorted_eigs, frac=CENTER_FRACTION):
    """Порт central_band_eigs: half = floor(n·frac/2) (fld-арифметика)."""
    n = sorted_eigs.size
    half = int((n * frac) // 2)
    return sorted_eigs[n // 2 - half: n // 2 + half]


def unfold_poly(vals, degs=(6, 5, 4, 3)):
    """Развёртка полиномиальным счётом; фолбэк — монотонная кусочно-линейная."""
    vals = np.asarray(vals, dtype=float)
    idx = np.arange(vals.size, dtype=float)
    for deg in degs:
        c = np.polyfit(vals, idx, deg)
        u = np.polyval(c, vals)
        if np.all(np.diff(u) > 0):
            return u
    knots = np.linspace(0, vals.size - 1, max(8, vals.size // 16)).astype(int)
    return np.interp(vals, vals[knots], idx[knots])


def window_u(u, k=200, off=10.0):
    u = np.asarray(u, dtype=float)
    i = int(np.searchsorted(u, u[0] + off))
    w = u[i:i + k]
    assert len(w) == k and np.all(np.diff(w) > 0), "окно развёртки нарушено"
    return w - w[0]


def gate_spectrum(Nv, q, W, alpha, L=24, seed=BASE_SEED, bc="open",
                  **handles):
    """Полный конвейер одного затвора: конфигурация → H → спектр → окно."""
    vrng = np.random.default_rng(seed + HARDCORE_OFFSET)
    signs = handles.pop("signs", "neutral")  # протокол C3
    vortices = random_vortex_configuration(Nv, L, L, q, vrng, "protocol",
                                           signs=signs) if Nv > 0 else []
    drng = np.random.default_rng(seed + HARDCORE_OFFSET + 1)
    H = build_hamiltonian(L, L, vortices, alpha, T_HOP, W, bc, drng,
                          **handles)
    ev = np.sort(eigvalsh(H, check_finite=False, driver="evr",
                          overwrite_a=True))
    cen = central_band(ev)
    return window_u(unfold_poly(cen)), float(np.mean(np.diff(cen))), ev


# ── нули ζ ──────────────────────────────────────────────────────────────────
def load_zeros(path, nmax=None):
    z = np.loadtxt(path, dtype=float)
    z = np.sort(z[z > 0])
    return z if nmax is None else z[:nmax]


def rvm_count(g):
    """Гладкий счёт Римана–фон Мангольдта N̄(γ), векторизованный."""
    g = np.asarray(g, dtype=float)
    return g / (2 * np.pi) * np.log(g / (2 * np.pi * np.e)) + 0.625


def sieve_lambda(nmax):
    """Функция фон Мангольдта Λ(n) для n ≤ nmax (решето наименьшего простого
    делителя). Возвращает (lam, primes): lam[n] = Λ(n), lam[0..1] = 0."""
    spf = np.zeros(nmax + 1, dtype=np.int64)
    primes = []
    for i in range(2, nmax + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > nmax:
                break
            spf[i * p] = p
    lam = np.zeros(nmax + 1)
    for p in primes:
        pk = p
        while pk <= nmax:
            lam[pk] = np.log(p)
            pk *= p
    return lam, np.array(primes, dtype=np.int64)
