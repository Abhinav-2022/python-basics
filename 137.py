#the intersection update method
# will also keep only the duplicates
#but it will use the original set insteAD of returning a new set

#keep the item that exist in both set1 , and set2

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set1.intersection_update(set2)
print(set1)