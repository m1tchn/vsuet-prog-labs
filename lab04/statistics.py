n = int(input())
first_number = int(input())

total = first_number
positive_count = 1 if first_number > 0 else 0
maximum = first_number

for _ in range(n - 1):
    number = int(input())
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")
