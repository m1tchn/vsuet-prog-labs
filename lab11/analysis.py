def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for index, todo in enumerate(data, start=1):
        if not isinstance(todo, dict):
            raise ValueError(f"Запись {index}: ожидался объект")

        for field in ("id", "userId"):
            if field not in todo:
                raise ValueError(f"Запись {index}: отсутствует поле {field}")
            value = todo[field]
            if type(value) is not int or value <= 0:
                raise ValueError(f"Запись {index}: поле {field} должно быть положительным целым")

        if todo["id"] in seen_ids:
            raise ValueError(f"Запись {index}: повторный id {todo['id']}")
        seen_ids.add(todo["id"])

        if "title" not in todo or not isinstance(todo["title"], str) or not todo["title"].strip():
            raise ValueError(f"Запись {index}: title должен быть непустой строкой")
        if "completed" not in todo or type(todo["completed"]) is not bool:
            raise ValueError(f"Запись {index}: completed должен быть логическим значением")

    return data


def completion_counts(todos):
    counts = {}
    for todo in todos:
        user_id = todo["userId"]
        counts.setdefault(user_id, 0)
        if todo["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user_id for user_id, count in counts.items() if count == maximum)


def leaders_tasks(todos, leaders):
    leader_ids = set(leaders)
    return [todo for todo in todos if todo["completed"] and todo["userId"] in leader_ids]


def select_tasks(todos, user_id, parameter=None):
    if parameter is None:
        raise ValueError("Для варианта 12 нужен порог")
    if type(parameter) is not int or parameter < 0:
        raise ValueError("Порог должен быть неотрицательным целым")

    return [
        todo
        for todo in todos
        if todo["userId"] == user_id
        and todo["completed"]
        and todo["id"] <= parameter
    ]
