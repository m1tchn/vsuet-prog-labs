def word_counts(text):
    #Возвращает частоты слов после очистки краевой пунктуации
    counts = {}
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_word_counts(counts):
    #Печатает пары cлово: количество» в алфавитном порядке
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    #Возвращает отсортированный список общих тем
    return sorted(set(first) & set(second))


def all_topics(first, second):
    #Возвращает отсортированный список всех уникальных тем
    return sorted(set(first) | set(second))


def totals_by_category(records):
    #Суммирует поле amount по категориям без изменения записей
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    #Возвращает названия записей указанной категории
    return [record["title"] for record in records if record["category"] == category]


def updated_course_record():
    #Создаёт изменённую учебную запись и пару из названия и часов.
    record = {"title": "Python", "hours": 2}
    record["hours"] = 4
    record["completed"] = False
    pair = (record["title"], record["hours"])
    return record, pair


def main():
    records = [
        {"title": "Фортепиано: гаммы", "category": "фортепиано", "amount": 45},
        {"title": "Вокал: дыхание", "category": "вокал", "amount": 30},
        {"title": "Фортепиано: этюд", "category": "фортепиано", "amount": 60},
        {"title": "Теория музыки", "category": "теория", "amount": 40},
        {"title": "Вокал: распевка", "category": "вокал", "amount": 25},
    ]

    print("Сводка по категориям:")
    for category, total in sorted(totals_by_category(records).items()):
        print(f"{category}: {total}")

    record, pair = updated_course_record()
    title, hours = pair
    print(f"Запись: {record}")
    print(f"Пара: {title}, {hours}")

    category = input()
    print(f"Названия категории: {titles_in_category(records, category)}")


if __name__ == "__main__":
    main()
