#Remove items
#note : you cannot remove items in a tuple

#tuple are unchangeable so you cannot remove item from it
#but we can use the same workaround as we used for changing

#and adding tuple
#convert the tuple into a list , remove "apple"
#and convert it back into a tuple

thislist = ("apple","banana", "cherry")
y = list(thislist)
y.remove("apple")
thistuple  = tuple(y)
print(thistuple)