def bmi(height, weight):
    bmi = weight / height ** 2

    return (f"BMI index: {bmi}")

height = int(input("Enter height in cm: ")) / 100
weight = int(input("Enter weight in kg: "))

print(bmi(height, weight))