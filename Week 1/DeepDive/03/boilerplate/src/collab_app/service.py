from .domain import Task, TaskRepository


def fetch_open_tasks(repo: TaskRepository) -> list[Task]:
    rows = repo.load()
    result: list[Task] = []
    for row in rows:
        if not row["done"]:
            result.append(Task(id=row["id"], title=row["title"], done=row["done"]))
    return result
