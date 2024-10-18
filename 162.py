#update Dictionary
#the update () method will update the dictionary
#with the item from the given argument

#the argument must be in dictionary
#or an iterable object with key: value pairs
#update the "year" of the car by using the update method

thisdict = {
    "brand" : "ford",
      "model" : "mustang",
    "year" : "1953",

}
thisdict.update({"year":2020})
print(thisdict)