# `fonts/` — Web Fonts of the Cover Design
> The Inter and Playfair Display font families (40 @font-face declarations, WOFF2) plus the stylesheets that bind them to the cover-design HTML.

_Location: [unpacked/](../README.md) › [fonts/](README.md)_

The package's PDF cover — the first page of the monograph, the preprints and the Academic Essence — is produced from an HTML/CSS design source shipped at the package root (`cover_design_source.html`, described in [`../README.md`](../README.md)). That design references two Google-font families, and this folder ships the actual font binaries together with the stylesheets so that the cover renders identically on any machine, **offline, with no network dependency**. The families are:

| Family | Role in the design | Files |
|---|---|---|
| **Playfair Display** | The display serif for titles and the package name — the high-contrast Didone-style face that gives the cover its typographic voice. | `nuFiD-vYSZviVYUb_rj3ij__anPXDT*.woff2` (4 files, Latin + extended subsets) |
| **Inter** | The workhorse sans for metadata, author block, DOI and labels. | `UcC73FwrK3iLTeHuS_nVMrMxCp50SjI*.woff2` (7 files, Latin + Cyrillic + extended subsets) |

The WOFF2 filenames are the original Google Fonts subset hashes; the package preserves them so the CSS `url()` references resolve without renaming. Inter's subsets include the **Cyrillic** range, which the bilingual (EN + RU) elements of the design require. Together the folder carries 11 font binaries and 40 `@font-face` declarations across the two stylesheets.

## The stylesheets

`fonts.css` is the stylesheet generated alongside the design (Google Fonts download format): it declares every face with its `unicode-range` so the browser loads only the subsets actually used. `fonts_local.css` is the localised variant that rewrites the font URLs to relative paths — this is the file `cover_design_source.html` links, and the reason the design works from a plain `file://` open with no internet connection. If you re-render the cover (open the HTML in a browser and print to PDF at A4), keep this folder next to the HTML file and the typography will match the shipped PDFs exactly.

## Complete contents inventory

| File | Size | Description |
|---|---|---|
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa0ZL7SUc.woff2` | 18.3 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7.woff2` | 47.1 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1pL7SUc.woff2` | 18.6 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa25L7SUc.woff2` | 83.1 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2JL7SUc.woff2` | 25.4 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2ZL7SUc.woff2` | 11.0 KB | WOFF2 web-font binary (subset). |
| `UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa2pL7SUc.woff2` | 10.0 KB | WOFF2 web-font binary (subset). |
| `fonts.css` | 14.5 KB · 360 lines | Generated stylesheet declaring all 40 @font-face entries of the Inter and Playfair Display families with their unicode ranges. |
| `fonts_local.css` | 12.9 KB · 360 lines | The localised stylesheet (relative font URLs) linked by cover_design_source.html — enables fully offline cover rendering. |
| `nuFiD-vYSZviVYUb_rj3ij__anPXDTLYgFE_.woff2` | 20.6 KB | WOFF2 web-font binary (subset). |
| `nuFiD-vYSZviVYUb_rj3ij__anPXDTPYgFE_.woff2` | 8.9 KB | WOFF2 web-font binary (subset). |
| `nuFiD-vYSZviVYUb_rj3ij__anPXDTjYgFE_.woff2` | 20.7 KB | WOFF2 web-font binary (subset). |
| `nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgA.woff2` | 37.5 KB | WOFF2 web-font binary (subset). |

---
_This README is part of the GitHub edition of the AB-Cloud v23 package (v34). Package overview: [../README.md](../README.md)._