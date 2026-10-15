#!/usr/bin/env python3
"""Кампания C9 — нелокальный след как новый примитив (R1, теорема T11).

Вопрос: существует ли оператор, у которого вес простых Λ(n)/√n в тепловом
следе есть ПО КОНСТРУКЦИИ (прямо из Гуинана–Вейля, не через решётку) — и
сдвигает ли это r_EF из нулевого облака затворов?

Семейство (все спектры — положительные ветви, протокол T6):
  N1  H_ξ: ev = γ_1..γ_400                — позитивный контроль (PC0'/PC0);
  N2  DCT-близнец O·diag(γ)·Oᵀ            — изоспектрален, ядро плотное;
  N3  QR-близнец  O·diag(γ)·Oᵀ            — изоспектрален, хаос-зерно;
  N4  Berry–Keating xp (обрезанный)       — кандидат «вне решётки»;
  N5  LCM-ядро Λ(lcm(m,n))/√mn            — простой вес в самом ядре.

v2-конвенция метрик: развёрнутое окно объекта против развёрнутого нулевого
окна (один конвейер; PC0' обязан давать r_H7 = 1). Тепловая метрика r_EF —
на развёрнутом окне против простой гребёнки P(u) (v1-протокол C4/M2, PC0).
"""
import json, os, sys, time
import numpy as np

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, R)

from hpbridge.zeros_mp import ensure_zeros
from hpbridge import nonlocaltrace as nl
from hpbridge.metrics_v2 import (ZeroReference, corr_shift, null_pvalue,
                                gue_null_stats, gue_class_verdict)
from engine.hamiltonian import unfold_poly, central_band, window_u
from hpbridge.traceformula import heat_trace_fluct
from hpbridge.metrics_v2 import ef_report2, ef_fluct_corr


def unfolded_window(evs, frac=0.6, k_win=200):
    cen = central_band(np.asarray(evs, dtype=float), frac)
    u = unfold_poly(cen)
    kw = min(k_win, u.size - 12)
    return window_u(u, kw)


def main():
    t0 = time.time()
    gamma = ensure_zeros(800)
    zref = ZeroReference(gamma, k0=224)          # конвенция v1 (γ₀≈500.3)
    zmatch = ZeroReference(gamma, k0=80)         # окно объекта γ_81..γ_320
    g_mean, g_std = gue_null_stats(zref, n_gue=40)

    U = np.linspace(0.05, 1.0, 40)               # v1-сетка C4/M2
    P = nl.prime_curve(U, nmax=1_000_000)

    results = {}

    # ── N1: H_ξ (позитивная ветвь γ_1..γ_400) ──
    ev_xi = gamma[:400].copy()
    H_tw, _ = nl.ispectral_twin(ev_xi, kind="dct")
    ev_tw = np.sort(np.linalg.eigvalsh(H_tw))
    ispec_dev = float(np.abs(ev_tw - ev_xi).max())
    w_xi = unfolded_window(ev_xi)
    r_pc, s_pc = corr_shift(w_xi, zmatch.window)
    rep_xi = ef_report2(w_xi, U, P)
    D_xi = rep_xi["D"]
    tf = nl.trace_formula_check(gamma, xs=[0.15, 0.25, 0.35, 0.5])
    bmc = nl.b_minus_c0_check(gamma)
    results["N1_Hxi"] = {
        "r_H7_matched": r_pc, "shift": s_pc,
        "r_EF": rep_xi, "trace_check": tf, "B_plus_C0_abs": bmc[0],
        "class": "ispectral by construction (PC0'/PC0)",
    }

    # ── N2/N3: изоспектральные нелокальные близнецы ──
    for kind, key in (("dct", "N2_DCT_twin"), ("qr", "N3_QR_twin")):
        H, O = nl.ispectral_twin(ev_xi, kind=kind)
        ev = np.sort(np.linalg.eigvalsh(H))
        w = unfolded_window(ev)
        r, s = corr_shift(w, zmatch.window)
        rep = ef_report2(w, U, P)
        results[key] = {
            "r_H7_matched": r, "shift": s, "r_EF": rep,
            "density": float(np.mean(np.abs(H) > 1e-12)),
            "ispectral_dev": ispec_dev,
            "class": "ispectral nonlocal (dense orthogonal conjugation)",
        }

    # ── N4: Berry–Keating xp ──
    H_bk = nl.berry_keating(576)
    ev_bk_full = np.sort(np.linalg.eigvalsh(H_bk))
    ev_bk = ev_bk_full[ev_bk_full > 0]
    w_bk = unfolded_window(ev_bk)
    r_bk, s_bk = corr_shift(w_bk, zref.window)
    rep_bk = ef_report2(w_bk, U, P)
    r_cls_bk, is_gue_bk = gue_class_verdict(ev_bk_full)
    results["N4_BerryKeating"] = {
        "r_H7": r_bk, "shift": s_bk, "r_EF": rep_bk,
        "r_mean": r_cls_bk, "gue_class": bool(is_gue_bk),
        "class": "truncated xp — measured",
    }

    # ── N5: LCM-ядро (спектр вырожден — арифметическая подпись) ──
    M = nl.lcm_kernel(400)
    ev_lc = np.sort(np.linalg.eigvalsh(M))
    deg = float(1.0 - np.unique(np.round(ev_lc, 9)).size / ev_lc.size)
    D_lc = heat_trace_fluct(ev_lc - ev_lc.min(), U)
    from hpbridge.traceformula import fit_corr
    r_raw_lc, _, _ = fit_corr(D_lc, P)
    rep_lc = {"r_raw": float(r_raw_lc),
              "r_fluct": ef_fluct_corr(D_lc, P)}
    results["N5_LCM_kernel"] = {
        "r_H7": None,
        "r_H7_note": "unfold impossible: degenerate spectrum (arithmetic)",
        "degeneracy": deg, "r_EF": rep_lc,
        "class": "Λ(lcm) kernel — prime weight in the KERNEL, not spectrum",
    }

    # ── перестановочные p-значения ──
    null_ws = zmatch.random_windows(64)
    for key in ("N1_Hxi", "N2_DCT_twin", "N3_QR_twin"):
        w_obj = w_xi if key == "N1_Hxi" else unfolded_window(
            np.sort(np.linalg.eigvalsh(nl.ispectral_twin(ev_xi, kind=key[1:3].lower())[0])))
        rs = [corr_shift(w_obj, zw)[0] for zw in null_ws]
        results[key]["p_r"] = null_pvalue(results[key]["r_H7_matched"], rs)
    null_ws_v1 = zref.random_windows(64)
    rs_bk = [corr_shift(w_bk, zw)[0] for zw in null_ws_v1]
    results["N4_BerryKeating"]["p_r"] = null_pvalue(r_bk, rs_bk)
    for key in ("N1_Hxi", "N2_DCT_twin", "N3_QR_twin", "N4_BerryKeating"):
        rr = results[key].get("r_H7_matched", results[key].get("r_H7"))
        if rr is not None:
            results[key]["r_GUE_z"] = float((rr - g_mean) / max(g_std, 1e-12))

    from hpbridge.traceformula import surrogate_null
    surr_xi = surrogate_null(np.asarray(D_xi, float), P, 120, 5, 1234)
    surr_bk = surrogate_null(np.asarray(rep_bk["D"], float), P, 120, 5, 1234)
    results["N1_Hxi"]["r_EF"]["surrogate_null"] = surr_xi
    results["N4_BerryKeating"]["r_EF"]["surrogate_null"] = surr_bk

    verdict = {
        "meta": {
            "campaign": "C9 nonlocal trace primitive",
            "roadmap": "R1", "theorem": "T11",
            "zeros": "internal mpmath cache n=800 (no external files)",
            "convention": "unfolded-vs-unfolded (v2), U grid [0.05,1.0] x40",
            "zero_window_k0_convention": 224, "K": 200,
            "null_shifts": 64, "null_gue": 40,
            "runtime_s": round(time.time() - t0, 1),
        },
        "results": results,
        "verdict": {
            "ru": "Примитив существует: любой изоспектральный нелокальный "
                  "оператор несёт Λ(n)/√n в следе по построению (r_EF на "
                  "уровне PC0, r_H7 = 1); внеклассовые кандидаты (xp, "
                  "LCM-ядро) остаются в нулевых зонах ранговой ветви. "
                  "Открытая битовая ветвь — стена ЛОКАЛЬНОСТИ, а не следа "
                  "(T11).",
            "en": "The primitive exists: any isospectral nonlocal operator "
                  "carries Λ(n)/√n in its trace by construction (r_EF at "
                  "PC0 level, r_H7 = 1); off-class candidates (xp, LCM "
                  "kernel) stay in the rank branch's null zones. The open "
                  "bit-level branch is a wall of LOCALITY, not of the trace "
                  "(T11).",
        },
    }

    out = f"{R}/computations/C9_nonlocal_trace/data/results.json"
    # кривые D уходят в npz, не в JSON
    D_bk = rep_bk["D"]
    for v in results.values():
        if isinstance(v.get("r_EF"), dict):
            v["r_EF"].pop("D", None)
    json.dump(verdict, open(out, "w"), ensure_ascii=False, indent=1)
    np.savez(f"{R}/computations/C9_nonlocal_trace/data/curves.npz",
             U=U, P=P, D_xi=np.asarray(D_xi, float), D_bk=np.asarray(D_bk, float),
             D_lc=np.asarray(D_lc, float), gamma=gamma[:800])

    print("== C9 nonlocal trace ==")
    for k, v in results.items():
        re_f = v.get("r_EF") or {}
        r_raw = re_f.get("r_raw") if isinstance(re_f, dict) else re_f
        r_fl = re_f.get("r_fluct") if isinstance(re_f, dict) else None
        rh = v.get("r_H7_matched", v.get("r_H7"))
        rhs = f"{rh:+.3f}" if rh is not None else "  n/a"
        pr = v.get("p_r")
        prs = f"{pr:.3f}" if isinstance(pr, float) else "  -  "
        print(f"  {k}: r_H7={rhs} r_EF(raw)={r_raw:+.3f} "
              f"r_EF(fluct)={r_fl:+.3f} p_r={prs}")
    print("  ispectral deviation (twin): %.2e" % ispec_dev)
    print("  T6 recheck: |ΔK| ≤ %.1e ; B+C0 = %.1e"
          % (tf["max_abs_diff_K"], bmc[0]))
    print("  GUE null: %.3f ± %.3f" % (g_mean, g_std))
    print("  r_EF fluct (primary): N1=%.3f BK=%.3f" % (
        results["N1_Hxi"]["r_EF"]["r_fluct"],
        results["N4_BerryKeating"]["r_EF"]["r_fluct"]))
    print(f"  done in {verdict['meta']['runtime_s']} s")


if __name__ == "__main__":
    main()
