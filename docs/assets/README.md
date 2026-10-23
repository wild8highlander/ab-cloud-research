# 🎨 docs Assets

> **🧭 Navigation:** [docs/](../README.md) · [Root README](../../README.md)

<!-- enriched-r3 -->

This folder is the **visual-identity shelf** of its module: the logos, banners and small vector decorations that the module's README pages embed. Nothing here carries numerical content — the files are artwork and layout assets, referenced relatively by the surrounding documentation. The images are committed so that every README renders identically on GitHub, in a local clone, and inside the archived package.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `avatars.svg` | 4.1 KB | vector figure |
| `banner.svg` | 9.0 KB | vector figure |

The banner and avatar art of the **documentation site** README. Everything here is
hand-written SVG with SMIL animation (no build step, no external fonts,
view-source friendly) or exported raster logos; the READMEs embed it with
plain `<img>`/`<picture>` tags.

| File | What it is |
|---|---|
| `avatars.svg` | animated SVG art |
| `banner.svg` | animated SVG art |

> [!NOTE]
> Art only — no data, no code, no results. The READMEs that consume these
> files live one level up: [`../README.md`](../README.md). The ports subtree
> keeps its own separate family in
> [`../../meridian-spectral-observatory/ports/assets/`](../../meridian-spectral-observatory/ports/assets/).
