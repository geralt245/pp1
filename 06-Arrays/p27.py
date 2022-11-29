array = [5, 4, 3, 2, 6, 5]

def asString(arr):
    string = ""

    for i in range(0, len(arr)):
        if i == len(arr) - 1:
            string += str(arr[i])
            break

        string += str(arr[i]) + ","

    return string

print(asString(array))