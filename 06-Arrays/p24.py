def greater(arr):
    amount = 0
    n = float(input("Enter a number: "))

    for i in arr:
        if i > n:
            amount += 1

    return amount

array = [3, 4.2, 12, 56.3, 122, 5]
print(greater(array))