with open("MeatAndFish.txt", "r") as f1, open("GrainsAndBread.txt", "r") as f2, open("shoppinglist.txt", "a") as f3:
    contents1 = f1.read()
    contents2 = f2.read()

    f3.write(contents1)
    f3.write("\n")
    f3.write(contents2)