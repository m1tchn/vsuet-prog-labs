import json
from pathlib import Path

from analysis import completion_counts, leaders_tasks, select_tasks, top_users, validate_todos


FOLDER = Path(__file__).resolve().parent
TODOS_PATH = FOLDER / "todos.json"
LEADERS_PATH = FOLDER / "leaders.json"
SELECTED_PATH = FOLDER / "selected.json"


def load_json(path):
    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, path):
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def read_positive_integer(prompt):
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("Нужно ввести положительное целое число")
            continue
        if value <= 0:
            print("Число должно быть больше нуля")
            continue
        return value


def read_nonnegative_integer(prompt):
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("Нужно ввести неотрицательное целое число")
            continue
        if value < 0:
            print("Число не может быть отрицательным")
            continue
        return value


def main():
    try:
        data = load_json(TODOS_PATH)
        todos = validate_todos(data)
        counts = completion_counts(todos)
        leaders = top_users(counts)
        leader_tasks = leaders_tasks(todos, leaders)

        user_id = read_positive_integer("Идентификатор пользователя: ")
        threshold = read_nonnegative_integer("Максимальный id задачи: ")
        selected = select_tasks(todos, user_id, threshold)

        save_json(leader_tasks, LEADERS_PATH)
        save_json(selected, SELECTED_PATH)

        print(f"Количество выполненных задач: {counts}")
        print(f"Лидеры: {leaders}")
        print(f"Задачи лидеров: {[todo['id'] for todo in leader_tasks]}")
        print(f"Выбранные задачи: {[todo['id'] for todo in selected]}")
    except FileNotFoundError:
        print(f"Файл не найден: {TODOS_PATH.name}")
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: строка {error.lineno}, столбец {error.colno}")
    except UnicodeError:
        print("Ошибка кодировки входного файла")
    except ValueError as error:
        print(f"Ошибка структуры или ввода: {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")


if __name__ == "__main__":
    main()
