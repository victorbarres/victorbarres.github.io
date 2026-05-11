#!/usr/bin/env bash
# build_cv.sh — build the CV PDF and publish it to assets/pdf/.
#
# Run from anywhere; resolves paths relative to this script.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SRC_DIR="$REPO_ROOT/cv-src"
OUT_PDF="$REPO_ROOT/assets/pdf/barres_cv.pdf"

cd "$SRC_DIR"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk not found. Install MacTeX or run 'brew install --cask mactex-no-gui'." >&2
  exit 1
fi

echo "Building CV..."
latexmk -xelatex -interaction=nonstopmode -halt-on-error barres_cv.tex >/dev/null

echo "Publishing to $OUT_PDF"
mkdir -p "$(dirname "$OUT_PDF")"
cp barres_cv.pdf "$OUT_PDF"

echo "Done. Pages: $(mdls -name kMDItemNumberOfPages "$OUT_PDF" | awk '{print $3}'), size: $(ls -lh "$OUT_PDF" | awk '{print $5}')"
