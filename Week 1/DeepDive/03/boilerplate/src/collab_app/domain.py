from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, TypedDict


class RawTask(TypedDict):
    id: int
    title: str
    done: bool


@dataclass
class Task:
    id: int
    title: str
    done: bool


class TaskRepository(Protocol):
    def load(self) -> list[RawTask]: ...
