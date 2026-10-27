# scripts/readme — README toolkit

Build and lint pipeline for the repository's README system: the root README,
every project landing page and the auto-enriched section headers.

| Script | Role |
|---|---|
| `lint_readme.py` | structural lint of the root README (sections, badge rows, anchor targets) |
| `enrich_sections.py` | injects the `AB-ENRICHED:v1` section headers (capsule banners + typing SVG) into section landing pages |
| `enrich_sub_readmes.py` | same enrichment pass for per-directory READMEs (colour map per project) |
| `generate_toc.py` | regenerates the table of contents block |
| `inject_urls.py` | rewrites absolute artifact URLs (Zenodo/DOI) into the citation blocks |
| `gen_images.py` / `make_svg_assets.py` | render dividers, banners and avatar sheets used by the enriched headers |
| `process_images.py` / `validate_assets.py` | normalise and validate every referenced image (size, format, alt text) |
| `update_badges.py` | refreshes the badge row (counts, versions) |
| `make-gif.sh` | assembles the animation GIFs from frame dumps |

Run the linter after any README edit: `python3 scripts/readme/lint_readme.py`.
The curated markdown surface for CI lives in `.markdownlint-cli2.jsonc`.
