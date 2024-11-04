#number of arguments
#by default a function must be called with the correct
# number of argument
# meaning that if your function expects 2 arguments
# you have to call the function with 2 argument not more
# and not less
#this function expects 2 arguments and get 2 arguments
from pstats import func_get_function_name


def my_function(fname,lname):
    print(fname + " " + lname)
my_function("Email","thomas")