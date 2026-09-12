# Composition in Python OOP

# Composition is an OOP relationship where one class contains an object of another class and uses that object to perform its work.

# The simple idea is:

# Composition = "has-a" relationship
# 2. Why Is It Called "Has-A"?
#     -------  Because one object has another object.




class Engine:

    def start(self):
        print("Engine started")


class Wheel:

    def rotate(self):
        print("Wheel rotating")


class Car:

    def __init__(self):
        # 
        self.engine = Engine()
        self.wheel = Wheel()

    def drive(self):
        self.engine.start()
        self.wheel.rotate()
        print("Car is driving")


car = Car()

car.drive()