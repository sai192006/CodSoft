class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("----- Add New Contact -----")
        name = input("Name: ").strip()
        phone = input("Phone Number: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        
        if name and phone:
            self.contacts.append({
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            })
            print(f"Contact for '{name}' added successfully.")
        else:
            print("Name and Phone Number are mandatory fields.")

    def view_contacts(self):
        print("----- Contact List -----")
        if not self.contacts:
            print("No contacts stored yet.")
            return
            
        for idx, c in enumerate(self.contacts, 1):
            print(f"{idx}. Name: {c['name']} | Phone: {c['phone']}")

    def search_contact(self):
        print("----- Search Contact -----")
        query = input("Enter name or phone number to search: ").strip().lower()
        found = False
        
        for c in self.contacts:
            if query in c['name'].lower() or query in c['phone']:
                print(f"\nFound match:")
                print(f"Name: {c['name']}")
                print(f"Phone: {c['phone']}")
                print(f"Email: {c['email']}")
                print(f"Address: {c['address']}")
                found = True
                
        if not found:
            print("No matching contact found.")

    def update_contact(self):
        print("----- Update Contact -----")
        name_to_find = input("Enter the precise name of the contact to update: ").strip().lower()
        
        for c in self.contacts:
            if c['name'].lower() == name_to_find:
                print("Leave blank to retain current information.")
                new_phone = input(f"New Phone [{c['phone']}]: ").strip()
                new_email = input(f"New Email [{c['email']}]: ").strip()
                new_address = input(f"New Address [{c['address']}]: ").strip()
                
                if new_phone: 
                    c['phone'] = new_phone
                if new_email: 
                    c['email'] = new_email
                if new_address: 
                    c['address'] = new_address
                    
                print("Contact information updated!")
                return
                
        print("Contact name not found.")

    def delete_contact(self):
        print("----- Delete Contact -----")
        name_to_find = input("Enter the precise name of the contact to delete: ").strip().lower()
        
        for idx, c in enumerate(self.contacts):
            if c['name'].lower() == name_to_find:
                removed = self.contacts.pop(idx)
                print(f"Deleted contact for '{removed['name']}'.")
                return
                
        print("Contact name not found.")


def main():
    book = ContactBook()
    
    while True:
        print("*_*_*_*_* Contact Book *_*_*_*_*")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1': 
            book.add_contact()
        elif choice == '2': 
            book.view_contacts()
        elif choice == '3': 
            book.search_contact()
        elif choice == '4': 
            book.update_contact()
        elif choice == '5': 
            book.delete_contact()
        elif choice == '6':
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice, please select valid option.")


if __name__ == "__main__":
    main()