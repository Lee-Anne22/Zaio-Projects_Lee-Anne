class Car:
    def __init__(self, make, model):
        self.make=make
        self.model=model
    def drive(self):
        return f"{self.make} {self.model} is driving."
# Object Obstantiation
my_car=Car("Toyota", "Corolla")
print(my_car.drive()) # Output: Toyota Corolla is driving.

#class Student: