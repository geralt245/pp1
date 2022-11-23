for i in range(1, 8):
    sum = i + 7
    print(i, end=" ")

    for j in range(1, 7):
        print(sum, end=" ")
        sum += 7

    print()