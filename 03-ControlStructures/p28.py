def fibonacci():
    list = []

    for i in range(0, 51):
        sum = 0
        if i == 0 or i == 1:
            list.append(i)
        else:
            sum = list[i - 1] + list[i - 2]
            list.append(sum)

    sequence = ""

    for item in list:
        sequence += str(item) + " "

    return sequence

print(fibonacci())