# Make chages in the original dictionary
#and see the values list gets updated

car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : "1954",


}
x = car.values()
print(x)#before the change

car ["year"] = 2020
print(x)#after the change 