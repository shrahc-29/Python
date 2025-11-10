print("Python Program: Phone Directory\n")

#Initializing the contact dictionary
contacts = {}

#Function to add a contact
def add_contacts():
    try:
        name = input("Enter Name: ")
        phn_num = input("Enter Phone Number: ")
        place = input("Enter Place/City: ")


        #Validating the phone number
        if not phn_num.isdigit():
            print("Invalid input. Phone number must contain digits only.\n")
            return
        if len(phn_num) != 10:
            print("Error: Phone number must contain exactly 10 digits.\n")
            return

        #Saving contact
        contacts[name] = {
            'Phone Number': phn_num,
            'Place/City': place
        }

        print("Contact added successfully.\n")

    except Exception as e:
        print(f"Error while adding contact: {e}")

#Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.\n")
        return

    print("\n*****Phone Directory*****")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone Number: {details['Phone Number']}")
        print(f"Place/City: {details['Place/City']}")

#Function to show menu
def menu():
    while True:
        try:
            print("Phone Directory Menu:")   #Printing choices
            print("1. Add Contact")
            print("2. Display Contacts")
            print("3. Exit")

            choice = int(input("Enter your choice (1, 2 or 3): "))
            print("\n")

            if choice == 1:    #Calling each function acc to the choice
                add_contacts()
            elif choice == 2:
                display_contacts()
                print("\n****\n")
            elif choice == 3:
                print("Exiting Phone Directory.")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.\n")   #Error for invalid choice

        except ValueError:
            print("Invalid input. Please enter a number (1, 2 or 3).\n")
        except Exception as e:
            print(f"An error occurred: {e}")

menu()
