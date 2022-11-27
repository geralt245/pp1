array = [15, 8, 31, 47, 2, 19]

def reverse(array):
    reversed = []
    for i in range(len(array), 0, -1):
        reversed.append(array[i - 1])
    return reversed


print("existed array:", end=" ")

for i in array:
    print(i, end=" ")

print()

print("reversed array:", end=" ")

for i in reverse(array):
    print(i, end=" ")