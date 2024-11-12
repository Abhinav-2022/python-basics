#match object
#A Match object is an object containing
#information about the search and the result
#if there is no match
#do a search that will return instead  of the match object

import re
txt = "the rain in spain"
x = re.search("ai",txt)
print(x) #this will print an object