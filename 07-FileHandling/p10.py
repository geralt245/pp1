with open("data.txt", "w") as file:
    file.write("Konrad\nPodgórski\nUniwersytet Ekonomiczny w Krakowie\nInformatyka stosowana")

with open("data.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line)