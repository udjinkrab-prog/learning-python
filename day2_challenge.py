
orders = [120.20, 550.40, 45.60, 1300.80, 80.20, 600.40, 25.60, 2100.80, 95.50]
vip_orders = []
for order in orders:
    if order >= 500:
        vip_orders.append(order)
        print(f"{order:.2f} ")




total_revenue = sum(vip_orders)

average_order = total_revenue / len(orders)
print("=== ИТОГИ ТОРГОВ ЗА НЕДЕЛЮ ===\n")
print(f"Всего заказов: {len(vip_orders)} шт.\n")
print(f"Общая сумма: {total_revenue} Rub \n")
print(f"{vip_orders}")

with open("vip_orders.txt", "w", encoding="utf-8") as f:
        f.write("=== ИТОГИ ТОРГОВ ЗА НЕДЕЛЮ ===\n")
        f.write(f"Всего заказов: {len(vip_orders)} шт.\n")
        f.write(f"Средний чек: {average_order:.2f} ₽\n")
        for vip in vip_orders:
             f.write(f"{vip:.2f}RUB\n")