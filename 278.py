#1- Create a Person class with firstname and lastname properties.

# Add an _init_ method to initialize these properties.
# Add a printname method to print the full name.

#2- Create a Student class that inherits from the Person class.
# Add a property called graduationyear to the Student class,
# with a default value of 2025.
# Modify the Student class so that you can pass
# a specific graduation year when creating an object.

#3- Write code to:

# Create an object of the Student class,
# using the name "Anna Smith" and a graduation year of 2023.
# Print the graduation year.
class person:
    def __init__(self,fname,lname,year):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
         print(self.firstname,self.lastname)

class employe(person):
    def __init__(self,fname,lname,salary):
        self.salary = 1000000
        self.graduationyear = 2003

x = employe("mike","jhon",100000)
print(x.salary)