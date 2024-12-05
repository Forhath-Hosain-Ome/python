import file_handler
import validators

class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def load_contacts(self):
        self.contacts = file_handler.load_from_file()

    def save_contacts(self):
        file_handler.save_to_file(self.contacts)

    def add_contact(self):
        name = input("Enter name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone number: ").strip()
        address = input("Enter address: ").strip()

        if not validators.is_valid_name(name) or not validators.is_valid_phone(phone):
            print("Invalid input. Please try again.")
            return

        if phone in self.contacts:
            print("This phone number is already in use.")
            return

        self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for phone, details in self.contacts.items():
                print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Address: {details['Address']}")

    def remove_contact(self):
        phone = input("Enter phone number of contact to remove: ").strip()
        if phone in self.contacts:
            del self.contacts[phone]
            self.save_contacts()
            print("Contact removed successfully.")
        else:
            print("Contact not found.")

    def search_contact(self):
        query = input("Enter name or phone to search: ").strip()
        results = {k: v for k, v in self.contacts.items() if query.lower() in v["Name"].lower() or query == k}
        if results:
            for phone, details in results.items():
                print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Address: {details['Address']}")
        else:
            print("No matching contacts found.")
