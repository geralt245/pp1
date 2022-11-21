import random

def diceRolls():
    firstRoll = random.randint(1, 6)
    secondRoll = random.randint(1, 6)
    thirdRoll = random.randint(1, 6)

    return firstRoll + secondRoll + thirdRoll

print(diceRolls())