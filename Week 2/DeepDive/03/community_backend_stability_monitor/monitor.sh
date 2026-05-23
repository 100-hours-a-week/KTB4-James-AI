#!/usr/bin/env bash
set -euo pipefail
B=${1:-http://localhost:8203}
for e in "/ai/predict" "/ai/predict?mode=fail" "/db/write" "/db/write?mode=fail"; do
 c=$(curl -s -o /dev/null -w "%{http_code}" "$B$e")
 echo "$e -> $c"
done
