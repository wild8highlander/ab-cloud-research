#!/usr/bin/env python3
"""Marker -> raw.githubusercontent.com URL injector.
Replaces single-line markers in README files:
    <!-- BANNER:key -->   ->  <img src="<raw>/assets/banners/<key>.webp" ... />
    <!-- ICON:key -->     ->  <img src="<raw>/assets/icons/<key>.png" ... />
    <!-- SVG:key -->      ->  <img src="<raw>/assets/svg/<key>.svg" ... />
where <raw> = https://raw.githubusercontent.com/<owner>/<repo>/<branch>.
`key` resolution: exact manifest key, or section name (banner-<key>), or file
stem. Markers whose key cannot be resolved are reported and left untouched.
Commit is handled by the calling workflow (readme-inject.yml).
"""
import json, os, re, sys

REPO = os.environ.get("REPO_ROOT", ".")
OWNER_REPO = os.environ.get("INJECT_OWNER_REPO", "wild8highlander/ab-cloud-research")
BRANCH = os.environ.get("INJECT_BRANCH", "main")

MARK = re.compile(r"^\s*<!--\s*(BANNER|ICON|SVG):([\w.\-]+)\s*-->\s*$", re.M)


def load_manifest():
    with open(os.path.join(REPO, "assets", "manifest.json"), encoding="utf-8") as f:
        return json.load(f)


def resolve(man, kind, key):
    """Return repo-relative asset path or None."""
    candidates = []
    if kind == "BANNER":
        candidates = [f"assets/banners/{key}.webp", f"assets/banners/banner-{key}.webp",
                      f"assets/banners/{key}"]
    elif kind == "ICON":
        candidates = [f"assets/icons/{key}.png", f"assets/icons/icon-{key}.png"]
    elif kind == "SVG":
        candidates = [f"assets/svg/{key}.svg"]
    for c in candidates:
        if os.path.exists(os.path.join(REPO, c)):
            return c
    # manifest lookup fallback
    blob = json.dumps(man)
    for tok in re.findall(r'"(assets/[^"]+?)"', blob):
        if key in tok:
            return tok
    return None


def main():
    man = load_manifest()
    base = f"https://raw.githubusercontent.com/{OWNER_REPO}/{BRANCH}"
    changed = 0
    unresolved = []

    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "site", "dist")]
        for fn in files:
            lf = fn.lower()
            if not (lf.startswith("readme") and lf.endswith(".md")):
                continue
            p = os.path.join(root, fn)
            src = open(p, encoding="utf-8", errors="replace").read()
            found = list(MARK.finditer(src))
            if not found:
                continue
            rel = os.path.relpath(p, REPO).replace(os.sep, "/")
            out, last = [], 0
            miss = False
            for m in found:
                kind, key = m.group(1), m.group(2)
                target = resolve(man, kind, key)
                if target is None:
                    miss = True
                    unresolved.append(f"{rel}: {kind}:{key}")
                    continue
                alt = os.path.basename(target).replace("-", " ").replace(".", " ")
                out.append(src[last:m.start()])
                out.append(f'<img src="{base}/{target}" alt="{alt}" width="100%"/>')
                last = m.end()
            if miss:
                continue  # leave file untouched until all keys resolve
            out.append(src[last:])
            new = "".join(out)
            if new != src:
                open(p, "w", encoding="utf-8").write(new)
                print(f"[inject] {rel}: {len(found)} marker(s)")
                changed += 1

    if unresolved:
        print("readme-inject: unresolved markers (left untouched):")
        for u in unresolved:
            print("  ?", u)
    print(f"readme-inject: {changed} file(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
