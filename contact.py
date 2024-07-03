import sys
contacts = []

# Function to add a contact to the list
def add_contact(name, phone):
    contacts.append((name, phone))
    print("Contact added successfully.")

# Function to delete a contact from the list
def delete_contact(index):
    try:
        del contacts[index]
        print("Contact deleted successfully.")
    except IndexError:
        print("No contact found at the specified index.")

# Function to clear all contacts from the list
def clear_contacts():
    contacts.clear()
    print("All contacts cleared.")

# Function to display all contacts
def display_contacts():
    if contacts:
        for index, (name, phone) in enumerate(contacts):
            print(f"{index + 1}. {name} - {phone}")
    else:
        print("No contacts found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Clear Contacts")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            index = int(input("Enter index of contact to delete: ")) - 1
            delete_contact(index)
        elif choice == "3":
            clear_contacts()
        elif choice == "4":
            display_contacts()
        elif choice == "5":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()