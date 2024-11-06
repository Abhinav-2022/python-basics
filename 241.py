#Lamda functions

#function definition to make a function
#that always the number you send in

#function definition
def myfunc(n):
    return lambda a : a * n

# my func takes one argument n
#it returns a lamda function lambda a : a *n
#which is an anonymous (unnamed) function
#this lambda takes one argument a and return the result of a * n

#creating a multiplier :
mydoubler = myfunc(2)

#here myfun(2) is called with n =2
#this return a lambda function equivalent
#lambda a : a * 2 (because n is 2)
#my doubler now holds a reference to this lambda fun
#so mydoubler (a) will double any input
#print output 22


