from collections_lab import (
    all_topics,
    common_topics,
    titles_in_category,
    totals_by_category,
    updated_course_record,
    word_counts,
)


assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("  ;Python:   SQL? python.") == {"python": 2, "sql": 1}

first_topics = ["python", "sql", "python"]
second_topics = ["sql", "git"]
assert common_topics(first_topics, second_topics) == ["sql"]
assert all_topics(first_topics, second_topics) == ["git", "python", "sql"]
assert common_topics([], ["python"]) == []
assert all_topics([], ["python", "python"]) == ["python"]

record, pair = updated_course_record()
assert record == {"title": "Python", "hours": 4, "completed": False}
assert pair == ("Python", 4)

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
records_copy = [record.copy() for record in records]
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert records == records_copy

music_records = [
    {"title": "Гаммы", "category": "фортепиано", "amount": 45},
    {"title": "Распевка", "category": "вокал", "amount": 30},
    {"title": "Этюд", "category": "фортепиано", "amount": 60},
    {"title": "Сольфеджио", "category": "теория", "amount": 40},
    {"title": "Арпеджио", "category": "фортепиано", "amount": 25},
]
music_copy = [record.copy() for record in music_records]
assert totals_by_category(music_records) == {
    "фортепиано": 130,
    "вокал": 30,
    "теория": 40,
}
assert titles_in_category(music_records, "фортепиано") == ["Гаммы", "Этюд", "Арпеджио"]
assert titles_in_category(music_records, "нет") == []
assert music_records == music_copy

print("Проверки коллекций пройдены")
