from db_connector import connection, cursor

def add_equipment():
    pass

def view_equipment():
    pass

def search_equipment():
    pass

def update_status():
    pass

def delete_equipment():
    pass

while True:
    print("\n==== IT Equipment Inventory System ====")
    print("1. Add Equipment")
    print("2. View Equipment")
    print("3. Search Equipment")
    print("4. Update Equipment Status")
    print("5. Delete Equipment")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_equipment()

    elif choice == "2":
        view_equipment()

    elif choice == "3":
        search_equipment()

    elif choice == "4":
        update_status()

    elif choice == "5":
        delete_equipment()

    elif choice == "6":
        break

    else:
        print("Invalid choice.")