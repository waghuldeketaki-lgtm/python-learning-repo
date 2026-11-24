
students = []

def add_students():
    student_id = int(input("Enter student ID: "))
    name = input("Enter student's name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!")

# Add student
add_students()

# Display student list
print("\nStudent Details:")
print(students)


    