try:
    first_discipline = input("Введите название первого предмета: ")
    second_discipline = input("Введите название второго предмета: ")

    first_discipline_count = int(input("Введите кол-во занятий по первому предмету за неделю: "))
    second_discipline_count = int(input("Введите кол-во занятий по второму предмету за неделю: "))

    first_discipline_length = int(input("Введите продолжительность первого занятия в минутах: "))
    second_discipline_length = int(input("Введите продолжительность второго занятия в минутах: "))

    available_week_time = float(input("Введите доступное время на неделю в часах: "))

    first_discipline_time = first_discipline_count * first_discipline_length
    second_discipline_time = second_discipline_count * second_discipline_length
    total_time_minutes = first_discipline_time + second_discipline_time
    total_time_hours = total_time_minutes / 60

    if (
        first_discipline_count < 0
        or second_discipline_count < 0
        or first_discipline_length < 1
        or second_discipline_length < 1
        or available_week_time < total_time_hours
    ):
        print("Неправильно введены данные.")
    else:
        free_time = available_week_time - total_time_hours
        four_weeks_minutes = total_time_minutes * 4
        four_weeks_hours = total_time_hours * 4

        print(f"\nВремя на предмет \"{first_discipline}\": {first_discipline_time} мин.")
        print(f"Время на предмет \"{second_discipline}\": {second_discipline_time} мин.")
        print(f"Общая нагрузка: {total_time_minutes} мин. ({total_time_hours:.2f} ч.)")
        print(f"Остаток свободного времени: {free_time:.2f} ч.")
        print(
            f"Нагрузка за 4 недели: "
            f"{four_weeks_minutes} мин. ({four_weeks_hours:.2f} ч.)"
        )

except ValueError:
    print("Количество занятий и продолжительность должны быть целыми числами")