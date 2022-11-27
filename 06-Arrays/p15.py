colors = ["green", "yellow", "blue", "red", "pink"]

with open("colors.txt", "w") as f:
    for color in colors:
        f.write(f"{color}\n")