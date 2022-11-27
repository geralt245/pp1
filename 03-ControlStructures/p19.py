def dogYears(dogAge):
    age = 0

    for i in range(1, dogAge + 1):
        if i <= 2:
            age += 10.5
        else:
            age += 4
    

    return age


humanYears = int(input("Enter the dog's age in human years: "))
print(f"The dog's age in dog's years is {dogYears(humanYears)} years.")