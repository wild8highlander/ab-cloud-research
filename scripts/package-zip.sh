#!/bin/bash
# package-zip.sh — build the deliverable ZIP from the working repo state.
set -euo pipefail
REPO=/home/z/work/ab-cloud-research
OUT=/home/z/my-project/download/ab-cloud-web-improvements.zip

cd "$REPO"
rm -f "$OUT"

# All modified + untracked files (tracked changes only), excluding the
# gitignored root dist/ (added separately below) and dist-docs/ (CI builds it).
git status --short | awk '
  $1 == "M"  { print $2 }
  $1 == "??" { print $2 }
' | grep -v '^dist-docs/$' > /tmp/zip-files.txt

# New files under untracked directories are listed as dirs by git status;
# expand them.
: > /tmp/zip-paths.txt
while IFS= read -r p; do
  if [ -d "$p" ]; then
    find "$p" -type f >> /tmp/zip-paths.txt
  else
    echo "$p" >> /tmp/zip-paths.txt
  fi
done < /tmp/zip-files.txt

# The rebuilt portal bundle (gitignored, but ships so the user needs no Node).
find dist -type f >> /tmp/zip-paths.txt

sort -u /tmp/zip-paths.txt > /tmp/zip-paths-final.txt
echo "files in zip: $(wc -l < /tmp/zip-paths-final.txt)"
zip -q "$OUT" -@ < /tmp/zip-paths-final.txt
ls -la "$OUT"
unzip -l "$OUT" | tail -3
