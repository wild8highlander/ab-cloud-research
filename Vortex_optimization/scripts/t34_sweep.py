"""
t34_sweep.py — оркестратор масштабной развёртки параметров вихрей Теста 34.

Стадии:
  A  скрин L=24: все оси (Nv × q × W) + геометрия (placement, BC) + α
  B  уточнение: L=32 (топ-20), L=48 (топ-12), L=64 (топ-8) по D_pooled
  C  верификация 96×96 (полный протокол теста 34b, n_real=5): топ-3 + референс
     (Nv=2, q=1.0, W=1.0, α=0.5, open, protocol — конфиг прогона 20260914_234626)
     + GUE-контроль L=96

Использование:
  python3 t34_sweep.py A
  python3 t34_sweep.py B
  python3 t34_sweep.py C
Результаты дописываются в CSV (crash-safe, дедуп по ключу конфигурации).
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t34_engine as E

REPO = "/home/z/my-project/ab-cloud-research"
ZETA_PATH = f"{REPO}/verification/data/zeta_zeros_50000_embedded.txt"
OUT_DIR = "/home/z/my-project/download/t34_research"
os.makedirs(OUT_DIR, exist_ok=True)

FIELDS = ["stage", "L", "Nv", "q", "W", "alpha", "bc", "placement", "n_real",
          "seed_base", "n_spacings", "D_pooled", "p_pooled", "D_min", "D_med",
          "D_max", "mean_abs_dR2", "d_GUE", "d_Pois", "r_mean", "D_excess",
          "ks_pass", "r2_pass", "gue_closer", "stab_pass", "composite_ok",
          "runtime_s"]

STAGE_FILES = {"A": "sweep_A_L24.csv", "B": "sweep_B_refine.csv",
               "C": "sweep_C_L96.csv"}


def load_existing(path):
    done = set()
    if os.path.exists(path):
        with open(path) as f:
            for row in csv.DictReader(f):
                done.add((int(row["L"]), int(row["Nv"]), float(row["q"]),
                          float(row["W"]), float(row["alpha"]), row["bc"],
                          row["placement"], int(row["n_real"])))
    return done


def append_rows(path, rows):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: (float(f"{v:.6g}") if isinstance(v, float) else v)
                        for k, v in r.items() if k in FIELDS})


def fmt(r, ctl_D):
    r = dict(r)
    r["D_excess"] = r["D_pooled"] - ctl_D
    return {k: r.get(k) for k in FIELDS}


def stage_A():
    path = os.path.join(OUT_DIR, STAGE_FILES["A"])
    done = load_existing(path)
    E.load_zeta(ZETA_PATH)
    ctl = E.gue_control(24, n_real=3)
    ctl_D = ctl["D_gue_vs_zeta"]
    print(f"[A] GUE-контроль L=24: D_floor={ctl_D:.4f} "
          f"R2cal={ctl['mean_abs_dR2_cal']:.4f} R2vsζ={ctl['mean_abs_dR2_vs_zeta']:.4f}")
    rows, jobs = [], []
    Nvs = [0, 1, 2, 3, 4, 6, 8, 12, 16]
    Qs = [0.2, 0.3, 0.5, 0.7, 1.0]
    Ws = [0.0, 0.5, 1.0]
    # базовая сетка Nv × q × W (Nv=0 — только q=0.3)
    for Nv in Nvs:
        for q in (Qs if Nv > 0 else [0.3]):
            for W in Ws:
                jobs.append(dict(Nv=Nv, q=q, W=W, alpha=0.5, bc="open",
                                 placement="protocol"))
    # геометрия: placement
    for Nv in [2, 4, 8, 16]:
        for q in [0.3, 1.0]:
            for pl in ["regular", "cluster"]:
                jobs.append(dict(Nv=Nv, q=q, W=1.0, alpha=0.5, bc="open",
                                 placement=pl))
    # геометрия: BC (торус)
    for Nv in [2, 4, 8, 16]:
        for q in [0.3, 1.0]:
            jobs.append(dict(Nv=Nv, q=q, W=1.0, alpha=0.5, bc="torus",
                             placement="protocol"))
    # α-скан
    for Nv in [2, 4, 8, 16]:
        for q in [0.3, 1.0]:
            for al in [0.3, 0.4, 0.6]:
                jobs.append(dict(Nv=Nv, q=q, W=1.0, alpha=al, bc="open",
                                 placement="protocol"))
    t00 = time.perf_counter()
    for j in jobs:
        key = (24, j["Nv"], j["q"], j["W"], j["alpha"], j["bc"], j["placement"], 3)
        if key in done:
            continue
        t0 = time.perf_counter()
        r = E.run_config(j["Nv"], j["q"], j["W"], j["alpha"], 24, j["bc"],
                         placement=j["placement"], n_real=3)
        r["runtime_s"] = time.perf_counter() - t0
        r["stage"] = "A"
        row = fmt(r, ctl_D)
        rows.append(row)
        print(f"[A] Nv={j['Nv']:2d} q={j['q']:.2f} W={j['W']:.1f} α={j['alpha']:.2f} "
              f"{j['bc']:5s}/{j['placement']:8s}: D={r['D_pooled']:.4f} "
              f"Dexc={row['D_excess']:+.4f} ⟨r⟩={r['r_mean']:.4f} "
              f"({'OK' if r['composite_ok'] else '--'}) [{r['runtime_s']:.1f}s]")
        if len(rows) >= 12:
            append_rows(path, rows); rows = []
    append_rows(path, rows)
    print(f"[A] готово за {time.perf_counter()-t00:.0f} с → {path}")


def read_csv_rows(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def stage_B():
    E.load_zeta(ZETA_PATH)
    import multiprocessing as mp
    ctx = mp.get_context("spawn")
    pathA = os.path.join(OUT_DIR, STAGE_FILES["A"])
    path = os.path.join(OUT_DIR, STAGE_FILES["B"])
    rowsA = read_csv_rows(pathA)
    base = [r for r in rowsA if r["placement"] == "protocol" and
            r["bc"] == "open" and abs(float(r["alpha"]) - 0.5) < 1e-9]
    base.sort(key=lambda r: float(r["D_pooled"]))
    # кандидаты: (Nv, q, W, alpha, bc, placement)
    cands = []
    for r in base[:15]:
        cands.append((int(r["Nv"]), float(r["q"]), float(r["W"]), 0.5, "open",
                      "protocol"))
    tor = [r for r in rowsA if r["bc"] == "torus" and r["placement"] == "protocol"]
    tor.sort(key=lambda r: float(r["D_pooled"]))
    for r in tor[:3]:
        cands.append((int(r["Nv"]), float(r["q"]), float(r["W"]), 0.5, "torus",
                      "protocol"))
    reg = [r for r in rowsA if r["placement"] == "regular" and r["bc"] == "open"]
    reg.sort(key=lambda r: float(r["D_pooled"]))
    for r in reg[:1]:
        cands.append((int(r["Nv"]), float(r["q"]), float(r["W"]), 0.5, "open",
                      "regular"))
    # α-варианты лучшей базовой конфигурации
    best = base[0]
    Nb, qb, Wb = int(best["Nv"]), float(best["q"]), float(best["W"])
    for al in (0.3, 0.4, 0.6):
        cands.append((Nb, qb, Wb, al, "open", "protocol"))
    # дедуп
    seen, cand_list = set(), []
    for c in cands:
        if c not in seen:
            seen.add(c)
            cand_list.append(c)
    print(f"[B] кандидаты ({len(cand_list)}): {cand_list}")
    done = load_existing(path)

    def run_cand(L, c, nreal, ctl_D):
        Nv, q, W, al, bc, pl = c
        key = (L, Nv, q, W, al, bc, pl, nreal)
        if key in done:
            return None
        t0 = time.perf_counter()
        payload = {"Nv": Nv, "q": q, "W": W, "alpha": al, "L": L, "bc": bc,
                   "placement": pl, "n_real": nreal,
                   "zeta_unf": E.ZETA_UNF, "r2_zeta": E.R2_ZETA_CACHE}
        with ctx.Pool(1) as pool:
            r = pool.apply(_config_worker, (payload,))
        E.malloc_trim()
        r["runtime_s"] = time.perf_counter() - t0
        r["stage"] = f"B(L={L})"
        row = fmt(r, ctl_D)
        append_rows(path, [row])
        print(f"[B] L={L} Nv={Nv:2d} q={q:.2f} W={W:.1f} α={al:.2f} {bc:5s}/{pl:8s}: "
              f"D={r['D_pooled']:.4f} Dexc={row['D_excess']:+.4f} ⟨r⟩={r['r_mean']:.4f} "
              f"dGUE={r['d_GUE']:.4f} [{r['runtime_s']:.1f}s]")
        return row

    plan = [(32, cand_list, 3), (48, None, 3), (64, None, 3)]
    t00 = time.perf_counter()
    for L, cs, nreal in plan:
        with ctx.Pool(1) as pool:
            ctl = pool.apply(_gue_ctl_worker,
                             ({"L": L, "n_real": 2, "seed": 777,
                               "zeta_unf": E.ZETA_UNF,
                               "r2_zeta": E.R2_ZETA_CACHE},))
        E.malloc_trim()
        print(f"[B] L={L}: GUE-контроль D_floor={ctl['D_gue_vs_zeta']:.4f}")
        if cs is None:
            rowsB = read_csv_rows(path)
            rowsB.sort(key=lambda r: float(r["D_pooled"]))
            keep = []
            for r in rowsB:
                c = (int(r["Nv"]), float(r["q"]), float(r["W"]),
                     float(r["alpha"]), r["bc"], r["placement"])
                if c not in keep:
                    keep.append(c)
                if len(keep) == (10 if L == 48 else 8):
                    break
            # α-скан текущего лучшего на этом L
            b = rowsB[0]
            for al in (0.3, 0.4, 0.6):
                c = (int(b["Nv"]), float(b["q"]), float(b["W"]), al,
                     b["bc"], b["placement"])
                if c not in keep:
                    keep.append(c)
            cs = keep
            print(f"[B] L={L}: кандидаты после отсева: {cs}")
        for c in cs:
            run_cand(L, c, nreal, ctl["D_gue_vs_zeta"])
    print(f"[B] готово за {time.perf_counter()-t00:.0f} с → {path}")


def _gue_ctl_worker(payload):
    import t34_engine as TE
    TE.ZETA_UNF = np.asarray(payload["zeta_unf"])
    TE.R2_ZETA_CACHE = np.asarray(payload["r2_zeta"])
    return TE.gue_control(payload["L"], n_real=payload["n_real"],
                          seed=payload["seed"])


def _config_worker(payload):
    """Субпроцесс для run_config: изоляция glibc-арен (см. ab_gc! оригинала)."""
    import t34_engine as TE
    TE.ZETA_UNF = np.asarray(payload["zeta_unf"])
    TE.R2_ZETA_CACHE = np.asarray(payload["r2_zeta"])
    r = TE.run_config(payload["Nv"], payload["q"], payload["W"],
                      payload["alpha"], payload["L"], payload["bc"],
                      placement=payload["placement"],
                      n_real=payload["n_real"])
    return {k: v for k, v in r.items() if not k.startswith("_")}


def _one_realization_worker(args):
    """Субпроцесс: одна реализация на L=96 (контроль памяти)."""
    (Nv, q, W, alpha, bc, placement, seed_base, k, use_fortran) = args
    import t34_engine as TE  # в субпроцессе
    vortex_rng = np.random.default_rng(seed_base + TE.HARDCORE_OFFSET)
    # воспроизводим потребление потока вихревого RNG реализациями 1..k−1
    for _ in range(k - 1):
        if Nv > 0:
            TE.random_vortex_configuration(Nv, 96, 96, q, vortex_rng,
                                            placement)
    vortices = (TE.random_vortex_configuration(Nv, 96, 96, q, vortex_rng,
                                               placement) if Nv > 0 else [])
    dis_rng = np.random.default_rng(seed_base + TE.HARDCORE_OFFSET + k)
    order = "F" if use_fortran else "C"
    H = TE.build_ab_cloud_hamiltonian(96, 96, vortices, alpha, TE.T_HOP, W,
                                      bc, dis_rng, order=order)
    ev = np.sort(__import__("scipy.linalg", fromlist=["eigvalsh"]).
                 eigvalsh(H, check_finite=False, driver="evr",
                          overwrite_a=True))
    central = TE.central_band_eigs(ev, TE.CENTER_FRACTION)
    sp = TE.unfold_spacings(central)
    r_mean = TE.mean_adjacent_r(central)
    return {"sp": sp.tolist(), "r_mean": r_mean}


def stage_C(cands=None):
    E.load_zeta(ZETA_PATH)
    path = os.path.join(OUT_DIR, STAGE_FILES["C"])
    import multiprocessing as mp
    ctx = mp.get_context("spawn")

    if cands is None:
        # выбор кандидатов: топ-3 стадии B + референс теста 34
        rowsB = read_csv_rows(os.path.join(OUT_DIR, STAGE_FILES["B"]))
        rowsB.sort(key=lambda r: float(r["D_pooled"]))
        seen, cands = set(), []
        for r in rowsB:
            c = (int(r["Nv"]), float(r["q"]), float(r["W"]), float(r["alpha"]),
                 r["bc"], r["placement"])
            if c not in seen:
                seen.add(c)
                cands.append(c)
            if len(cands) == 3:
                break
        ref = (2, 1.0, 1.0, 0.5, "open", "protocol")
        if ref not in cands:
            cands.append(ref)
    print(f"[C] кандидаты 96×96: {cands}")

    done = load_existing(path)
    for (Nv, q, W, al, bc, pl) in cands:
        key = (96, Nv, q, W, al, bc, pl, 5)
        if key in done:
            print(f"[C] Nv={Nv} q={q} W={W}: уже выполнено, пропуск")
            continue
        t0 = time.perf_counter()
        ab_all, per_real_D, r_means = [], [], []
        for k in range(1, 6):
            args = (Nv, q, W, al, bc, pl, E.BASE_SEED, k, True)
            with ctx.Pool(1) as pool:
                out = pool.apply(_one_realization_worker, (args,))
            sp = np.array(out["sp"])
            ab_all.append(sp)
            r_means.append(out["r_mean"])
            D_k, _ = E.ks2sample(sp, E.ZETA_UNF)
            per_real_D.append(D_k)
            print(f"[C] Nv={Nv} q={q:.2f} W={W:.1f} α={al:.2f} {bc:5s}/{pl:8s} "
                  f"real {k}/5: {len(sp)} spacings, D_k={D_k:.4f}, "
                  f"⟨r⟩={out['r_mean']:.4f}", flush=True)
        ab_pooled = np.concatenate(ab_all)
        D_pooled, p_pooled = E.ks2sample(ab_pooled, E.ZETA_UNF)
        pos = np.concatenate(([0.0], np.cumsum(ab_pooled)))
        s_grid, R2_ab = E.pair_corr_R2(pos, 4.0, 0.05)
        R2_gue = 1.0 - (np.sin(np.pi * s_grid) / (np.pi * s_grid)) ** 2
        mean_dR2 = float(np.mean(np.abs(R2_ab - E.R2_ZETA_CACHE)))
        d_gue = float(np.mean(np.abs(R2_ab - R2_gue)))
        d_pois = float(np.mean(np.abs(R2_ab - 1.0)))
        per_real_D.sort()
        r = {"stage": "C(96x96)", "L": 96, "Nv": Nv, "q": q, "W": W,
             "alpha": al, "bc": bc, "placement": pl, "n_real": 5,
             "seed_base": E.BASE_SEED, "n_spacings": len(ab_pooled),
             "D_pooled": D_pooled, "p_pooled": p_pooled,
             "D_min": per_real_D[0], "D_med": float(np.median(per_real_D)),
             "D_max": per_real_D[-1], "mean_abs_dR2": mean_dR2,
             "d_GUE": d_gue, "d_Pois": d_pois,
             "r_mean": float(np.mean(r_means)), "D_excess": float("nan"),
             "ks_pass": bool((p_pooled > 0.01) or (D_pooled < 0.10)),
             "r2_pass": bool(mean_dR2 < 0.10), "gue_closer": bool(d_gue < d_pois),
             "stab_pass": bool((per_real_D[-1] - per_real_D[0]) < 0.10),
             "runtime_s": time.perf_counter() - t0}
        r["composite_ok"] = bool(r["ks_pass"] and r["r2_pass"] and
                                 r["gue_closer"] and r["stab_pass"])
        append_rows(path, [{k: r.get(k) for k in FIELDS}])
        print(f"[C] ИТОГ Nv={Nv} q={q:.2f} W={W:.1f} α={al:.2f} {bc:5s}/{pl:8s}: D={D_pooled:.4f} "
              f"p={p_pooled:.3g}, per-real {per_real_D[0]:.4f}/{np.median(per_real_D):.4f}/"
              f"{per_real_D[-1]:.4f}, ⟨|ΔR₂|⟩={mean_dR2:.4f}, d_GUE={d_gue:.4f} "
              f"vs d_Pois={d_pois:.4f} → composite {'PASS' if r['composite_ok'] else 'WARN'} "
              f"[{r['runtime_s']:.0f}s]")
        # сохраняем R₂-кривые победителей для отчёта
        tag = f"Nv{Nv}_q{q:.2f}_W{W:.2f}_a{al:.2f}_{bc}_{pl}"
        np.savez(os.path.join(OUT_DIR, f"R2_L96_{tag}.npz"),
                 s_grid=s_grid, R2_ab=R2_ab, R2_gue=R2_gue, R2_zeta=E.R2_ZETA_CACHE)
    # GUE-контроль L=96 (2 реализации)
    ctl_path = os.path.join(OUT_DIR, "gue_control_L96.json")
    if not os.path.exists(ctl_path):
        ctl = {}
        for k in (1, 2):
            t0 = time.perf_counter()
            with ctx.Pool(1) as pool:
                out = pool.apply(_gue_realization_worker, (777000 + k,))
            ctl.setdefault("sps", []).extend(out["sp"])
            print(f"[C] GUE control real {k}: {len(out['sp'])} spacings "
                  f"[{time.perf_counter()-t0:.0f}s]", flush=True)
        pooled = np.array(ctl["sps"])
        D, p = E.ks2sample(pooled, E.ZETA_UNF)
        pos = np.concatenate(([0.0], np.cumsum(pooled)))
        s_grid, R2_g = E.pair_corr_R2(pos, 4.0, 0.05)
        R2t = 1.0 - (np.sin(np.pi * s_grid) / (np.pi * s_grid)) ** 2
        res = {"L": 96, "n_real": 2, "n_spacings": len(pooled),
               "D_gue_vs_zeta": D, "p": p,
               "mean_abs_dR2_cal": float(np.mean(np.abs(R2_g - R2t))),
               "mean_abs_dR2_vs_zeta": float(np.mean(np.abs(R2_g - E.R2_ZETA_CACHE)))}
        with open(ctl_path, "w") as f:
            json.dump(res, f, indent=1)
        print(f"[C] GUE-контроль L=96: D_floor={D:.4f}, "
              f"⟨|ΔR₂|⟩_cal={res['mean_abs_dR2_cal']:.4f}")


def _gue_realization_worker(seed_k):
    import t34_engine as TE
    rng = np.random.default_rng(seed_k)
    n = 96 * 96
    X = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    H = (X + X.conj().T) / 2
    del X
    ev = np.sort(__import__("scipy.linalg", fromlist=["eigvalsh"]).
                 eigvalsh(H, check_finite=False, driver="evr", overwrite_a=True))
    central = TE.central_band_eigs(ev, TE.CENTER_FRACTION)
    sp = TE.unfold_spacings(central)
    return {"sp": sp.tolist(), "r_mean": 0.0}


if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "A"
    if stage == "A":
        stage_A()
    elif stage == "B":
        stage_B()
    elif stage == "C":
        stage_C(sys.argv[2:] and json.loads(sys.argv[2]) or None)
    else:
        raise SystemExit(f"неизвестная стадия {stage}")
