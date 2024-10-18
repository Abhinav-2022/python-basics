#Add a new item to the original dictionary
#and see that the values list gets updated as well

car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : "1954",

}
x = car.values()
print(x)#before the change

car["color"] = "red"
print(x )#after the change 