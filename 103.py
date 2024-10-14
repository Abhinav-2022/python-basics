#update tuple

#change tuple values
#once a tuple created you cannot change its values
#tuple are unchangeable or immutable it also is called
#you can convert the tuple into list
#change the list and convert the list back into a tuple

#convert the tuple into a list to be able to change it

x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)