while True:
    item_name = input("\nНазвание товара ? ")
    quantity_text = input("Количество товара ? ")
    quantity = int(quantity_text)

    if quantity <= 0: 
        print("Ошибка: количество должно быть больше 0 ")
    else: 
        price_text = input("Цена товара за штуку (первый круг) ? ")
        price = float(price_text)
        
        if price <= 0:
            print("Ошибка: цена должна быть больше 0 ")
        else: 
            dirty_money = quantity * price 
            commission = dirty_money * 0.10727     
            balance_FP = dirty_money - commission

            if balance_FP >= 5000:
                card_fee_rate = 0.06
            else: 
                card_fee_rate = 0.15 

            card_balance_comision = balance_FP * card_fee_rate
            card_balance = balance_FP - card_balance_comision
                
            if card_balance > 5000: 
                print("Крупная сделка! Не забудь пополнить баланс ")
            elif card_balance < 1000:
                print("Мелкая сделка")

            print(f"Товар: {item_name} | Продано: {quantity} шт.")
            print(f"Грязная сумма: {dirty_money:.2f} ₽")
            print(f"Комиссия FunPay: {commission:.2f} ₽")
            print(f"На баланс FunPay: {balance_FP:.2f} ₽")
            print(f"К получению на карту (-{card_fee_rate * 100:.0f}%): {card_balance:.2f} ₽")

    # Спрашиваем о повторе в самом конце круга цикла:
    answer = input("\nХочешь посчитать ещё один товар? (да/нет): ")
    if answer.lower() != "да":
        print("Работа завершена. Удачных продаж на FunPay!")
        break