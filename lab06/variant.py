numbers = [int(part) for part in input().split()]
selected = []

for number in numbers:
    if number > 0 and number % 2 == 0:
        selected.append(number)

print(f"Исходная выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Сортированная копия: {sorted(selected)}")
