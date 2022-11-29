def occurs(number, array):
    if number in array:
        return True
    else:
        return False


user = int(input("Enter a number: "))
array = [15, 38, 7, 23, 14]

print(occurs(user, array))