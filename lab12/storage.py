"""Загрузка и сохранение данных проекта в JSON."""

import json
from pathlib import Path

from logic import validate_records


def load_records(path):
    """Читает, разбирает и проверяет JSON; ошибки передаются вызывающему коду."""
    with Path(path).open("r", encoding="utf-8") as file:
        records = json.load(file)
    return validate_records(records)


def save_records(path, records):
    """Проверяет и записывает записи в UTF-8 JSON."""
    validate_records(records)
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
