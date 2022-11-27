amount = int(input("Enter the amount in PLN: "))


ones = 0
twos = 0
fives = 0

print(f"The amount of PLN {amount} in coins:")

fives += int(amount / 5)
amount -= int(amount / 5) * 5

twos += int(amount / 2)
amount -= int(amount / 2) * 2

ones += int(amount / 1)

print(f"5 zł - {fives}")
print(f"2 zł - {twos}")
print(f"1 zł - {ones}")