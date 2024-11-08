#delete object
#you can delete objects by using the del keyword
#delete p1 object
class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello my name is " + self.name)

p1 = person("jhon",34)
del p1
print(p1)
 
