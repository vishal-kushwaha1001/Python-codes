order_amount = int(input("Enter order price : "))

delivery_fee = 0 if order_amount > 300 else 30

print(f"your total price  is {order_amount + delivery_fee}")