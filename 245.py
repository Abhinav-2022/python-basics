#function definition to make both functions (double ,triple)
#in the same programe

def myfun(n):
    return lambda a : a * n
mydoubler = myfun(2)
mytriple = myfun(3)
print(mydoubler(5))
print(mytriple(4))