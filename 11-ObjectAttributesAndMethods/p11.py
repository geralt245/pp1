class Student():
    id = 100000
    university = "UEK Kraków"

    def __init__(self, name, surname, field):
        Student.id += 1
        self.name = name
        self.surname = surname
        self.field = field

    def __str__(self):
        return f"{self.name} {self.surname.upper()} ({Student.id}), {self.field}, {Student.university}"


student1 = Student("Anna", "Maj", "Applied Informatics")
print(student1)

student2 = Student("Jon", "Snow", "Warfare")
print(student2)

student3 = Student("Geralt", "of Rivia", "Witcher Studies")
print(student3)
