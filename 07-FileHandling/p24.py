import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)

sum = 0

for temp in temperatures:
    sum += int(temp)

print(sum / len(temperatures))