order_amount = 0.0
while True:
    user_input = input("Enter order amount (or 'q' to quit): ")
    if(user_input == "q"):
        break
    if not user_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        continue
    order_amount+=float(user_input)

print("Total order amount: ", order_amount)