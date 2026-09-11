order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

first_item_name = input("Введите название первой позиции: ")
first_item_quantity = int(input("Введите количество первой позиции: "))
first_item_price = float(input("Введите цену первой позиции, руб.: "))

second_item_name = input("Введите название второй позиции: ")
second_item_quantity = int(input("Введите количество второй позиции: "))
second_item_price = float(input("Введите цену второй позиции, руб.: "))

delivery_cost = float(input("Введите стоимость доставки, руб.: "))
discount_percent = float(input("Введите скидку на товары, %: "))
paid_amount = float(input("Введите внесённую сумму, руб.: "))

first_item_cost = first_item_quantity * first_item_price
second_item_cost = second_item_quantity * second_item_price
goods_cost = first_item_cost + second_item_cost
discount_amount = goods_cost * discount_percent / 100
total_cost = goods_cost - discount_amount + delivery_cost
total_quantity = first_item_quantity + second_item_quantity
change = paid_amount - total_cost

print(f"\nЗаказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("Название | Количество | Цена, руб. | Стоимость, руб.")
print(
    f"{first_item_name} | {first_item_quantity} | "
    f"{first_item_price:.2f} | {first_item_cost:.2f}"
)
print(
    f"{second_item_name} | {second_item_quantity} | "
    f"{second_item_price:.2f} | {second_item_cost:.2f}"
)
print(f"Стоимость товаров: {goods_cost:.2f} руб.")
print(f"Скидка ({discount_percent:.2f}%): {discount_amount:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"Итоговая сумма: {total_cost:.2f} руб.")
print(f"Общее количество единиц: {total_quantity}")
print(f"Внесённая сумма: {paid_amount:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
