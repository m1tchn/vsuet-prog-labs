"""Консольное приложение для плана музыкальных занятий."""

import json
from pathlib import Path

from logic import add_record, delete_record, find_records, set_completed, statistics
from storage import load_records, save_records


DATA_PATH = Path(__file__).resolve().parent / "data.json"


def print_menu():
    """Показывает команды приложения."""
    print("\nМеню:")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")


def read_nonempty(prompt):
    """Читает строку, непустую после удаления краевых пробелов."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Значение не должно быть пустым")


def read_nonnegative_amount():
    """Читает целое количество минут не меньше нуля."""
    while True:
        raw_value = input("Продолжительность в минутах: ").strip()
        try:
            amount = int(raw_value)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if amount < 0:
            print("Количество минут не может быть отрицательным")
            continue
        return amount


def read_record_id():
    """Читает целый идентификатор записи."""
    while True:
        raw_value = input("ID записи: ").strip()
        try:
            record_id = int(raw_value)
        except ValueError:
            print("ID должен быть целым числом")
            continue
        if record_id <= 0:
            print("ID должен быть положительным")
            continue
        return record_id


def print_record(record):
    """Печатает одну запись в едином формате."""
    status = "выполнено" if record["completed"] else "не выполнено"
    print(
        f"ID: {record['id']}; {record['title']}; "
        f"категория: {record['category']}; "
        f"{record['amount']} мин.; статус: {status}"
    )


def show_records(records):
    """Показывает записи по возрастанию ID."""
    if not records:
        print("Нет записей")
        return
    for record in sorted(records, key=lambda item: item["id"]):
        print_record(record)


def add_record_interactively(records):
    """Запрашивает поля и добавляет новую незавершённую запись."""
    title = read_nonempty("Название: ")
    category = read_nonempty("Категория: ")
    amount = read_nonnegative_amount()
    record = add_record(records, title, category, amount)
    print(f"Запись добавлена с ID {record['id']}")


def find_records_interactively(records):
    """Ищет записи по непустой подстроке названия."""
    query = read_nonempty("Поиск по названию: ")
    matches = find_records(records, query)
    if not matches:
        print("Ничего не найдено")
        return
    for record in matches:
        print_record(record)


def set_status_interactively(records):
    """Устанавливает выбранный статус записи."""
    record_id = read_record_id()
    while True:
        answer = input("Статус (да — выполнено, нет — не выполнено): ").strip().casefold()
        if answer == "да":
            completed = True
            break
        if answer == "нет":
            completed = False
            break
        print("Введите «да» или «нет»")

    if set_completed(records, record_id, completed):
        print("Статус изменён")
    else:
        print("Запись с таким ID не найдена")


def delete_record_interactively(records):
    """Удаляет запись только после подтверждения «да»."""
    record_id = read_record_id()
    record = next((item for item in records if item["id"] == record_id), None)
    if record is None:
        print("Запись с таким ID не найдена")
        return

    print_record(record)
    confirmation = input("Удалить запись? (да/нет): ").strip().casefold()
    if confirmation != "да":
        print("Удаление отменено")
        return
    delete_record(records, record_id)
    print("Запись удалена")


def show_statistics(records):
    """Печатает общую статистику и суммы по категориям."""
    result = statistics(records)
    print(f"Всего записей: {result['total']}")
    print(f"Выполнено: {result['completed']}")
    print(f"Не выполнено: {result['pending']}")
    print(f"Всего минут: {result['amount']}")
    print("По категориям:")
    if not result["by_category"]:
        print("Нет категорий")
    else:
        for category, amount in result["by_category"].items():
            print(f"{category}: {amount} мин.")


def save_interactively(records):
    """Сохраняет записи и сообщает об успехе только после записи."""
    try:
        save_records(DATA_PATH, records)
    except (OSError, ValueError) as error:
        print(f"Не удалось сохранить данные: {error}")
        return False
    print("Данные сохранены")
    return True


def ask_exit(records):
    """Обрабатывает запрос выхода и возвращает True при завершении программы."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().casefold()
        if answer == "нет":
            return True
        if answer == "да":
            return save_interactively(records)
        print("Введите «да» или «нет»")


def load_at_start():
    """Загружает данные до показа меню; повреждённый файл останавливает запуск."""
    try:
        records = load_records(DATA_PATH)
    except FileNotFoundError:
        print("Файл data.json не найден. Начинаем с пустого списка.")
        return []
    except json.JSONDecodeError as error:
        print(f"Повреждённый JSON: строка {error.lineno}, столбец {error.colno}")
        return None
    except UnicodeError:
        print("Неверная кодировка data.json")
        return None
    except ValueError as error:
        print(f"Неверная структура data.json: {error}")
        return None
    except OSError as error:
        print(f"Ошибка доступа к data.json: {error}")
        return None
    print(f"Загружено записей: {len(records)}")
    return records


def main():
    records = load_at_start()
    if records is None:
        return

    actions = {
        "1": show_records,
        "2": add_record_interactively,
        "3": find_records_interactively,
        "4": set_status_interactively,
        "5": delete_record_interactively,
        "6": show_statistics,
    }

    while True:
        print_menu()
        command = input("Команда: ").strip()
        if command in actions:
            actions[command](records)
        elif command == "7":
            save_interactively(records)
        elif command == "8":
            if ask_exit(records):
                print("Работа завершена")
                return
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
