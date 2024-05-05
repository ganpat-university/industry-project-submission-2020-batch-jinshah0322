class Course:
    def __init__(self, course_id, title, instructor):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.students = []
        self.assignments = []

    def add_student(self, student):
        self.students.append(student)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_assignments(self):
        return self.assignments


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = {}

    def enroll(self, course):
        if course.course_id not in self.courses_enrolled:
            self.courses_enrolled[course.course_id] = {'course': course, 'assignments_completed': set()}

    def complete_assignment(self, course, assignment):
        if course.course_id in self.courses_enrolled:
            self.courses_enrolled[course.course_id]['assignments_completed'].add(assignment)

    def get_progress(self):
        progress = {}
        for course_id, course_info in self.courses_enrolled.items():
            total_assignments = len(course_info['course'].get_assignments())
            completed_assignments = len(course_info['assignments_completed'])
            progress[course_id] = {'completed': completed_assignments, 'total': total_assignments}
        return progress


class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name

    def create_course(self, course_id, title):
        return Course(course_id, title, self)

    def grade_assignment(self, student, course, assignment):
        if course.course_id in student.courses_enrolled:
            student.complete_assignment(course, assignment)


instructor = Instructor(1, "Karan thakor")

course = instructor.create_course(101, "Introduction to Python")

student1 = Student(1001, "Simha")
student2 = Student(1002, "Sooryavanshi")

student1.enroll(course)
student2.enroll(course)

assignment1 = "Assignment 1"
assignment2 = "Assignment 2"
course.add_assignment(assignment1)
course.add_assignment(assignment2)

student1.complete_assignment(course, assignment1)
student2.complete_assignment(course, assignment2)

instructor.grade_assignment(student1, course, assignment1)
instructor.grade_assignment(student2, course, assignment2)

print("Student 1 Progress:", student1.get_progress())
print("Student 2 Progress:", student2.get_progress())
