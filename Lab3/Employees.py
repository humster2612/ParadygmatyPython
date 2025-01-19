import json

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeesManager:

    def __init__(self, file_path='data.json'):

        self.file_path = file_path
        self.employees = []
        self.load_employees()

    def load_employees(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)

                self.employees = [Employee(emp['name'] , emp ['age'], emp['salary'] ) for emp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print(" Brak danych ")

    def save_employees(self):

        with open(self.file_path, 'w') as file:
            data = [{'name': emp.name, 'age': emp.age, 'salary': emp.salary} for emp in self.employees]
            json.dump(data, file, indent=4)

    def add_employee(self, employee):

        if self.validate_employee(employee):
            self.employees.append(employee)
            self.save_employees()
            print(f"Pracownik {employee.name} został dodany")
        else:
            print("Nieprawidłowe dane pracownika")

    def display_employees(self):
        if not self.employees:
            print("Brak pracownikow")
        for employee in self.employees:
            print(employee)

    def remove_employees_in_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        self.save_employees()
        print(f"Usunieto pracowników w wieku od {min_age} do {max_age}")

    def find_employee_by_name(self, name):
        found = [emp for emp in self.employees if emp.name.lower() == name.lower()]
        if found:
            return found
        else:
            return "Nie znaleziono pracownika o podanym imieniu i nazwisku w liscie"

    def update_salary(self, name, new_salary):

        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.salary = new_salary
                self.save_employees()
                print(f"Wynagrodzenie pracownika {name} zostało zaktualizowane")
                return
        print("Nie znaleziono pracownika o podanym imieniu i nazwisku w liscie")

    def validate_employee(self, employee):

        if not employee.name or not isinstance(employee.name, str):
            return False
        if not isinstance(employee.age, int) or not (18 <= employee.age <= 100):
            return False
        if not isinstance(employee.salary, (int, float)) or employee.salary <= 0:
            return False
        return True
