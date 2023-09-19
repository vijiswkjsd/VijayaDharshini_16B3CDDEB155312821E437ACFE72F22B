def linear_search_product(list_of_products, target_product):
    indices = []
    for i, product in enumerate(list_of_products):
        if product == target_product:
            indices.append(i)
    return indices
products = ["apple", "banana", "orange", "apple", "grape","banana","grape","orange","pineapple"]
print("apple,banana,grape,orange,pineapple")
target_product =input("Enter a product to search:")
result = linear_search_product(products, target_product)
print(products)
print("product's indices are ",result)