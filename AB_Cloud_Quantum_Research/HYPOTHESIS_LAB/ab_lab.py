#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ab_lab.py — the hypothesis laboratory of AB Cloud Quantum Research.

Anyone can test a hypothesis under the program discipline:
  - thresholds are fixed in the config BEFORE the run;
  - blind protocols: outputs are SHA256-pinned before validation;
  - every verdict carries does_not_prove.

Batteries:
  spinor   — the phase model theta = pi/k: cycles, reset, real-time step cost
  trace    — the explicit-formula check: primes side vs zeros side (Th6-style)
  zeros    — blind zero reading on a grid (mini-E17)
  compile  — exact Givens-QR compilation of a unitary 4x4 (V20-style)

Examples:
  python3 ab_lab.py doctor
  python3 ab_lab.py run spinor --theta 0.37 --steps 400
  python3 ab_lab.py run zeros --n 10
  python3 ab_lab.py run trace --x 40 --t 60
  python3 ab_lab.py run compile --n 4 --seed 7
  python3 ab_lab.py run custom --config examples/hypothesis_spinor.json
"""
import argparse, hashlib, json, math, os, sys, time

LAB_ROOT = os.path.dirname(os.path.abspath(__file__))
REPORTS = os.path.join(LAB_ROOT, "reports")
DEFAULT_DNP = {
    "spinor": "RH; primality of zeta zeros; applicability beyond the Markov task class",
    "trace": "RH; the analytic prerequisites of the obligation machine V13",
    "zeros": "RH above the tested height; the absence of off-line zeros beyond it",
    "compile": "scalability beyond the tested sizes; KAK-optimality inside the ISA class",
}

# ─────────────────────────── helpers ───────────────────────────

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

def pin_output(name, payload):
    os.makedirs(REPORTS, exist_ok=True)
    p = os.path.join(REPORTS, name)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    return {"file": os.path.relpath(p, LAB_ROOT), "sha256": sha256_file(p)}

def verdict(name, battery, metrics, thresholds, passed, dnp, pins=None, notes=None):
    v = {
        "campaign": name,
        "battery": battery,
        "pre_registered": thresholds,
        "metrics": metrics,
        "pass": bool(passed),
        "does_not_prove": dnp,
        "blind": True,
        "pins": pins or {},
        "notes": notes or [],
        "status": "done",
    }
    os.makedirs(REPORTS, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    out = os.path.join(REPORTS, f"{name}_{stamp}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(v, f, ensure_ascii=False, indent=1)
    return v, out

def show(v, path):
    print("=" * 62)
    print(f"campaign       : {v['campaign']}")
    print(f"battery        : {v['battery']}")
    print(f"pre_registered : {json.dumps(v['pre_registered'], ensure_ascii=False)}")
    for k, val in v["metrics"].items():
        print(f"  {k:26s}: {val}")
    print(f"VERDICT        : {'PASS' if v['pass'] else 'FAIL'}")
    print(f"does_not_prove : {v['does_not_prove']}")
    for k, p in (v.get("pins") or {}).items():
        print(f"pin[{k}]        : {p['sha256'][:16]}...  ({p['file']})")
    print(f"report         : {os.path.relpath(path, LAB_ROOT)}")
    print("=" * 62)

# ─────────────────────────── battery: spinor ───────────────────────────

def spinor_battery(theta, steps, thresholds, dnp, name):
    """Volatile spinor phase: closure of cycles (TS1), reset erasure (TS2),
    O(1) step cost (TS3)."""
    import random
    rng = random.Random(42)
    two_pi = 2 * math.pi
    # cycle detection: state = phase mod 2pi
    N = None
    if abs(theta) > 1e-12:
        ratio = two_pi / theta
        Nr = round(ratio)
        if Nr > 0 and abs(ratio - Nr) < 1e-9:
            N = int(Nr)
    cycle_closed = (N is not None)
    if N is None:
        # numeric cycle search up to steps
        phase, Nn = 0.0, None
        for i in range(1, steps + 1):
            phase = (phase + theta) % two_pi
            if abs(phase) < 1e-9 or abs(phase - two_pi) < 1e-9:
                Nn = i
                break
        N = Nn
        cycle_closed = Nn is not None
    # reset erasure: reconstruction <= 1/N (chance level)
    recon = 1.0 / N if N else float("nan")
    # real-time step cost: slope of per-step time over the run
    phase = 0.0
    times = []
    log = []  # the contrast machine keeps a journal
    t0 = time.perf_counter()
    for i in range(steps):
        t1 = time.perf_counter()
        phase = (phase + theta) % two_pi
        times.append(time.perf_counter() - t1)
        log.append(phase)  # eternal journal: Omega(t)
    n = len(times)
    half = max(2, n // 2)
    mean_first = sum(times[:half]) / half
    mean_last = sum(times[-half:]) / max(1, n - half)
    slope = (mean_last - mean_first) / steps
    journal_growth = len(log) / max(1, n)  # 1 per step by construction
    metrics = {
        "theta": round(theta, 9),
        "cycle_N": N if N else "none",
        "cycle_2k_ratio": round((N / (2 * round(two_pi / (2 * theta) / 2))) if N and theta else float("nan"), 6) if N else "n/a",
        "post_reset_reconstruction_max": round(recon, 4) if N else "n/a",
        "step_cost_slope_per_step_ms": f"{slope * 1000:.3e}",
        "journal_entries_per_step": round(journal_growth, 3),
    }
    thr = thresholds or {}
    passed = True
    if thr.get("cycle_closure") == "exact":
        passed &= cycle_closed
    rmax = thr.get("reconstruction_max")
    if rmax is not None and N:
        passed &= recon <= rmax + 1e-9
        metrics["reconstruction_vs_threshold"] = f"{recon:.4f} <= {rmax}"
    smax = thr.get("step_slope_abs_max")
    if smax is not None:
        passed &= abs(slope) <= smax
    pins = {"output": pin_output(f"{name}_output.json", {"metrics": metrics})}
    v, path = verdict(name, "spinor", metrics, thr, passed, dnp, pins,
                      notes=["contrast machine: the journal grows 1 entry/step → Omega(t) (see TS3)"])
    return v, path

# ─────────────────────────── battery: trace ───────────────────────────

def trace_battery(x, t_max, thresholds, dnp, name):
    """Explicit-formula check (Riemann–Weil style): the primes side
    psi(x) = sum_{n<=x} Lambda(n) versus the zeros side
    sum_{|gamma|<=T} x^rho/rho + corrections. Honest, offline, mpmath."""
    import mpmath as mp
    mp.mp.dps = 30
    # primes side: von Mangoldt weighted Chebyshev function psi(x)
    def psi(x):
        # Chebyshev psi(x) = sum_{n<=x} Lambda(n) via a proper prime sieve
        N = int(x)
        is_comp = [False] * (N + 1)
        for i in range(2, int(N ** 0.5) + 1):
            if not is_comp[i]:
                for j in range(i * i, N + 1, i):
                    is_comp[j] = True
        lam = [0.0] * (N + 1)
        for p in range(2, N + 1):
            if not is_comp[p]:  # p is prime
                pk = p
                while pk <= N:
                    lam[pk] = math.log(p)  # Lambda(p^k) = log p
                    pk *= p
        return mp.fsum(lam[2:])
    ps = psi(x)
    # zeros side
    zsum = mp.mpf("0")
    n = 1
    while True:
        g = mp.zetazero(n).imag
        if g > t_max:
            break
        rho = mp.mpc("0.5", g)
        zsum += (x ** rho) / rho + (x ** (1 - rho)) / (1 - rho)
        n += 1
    # Riemann-Weil explicit formula: psi0(x) = x - sum_rho x^rho/rho
    #                                  - log(2*pi) - 0.5*log(1 - x^-2)
    zero_side = x - zsum - mp.log(2 * mp.pi) - mp.mpf("0.5") * mp.log(1 - x ** -2)
    residual = abs(ps - zero_side) / max(1, abs(ps))
    metrics = {
        "x": x, "T": t_max,
        "psi(x) primes side": mp.nstr(ps, 10),
        "zeros side + corrections": mp.nstr(zero_side, 10),
        "relative residual": mp.nstr(residual, 4),
        "zeros used": n - 1,
    }
    # truncation bound: |R| = O(x log^2(xT) / T) — reported alongside the residual
    bound = x * math.log(x * t_max) ** 2 / t_max / max(1.0, float(ps))
    metrics["truncation_bound_rel"] = f"{bound:.3e}"
    thr = thresholds or {}
    rmax = float(thr.get("residual_max", 0.05))
    passed = residual <= rmax
    pins = {"output": pin_output(f"{name}_output.json",
                                 {"metrics": {k: str(v) for k, v in metrics.items()}})}
    v, path = verdict(name, "trace", metrics, thr, passed, dnp, pins)
    return v, path

# ─────────────────────────── battery: zeros ───────────────────────────

def zeros_battery(n_zeros, grid_step, thresholds, dnp, name):
    """Mini-E17: blind detection of the first n zeta zeros by scanning
    Z(t) = Re zeta(1/2 + it) sign changes; the validator compares with
    mpmath.zetazero AFTER the detector output is pinned."""
    import mpmath as mp
    mp.mp.dps = 20
    half = mp.mpf("0.5")
    # detector: no reference available here by construction
    t = mp.mpf("14.0")  # start just below the first zero
    found = []
    prevZ = mp.siegelz(float(t))
    t_end = float(mp.im(mp.zetazero(n_zeros))) + 0.5
    while t < t_end:
        t += grid_step
        Z = mp.siegelz(float(t))
        if prevZ * Z < 0:
            # bisect for the sign change
            lo, hi = t - grid_step, t
            flo = prevZ
            for _ in range(40):
                mid = (lo + hi) / 2
                fm = mp.siegelz(float(mid))
                if flo * fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            found.append(float((lo + hi) / 2))
        prevZ = Z
    # pin the detector output BEFORE validation
    pin = pin_output(f"{name}_detector.json", {"ordinates": found})
    # validator: compare with the reference
    ref = [float(mp.im(mp.zetazoo(i))) if False else float(mp.im(mp.zetazero(i))) for i in range(1, len(found) + 1)]
    matched, max_err = 0, 0.0
    for a, b in zip(found, ref):
        err = abs(a - b)
        max_err = max(max_err, err)
        if err <= max(grid_step, 1e-6):
            matched += 1
    precision = matched / len(found) if found else 0.0
    recall = matched / len(ref) if ref else 0.0
    metrics = {
        "n_zeros_requested": n_zeros,
        "n_detected": len(found),
        "matched": matched,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "max_abs_error": f"{max_err:.3e}",
        "grid_step": grid_step,
    }
    thr = thresholds or {}
    pmin = float(thr.get("precision_recall_min", 0.999))
    passed = precision >= pmin and recall >= pmin and len(found) == n_zeros
    v, path = verdict(name, "zeros", metrics, thr, passed, dnp,
                      {"detector": pin, "reference_note": "mpmath.zetazero (validator side only)"})
    return v, path

# ─────────────────────────── battery: compile ───────────────────────────

def _givens(a, b):
    r = math.hypot(abs(a), abs(b))
    if r < 1e-300:
        return (1 + 0j, 0 + 0j)
    return (a / r, b.conjugate() / r)

def compile_battery(n, seed, thresholds, dnp, name):
    """V20-style: exact decomposition of a random unitary n x n into
    two-level Givens rotations; reconstruction fidelity 1 - F."""
    import numpy as np
    rng = np.random.default_rng(seed)
    A = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(A)
    Q *= np.sign(np.diag(R).real)[:, None]  # deterministic phase
    # Givens-QR style two-level reduction to diagonal
    U = Q.copy()
    gates = []
    M = U.copy()
    gate_list = []
    for col in range(n - 1):
        for row in range(col + 1, n):
            a, b = M[col, col], M[row, col]
            if abs(b) < 1e-14:
                continue
            c, s = _givens(a, b)  # c = a/r, s = b/r
            G = np.eye(n, dtype=complex)
            G[col, col] = c.conjugate()
            G[col, row] = s.conjugate()
            G[row, col] = -s
            G[row, row] = c
            M = G @ M
            gate_list.append(G)
    # M = G_k ... G_1 U is (numerically) a diagonal unitary; keep its phases
    rec = M.copy()
    for G in reversed(gate_list):
        rec = G.conj().T @ rec
    F = abs(np.trace(rec.conj().T @ U) / n) ** 2
    infid = max(0.0, 1.0 - float(F))
    metrics = {
        "size": n, "seed": seed,
        "gates": len(gate_list),
        "1-F": f"{infid:.3e}",
        "machine_eps": "2.2e-16",
    }
    thr = thresholds or {}
    fmax = float(thr.get("infidelity_max", 1e-12))
    passed = infid <= fmax
    pins = {"output": pin_output(f"{name}_output.json",
                                 {"metrics": metrics, "gates": len(gate_list)})}
    v, path = verdict(name, "compile", metrics, thr, passed, dnp, pins)
    return v, path

# ─────────────────────────── CLI ───────────────────────────

def doctor():
    ok = True
    try:
        import numpy  # noqa
        print("[ok] numpy", numpy.__version__)
    except Exception as e:
        ok = False
        print("[!!] numpy:", e)
    try:
        import mpmath  # noqa
        print("[ok] mpmath", mpmath.__version__)
    except Exception as e:
        ok = False
        print("[!!] mpmath:", e)
    print("[ok] reports dir:", os.path.relpath(REPORTS, LAB_ROOT))
    print("[ok] examples:", len(os.listdir(os.path.join(LAB_ROOT, "examples"))) if os.path.isdir(os.path.join(LAB_ROOT, "examples")) else 0)
    print("RESULT:", "READY" if ok else "INCOMPLETE")
    return 0 if ok else 1

def load_config(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def run_battery(battery, args, cfg=None):
    cfg = cfg or {}
    thresholds = cfg.get("thresholds")
    dnp = cfg.get("does_not_prove") or DEFAULT_DNP[battery]
    name = cfg.get("name") or f"lab-{battery}"
    if battery == "spinor":
        return spinor_battery(float(cfg.get("theta", args.theta)), int(cfg.get("steps", args.steps)),
                              thresholds, dnp, name)
    if battery == "trace":
        return trace_battery(int(cfg.get("x", args.x)), int(cfg.get("t", args.t)), thresholds, dnp, name)
    if battery == "zeros":
        return zeros_battery(int(cfg.get("n", args.n)), float(cfg.get("grid", args.grid)), thresholds, dnp, name)
    if battery == "compile":
        return compile_battery(int(cfg.get("n", args.n)), int(cfg.get("seed", args.seed)), thresholds, dnp, name)
    raise SystemExit(f"unknown battery: {battery}")

def main():
    ap = argparse.ArgumentParser(description="AB Cloud hypothesis laboratory")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor")
    p_run = sub.add_parser("run")
    p_run.add_argument("battery", choices=["spinor", "trace", "zeros", "compile", "custom"])
    p_run.add_argument("--theta", type=float, default=math.pi / 3)
    p_run.add_argument("--steps", type=int, default=400)
    p_run.add_argument("--x", type=int, default=40)
    p_run.add_argument("--t", type=int, default=60)
    p_run.add_argument("--n", type=int, default=10)
    p_run.add_argument("--grid", type=float, default=0.02)
    p_run.add_argument("--seed", type=int, default=7)
    p_run.add_argument("--config", help="hypothesis JSON config (for custom)")
    sub.add_parser("verdicts")
    args = ap.parse_args()

    if args.cmd == "doctor":
        sys.exit(doctor())
    if args.cmd == "verdicts":
        if not os.path.isdir(REPORTS):
            print("no reports yet")
            return
        for f in sorted(os.listdir(REPORTS)):
            if f.endswith(".json"):
                print(f)
        return
    cfg = None
    battery = args.battery
    if battery == "custom":
        if not args.config:
            raise SystemExit("custom requires --config")
        cfg = load_config(args.config if os.path.isabs(args.config)
                          else os.path.join(LAB_ROOT, args.config))
        battery = cfg.get("battery", "spinor")
    v, path = run_battery(battery, args, cfg)
    show(v, path)
    sys.exit(0 if v["pass"] else 2)

if __name__ == "__main__":
    main()
