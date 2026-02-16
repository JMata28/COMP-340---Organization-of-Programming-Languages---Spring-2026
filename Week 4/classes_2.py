class Car:
    number_of_tires = 4

    def __init__(self, color, make):
        self.color_of_car = color #instance attribute
        self.make_of_Car = make

car_1 = Car("red", "Toyota")
print(car_1.make_of_Car)
print(car_1.number_of_tires)

car_2 = Car("black", "Nissan")
print(car_2.color_of_car)
car_2.number_of_tires = 3
print(f"Oh no, the Nissan has {car_2.number_of_tires} tires!")