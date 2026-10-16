# -*- coding: utf-8 -*-
"""One-shot extraction of the embedded ζ-zero tables from the Julia sources.

Parses the `const ZETA_ZEROS = Float64[...]` literal in RH_Sweep_Pro.jl
(13 661 verified zeros, source lines 830-4245) and the
`const ZETA_ZEROS_EMBEDDED = Float64[...]` literal in RH_Unified_v5.jl
(500 zeros, source lines 795-1080), and writes them one-per-line at full
printed precision into ports/python/abcloud/data/.

Run once from the meridian-spectral-observatory directory:
    python3 ports/python/extract_rh_zeros.py
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # meridian-spectral-observatory/
OUT_DIR = os.path.join(HERE, "abcloud", "data")

TOKEN_RE = re.compile(r"-?\d+\.\d+(?:[eE][+-]?\d+)?")


def extract(jl_path, const_name, expected_count, out_name):
    start_pat = "const %s = Float64[" % const_name
    text = None
    with open(jl_path, "r", encoding="utf-8") as f:
        src = f.read()
    i = src.find(start_pat)
    if i < 0:
        raise RuntimeError("declaration not found for %s in %s" % (const_name, jl_path))
    j = src.index("[", i) + 1
    k = src.index("]", j)  # first closing bracket ends the literal
    text = src[j:k]
    # Strip Julia comments just in case
    text = re.sub(r"#[^\n]*", " ", text)
    tokens = TOKEN_RE.findall(text)
    if len(tokens) != expected_count:
        raise RuntimeError("%s: expected %d zeros, found %d"
                           % (const_name, expected_count, len(tokens)))
    vals = [float(t) for t in tokens]
    if any(b <= a for a, b in zip(vals, vals[1:])):
        raise RuntimeError("%s: zeros are not strictly increasing" % const_name)

    out_path = os.path.join(OUT_DIR, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        for t in tokens:
            f.write(t + "\n")
    print("%-28s n=%d  first=%s  last=%s  -> %s"
          % (out_name, len(vals), tokens[0], tokens[-1], out_path))
    return vals


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    sp = extract(os.path.join(ROOT, "RH_Sweep_Pro.jl"),
                 "ZETA_ZEROS", 13661, "rh_embedded_zeros_sp.txt")
    v5 = extract(os.path.join(ROOT, "RH_Unified_v5.jl"),
                 "ZETA_ZEROS_EMBEDDED", 500, "rh_embedded_zeros_v5.txt")
    # sanity: the v5 table must agree with the first 500 SP zeros
    max_dev = max(abs(a - b) for a, b in zip(sp[:500], v5))
    print("cross-check max|SP[:500] - v5| = %.3e" % max_dev)
    if max_dev > 1e-12:
        sys.exit("cross-check FAILED")
    print("OK")


if __name__ == "__main__":
    main()
