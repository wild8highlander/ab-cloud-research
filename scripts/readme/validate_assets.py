#!/usr/bin/env python3
"""Asset optimizer + validator.

optimize mode (--optimize):
  For every PNG under assets/ larger than 150 KB with no sibling WebP —
  write a quality-82 WebP next to it (PNG kept as source of truth).

validate mode (default):
  1. manifest.json: every referenced file exists.
  2. every file under managed asset dirs (banners, icons, backgrounds, og,
     avatar, svg) is referenced by manifest.json (orphan check).
  3. weight limits per STYLE_GUIDE §6 (banner <=200 KB, hero <=250 KB).
"""
import json, os, sys

REPO = os.environ.get("REPO_ROOT", ".")
ASSETS = os.path.join(REPO, "assets")
MANAGED = ("banners", "icons", "backgrounds", "og", "avatar", "svg")
LIMITS = {"hero-main.webp": 250 * 1024}
DEFAULT_LIMIT = 200 * 1024
PNG_TO_WEBP_ABOVE = 150 * 1024


def optimize():
    from PIL import Image
    converted = 0
    for root, _, files in os.walk(ASSETS):
        for fn in files:
            if not fn.endswith(".png"):
                continue
            p = os.path.join(root, fn)
            if os.path.getsize(p) < PNG_TO_WEBP_ABOVE:
                continue
            out = p[:-4] + ".webp"
            if os.path.exists(out):
                continue
            Image.open(p).convert("RGB").save(out, "WEBP", quality=82, method=6)
            print(f"[webp] {os.path.relpath(p, REPO)} -> {os.path.relpath(out, REPO)} "
                  f"({os.path.getsize(out) // 1024} KB)")
            converted += 1
    print(f"assets-optimize: {converted} file(s) converted")


def referenced_files(man):
    refs = set()
    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, str) and ("assets/" in x):
            parts = x.split()
            for tok in parts:
                tok = tok.strip(',*"\'')
                if tok.startswith("assets/"):
                    refs.add(tok)
    walk(man)
    return refs


def validate():
    ok = True
    man_path = os.path.join(ASSETS, "manifest.json")
    if not os.path.exists(man_path):
        print("assets-validate: manifest.json missing"); return False
    with open(man_path, encoding="utf-8") as f:
        man = json.load(f)
    refs = referenced_files(man)

    missing = [r for r in refs if not os.path.exists(os.path.join(REPO, r))]
    for m in missing:
        print(f"  ✗ manifest references missing file: {m}")
        ok = False

    actual = set()
    for d in MANAGED:
        dp = os.path.join(ASSETS, d)
        if not os.path.isdir(dp):
            continue
        for root, _, files in os.walk(dp):
            for fn in files:
                rel = os.path.relpath(os.path.join(root, fn), REPO).replace(os.sep, "/")
                actual.add(rel)

    orphans = sorted(actual - refs)
    for o in orphans:
        print(f"  ✗ orphan asset (not in manifest.json): {o}")
        ok = False

    for rel in sorted(actual):
        if rel.endswith(".webp"):
            size = os.path.getsize(os.path.join(REPO, rel))
            limit = LIMITS.get(os.path.basename(rel), DEFAULT_LIMIT)
            if size > limit:
                print(f"  ✗ {rel}: {size // 1024} KB exceeds limit {limit // 1024} KB")
                ok = False

    print(f"assets-validate: {len(refs)} manifest refs, {len(actual)} managed files")
    if ok:
        print("assets-validate: OK ✓")
    return ok


if __name__ == "__main__":
    sys.exit(0 if (optimize() if "--optimize" in sys.argv else validate()) else 1)
