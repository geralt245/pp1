import json

header = "Date          Buying Rate          Selling Rate"
print(header)

for i in header:
    print("=", end="")

print()

with open("euro.json", "r") as file:
    content = json.load(file)

for i in content["rates"]:
    print(str(i["effectiveDate"]) + "       " + str(i["bid"]) + "              " + str(i["ask"]))