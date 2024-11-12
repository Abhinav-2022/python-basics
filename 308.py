#You can also define the separators,

# default value is (", "     ": "),

# which means using a comma and a space to separate each object,
# and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator ?
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
print(json.dumps(x,indent=4,separators=(".","=")))