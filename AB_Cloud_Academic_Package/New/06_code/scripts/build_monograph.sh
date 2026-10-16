#!/usr/bin/env bash
# build the monograph PDFs + DOCX (pandoc + tectonic + docx-js pipeline)
set -euo pipefail
echo "-> PDF:  python3 /home/z/my-project/scripts/build_monograph_pdf.py (in the build environment)"
echo "-> DOCX: node /home/z/my-project/scripts/gen_monograph_docx.js ru|en"
echo "This script documents the pipeline; the artefacts ship pre-built in 01_monographs/."
