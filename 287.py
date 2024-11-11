#inheritance class polymorphism
#the child class inherit the vehicle method
#creat a class called vehicle


class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move")

class car(vehicle):
    def move(self):
        print("drive")

class boat(vehicle):
    def move(self):
        print("saile")

class plane(vehicle):
    def move(self):
        print("fly")

car1 = car("ford","mustang")
boat1 = boat("ibize","touring")
plane1 = plane("boeing","742")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()

#child classes inherit the properties and methods drom parent class
#in the example above you can see that the car class is empty
#but it inherit brand ,model,and move() from vehicle








