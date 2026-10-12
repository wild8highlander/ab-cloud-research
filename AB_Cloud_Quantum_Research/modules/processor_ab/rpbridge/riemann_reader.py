# -*- coding: utf-8 -*-
"""rpbridge.riemann_reader — V23-превью: слепое считывание нулей
критической прямой из прямой алгебраической функции.

Главный тезис программы (формулировка пользователя, переведённая в
протокол): суть не в том, что облако «несёт» нули Римана, а в том, что
оно **считывает** нули с критической прямой через прямые алгебраические
функции. Протокол отделяет «читает» от «хранит»:

  Вход  — прямая формула ζ(s) (определяющий ряд/Эйлер–Маклорен,
          mpmath, O(1) констант; ТАБЛИЦА НУЛЕЙ НЕ ИСПОЛЬЗУЕТСЯ нигде
          в пайплайне считывания);
  Механизм — аргументная намотка (winding): фаза arg ζ(½+it) вдоль
          критической прямой совершает скачок π на каждом нуле
          (V19: Z₂-монодромия, строгое чередование); число скачков =
          число нулей на отрезке — это аргументный принцип,
          исполненный фазовой аппаратурой процессора (фаза — родной
          язык AB-облака: V19, фазовый закон ζ^{ra+sb});
  Выход — положения нулей (уточнение по минимуму |ζ| —
          интерферометрическое считывание);
  Контроль — независимый метод (знаки вещественной функции
          Z(t) = e^{iθ(t)}ζ(½+it), бисекция) применяется ТОЛЬКО после
          фиксации результата чтения (blind-протокол V1).

Метрики: совпадение числа нулей (точно), максимальное позиционное
отклонение, полоса считывания, бухгалтерия хранения (0 нулей
хранится; хранится только формула).
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 25


def zeta_samples(t_grid):
    """Прямая формула: ζ(½+it) на сетке (mpmath). Это ВЕСЬ вход
    пайплайна считывания — O(1) констант, нулевой таблицы нет."""
    return np.array([complex(mp.zeta(mp.mpc('0.5', float(t))))
                     for t in t_grid])


def winding_zeros(z_samples, t_grid, refine=17):
    """Чтение нулей аргументной намоткой.

    1. φ_j = arg ζ; намотка unwrapped.
    2. Скачки |Δφ| > π/2 — прохождения нулей (монодромия π, V19).
    3. Позиция: середина интервала-скобки, уточнение минимумом |ζ|
       на под-сетке (интерферометрическое считывание).
    Возвращает (позиции, число скачков, развёрнутая намотка)."""
    phi = np.angle(z_samples)
    phi_u = np.unwrap(phi)
    dphi = np.diff(phi_u)
    slips = np.where(np.abs(dphi) > np.pi / 2)[0]
    positions = []
    for j in slips:
        t_lo, t_hi = t_grid[j], t_grid[j + 1]
        if refine > 2:
            sub = np.linspace(t_lo, t_hi, refine)
            zs = zeta_samples(sub)
            positions.append(float(sub[int(np.argmin(np.abs(zs)))]))
        else:
            positions.append(float(0.5 * (t_lo + t_hi)))
    return np.array(positions), len(slips), phi_u


def reference_positions(t0, t1):
    """Независимый контроль: нули вещественной функции
    Z(t) = e^{iθ(t)}ζ(½+it) (θ — Зигель-тета), бисекция по смене знака.
    Используется ТОЛЬКО как контроль после чтения."""
    def Z(t):
        return mp.zeta(mp.mpc('0.5', float(t))) * \
            mp.exp(1j * mp.siegeltheta(float(t)))
    # сетка грубая для скобок
    grid = np.linspace(t0, t1, max(64, int((t1 - t0) * 8)))
    vals = [mp.re(Z(float(t))) for t in grid]
    zeros = []
    for i in range(len(grid) - 1):
        if vals[i] == 0:
            zeros.append(float(grid[i]))
            continue
        if vals[i] * vals[i + 1] < 0:
            lo, hi = float(grid[i]), float(grid[i + 1])
            flo = vals[i]
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                fm = mp.re(Z(mid))
                if flo * fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            zeros.append(0.5 * (lo + hi))
    return np.array(zeros)


def read_zeros(t0=2.0, t1=58.0, M=560, refine=17):
    """Полный протокол считывания + контроль. Возвращает вердикт
    чтения: счёт (точно), позиции, отклонения, бухгалтерия."""
    t_grid = np.linspace(t0, t1, M)
    z = zeta_samples(t_grid)
    pos, n_slips, phi_u = winding_zeros(z, t_grid, refine=refine)
    ref = reference_positions(t0, t1)
    K = len(ref)
    count_match = bool(n_slips == K)
    devs = []
    if count_match and K > 0:
        devs = np.abs(np.sort(pos) - ref)
    dt = float(t_grid[1] - t_grid[0])
    return dict(
        window=[t0, t1], n_samples=M,
        zeros_read=int(n_slips), zeros_reference=int(K),
        count_exact=count_match,
        positions_read=[float(p) for p in np.sort(pos)],
        positions_reference=[float(p) for p in ref],
        max_position_dev=float(np.max(devs)) if len(devs) else None,
        sampling_dt=dt,
        reading_bandwidth_zeros_per_1000=float(1000.0 * K / M),
        stored_zero_tables=0,
        stored_constants='O(1): формула ζ (Euler–Maclaurin, mpmath)',
        passed=bool(count_match
                    and (len(devs) == 0
                         or float(np.max(devs)) <= 0.5 * dt)))


def storage_accounting(K):
    """Бухгалтерия «хранение vs чтение»: чтобы ВЫДАТЬ K нулей, пайплайн
    хранит формулу (O(1) констант), а не таблицу K нулей (2K чисел).
    Коэффициент считывания = K / c."""
    c = 6   # константы формулы ζ (укрупнённо: ряд + ускорение + точность)
    return dict(zeros_produced=K, stored_zeros=0,
                stored_formula_constants=c,
                reading_ratio=float(K / c),
                note='нули воспроизводятся из функции по запросу; '
                     'таблица нулей не входит ни во вход, ни в состояние')
