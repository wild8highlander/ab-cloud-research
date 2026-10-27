#!/usr/bin/env python3
"""Refresh (or verify) 02_data/checksums.sha256."""
import hashlib, os, sys

PKG = os.environ.get("AB_CLOUD_ROOT",
                     os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(PKG, "02_data")
OUT = os.path.join(DATA, "checksums.sha256")

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    verify_only = "--verify-only" in sys.argv
    lines = []
    for root, dirs, files in os.walk(DATA):
        dirs.sort(); files.sort()
        for fn in files:
            if fn.startswith("checksums."):
                continue
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, DATA)
            lines.append(f"{sha256(full)}  {rel}")
    if verify_only:
        current = {rel: h for h, rel in
                   (l.split("  ", 1) for l in lines if "  " in l)}
        old = {}
        if os.path.exists(OUT):
            for l in open(OUT, encoding="utf-8").read().splitlines():
                if "  " in l:
                    h, p = l.split("  ", 1)
                    old[p] = h
        bad = [p for p, h in old.items() if current.get(p) != h]
        if bad:
            print("CHECKSUM MISMATCH:", *bad, sep="\n  ")
            sys.exit(1)
        print(f"checksums verified: {len(old)} files OK")
    else:
        with open(OUT, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"checksums written: {len(lines)} files")

if __name__ == "__main__":
    main()
