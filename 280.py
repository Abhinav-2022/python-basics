#1-Create a Vehicle cla# make (e.g., "Toyota")
# model (e.g., "Corolla")
# year (e.g., 2020)
# Add an _init_ method to initialize these properties.


#2-Add a display_info method to the Vehicle class that prints
# the vehicle's details in this format
#Vehicle Info: Toyota Corolla, Year: 2020


#3-Create a Car class that inherits from the Vehicle class and has:

#An additional property called fuel_type (e.g., "Gasoline").
#Modify the _init_ method in the Car class
# to accept a fuel_type argument in addition
# to the inherited properties (make, model, and year).


#4-Add a display_info method to the Car class that overrides
# the Vehicle class’s method. It should display the vehicle's details,
# including fuel type, in this format:
#Car Info: Toyota Corolla, Year: 2020, Fuel Type: Gasoline



#5-Create a Truck class that also inherits from Vehicle and has:

# An additional property called payload_capacity (in tons).
# Modify the _init_ method in the Truck class to accept
# a payload_capacity argument in addition to the
# inherited properties (make, model, and year).


#6-Add a display_info method to the Truck class that overrides
# the Vehicle class’s method. It should display the vehicle’s details,
# including payload capacity, in this format:
#Truck Info: Ford F-150, Year: 2019, Payload Capacity: 3 tons


#7-Write code to:

# Create an object of the Car class
# with make "Toyota", model "Corolla", year 2020, and fuel type "Gasoline".

# Create an object of the Truck class with
# make "Ford", model "F-150", year 2019, and payload capacity of 3 tons.

# Call display_info for both objects to verify that
# they display the information in the correct format.


#Expected Output:

# Car Info: Toyota Corolla, Year: 2020, Fuel Type: Gasoline
# Truck Info: Ford F-150, Year: 2019, Payload Capacity: 3tons
#ss with the following properties:
from msilib import make_id



class vechicle():
    def __init__(self,model,year,make):
      self.model = model
      self.make = make
      self.year = year

    def disply_info(self):
        print("vehicle info  " +  self.model,self.year)

v1 = vechicle("corolla",2020,2003)
v1.disply_info()




