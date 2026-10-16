# -*- coding: utf-8 -*-
"""CLI: python3 -m abcloud <command> [options]

Commands: selftest | zeros | suite | ham | bN | gram | test11 | hp | sweep
"""

import os
import sys
from math import log, sqrt, pi

from .mt19937 import MT19937
from .special import compute_bN, gram_point
from .gof import (normalized_spacings, ks_test, cvm_test, anderson_darling_stat,
                  chi2_gue_test, mean_adjacent_spacing_ratio,
                  unfolded_positions, number_variance, delta3_rigidity,
                  compute_K_form_factor)
from .rmt_table import RMT
from .lattice import Vortex, ABCloudConfig, build_ab_cloud_hamiltonian, safe_eigvals
from .unfold import hp_raw_ft, default_omega_grid, h1_report
from .golden import run_selftest, tvals_envelope
from .suite import run_suite


def _usage():
    sys.stderr.write(
        "usage: python3 -m abcloud <command> [options]\n"
        "commands:\n"
        "  selftest [--golden P] [--data P]   golden-reference parity check\n"
        "  zeros [--data P] [--n N]           full zero-analysis battery\n"
        "  suite [--test N|all] [--data P]    portable subset of the 39-test suite\n"
        "  bN --N n... [--offset k]           b(N) statistic\n"
        "  gram --n n...                      Gram points\n"
        "  test11 [--mc n] [--seed s]         Anderson-Darling honest test\n"
        "  hp [--data P] [--n N]              H1 primary detector\n"
        "  sweep                              b(N) ladder sweep\n")
    return 2


def _load_zeros(path):
    z = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    z.append(float(line))
                except ValueError:
                    pass
    z.sort()
    return z


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return _usage()
    cmd = argv[0]
    data = golden = test = None
    ns = []
    offset = 0
    ncut = 0
    mc, seed = 200, 777
    i = 1
    while i < len(argv):
        a = argv[i]
        nxt = argv[i + 1] if i + 1 < len(argv) else ""
        if a == "--data":
            data = nxt
            i += 2
        elif a == "--golden":
            golden = nxt
            i += 2
        elif a == "--test":
            test = nxt
            i += 2
        elif a in ("--N", "--n"):
            j = i + 1
            while j < len(argv) and not argv[j].startswith("-"):
                ns.append(int(float(argv[j])))
                j += 1
            i = j
        elif a == "--offset":
            offset = int(float(nxt))
            i += 2
        elif a == "--mc":
            mc = int(nxt)
            i += 2
        elif a == "--seed":
            seed = int(nxt)
            i += 2
        else:
            i += 1

    # default paths relative to the package layout:
    #   ports/python/abcloud -> ../../../zeros50k.txt, ../../golden/abcloud_golden.json
    pkg_dir = os.path.dirname(os.path.abspath(__file__))
    default_zeros = os.path.normpath(
        os.path.join(pkg_dir, "..", "..", "..", "zeros50k.txt"))
    default_golden = os.path.normpath(
        os.path.join(pkg_dir, "..", "..", "golden", "abcloud_golden.json"))
    zeros_path = data or default_zeros
    golden_path = golden or default_golden

    if cmd == "selftest":
        z = _load_zeros(zeros_path)
        return run_selftest(z, golden_path)

    if cmd == "zeros":
        z = _load_zeros(zeros_path)
        if ncut:
            z = z[:ncut]
        sp = normalized_spacings(z)
        mean = sum(sp) / len(sp)
        var = sum((s - mean) * (s - mean) for s in sp) / (len(sp) - 1)
        D, p = ks_test(sp)
        print("zeros: n=%d  g1=%.6f  gN=%.6f" % (len(z), z[0], z[-1]))
        print("spacings: n=%d  mean=%.6f  var=%.6f" % (len(sp), mean, var))
        print("KS  : D=%.6f  p=%.6e" % (D, p))
        print("CvM : W2=%.6f" % cvm_test(sp))
        print("A2  : %.6f" % anderson_darling_stat(sp))
        chi2, df, pchi = chi2_gue_test(sp, 30)
        print("chi2: %.4f  df=%d  p=%.6e" % (chi2, df, pchi))
        r, n_r = mean_adjacent_spacing_ratio(z)
        print("<r> : %.6f  (n_r=%d; GUE 0.5992, Poisson 0.6243)" % (r, n_r))
        pos = unfolded_positions(z)
        rng = MT19937(777)
        for L in (5.0, 10.0, 20.0, 50.0, 100.0):
            print("S2(L=%6.1f) = %.6f  [Poisson %.1f]"
                  % (L, number_variance(pos, L, 3000, rng), L))
        for L in (5.0, 10.0, 20.0, 50.0):
            print("D3(L=%6.1f) = %.6f  [Poisson %.4f]"
                  % (L, delta3_rigidity(pos, L, 300, 300, rng), L / 15.0))
        tvals = [0.1 * i for i in range(1, 31)]
        K = compute_K_form_factor(z, tvals)
        for t in (0.2, 0.5, 1.0, 2.0, 3.0):
            idx = int(round(t / 0.1)) - 1
            print("K(t=%.1f) = %.6f  [GUE envelope %.6f]"
                  % (t, K[idx], tvals_envelope(t)))
        return 0

    if cmd == "suite":
        z = _load_zeros(zeros_path)
        run_suite(z, test or "all")
        return 0

    if cmd == "bN":
        z = _load_zeros(zeros_path)
        ns = ns or [100, 1000, 10000]
        for N in ns:
            print("b(N=%6d, offset=%d) = %.10f" % (N, offset, compute_bN(z, N, offset)))
        return 0

    if cmd == "gram":
        ns = ns or [1, 10, 100]
        for n in ns:
            print("g_%d = %.10f" % (n, gram_point(n)))
        return 0

    if cmd == "test11":
        z = _load_zeros(zeros_path)
        sp = normalized_spacings(z)
        A2 = anderson_darling_stat(sp)
        print("Test 11 (honest): exact A2 on n=%d spacings: %.6f" % (len(sp), A2))
        if mc > 0:
            rng = MT19937(seed)
            buf = [0.0] * len(sp)
            count = 0
            for _ in range(mc):
                RMT.sample(rng, buf)
                if anderson_darling_stat(buf) >= A2:
                    count += 1
            print("MC null (law-exact inverse-CDF, %d draws): p = %.6f  (%d/%d >= A2)"
                  % (mc, (count + 1.0) / (mc + 1.0), count, mc))
        return 0

    if cmd == "hp":
        z = _load_zeros(zeros_path)
        if ncut:
            z = z[:ncut]
        rep = h1_report(z, default_omega_grid())
        print("H1 primary detector on %d positions (band median %.6e):"
              % (len(z), rep["median"]))
        for ln in rep["lines"]:
            print(ln)
        print("  verdict: " + rep["verdict"])
        return 0

    if cmd == "sweep":
        z = _load_zeros(zeros_path)
        ns = ns or [100, 500, 1000, 5000, 10000, 50000]
        print("  N        b(N)")
        for N in ns:
            print("%6d  %.8f" % (N, compute_bN(z, N)))
        return 0

    if cmd == "ham":
        # demo battery: the three golden Hamiltonian configurations
        for name, cfg in (
            ("L8_open_a05_clean",
             ABCloudConfig(8, 8, [], 0.5, 1.0, "open", 0.0, 96, "monumental")),
            ("L8_open_a025_2vort",
             ABCloudConfig(8, 8, [Vortex(3.5, 3.5, 1.0), Vortex(6.5, 6.5, -1.0)],
                           0.25, 1.0, "open", 0.0, 96, "monumental")),
            ("L10_torus_a02_clean",
             ABCloudConfig(10, 10, [], 0.2, 1.0, "torus", 0.0, 96, "monumental")),
        ):
            ev = safe_eigvals(build_ab_cloud_hamiltonian(cfg))
            n = len(ev)
            print("%s: eig1=%.10f eigmid=%.10f eigend3=%.10f"
                  % (name, ev[0], ev[n // 2 - 1], ev[-1]))
        return 0

    sys.stderr.write("unknown command: %s\n" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main())
