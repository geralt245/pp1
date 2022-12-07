class University:

    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname

    def display_name(self):
        print(self.name)

    def set_name(self, new_name):
        self.name = new_name

    def display_fullname(self):
        print(self.fullname)

    def set_fullname(self, new_fullname):
        self.fullname = new_fullname


uek = University("UEK", "Uniwersytet Ekonomiczny w Krakowie")
uek.display_name()
uek.display_fullname()
uek.set_name("UJ")
uek.set_fullname("Uniwersytet Jagielloński")
uek.display_name()
uek.display_fullname()
