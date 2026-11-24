"""Автоматические проверки бизнес-логики проекта."""

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)


def make_records():
    return [
        {"id": 1, "title": "Гаммы", "category": "фортепиано", "amount": 45, "completed": True},
        {"id": 2, "title": "Арпеджио", "category": "фортепиано", "amount": 30, "completed": False},
        {"id": 3, "title": "Распевка", "category": "вокал", "amount": 25, "completed": True},
        {"id": 4, "title": "Сольфеджио", "category": "теория", "amount": 40, "completed": False},
    ]


records = make_records()
assert validate_records(records) is records
assert find_records(records, "гам") == [records[0]]
assert find_records(records, "ГАМ") == [records[0]]
assert find_records(records, "а") == [records[0], records[1], records[2]]
assert find_records(records, "нет") == []

assert statistics(records) == {
    "total": 4,
    "completed": 2,
    "pending": 2,
    "amount": 140,
    "by_category": {"вокал": 25, "теория": 40, "фортепиано": 75},
}

new_record = add_record(records, "  Новый этюд  ", "  фортепиано ", 20)
assert new_record == {
    "id": 5,
    "title": "Новый этюд",
    "category": "фортепиано",
    "amount": 20,
    "completed": False,
}
assert records[-1] is new_record
same_title = add_record(records, "Гаммы", "вокал", 10)
assert same_title["title"] == "Гаммы"
assert len([record for record in records if record["title"] == "Гаммы"]) == 2
assert set_completed(records, 5, True) is True
assert next(record for record in records if record["id"] == 5)["completed"] is True
assert set_completed(records, 999, True) is False
assert delete_record(records, 5) is True
assert delete_record(records, same_title["id"]) is True
assert [record["id"] for record in records] == [1, 2, 3, 4]
assert delete_record(records, 999) is False

records_with_spaces = [
    {"id": 1, "title": "A", "category": "  одна ", "amount": 2, "completed": False},
    {"id": 2, "title": "B", "category": "одна", "amount": 3, "completed": False},
]
assert statistics(records_with_spaces)["by_category"] == {"одна": 5}

invalid_records = [
    {},
    [{"id": 1, "title": "A", "category": "x", "amount": 1}],
    [{"id": True, "title": "A", "category": "x", "amount": 1, "completed": False}],
    [{"id": 1, "title": "A", "category": "x", "amount": True, "completed": False}],
    [{"id": 1, "title": "A", "category": "x", "amount": 1, "completed": 1}],
    [{"id": 1, "title": " ", "category": "x", "amount": 1, "completed": False}],
    [{"id": 1, "title": "A", "category": " ", "amount": 1, "completed": False}],
    [{"id": 1, "title": "A", "category": "x", "amount": -1, "completed": False}],
    [
        {"id": 1, "title": "A", "category": "x", "amount": 1, "completed": False},
        {"id": 1, "title": "B", "category": "y", "amount": 2, "completed": False},
    ],
]
for invalid in invalid_records:
    try:
        validate_records(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("Неверная запись не обнаружена")

for invalid_amount in (-1, True, 1.5):
    try:
        add_record([], "A", "x", invalid_amount)
    except ValueError:
        pass
    else:
        raise AssertionError("Неверное количество принято")

try:
    find_records(records, "   ")
except ValueError:
    pass
else:
    raise AssertionError("Пустой запрос принят")

print("Проверки логики пройдены")
