toy_count = int(input("Количество игрушек: "))
toys_per_set = int(input("Игрушек в одном наборе: "))

full_sets = toy_count // toys_per_set
remaining_toys = toy_count % toys_per_set
sets_needed = (toy_count + toys_per_set - 1) // toys_per_set

print(f"\nПолностью заполненных наборов: {full_sets}")
print(f"Остаток игрушек: {remaining_toys}")
print(f"Минимальное число наборов: {sets_needed}")
