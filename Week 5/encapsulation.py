#Code taken from https://www.geeksforgeeks.org/python/encapsulation-in-python/ 

#Public and private items

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
print(emp.__salary) #cannot be accessed outside the class

