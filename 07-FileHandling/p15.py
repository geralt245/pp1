fileName = input("Enter file name: ")

with open(fileName, "r") as f:
    lines = f.readlines()
    amountOfLines = 0

    for line in lines:
        amountOfLines += 1

print(f"File name: {fileName}")
print(f"Number of lines: {amountOfLines}")