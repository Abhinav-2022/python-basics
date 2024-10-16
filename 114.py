#using a while loop
#you can loop through the tuple item by using while loop

#use the len() to determine the length of tuple
#then start at 0 and loop your way through the tuple items by
#reffering to their indexes

#remember to increase the index 1  after each iteration
#print all item using a while loop to go through all index numbers

thistuple = ("apple","banan", "cherry")
i = 0
while i < len (thistuple):
    print(thistuple[i])
    i = i+1
