#A language with duck typing doesn’t care what type an object is
# It only cares whether the object supports the required operations
#In the example below, both work because both objects have a quack() method.

def make_sound(animal):
    animal.quack()

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

make_sound(Duck())
make_sound(Person())

