import json

with open("MOCK_DATA.json") as file:
    data = json.load(file)

for k, v in data.items():
    print(k,":",v)