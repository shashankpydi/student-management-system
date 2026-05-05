import json

students = []

# LOAD DATA
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []

# SAVE FUNCTION (must be at top level)
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    student = {
        "name": name,
        "roll": roll,
        "branch": branch
    }

    students.append(student)
    save_data()  # correct place
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("Student List:")
        for i, student in enumerate(students, start=1):
            print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Branch: {student['branch']}")
        print()


def delete_student():
    view_students()
    if len(students) == 0:
        return

    num = int(input("Enter student number to delete: "))

    if 1 <= num <= len(students):
        removed = students.pop(num - 1)
        save_data()  # correct place
        print(removed, "removed successfully!\n")
    else:
        print("Invalid number\n")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")