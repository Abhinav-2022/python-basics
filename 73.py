#Without list comprhension

#you will have to write a for statement with a conditional test case

fruits = ["apple" , "banana", "cherry","kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:

         newlist.append(x)
print(newlist)

#using list comprehension


fruits1 = ["apple" , "banana", "cherry","kiwi", "mango"]

newlist1= [x for x in fruits if "a" in x]
 
print(newlist1)
