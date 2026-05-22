from .domain import RawTask


class InMemoryRepo:
    def load(self) -> list[RawTask]:
        return [
            {"id": 1, "title": "type hint", "done": False},
            {"id": 2, "title": "review", "done": True},
        ]
