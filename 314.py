#The search()function search the string for a match
#and return a match object if there is a match
#if there is more than one match
#only the first occurrence of the match will be returned

import re
txt = "the rain in spain"
x = re.search("\s",txt)
#\s-- retruns a match the string contain a white space character
print("the first white-space character is located in position:",x.start())