price_dict = {
    "Laptop": 1200,
    "Smartphone": 800,
    "Tablet": 600,
    "Headphones": 100,
    "Monitor": 300,
    "Keyboard": 50,
    "Mouse": 25,
    "Printer": 150
}

price_dict["Mouse"] = 30

price_dict["Phone"] = 850

product_to_remove = "Printer"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
else:
    print(product_to_remove, "does not exist.")
    
print("Updated price dictionary:", price_dict)

total_price = sum(price_dict.values())
average_price = total_price / len(price_dict)

print("Average price:", average_price)

max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Most expensive product:",max_product,"-",price_dict[max_product])
print("Least expensive product:",min_product,"-",price_dict[min_product])