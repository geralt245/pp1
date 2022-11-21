import random

computerDice = random.randint(1, 6)
print(computerDice)

while True:
    playerDice = int(input("Enter a number between 1 and 6: "))

    if playerDice < 1 or playerDice > 6:
        continue
    else:
        break

print(playerDice == computerDice)