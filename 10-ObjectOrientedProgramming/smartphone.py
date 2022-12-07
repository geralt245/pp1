from contact_list import Contact_List
from contact import Contact

list_of_contacts = Contact_List()
list_of_contacts.add_contact(
    Contact("John Brown", "brown@onet.pl", "555234000"))
list_of_contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
list_of_contacts.add_contact(
    Contact("George Small", "smallg@google.pl", "222999100"))
list_of_contacts.add_contact(
    Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

list_of_contacts.display_contacts()
