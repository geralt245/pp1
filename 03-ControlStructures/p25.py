a = 6
b = 20

for i in range(0, a):
    if i == 0 or i == a - 1:
        print("*" * b)
    else:
        print("*" + " " * (b - 2) + "*")