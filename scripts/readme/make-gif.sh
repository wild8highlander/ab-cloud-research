#!/usr/bin/env bash
# make-gif.sh — convert an AI-generated video clip (mp4/mov/webm) into a
# seamless-looping animated WebP for README embedding (GitHub-native).
# Usage: scripts/readme/make-gif.sh clip.mp4 [output.webp] [width]
set -euo pipefail

IN="${1:?usage: make-gif.sh clip.mp4 [output.webp] [width]}"
OUT="${2:-${IN%.*}.webp}"
WIDTH="${3:-1280}"

command -v ffmpeg >/dev/null || { echo "ffmpeg not found"; exit 1; }

ffmpeg -y -i "$IN" -vf "fps=24,scale=${WIDTH}:-1:flags=lanczos" \
  -c:v libwebp -lossless 0 -q:v 70 -loop 0 -preset picture -an -vsync 0 "$OUT"

SIZE=$(du -k "$OUT" | cut -f1)
echo "✔ ${OUT} (${SIZE} KB)"
# STYLE_GUIDE §6: keep README gifs under ~1000 KB; if larger, lower -q:v or WIDTH.
if [ "$SIZE" -gt 1000 ]; then
  echo "⚠ exceeds 1000 KB — re-run with a smaller width or lower quality:"
  echo "  scripts/readme/make-gif.sh $IN $OUT 960   # and/or edit -q:v (e.g. 55)"
fi
