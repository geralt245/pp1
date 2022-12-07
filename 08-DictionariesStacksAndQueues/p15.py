import json

student = {
    "name": "John",
    "surname": "Smith",
    "index": "542365342",
    "phone": {"mobile": "742346", "home": "234542"},
    "university": "harvard",
    "average_grade": 4.2,
    "active_student": True,
    "semester": 3
}


with open("student.json", "w") as file:
    json.dump(student, file, indent = 3)