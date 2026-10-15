def sum_digits(number):
    """Возвращает сумму цифр модуля целого числа."""
    value = abs(number)
    total = 0

    while value > 0:
        total += value % 10
        value //= 10

    return total


def average(numbers):
    """Возвращает среднее списка или None для пустого списка."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Приводит текст к нижнему регистру и нормализует пробелы."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Возвращает положительные чётные числа больше порога."""
    selected = []
    for number in numbers:
        if number % 2 == 0 and number > threshold:
            selected.append(number)
    return selected
