
class Phonebook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def print_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, phone_number):
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                print(contact)
                self.contacts.remove(contact)

    def print_favorite(self):
        for contact in self.contacts:
            if contact.favorite:
                print(contact)

    def search_contact(self, first, last):
        for contact in self.contacts:
            if contact.first_name == first and contact.last_name == last:
                print(contact)

