array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5, 1, 36]

def numbers(n1, n2):
    elements = ""

    for i in array1:
        if i not in array2:
            elements += str(i) + " "
    return elements


print(numbers(array1, array2))