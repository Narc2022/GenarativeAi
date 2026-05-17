products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Shirt", "category": "Clothing"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Pants", "category": "Clothing"},
    {"name": "Blender", "category": "Home Appliances"},
]

price_dict ={
    "Laptop": 1200,
    "Shirt": 40,
    "Phone": 800,
    "Pants": 50,
    "Blender": 150,
}

catalog = [(p["name"], price_dict.get(p["name"],0), p["category"]) for p in products]
print(catalog)
category_to_products = {}

for name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] =[]
    category_to_products[category].append(name)


max_category =  max(category_to_products, key=lambda k: len(category_to_products[k]))

print("Catalog:", catalog)
print("Category to Products:", category_to_products)
print("Category with max products:", max_category)
print("Products in that category:", category_to_products[max_category])