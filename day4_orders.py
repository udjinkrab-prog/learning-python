orders = [
    {"item":"Gilded Needle","price":9.84,"quantity":125},
    {"item":"Forge Needle","price":9.84,"quantity":75},
    {"item":"Idol of Yun'Shul","price":1.24,"quantity":600},
]
grand_total = 0
for order in orders:
    total = order["price"] * order["quantity"]
    grand_total = grand_total + total
    print (f"{order['item']}: {total:.2f} RUB")  
