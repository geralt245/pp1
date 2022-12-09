class Message():

    def __init__(self):
        self.message = ""

    def set_message(self, message):
        new_message = ""
        for i in range(0, len(message)):
            if i == 0:
                new_message += message[i].upper()
            else:
                new_message += message[i].lower()

        new_message += " BYE."
        self.message = new_message
