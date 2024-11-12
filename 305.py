#convert python to json
#if you have a python object
#you can convert it into a json string by
#using the jason.dumps() methods
#convert from python to jason
import json
#a python objects (dict):
x = {
    "name": "jhon",
    "age": 30,
    "city":"new york"


}
#convert into json
y = json.dumps(x)
#the result is a json string
print(y)
