class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"P({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(4, 9)
p2 = Point(4, 9)

if p1 == p2:
    print("The distance between the points is 0")
else:
    print(f"The distance between the points is ({p1.x - p2.x}, {p1.y - p2.y})")
