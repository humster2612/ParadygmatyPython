import json
from Employees import Employee, EmployeesManager

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()
        self.is_logged_in = False

