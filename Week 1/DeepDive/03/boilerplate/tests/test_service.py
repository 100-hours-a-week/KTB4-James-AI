from collab_app.infrastructure import InMemoryRepo
from collab_app.service import fetch_open_tasks


def test_fetch_open_tasks() -> None:
    tasks = fetch_open_tasks(InMemoryRepo())
    assert len(tasks) == 1
    assert tasks[0].title == "type hint"
