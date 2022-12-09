from p7 import Message


class SMS(Message):

    def __init__(self, sender, recipient):
        super().__init__()
        self.sender = sender
        self.recipient = recipient

    def send(self):
        return f"Sending SMS...\nFrom: {self.sender}\nTo: {self.recipient}\n{self.message}"


sms = SMS("542346", "43626524")
sms.set_message(
    "I would like to inform you that our Thursday meeting has been canceled.")
print(sms.send())
