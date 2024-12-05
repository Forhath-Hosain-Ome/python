from contacts import ContactsManager

def display_menu():
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

def main():
    manager = ContactsManager()
    manager.load_contacts()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.remove_contact()
        elif choice == "4":
            manager.search_contact()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
