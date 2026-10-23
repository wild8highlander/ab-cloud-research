# 🎨 Observatory Assets

> **🧭 Navigation:** [meridian-spectral-observatory/](../README.md) · [Root README](../../README.md)

<!-- enriched-r3 -->

This folder is the **visual-identity shelf** of its module: the logos, banners and small vector decorations that the module's README pages embed. Nothing here carries numerical content — the files are artwork and layout assets, referenced relatively by the surrounding documentation. The images are committed so that every README renders identically on GitHub, in a local clone, and inside the archived package.

## Folder contents

| File | Size | What it is |
|---|---|---|
| `banner_dark.svg` | 24 KB | vector figure |
| `banner_light.svg` | 24 KB | vector figure |

The animated banner art of the meridian-spectral-observatory landing pages.

| File | Used by |
|---|---|
| [`banner_dark.svg`](banner_dark.svg) | [`../README.md`](../README.md) — dark color-scheme variant |
| [`banner_light.svg`](banner_light.svg) | the same pages — light color-scheme variant |

The two files share one drawing: the critical line Re(s)=½ with rising ζ zeros,
an AB-cloud lattice with flux vortices, the GUE spacing density and the
meridian compass; the dark/light pair is switched by the `<picture>` element
with `prefers-color-scheme` in the READMEs. Both are hand-written SVG with
SMIL animation — no build step, no external fonts, view-source friendly.

> [!NOTE]
> The ports subtree keeps its own, separate banner family in
> [`ports/assets/`](../ports/assets/) (terminal + four language seals).

Landing page: [`../README.md`](../README.md)
