#python iterators
#An iterator is an object that contain a countable numbers of values
#An iterator is an object which contain of the methods
#__iter__()and __next__()
#return an iterator from a tuple and print each value
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))