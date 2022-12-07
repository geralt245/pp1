import random


class Thermometer:

    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure(self):
        if self.is_on == True:
            self.temperature = round(random.uniform(34, 43), 1)

    def display_temp(self):
        if self.is_on == False:
            return "Thermometer is off"

        if self.temperature > 41.0:
            return f"Temperature: {self.temperature} (fever)\nCRITICAL TEMPERATURE!!"
        elif self.temperature > 37.0:
            return f"Temperature: {self.temperature} (fever)"
        else:
            return f"Temperature: {self.temperature}"
