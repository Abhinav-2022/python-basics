#function definition to make a function
# that always triples the number you send in?
def myfun(n):
    return lambda : a * n
mytriple = myfun(3)
print(mytriple(6))