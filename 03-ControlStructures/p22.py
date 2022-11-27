for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        i = str("BINGO")
    elif i % 3 == 0:
        i = str("THREE")
    elif i % 5 == 0:
        i = str("FIVE")

    print(i, end=" ")