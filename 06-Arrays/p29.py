array1 = [5, 15, 13, 12, 152]
array2 = [5, 15, 13, 12, 153]

def isSubset(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False

    return True

print(isSubset(array1, array2))