def calculate_fp_net(total_revenue):
    fee = (total_revenue * 0.10727)
    net_profit = total_revenue - fee 
    return net_profit
def calculate_card_withdrawal(order):
    if order >= 5000:
        card_fee_rate = 0.06    
    else: 
        card_fee_rate = 0.15 
    card_balance_comision = order * card_fee_rate
    card_balance = order - card_balance_comision
    return card_balance
while True:
    
    total_revenue_text = input("Общая выручка (RUB) ")
    total_revenue = float(total_revenue_text)

    balance_fp = calculate_fp_net(total_revenue)
    card_balance = calculate_card_withdrawal(balance_fp)

    print(f"Общая выручка на фп баланс (RUB) {balance_fp:.2f} ")
    print(f"Общая выручка на карту (RUB) {card_balance:.2f} ")

    answer = input("\nХочешь посчитать ещё один товар? (да/нет): ")
    if answer.lower() != "да":
        print("Работа завершена. Удачных продаж на FunPay!")
        break