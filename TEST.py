class Student:

    def __init__(self, name, section, building, department, room, oop, stat):
        self.name = name
        self.section = section
        self.building = building
        self.department = department
        self.room = room
        self.oop = oop
        self.stat = stat

yasir = Student("YASIR", "E2", "OLD Engineering", "Software Engineering", "1.55", "2:30", "3:45")
ahmad = Student("AHMAD", "M1", "OLD Engineering", "Computer Science", "2.15", "9:30", "10:45")

print(yasir.name, yasir.department, ahmad.room, yasir.oop)
