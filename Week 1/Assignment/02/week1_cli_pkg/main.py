from __future__ import annotations

from pathlib import Path

from .models import Task
from .storage import iter_lines, parse_tasks, save_tasks


def show(tasks: list[Task]) -> None:
    if not tasks:
        print("등록된 할 일이 없습니다.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. [{'완료' if t.done else '진행중'}] {t.title}")


def run() -> None:
    data_path = Path("tasks.txt")
    tasks = parse_tasks(iter_lines(data_path)) if data_path.exists() else []

    while True:
        print("\n1) 추가 2) 조회 3) 완료 4) 종료")
        cmd = input("선택: ").strip()

        if cmd == "1":
            title = input("제목: ").strip()
            if not title:
                print("빈 제목 불가")
                continue
            tasks.append(Task(title=title))
        elif cmd == "2":
            show(tasks)
        elif cmd == "3":
            show(tasks)
            raw = input("번호: ").strip()
            try:
                i = int(raw)
                if i < 1 or i > len(tasks):
                    raise IndexError
                tasks[i - 1].done = True
            except ValueError:
                print("숫자 필요")
            except IndexError:
                print("범위 오류")
        elif cmd == "4":
            save_tasks(data_path, tasks)
            print("저장 후 종료")
            break
        else:
            print("1~4 중 선택")
