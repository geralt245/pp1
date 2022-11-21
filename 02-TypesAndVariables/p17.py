def heightInFeet(height):
    feet = 0
    inches = 0
    feet += int(height / 30.48)
    newHeight = height - 30.48 * feet
    inches += float(newHeight / 2.54)

    return (f"I am {height} cm tall, i.e. {feet} feet and {inches} inches")

height = float(input("Enter your height: "))
print(heightInFeet(height))