from mymath import *

computerNumber = generate_number()
print(computerNumber)
playerNumber = read_number()

if playerNumber == computerNumber:
    print("You win")
else:
    print("Try again!")