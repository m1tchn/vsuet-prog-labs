numbers = [int(part) for part in input().split()]

if not numbers:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)
    print(f"Индексы максимума: {positions}")
