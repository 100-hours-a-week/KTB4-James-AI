#!/usr/bin/env bash
set -euo pipefail

SIZE="${1:-200000}"
OUT="${2:-benchmark_result.txt}"

python3 - <<PY
from pathlib import Path
n = int(${SIZE})
p = Path('sample_large.log')
with p.open('w', encoding='utf-8') as f:
    for i in range(n):
        level = 'ERROR' if i % 10 == 0 else 'INFO'
        f.write(f"{i} {level} message\\n")
print(p)
PY

/usr/bin/time -f "sync_elapsed=%e sync_mem_kb=%M" python3 ../../Assignment/01/cli_study_tracker.py >/dev/null 2>sync.time || true
/usr/bin/time -f "gen_elapsed=%e gen_mem_kb=%M" python3 -m week1_cli_pkg.main >/dev/null 2>gen.time || true

{
  echo "log_size=$SIZE"
  cat sync.time
  cat gen.time
} > "$OUT"

echo "saved: $OUT"
