first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, * или /): ").strip()

if operation == "+":
    result = first + second
    print(f"{result:.2f}")
elif operation == "-":
    result = first - second
    print(f"{result:.2f}")
elif operation == "*":
    result = first * second
    print(f"{result:.2f}")
elif operation == "/":
    if second == 0:
        print(f"\nДеление на ноль запрещено")
    else:
        result = first / second
        print(f"{result:.2f}")
else:
    print(f"\nНеизвестная операция")
