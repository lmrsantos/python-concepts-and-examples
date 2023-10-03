class Vehicle():
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type):
        super().__init__(type)

    def move(self):
        print ("Move")

class Airplane(Vehicle):
    def __init__(self, type):
        super().__init__(type)

    def move(self):
        print ("Fly")

class Boat(Vehicle):
    def __init__(self, type):
        super().__init__(type)
    
    def move(self):
        print ("Sail")

car1 = Car("Truck")
plane1 = Airplane("737")
boat1 = Boat("Titanic")

for v in (car1, plane1, boat1):
    print (v.type)
    v.move()




