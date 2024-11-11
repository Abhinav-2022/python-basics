class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
         print(self.firstname,self.lastname)



    class employee(person):
        def __init__(self, fname, lname):
            self.position = "softwarengineer "


e1 = employee()

