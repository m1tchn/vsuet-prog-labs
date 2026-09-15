price = int(input("Цена одной тетради (руб.): "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма (руб.): "))

if price < 0 or count < 0 or paid < 0 or paid < price * count:
    print("\nБыло передано отрицательное значение либо не соблюдено условие paid >= price * count (недостаточно средств)")
else:
    cost = price * count
    change = paid - cost

    print(f"\nСтоимость: {cost} руб.")
    print(f"Сдача: {change} руб.")
