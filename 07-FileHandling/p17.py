with open("song.txt", "r") as file:
    contents = file.read()

with open("copy.txt", "w") as file:
    file.write(contents)