#you can control the number of replacement
#by specifying the count parameter
#replace the first 2 occurrence
import re
txt = "the rain in spain"
x = re.subn("\s","9",2)
print(x)