products = []

while True:
    product = input("Enter a product: ")

    if product == "":
        break
    else:
        products.append(product)


with open("products.txt", "a") as f:
        for i in range(0, len(products)):
            if i == len(products) - 1:
                f.write(products[i])
            else:
                f.write(products[i] + "\n")