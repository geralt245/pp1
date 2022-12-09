class Phone:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def change_year(self, new_year):
        self.year = new_year

    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear of release: {self.year}"


lgk52 = Phone("LG", "K52", "2015")
print(lgk52)
nokia3310 = Phone("Nokia", "3310", "2000")
print(nokia3310)
