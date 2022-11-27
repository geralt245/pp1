array = [4, 3, 7, 1, 3]

def sum(array):
    sum = 0

    for i in array:
        sum += i

    return sum


def array2str(array):
    elements = ""
    for i in array:
        elements += str(i)
    elements = " ".join(elements)
    return elements


print(f"Array: {array2str(array)}")
print(f"Sum of values: {sum(array)}")