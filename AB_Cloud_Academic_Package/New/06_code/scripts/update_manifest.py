#!/usr/bin/env python3
"""Regenerate 00_meta/manifest.json (structure + counts)."""
import json, os

PKG = os.environ.get("AB_CLOUD_ROOT",
                     os.path.join(os.path.dirname(__file__), "..", ".."))
MAN = os.path.join(PKG, "00_meta", "manifest.json")

m = json.load(open(MAN, encoding="utf-8"))
m["generated"] = "auto"
for sec in m["structure"]["sections"]:
    p = os.path.join(PKG, sec)
    n = sum(len(f) for _, _, f in os.walk(p)) if os.path.isdir(p) else 0
    m["structure"].setdefault("counts", {})[sec] = n
with open(MAN, "w", encoding="utf-8") as f:
    json.dump(m, f, indent=2, ensure_ascii=False)
print("manifest updated:", {k: v for k, v in m["structure"].get("counts", {}).items()})
