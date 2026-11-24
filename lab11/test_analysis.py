import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import completion_counts, leaders_tasks, select_tasks, top_users, validate_todos
from main import load_json, save_json

todos_file = Path(__file__).resolve().parent / "todos.json"

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

assert validate_todos(TODOS) is TODOS
assert completion_counts(TODOS) == {5: 2, 10: 2}
assert top_users({5: 2, 10: 2}) == [5, 10]
assert [todo["id"] for todo in leaders_tasks(TODOS, [5, 10])] == [1, 3, 4, 5]
assert top_users({5: 0, 10: 0}) == []
assert top_users({}) == []
assert top_users({5: 3, 10: 1}) == [5]
assert top_users({5: 2, 10: 2, 20: 1}) == [5, 10]

assert select_tasks(TODOS, 5, 2) == [TODOS[0]]
assert select_tasks(TODOS, 10, 4) == [TODOS[2], TODOS[3]]
assert select_tasks(TODOS, 999, 10) == []
assert select_tasks(TODOS, 5, 0) == []
assert select_tasks([], 5, 2) == []

for invalid in (
    {},
    [{"id": 1, "userId": 1, "title": "x", "completed": True},
     {"id": 1, "userId": 2, "title": "y", "completed": False}],
    [{"id": True, "userId": 1, "title": "x", "completed": False}],
    [{"id": 1, "userId": 1, "title": "x", "completed": "false"}],
    [{"id": 1, "title": "x", "completed": False}],
):
    try:
        validate_todos(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("Неверная структура не обнаружена")

with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(TODOS, 5, 2)
    save_json(selected, path)
    assert load_json(path) == selected

assert json.loads(todos_file.read_text(encoding="utf-8")) == [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

print("Проверки JSON-анализа пройдены")
