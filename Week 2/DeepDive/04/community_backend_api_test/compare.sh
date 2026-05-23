#!/usr/bin/env bash
set -euo pipefail
B=${1:-http://localhost:8204}
for i in {1..10}; do
  /usr/bin/time -f "%E" curl -s "$B/ai/chat" \
    -H "content-type: application/json" \
    -d '{"prompt":"hello"}' >/dev/null
done
