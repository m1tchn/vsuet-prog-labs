rejected_attempts = 0
number = int(input())
while number <= 0:
    rejected_attempts += 1
    number = int(input())

print(f"Квадрат: {number ** 2}")
print(f"Отклонено: {rejected_attempts}")
