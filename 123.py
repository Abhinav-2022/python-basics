#Add any iterable
#the object in the update method does not have to be a set
#it can be any iterable object (tuple,lists,dictonaries etc)

thisset = {"apple","banana","cherry"}
mylist = ["kiwi","orange"]
thisset.update(mylist)
print(thisset)