from db_connector import connection, cursor
import os

def clear_screen():
    os.system('cls')

def add_equipment():

    asset_tag = input("Enter asset tag: ")
    device_type = input("Enter device type: ")
    brand = input("Enter brand: ")
    assigned_to = input("Assigned to: ")
    status = input("Enter status: ")
    location = input("Enter location: ")

    query = """
    INSERT INTO equipment
    (asset_tag, device_type, brand, assigned_to, status, location)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        asset_tag,
        device_type,
        brand,
        assigned_to,
        status,
        location
    )

    cursor.execute(query, values)
    connection.commit()

    print("Equipment added successfully.")

    input("\nPress Enter to continue...")
    clear_screen()


def view_equipment():
    query = "SELECT * FROM equipment"

    cursor.execute(query)
    records = cursor.fetchall()

    if not records:
        print("No equipment found.")
    else:
        for row in records:
            print("\n-------------------")
            print(f"ID: {row[0]}")
            print(f"Asset Tag: {row[1]}")
            print(f"Device Type: {row[2]}")
            print(f"Brand: {row[3]}")
            print(f"Assigned To: {row[4]}")
            print(f"Status: {row[5]}")
            print(f"Location: {row[6]}")
    
    input("\nPress Enter to continue...")
    clear_screen()

def search_equipment():
    asset_tag = input("Enter asset tag to search: ")

    query = "SELECT * FROM equipment WHERE asset_tag = %s"

    cursor.execute(query, (asset_tag,))
    record = cursor.fetchone()

    if record:
        print("\nEquipment Found")
        print(f"ID: {record[0]}")
        print(f"Asset Tag: {record[1]}")
        print(f"Device Type: {record[2]}")
        print(f"Brand: {record[3]}")
        print(f"Assigned To: {record[4]}")
        print(f"Status: {record[5]}")
        print(f"Location: {record[6]}")
    else:
        print("No equipment found.")

    input("\nPress Enter to continue...")
    clear_screen()

def update_status():
    equipment_id = input("Enter equipment ID: ")
    new_status = input("Enter new status: ")

    query = """
    UPDATE equipment
    SET status = %s
    WHERE equipment_id = %s
    """

    values = (new_status, equipment_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        print("Status updated successfully.")
    else:
        print("Equipment ID not found.")
    
    input("\nPress Enter to continue...")
    clear_screen()

def delete_equipment():
    equipment_id = input("Enter equipment ID to delete: ")

    query = "DELETE FROM equipment WHERE equipment_id = %s"

    cursor.execute(query, (equipment_id,))
    connection.commit()

    if cursor.rowcount > 0:
        print("Equipment deleted successfully.")
    else:
        print("Equipment ID not found.")
    
    input("\nPress Enter to continue...")
    clear_screen()

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
        print("Exiting system ....")
        break

    else:
        print("Invalid choice.")

cursor.close()
connection.close()