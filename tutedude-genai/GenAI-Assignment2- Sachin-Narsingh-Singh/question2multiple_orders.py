def apply_discount(order_amount):
    if order_amount >= 2000:
        final_amount = order_amount - (order_amount * 0.15)
        discount = 0.15 * 100
    elif order_amount < 2000 and order_amount >= 1500:
        final_amount = order_amount - (order_amount * 0.10)
        discount = 0.10 * 100
    elif order_amount < 1500 and order_amount >= 1000:
        final_amount = order_amount - (order_amount * 0.07)
        discount = 0.07 * 100
    else:
        final_amount = order_amount
        discount = 0
    return [order_amount, discount, final_amount]


orders = [1200, 2500, 800, 1750, 3000]

order_list= [["order_amount", "discount%" , "final_amount"]]

for order in orders:
  order_list.append(apply_discount(order))
  

for row in order_list:
   print("{:<15} {:<10} {:<15}".format(*row))

for row in order_list:
    total_revenue = sum([row[2] for row in order_list])
print("Total revenue after discounts: ", total_revenue)