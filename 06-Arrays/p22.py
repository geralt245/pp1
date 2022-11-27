array = [5, 1, 9, 6, 1]

def difference(arr):
    largest = arr[0]
    smallest = arr[0]

    for i in arr:
        if i > largest:
            largest = i
        
        if i < smallest:
            smallest = i

    return largest - smallest


print(difference(array))