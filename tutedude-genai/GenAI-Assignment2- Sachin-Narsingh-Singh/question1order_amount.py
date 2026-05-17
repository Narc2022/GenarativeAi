order_amount = int(input("Enter the order amount: "))
print("Order amount is:", order_amount)

final_amount = 0

if order_amount >= 2000:
    final_amount = order_amount - (order_amount * 0.15)
elif order_amount < 2000 and order_amount >= 1500:
    final_amount = order_amount - (order_amount * 0.10)
elif order_amount < 1500 and order_amount >= 1000:
    final_amount = order_amount - (order_amount * 0.07)
else:
    final_amount = order_amount

print("Final order amount is:", final_amount)
