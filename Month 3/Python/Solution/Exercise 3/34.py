class Student:
    def __init__(self, name, reg_no, roll_no, standard, admission_year):
        self.name = name
        self.reg_no = reg_no
        self.roll_no = roll_no
        self.standard = standard
        self.admission_year = admission_year
        self.marks = []
        self.result = False

        if not name.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        if not reg_no.isalnum():
            raise ValueError("Registration number must be alphanumeric")
        if not roll_no.isnumeric():
            raise ValueError("Roll number must be numeric")
        if not standard.isnumeric():
            raise ValueError("Standard must be numeric")
        if not admission_year.isnumeric():
            raise ValueError("Admission year must be numeric")
    
    def add_marks(self, marks_dict):
        for subject, mark in marks_dict.items():
            if not isinstance(mark, int):
                raise ValueError("Marks must be integers")
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100")
        
        obtained_marks = sum(marks_dict.values())
        if obtained_marks >= 40:
            self.result = "Pass"
        else:
            self.result = "Fail"

        self.marks.append(marks_dict)
    
    def generate_result(self):
        fail = False
        for mark in self.marks:
            for subject, marks in mark.items():
                if marks < 40:
                    fail = True
                    break

        
        if fail:
            final_result = "Fail"
        else:
            final_result = "Pass"
        
        print("*" * 95)
        print("Name:", self.name)
        print("Roll No:", self.roll_no, "\t\t\t\t\t\t\t\t\t  Standard:", self.standard)
        print("*" * 95)
        print("Subject\t\tTotal Marks\t\tPassing Marks\t\tObtained Marks\t\tResult")
        for mark in self.marks:
            for subject, marks in mark.items():
                print(f"{subject}\t\t    100\t\t\t       40\t\t     {marks}\t\t\t {'Pass' if marks >= 40 else 'Fail'}")
        print("*" * 95)
        total_marks = len(self.marks[0].keys()) * 100
        total_passing_marks = len(self.marks[0].keys()) * 40
        total_obtained_marks = sum([marks for mark in self.marks for marks in mark.values()])
        if fail:
            print("Result: --")
        else:
            print(f"TOTAL \t\t    {total_marks} \t\t       {total_passing_marks}\t\t     {total_obtained_marks}")
            print(f"Result: {final_result} \t\t\t\t\t\t\t\t    Percentage: {round((total_obtained_marks / total_marks) * 100, 2)}%")

    def calculate_grade(percentage):
        if percentage < 40:
            return "F"
        elif percentage >= 95:
            return "O+"
        elif percentage >= 90:
            return "O"
        elif percentage >= 85:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 75:
            return "B+"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "E"


try:
    student1 = Student("Jinay", "123ABC", "456", "10", "2022")
    student1.add_marks({"Maths": 85, "Science": 75, "English": 20})
    student1.generate_result()
    total_marks = len(student1.marks[0].keys()) * 100
    total_obtained_marks = sum([marks for mark in student1.marks for marks in mark.values()])
    percentage = (total_obtained_marks / total_marks) * 100
    print("Grade:", Student.calculate_grade(percentage))
except ValueError as e:
    print("Error:", e)