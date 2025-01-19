import json
from Employees import Employee, EmployeesManager

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()
        self.is_logged_in = False

    def login(self):
        username = input("podaj login: ")
        password = input("podaj haslo: ")

        if username == "root" and password == "root":
            print("Jest zalogowano ")
            self.is_logged_in = True
        else:
            print("Nieprawidlowy login lub haslo")

    def show_menu(self):
        print("\nWybierz opcje ")
        print("1. dodaj nowego pracownika")
        print("2. wyswietl wszystkich pracowników")
        print("3. usun pracownikow w okreslonym przedziale wiekowym")
        print("4. wyszukaj pracownika wedlug imienia i nazwiska")
        print("5. zaktualizuj wynagrodzenie pracownika")
        print("6. wyloguj się")
        print("7. zakoncz")

    def add_employee(self):
        name = input(" Podaj imie i nazwisko pracownika: ")
        age = int(input("Podaj wiek pracownika: "))
        salary = float(input("Wynagrodzenie pracownika: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def display_employees(self):


        print("\nLista pracownikow:")
        self.manager.display_employees()

    def remove_employees(self):

        min_age = int(input("Minimalny wiek: "))
        max_age = int(input("Maksymalny wiek: "))
        self.manager.remove_employees_in_age_range(min_age, max_age)

    def find_employee(self):
        name = input("Imie i nazwisko pracownika do wyszukania: ")
        found = self.manager.find_employee_by_name(name)
        if isinstance(found, list):
            for employee in found:
                print(employee)
        else:
            print(found)

    def update_salary(self):
        name = input("Imie i nazwisko pracownika: ")
        new_salary = float(input("Nowe wynagrodzenie: "))
        self.manager.update_salary(name, new_salary)

    def logout(self):
        self.is_logged_in = False
        print("Wylogowano")

    def start(self):
        self.login()
        if not self.is_logged_in:
            return
        while True:
            self.show_menu()
            choice = input("Wybor: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.display_employees()
            elif choice == '3':
                self.remove_employees()
            elif choice == '4':
                self.find_employee()
            elif choice == '5':
                self.update_salary()
            elif choice == '6':
                self.logout()
                break
            elif choice == '7':
                print("Zakonczenie programu")
                break
            else:
                print("Nieprawidlowy wybor, sprobuj ponownie")

