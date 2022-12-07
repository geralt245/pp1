with open("numbers.txt") as file:
    numbers = file.readlines()
    sum = 0
    for i in range(0, len(numbers)):
        sum += int(numbers[i])

print(sum)