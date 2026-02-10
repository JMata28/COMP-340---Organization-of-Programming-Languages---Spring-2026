# Classes
# The __init__() method
class Student:
    tuition = 5000
    def __init__(self, first, last, GPA, address):
        self.first = first
        self.last = last
        self.GPA = GPA
        self.address_of_student = address
    def name(self):
        print(f"The name of this student is: {self.first} {self.last}. has a GPA of {self.GPA} and their address is {self.address_of_student}")

student_1 = Student("John", "Johnson", 3, "Bridgewater, MA")
# student_1.name()
print(student_1.tuition)
student_2 = Student("Tyler", "Parker", 4, "Boston. MA")
# student_2.name()
student_2.tuition = 3000
print(student_2.tuition)
print(student_1.tuition)