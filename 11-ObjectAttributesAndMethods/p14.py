class SurfaceArea():

    @staticmethod
    def triangle(base, height):
        return (base * height) / 2

    @staticmethod
    def circle(radius):
        return 3.14 * radius ** 2

    @staticmethod
    def rectangle(side1, side2):
        return side1 * side2


print(SurfaceArea.circle(3))
print(SurfaceArea.rectangle(4, 7))
print(SurfaceArea.triangle(6, 2))
