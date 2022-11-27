import random

def rand_elem(array):
    return random.choice(array)

arr = [3, 4, 12, 55, 135]
print(rand_elem(arr))