from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


def print_menu() -> None:
    print("\n=== Study Tracker ===")
    print("1) 할 일 추가")
    print("2) 할 일 목록")
    print("3) 완료 처리")
    print("4) 종료")


def show_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("등록된 할 일이 없습니다.")
        return
    for idx, task in enumerate(tasks, start=1):
        state = "완료" if task.done else "진행중"
        print(f"{idx}. [{state}] {task.title}")


def mark_done(tasks: list[Task], raw_index: str) -> None:
    try:
        index = int(raw_index)
    except ValueError:
        print("숫자를 입력해주세요.")
        return

    if index < 1 or index > len(tasks):
        print("존재하지 않는 번호입니다.")
        return

    tasks[index - 1].done = True
    print("완료 처리되었습니다.")


def run() -> None:
    tasks: list[Task] = []
    while True:
        print_menu()
        try:
            choice = input("메뉴 번호 선택: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n입력이 종료되어 프로그램을 종료합니다.")
            break

        if choice == "1":
            title = input("할 일 제목: ").strip()
            if not title:
                print("빈 제목은 허용되지 않습니다.")
                continue
            tasks.append(Task(title=title))
            print("할 일이 추가되었습니다.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            if not tasks:
                print("완료 처리할 항목이 없습니다.")
                continue
            show_tasks(tasks)
            idx = input("완료할 번호: ").strip()
            mark_done(tasks, idx)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("1~4 중에서 선택해주세요.")


if __name__ == "__main__":
    run()
