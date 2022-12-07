import random

with open("random_numbers.txt", "a") as f:
    for i in range(1, 51):
        if i == 50:
            f.write(str(random.randint(100, 999)))
        else:
            f.write(str(random.randint(100, 999)) + "\n")