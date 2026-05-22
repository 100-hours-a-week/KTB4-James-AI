from __future__ import annotations

from pathlib import Path


def parse_metrics(path: Path) -> dict[str, float]:
    data: dict[str, float] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        for token in line.split():
            if "=" in token:
                k, v = token.split("=", maxsplit=1)
                try:
                    data[k] = float(v)
                except ValueError:
                    pass
    return data


def main() -> None:
    m = parse_metrics(Path("benchmark_result.txt"))
    print("=== Memory/Time Monitor ===")
    for key in ["log_size", "sync_elapsed", "sync_mem_kb", "gen_elapsed", "gen_mem_kb"]:
        print(f"{key}: {m.get(key, -1)}")


if __name__ == "__main__":
    main()
