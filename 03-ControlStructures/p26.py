pin = "0802"
tries = 0

while True:
    userInput = input("Enter the PIN code: ")

    if userInput == pin:
        print("Correct pin")
        break
    else:
        print("Incorrect")
        tries = tries + 1

    if tries == 3:
        print("Sorry, your payment card has been blocked")
        break