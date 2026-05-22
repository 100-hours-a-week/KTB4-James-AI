from __future__ import annotations

from collections.abc import Generator, Iterable
from pathlib import Path

from .models import Task


def iter_lines(path: Path) -> Generator[str, None, None]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def parse_tasks(lines: Iterable[str]) -> list[Task]:
    tasks: list[Task] = []
    for line in lines:
        if not line.strip():
            continue
        try:
            flag, title = line.split("|", maxsplit=1)
        except ValueError:
            continue
        tasks.append(Task(title=title, done=(flag == "1")))
    return tasks


def save_tasks(path: Path, tasks: list[Task]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for t in tasks:
            f.write(f"{'1' if t.done else '0'}|{t.title}\n")
