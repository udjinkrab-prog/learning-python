sales = []

print("=== ТРЕКЕР ПРОДАЖ ЗА ДЕНЬ ===")
print("Вводите сумму каждого заказа. Когда закончите напишите — 'стоп'.\n")

while True:
    user_input = input("Сумма заказа в рублях (или 'стоп'): ")

    if user_input.lower() == "стоп":
        break 


    order_amount = float(user_input)
    sales.append(order_amount)
    print(f"-> Добавлен заказ: {order_amount:.2f}Rub (всего заказов в базе: {len(sales)})")


print("\n" + "=" * 30)
print("ИТОГИ ТОРГОВОГО ДНЯ: ")

if len(sales) == 0:
    print("Сегодня продаж не было.")
else:
    total_revenue = sum(sales)
    best_order = max(sales)
    worst_order = min(sales)
    average_order = total_revenue / len(sales)

    net_total = total_revenue * 0.89273


    print(f"Всего закрыто заказов: {len(sales)} шт.")
    print(f"Общая 'грящная' выручка: {total_revenue:.2f} Rub")
    print(f"Чистая прибыль (на баланс FP): {net_total:.2f} Rub")
    print(f"Самый крупный заказ: {best_order:.2f} Rub")
    print(f"Самый мелкий заказ: {worst_order:.2f} Rub")
    print(f"Средний чек: {average_order:.2f} Rub")
        # Сохраняем отчёт в файл на жёсткий диск:
    with open("daily_report.txt", "w", encoding="utf-8") as f:
        f.write("=== ИТОГИ ТОРГОВОГО ДНЯ ===\n")
        f.write(f"Всего заказов: {len(sales)} шт.\n")
        f.write(f"Грязная выручка: {total_revenue:.2f} ₽\n")
        f.write(f"Чистая прибыль (FP): {net_total:.2f} ₽\n")
        f.write(f"Крупнейший заказ: {best_order:.2f} ₽\n")
        f.write(f"Средний чек: {average_order:.2f} ₽\n")

    print("\n[V] Полный отчёт успешно сохранён в файл daily_report.txt!")