#Order the Result

# The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter
# to specify if the result should be sorted or not:
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
#sort the result alphabetically by keys
print(json.dumps(x,indent=4,sort_keys=True))