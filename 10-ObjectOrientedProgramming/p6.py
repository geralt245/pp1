class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        return self.title

    def add_page(self):
        self.pages += 1

    def __str__(self):
        return f"{self.title}, written by {self.author}. Has {self.pages} pages."


class Connection:

    def __init__(self, caller, called, length):
        self.caller = caller
        self.called = called
        self.length = length

    def get_caller(self):
        return self.caller

    def get_called(self):
        return self.called

    def length_to_seconds(self):
        return self.length * 60

    def __str__(self):
        return f"{self.caller} called {self.called}. They talked for {self.length_to_seconds()} seconds."


class Students:

    def __init__(self, group, university):
        self.group = group
        self.university = university
        self.amount = len(self.group)

    def add_student(self, student):
        self.group.append(student)

    def remove_student(self):
        self.group.pop()

    def get_students(self):
        students = ""

        for i in range(0, len(self.group)):
            if i == len(self.group) - 1:
                students += self.group[i] + "."
            else:
                students += self.group[i] + ", "

        return students

    def __str__(self):
        return f"The group consists of {self.amount} students from {self.university}. The students are: {self.get_students()}"
