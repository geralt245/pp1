def median(array):
    middle = int(len(array) / 2)

    if len(array) % 2 != 0:
        return array[middle]
    else:
        return array[middle] + array[middle - 1]

array = [2, 4, 5, 7, 2, 4, 1, 3, 4, 10]
print(median(array))