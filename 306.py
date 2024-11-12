#convert a python object containing all the legal data types
import json
x = {
    "name":"jhon",
    "age":50,
    "married":False,
    "divorce":False,
    "childern":("Ann","billy"),
    "pets":None,
    "cars":[{"model":"bmw630","mpg":24.5},
{"model":"ford","mpg":"34.5"}]



}
print(json.dumps(x))