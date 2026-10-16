# Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `pytest 09_tests/python` fails on i18n parity | a message key exists in RU but not EN (or vice versa) | add the missing key to both `06_code/shared/i18n/{ru,en}.json` |
| `pytest` fails on checksums | a data file was modified after `checksums.sha256` was written | re-run `python3 06_code/scripts/update_checksums.py` and commit both |
| `tectonic` fails on the monograph .tex | missing package on cold start (first run downloads) | re-run; ensure network access on first compile |
| Cyrillic shows as boxes in the PDF | the viewer, not the file — Liberation fonts are embedded | open in a PDF viewer with embedded-font support (any modern viewer) |
| DOCX TOC shows no page numbers | field codes need a refresh | open in Word/WPS → right-click the TOC → «Update Field» |
| Web lab opens blank | file:// restrictions in some browsers | use `python3 -m http.server` in `07_web_lab/` and open the local URL |
| `./run.sh` not executable | clone lost the exec bit | `chmod +x 06_code/cli/run.sh` |
| Julia runner exits on `LinearAlgebra` | Julia < 1.10 | use Julia ≥ 1.10 |
| Rust runner: `cargo run` offline | crates.io access needed once | build with network once, then `--offline` works |
| Streamlit not installed | optional dependency | `pip install streamlit` or use the static `index.html` instead |
| Numbers differ from the README table | you are looking at a different campaign's variant | every number names its campaign — check `05_logs/metrics.json` first |

## Golden rule

Before debugging further: run `python3 06_code/python/run.py doctor` — it
checks the environment, the config schema, the data checksums and the
package structure in one pass.
