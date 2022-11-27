array = [5, 23, 11, 1234, 5, -2, 4, 33, 1234, 12, 13, 71]

formattedArray = "|  "

number = 0

for i in array:
    if number == 2:
        formattedArray += " "
        number = 0

    formattedArray += str(i) + "| "
    number += 1

formattedArray += " |"

print("-" * len(formattedArray))
print(formattedArray)
print("-" * len(formattedArray))