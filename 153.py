#Add a new item to the original dictionary
# and see that keys gets updated as well

car = {
    "brand": "ford",
    "model" : "mustang",
    "year" : "6358"


}
x = car.keys()
print(x)#before the change

car ["color"] = "white"
print(x)#after the change 
