# Add a salary parameter,
# and pass the correct salary when creating objects.
# Use the Employee class to create an object with the specified salary,
# and then print the salary property:
class person:
    def __init__(self,fname,lname,year):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
         print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,salary):
        self.salary = salary

x = student("mike","olsen",1000000)
print(x.salary)