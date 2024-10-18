#the values of true and 1 are consider the same
#same as goes for false and 0

#join set that contain the  values
#true ,false , 1,and 0, and see what is considered as duplicates
set1 = {"apple",1,"banana",0,"cherry"}
set2 = {"google",1,False,2,True,"apple"}
set3 = set1.intersection(set2)
print(set3)