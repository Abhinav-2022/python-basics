#using astricsk *

#if the number of variables less than the number of values
#you can add an * to the variable
#and the values will be assingned to the variable as alist

#Assign the rest of the values as a list called a'reda'


fruits = ("apple", "banana","cherry","strawberry","rasberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)



