# ----------------------------------------------
# Name: Khushi Panwar
# Roll No. : 2501940062
# Date: 14-Nov-2025
# Project: Contact Book Manager
# ----------------------------------------------

# ---------------------------------------------------------
# Name: Khushi Panwar
# Date: November 2025
# Project: Contact Book Manager
# ---------------------------------------------------------

import csv
import json
import datetime

print("Welcome to the Contact Book Manager!")
print("This program allows you to add, view, update, and delete contacts easily.\n")

# ---------- TASK 6: ERROR LOGGING ----------
def log_error(error_message, operation):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("error_log.txt", "a") as log:
            log.write(f"[{timestamp}] - Operation: {operation} - Error: {error_message}\n")
    except:
        print("Critical Error: Unable to write to log file!")


# ---------- TASK 2: ADD CONTACT ----------
def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")

        contact = {"name": name, "phone": phone, "email": email}

        with open("contacts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([contact["name"], contact["phone"], contact["email"]])

        print("Contact saved successfully!\n")

    except Exception as e:
        print("Error saving contact!")
        log_error(str(e), "Add Contact")


# ---------- TASK 3: VIEW CONTACTS ----------
def view_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        if not contacts:
            print("No contacts found.\n")
            return

        print("\n--------------------------------------------")
        print(f"{'Name':15}\t{'Phone Number':15}\t{'Email Address'}")
        print("--------------------------------------------")

        for c in contacts:
            print(f"{c[0]:15}\t{c[1]:15}\t{c[2]}")

        print()

    except FileNotFoundError:
        print("Error: contacts.csv not found!")
        log_error("File Missing", "View Contacts")

    except Exception as e:
        print("Unexpected error!")
        log_error(str(e), "View Contacts")


# ---------- TASK 4: SEARCH CONTACT ----------
def search_contact():
    try:
        name = input("Enter name to search: ").strip()

        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        for c in contacts:
            if c[0].lower() == name.lower():
                print("\nContact Found:")
                print(f"Name  : {c[0]}")
                print(f"Phone : {c[1]}")
                print(f"Email : {c[2]}\n")
                return

        print("No contact found with that name.\n")

    except Exception as e:
        print("Error searching contact!")
        log_error(str(e), "Search Contact")


# ---------- TASK 4: UPDATE CONTACT ----------
def update_contact():
    try:
        name = input("Enter the name of the contact to update: ").strip()

        with open("contacts.csv", "r") as file:
            contacts = list(csv.reader(file))

        updated = False
        for c in contacts:
            if c[0].lower() == name.lower():

                print("\nWhat do you want to update?")
                print("1. Phone Number")
                print("2. Email Address")
                choice = input("Enter option: ")

                if choice == "1":
                    c[1] = input("Enter new phone: ")
                elif choice == "2":
                    c[2] = input("Enter new email: ")
                else:
                    print("Invalid choice!")
                    return

                updated = True
                break

        if updated:
            with open("contacts.csv", "w", newline="") as file:
                csv.writer(file).writerows(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Contact not found.\n")

    except Exception as e:
        print("Error updating contact!")
        log_error(str(e), "Update Contact")


# ---------- TASK 4: DELETE CONTACT ----------
def delete_contact():
    try:
        name = input("Enter name to delete: ").strip()

        with open("contacts.csv", "r") as file:
            contacts = list(csv.reader(file))

        new_list = [c for c in contacts if c[0].lower() != name.lower()]

        if len(new_list) == len(contacts):
            print("Contact not found.\n")
            return

        with open("contacts.csv", "w", newline="") as file:
            csv.writer(file).writerows(new_list)

        print("Contact deleted successfully!\n")

    except Exception as e:
        print("Error deleting contact!")
        log_error(str(e), "Delete Contact")


# ---------- TASK 5: EXPORT CSV → JSON ----------
def export_to_json():
    try:
        with open("contacts.csv", "r") as file:
            contacts = list(csv.reader(file))

        data = [
            {"name": c[0], "phone": c[1], "email": c[2]}
            for c in contacts
        ]

        with open("contacts.json", "w") as jf:
            json.dump(data, jf, indent=4)

        print("Exported to contacts.json successfully!\n")

    except Exception as e:
        print("Error exporting JSON!")
        log_error(str(e), "Export JSON")


# ---------- TASK 5: LOAD JSON ----------
def load_from_json():
    try:
        with open("contacts.json", "r") as jf:
            contacts = json.load(jf)

        print("\nContacts Loaded from JSON:")
        print("----------------------------------------")
        for c in contacts:
            print(f"Name  : {c['name']}")
            print(f"Phone : {c['phone']}")
            print(f"Email : {c['email']}")
            print("----------------------------------------")
        print()

    except Exception as e:
        print("Error loading JSON!")
        log_error(str(e), "Load JSON")


# ---------- MENU ----------
def menu():
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Load from JSON")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": add_contact()
        elif choice == "2": view_contacts()
        elif choice == "3": search_contact()
        elif choice == "4": update_contact()
        elif choice == "5": delete_contact()
        elif choice == "6": export_to_json()
        elif choice == "7": load_from_json()
        elif choice == "8": break
        else:
            print("Invalid choice, try again!\n")


# Run menu
menu()
