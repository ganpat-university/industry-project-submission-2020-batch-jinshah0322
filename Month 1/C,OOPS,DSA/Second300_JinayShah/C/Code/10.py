class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print("Student added successfully.")

def display_students(students):
    if not students:
        print("No students available.")
    else:
        for student in students:
            print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")


students = []

while True:
    print("\nStudent Information System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_students(students)
    elif choice == '3':
        print("Exiting the Student Information System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")