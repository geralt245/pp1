def separated(arr):
    newArray = []

    for i in arr:
        if i % 2 == 0:
            newArray.append(i)

    for i in arr:
        if i % 2 != 0:
            newArray.append(i)

    return newArray


array = [4, 3, 12, 16, 27, 13, 16]
print(separated(array))