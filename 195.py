#Nested if
#if statement inside if statement
# this is called nested if statement

x = 43
if x > 10:
    print("10")
    if x > 20 :
        print("and also above 20 ")
    else:
        print("but not also above 20")
else :
    print("less than 10 ")