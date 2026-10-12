#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_animations_v2.py — анимации v2.0 (GIF + MP4, ffmpeg).

anim_wavepacket — транспорт волнового пакета на ζ-облаке (C7-продолжение);
anim_coloc      — жёсткая ко-локация потока простых: β вращается, условие
                  (Φ_p,Φ_q) ≡ Φ_pq выполняется при любом β (T12).
Сохранение: figures/animations/ + копии в computations/.
"""
import os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

import figstyle  # noqa
import matplotlib.pyplot as plt  # noqa
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter  # noqa

OUT = os.path.join(ROOT, "figures", "animations")
os.makedirs(OUT, exist_ok=True)


def anim_wavepacket(t, L=48, n_frames=60, T_end=30.0):
    from engine.hamiltonian import random_vortex_configuration
    from hpbridge.blindfamilies import _protocol_H
    from scipy.linalg import eigh

    vrng = np.random.default_rng(96 + 3500)
    v = random_vortex_configuration(64, L, L, 1.0, vrng, "protocol")
    H = _protocol_H(L, v, 0.5, 0.0)
    ev, vec = eigh(H, check_finite=False)
    # пакет: гаусс по энергии в центре полосы
    e0 = np.median(ev)
    c0 = np.exp(-(ev - e0) ** 2 / (2 * 0.15 ** 2))
    c0 /= np.linalg.norm(c0)
    psi0 = vec @ c0

    ts = np.linspace(0, T_end, n_frames)
    phases = np.exp(-1j * np.outer(ts, ev))    # (frames, dim)
    probs = np.abs((phases * c0) @ vec.T) ** 2  # (frames, dim)
    probs = probs.reshape(n_frames, L, L)
    xx = np.arange(1, L + 1)
    mx = (probs.sum(axis=1) * xx).sum(axis=1) / probs.sum(axis=(1, 2))

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6),
                             constrained_layout=True)
    fig.patch.set_facecolor(t["bg"])

    def draw(k):
        for ax in axes:
            ax.clear()
        im = axes[0].imshow(probs[k], cmap="copper", origin="lower")
        axes[0].set_title(f"|psi(x,t)|^2, t = {ts[k]:.1f}", fontsize=11,
                          color=t["ink"])
        axes[0].set_xticks([]); axes[0].set_yticks([])
        axes[1].plot(ts[:k + 1], mx[:k + 1], color=t["line"], lw=1.6)
        axes[1].plot(ts[k], mx[k], "o", color=t["copper"], ms=7)
        axes[1].set_xlabel("t"); axes[1].set_ylabel("<x>(t)")
        axes[1].set_xlim(0, T_end); axes[1].set_ylim(0.25 * L, 0.75 * L)
        for ax in axes:
            figstyle.clean_axis(ax)
        return []

    anim = FuncAnimation(fig, draw, frames=list(range(n_frames)),
                         interval=90, blit=False, cache_frame_data=False)
    gif = os.path.join(OUT, "anim_wavepacket.gif")
    mp4 = os.path.join(OUT, "anim_wavepacket.mp4")
    anim.save(gif, writer=PillowWriter(fps=14), dpi=110)
    try:
        anim.save(mp4, writer=FFMpegWriter(fps=16, bitrate=2200), dpi=110)
    except Exception as e:
        print("  mp4 skipped:", e)
    plt.close(fig)
    return gif, mp4


def anim_coloc(t, n_frames=48):
    """Поток простых: узлы Φ_p = 2π{β ln p}; при любом β композит (p,q)
    несёт Φ_p+Φ_q ≡ Φ_pq — подсветка пар и композита."""
    from hpbridge.phasecoding import primes_upto, phase_system_beta
    primes = primes_upto(97)
    betas = np.linspace(0.0, 0.5, n_frames)
    P = primes[:12]

    fig, ax = plt.subplots(figsize=(7.6, 5.4), constrained_layout=True)
    fig.patch.set_facecolor(t["bg"])

    def draw(k):
        ax.clear()
        beta = betas[k]
        phi = phase_system_beta(primes, beta)
        pmap = {int(p): i for i, p in enumerate(primes)}
        xs = np.arange(len(P))
        ph = [phi[pmap[int(p)]] for p in P]
        sc = ax.scatter(xs, np.zeros_like(xs), c=ph, cmap="twilight",
                        s=340, vmin=0, vmax=2 * np.pi, edgecolors=t["ink"])
        for x, p, phv in zip(xs, P, ph):
            ax.text(x, 0.0, str(p), ha="center", va="center", fontsize=9,
                    color="white", weight="bold")
        # дуги: (p,q) → pq
        for i, p in enumerate(P[:7]):
            for j, q in enumerate(P[:7]):
                pq = int(p) * int(q)
                if pq in pmap and pq <= 97:
                    xp = pmap[pq]
                    ph_sum = np.mod(ph[i] + ph[j], 2 * np.pi)
                    ph_pq = phi[pmap[pq]]
                    d = abs(np.mod(ph_pq - ph_sum + np.pi, 2 * np.pi)
                            - np.pi)
                    ok = d < 1e-10
                    ax.plot([xs[i], xs[j], xp],
                            [0, 0.55 if j > i else -0.55, 0],
                            color=t["ok"] if ok else t["bad"],
                            lw=1.1, alpha=0.55)
        ax.text(0.02, 0.95, f"β = {beta:.3f}   "
                f"(Φ_p,Φ_q) ≡ Φ_pq  ✓ по построению (T12)",
                transform=ax.transAxes, fontsize=11, color=t["ink"])
        ax.set_ylim(-0.8, 1.05)
        ax.set_xlim(-0.7, len(P) - 0.3)
        ax.axis("off")
        return []

    anim = FuncAnimation(fig, draw, frames=list(range(n_frames)),
                         interval=110, cache_frame_data=False)
    gif = os.path.join(OUT, "anim_coloc.gif")
    mp4 = os.path.join(OUT, "anim_coloc.mp4")
    anim.save(gif, writer=PillowWriter(fps=12), dpi=110)
    try:
        anim.save(mp4, writer=FFMpegWriter(fps=14, bitrate=2000), dpi=110)
    except Exception as e:
        print("  mp4 skipped:", e)
    plt.close(fig)
    return gif, mp4


def main():
    t = figstyle.apply("light")
    import traceback
    try:
        fig, ax = plt.subplots(figsize=(7.6, 5.4), constrained_layout=True)
        # сухой прогон draw для выявления реальной ошибки
        import matplotlib.animation as manim
        class _Fake:
            pass
        # вызовем draw напрямую, повторив внутренности anim_coloc
    except Exception:
        traceback.print_exc()
    t0 = time.time()
    g, m = anim_coloc(t)
    print("anim_coloc:", g, m, f"({time.time()-t0:.0f}s)")
    t0 = time.time()
    g, m = anim_wavepacket(t, L=48, n_frames=56, T_end=26.0)
    print("anim_wavepacket:", g, m, f"({time.time()-t0:.0f}s)")
    # копии в кампании
    import shutil
    for src, camp in (("anim_coloc", "C10_phase_coded"),
                      ("anim_wavepacket", "C7_wave_dynamics")):
        for ext in (".gif", ".mp4"):
            p = os.path.join(OUT, src + ext)
            if os.path.exists(p):
                dst = os.path.join(ROOT, "computations", camp)
                shutil.copy(p, dst)
    print("animations done")


if __name__ == "__main__":
    main()
