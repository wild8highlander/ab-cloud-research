# -*- coding: utf-8 -*-
"""Extract the embedded 1000 Riemann zeta zeros from AB_Cloud_Monumental_v6_3.jl.

One-off provenance script (sibling of extract_rh_zeros.py): parses the
``const _ZETA_ZEROS_1000 = Float64[...]`` block (Julia L491-1492) and writes
one value per line, FULL printed precision, to

    ports/data/monumental_zeta_zeros_1000.txt

Run from anywhere:  python3 extract_monumental_zeros.py
"""

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_JULIA_SRC = os.path.join(
    _HERE, "..", "..", "AB_Cloud_Monumental_v6_3.jl")
_OUT = os.path.join(_HERE, "..", "data", "monumental_zeta_zeros_1000.txt")

_VAL = re.compile(r"^\s*(-?\d+\.\d+(?:[eE][-+]?\d+)?)\s*,?\s*$")


def main() -> int:
    with open(_JULIA_SRC, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    # Locate the const block.
    start = end = None
    for i, ln in enumerate(lines):
        if "_ZETA_ZEROS_1000 = Float64[" in ln:
            start = i + 1
        elif start is not None and ln.strip() == "]":
            end = i
            break
    if start is None or end is None:
        print("ERROR: _ZETA_ZEROS_1000 block not found")
        return 1
    vals = []
    for ln in lines[start:end]:
        m = _VAL.match(ln)
        if m:
            vals.append(m.group(1))
        elif ln.strip():
            print("WARNING: unparsed line %d: %r" % (i + 1, ln))
    if len(vals) != 1000:
        print("ERROR: expected 1000 zeros, parsed %d" % len(vals))
        return 1
    os.makedirs(os.path.dirname(os.path.abspath(_OUT)), exist_ok=True)
    with open(_OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(vals) + "\n")
    print("wrote %d zeros -> %s" % (len(vals), os.path.abspath(_OUT)))
    print("first 3:", vals[:3])
    print("last 3:", vals[-3:])
    return 0


if __name__ == "__main__":
    sys.exit(main())
