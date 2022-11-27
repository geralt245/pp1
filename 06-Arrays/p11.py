def compare(array1, array2):
    if not len(array1) == len(array2):
        return False

    for i in range(0, len(array1)):
        if not array1[i] == array2[i]:
            return False

    return True


array1 = [3,2,1]
array2 = [3,2]

print("Array1:", end=" ")

for i in array1:
    print(i, end=" ")

print()

print("Array2:", end=" ")

for i in array2:
    print(i, end=" ")

print()

if compare(array1, array2) == True:
    print("Comparison: arrays are the same")
else:
    print("Comparison: arrays are not the same")