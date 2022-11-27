array = [12, 6, 4, 9, 3]

def star(n):

    for number in array:
        print(f"{number}:", "*" * number)


star(array)