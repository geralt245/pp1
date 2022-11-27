def month(n):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if n >= 1 and n <= 12:
        return months[n - 1]

print(month(1))