#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bridge Explorer — интерактивный интерфейс v2.0 (пункт 9 плана).

Запуск:  streamlit run explorer/streamlit_app.py
Крутишь ручки затвора → видишь живой спектр и три проекции разрыва Г2
(ранговая r_H7, тепловая r_EF, GUE-класс) с позитивными контролями PC0'/PC0.
Данные вердиктов C9–C16 — из computations/*/data/results.json (кэш репо).
"""
import json, os, sys
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import streamlit as st  # noqa: E402

st.set_page_config(page_title="Hilbert–Pólya Bridge Explorer v2.0",
                   page_icon="∎", layout="wide")


@st.cache_data(show_spinner=False)
def load_verdicts():
    out = {}
    for c, key in (("C9_nonlocal_trace", "C9"),
                   ("C10_phase_coded", "C10"),
                   ("C11_alpha_third", "C11"),
                   ("C12_band_5000", "C12"),
                   ("C13_blind_families", "C13"),
                   ("C14_anomaly_hunt", "C14"),
                   ("C15_dirichlet", "C15"),
                   ("C16_qinfo", "C16")):
        p = os.path.join(ROOT, "computations", c, "data", "results.json")
        if os.path.exists(p):
            out[key] = json.load(open(p))
    return out


@st.cache_data(show_spinner=False)
def zeros():
    from hpbridge.zeros_mp import ensure_zeros
    return ensure_zeros(800)


V = load_verdicts()

st.title("Hilbert–Pólya Bridge · Explorer v2.0")
st.caption("«The Operator That Almost Exists» — живой инструмент поверх "
           "закоммиченных вердиктов C1–C16")

tab_live, tab_verdicts, tab_map = st.tabs(
    ["🔴 Живой затвор", "📊 Вердикты C9–C16", "🗺️ Карта моста"])

# ─────────────────────────── вкладка 1: живой затвор ───────────────────────
with tab_live:
    colL, colR = st.columns([1, 2])
    with colL:
        st.subheader("Ручки затвора")
        Nv = st.slider("Nv (вихри)", 0, 64, 16, step=2)
        q = st.select_slider("q (заряд)", [0.5, 1.0], value=1.0)
        W = st.slider("W (беспорядок)", 0.0, 1.0, 0.5, 0.1)
        alpha = st.select_slider("α (флакс)", [0.4, 0.5, 0.6], value=0.5)
        mass = st.slider("mass (стэггерд)", 0.0, 0.5, 0.0, 0.05)
        dalpha = st.slider("δα (сдвиг флакса)", -0.05, 0.05, 0.0, 0.01)
        phase_mode = st.selectbox("Фазовое кодирование (C10)",
                                  ["нет (протокол v1)",
                                   "β·ln p (жёсткая ко-локация)",
                                   "случайные фазы (контроль)"])
        beta = st.slider("β", 0.0, 0.5, 0.23, 0.01,
                         disabled=phase_mode != "β·ln p (жёсткая ко-локация)")
        run = st.button("▶ Пересчитать спектр", type="primary")

    with colR:
        if run or "last" not in st.session_state:
            with st.spinner("eigvalsh 576×576 + развёртка + метрики…"):
                from engine.solver import gate_spectrum
                from hpbridge.metrics_v2 import (ZeroReference, corr_shift,
                                                spacing_ratio_mean,
                                                ef_report2)
                from hpbridge import nonlocaltrace as nl
                from engine.hamiltonian import unfold_poly, central_band, \
                    window_u
                gamma = zeros()
                zref = ZeroReference(gamma, k0=224)
                handles = {}
                if mass:
                    handles["mass"] = mass
                if dalpha:
                    handles["dalpha"] = dalpha
                if phase_mode == "нет (протокол v1)":
                    w, mean_sp, ev = gate_spectrum(Nv, q, W, alpha, **handles)
                else:
                    from hpbridge.phasecoding import phase_coded_spectrum
                    mode = ("beta" if "жёсткая" in phase_mode else "random")
                    ev, phi, _ = phase_coded_spectrum(
                        24, Nv=Nv, q=q, alpha=alpha, W=W, mode=mode,
                        beta=beta)
                    cen = central_band(ev, 0.6)
                    w = window_u(unfold_poly(cen), 200)
                    mean_sp = float(np.mean(np.diff(cen)))
                r, s = corr_shift(w, zref.window)
                U = np.linspace(0.05, 1.0, 40)
                P = nl.prime_curve(U, nmax=1_000_000)
                rep = ef_report2(w, U, P)
                r_mean = spacing_ratio_mean(ev)
                st.session_state["last"] = dict(
                    r=r, s=s, r_ef=rep["r_fluct"], r_mean=r_mean,
                    w=w, ev=ev, mean_sp=mean_sp)
        d = st.session_state.get("last")
        if d:
            c1, c2, c3 = st.columns(3)
            c1.metric("r_H7 (ранговая)", f"{d['r']:+.3f}",
                      "нулевая зона" if abs(d["r"]) < 0.25 else "вне нуля!")
            c2.metric("r_EF (тепловая, fluct)", f"{d['r_ef']:+.3f}",
                      "нулевая зона" if abs(d["r_ef"]) < 0.8 else "вне нуля!")
            c3.metric("⟨r⟩ (класс)", f"{d['r_mean']:.3f}",
                      "GUE" if abs(d["r_mean"] - 0.5996) <= 0.03 else
                      ("GOE?" if abs(d["r_mean"] - 0.531) <= 0.03 else "—"))
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, 2, figsize=(9, 3.2),
                                     constrained_layout=True)
            axes[0].plot(d["w"], lw=1.0, color="#0E7C86")
            axes[0].set_title("Развёрнутое окно (200 уровней)", fontsize=10)
            axes[1].plot(U, rep["D"], lw=1.2, color="#C96F4A")
            axes[1].set_title("Флуктуация теплового следа D(u)", fontsize=10)
            for ax in axes:
                ax.grid(alpha=0.15)
            st.pyplot(fig)
            st.caption(f"PC0' (изоспектральный контроль) обязан давать "
                       f"r = 1.000 — см. C9. Средний зазор полосы: "
                       f"{d['mean_sp']:.4f}")

# ─────────────────────────── вкладка 2: вердикты ───────────────────────────
with tab_verdicts:
    st.subheader("Закоммиченные вердикты новых кампаний")
    for key in ("C9", "C10", "C11", "C12", "C13", "C14", "C15", "C16"):
        if key not in V:
            continue
        d = V[key]
        with st.expander(f"{key} — {d['meta'].get('campaign', '')}"):
            v = d.get("verdict", {})
            st.markdown(f"**RU:** {v.get('ru', '')}")
            st.markdown(f"**EN:** {v.get('en', '')}")
            meta = {k: v2 for k, v2 in d["meta"].items()
                    if k not in ("campaign",)}
            st.json(meta, expanded=False)

# ─────────────────────────── вкладка 3: карта ──────────────────────────────
with tab_map:
    st.subheader("Карта моста v2.0")
    rows = [
        ("C9 · нелокальный след", "T11", "r_H7 = 1.000; r_EF = 0.999 — "
         "примитив существует", "Г2 = стена ЛОКАЛЬНОСТИ"),
        ("C10 · фазовое кодирование", "T12", "ко-локация 4.4e-16, "
         "спектр слеп", "универсальность стирает кодировки"),
        ("C11 · α=1/3", "T13", "N₀ = 2L−6·[L≡0 mod 12], индекс −2",
         "первый мост «арифметика → спектр»"),
        ("C12 · полоса T=5000", "T14", "N = 4520 = 4520, S_max = 0.91",
         "RH верифицирована шире"),
        ("C13 · слепые семейства", "T15", "16 затворов, все в нуле, GUE",
         "разрыв устойчив к новым дизайнам"),
        ("C14 · поиск аномалий", "T16", "97 GUE / 18 интегрир. / 6 промежут.",
         "аттрактор глобален, бассейн структурирован"),
        ("C15 · Дирихле L", "T17", "|ΔK| ≤ 9.6e-6, скрученный вес",
         "разрыв Г2 УНИВЕРСАЛЕН"),
        ("C16 · квантовый слой", "T18", "локальность давит запутанность",
         "сложность стирает арифметику"),
    ]
    st.table({"кампания": [r[0] for r in rows],
              "теорема": [r[1] for r in rows],
              "число": [r[2] for r in rows],
              "смысл": [r[3] for r in rows]})
    st.info("Позитивные контроли: PC0' (изоспектральный близнец, r = 1.000), "
            "PC0 (окно нулей против гребёнки, r ≈ +0.999), PC1/PC2 (v1). "
            "Ни один отрицательный вердикт не публикуется без них.")
