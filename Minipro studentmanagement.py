
# Student Management System
# Operations: Add, View, Update and Delete Students

students = []


# Add Student
def add_student():
    student_id = int(input("Enter student's ID: "))

    # Check for duplicate student ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


# View Students
def view_students():
    if len(students) == 0:
        print("No students found!")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print("-------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])


# Update Student
def update_student():
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = int(input("Enter new age: "))
            student["grade"] = input("Enter new grade: ")

            print("Student updated successfully!")
            return

    print("Student not found!")


# Delete Student
def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# Main Menu
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using our application!")
        break

    else:
        print("Invalid choice! Please try again.")


    
