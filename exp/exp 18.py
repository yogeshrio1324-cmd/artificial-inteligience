# Database with Name and DOB

database = []

# Function to add records
def add_record():
    name = input("Enter Name: ")
    dob = input("Enter Date of Birth (DD-MM-YYYY): ")

    record = {
        "Name": name,
        "DOB": dob
    }

    database.append(record)
    print("Record Added Successfully!")


# Function to display records
def display_records():
    print("\nDatabase Records:")

    if not database:
        print("No records found!")
    else:
        for record in database:
            print("Name:", record["Name"])
            print("DOB:", record["DOB"])
            print("-------------------")


# Main Program
while True:
    print("\n1. Add Record")
    print("2. Display Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_record()

    elif choice == '2':
        display_records()

    elif choice == '3':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
