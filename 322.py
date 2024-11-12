#print a string passed through the function
import re

txt = "the rain in spain"
x =re.search(r"\bS\w+",txt)
print(x.string)