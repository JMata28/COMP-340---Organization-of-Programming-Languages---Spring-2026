#Example generated using AI (ChatGPT)

# Base class (OOP)
class Animal:
    def speak(self):
        return "Some generic animal sound"


# Single inheritance
class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Another base class (for multiple inheritance)
class Walker:
    def walk(self):
        return "Walking on land"


# Multiple inheritance
class RobotDog(Dog, Walker):
    def speak(self):
        return "Electronic bark"


# --- Polymorphism in action ---
animals = [Dog(), Cat(), RobotDog()]

for a in animals:
    print(a.speak())  # Same method call, different behavior

# Using multiple inheritance method
r = RobotDog()
print(r.walk())