from collections import deque


class Chore:
    def __init__(self, name, duration, preferred_member=None):
        self.name = name
        self.duration = duration
        self.preferred_member = preferred_member  
        self.assigned_member = None  



    def assign_to(self, member):

        self.assigned_member = member
        print(f"Zadanie '{self.name}' przypisane do {member.name}.")




class FamilyMember:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability  
        self.assigned_chores = []  

    def is_available(self, chore):

        for time_slot in self.availability:
            if time_slot >= chore.duration:
                return True
        return False

class TaskScheduler:
    
    def __init__(self):
        self.tasks = deque()  
        self.members = []  

    def add_member(self, member):
        self.members.append(member)

    def add_task(self, chore):
        self.tasks.append(chore)

    def assign_tasks(self):
        while self.tasks:
            chore = self.tasks.popleft() 
            assigned = False

            for member in self.members:
                if member.is_available(chore):  
                    chore.assign_to(member)
                    member.assigned_chores.append(chore)
                    assigned = True
                    break

            if not assigned:
                print(f"Nie udało się przypisać zadania '{chore.name}'.")


family_members = [
    FamilyMember("Anna", [2, 4, 5]),  
    FamilyMember("Jan", [3, 6, 7]),   
]

chores = [
    Chore("Sprzątanie", 2), 
    Chore("Gotowanie", 4),   
    Chore("Zakupy", 6),     
]


scheduler = TaskScheduler()


for member in family_members:
    scheduler.add_member(member)


for chore in chores:
    scheduler.add_task(chore)


scheduler.assign_tasks()
