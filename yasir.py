import abc


class Department(abc.ABC):
    def __init__(self, name):
        self.name = name
    
    @abc.abstractmethod
    def get_description(self):
        pass

class Accountancy(Department):
    def get_description(self):
        return "Accountancy Department"

class HumanResources(Department):
    def get_description(self):
        return "Human Resources Department"
        
class Room(abc.ABC):
    def __init__(self, number, department):
        self.number = number
        self.department = department
    
    @abc.abstractmethod
    def get_description(self):
        pass

class Office(Room):
    def __init__(self, number, department, employee_count):
        super().__init__(number, department)
        self.employee_count = employee_count
    
    def get_description(self):
        return f"Office {self.number} in {self.department.get_description()} with {self.employee_count} employees."

class ConferenceRoom(Room):
    def __init__(self, number, department, capacity):
        super().__init__(number, department)
        self.capacity = capacity
    
    def get_description(self):
        return f"Conference room {self.number} in {self.department.get_description()} with capacity for {self.capacity} people."

# example usage
acct_dept = Accountancy('Accounting')
hr_dept = HumanResources('HR')

office_1 = Office(101, acct_dept, 4)
office_2 = Office(201, hr_dept, 6)
conf_1 = ConferenceRoom(301, hr_dept, 16)

print(office_1.get_description())  # Office 101 in Accounting Department with 4 employees.
print(office_2.get_description())  # Office 201 in Human Resources Department with 6 employees.
print(conf_1.get_description()) 
