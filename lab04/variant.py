n = int(input())
count = 0
total = 0

for _ in range(n):
    number = int(input())
    if number > 0 and number % 2 == 0:
        count += 1
        total += number

print(f"Количество: {count}")
print(f"Сумма: {total}")
