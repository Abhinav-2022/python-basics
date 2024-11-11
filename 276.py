#Add a year parameter,
# and pass the correct year when creating objects?

class person:
    def __init__(self,fname,lname,year):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
         print(self.firstname,self.lastname)

class student(person):
    def __init__(self,fname,lname,year):
        self.graduationyear = 2019

x = student("mike","olsen",2017)
print(x.graduationyear)