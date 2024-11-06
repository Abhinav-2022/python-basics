# Write a Python function, power_func,
# that takes one argument n and returns a lambda function
# that raises any number passed to it to the power of n.
# In the same program, create both square and cube functions using power_func.
# Test them by squaring the number 5 and cubing the number 3.

def myfun(n):
    return lambda a : a**n
mysquare = myfun(2)
mycube  = myfun(3)
print(mysquare(5))
print(mycube(3))