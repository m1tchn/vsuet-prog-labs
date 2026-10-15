from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input())
    numbers = [int(part) for part in input().split()]
    text = input()
    threshold = int(input())

    print(f"Сумма цифр: {sum_digits(number)}")

    numbers_average = average(numbers)
    if numbers_average is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {numbers_average}")

    print(f"Нормализованный текст: {normalize_text(text)}")
    print(f"Выборка: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()
