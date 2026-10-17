#!/usr/bin/env python3
"""Workflow trigger sanity: every .github/workflows/*.yml must parse,
declare an `on:` trigger, and include `main` in every push/pull_request
branch filter that uses a list. Catches silently-dead CI (e.g. a typo in
a branch name)."""
import glob
import os
import sys

try:
    import yaml
except ImportError:
    print("::error::PyYAML is required (pip install pyyaml)")
    sys.exit(1)

bad = 0
n = 0
for path in sorted(glob.glob(".github/workflows/*.y*ml")):
    n += 1
    try:
        doc = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"::error file={path}::YAML parse error: {e}")
        bad += 1
        continue
    if not isinstance(doc, dict) or not (True in doc or "on" in doc):
        # PyYAML parses bare `on:` as boolean True
        print(f"::error file={path}::no 'on:' trigger section found")
        bad += 1
        continue
    trig = doc.get(True, doc.get("on", {})) or {}
    if not isinstance(trig, dict):
        continue
    for ev in ("push", "pull_request"):
        cfg = trig.get(ev)
        if not isinstance(cfg, dict):
            continue
        branches = cfg.get("branches")
        if branches is None:
            continue
        if isinstance(branches, str):
            branches = [branches]
        if isinstance(branches, list) and "main" not in branches:
            print(f"::error file={path}::{ev}.branches {branches} does not "
                  f"include 'main' — the workflow would never run on main")
            bad += 1
print(f"workflow-triggers: checked {n} workflow(s), {bad} problem(s)")
sys.exit(1 if bad else 0)
