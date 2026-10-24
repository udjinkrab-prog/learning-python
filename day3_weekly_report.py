weekly_sales = [
    71.28, 453.81, 26.78, 49.10, 196.40,
    35.62, 39.87, 398.70, 3.98, 128.04,
    79.74, 199.35, 550.40, 1300.80, 600.40
]
def calculate_fp_net(order):
    fee = (order * 0.10727)
    net_profit = order - fee 
    return net_profit
def calculate_card_withdrawal(order):
    if order >= 5000:
        card_fee_rate = 0.06    
    else: 
        card_fee_rate = 0.15 
    card_balance_comision = order * card_fee_rate
    card_balance = order - card_balance_comision
    return card_balance
def classify_order(order):
    if order >= 500:
        order = ("Vip")  
    elif order >= 100:
        order = ("Средний")
    elif order <= 100:
        order = ("Мелкий")
    return order
for order in weekly_sales:

    print(f"=== КАЖДЫЙ ТОВАР СЧИТАЕМ ===\n")
    print(f"Грязная сумма: {order:.2f} ₽")
    print(f"На баланс FunPay: {calculate_fp_net(order):.2f} ₽")
    print(f"К получению на карту: {calculate_card_withdrawal(calculate_fp_net(order)):.2f} ₽")
    print(f"Категория: {classify_order(order)} ")
    print("=== Удачных продаж на платформе ===\n")


total_revenue = sum(weekly_sales)
clean_money = sum (calculate_card_withdrawal(calculate_fp_net(order)) for order in weekly_sales)

print("=== ИТОГИ ВСЕГО ===\n")
print(f"Всего заказов: {len(weekly_sales)} шт.\n")
print(f"Грязная выручка: {total_revenue:.2f} ₽\n")
print(f"Чистая прибыль (FP): {clean_money:.2f} ₽\n")


with open("weekly_full_report.txt", "w", encoding="utf-8") as f:
    f.write("=== ИТОГИ ВСЕГО ===\n")
    f.write(f"Всего заказов: {len(weekly_sales)} шт.\n")
    f.write(f"Грязная выручка: {total_revenue:.2f} ₽\n")
    f.write(f"Чистая прибыль (FP): {clean_money:.2f} ₽\n")
    
print("\n[V] Полный отчёт успешно сохранён в файл weekly_full_report.txt!")