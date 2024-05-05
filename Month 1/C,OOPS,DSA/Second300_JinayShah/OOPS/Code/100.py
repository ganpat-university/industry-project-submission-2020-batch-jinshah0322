class Salary:
    def __init__(self, basic_salary, bonuses=0, deductions=0):
        self.basic_salary = basic_salary
        self.bonuses = bonuses
        self.deductions = deductions

    def calculate_total_salary(self):
        return self.basic_salary + self.bonuses - self.deductions


class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def generate_pay_stub(self):
        total_salary = self.salary.calculate_total_salary()
        pay_stub = f"Pay Stub for {self.name}\n"
        pay_stub += f"Employee ID: {self.employee_id}\n"
        pay_stub += f"Basic Salary: ${self.salary.basic_salary}\n"
        pay_stub += f"Bonuses: ${self.salary.bonuses}\n"
        pay_stub += f"Deductions: ${self.salary.deductions}\n"
        pay_stub += f"Total Salary: ${total_salary}\n"
        return pay_stub


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.salary.calculate_total_salary()
        return total_payroll

    def generate_payroll_report(self):
        report = "Payroll Report\n"
        report += "=" * 40 + "\n"
        for employee in self.employees:
            report += f"{employee.name}: ${employee.salary.calculate_total_salary()}\n"
        report += "=" * 40 + "\n"
        report += f"Total Payroll: ${self.calculate_total_payroll()}\n"
        return report


salary1 = Salary(basic_salary=50000, bonuses=5000, deductions=2000)
salary2 = Salary(basic_salary=60000, bonuses=7000, deductions=2500)

employee1 = Employee(employee_id=101, name="Alice", salary=salary1)
employee2 = Employee(employee_id=102, name="Bob", salary=salary2)

payroll = Payroll()
payroll.add_employee(employee1)
payroll.add_employee(employee2)

pay_stub1 = employee1.generate_pay_stub()
pay_stub2 = employee2.generate_pay_stub()

payroll_report = payroll.generate_payroll_report()

print(pay_stub1)
print(pay_stub2)
print(payroll_report)
