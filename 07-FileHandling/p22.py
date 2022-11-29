with open("power.txt", "a") as f:
    for i in range(1, 11):
        f.write(f"{i},{i**2},{i**3}\n")