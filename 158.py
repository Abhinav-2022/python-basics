#Make changes in the original dictionary
#and see that the items list get updated as well
car = {
    "brand" : "ford",
    "model" : "mustang",
    "year" : 1954,
}
x = car.items()
print(x)#before change

car["year"] = 2020
print(x)#after the change