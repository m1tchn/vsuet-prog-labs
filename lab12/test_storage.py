"""Автоматические проверки JSON-хранилища проекта."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import load_records, save_records


records = [
    {"id": 2, "title": "Занятие", "category": "вокал", "amount": 30, "completed": True},
]

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    save_records(path, records)
    assert load_records(path) == records
    assert json.loads(path.read_text(encoding="utf-8")) == records

with TemporaryDirectory() as directory:
    path = Path(directory) / "missing.json"
    try:
        load_records(path)
    except FileNotFoundError:
        pass
    else:
        raise AssertionError("Отсутствующий файл не обнаружен")

with TemporaryDirectory() as directory:
    path = Path(directory) / "bad.json"
    path.write_text("{", encoding="utf-8")
    try:
        load_records(path)
    except json.JSONDecodeError:
        pass
    else:
        raise AssertionError("Повреждённый JSON не обнаружен")

with TemporaryDirectory() as directory:
    path = Path(directory) / "bad_structure.json"
    path.write_text("[]", encoding="utf-8")
    assert load_records(path) == []

with TemporaryDirectory() as directory:
    path = Path(directory) / "preserve.json"
    original = "old content\n"
    path.write_text(original, encoding="utf-8")
    try:
        save_records(path, [{"id": True}])
    except ValueError:
        pass
    else:
        raise AssertionError("Неверные записи сохранены")
    assert path.read_text(encoding="utf-8") == original

print("Проверки хранения пройдены")
