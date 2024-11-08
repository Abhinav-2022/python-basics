# Create a class named Car.
# Use the __init__() function
# to assign values for make, model, and year.
class car():
    def __init__(self,make,model,year):
        self.model = model
        self.year=year
        self.make = make

car1 = car("toyota","bmw",2000)
print(car1.make)
print(car1.model)
print(car1.year)
