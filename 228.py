#Default Parameter Value

#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
def my_function (country = "norway "):
    print("iam from " + country)

my_function("sweden")
my_function("india")
my_function()
my_function("brazil")