import requests

code_value_txt = input("Код валюты ? USD , EUR: ")

url = (f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={code_value_txt}&json")

try:
    response = requests.get(url)

    data = response.json()

    if data == []:
        print(f"Валюту з кодом {code_value_txt} не знайдено" )
    else: 
        print(f"{data[0]["txt"]} — {data[0]["rate"]} грн")
except:
    print("Помилка з'єднання. Перевірте інтернет." )





    
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
