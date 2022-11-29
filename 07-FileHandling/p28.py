import re

with open("grades.txt", "r") as f:
    content = f.read()
    grades = re.findall("\d+\.\d+", content)

sum = 0
for grade in grades:
    sum += float(grade)

print(sum / len(grades))