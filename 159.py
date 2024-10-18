#Add a new item to the original dictionary
#and see that the item list gets updated as well
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1954,
}
x = car.items()
print(x)#before the change

car ["color"] = "red"
print(x)#after the change