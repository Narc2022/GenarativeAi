products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"] #List of products

sample_product = ("Laptop", 1200, "Electronics") #Tuple representing a sample product with name, price, and category

print("2nd product:", products[1])
print("Last product:", products[-1])

products.append("Mouse")
products.append("Printer")

print("Updated products list:", products)

sample_list = list(sample_product)
sample_list[1] =1100
sample_product = tuple(sample_list)

print("Updated sample product:", sample_product)