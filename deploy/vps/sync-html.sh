#!/bin/sh
# Copy the canonical public site into the nginx html root.
set -eu
root="$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)"
src="$root/docs/azm-deliverables/K-TA-7.1"
dest="$root/deploy/vps/html"
mkdir -p "$dest"
cp "$src/tamia4life-site.html" "$dest/index.html"
cp "$src/favicon.svg" "$src/favicon.ico" "$src/apple-touch-icon.png" "$dest/"
echo "wrote deploy/vps/html/index.html + favicon assets"
