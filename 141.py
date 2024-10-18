##the difference_update method will also keep items
#from the first set that are not in other set
#but it will change the original  set instead of returning a new set

#use the difference _ update() mthod to keep the item
#that are not present in both sets

set1 = {"apple", "banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.difference_update(set2)
print(set1)