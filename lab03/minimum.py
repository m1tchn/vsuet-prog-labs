a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
c = int(input("Введите третье целое число: "))

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print(f"\n{minimum}")
