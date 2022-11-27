def circle(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius

    return (f"Area of the circle is {area} and circumference is {circumference}")

radius = int(input("Enter the radius: "))
print(circle(radius))