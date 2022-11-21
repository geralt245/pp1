def triangleArea(a, b, c):
    area = (a + b + c) / 2
    return area

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

print(triangleArea(a, b, c))