class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents
    
    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_numberOfStudents(self):
        return self.numberOfStudents
    def set_numberOfStudents(self, new_Studentcount):
        self.numberOfStudents = new_Studentcount

    def __repr__(self):
        return f"{self.level} school named {self.name} with {self.numberOfStudents} students"

print(School("64 vsk", "Middle", 1000))

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "Primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy
    def get_policy(self):
        return self.pickupPolicy
    def __repr__(self):
        return super().__repr__() + f" and with policy {self.pickupPolicy}" 
    
#devious code
PrimarySchool1 = PrimarySchool("64 sakumskola", 500, "IDK")
print(PrimarySchool1)




    

        