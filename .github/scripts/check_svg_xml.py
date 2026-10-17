#!/usr/bin/env python3
"""Well-formedness gate: every tracked .svg/.xml/.xsd/.plist must parse
as XML (stdlib ElementTree). Catches hand-edit breakage in assets."""
import os
import sys
import xml.etree.ElementTree as ET

SKIP_DIRS = {".git", "node_modules", "site", ".ruff_cache", "__pycache__"}
EXTS = (".svg", ".xml", ".xsd", ".plist")
MAX_BYTES = 32 * (1 << 20)

bad = []
n = 0
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    for fn in sorted(filenames):
        if not fn.lower().endswith(EXTS):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p)
        try:
            if os.path.getsize(p) > MAX_BYTES:
                print(f"::warning file={rel}::skipped (too large)")
                continue
            n += 1
            ET.parse(p)
        except (ET.ParseError, OSError) as e:
            bad.append(rel)
            print(f"::error file={rel}::{type(e).__name__}: {e}")
print(f"parsed {n} XML-family files, {len(bad)} malformed")
sys.exit(1 if bad else 0)
