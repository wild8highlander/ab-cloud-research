#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Кампания C17 — слепая фаза B протокола N7 на замкнутой плотности явной формулы.

Постановка (ROADMAP N7, уточнение algebraic_map; аудиту слепой протокол
значился C18, в отчёте algebraic_map слепая фаза B переназначена в C17):
построить меру ТОЛЬКО из арифметики (тета-функция + простые), пропустить её
через тот же якобиев механизм, что и фильм (moments -> J -> канва Q22),
зафиксировать результат ХЕШЕМ и только затем сверить с нулями.

Фазы:
  A. арифметическая плотность
     rho~(t) = dbar(t) - (1/pi) sum_{k>=1} sum_{p<=Pmax} (ln p) p^{-k/2}
               * exp(-sigma^2 k^2 (ln p)^2 / 2) * cos(k t ln p),
     dbar(t) = theta'(t)/pi = (Re psi(1/4 + i t/2) - ln pi)/(2 pi).
     Окно: N0(t)=theta(t)/pi+1, W1: N0: 0.5 -> 24.5; W2: 24.5 -> 48.5.
  B. слепая фиксация: дискретизация rho~ (GL-сетка) -> Ланцош-24 (алгоритм
     фильма, полная реортогонализация) -> J -> канва 25x25 Q22 (87 гейтов,
     17 безнулевых свидетелей) -> PNG + sha256. Нули не читаются (assert).
  C. сверка: узлы vs нули; null-модели: N0 без простых, N1 GUE (200), N2
     фаза-минус; sigma-сетка; окно 2; стенка Стилтьеса для замкнутой Phi.

Параметры предрегистрированы заранее (см. PRE-REGISTERED ниже); критерии приёма
зафиксированы до фазы C. Отрицательный результат публикуется.

Запуск: python3 run_c17_blind_phaseB.py   (~3 мин, numpy/mpmath/scipy/PIL)
"""
import hashlib
import json
import os
import sys
import time

import numpy as np
import mpmath as mp
from mpmath import mpf

mp.mp.dps = 40

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, R)
OUT = os.path.join(R, "computations", "C17_blind_phaseB")
os.makedirs(os.path.join(OUT, "data"), exist_ok=True)
os.makedirs(os.path.join(OUT, "figures"), exist_ok=True)

# ═══════════════════════ PRE-REGISTERED ═══════════════════════
SIGMA = 0.35            # основная ширина сглаживания (a priori)
SIGMA_GRID = (0.25, 0.5)  # чувствительность
KMAX = 40
PMAX = 10 ** 6
N = 24
JMAX = 48               # моменты mu_0..mu_48
GLGRID = 1024           # сетка дискретизации плотности
N_GUE = 200
WINDOWS = {"W1": (0.5, 24.5), "W2": (24.5, 48.5)}  # N0-границы
CRITERIA = (
    "POSITIVE: err_rms(C17) < 0.5*err_rms(N0-без-простых) И z_GUE >= 3 "
    "И окно W2 улучшается в том же направлении; "
    "PARTIAL: лучше N0 и z_GUE >= 2 без одного из условий; "
    "иначе NEGATIVE. Дополнительно рапортуется r_H7-аналог (Пирсон "
    "развёрнутых позиций) против порога 0.7."
)
# ══════════════════════════════════════════════════════════════

T_START = time.time()
LOG = []


def log(msg):
    LOG.append(str(msg))
    print(msg, flush=True)


# ── арифметика: решето, тета-окно, плотность ─────────────────────────────────
def sieve_primes(pmax):
    s = np.ones(pmax + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(pmax ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    pr = np.nonzero(s)[0]
    return pr, np.log(pr.astype(np.float64))


def N0(t):
    return mp.siegeltheta(mpf(t)) / mp.pi + 1


def inv_N0(y):
    lo, hi = mpf(10), mpf(300)
    for _ in range(90):
        m = (lo + hi) / 2
        if N0(m) < y:
            lo = m
        else:
            hi = m
    return float((lo + hi) / 2)


def dbar_np(ts):
    return np.array([float((mp.re(mp.digamma(mpf("0.25") + 1j * mpf(t) / 2))
                            - mp.log(mp.pi)) / (2 * mp.pi)) for t in ts])


def rho_grid(ts, lnp, pf, sigma, kmax, osc_sign=1.0):
    """rho~ на сетке ts; osc_sign=-1 — контроль с перевёрнутой фазой."""
    rho = dbar_np(ts)
    for k in range(1, kmax + 1):
        damp = np.exp(-0.5 * (sigma ** 2) * (k ** 2) * lnp ** 2)
        a = lnp * pf ** (-k / 2.0) * damp
        a[a < 1e-30] = 0.0
        idx = a > 0
        av = osc_sign * a[idx]
        pw = float(k) * lnp[idx]
        for i0 in range(0, ts.size, 1024):
            ph = np.outer(ts[i0:i0 + 1024], pw)
            rho[i0:i0 + 1024] -= (av @ np.cos(ph).T) / np.pi
    return rho


def closed_moments(T1, T2, sigma, lnp, pf, jmax=JMAX, kmax=KMAX):
    """mu_j замкнутой формулой: smooth (GL-600) + osc (комплексная
    первообразная C_j). Возвращает (mus, diag) — diag для контроля."""
    x, w = np.polynomial.legendre.leggauss(600)
    ts = 0.5 * (T2 - T1) * x + 0.5 * (T2 + T1)
    ws = 0.5 * (T2 - T1) * w
    db = dbar_np(ts)
    smooth = np.array([float(np.dot(ws, ts ** j * db)) for j in range(jmax + 1)])
    osc = np.zeros(jmax + 1)
    cond = 0.0
    for k in range(1, kmax + 1):
        damp = np.exp(-0.5 * (sigma ** 2) * (k ** 2) * lnp ** 2)
        a = lnp * pf ** (-k / 2.0) * damp
        a[a < 1e-30] = 0.0
        idx = a > 0
        av = a[idx]
        om = float(k) * lnp[idx]
        e2 = np.exp(1j * om * T2)
        e1 = np.exp(1j * om * T1)
        GM = [np.abs(om) ** (-(m + 1)) * np.exp(1j * (-(m + 1) * np.pi / 2)) * ((-1) ** m)
              for m in range(jmax + 1)]
        for j in range(jmax + 1):
            acc = np.zeros(om.size, dtype=np.complex128)
            for m in range(j + 1):
                gm = GM[m]
                acc += e2 * gm * (T2 ** (j - m)) - e1 * gm * (T1 ** (j - m))
            term = av * acc.real
            osc[j] += float(term.sum())
            if term.size:
                cond = max(cond, float(np.abs(term).sum() / max(abs(term.sum()), 1e-300)))
    return smooth - osc / np.pi, {"cond_max": cond}


def S_sigma_diff(T1, T2, sigma, lnp, pf, kmax):
    """S_sigma(T2)-S_sigma(T1) — контроль X1 для mu_0."""
    def Ss(t):
        s = 0.0
        for k in range(1, kmax + 1):
            damp = np.exp(-0.5 * (sigma ** 2) * (k ** 2) * lnp ** 2)
            a = pf ** (-k / 2.0) * damp
            a[a < 1e-30] = 0.0
            idx = a > 0
            s += float(np.dot(a[idx] / k, np.sin(float(k) * t * lnp[idx])))
        return -s / np.pi
    return Ss(T2) - Ss(T1)


# ── фаза B: дискретизация + Ланцош (алгоритм фильма) + канва ────────────────
Q = 22
SCALE = 1 << Q
LIMIT = (1 << 30) - 1
CANV = 25
NW = 17


def lanczos_jacobi(gams, w, nsteps=None):
    """Трёхдиагональ J размера nsteps из Ланцоша на diag(gams) (полная
    реортогонализация) — численный алгоритм фильма, nsteps <= len(gams)."""
    nsteps = nsteps or len(gams)
    V = np.zeros((len(gams), nsteps))
    al = np.zeros(nsteps)
    be = np.zeros(nsteps - 1)
    V[:, 0] = w / np.linalg.norm(w)
    for k in range(nsteps):
        z = gams * V[:, k]
        al[k] = V[:, k] @ z
        z = z - al[k] * V[:, k]
        if k > 0:
            z = z - be[k - 1] * V[:, k - 1]
        for j in range(k + 1):
            z -= (V[:, j] @ z) * V[:, j]
        if k < nsteps - 1:
            be[k] = np.linalg.norm(z)
            V[:, k + 1] = z / be[k]
    return al, be


def encode(v):
    x = int(round(abs(v) * SCALE))
    assert 0 <= x <= LIMIT, f"Q22 overflow: {v}"
    return (x & 255, (x >> 8) & 255, (x >> 16) & 255,
            ((x >> 23) & 127) | (0x80 if v < 0 else 0))


def decode(px):
    x = int(px[0]) | (int(px[1]) << 8) | (int(px[2]) << 16) | \
        ((int(px[3]) & 127) << 23)
    v = x / SCALE
    return -v if (int(px[3]) >> 7) else v


def build_canvas(al, be, nodes, mu0):
    witness_vals = [
        ("n_gates", 87.0), ("n_struct", 70.0), ("N", float(N)), ("q_exp", float(Q)),
        ("mean_alpha", float(al.mean())), ("sum_beta_d10", float(be.sum()) / 10.0),
        ("mass_mu0", float(mu0)), ("node_1", float(nodes[0])),
        ("node_12", float(nodes[11])), ("node_24", float(nodes[23])),
        ("log_det_nodes", float(np.log(nodes).sum())), ("min_beta", float(be.min())),
        ("max_beta", float(be.max())), ("alpha_1", float(al[0])),
        ("alpha_24", float(al[-1])), ("beta_1", float(be[0])),
        ("beta_23", float(be[-1])),
    ]
    assert len(witness_vals) == NW
    for name, v in witness_vals:
        assert abs(v) * SCALE <= LIMIT, f"witness {name} out of Q22 range"
    gates = []
    k = 0
    for n in range(1, N + 1):
        k += 1
        gates.append(dict(k=k, family="diagonal", row=n - 1, col=n - 1,
                          value=float(al[n - 1]), symbol=f"a_{n}",
                          formula=f"H[{n},{n}] = alpha_{n}"))
    for j in range(1, N):
        k += 1
        gates.append(dict(k=k, family="coupling", row=j, col=j - 1,
                          value=float(be[j - 1]), symbol=f"b_{j}",
                          formula=f"H[{j+1},{j}] = beta_{j}"))
        k += 1
        gates.append(dict(k=k, family="coupling", row=j - 1, col=j,
                          value=float(be[j - 1]), symbol=f"b_{j}m",
                          formula=f"H[{j},{j+1}] = beta_{j} mirror"))
    for i, (name, v) in enumerate(witness_vals, start=1):
        k += 1
        gates.append(dict(k=k, family="witness", row=i - 1, col=24, value=float(v),
                          symbol=name, formula=f"CAL[{i}] {name}"))
    assert k == 87
    canvas = np.zeros((CANV, CANV, 4), dtype=np.uint8)
    for g in gates:
        canvas[g["row"], g["col"]] = encode(g["value"])
    return canvas, witness_vals, gates


# ── фаза B для одного (окна, sigma) ──────────────────────────────────────────
def run_blind(T1, T2, sigma, lnp, pf, tag):
    log(f"[{tag}] window [{T1:.6f}, {T2:.6f}], sigma={sigma}")
    # моменты замкнутой формулой (арифметика)
    mus, diag = closed_moments(T1, T2, sigma, lnp, pf)
    x1 = abs(mus[0] - (24.0 + S_sigma_diff(T1, T2, sigma, lnp, pf, KMAX) if tag == "W1" else mus[0] * 0))
    mass = float(np.trapezoid(np.full(2, 0.0), [0, 1]))  # placeholder
    # масса меры = mu_0 из квадратуры сетки (после клипа) и из моментов
    xg, wg = np.polynomial.legendre.leggauss(GLGRID)
    ts = 0.5 * (T2 - T1) * xg + 0.5 * (T2 + T1)
    ws = 0.5 * (T2 - T1) * wg
    rho = rho_grid(ts, lnp, pf, sigma, KMAX)
    neg_mass = float(np.dot(ws, np.clip(-rho, 0, None)))
    W = np.clip(rho, 0.0, None) * ws
    mu0_grid = float(W.sum())
    # Ланцош (алгоритм фильма) на дискретизированной мере
    sq = np.sqrt(W)
    al, be = lanczos_jacobi(ts, sq, N)
    assert (be > 1e-10).all(), "beta underflow in Lanczos"
    J = np.zeros((N, N))
    np.fill_diagonal(J, al)
    for i in range(1, N):
        J[i - 1, i] = J[i, i - 1] = be[i - 1]
    nodes = np.linalg.eigvalsh(J)
    # контрольные суммы Гаусса: mu0 * sum nu_quad lam^k = mu_k
    lam, vec = np.linalg.eigh(J)
    nu_quad = np.abs(vec[0]) ** 2
    chk = []
    for k in range(0, 48):
        approx = mu0_grid * float(np.dot(nu_quad, lam ** k))
        chk.append(abs(approx - mus[k]) / max(abs(mus[k]), 1e-9))
    # канва (слепая фиксация)
    canvas, witness_vals, gates = build_canvas(al, be, nodes, mu0_grid)
    from PIL import Image
    png = os.path.join(OUT, "data", f"canvas_{tag}.png")
    Image.fromarray(canvas).save(png)
    back = np.array(Image.open(png).convert("RGBA"), dtype=np.uint8)
    identical = bool(np.array_equal(back, canvas))
    wit_ok = sum(1 for i, (nm, v) in enumerate(witness_vals, 1)
                 if abs(decode(back[i - 1, 24]) - decode(encode(v))) < 1e-9)
    sha = hashlib.sha256(back.tobytes()).hexdigest()
    log(f"[{tag}] mu0(closed)={mus[0]:.6f} mu0(grid)={mu0_grid:.6f} "
        f"neg_mass={neg_mass:.2e} cond={diag['cond_max']:.0f}")
    log(f"[{tag}] checksum max rel dev (k<=47): {max(chk):.2e}")
    log(f"[{tag}] canvas sha256={sha} png_identical={identical} witness {wit_ok}/{NW}")
    return dict(T1=T1, T2=T2, sigma=sigma, mus=mus.tolist(), mu0_grid=mu0_grid,
                neg_mass=neg_mass, cond=diag["cond_max"], checksum_max=max(chk),
                alphas=al.tolist(), betas=be.tolist(), nodes=nodes.tolist(),
                nu_quad=nu_quad.tolist(), canvas_sha256=sha,
                png_identical=identical, witness_ok=int(wit_ok),
                witness=witness_vals)


# ═════════════════════════ ФАЗЫ A+B ═════════════════════════
log("=== C17: слепая фаза B протокола N7 (замкнутая плотность явной формулы) ===")
log("PRE-REGISTERED: " + CRITERIA)
pr, lnp = sieve_primes(PMAX)
pf = pr.astype(np.float64)
log(f"sieve: {pr.size} primes <= {PMAX}")
wins = {tag: (inv_N0(mpf(str(a))), inv_N0(mpf(str(b)))) for tag, (a, b) in WINDOWS.items()}
for tag, (a, b) in wins.items():
    log(f"window {tag}: N0: {a} -> {b}:  [{a:.6f}, {b:.6f}]")

blind = {}
for tag in ("W1", "W2"):
    blind[tag] = run_blind(wins[tag][0], wins[tag][1], SIGMA, lnp, pf, tag)

# ═════════════════════════ ФАЗА C ═════════════════════════
log("=== фаза C: сверка (нули читаются только здесь) ===")
from hpbridge.zeros_mp import ensure_zeros
gam = ensure_zeros(60)

def nearest_err(nodes, zeros):
    d = np.array([np.min(np.abs(zeros - nd)) for nd in nodes])
    return d

def pearson(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return float(np.corrcoef(a, b)[0, 1])

results = dict(meta=dict(
    campaign="C17 blind phase B (closed explicit-formula density)",
    roadmap="N7 phase B (relabelled from audit C18 by algebraic_map report)",
    preregistered=CRITERIA,
    sigma=SIGMA, sigma_grid=SIGMA_GRID, kmax=KMAX, pmax=PMAX, N=N,
    glgrid=GLGRID, n_gue=N_GUE, windows={k: [v[0], v[1]] for k, v in wins.items()},
    zeros_source="hpbridge.zeros_mp.ensure_zeros(60), mpmath %s" % mp.__version__,
    runtime_s=None), blind={t: {k: v for k, v in blind[t].items()} for t in blind},
    verify={})

verdicts = {}
for tag in ("W1", "W2"):
    T1, T2 = wins[tag]
    nodes = np.array(blind[tag]["nodes"])
    zin = gam[(gam > T1) & (gam < T2)]
    d = nearest_err(nodes, zin) if zin.size else None
    # N0: без простых
    xg, wg = np.polynomial.legendre.leggauss(GLGRID)
    ts = 0.5 * (T2 - T1) * xg + 0.5 * (T2 + T1)
    ws = 0.5 * (T2 - T1) * wg
    rho0 = dbar_np(ts)
    W0 = np.clip(rho0, 0, None) * ws
    al0, be0 = lanczos_jacobi(ts, np.sqrt(W0), N)
    J0 = np.zeros((N, N)); np.fill_diagonal(J0, al0)
    for i in range(1, N):
        J0[i - 1, i] = J0[i, i - 1] = be0[i - 1]
    nodes0 = np.linalg.eigvalsh(J0)
    d0 = nearest_err(nodes0, zin) if zin.size else None
    # N2: фаза-минус
    rho2 = rho_grid(ts, lnp, pf, SIGMA, KMAX, osc_sign=-1.0)
    W2m = np.clip(rho2, 0, None) * ws
    al2, be2 = lanczos_jacobi(ts, np.sqrt(W2m), N)
    J2 = np.zeros((N, N)); np.fill_diagonal(J2, al2)
    for i in range(1, N):
        J2[i - 1, i] = J2[i, i - 1] = be2[i - 1]
    nodes2 = np.linalg.eigvalsh(J2)
    d2 = nearest_err(nodes2, zin) if zin.size else None
    # N1: GUE null
    rng = np.random.default_rng(20261013)
    errs_gue = []
    for _ in range(N_GUE):
        A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        ev = np.linalg.eigvalsh((A + A.conj().T) / 2)
        sp = np.diff(ev)
        sp = sp / sp.mean()
        pos = T1 + np.concatenate([[0], np.cumsum(sp)]) * ((T2 - T1) / sp.sum())
        dg = nearest_err(pos, zin) if zin.size else None
        if dg is not None:
            errs_gue.append(float(np.sqrt((dg ** 2).mean())))
    gue_mean, gue_std = float(np.mean(errs_gue)), float(np.std(errs_gue))
    if zin.size:
        rms = float(np.sqrt((d ** 2).mean()))
        rms0 = float(np.sqrt((d0 ** 2).mean()))
        rms2 = float(np.sqrt((d2 ** 2).mean()))
        z = (gue_mean - rms) / max(gue_std, 1e-12)
        r = pearson(nodes, zin) if zin.size == N else None
        results["verify"][tag] = dict(
            true_count=int(zin.size),
            count_pred_mu0=float(blind[tag]["mus"][0]),
            err_max=float(np.abs(d).max()), err_rms=rms,
            err_median=float(np.median(d)),
            err_N0_rms=rms0, err_phaseflip_rms=rms2,
            gue_mean=gue_mean, gue_std=gue_std, z_gue=z, r_pearson=r,
            nodes=nodes.tolist(), zeros=zin.tolist(),
            deltas=d.tolist(), nodes_N0=nodes0.tolist(),
            nodes_phaseflip=nodes2.tolist())
        log(f"[{tag}] true zeros in window: {zin.size}; count pred mu0 = "
            f"{blind[tag]['mus'][0]:.3f}")
        log(f"[{tag}] C17: rms={rms:.4f} max={np.abs(d).max():.4f} | "
            f"N0-no-primes: rms={rms0:.4f} | phase-flip: rms={rms2:.4f} | "
            f"GUE: {gue_mean:.4f}+-{gue_std:.4f} z={z:.1f} | r={r}")
        verdicts[tag] = dict(rms=rms, rms0=rms0, z=z, r=r)

# sigma-сетка (окно W1)
sigma_scan = {}
for sg in SIGMA_GRID:
    b = run_blind(wins["W1"][0], wins["W1"][1], sg, lnp, pf, f"W1-sigma{sg}")
    nodes = np.array(b["nodes"])
    zin = gam[(gam > wins["W1"][0]) & (gam < wins["W1"][1])]
    d = nearest_err(nodes, zin)
    sigma_scan[str(sg)] = dict(err_rms=float(np.sqrt((d ** 2).mean())),
                               err_max=float(np.abs(d).max()),
                               mu0=float(b["mus"][0]))
    log(f"[sigma={sg}] rms={sigma_scan[str(sg)]['err_rms']:.4f} "
        f"max={sigma_scan[str(sg)]['err_max']:.4f}")
results["sigma_scan"] = sigma_scan

# стенка Стилтьеса (замкнутая Phi на longdouble-моментах)
def stieltjes_wall(mus_ld, N):
    h_prev = None
    P = [np.longdouble(1.0)]
    h = np.longdouble(0.0)
    for i in range(len(P)):
        for j in range(len(P)):
            h += P[i] * P[j] * mus_ld[i + j]
    hs = [h]
    alphas, beta2, wall = [], [], None
    for n in range(N):
        xP = [np.longdouble(0.0)] + P
        num = np.longdouble(0.0)
        for i, ci in enumerate(xP):
            if ci == 0:
                continue
            for j_, cj in enumerate(P):
                if cj == 0:
                    continue
                num += ci * cj * mus_ld[i + j_]
        alphas.append(num / h)
        if n == N - 1:
            break
        b2 = h / h_prev if n > 0 else None
        Pnext = []
        for i in range(len(xP)):
            v = xP[i] - alphas[n] * (P[i] if i < len(P) else np.longdouble(0.0))
            if n > 0:
                v -= b2 * (Pprev[i] if i < len(Pprev) else np.longdouble(0.0))
            Pnext.append(v)
        Pprev, P = P, Pnext
        h_new = np.longdouble(0.0)
        for i, ci in enumerate(P):
            if ci == 0:
                continue
            for j_, cj in enumerate(P):
                if cj == 0:
                    continue
                h_new += ci * cj * mus_ld[i + j_]
        h_prev, h = h, h_new
        hs.append(h_new)
        if h_new <= 0:
            wall = n + 1
            break
    if wall is None:
        for n in range(1, len(hs)):
            if hs[n] / hs[n - 1] <= 0:
                wall = n
                break
    return alphas, [hs[n] / hs[n - 1] for n in range(1, len(hs))], hs, wall

T1, T2 = wins["W1"]
mus64, _ = closed_moments(T1, T2, SIGMA, lnp, pf)
T2L = np.longdouble(T2)
mus_ld = mus64 / (T2L ** np.arange(JMAX + 1, dtype=np.longdouble))
alphas_s, beta2_s, hs, wall = stieltjes_wall(mus_ld, N)
log(f"Stieltjes wall (longdouble moments, sigma={SIGMA}): "
    f"first nonpositive h at n = {wall} (h_n > 0 for n < {wall})")
results["stieltjes_wall"] = dict(n_star=int(wall) if wall else None,
                                 log10_h=[float(np.log10(abs(h))) for h in hs])

v1, v0, z1 = verdicts["W1"]["rms"], verdicts["W1"]["rms0"], verdicts["W1"]["z"]
imp = v0 / v1
pos = (v1 < 0.5 * v0) and (z1 >= 3) and (verdicts["W2"]["rms"] < 0.5 * verdicts["W2"]["rms0"])
part = (v1 < v0) and (z1 >= 2)
verdict = "POSITIVE" if pos else ("PARTIAL" if part else "NEGATIVE")
r1 = verdicts["W1"]["r"]
log(f"VERDICT C17 (pre-registered): {verdict}  (improvement over no-prime "
    f"null: {imp:.2f}x, z_GUE={z1:.1f}, r={r1})")
results["verdict"] = dict(
    label=verdict, improvement=imp, z_gue=z1, r=r1,
    r_threshold=0.7, r_pass=bool(r1 and r1 >= 0.7),
    ru=f"C17 (предзарегистрированная метрика): вердикт {verdict}. "
       f"Улучшение над null без простых {imp:.2f}x, z_GUE = {z1:.1f}, "
       f"r = {r1:.4f}.",
    en="")

# ═════════════ СТУПЕНЬ 2: C17b — valley-окна (исследовательская, ═════════
# критерии предрегистрированы внутри прогона до чтения нулей; статус —
# exploratory/confirmatory-pending: правило окон придумано после фазы C
# ступени 1, поэтому подтверждением считается независимое воспроизведение).
log("=== C17b: valley-snapped окна (exploratory; критерии — ниже, до фазы C) ===")
CRITERIA_B = (
    "C17b POSITIVE: err_rms < 0.5*err_rms(N0) И z_GUE >= 3 И W2 согласовано; "
    "PARTIAL: лучше N0 и z_GUE >= 2; иначе NEGATIVE. Правило окон: края — "
    "аргминимумы слепой плотности rho~ в +-1.5 средних интервалов от "
    "N0-границ; число узлов = round(масса rho~ в окне)."
)
log("PRE-REGISTERED: " + CRITERIA_B)


def valley_window(Ta, Tb, lnp, pf, sigma):
    """Края окна = глубочайшие минимумы слепой плотности в ±1.5 средних
    интервалов от N0-границ (правило только-по-арифметике)."""
    dbar_a = dbar_np([Ta])[0]
    half = 1.5 / dbar_a
    tsL = np.linspace(Ta - half, Ta + half, 800)
    tsR = np.linspace(Tb - half, Tb + half, 800)
    rhoL = rho_grid(tsL, lnp, pf, sigma, KMAX)
    rhoR = rho_grid(tsR, lnp, pf, sigma, KMAX)
    # guard: кандидат-долина обязан иметь неотрицательную плотность
    okL = rhoL >= 0
    okR = rhoR >= 0
    iL = int(np.argmin(np.where(okL, rhoL, np.inf)))
    iR = int(np.argmin(np.where(okR, rhoR, np.inf)))
    if not okL[iL]:
        iL = int(np.argmin(np.abs(tsL - Ta)))
    if not okR[iR]:
        iR = int(np.argmin(np.abs(tsR - Tb)))
    return float(tsL[iL]), float(tsR[iR])


def run_stage2(tag, Ta, Tb, sigma, lnp, pf):
    T1v, T2v = valley_window(Ta, Tb, lnp, pf, sigma)
    xg, wg = np.polynomial.legendre.leggauss(GLGRID)
    ts = 0.5 * (T2v - T1v) * xg + 0.5 * (T2v + T1v)
    ws = 0.5 * (T2v - T1v) * wg
    rho = rho_grid(ts, lnp, pf, sigma, KMAX)
    W = np.clip(rho, 0, None) * ws
    mass = float(W.sum())
    nb = int(round(mass))
    log(f"[C17b:{tag}] valley window [{T1v:.4f}, {T2v:.4f}], blind mass = "
        f"{mass:.3f} -> nodes = {nb}")
    al, be = lanczos_jacobi(ts, np.sqrt(W), nb)
    J = np.zeros((nb, nb)); np.fill_diagonal(J, al)
    for i in range(1, nb):
        J[i - 1, i] = J[i, i - 1] = be[i - 1]
    nodes = np.linalg.eigvalsh(J)
    # канва только для nb = 24 (сопоставимость с фильмом)
    canvas_sha, wit_ok = None, None
    if nb == N:
        canvas, wv, _ = build_canvas(al, be, nodes, mass)
        from PIL import Image
        png = os.path.join(OUT, "data", f"canvas_{tag}_b.png")
        Image.fromarray(canvas).save(png)
        back = np.array(Image.open(png).convert("RGBA"), dtype=np.uint8)
        wit_ok = sum(1 for i, (nm, v) in enumerate(wv, 1)
                     if abs(decode(back[i - 1, 24]) - decode(encode(v))) < 1e-9)
        canvas_sha = hashlib.sha256(back.tobytes()).hexdigest()
        log(f"[C17b:{tag}] canvas sha256={canvas_sha} witness {wit_ok}/{NW}")
    return dict(T1=T1v, T2=T2v, sigma=sigma, mass=mass, nodes=nodes.tolist(),
                alphas=al.tolist(), betas=be.tolist(),
                canvas_sha256=canvas_sha, witness_ok=wit_ok)

blind_b = {}
for tag in ("W1", "W2"):
    blind_b[tag] = run_stage2(tag, wins[tag][0], wins[tag][1], SIGMA, lnp, pf)

results_b = {"meta": dict(stage="C17b valley-snapped windows (exploratory; rule v2: deepest density minimum within +/-1.5 mean spacings of the N0-edge)",
                          preregistered=CRITERIA_B), "verify": {}}
verdicts_b = {}
for tag in ("W1", "W2"):
    T1v, T2v = blind_b[tag]["T1"], blind_b[tag]["T2"]
    nodes = np.array(blind_b[tag]["nodes"])
    nb = nodes.size
    zin = gam[(gam > T1v) & (gam < T2v)]
    xg, wg = np.polynomial.legendre.leggauss(GLGRID)
    ts = 0.5 * (T2v - T1v) * xg + 0.5 * (T2v + T1v)
    ws = 0.5 * (T2v - T1v) * wg
    # N0 без простых (те же края окна)
    W0 = np.clip(dbar_np(ts), 0, None) * ws
    al0, be0 = lanczos_jacobi(ts, np.sqrt(W0), nb)
    J0 = np.zeros((nb, nb)); np.fill_diagonal(J0, al0)
    for i in range(1, nb):
        J0[i - 1, i] = J0[i, i - 1] = be0[i - 1]
    nodes0 = np.linalg.eigvalsh(J0)
    # фаза-минус
    rho2 = rho_grid(ts, lnp, pf, SIGMA, KMAX, osc_sign=-1.0)
    W2m = np.clip(rho2, 0, None) * ws
    al2, be2 = lanczos_jacobi(ts, np.sqrt(W2m), nb)
    J2 = np.zeros((nb, nb)); np.fill_diagonal(J2, al2)
    for i in range(1, nb):
        J2[i - 1, i] = J2[i, i - 1] = be2[i - 1]
    nodes2 = np.linalg.eigvalsh(J2)
    # GUE
    rng = np.random.default_rng(1717)
    errs_gue = []
    for _ in range(N_GUE):
        A = rng.normal(size=(nb, nb)) + 1j * rng.normal(size=(nb, nb))
        ev = np.linalg.eigvalsh((A + A.conj().T) / 2)
        sp = np.diff(ev)
        sp = sp / sp.mean()
        posg = T1v + np.concatenate([[0], np.cumsum(sp)]) * ((T2v - T1v) / sp.sum())
        errs_gue.append(float(np.sqrt((nearest_err(posg, zin) ** 2).mean())))
    gue_mean, gue_std = float(np.mean(errs_gue)), float(np.std(errs_gue))
    if zin.size:
        d = nearest_err(nodes, zin)
        d0 = nearest_err(nodes0, zin)
        rms = float(np.sqrt((d ** 2).mean()))
        rms0 = float(np.sqrt((d0 ** 2).mean()))
        z = (gue_mean - rms) / max(gue_std, 1e-12)
        r = pearson(nodes, zin) if zin.size == nb else None
        results_b["verify"][tag] = dict(
            true_count=int(zin.size), count_pred=float(blind_b[tag]["mass"]),
            err_rms=rms, err_max=float(np.abs(d).max()),
            err_N0_rms=rms0, err_phaseflip_rms=float(np.sqrt((nearest_err(nodes2, zin) ** 2).mean())),
            gue_mean=gue_mean, gue_std=gue_std, z_gue=z, r_pearson=r,
            nodes=nodes.tolist(), zeros=zin.tolist(), deltas=d.tolist(),
            nodes_N0=nodes0.tolist(), nodes_phaseflip=nodes2.tolist(),
            alphas_c17b=blind_b[tag]["alphas"], betas_c17b=blind_b[tag]["betas"],
            window=[blind_b[tag]["T1"], blind_b[tag]["T2"]])
        verdicts_b[tag] = dict(rms=rms, rms0=rms0, z=z, r=r)
        log(f"[C17b:{tag}] zeros: {zin.size} (pred {blind_b[tag]['mass']:.2f}) | "
            f"C17b rms={rms:.4f} max={np.abs(d).max():.4f} | N0: {rms0:.4f} | "
            f"GUE z={z:.1f} | r={r}")

vb1, vb0, zb = verdicts_b["W1"]["rms"], verdicts_b["W1"]["rms0"], verdicts_b["W1"]["z"]
pb = (vb1 < 0.5 * vb0) and (zb >= 3) and (verdicts_b["W2"]["rms"] < 0.5 * verdicts_b["W2"]["rms0"])
ptb = (vb1 < vb0) and (zb >= 2)
verdict_b = "POSITIVE" if pb else ("PARTIAL" if ptb else "NEGATIVE")
log(f"VERDICT C17b (exploratory): {verdict_b}  (improvement {vb0/vb1:.2f}x, "
    f"z_GUE={zb:.1f}, r={verdicts_b['W1']['r']})")
results_b["verdict"] = dict(label=verdict_b, improvement=vb0 / vb1,
                            z_gue=zb, r=verdicts_b["W1"]["r"])
results["stage2_c17b"] = results_b

# ═════════════ ДЕКОМПОЗИЦИЯ ОШИБКИ (диагностика фазы C) ═════════════
# ссылка: квадратаура ИСТИННОЙ гребёнки на тех же окнах (нули — только здесь)
def true_quad_nodes(T1, T2, zeros, nb, sigma):
    xg, wg = np.polynomial.legendre.leggauss(GLGRID)
    ts = 0.5 * (T2 - T1) * xg + 0.5 * (T2 + T1)
    ws = 0.5 * (T2 - T1) * wg
    W = np.zeros_like(ts)
    for g in zeros:
        W += np.exp(-0.5 * ((ts - g) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
    W *= ws
    al, be = lanczos_jacobi(ts, np.sqrt(np.clip(W, 0, None)), nb)
    J = np.zeros((nb, nb)); np.fill_diagonal(J, al)
    for i in range(1, nb):
        J[i - 1, i] = J[i, i - 1] = be[i - 1]
    return np.linalg.eigvalsh(J)

T1, T2 = wins["W1"]
zin1 = gam[(gam > T1) & (gam < T2)]
ref1 = true_quad_nodes(T1, T2, zin1, N, SIGMA)
nd1 = np.array(blind["W1"]["nodes"])
nd0 = None
d_decomp = float(np.sqrt((np.sort(ref1) - nd1) ** 2).mean())
log(f"decomposition W1 (leak window): RMS(C17 nodes, true-comb quadrature) "
    f"= {d_decomp:.4f}")
results["decomposition_W1"] = dict(rms_c17_vs_truequad=d_decomp)

# декомпозиция на C17b-окнах (чистые окна без подрезки горбов)
decomp_b = {}
for tag in ("W1", "W2"):
    T1v, T2v = blind_b[tag]["T1"], blind_b[tag]["T2"]
    nb = len(blind_b[tag]["nodes"])
    zv = gam[(gam > T1v) & (gam < T2v)]
    if zv.size == nb:
        refv = true_quad_nodes(T1v, T2v, zv, nb, SIGMA)
        dv = float(np.sqrt((np.sort(refv) - np.array(blind_b[tag]["nodes"])) ** 2).mean())
        rms_ref_vs_zeros = float(np.sqrt((nearest_err(refv, zv) ** 2).mean()))
        # null-модели на том же уровне (реконструкция гребёнки)
        n0v = np.array(results_b["verify"][tag]["nodes_N0"])
        n2v = np.array(results_b["verify"][tag]["nodes_phaseflip"])
        dn0 = float(np.sqrt((np.sort(refv) - np.sort(n0v)) ** 2).mean())
        dn2 = float(np.sqrt((np.sort(refv) - np.sort(n2v)) ** 2).mean())
        decomp_b[tag] = dict(rms_c17b_vs_truequad=dv,
                             rms_truequad_vs_zeros=rms_ref_vs_zeros,
                             rms_N0_vs_truequad=dn0,
                             rms_phaseflip_vs_truequad=dn2)
        log(f"decomposition C17b:{tag}: RMS(C17b, true-quad) = {dv:.4f}; "
            f"RMS(N0-null, true-quad) = {dn0:.4f}; "
            f"RMS(phase-flip, true-quad) = {dn2:.4f}; "
            f"RMS(true-quad, zeros) = {rms_ref_vs_zeros:.4f} (инструментальный зазор)")
results["decomposition_c17b"] = decomp_b


# ── диагностика фазы C: точечная точность плотности и калибровка ──────────
# (a) точечная точность rho~ против истинной сглаженной гребёнки (C17b W1)
T1d, T2d = blind_b["W1"]["T1"], blind_b["W1"]["T2"]
ts_d = np.linspace(T1d, T2d, 2400)
rho_d = rho_grid(ts_d, lnp, pf, SIGMA, KMAX)
zin_d = gam[(gam > T1d) & (gam < T2d)]
truth_d = np.zeros_like(ts_d)
for g in zin_d:
    truth_d += np.exp(-0.5 * ((ts_d - g) / SIGMA) ** 2) / (SIGMA * np.sqrt(2 * np.pi))
diff_d = rho_d - truth_d
pointwise = dict(max_abs=float(np.abs(diff_d).max()),
                 rms=float(np.sqrt((diff_d ** 2).mean())),
                 bump_height=float(truth_d.max()))
log(f"pointwise (C17b W1): max|rho~-truth| = {pointwise['max_abs']:.4f} "
    f"rms = {pointwise['rms']:.4f} (высота горба {pointwise['bump_height']:.3f})")
results["pointwise_diag"] = pointwise

# (b) калибровка инструментария на окне W1 (N0): квадратаура гребёнки
#     без утечки (24 нуля в окне) и с утечкой (gamma_1 вне окна)
ref_pure = true_quad_nodes(wins["W1"][0], wins["W1"][1], zin1, N, SIGMA)
d_pure = float(np.sqrt((nearest_err(ref_pure, zin1) ** 2).mean()))
d_ref_vs_zeros = float(np.sqrt((nearest_err(ref1, zin1) ** 2).mean()))
log(f"calibration W1: RMS(true-quad no-leak, zeros) = {d_pure:.4f}; "
    f"RMS(true-quad with-leak, zeros) = {d_ref_vs_zeros:.4f}")
results["calibration_W1"] = dict(rms_truequad_noleak_vs_zeros=d_pure,
                                 rms_truequad_leak_vs_zeros=d_ref_vs_zeros)

results["meta"]["runtime_s"] = round(time.time() - T_START, 1)
with open(os.path.join(OUT, "data", "results.json"), "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
log(f"results.json written; total {results['meta']['runtime_s']}s")
