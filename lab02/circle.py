import math

radius = float(input("Радиус круга: "))

circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"\nДлина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
