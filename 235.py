#Recursion
#python also accept function recursion
#which means a defined function can call itself

#example

def factorial(x):
    if x ==1:
        return 1
    else:
        return (x * factorial(x-1))     #3*2

num =3
print("the factorial of ", num  ,"is" ,factorial(num))
#factorial of 3 =  1*2*3 =6
# putting it all together 3