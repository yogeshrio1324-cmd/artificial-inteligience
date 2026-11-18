# Student-Teacher-Subject Code Database

database = []

# Function to add student details
def add_record():
    student = input("Enter Student Name: ")
    teacher = input("Enter Teacher Name: ")
    sub_code = input("Enter Subject Code: ")

    record = {
        "Student": student,
        "Teacher": teacher,
        "Subject Code": sub_code
    }

    database.append(record)

    print("Record Added Successfully!")


# Function to display records
def display_records():
    print("\nStudent-Teacher-Subject Database")

    if not database:
        print("No Records Found!")
    else:
        for record in database:
            print("Student Name:", record["Student"])
            print("Teacher Name:", record["Teacher"])
            print("Subject Code:", record["Subject Code"])
            print("------------------------")


# Main Program
while True:

    print("\n1. Add Record")
    print("2. Display Records")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == '1':
        add_record()

    elif choice == '2':
        display_records()

    elif choice == '3':
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
