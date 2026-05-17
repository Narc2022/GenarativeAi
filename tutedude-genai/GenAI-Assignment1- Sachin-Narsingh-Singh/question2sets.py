products = [
    "Laptop",
    "Smartphone",
    "Tablet",
    "Headphones",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
]  # List of products

categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Accessories",
    "Electronics",
    "Accessories",
    "Accessories",
    "Office",
]  # List of product categories

categories_set = set(categories)  # Set of unique categories
print("Unique product categories:", categories_set)

categories_set.add("Gaming")  # Adding a new category to the set
categories_set.add("Electronics")  # Attempting to add a duplicate category

print("After adding categories:", categories_set)

print("Is 'Office' in set?", "Office" in categories_set)

print("Total unique categories:", len(categories_set))
