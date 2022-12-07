import csv

with open("students.txt", "r") as file:
    reader = csv.reader(file)

    line_count = 0

    for row in reader:
        if line_count == 0:
            line_count += 1
            continue

        if int(row[2]) < 30:
            print(f"{row[0]}  {row[1]}  {row[4]}")