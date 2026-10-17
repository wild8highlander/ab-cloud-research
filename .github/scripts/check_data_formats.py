#!/usr/bin/env python3
"""Parse-validate every tracked JSON and TOML file in the repository.

Catches malformed registry/metadata/config files at the PR stage. Exits 1
with GitHub annotations on the first pass over all failures (not fail-fast).
"""
import json
import os
import subprocess
import sys
import tomllib

SKIP_DIRS = {".git", "node_modules", "site", ".ruff_cache", "__pycache__", ".venv"}

bad = []
n_json = n_toml = 0
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    for fn in sorted(filenames):
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p)
        try:
            if fn.endswith(".json"):
                n_json += 1
                json.load(open(p, encoding="utf-8"))
            elif fn.endswith(".toml"):
                n_toml += 1
                tomllib.load(open(p, "rb"))
        except Exception as e:  # noqa: BLE001 — report every parse failure
            msg = f"{type(e).__name__}: {e}"
            bad.append((rel, msg))
            print(f"::error file={rel}::{msg[:200]}")

print(f"parsed {n_json} JSON + {n_toml} TOML files, {len(bad)} invalid")
if bad:
    sys.exit(1)

# Bonus: validate the shell scripts' syntax (bash -n) — cheap and catches typos.
n_sh = 0
bad_sh = []
for dirpath, dirnames, filenames in os.walk("."):
    dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
    for fn in sorted(filenames):
        if not fn.endswith(".sh"):
            continue
        p = os.path.join(dirpath, fn)
        n_sh += 1
        r = subprocess.run(["bash", "-n", p], capture_output=True, text=True)
        if r.returncode != 0:
            bad_sh.append(p)
            print(f"::error file={p}::{r.stderr.strip()[:200]}")
print(f"bash -n over {n_sh} shell scripts, {len(bad_sh)} invalid")
sys.exit(1 if bad_sh else 0)
