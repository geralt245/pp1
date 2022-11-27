array = [51, 23, 6, 123, 25, 1, 3, 56]

def bubblesort(arr):
    swapped = False

    for i in range(len(arr) - 1, 0, -1):

        for j in range(i):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

print(array)
bubblesort(array)
print(array)