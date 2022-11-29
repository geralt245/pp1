countries = open("countries.txt")
lines = countries.readlines()

count = 1
for line in lines:
    print(str(count) + ": " + line)
    count += 1

countries.close()