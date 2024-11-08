#delete object properties
#you can delete properties on object by using the del keyword
#delete the age property from the p1 object

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)

p1 = person("jhon",34)
del p1.age
print(p1.age)