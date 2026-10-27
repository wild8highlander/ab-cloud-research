# Decision log

| # | Date | Decision | Rationale |
|---|---|---|---|
| D1 | 2026-10-14 | Unified edition replaces the legacy v23/v34 structure; no version numbers anywhere | the package is a living academic structure; editorial history replaces semver |
| D2 | 2026-10-14 | Heritage run archive referenced via provenance rows, not bulk-copied | 108 MB of run data would double the package; the sources remain canonical |
| D3 | 2026-10-14 | Monograph: full RU + EN; zh/de/es/fr/ar as faithful abstracts | scientific record must not rest on unreviewed machine translation of a full volume |
| D4 | 2026-10-14 | Numbers verbatim from verdict files; disagreements shown, not resolved | the sources themselves document convention differences; hiding them would be dishonest |
| D5 | 2026-10-14 | CLI in Python+Julia+Rust+Go+JS+Bash (no R/SQL yet) | matches the sources' verified stack; R/SQL are roadmap items |
| D6 | 2026-10-14 | Web lab is a single offline index.html | the honest default: no CDN, no telemetry, works from the ZIP |
