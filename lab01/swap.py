first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print("\nИсходные значения:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")

temporary_room = first_room
first_room = second_room
second_room = temporary_room

print("\nЗначения после обмена:")
print(f"Первая аудитория: {first_room}")
print(f"Вторая аудитория: {second_room}")