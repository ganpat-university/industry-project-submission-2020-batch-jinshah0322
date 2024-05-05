class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def promote(self):
        print(f"{self.name} has been promoted.")

class Manager(Employee):
    def __init__(self, employee_id, name, role, salary, team=None):
        super().__init__(employee_id, name, role, salary)
        self.team = team or []

    def add_employee(self, employee):
        self.team.append(employee)
        print(f"{employee.name} has been added to {self.name}'s team.")

    def remove_employee(self, employee):
        if employee in self.team:
            self.team.remove(employee)
            print(f"{employee.name} has been removed from {self.name}'s team.")
        else:
            print(f"{employee.name} is not in {self.name}'s team.")

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = len(self.team) * 1000  # Bonus for each team member
        total_salary = base_salary + bonus
        return total_salary

class Department:
    def __init__(self, name, manager=None):
        self.name = name
        self.manager = manager
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added to the {self.name} department.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.name} has been removed from the {self.name} department.")
        else:
            print(f"{employee.name} is not in the {self.name} department.")

    def set_manager(self, manager):
        self.manager = manager
        print(f"{manager.name} is now the manager of the {self.name} department.")

employee1 = Employee(1, "Alice", "Developer", 50000)
employee2 = Employee(2, "Bob", "Designer", 45000)

manager = Manager(3, "Charlie", "Manager", 60000)

department = Department("Engineering")
department.set_manager(manager)

department.add_employee(employee1)
department.add_employee(employee2)

manager.add_employee(employee1)
manager.add_employee(employee2)

print(f"{employee1.name}'s salary: ${employee1.calculate_salary()}")
print(f"{employee2.name}'s salary: ${employee2.calculate_salary()}")
print(f"{manager.name}'s salary: ${manager.calculate_salary()}")