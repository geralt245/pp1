from contact import Contact


class Contact_List:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"{contact.name}   {contact.email}   {contact.telephone}")
