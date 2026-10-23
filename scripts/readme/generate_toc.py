#!/usr/bin/env python3
"""TOC generator for large READMEs (>= 8 KB).
Only touches files that already contain TOC markers:
  <!-- TOC-START --> ... <!-- TOC-END -->
Regenerates a two-level TOC (H2 / H3) between the markers.
Run with --bootstrap to INSERT markers + TOC after the first H1 of large READMEs
that lack any TOC section (skips files that already contain a 'Table of Contents').
"""
import os, re, sys

REPO = os.environ.get("REPO_ROOT", ".")
START, END = "<!-- TOC-START -->", "<!-- TOC-END -->"
MIN_SIZE = 8000
SKIP_TOKENS = ("_source", "_original", "_template", "_documents")


def slugify_github(text):
    """GitHub-style anchor slug for a heading."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\- \u0400-\u04ff\u0370-\u03ff\u4e00-\u9fff]", "", text)
    return text.replace(" ", "-")


def heading_label(line):
    return line.lstrip("#").strip()


def collect(lines):
    in_code = False
    items = []
    for ln in lines:
        if ln.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^(#{2,3})\s+(?!#)(.+)$", ln)
        if m:
            level, txt = len(m.group(1)), heading_label(m.group(2))
            items.append((level, txt, slugify_github(txt)))
    return items


def render(items):
    if not items:
        return None
    out = ["- [Top](#)"] if False else []
    for level, txt, slug in items:
        indent = "" if level == 2 else "  "
        out.append(f"{indent}- [{txt}](#{slug})")
    return "\n".join(out)


def process(path, bootstrap=False):
    with open(path, encoding="utf-8", errors="replace") as f:
        src = f.read()
    rel = os.path.relpath(path, REPO).replace(os.sep, "/")

    if START in src and END in src:
        pre = src.split(START, 1)[0]
        body_lines = src.split(START, 1)[1].split(END, 1)[1].splitlines()
        toc = render(collect(body_lines))
        if toc is None:
            print(f"[skip] {rel}: no headings found")
            return False
        new = pre + START + "\n" + toc + "\n" + END + src.split(END, 1)[1]
        if new != src:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new)
            print(f"[regen] {rel}")
            return True
        print(f"[same] {rel}")
        return False

    if not bootstrap:
        return False
    if os.path.getsize(path) < MIN_SIZE:
        return False
    if re.search(r"table of contents", src, re.I):
        print(f"[skip] {rel}: already has a TOC section")
        return False
    lines = src.splitlines()
    h1_idx = next((i for i, ln in enumerate(lines) if ln.startswith("# ")), None)
    if h1_idx is None:
        print(f"[skip] {rel}: no H1")
        return False
    toc = render(collect(lines))
    if toc is None:
        return False
    insert_at = h1_idx + 1
    block = ["", START, toc, END, ""]
    lines[insert_at:insert_at] = block
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[bootstrap] {rel}")
    return True


def main():
    bootstrap = "--bootstrap" in sys.argv
    changed = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "site", "dist")]
        for fn in files:
            lf = fn.lower()
            if not (lf.startswith("readme") and lf.endswith(".md")):
                continue
            if any(t in lf for t in SKIP_TOKENS):
                continue
            p = os.path.join(root, fn)
            if os.path.getsize(p) < MIN_SIZE:
                continue
            changed += bool(process(p, bootstrap))
    print(f"readme-toc: {changed} file(s) updated")


if __name__ == "__main__":
    main()
