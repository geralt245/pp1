def amount(letter, string):
    amount = 0

    for x in string:
        if x == letter:
            amount = amount + 1

    return amount


print(amount("e", "You never get a second chance to make a first impression"))
