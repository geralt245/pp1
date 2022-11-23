sum = 0
quantity = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    sum += number
    quantity = quantity + 1


mean = sum / quantity

print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={mean}")