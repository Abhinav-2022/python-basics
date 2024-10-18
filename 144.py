#the symmetric_differnce update() method
#will also keep all but the duplicates
#but it will change the original set instead of returning a new set

#use the symmetric_update() method to
#keep the items that are not present in both set
set1 = {"apple", "banana","cherry"}
set2 = {"google","microsoft","apple"}
set1.symmetric_difference(set2)
print(set1)
