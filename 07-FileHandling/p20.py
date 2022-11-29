with open("numbers_in_range.txt", "a") as f:
    for i in range(1, 51):
        if i == 50:
            f.write(str(i))
        else:
            f.write(str(i) + "\n")