def numberOfDigits(digits):
    sum = 0

    for digit in str(digits):
        sum += int(digit)

    return sum


print(numberOfDigits(7182))