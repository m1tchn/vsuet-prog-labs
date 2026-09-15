total_seconds = int(input("Общее количество секунд: "))

if total_seconds < 0:
    print("\nВремя не может быть отрицательным, т.к. по условию total_seconds >= 0")
else:
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    print(f"\n{hours} ч {minutes} мин {seconds} с")
