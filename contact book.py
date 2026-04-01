contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. search Contact")
    print("4. delete Contact")
    print("5. Exit")

    choice = input("choose an option (1-5): ")
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts.append({'name': name, 'phone': phone})
        print("Contact added successfully!")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == '3':
        search_name = input("Enter the name to search: ")
        found = False
        for contact in contacts:
            if contact['name'].lower() == search_name.lower():
                print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == '4':
        delete_name = input("Enter the name to delete: ")
        found = False
        for contact in contacts:
            if contact['name'].lower() == delete_name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "5":
        print("Exit")