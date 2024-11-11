#classs polymorphism
#polymorphisam is often used in class method
#where we can have multiple classes with the same method name
#different classes with the same method
class car:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def move(self):
       print("drive")


class boat:
    def __init__(self, name, type):
        self.name = name
        self.type = type


    def move(self):
        print("saile")

class plane:
    def __init__(self, name, type):
            self.name = name
            self.type = type

    def move(self):
        print("fly")

car1 = car ("ford","mustang")
boat1 = boat("ibiz","touring20")
plane1 = plane("boeing","987")

for x in (car1,boat1,plane1):
    x.move()
#we have three classes:car,boat,and plane
#and they all have method called move():