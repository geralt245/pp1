def minmax(arr):
    newList = []
    newList.append(max(arr))
    newList.append(min(arr))

    return newList


array = [4, 2, 8, 4, 7, 9, 5]
print(minmax(array))