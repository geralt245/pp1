def month(n):
    list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if n >= 1 and n <= 12:
        return list[n - 1]

print(month(7))