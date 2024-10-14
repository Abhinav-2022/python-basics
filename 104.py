#append() method
#convert the tuple into a list add "orange",and
#convert it back into a tuple

thislist = ("apple","banana","cherry")
y = list(thislist)
y.append("orange")
thislist = tuple(y)
print(thislist)