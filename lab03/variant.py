signal = int(input("Введите уровень сигнала от 0 до 100: "))

if signal < 0 or signal > 100:
    print(f"\nОшибка диапазона")
elif signal <= 34:
    print(f"\nСлабый")
elif signal <= 74:
    print(f"\nСредний")
else:
    print(f"\nСильный")
