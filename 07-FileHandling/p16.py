with open("song.txt", "r") as file:
    lines = file.readlines()
    repetitions = 0

    for line in lines:
        if repetitions == 5:
            userInput = input("Awaiting input... ")

            if userInput == "":
                repetitions = 0
                continue
            else:
                break
            
        print(line)
        repetitions += 1