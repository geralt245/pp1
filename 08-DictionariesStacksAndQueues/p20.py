import json

keys_allowed = ["first_name", "last_name", "student_id"]

with open("students.json", "r", encoding="utf8") as file:
    content = json.load(file)

list_of_dicts = []

with open("limited.json", "a", encoding="utf8") as file:
    for i in content:
        new_dict = {}
        for key, value in i.items():
            if key in keys_allowed:
                new_dict[key] = value
        list_of_dicts.append(new_dict)

    json.dump(list_of_dicts, file, indent=4)