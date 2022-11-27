array = [4, 7, 12, 14, 23, 31, 46]
evenNumbers = 0
oddNumbers = 0

for i in array:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print(f"Even numbers: {evenNumbers} Odd Numbers: {oddNumbers}")