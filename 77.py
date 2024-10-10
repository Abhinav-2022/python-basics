#return the orange instead of banana

fruits = ["apple","banana", "cherry", "kiwi", "mnago"]

newlist = [x if x !="banana" else "orange" for x in fruits]

print(newlist)