item_name = input("Название товара ? ")
price_text = input("Цена за 1 штуку в рублях (онли цифрой(без первого курса комисии)) ")
quantity_text = input("Количество проданых штук (онли цифрой) ")
# есть два круга комисии , первый это на товар, то есть для покупателя к примеру товар стоит 11 рублей за штуку, но 
#продавец получает 9.82 рубля, — это первый круг комисии, второй круг комисии это уже вывод баланса из фп на банковскую карту
#тоесть если выводить 10000 рублей из фп, ты выведешь на картку 9400

price = float(price_text)
quantity = int(quantity_text) 


total_revenue = price * quantity 


fee = (total_revenue * 0.10727)

net_profit = total_revenue - fee 

card_fee = (net_profit * 0.06)
card_balance = (net_profit - card_fee)

print(f"Товар: {item_name} | Продано: {quantity} шт.")
print(f"Грязная сумма: {total_revenue:.2f} ₽")
print(f"Комиссия FunPay: {fee:.2f} ₽")
print(f"На баланс FunPay: {net_profit:.2f} ₽")
print(f"К получению на карту (-6%): {card_balance:.2f} ₽")