import random

def read_number():
    number = int(input("Enter a number: "))
    return number

def generate_number():
    randomNumber = random.randint(1, 9)
    return randomNumber