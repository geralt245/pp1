array = [5, 1, 9, 6, 1]

def secondLargest(arr):
    largest = min(arr)
    secondLargest = 0

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        else:
            secondLargest = max(secondLargest, arr[i])

    return secondLargest

print(secondLargest(array))