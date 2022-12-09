from p7 import Message


class Email(Message):

    def __init__(self, sender, recipient, subject):
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject

    def send(self):
        return f"Sending email...\nFrom: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n{self.message}"


email = Email("nowak@onet.pl", "kowalski@gmail.com", "Meeting on Thursday")
email.set_message(
    "I would like to inform you that our Thursday meeting has been canceled.")

print(email.send())
