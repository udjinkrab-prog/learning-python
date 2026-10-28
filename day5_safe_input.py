def calculate_fp_net(price):
    fee = (price * 0.10727)
    net_profit = price - fee 
    return net_profit
while True:

    try:
        price_text = input("Цена товара ? ")
        price = float(price_text)
    except ValueError:
        print("Ошибка введите число ")
        continue
    if(price <= 0):
        print("введите больше 0")
        continue
    balance_fp = calculate_fp_net(price)
    print(f"После комисии: {balance_fp}")

    answer = input("\nХочешь посчитать ещё одну цену товара ? (да/нет): ")
    if answer.lower() != "да":
        print("Работа завершена. Удачных продаж на FunPay!")
        break