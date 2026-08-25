#!/bin/sh
# Copy the canonical public site into the nginx html root.
set -eu
root="$(CDPATH= cd -- "$(dirname "$0")/../.." && pwd)"
mkdir -p "$root/deploy/vps/html"
cp "$root/docs/azm-deliverables/K-TA-7.1/tamia4life-site.html" \
  "$root/deploy/vps/html/index.html"
echo "wrote deploy/vps/html/index.html"
