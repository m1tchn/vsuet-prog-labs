"""Правила и операции над записями плана музыкальных занятий."""


REQUIRED_FIELDS = ("id", "title", "category", "amount", "completed")


def validate_records(records):
    """Проверяет список записей и возвращает его без изменения."""
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for position, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {position}: ожидался объект")

        for field in REQUIRED_FIELDS:
            if field not in record:
                raise ValueError(f"Запись {position}: отсутствует поле {field}")

        record_id = record["id"]
        if type(record_id) is not int or record_id <= 0:
            raise ValueError(f"Запись {position}: id должен быть положительным целым")
        if record_id in seen_ids:
            raise ValueError(f"Запись {position}: повторный id {record_id}")
        seen_ids.add(record_id)

        for field in ("title", "category"):
            if not isinstance(record[field], str) or not record[field].strip():
                raise ValueError(f"Запись {position}: {field} должна быть непустой строкой")

        amount = record["amount"]
        if type(amount) is not int or amount < 0:
            raise ValueError(f"Запись {position}: amount должен быть целым числом не меньше нуля")

        if type(record["completed"]) is not bool:
            raise ValueError(f"Запись {position}: completed должен быть логическим значением")

    return records


def add_record(records, title, category, amount):
    """Добавляет запись и возвращает её; список изменяется только после проверки."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название не должно быть пустым")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество минут должно быть целым числом не меньше нуля")

    new_id = max((record["id"] for record in records), default=0) + 1
    record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    """Возвращает записи с подстрокой в названии без учёта регистра."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")
    normalized_query = query.strip().casefold()
    return [record for record in records if normalized_query in record["title"].casefold()]


def set_completed(records, record_id, completed):
    """Устанавливает статус записи; возвращает False для неизвестного ID."""
    if type(record_id) is not int or type(completed) is not bool:
        raise ValueError("ID должен быть целым числом, статус — логическим значением")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись по ID; возвращает False для неизвестного ID."""
    if type(record_id) is not int:
        raise ValueError("ID должен быть целым числом")
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    """Возвращает статистику без изменения исходного списка."""
    by_category = {}
    completed_count = 0
    amount_total = 0

    for record in records:
        if record["completed"]:
            completed_count += 1
        amount_total += record["amount"]
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]

    return {
        "total": len(records),
        "completed": completed_count,
        "pending": len(records) - completed_count,
        "amount": amount_total,
        "by_category": dict(sorted(by_category.items())),
    }
