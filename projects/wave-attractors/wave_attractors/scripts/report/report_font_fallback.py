"""report_font_fallback.py — font-fallback hook for the W1 report build.

The original document pipeline used a monkey-patch of ``Paragraph.__init__``
that remapped glyphs missing from the primary font onto fallback fonts.
The W1 report body uses only the FreeSerif family (Latin / Cyrillic / Greek
plus common math operators) and the DejaVu mono face for code, all of which
are registered explicitly by ``w1_report_build.py``; the patch is therefore
not required. This module keeps the same import surface so the build script
stays drop-in compatible, and documents where to plug a real fallback chain
if new scripts or symbols are ever added.
"""


def install_font_fallback():
    """No-op fallback installer (idempotent, safe to call repeatedly).

    To enable real glyph remapping, replace the body of this function with a
    monkey-patch of ``reportlab.platypus.Paragraph.__init__`` that walks a
    ``FONT_FALLBACK_CHAIN = {'FreeSerif': [...], ...}`` mapping and rewrites
    characters not present in the base font with tags of a fallback font.
    """
    return None
