  #global variables
  #creat a variables outside of a function
  #use u=it inside and outside  the function
x = "awesome"   #scope for x is global
def myfunc():

   print("python is " + x)
myfunc()
print(x)