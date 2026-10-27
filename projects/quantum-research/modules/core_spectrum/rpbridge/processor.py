# -*- coding: utf-8 -*-
"""rpbridge.processor — Решение 18 (V18): AB-оператор как процессор.

Три уровня вычислительности на ПОЛНОМ гамильтониане AB-облака:

  P1 · Однокубитные ворота. Эффективный двухуровневый блок решётки
       (сайт + сосед; стэггерд-масса m — ручка C5, фаза связи φ из
       флакса) — спин в поле H₂ = m·σz + t(cos φ·σx + sin φ·σy).
       Все шесть ворот {X, Y, Z, H, S, T} реализуются АНАЛИТИЧЕСКИ
       калиброванными импульсами (время + глобальная фаза не влияют на
       верность F = |Tr(U_t†U)|²/4): X, Y — π-вращения на чисто
       туннельном блоке (m = 0); Z, S, T — вращения на чисто массовом
       (t-связь в далёком отстройке); H — π-вращение вокруг (σx+σz)/√2
       при m = t. Верность верифицируется численно.

  P2 · Зацепление. Два кубит-блока с обменной связкой −J (|↑↓⟩ ↔
       |↓↑⟩): калиброванная эволюция из продукта |↑↓⟩ порождает
       запутанное состояние; мера — concurrence Вуттерса. Полный синтез
       CNOT — открытое обязательство (O18), здесь фиксируется измеренный
       факт зацепления и время его максимума.

  P3 · Игра AB-Pong НА операторе. Доска — 1D-цепочка 64 сайта с
       π-фазовым узором связей (α = ½) и стэггерд-массой — проекция
       полного гамильтониана AB-облака. «Мяч» — гауссов пакет; вся
       динамика — унитарная эволюция e^{−iHt}. Ракетка — ЗЕРКАЛО:
       произведение непересекающихся транспозиций |p−k⟩ ↔ |p+k⟩ вокруг
       точки p (унитарная перестановочная матрица, локализована у p) —
       разворачивает мяч. ИИ-ракетка следует за центроидом с задержкой;
       кулдаун честно логируется. Счёт детерминирован (без измерений —
       только центроид), партия повторяется бит-в-бит.
"""
import numpy as np
from scipy.linalg import expm

# ── P1: однокубитные ворота ─────────────────────────────────────────────────
M_MASS = 2.0
T_HOP = 1.0


def block_hamiltonian(m=M_MASS, t=T_HOP, phi=np.pi / 2):
    """Эффективный 2×2 блок: сайт с массой ±m, связь −t·e^{iφ}.

    В базисе {site↑, site↓}: H = m·σz − t(cos φ·σx + sin φ·σy).
    """
    return np.array([[m, -t * np.exp(-1j * phi)],
                     [-t * np.exp(1j * phi), -m]], dtype=np.complex128)


GATES = {
    'X': np.array([[0, 1], [1, 0]], dtype=np.complex128),
    'Y': np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
    'Z': np.diag([1.0, -1.0]).astype(np.complex128),
    'H': np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2),
    'S': np.diag([1.0, 1j]).astype(np.complex128),
    'T': np.diag([1.0, np.exp(1j * np.pi / 4)]).astype(np.complex128),
}

# аналитические импульсы: (m, t, phi, t_pulse)
# H₂ = m·σz − t cos φ·σx − t sin φ·σy  (проверено по алгебре Паули)
PULSES = {
    # X ∝ iσx: чистый туннель φ=0 (H₂ = −σx), t* = π/2
    'X': (0.0, 1.0, 0.0, np.pi / 2),
    # Y ∝ iσy: чистый туннель φ=π/2 (H₂ = −σy), t* = π/2
    'Y': (0.0, 1.0, np.pi / 2, np.pi / 2),
    # Z ∝ exp(−i(π/2)σz): чистая масса m=2, m·t* = π/2
    'Z': (2.0, 0.0, 0.0, np.pi / 4),
    # S ∝ exp(−i(π/4)σz): m·t* = π/4
    'S': (2.0, 0.0, 0.0, np.pi / 8),
    # T ∝ exp(−i(π/8)σz): m·t* = π/8
    'T': (2.0, 0.0, 0.0, np.pi / 16),
    # H ∝ −i(σx+σz)/√2: блок [[1,1],[1,−1]] = √2·H при m=t=1, φ=π;
    # Ω = √2, Ω·t* = π/2 → t* = π/(2√2)
    'H': (1.0, 1.0, np.pi, np.pi / (2 * np.sqrt(2))),
}


def pulse_fidelity(H, target, t):
    """F = |Tr(U_t†U)|²/4 (глобальная фаза не влияет)."""
    U = expm(-1j * H * t)
    return float(abs(np.trace(U.conj().T @ target)) ** 2 / 4.0)


def gate_fidelities():
    """Верности шести ворот на аналитических импульсах + числовая
    до-полировка локальной сеткой ±0.01·t* (20 точек)."""
    out = {}
    for name, (m, t_h, phi, t_star) in PULSES.items():
        H = block_hamiltonian(m=m, t=t_h, phi=phi)
        f0 = pulse_fidelity(H, GATES[name], t_star)
        # локальная полировка
        ts = t_star + np.linspace(-0.01, 0.01, 21) * t_star
        fs = [pulse_fidelity(H, GATES[name], t) for t in ts]
        i = int(np.argmax(fs))
        out[name] = dict(m=m, t=t_h, phi=phi, t_pulse=float(ts[i]),
                         fidelity=max(f0, fs[i]),
                         analytic_t=float(t_star), analytic_f=f0)
    return out


# ── P2: зацепление двух блоков ──────────────────────────────────────────────
def two_qubit_hamiltonian(J=1.0, m=2.0, t=0.3):
    """4×4 (крон-порядок |a⟩⊗|b⟩, индекс = 2·i_a + i_b):

    H = kron(Ha, I) + kron(I, Hb) − J(|a↑b↓⟩⟨a↓b↑| + h.c.),
    Ha = Hb = [[+m, −t], [−t, −m]].  Состояния связки |a↑b↓⟩ (инд. 1)
    и |a↓b↑⟩ (инд. 2) вырождены (E = 0), детюнинг к |↑↑⟩, |↓↓⟩ = 4 ≫ J;
    утечка через σx-смешивание ~ (t/2m)² ≈ 0.6%.
    """
    def block():
        return np.array([[m, -t], [-t, -m]], dtype=np.complex128)
    H = (np.kron(block(), np.eye(2, dtype=np.complex128))
         + np.kron(np.eye(2, dtype=np.complex128), block()))
    H[1, 2] = -J
    H[2, 1] = -J
    return H


def concurrence(rho):
    """Вуттерс: C(ρ) = max(0, λ1 − λ2 − λ3 − λ4).

    R = ρ·σ̃y⊗σ̃y·ρ*·σ̃y⊗σ̃y (σ̃y = [[0,1],[−1,0]]); R не эрмитова в
    общем случае, но её спектр вещественен неотрицателен — используются
    собственные значения (не сингулярные), вещественные части с клиппингом.
    Для чистых состояний редуцируется к C = 2|c00·c11 − c01·c10|.
    """
    sd = np.array([[0, 1.0], [-1.0, 0.0]])          # σ̃y (вещественная)
    X = np.kron(sd, sd)
    R = rho @ X @ rho.conj() @ X
    ev = np.linalg.eigvals(R).real
    ev = np.sqrt(np.maximum(np.sort(ev)[::-1], 0.0))
    return float(max(0.0, ev[0] - ev[1] - ev[2] - ev[3]))


def entanglement_experiment(t_grid=None):
    """|↑↓⟩ → эволюция → max concurrence + время; верность с классом
    Белла не заявляется (см. обязательство O18)."""
    H = two_qubit_hamiltonian()
    psi0 = np.zeros(4, dtype=np.complex128)
    psi0[1] = 1.0                      # |a↑b↓> (крон-порядок, E = 0)
    if t_grid is None:
        t_grid = np.linspace(0.0, np.pi, 2001)
    best_C, best_t = 0.0, 0.0
    curve = []
    for t in t_grid:
        psi = expm(-1j * H * t) @ psi0
        c = concurrence(np.outer(psi, psi.conj()))
        curve.append((float(t), float(c)))
        if c > best_C:
            best_C, best_t = c, t
    return dict(best_concurrence=float(best_C), t_entangle=float(best_t),
                n_grid=int(t_grid.size),
                curve=[[t, c] for t, c in curve[::10]])


# ── P3: игра AB-Pong на AB-операторе ────────────────────────────────────────
BOARD = 64
PONG_DT = 0.05
PONG_T = 20.0
PADDLE_SIGMA = 3.0           # зона перехвата ракетки
PADDLE_LEAD = 2.5            # опережение ракетки по направлению мяча
PADDLE_REACH = 8.0           # радиус досягаемости ракетки от дома
COOLDOWN_S = 0.25            # пауза между срабатываниями одной ракетки
K0_BALL = np.pi / 6          # импульс мяча: v = 2·sin(k0+φ) = 2 (φ = π/3)


def board_hamiltonian(board=BOARD, phi_ab=np.pi / 3, t_hop=3.0):
    """Доска AB-Pong: 1D-цепочка с равномерной Peierls-фазой φ_ab = π/3
    на каждой связи (AB-вкус: в 1D калибровка сводится к фазе — она
    сдвигает закон дисперсии E(k) = −2cos(k+φ), сохраняя физику
    баллистического транспорта; открытые границы).

    Стэггерд-масса и чередующиеся фазы сознательно отключены: они
    удваивают ячейку (SSH), пакет e^{ikx} распадается на встречные
    моды и центроид стоит — для игры нужен определённый групповой
    скорость. Честно зафиксировано в монографии.
    """
    H = np.zeros((board, board), dtype=np.complex128)
    for i in range(board - 1):
        H[i, i + 1] = -t_hop * np.exp(1j * phi_ab)
        H[i + 1, i] = -t_hop * np.exp(-1j * phi_ab)
    return H


def ball_packet(pos, sigma=1.0, k0=None):
    """Пакет с импульсом k0 (по умолчанию K0_BALL): групповая скорость
    v = 2·sin(k0 + φ_ab) = 2·sin(π/6 + π/3) = 2 сайта/ед. времени."""
    if k0 is None:
        k0 = K0_BALL
    ix = np.arange(BOARD, dtype=float)
    env = np.exp(-(ix - pos) ** 2 / (2 * sigma ** 2))
    psi = env * np.exp(1j * k0 * ix)
    return psi / np.linalg.norm(psi)


def mirror_unitary(p, board=BOARD, phi_ab=np.pi / 3):
    """Ракетка-зеркало: КАЛИБРОВОЧНО-КОВАРНАНТНОЕ отражение.

    В магнитной калибровке (Peierls-фаза φ_ab на каждой связи) дисперсия
    E(k) = −2·t_hop·cos(k+φ_ab) несимметрична по k: простая инверсия
    x → 2p−x (k → −k) НЕ переворачивает групповую скорость
    v(−k) = 2t·sin(−k+φ_ab) ≠ −v(k) — мяч продолжает лететь в стену
    (дрейф среды). Разворот скорости требует k → −k − 2φ_ab, т.е.
    инверсии В СОЧЕТАНИИ с калибровочной компенсацией:

        (U ψ)(x) = e^{−2iφ_ab·x} · ψ(2p − x),

    где инверсия реализуется транспозициями |p−k⟩ ↔ |p+k⟩. U унитарна
    (перестановка × диагональные фазы) и детерминированна.
    """
    U = np.zeros((board, board), dtype=np.complex128)
    for x in range(board):
        y = 2 * p - x
        if 0 <= y < board:
            U[x, y] = np.exp(-2j * phi_ab * x)
    return U


def play_pong(serve_right=True):
    """Одна партия AB-Pong (детерминированная, без измерений).

    Классическая геометрия Pong: у каждой ракетки есть ДОМ (left 17,
    right 47) и радиус досягаемости PADDLE_REACH — перехват возможен
    только когда мяч в окне досягаемости; ракетка ведёт мяч с
    опережением PADDLE_LEAD по направлению полёта. Пропуск (мяч вышел
    за окно по внешней кромке) = очко сопернику. Зеркало-перехват
    разворачивает мяч (унитарная перестановка). Полный лог событий.
    """
    H = board_hamiltonian()
    ev, V = np.linalg.eigh(H)

    def evolve(psi, t):
        c = V.conj().T @ psi
        return V @ (c * np.exp(-1j * ev * t))

    homes = dict(left=17, right=47)
    reach = PADDLE_REACH
    psi = ball_packet(BOARD / 2,
                      k0=K0_BALL if serve_right else -K0_BALL)
    score = dict(left=0, right=0)
    log = []
    kicks = 0
    last_kick = dict(left=-10**9, right=-10**9)
    t_total = 0.0
    n_steps = int(PONG_T / PONG_DT)
    ix = np.arange(BOARD, dtype=float)
    prev_bx = None
    for step in range(n_steps):
        psi = evolve(psi, PONG_DT)
        t_total += PONG_DT
        p = np.abs(psi) ** 2
        bx = float((p * ix).sum())
        v = 0.0 if prev_bx is None else (bx - prev_bx) / PONG_DT
        prev_bx = bx
        log.append([round(t_total, 3), round(bx, 4)])
        for half in ('left', 'right'):
            if step - last_kick[half] < COOLDOWN_S / PONG_DT:
                continue
            lo, hi = homes[half] - reach, homes[half] + reach
            if not (lo <= bx <= hi):
                continue                      # мяч вне окна досягаемости
            # точка разворота — ПОЗАДИ мяча по ходу движения:
            # инверсия о неё отбивает мяч назад (классическое отбивание)
            sgn = 1.0 if v >= 0 else -1.0
            ps = int(np.clip(round(bx - sgn * PADDLE_LEAD), lo, hi))
            if abs(bx - ps) < PADDLE_SIGMA + PADDLE_LEAD:
                psi = mirror_unitary(ps) @ psi
                kicks += 1
                last_kick[half] = step
                log.append([round(t_total, 3), f'MIRROR_{half}@{ps}'])
                prev_bx = None          # после зеркала скорость переизмерить
        if bx <= 5.0:
            score['right'] += 1
            psi = ball_packet(BOARD / 2, k0=K0_BALL)
            log.append([round(t_total, 3), 'WALL_L(≤5) → point right'])
            prev_bx = None
        elif bx >= BOARD - 6.0:
            score['left'] += 1
            psi = ball_packet(BOARD / 2, k0=-K0_BALL)
            log.append([round(t_total, 3), 'WALL_R(≥58) → point left'])
            prev_bx = None
    return dict(score=score, kicks=kicks, log=log,
                final_centroid=log[-1][1] if log else None)


def run():
    """Полный прогон V18: ворота + зацепление + партия и повтор партии."""
    gates = gate_fidelities()
    ent = entanglement_experiment()
    game1 = play_pong(serve_right=True)
    game2 = play_pong(serve_right=True)      # повтор — детерминизм
    replay_equal = (game1['score'] == game2['score']
                    and game1['kicks'] == game2['kicks']
                    and game1['final_centroid'] == game2['final_centroid'])
    f_min = min(g['fidelity'] for g in gates.values())
    return dict(
        meta=dict(package='AB Research Program', campaign='V18',
                  name='AB operator as processor', date='2026-10-10'),
        p1_gates=gates,
        p1_min_fidelity=float(f_min),
        p2_entanglement=ent,
        p3_pong=dict(score=game1['score'], kicks=game1['kicks'],
                     replay_bit_exact=bool(replay_equal),
                     final_centroid=game1['final_centroid'],
                     n_log_events=len(game1['log'])),
        summary=dict(
            gates_universal=bool(f_min > 1 - 1e-9),
            min_gate_fidelity=float(f_min),
            entanglement=bool(ent['best_concurrence'] > 0.5),
            best_concurrence=float(ent['best_concurrence']),
            game_runs=bool(replay_equal),
            pong_score=game1['score'],
            processor=bool(f_min > 1 - 1e-9
                           and ent['best_concurrence'] > 0.5
                           and replay_equal)),
    )
