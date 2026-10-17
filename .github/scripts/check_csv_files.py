#!/usr/bin/env python3
"""Parse-validate every tracked CSV file (stdlib csv, delimiter sniffing).

Gate semantics (deliberate):
  * lines starting with `#` are comments (scientific preambles) — skipped;
  * genuine CSV syntax errors (unclosed quotes, decode failures) = ERROR;
  * ragged rows (field count differs from the first data row) = WARNING
    (legacy instrument outputs are data — they are flagged, not blocked).
"""
import csv
import io
import os
import sys

SKIP_DIRS = {".git", "node_modules", "site", ".ruff_cache", "__pycache__"}
MAX_BYTES = 64 * (1 << 20)

errors = []
warned = []
n = 0
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    for fn in sorted(filenames):
        if not fn.lower().endswith(".csv"):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p)
        try:
            if os.path.getsize(p) > MAX_BYTES:
                print(f"::warning file={rel}::skipped (>{MAX_BYTES >> 20} MB)")
                continue
            n += 1
            raw = open(p, "rb").read().decode("utf-8")
            lines = [ln for ln in raw.splitlines()
                     if ln.strip() and not ln.lstrip().startswith("#")]
            if not lines:
                continue
            sample = "\n".join(lines[:64])
            try:
                dialect = csv.Sniffer().sniff(sample)
            except csv.Error:
                dialect = csv.excel
            reader = csv.reader(io.StringIO("\n".join(lines)), dialect)
            header_cols = None
            ragged = 0
            for i, row in enumerate(reader, 1):
                if header_cols is None:
                    header_cols = len(row)
                elif len(row) != header_cols:
                    ragged += 1
            if ragged:
                warned.append(rel)
                print(f"::warning file={rel}::{ragged} ragged row(s) "
                      f"(header has {header_cols} fields) — legacy format, "
                      f"not blocking")
        except (csv.Error, UnicodeDecodeError, OSError) as e:
            errors.append(rel)
            print(f"::error file={rel}::{type(e).__name__}: {e}")
print(f"parsed {n} CSV files, {len(errors)} invalid, {len(warned)} ragged "
      f"(warned)")
sys.exit(1 if errors else 0)
