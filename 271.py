# Create a class named Vehicle,
# with brand and year properties, and a print_info method:
# Use the Vehicle class to create an object,
# and then execute the print_info method:
# Create a class named Car,
# which will inherit the properties and methods from the Vehicle class:

# class vehicle :
#     def _init_(self,model,year):
#         self.model = model
#         self.year = year
#
#     def disp(self):
#         print(f"{self.model}\n{self.year}")
#
# class car(vehicle):
#     pass
#
# x = car("BMW M3 sport",2004)
# x.disp()
# x.year =2006
# x.disp()
# Create a class named Vehicle,
# with brand and year properties, and a print_info method:
# Use the Vehicle class to create an object,
# # and then execute the print_info method:
# Create a class named Car,
# which will inherit the properties and methods from the Vehicle class
class vehicle:
    def _init_(self,brand,year):
        self.brand = brand
        self.year = year

    def vehicle1(self):
        print(f"{self.brand},manufactured in {self.year}")

v1 = vehicle("bmw",2021)
v1.vehicle1()

class car(vehicle):
    pass
v2 = car("benz",2022)
v2.vehicle1()