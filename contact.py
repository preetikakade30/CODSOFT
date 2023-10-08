class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name}: {contact.phone_number}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword in contact.name or keyword in contact.phone_number:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print(f"{old_name}'s contact information updated.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name}'s contact deleted.")
                return
        print(f"Contact with the name '{name}' not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_manager.view_contact_list()
        elif choice == "3":
            keyword = input("Enter a name or phone number to search: ")
            results = contact_manager.search_contact(keyword)
            if results:
                print("\nSearch Results:")
                for idx, result in enumerate(results, start=1):
                    print(f"{idx}. Name: {result.name}")
                    print(f"   Phone Number: {result.phone_number}")
                    print(f"   Email: {result.email}")
                    print(f"   Address: {result.address}\n")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter the new name: ")
            new_phone_number = input("Enter the new phone number: ")
            new_email = input("Enter the new email: ")
            new_address = input("Enter the new address: ")
            new_contact = Contact(new_name, new_phone_number, new_email, new_address)
            contact_manager.update_contact(name, new_contact)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
